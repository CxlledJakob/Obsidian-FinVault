#!/usr/bin/env python3
"""Hilfsskript für die zwei Cursor-Agenten.

Der Zuordnungs-Agent schreibt nur Quellenzeilen (link).
Der Ergänzungs-Agent hängt nur neue Stichpunkte an (add).
Keine der beiden Rollen schreibt eine Begriffsnotiz im Ganzen neu.

Aufrufe:
  python3 apply_update.py prepare
  python3 apply_update.py next
  python3 apply_update.py link zuordnungen.json
  python3 apply_update.py add ergaenzungen.json
  python3 apply_update.py pending
  python3 apply_update.py link-shards
  python3 apply_update.py fill-shards
  python3 apply_update.py publish "Commit-Nachricht"
  python3 apply_update.py self-test

Modell und Grenzen liegen in parameter.json neben diesem Skript.
"""

from __future__ import annotations

import json
import re
import subprocess
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
BRANCH = "jakob/features"
BULLET_CHARS = 220
ALLOWED_MODELS = frozenset(
    {
        "grok-4.7-low",
        "grok-4.7-medium",
        "grok-4.7-high",
        "grok-4.7-xhigh",
    }
)
STRENGE_TEXT = {
    "streng": (
        "Nur zuordnen, wenn das Fragment den Begriff definiert, eine Regel gibt oder ein Kriterium nennt. "
        "Eine Erwähnung, ein Beispiel oder ein Wort im Inhaltsverzeichnis reicht nicht. Lieber zu wenige als zu viele."
    ),
    "mittel": (
        "Nur zuordnen, wenn das Fragment den Begriff erklärt oder eine konkrete Regel daran hängt. "
        "Eine bloße Namensnennung reicht nicht."
    ),
    "locker": (
        "Zuordnen, wenn der Begriff im Fragment eine Rolle spielt. "
        "Ein Inhaltsverzeichnis oder eine Namensliste ohne Ausführung reicht nicht."
    ),
}
NOTES_PREFIX = "01_Dateiarchitektur_Finanzen/Trading/Notes/"
LEDGER_REL = "01_Dateiarchitektur_Finanzen/Trading/Pilot/data/ledger.jsonl"
APPLY_REL = "01_Dateiarchitektur_Finanzen/Trading/Pilot/pipeline/apply_update.py"
PARAMETER_REL = "01_Dateiarchitektur_Finanzen/Trading/Pilot/pipeline/parameter.json"


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


@dataclass(frozen=True)
class Lauf:
    zuordnung_modell: str = "grok-4.7-medium"
    strenge: str = "mittel"
    max_begriffe: int = 18
    link_shard_size: int = 4
    ergaenzung_modell: str = "grok-4.7-high"
    max_neue_punkte: int = 12
    max_zeichen: int = 360
    wiederholung_schwelle: float = 0.72
    fill_shard_size: int = 3
    vorhandene_punkte: int = 12


def clamp_modell(value: object, default: str) -> str:
    if value is None or value == "":
        return default
    text = str(value).strip()
    if text in ALLOWED_MODELS:
        return text
    print(f"parameter modell {text} ungültig, {default}", file=sys.stderr)
    return default


def clamp_strenge(value: object) -> str:
    if value is None or value == "":
        return "mittel"
    text = str(value).strip().lower()
    if text in STRENGE_TEXT:
        return text
    print(f"parameter strenge {text} ungültig, mittel", file=sys.stderr)
    return "mittel"


def clamp_int(value: object, default: int, low: int, high: int, label: str) -> int:
    if value is None or value == "":
        return default
    try:
        number = int(value)
    except (TypeError, ValueError):
        print(f"parameter {label} ungültig, {default}", file=sys.stderr)
        return default
    if number < low or number > high:
        bounded = min(max(number, low), high)
        print(f"parameter {label} auf {bounded} begrenzt", file=sys.stderr)
        return bounded
    return number


def clamp_schwelle(value: object, default: float) -> float:
    if value is None or value == "":
        return default
    try:
        number = float(value)
    except (TypeError, ValueError):
        print(f"parameter wiederholung_schwelle ungültig, {default}", file=sys.stderr)
        return default
    if number < 0 or number > 0.95:
        bounded = min(max(number, 0.0), 0.95)
        print(f"parameter wiederholung_schwelle auf {bounded} begrenzt", file=sys.stderr)
        return bounded
    return number


