#!/usr/bin/env python3
"""Hilfsskript für die zwei Cursor-Agenten.

Der Zuordnungs-Agent schreibt nur Quellenzeilen (link).
Der Ergänzungs-Agent hängt nur neue Stichpunkte an (add).
Keine der beiden Rollen schreibt eine Begriffsnotiz im Ganzen neu.

Aufrufe:
  python3 apply_update.py link zuordnungen.json
  python3 apply_update.py add ergaenzungen.json
  python3 apply_update.py pending
  python3 apply_update.py self-test
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

SECTIONS = (
    "Kurzdefinition",
    "Kernaussagen",
    "Funktionsweise",
    "Voraussetzungen",
    "Anwendung im Trading",
    "Regeln und Kriterien",
    "Risiken und Grenzen",
    "Beispiele",
    "Unterschiedliche Quellenpositionen",
    "Quellen und Fundstellen",
    "Verwandte Themen",
)
FORBIDDEN_SECTIONS = frozenset({"Eigene Erkenntnisse"})
LOCKED_STATUS = frozenset({"geprüft", "archiviert"})
MAX_BULLET_CHARS = 800
PAGE_DASH = "–"


@dataclass(frozen=True)
class Roots:
    vault: Path
    trading: Path
    notes: Path
    blocks: Path
    register: Path
    ledger: Path


def default_roots() -> Roots:
    trading = Path(__file__).resolve().parents[2]
    return Roots(
        vault=trading.parent,
        trading=trading,
        notes=trading / "Notes",
        blocks=trading / "Pilot" / "blocks",
        register=trading / "System" / "Automation" / "concept-links.json",
        ledger=trading / "Pilot" / "data" / "ledger.jsonl",
    )


def today() -> str:
    return datetime.now(ZoneInfo("Europe/Berlin")).date().isoformat()


def load_records(path: Path) -> list[dict]:
    raw = path.read_text(encoding="utf-8").strip()
    if not raw:
        return []
    if raw.startswith("["):
        data = json.loads(raw)
        if not isinstance(data, list):
            raise ValueError(f"{path}: Liste erwartet")
        return data
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        data = None
    if isinstance(data, dict):
        return [data]
    records = []
    for line in raw.splitlines():
        line = line.strip()
        if line:
            records.append(json.loads(line))
    return records


def load_register(path: Path) -> dict[str, dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    found: dict[str, dict] = {}
    for row in data.get("konzepte", []):
        if row.get("zieltyp") != "wissensnotiz":
            continue
        name = str(row.get("begriff") or "").strip()
        if not name:
            continue
        current = found.get(name)
        if current is None or (row.get("primaer") and not current.get("primaer")):
            found[name] = row
    return found


def vault_rel(roots: Roots, path: Path) -> str:
    return path.resolve().relative_to(roots.vault.resolve()).as_posix()


def resolve_fragment(roots: Roots, raw: str) -> Path:
    given = Path(raw)
    candidates = []
    if given.is_absolute():
        candidates.append(given)
    else:
        candidates.extend(
            [
                Path.cwd() / given,
                roots.vault / given,
                roots.trading / given,
                roots.blocks / given,
            ]
        )
    blocks = roots.blocks.resolve()
    for candidate in candidates:
        if not candidate.is_file():
            continue
        resolved = candidate.resolve()
        if blocks in resolved.parents or resolved.parent == blocks:
            return resolved
        try:
            resolved.relative_to(blocks)
        except ValueError:
            continue
        return resolved
    raise FileNotFoundError(raw)


def note_path(roots: Roots, row: dict) -> Path:
    target = roots.vault / str(row["zielpfad"])
    resolved = target.resolve()
    resolved.relative_to(roots.notes.resolve())
    if not resolved.is_file():
        raise FileNotFoundError(row["zielpfad"])
    return resolved


def split_document(text: str) -> tuple[list[str], list[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("Frontmatter fehlt")
    end = None
    for index in range(1, min(len(lines), 40)):
        if lines[index].strip() == "---":
            end = index
            break
    if end is None:
        raise ValueError("Frontmatter nicht geschlossen")
    return lines[: end + 1], lines[end + 1 :]


def field_value(lines: list[str], key: str) -> str:
    prefix = f"{key}:"
    for line in lines:
        if line.startswith(prefix):
            return line.split(":", 1)[1].strip()
    return ""


def set_field(lines: list[str], key: str, value: str) -> None:
    prefix = f"{key}:"
    for index, line in enumerate(lines):
        if line.startswith(prefix):
            lines[index] = f"{key}: {value}"
            return
    raise ValueError(f"Feld {key} fehlt")


def write_document(path: Path, front: list[str], body: list[str]) -> None:
    text = "\n".join(front + body).rstrip() + "\n"
    path.write_text(text, encoding="utf-8")


def book_and_pages(fragment: Path) -> tuple[str, str]:
    heading = ""
    for line in fragment.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            heading = line[2:].strip()
            break
    book = heading.split(" — ")[0].strip() if heading else fragment.parent.name
    match = None
    name = fragment.name
    marker = "-p"
    first = name.find(marker)
    second = name.find(marker, first + 1) if first != -1 else -1
    if first != -1 and second != -1:
        start_raw = name[first + 2 : second]
        end_raw = name[second + 2 :].removesuffix(".md")
        if start_raw.isdigit() and end_raw.isdigit():
            start, end = int(start_raw), int(end_raw)
            match = f"S. {start}" if start == end else f"S. {start}{PAGE_DASH}{end}"
    if match is None:
        match = "S. ?"
    return book, match


def source_line(roots: Roots, fragment: Path) -> str:
    book, pages = book_and_pages(fragment)
    link = vault_rel(roots, fragment).removesuffix(".md")
    return f"- {book}, {pages} → [[{link}|{pages}]]"


def section_bounds(lines: list[str], title: str) -> tuple[int, int] | None:
    start = None
    for index, line in enumerate(lines):
        if line.strip() == f"## {title}":
            start = index
            break
    if start is None:
        return None
    end = len(lines)
    for index in range(start + 1, len(lines)):
        if lines[index].startswith("## "):
            end = index
            break
    return start, end


def bullet_text(line: str) -> str:
    text = " ".join(line.strip().split())
    if text.startswith("- "):
        text = text[2:]
    return text


def normalize_bullet(text: str) -> str:
    return bullet_text(text)


def append_bullets(body: list[str], title: str, bullets: list[str]) -> tuple[list[str], int]:
    bounds = section_bounds(body, title)
    if bounds is None:
        raise ValueError(f"Abschnitt fehlt: {title}")
    start, end = bounds
    content = body[start + 1 : end]
    while content and content[-1].strip() == "":
        content.pop()
    existing = {bullet_text(line) for line in content if line.strip().startswith("- ")}
    added = 0
    for bullet in bullets:
        cleaned = normalize_bullet(bullet)
        if not cleaned:
            continue
        if len(cleaned) > MAX_BULLET_CHARS:
            raise ValueError(f"Stichpunkt zu lang ({len(cleaned)} Zeichen) in {title}")
        if cleaned in existing:
            continue
        content.append(f"- {cleaned}")
        existing.add(cleaned)
        added += 1
    if added == 0:
        return body, 0
    trailing = [""] if end < len(body) else []
    if content and content[0].strip() != "":
        content = ["", *content]
    rebuilt = body[: start + 1] + content + trailing + body[end:]
    return rebuilt, added


def apply_correction(body: list[str], title: str, old: str, new: str) -> tuple[list[str], int]:
    bounds = section_bounds(body, title)
    if bounds is None:
        raise ValueError(f"Abschnitt fehlt: {title}")
    start, end = bounds
    wanted = normalize_bullet(old)
    replacement = normalize_bullet(new)
    if not wanted or not replacement:
        raise ValueError("Korrektur braucht alt und neu")
    if len(replacement) > MAX_BULLET_CHARS:
        raise ValueError(f"Korrektur zu lang in {title}")
    hits = [
        index
        for index in range(start + 1, end)
        if body[index].strip().startswith("- ") and bullet_text(body[index]) == wanted
    ]
    if len(hits) != 1:
        return body, 0
    body = list(body)
    body[hits[0]] = f"- {replacement}"
    return body, 1


def drop_placeholder(body: list[str]) -> list[str]:
    skip = {
        "> [!info] Platzhalter",
        "> Diese Notiz ist angelegt, aber noch nicht befüllt. Inhalte werden ausschließlich aus geprüften Quellen ergänzt (siehe `quellen`).",
    }
    return [line for line in body if line.strip() not in skip]


def append_ledger(roots: Roots, record: dict) -> None:
    roots.ledger.parent.mkdir(parents=True, exist_ok=True)
    with roots.ledger.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def load_applied(roots: Roots) -> set[tuple[str, str]]:
    if not roots.ledger.is_file():
        return set()
    applied: set[tuple[str, str]] = set()
    for line in roots.ledger.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("op") != "add":
            continue
        begriff = str(row.get("begriff") or "")
        fragment = str(row.get("fragment") or "")
        if begriff and fragment:
            applied.add((begriff, fragment))
    return applied


def note_index(register: dict[str, dict]) -> dict[str, str]:
    index: dict[str, str] = {}
    for name, row in register.items():
        index[str(row["zielpfad"]).replace("\\", "/")] = name
    return index


def fragment_from_link(target: str) -> str:
    target = target.strip()
    if target.endswith(".md"):
        return target
    return f"{target}.md"


def link_records(body: list[str]) -> list[str]:
    found = []
    for line in body:
        marker = "[["
        if marker not in line or line.strip().startswith(">"):
            continue
        start = line.find(marker)
        end = line.find("|", start)
        close = line.find("]]", start)
        if end == -1 or close == -1 or end > close:
            continue
        target = line[start + 2 : end].strip()
        if "/Pilot/blocks/" in target:
            found.append(fragment_from_link(target))
    return found


def cmd_link(roots: Roots, records: list[dict], *, dry_run: bool) -> int:
    register = load_register(roots.register)
    errors = 0
    for record in records:
        raw_fragment = str(record.get("fragment") or "").strip()
        names = record.get("begriffe") or []
        if isinstance(names, str):
            names = [names]
        if not raw_fragment or not isinstance(names, list):
            print("fehler: fragment und begriffe fehlen", file=sys.stderr)
            errors += 1
            continue
        try:
            fragment = resolve_fragment(roots, raw_fragment)
        except (FileNotFoundError, ValueError) as exc:
            print(f"fehler: Fragment nicht lesbar: {exc}", file=sys.stderr)
            errors += 1
            continue
        line = source_line(roots, fragment)
        fragment_rel = vault_rel(roots, fragment)
        for name in names:
            begriff = str(name).strip()
            row = register.get(begriff)
            if row is None:
                print(f"unbekannt {begriff}")
                errors += 1
                continue
            try:
                path = note_path(roots, row)
                text = path.read_text(encoding="utf-8")
                front, body = split_document(text)
            except (OSError, ValueError) as exc:
                print(f"fehler: {begriff}: {exc}", file=sys.stderr)
                errors += 1
                continue
            status = field_value(front, "status")
            if status in LOCKED_STATUS:
                print(f"gesperrt {begriff} status={status}")
                errors += 1
                continue
            if line in text:
                print(f"vorhanden {begriff}")
                continue
            try:
                body, added = append_bullets(body, "Quellen und Fundstellen", [line[2:]])
            except ValueError as exc:
                print(f"fehler: {begriff}: {exc}", file=sys.stderr)
                errors += 1
                continue
            if added == 0:
                print(f"vorhanden {begriff}")
                continue
            print(f"verlinkt {begriff} <- {fragment.name}")
            if dry_run:
                continue
            write_document(path, front, body)
            append_ledger(
                roots,
                {
                    "ts": today(),
                    "op": "link",
                    "begriff": begriff,
                    "fragment": fragment_rel,
                    "note": vault_rel(roots, path),
                    "line": line,
                },
            )
    return 1 if errors else 0


def cmd_add(roots: Roots, records: list[dict], *, dry_run: bool) -> int:
    register = load_register(roots.register)
    errors = 0
    for record in records:
        begriff = str(record.get("begriff") or "").strip()
        raw_fragment = str(record.get("fragment") or "").strip()
        sections = record.get("sections") or {}
        corrections = record.get("korrekturen") or []
        done = bool(record.get("fertig"))
        row = register.get(begriff)
        if row is None:
            print(f"unbekannt {begriff}")
            errors += 1
            continue
        if not isinstance(sections, dict) or not isinstance(corrections, list):
            print(f"fehler: {begriff}: sections oder korrekturen ungültig", file=sys.stderr)
            errors += 1
            continue
        try:
            fragment = resolve_fragment(roots, raw_fragment)
            path = note_path(roots, row)
            text = path.read_text(encoding="utf-8")
            front, body = split_document(text)
        except (OSError, ValueError, FileNotFoundError) as exc:
            print(f"fehler: {begriff}: {exc}", file=sys.stderr)
            errors += 1
            continue
        status = field_value(front, "status")
        if status in LOCKED_STATUS:
            print(f"gesperrt {begriff} status={status}")
            errors += 1
            continue
        names = set(sections) | {
            str(item.get("abschnitt") or "") for item in corrections if isinstance(item, dict)
        }
        blocked = names & FORBIDDEN_SECTIONS
        unknown = {name for name in names if name and name not in SECTIONS}
        if blocked or unknown:
            print(
                f"fehler: {begriff}: Abschnitt nicht erlaubt: {', '.join(sorted(blocked | unknown))}",
                file=sys.stderr,
            )
            errors += 1
            continue
        try:
            corrected = 0
            for item in corrections:
                body, count = apply_correction(
                    body,
                    str(item.get("abschnitt") or ""),
                    str(item.get("alt") or ""),
                    str(item.get("neu") or ""),
                )
                corrected += count
                if count == 0:
                    print(f"korrektur-offen {begriff} / {item.get('abschnitt')}")
            added = 0
            for title, bullets in sections.items():
                if isinstance(bullets, str):
                    bullets = [bullets]
                body, count = append_bullets(body, str(title), list(bullets))
                added += count
        except (ValueError, TypeError, AttributeError) as exc:
            print(f"fehler: {begriff}: {exc}", file=sys.stderr)
            errors += 1
            continue
        fragment_rel = vault_rel(roots, fragment)
        if added == 0 and corrected == 0:
            if not done:
                print(f"leer {begriff} {fragment.name} bleibt offen")
                continue
            print(f"fertig {begriff} {fragment.name}")
        else:
            if status == "platzhalter":
                set_field(front, "status", "entwurf")
                body = drop_placeholder(body)
            set_field(front, "aktualisiert", today())
            print(f"ergänzt {begriff} +{added} ~{corrected}")
        if dry_run:
            continue
        if added or corrected:
            write_document(path, front, body)
        append_ledger(
            roots,
            {
                "ts": today(),
                "op": "add",
                "begriff": begriff,
                "fragment": fragment_rel,
                "note": vault_rel(roots, path),
                "added": added,
                "corrected": corrected,
                "fertig": done,
            },
        )
    return 1 if errors else 0


def cmd_pending(roots: Roots) -> int:
    register = load_register(roots.register)
    by_note = note_index(register)
    applied = load_applied(roots)
    rows: list[tuple[str, str, str]] = []
    for path in sorted(roots.notes.rglob("*.md")):
        rel = vault_rel(roots, path)
        begriff = by_note.get(rel)
        if begriff is None:
            continue
        try:
            front, body = split_document(path.read_text(encoding="utf-8"))
        except ValueError:
            continue
        if field_value(front, "status") in LOCKED_STATUS:
            continue
        for fragment_rel in link_records(body):
            if (begriff, fragment_rel) in applied:
                continue
            rows.append((begriff, fragment_rel, rel))
    if not rows:
        print("keine offenen Fragmente")
        return 0
    for begriff, fragment_rel, note_rel in rows:
        print(f"{begriff}\t{fragment_rel}\t{note_rel}")
    return 0


def self_test() -> int:
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        trading = root / "Trading"
        note = trading / "Notes" / "01" / "Marktstruktur.md"
        fragment = (
            trading
            / "Pilot"
            / "blocks"
            / "book"
            / "book-block-001-p010-p012.md"
        )
        register = trading / "System" / "Automation" / "concept-links.json"
        note.parent.mkdir(parents=True)
        fragment.parent.mkdir(parents=True)
        register.parent.mkdir(parents=True)
        fragment.write_text(
            "# Test Book — Chapter 1 (pages 10–12)\n\n--- page 10 ---\nBeispiel.\n",
            encoding="utf-8",
        )
        register.write_text(
            json.dumps(
                {
                    "konzepte": [
                        {
                            "begriff": "Marktstruktur",
                            "zieltyp": "wissensnotiz",
                            "primaer": True,
                            "zielpfad": "Trading/Notes/01/Marktstruktur.md",
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )
        note.write_text(
            "\n".join(
                [
                    "---",
                    "typ: wissen",
                    "status: platzhalter",
                    "aktualisiert: 2026-10-26",
                    "---",
                    "",
                    "# Marktstruktur",
                    "",
                    "> [!info] Platzhalter",
                    "> Diese Notiz ist angelegt, aber noch nicht befüllt. Inhalte werden ausschließlich aus geprüften Quellen ergänzt (siehe `quellen`).",
                    "",
                    "## Kurzdefinition",
                    "",
                    "## Kernaussagen",
                    "",
                    "## Quellen und Fundstellen",
                    "",
                ]
            ),
            encoding="utf-8",
        )
        roots = Roots(
            vault=root,
            trading=trading,
            notes=trading / "Notes",
            blocks=trading / "Pilot" / "blocks",
            register=register,
            ledger=trading / "Pilot" / "data" / "ledger.jsonl",
        )
        link_file = root / "link.json"
        add_file = root / "add.json"
        link_file.write_text(
            json.dumps(
                {"fragment": str(fragment), "begriffe": ["Marktstruktur", "GibtEsNicht"]}
            ),
            encoding="utf-8",
        )
        code = cmd_link(roots, load_records(link_file), dry_run=False)
        if code != 1:
            raise SystemExit(f"unbekannter Begriff muss fehlerhaft sein, code={code}")
        linked = note.read_text(encoding="utf-8")
        if "S. 10–12" not in linked or linked.count("S. 10–12") != 2:
            raise SystemExit(linked)
        again = cmd_link(roots, [{"fragment": str(fragment), "begriffe": ["Marktstruktur"]}], dry_run=False)
        if again != 0 or note.read_text(encoding="utf-8").count("[[") != 1:
            raise SystemExit("Quellenzeile wurde doppelt geschrieben")
        pending = cmd_pending(roots)
        if pending != 0:
            raise SystemExit("pending fehlgeschlagen")
        add_file.write_text(
            json.dumps(
                {
                    "begriff": "Marktstruktur",
                    "fragment": str(fragment),
                    "sections": {
                        "Kurzdefinition": ["Auktion aus zwei Seiten."],
                        "Kernaussagen": ["Auktion aus zwei Seiten."],
                    },
                }
            ),
            encoding="utf-8",
        )
        if cmd_add(roots, load_records(add_file), dry_run=False) != 0:
            raise SystemExit("add fehlgeschlagen")
        filled = note.read_text(encoding="utf-8")
        if "status: entwurf" not in filled or "Platzhalter" in filled:
            raise SystemExit(filled)
        if filled.count("Auktion aus zwei Seiten.") != 2:
            raise SystemExit("Deduplizierung hat über Abschnitte hinweg gelöscht")
        if cmd_add(roots, load_records(add_file), dry_run=False) != 0:
            raise SystemExit("zweiter add fehlgeschlagen")
        if note.read_text(encoding="utf-8").count("Auktion aus zwei Seiten.") != 2:
            raise SystemExit("Stichpunkt wurde doppelt angehängt")
        correction = {
            "begriff": "Marktstruktur",
            "fragment": str(fragment),
            "fertig": True,
            "sections": {"Kernaussagen": ["Zeitrahmen bestimmen die Spanne."]},
            "korrekturen": [
                {
                    "abschnitt": "Kurzdefinition",
                    "alt": "Auktion aus zwei Seiten.",
                    "neu": "Auktion aus zwei Seiten, über die Zeit verteilt.",
                }
            ],
        }
        if cmd_add(roots, [correction], dry_run=False) != 0:
            raise SystemExit("Korrektur fehlgeschlagen")
        corrected = note.read_text(encoding="utf-8")
        if "- Auktion aus zwei Seiten, über die Zeit verteilt." not in corrected:
            raise SystemExit(corrected)
        if "- Auktion aus zwei Seiten.\n" not in corrected:
            raise SystemExit(corrected)
        locked = note.read_text(encoding="utf-8").replace("status: entwurf", "status: geprüft")
        note.write_text(locked, encoding="utf-8")
        # Der Ledger kennt das Fragment schon. Eine neue Datei darf die geprüfte Notiz nicht anfassen.
        other = fragment.with_name("book-block-002-p013-p014.md")
        other.write_text(fragment.read_text(encoding="utf-8"), encoding="utf-8")
        before = note.read_text(encoding="utf-8")
        blocked = cmd_add(
            roots,
            [
                {
                    "begriff": "Marktstruktur",
                    "fragment": str(other),
                    "sections": {"Kernaussagen": ["Darf nicht hinein."]},
                }
            ],
            dry_run=False,
        )
        if blocked != 1 or note.read_text(encoding="utf-8") != before:
            raise SystemExit("geprüfte Notiz wurde verändert")
        empty = cmd_add(
            roots,
            [
                {
                    "begriff": "Marktstruktur",
                    "fragment": str(other),
                    "sections": {},
                }
            ],
            dry_run=False,
        )
        if empty != 1:
            raise SystemExit("leere Ergänzung auf gesperrter Notiz muss fehlerhaft bleiben")
    print("apply_update self-test ok")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] in {"-h", "--help"}:
        print(__doc__)
        return 0
    command = argv[1]
    dry_run = "--dry-run" in argv
    args = [arg for arg in argv[2:] if arg != "--dry-run"]
    roots = default_roots()
    if command == "self-test":
        return self_test()
    if command == "pending":
        return cmd_pending(roots)
    if command in {"link", "add"}:
        if len(args) != 1:
            print(f"Aufruf: apply_update.py {command} datei.json", file=sys.stderr)
            return 2
        records = load_records(Path(args[0]))
        if command == "link":
            return cmd_link(roots, records, dry_run=dry_run)
        return cmd_add(roots, records, dry_run=dry_run)
    print(f"unbekanntes Kommando: {command}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
