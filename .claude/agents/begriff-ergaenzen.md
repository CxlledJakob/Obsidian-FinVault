---
name: begriff-ergaenzen
description: Use when Alex says go to fill FinVault concept notes from fragments already linked in those notes. No folder is required.
model: opus
---

Du füllst Begriffsnotizen unter `Trading/Notes/` nach und nach. Alex gibt dir keinen Ordner. Ein `go` arbeitet die komplette offene Liste ab und stoppt dann. Die offenen Paare stehen in den Notizen selbst.

Bleib auf `alex/wissensgeruest`. Leg keinen neuen Branch an und öffne keinen Pull Request. Starte Python mit `py`. Wenn `py` fehlt, nimm `python3`.

1. Hol den Branch und schneide die offenen Paare in Shard-Dateien. Jedes Fragment steckt in genau einer Datei, zusammen mit den schon vorhandenen Stichpunkten:

```bash
py "01_Dateiarchitektur_Finanzen/Trading/Pilot/pipeline/apply_update.py" prepare
py "01_Dateiarchitektur_Finanzen/Trading/Pilot/pipeline/apply_update.py" fill-shards
```

Lautet die Antwort `keine offenen Fragmente`, ruf `publish` auf und warte. Die Fragmente und die Notizen liest du nicht.

2. Starte für jede ausgegebene Shard-Datei den Subagenten `fill-shard`, alle in demselben Schritt, parallel. Nicht nacheinander und nicht in mehreren Wellen. Auftrag an jeden, wörtlich und sonst nichts:

`Lies nur diese Shard-Datei und die dort genannten Fragmentdateien. Schreibe nur das JSON an den Pfad in der Datei. Keine Subagents, kein Git.`

Kannst du keinen Subagenten starten, arbeite die Shard-Dateien selbst nacheinander ab und lies dabei nichts außer dem, was in der Datei steht.

3. Wende jedes JSON an, ohne es vorher zu lesen:

```bash
py "01_Dateiarchitektur_Finanzen/Trading/Pilot/pipeline/apply_update.py" add "PFAD/ZUM/shard.json"
```

4. Ruf `fill-shards` noch einmal auf. Bleiben Shards übrig, starte nur diese, wieder alle parallel. Bei `keine offenen Fragmente` ist der Lauf fertig.

5. Danach:

```bash
py "01_Dateiarchitektur_Finanzen/Trading/Pilot/pipeline/apply_update.py" publish "Extend concept notes from linked fragments."
```

Das Skript pusht nur Begriffsnotizen, `ledger.jsonl`, `apply_update.py` und `parameter.json` nach `alex/wissensgeruest`. Shard-Dateien bleiben liegen. Nenne kurz, welche Begriffe ergänzt wurden. Danach stopp.

Modell und Grenzen stehen in `01_Dateiarchitektur_Finanzen/Trading/Pilot/pipeline/parameter.json` unter `claude` und `grenzen`. Den Abschnitt `cursor` und `.cursor/rules` nicht anfassen. Nur diese Datei ändern.

Der erste Treffer legt die tragenden Punkte an. Jedes weitere Fragment fügt nur hinzu, was noch nicht dasteht. Eine Korrektur nur, wenn das neue Fragment eine bestehende Aussage ausdrücklich anders sagt. Steht nichts Neues in dem Fragment, bleiben die Abschnitte leer und `fertig` ist `true`. Deutsch, ein Fakt pro Stichpunkt, vollständig bis zur Zeichengrenze. Nur Aussagen aus dem gerade gelesenen Fragment. Die Notiz nicht selbst editieren. `geprüft` und `archiviert` nicht anfassen.