def load_lauf() -> Lauf:
    defaults = Lauf()
    path = Path(__file__).resolve().parent / "parameter.json"
    if not path.is_file():
        print("parameter fehlt, Voreinstellung", file=sys.stderr)
        return defaults
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"parameter ungültig: {exc}", file=sys.stderr)
        return defaults
    if not isinstance(data, dict):
        print("parameter ungültig, Voreinstellung", file=sys.stderr)
        return defaults
    zuordnung = data.get("zuordnung") or {}
    ergaenzung = data.get("ergaenzung") or {}
    if not isinstance(zuordnung, dict) or not isinstance(ergaenzung, dict):
        print("parameter abschnitte ungültig, Voreinstellung", file=sys.stderr)
        return defaults
    return Lauf(
        zuordnung_modell=clamp_modell(zuordnung.get("modell"), defaults.zuordnung_modell),
        strenge=clamp_strenge(zuordnung.get("strenge")),
        max_begriffe=clamp_int(
            zuordnung.get("max_begriffe_pro_fragment"),
            defaults.max_begriffe,
            1,
            40,
            "max_begriffe_pro_fragment",
        ),
        link_shard_size=clamp_int(
            zuordnung.get("fragmente_pro_shard"),
            defaults.link_shard_size,
            1,
            8,
            "fragmente_pro_shard",
        ),
        ergaenzung_modell=clamp_modell(ergaenzung.get("modell"), defaults.ergaenzung_modell),
        max_neue_punkte=clamp_int(
            ergaenzung.get("max_neue_punkte_pro_fragment"),
            defaults.max_neue_punkte,
            1,
            30,
            "max_neue_punkte_pro_fragment",
        ),
        max_zeichen=clamp_int(
            ergaenzung.get("max_zeichen_pro_punkt"),
            defaults.max_zeichen,
            80,
            MAX_BULLET_CHARS,
            "max_zeichen_pro_punkt",
        ),
        wiederholung_schwelle=clamp_schwelle(
            ergaenzung.get("wiederholung_schwelle"),
            defaults.wiederholung_schwelle,
        ),
        fill_shard_size=clamp_int(
            ergaenzung.get("fragmente_pro_shard"),
            defaults.fill_shard_size,
            1,
            8,
            "fragmente_pro_shard",
        ),
        vorhandene_punkte=clamp_int(
            ergaenzung.get("vorhandene_punkte_zeigen"),
            defaults.vorhandene_punkte,
            0,
            40,
            "vorhandene_punkte_zeigen",
        ),
    )


def limit_names(names: list, cap: int) -> tuple[list[str], int]:
    kept: list[str] = []
    seen: set[str] = set()
    extra = 0
    for name in names:
        begriff = str(name).strip()
        if not begriff or begriff in seen:
            continue
        seen.add(begriff)
        if len(kept) >= cap:
            extra += 1
            continue
        kept.append(begriff)
    return kept, extra


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
    # The span is the trailing -pNNN-pNNN.md. The first "-p" in the name can
    # belong to the book slug, as in markets-in-profile.
    found = re.search(r"-p(\d+)-p(\d+)\.md$", fragment.name)
    if found:
        start, end = int(found.group(1)), int(found.group(2))
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


STOPWORDS = frozenset(
    """
    aber alle allem allen aller alles als also auch auf aus bei bin bis bist da
    damit dann das dass der den des dem die dies diese diesem diesen dieser
    dieses doch dort du durch ein eine einem einen einer eines er es euer für
    hatte hatten hier hin ich ihm ihn ihnen ihr ihre ihrem ihren ihres im in ist
    jede jedem jeden jeder jedes jetzt kann kein keine keinem keinen keiner
    keines können man mit muss müssen nach nicht nichts noch nur ob oder ohne
    sehr sein seine seinem seinen seiner seines selbst sich sie sind so solche
    sondern sonst über um und uns unser unsere unserem unseren unserer unseres
    unter vom von vor während war waren was weg weil weiter welche welchem
    welchen welcher welches wenn wer werde werden wie wir wird wirst wo wollen
    wollte wurde wurden würde würden zu zum zur zwar the and with that this from
    into over when your their they are was were been have has had not but for
    you its his her
    """.split()
)


def content_tokens(text: str) -> set[str]:
    return {
        word
        for word in re.findall(r"[a-z0-9äöüß]+", text.lower())
        if len(word) > 3 and word not in STOPWORDS
    }


def too_similar(candidate: str, existing: str, threshold: float) -> bool:
    if threshold <= 0:
        return False
    left = content_tokens(candidate)
    right = content_tokens(existing)
    if len(left) < 4 or len(right) < 4:
        return False
    union = left | right
    if not union:
        return False
    return len(left & right) / len(union) >= threshold


def append_bullets(
    body: list[str],
    title: str,
    bullets: list[str],
    *,
    similar: float = 0.0,
) -> tuple[list[str], int]:
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
        if cleaned in existing or any(too_similar(cleaned, item, similar) for item in existing):
            if cleaned not in existing:
                print(f"wiederholt {title}: {cleaned[:60]}")
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


def load_assigned(roots: Roots) -> set[str]:
    if not roots.ledger.is_file():
        return set()
    assigned: set[str] = set()
    for line in roots.ledger.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("op") != "zugeordnet":
            continue
        fragment = str(row.get("fragment") or "").replace("\\", "/")
        if fragment:
            assigned.add(fragment)
    return assigned


def open_books(roots: Roots) -> list[tuple[Path, list[Path]]]:
    if not roots.blocks.is_dir():
        return []
    assigned = load_assigned(roots)
    found: list[tuple[Path, list[Path]]] = []
    for folder in sorted(path for path in roots.blocks.iterdir() if path.is_dir()):
        pending_files = [
            fragment
            for fragment in sorted(folder.glob("*.md"))
            if vault_rel(roots, fragment) not in assigned
        ]
        if pending_files:
            found.append((folder, pending_files))
    return found


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
    assigned = load_assigned(roots)
    lauf = load_lauf()
    errors = 0
    for record in records:
        raw_fragment = str(record.get("fragment") or "").strip()
        if "begriffe" not in record:
            print("fehler: fragment und begriffe fehlen", file=sys.stderr)
            errors += 1
            continue
        names = record.get("begriffe")
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
        if fragment_rel in assigned:
            print(f"erledigt {fragment.name}")
            continue
        names, extra = limit_names(names, lauf.max_begriffe)
        if extra:
            print(f"gekürzt {fragment.name} {len(names)}/{len(names) + extra}")
        fragment_errors = 0
        linked: list[str] = []
        for name in names:
            begriff = str(name).strip()
            row = register.get(begriff)
            if row is None:
                print(f"unbekannt {begriff}")
                fragment_errors += 1
                errors += 1
                continue
            try:
                path = note_path(roots, row)
                text = path.read_text(encoding="utf-8")
                front, body = split_document(text)
            except (OSError, ValueError) as exc:
                print(f"fehler: {begriff}: {exc}", file=sys.stderr)
                fragment_errors += 1
                errors += 1
                continue
            status = field_value(front, "status")
            if status in LOCKED_STATUS:
                print(f"gesperrt {begriff} status={status}")
                fragment_errors += 1
                errors += 1
                continue
            if line in text:
                print(f"vorhanden {begriff}")
                linked.append(begriff)
                continue
            try:
                body, added = append_bullets(body, "Quellen und Fundstellen", [line[2:]])
            except ValueError as exc:
                print(f"fehler: {begriff}: {exc}", file=sys.stderr)
                fragment_errors += 1
                errors += 1
                continue
            if added == 0:
                print(f"vorhanden {begriff}")
                linked.append(begriff)
                continue
            print(f"verlinkt {begriff} <- {fragment.name}")
            linked.append(begriff)
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
        if fragment_errors:
            continue
        print(f"zugeordnet {fragment.name}")
        if dry_run:
            continue
        append_ledger(
            roots,
            {
                "ts": today(),
                "op": "zugeordnet",
                "fragment": fragment_rel,
                "begriffe": linked,
            },
        )
        assigned.add(fragment_rel)
    return 1 if errors else 0


def cap_sections(begriff: str, sections: dict, lauf: Lauf) -> dict:
    remaining = lauf.max_neue_punkte
    kept: dict = {}
    dropped = 0
    long_ones = 0
    for title, bullets in sections.items():
        if isinstance(bullets, str):
            bullets = [bullets]
        if not isinstance(bullets, list):
            raise TypeError(f"Abschnitt {title} ist keine Liste")
        chosen: list[str] = []
        for bullet in bullets:
            cleaned = normalize_bullet(str(bullet))
            if not cleaned:
                continue
            if len(cleaned) > lauf.max_zeichen:
                long_ones += 1
                continue
            if remaining <= 0:
                dropped += 1
                continue
            chosen.append(cleaned)
            remaining -= 1
        if chosen:
            kept[str(title)] = chosen
    if long_ones:
        print(f"zu-lang {begriff} {long_ones}")
    if dropped:
        print(f"punkte-gekürzt {begriff} {dropped}")
    return kept


def cmd_add(roots: Roots, records: list[dict], *, dry_run: bool) -> int:
    register = load_register(roots.register)
    lauf = load_lauf()
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
            usable_corrections = []
            for item in corrections:
                if not isinstance(item, dict):
                    raise TypeError("Korrektur ist kein Objekt")
                neu = normalize_bullet(str(item.get("neu") or ""))
                if neu and len(neu) > lauf.max_zeichen:
                    print(f"zu-lang {begriff} / {item.get('abschnitt')}")
                    continue
                usable_corrections.append(item)
            sections = cap_sections(begriff, sections, lauf)
            corrected = 0
            for item in usable_corrections:
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
                body, count = append_bullets(
                    body,
                    str(title),
                    list(bullets),
                    similar=lauf.wiederholung_schwelle,
                )
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


def cmd_next(roots: Roots) -> int:
    books = open_books(roots)
    if not books:
        print("keine offenen Bücher")
        return 0
    folder, files = books[0]
    print(f"ordner {vault_rel(roots, folder)}")
    print(f"offen {len(files)}")
    for fragment in files:
        print(vault_rel(roots, fragment))
    return 0


def pending_pairs(roots: Roots) -> list[tuple[str, str, str]]:
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
    return rows


def cmd_pending(roots: Roots) -> int:
    rows = pending_pairs(roots)
    if not rows:
        print("keine offenen Fragmente")
        return 0
    for begriff, fragment_rel, note_rel in rows:
        print(f"{begriff}\t{fragment_rel}\t{note_rel}")
    return 0


def split_groups(items: list, size: int) -> list[list]:
    if size < 1:
        raise ValueError("Shard-Größe fehlt")
    return [items[index : index + size] for index in range(0, len(items), size)]


def display_path(roots: Roots, path: Path) -> str:
    try:
        return path.resolve().relative_to(roots.vault.parent.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def content_bullets(body: list[str]) -> list[str]:
    found: list[str] = []
    for title in SECTIONS:
        if title == "Quellen und Fundstellen":
            continue
        bounds = section_bounds(body, title)
        if bounds is None:
            continue
        start, end = bounds
        for line in body[start + 1 : end]:
            if not line.strip().startswith("- "):
                continue
            text = bullet_text(line)
            if text:
                found.append(text)
    return found


def work_dir(roots: Roots) -> Path:
    return roots.trading / "Pilot" / "data" / "work"


def clear_shard_files(directory: Path, prefix: str) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    ignore = directory / ".gitignore"
    if not ignore.exists():
        ignore.write_text("*\n!.gitignore\n", encoding="utf-8")
    for path in directory.glob(f"{prefix}-*"):
        if path.is_file():
            path.unlink()


def print_shards(roots: Roots, paths: list[Path], empty: str) -> int:
    if not paths:
        print(empty)
        return 0
    print(f"shards {len(paths)}")
    for path in paths:
        print(display_path(roots, path))
    return 0


def write_link_shards(roots: Roots, lauf: Lauf | None = None) -> list[Path]:
    books = open_books(roots)
    directory = work_dir(roots)
    clear_shard_files(directory, "link")
    if not books:
        return []
    if lauf is None:
        lauf = load_lauf()
    folder, files = books[0]
    taxonomy = roots.trading / "Research" / "Taxonomie" / "Themenstruktur.txt"
    paths: list[Path] = []
    for index, group in enumerate(split_groups(files, lauf.link_shard_size), start=1):
        path = directory / f"link-{index:02d}.md"
        json_path = directory / f"link-{index:02d}.json"
        lines = [
            f"# Link {index}",
            "",
            f"Buch: {vault_rel(roots, folder)}",
            f"JSON: {display_path(roots, json_path)}",
            f"Themenliste: {display_path(roots, taxonomy)}",
            "",
            "Lies die Themenliste einmal. Lies jede Fragmentdatei unten genau einmal, vollständig.",
            "Keine andere Datei. Keine Subagents. Kein Git. Keine Begriffsnotiz anfassen.",
            "Schreibe ein JSON-Array. Pro Fragment genau ein Objekt, in dieser Reihenfolge:",
            '{"fragment": "exakter Pfad", "begriffe": ["Exakter Begriff"]}',
            "Der Fragmentpfad ist der Pfad aus dieser Datei, unverändert.",
            "begriffe bleibt leer, wenn nichts passt. Namen müssen exakt aus der Themenliste stammen.",
            f"Strenge: {lauf.strenge}. {STRENGE_TEXT[lauf.strenge]}",
            f"Höchstens {lauf.max_begriffe} Begriffe. Die wichtigsten zuerst. Das Skript behält nur diese und streicht den Rest.",
            "Keine neuen Begriffe.",
            "",
            "## Fragmente",
            "",
        ]
        for fragment in group:
            lines.append(f"- {vault_rel(roots, fragment)}")
        path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        paths.append(path)
    return paths


def write_fill_shards(roots: Roots, lauf: Lauf | None = None) -> list[Path]:
    pairs = pending_pairs(roots)
    directory = work_dir(roots)
    clear_shard_files(directory, "fill")
    if not pairs:
        return []
    if lauf is None:
        lauf = load_lauf()
    by_fragment: dict[str, list[tuple[str, str]]] = {}
    for begriff, fragment_rel, note_rel in pairs:
        by_fragment.setdefault(fragment_rel, []).append((begriff, note_rel))
    sections = ", ".join(title for title in SECTIONS if title != "Quellen und Fundstellen")
    paths: list[Path] = []
    fragments = sorted(by_fragment)
    for index, group in enumerate(split_groups(fragments, lauf.fill_shard_size), start=1):
        path = directory / f"fill-{index:02d}.md"
        json_path = directory / f"fill-{index:02d}.json"
        lines = [
            f"# Fill {index}",
            "",
            f"JSON: {display_path(roots, json_path)}",
            "",
            "Lies jede Fragmentdatei unten genau einmal, vollständig. Keine andere Datei.",
            "Keine Subagents. Kein Git. Die Notizdateien nicht öffnen.",
            "Schreibe ein JSON-Array. Pro genanntem Begriff genau ein Objekt:",
            '{"begriff": "Exakter Begriff", "fragment": "exakter Pfad", "sections": {"Kernaussagen": ["Ein Fakt."]}, "korrekturen": [], "fertig": true}',
            "fragment ist der Pfad aus der Überschrift, unverändert. begriff ist die Überschrift, unverändert.",
            "Setze fertig immer auf true, auch wenn du Stichpunkte ergänzt.",
            "Steht in dem Fragment nichts Neues, lass sections leer.",
            f"Erlaubte Abschnitte: {sections}.",
            "Eigene Erkenntnisse nicht füllen. Deutsch, ein Fakt pro Stichpunkt, höchstens zwei Sätze.",
            f"Höchstens {lauf.max_neue_punkte} neue Stichpunkte für diesen Begriff aus diesem Fragment, über alle Abschnitte. Die wichtigsten zuerst.",
            f"Ein Stichpunkt hat höchstens {lauf.max_zeichen} Zeichen. Das Skript streicht darüber hinaus.",
            "Nur Aussagen aus dem gerade gelesenen Fragment. Vorhandene Stichpunkte nicht wiederholen und nicht umformulieren.",
            "Eine Korrektur nur, wenn das Fragment eine vorhandene Aussage ausdrücklich anders sagt.",
            "",
        ]
        for fragment_rel in group:
            lines.append(f"## {fragment_rel}")
            lines.append("")
            for begriff, note_rel in sorted(by_fragment[fragment_rel]):
                lines.append(f"### {begriff}")
                lines.append(f"Notiz: {note_rel}")
                lines.append("Vorhanden:")
                bullets: list[str] = []
                try:
                    _front, body = split_document((roots.vault / note_rel).read_text(encoding="utf-8"))
                    bullets = content_bullets(body)
                except (OSError, ValueError):
                    bullets = []
                if not bullets:
                    lines.append("(keine)")
                else:
                    for item in bullets[: lauf.vorhandene_punkte]:
                        short = item if len(item) <= BULLET_CHARS else item[:BULLET_CHARS].rstrip() + "…"
                        lines.append(f"- {short}")
                    extra = len(bullets) - lauf.vorhandene_punkte
                    if extra > 0:
                        lines.append(f"- … {extra} weitere")
                lines.append("")
        path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        paths.append(path)
    return paths


def cmd_link_shards(roots: Roots) -> int:
    lauf = load_lauf()
    print(f"modell {lauf.zuordnung_modell}")
    print(f"strenge {lauf.strenge}")
    print(f"max_begriffe {lauf.max_begriffe}")
    return print_shards(roots, write_link_shards(roots, lauf), "keine offenen Bücher")


def cmd_fill_shards(roots: Roots) -> int:
    lauf = load_lauf()
    print(f"modell {lauf.ergaenzung_modell}")
    print(f"max_neue_punkte {lauf.max_neue_punkte}")
    return print_shards(roots, write_fill_shards(roots, lauf), "keine offenen Fragmente")


def allowed_work_path(path: str) -> bool:
    path = path.replace("\\", "/").lstrip("./")
    if path in {LEDGER_REL, APPLY_REL, PARAMETER_REL}:
        return True
    return path.startswith(NOTES_PREFIX)


def parse_status_z(raw: str) -> list[str]:
    paths: list[str] = []
    index = 0
    parts = raw.split("\0")
    while index < len(parts):
        entry = parts[index]
        index += 1
        if len(entry) < 4:
            continue
        status = entry[:2]
        paths.append(entry[3:])
        if "R" in status or "C" in status:
            index += 1
    return paths


def selectable_paths(raw: str) -> list[str]:
    return [path for path in parse_status_z(raw) if allowed_work_path(path)]


def repo_root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=Path(__file__).resolve().parent,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0 or not result.stdout.strip():
        detail = (result.stderr or result.stdout).strip()
        raise RuntimeError(detail or "git rev-parse fehlgeschlagen")
    return Path(result.stdout.strip())


def git(repo: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )


def git_text(repo: Path, *args: str) -> str:
    result = git(repo, *args)
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()
        raise RuntimeError(f"git {' '.join(args)}: {detail}")
    return result.stdout


def current_branch(repo: Path) -> str:
    return git_text(repo, "rev-parse", "--abbrev-ref", "HEAD").strip()


def stash_tracked(repo: Path) -> bool:
    dirty = False
    for line in git_text(repo, "status", "--porcelain").splitlines():
        if line and not line.startswith("??"):
            dirty = True
            break
    if not dirty:
        return False
    result = git(repo, "stash", "push", "-m", "finvault-prepare")
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()
        raise RuntimeError(f"git stash: {detail}")
    return True


def pop_stash(repo: Path) -> None:
    result = git(repo, "stash", "pop")
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()
        raise RuntimeError(f"git stash pop: {detail}")


def checkout_work_branch(repo: Path) -> None:
    if current_branch(repo) == BRANCH:
        return
    stashed = stash_tracked(repo)
    try:
        exists = git(repo, "show-ref", "--verify", "--quiet", f"refs/heads/{BRANCH}")
        if exists.returncode == 0:
            checkout = git(repo, "checkout", BRANCH)
        else:
            checkout = git(repo, "checkout", "-B", BRANCH, f"origin/{BRANCH}")
        if checkout.returncode != 0:
            detail = (checkout.stderr or checkout.stdout).strip()
            raise RuntimeError(f"Wechsel auf {BRANCH}: {detail}")
    except Exception:
        if stashed:
            git(repo, "stash", "pop")
        raise
    if stashed:
        pop_stash(repo)


def cmd_prepare() -> int:
    try:
        repo = repo_root()
        fetch = git(repo, "fetch", "origin", BRANCH)
        if fetch.returncode != 0:
            detail = (fetch.stderr or fetch.stdout).strip()
            raise RuntimeError(f"git fetch: {detail}")
        checkout_work_branch(repo)
        pull = git(repo, "pull", "--rebase", "--autostash", "origin", BRANCH)
        if pull.returncode != 0:
            detail = (pull.stderr or pull.stdout).strip()
            raise RuntimeError(f"git pull: {detail}")
        head = git_text(repo, "rev-parse", "--short", "HEAD").strip()
    except RuntimeError as exc:
        print(f"fehler: {exc}", file=sys.stderr)
        return 1
    print(f"branch {BRANCH} {head}")
    return 0


def push_work_branch(repo: Path) -> None:
    last_detail = ""
    for _attempt in range(2):
        pull = git(repo, "pull", "--rebase", "--autostash", "origin", BRANCH)
        if pull.returncode != 0:
            detail = (pull.stderr or pull.stdout).strip()
            raise RuntimeError(f"git pull: {detail}")
        push = git(repo, "push", "-u", "origin", f"HEAD:{BRANCH}")
        if push.returncode == 0:
            return
        last_detail = (push.stderr or push.stdout).strip()
    raise RuntimeError(f"git push: {last_detail}")


def cmd_publish(message: str) -> int:
    message = " ".join(message.split())
    if not message:
        print("fehler: Commit-Nachricht fehlt", file=sys.stderr)
        return 2
    try:
        repo = repo_root()
        if current_branch(repo) != BRANCH:
            print(
                f"fehler: Branch ist {current_branch(repo)}. Zuerst prepare.",
                file=sys.stderr,
            )
            return 2
        raw = git_text(repo, "status", "--porcelain", "-z")
        paths = selectable_paths(raw)
        if not paths:
            print("nichts zu committen")
            return 0
        add = git(repo, "add", "--", *paths)
        if add.returncode != 0:
            detail = (add.stderr or add.stdout).strip()
            raise RuntimeError(f"git add: {detail}")
        commit = git(repo, "commit", "-m", message)
        if commit.returncode != 0:
            detail = (commit.stderr or commit.stdout).strip()
            raise RuntimeError(f"git commit: {detail}")
        if commit.stdout.strip():
            print(commit.stdout.strip())
        push_work_branch(repo)
        head = git_text(repo, "rev-parse", "--short", "HEAD").strip()
    except RuntimeError as exc:
        print(f"fehler: {exc}", file=sys.stderr)
        return 1
    print(f"gepusht {BRANCH} {head}")
    return 0


def self_test() -> int:
    sample = (
        " M 01_Dateiarchitektur_Finanzen/Trading/Notes/A.md\0"
        "?? 02_n8n Flows/Jakob/x\0"
        " D 02_n8n Flows/Dockerfile\0"
        "M  01_Dateiarchitektur_Finanzen/Trading/Pilot/pipeline/apply_update.py\0"
        "R  01_Dateiarchitektur_Finanzen/Trading/Pilot/data/ledger.jsonl\0"
        "01_Dateiarchitektur_Finanzen/Trading/Notes/Old.md\0"
    )
    chosen = selectable_paths(sample)
    expected = [
        "01_Dateiarchitektur_Finanzen/Trading/Notes/A.md",
        APPLY_REL,
        LEDGER_REL,
    ]
    if chosen != expected:
        raise SystemExit(f"Publish-Auswahl falsch: {chosen}")
    if not allowed_work_path(PARAMETER_REL):
        raise SystemExit("parameter.json wird nicht veröffentlicht")
    if split_groups(["a", "b", "c", "d", "e"], 3) != [["a", "b", "c"], ["d", "e"]]:
        raise SystemExit("Shard-Schnitt falsch")
    if clamp_modell("grok-4.7-high-fast", "grok-4.7-high") != "grok-4.7-high":
        raise SystemExit("fast-modell wurde akzeptiert")
    if clamp_modell("grok-4.7-medium", "grok-4.7-high") != "grok-4.7-medium":
        raise SystemExit("medium abgelehnt")
    kept, extra = limit_names(["A", " A", "B", "", "C"], 2)
    if kept != ["A", "B"] or extra != 1:
        raise SystemExit(f"Begriffsgrenze falsch: {kept} {extra}")
    sample_body = [
        "## Kernaussagen",
        "",
        "- Aufwand ist das Volumen und Ergebnis ist die Preisspanne.",
        "",
    ]
    _, similar_added = append_bullets(
        sample_body,
        "Kernaussagen",
        ["Aufwand ist das Volumen, Ergebnis ist die Preisspanne."],
        similar=0.72,
    )
    if similar_added != 0:
        raise SystemExit("ähnlicher Stichpunkt wurde behalten")
    _, different_added = append_bullets(
        sample_body,
        "Kernaussagen",
        ["Eine enge Kerze mit hohem Volumen ist eine Anomalie."],
        similar=0.72,
    )
    if different_added != 1:
        raise SystemExit("anderer Stichpunkt wurde verworfen")
    capped = cap_sections(
        "X",
        {"Kernaussagen": ["eins", "zwei", "drei"]},
        Lauf(max_neue_punkte=2, max_zeichen=360),
    )
    if capped != {"Kernaussagen": ["eins", "zwei"]}:
        raise SystemExit(f"Punktegrenze falsch: {capped}")
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
        profile = fragment.with_name("markets-in-profile-block-001-p001-p020.md")
        profile.write_text(fragment.read_text(encoding="utf-8"), encoding="utf-8")
        _, pages = book_and_pages(profile)
        profile.unlink()
        if pages != f"S. 1{PAGE_DASH}20":
            raise SystemExit(f"Seitenspanne im Buchslug falsch: {pages}")
        _, plain = book_and_pages(fragment)
        if plain != f"S. 10{PAGE_DASH}12":
            raise SystemExit(f"Seitenspanne falsch: {plain}")
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
        lauf = load_lauf()
        if lauf.zuordnung_modell not in ALLOWED_MODELS or lauf.ergaenzung_modell not in ALLOWED_MODELS:
            raise SystemExit("modell nicht erlaubt")
        early = write_link_shards(roots, lauf)
        if len(early) != 1:
            raise SystemExit(f"link-shards: {early}")
        early_text = early[0].read_text(encoding="utf-8")
        if f"Strenge: {lauf.strenge}" not in early_text or f"Höchstens {lauf.max_begriffe}" not in early_text:
            raise SystemExit(early_text)
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
        open_names = [path.name for _, files in open_books(roots) for path in files]
        if fragment.name not in open_names:
            raise SystemExit("fehlerhafter Lauf hat das Fragment abgehakt")
        linked = note.read_text(encoding="utf-8")
        if "S. 10–12" not in linked or linked.count("S. 10–12") != 2:
            raise SystemExit(linked)
        again = cmd_link(roots, [{"fragment": str(fragment), "begriffe": ["Marktstruktur"]}], dry_run=False)
        if again != 0 or note.read_text(encoding="utf-8").count("[[") != 1:
            raise SystemExit("Quellenzeile wurde doppelt geschrieben")
        if any(path.name == fragment.name for _, files in open_books(roots) for path in files):
            raise SystemExit("abgehaktes Fragment bleibt offen")
        pending = cmd_pending(roots)
        if pending != 0:
            raise SystemExit("pending fehlgeschlagen")
        fill_paths = write_fill_shards(roots)
        if len(fill_paths) != 1:
            raise SystemExit(f"fill-shards: {fill_paths}")
        fill_text = fill_paths[0].read_text(encoding="utf-8")
        if "Marktstruktur" not in fill_text or "fertig" not in fill_text or "Höchstens" not in fill_text:
            raise SystemExit(fill_text)
        link_paths = write_link_shards(roots)
        if link_paths:
            raise SystemExit("abgehaktes Buch darf keine Link-Shards haben")
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
        if cmd_link(roots, [{"fragment": str(other), "begriffe": []}], dry_run=False) != 0:
            raise SystemExit("leere Zuordnung fehlgeschlagen")
        if any(path.name == other.name for _, files in open_books(roots) for path in files):
            raise SystemExit("Fragment ohne Begriff bleibt offen")
        nxt = trading / "Pilot" / "blocks" / "zzz-next" / "zzz-next-block-001-p001-p002.md"
        nxt.parent.mkdir(parents=True)
        nxt.write_text("# Next — Chapter (pages 1–2)\n\n--- page 1 ---\nX.\n", encoding="utf-8")
        opened = open_books(roots)
        if len(opened) != 1 or opened[0][0].name != "zzz-next" or opened[0][1][0] != nxt:
            raise SystemExit(f"nächstes Buch falsch: {[item[0].name for item in opened]}")
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
    if command == "prepare":
        return cmd_prepare()
    if command == "publish":
        return cmd_publish(" ".join(args))
    if command == "pending":
        return cmd_pending(roots)
    if command == "next":
        return cmd_next(roots)
    if command == "link-shards":
        return cmd_link_shards(roots)
    if command == "fill-shards":
        return cmd_fill_shards(roots)
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
