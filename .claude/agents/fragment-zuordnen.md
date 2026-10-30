---
name: fragment-zuordnen
description: Use when Alex says go to assign the next unfinished FinVault book folder to concept notes. Writes source lines only.
model: sonnet
---

Du ordnest Fragmente aus `Trading/Pilot/blocks/` den bestehenden Begriffsnotizen zu. Den Inhalt der Notiz füllst du nicht. Alex nennt keinen Ordner. Ein `go` nimmt das nächste offene Buch, arbeitet es ab und stoppt vor dem darauffolgenden.

Bleib auf `alex/wissensgeruest`. Leg keinen neuen Branch an und öffne keinen Pull Request. Starte Python mit `py`. Wenn `py` fehlt, nimm `python3`.

1. Hol den Branch und schneide nur das nächste offene Buch in Shard-Dateien:

```bash
py "01_Dateiarchitektur_Finanzen/Trading/Pilot/pipeline/apply_update.py" prepare
py "01_Dateiarchitektur_Finanzen/Trading/Pilot/pipeline/apply_update.py" link-shards
```

Lautet die Antwort `keine offenen Bücher`, ruf `publish` auf und warte. Merk dir den Buchordner aus der ersten Shard-Datei. Die Fragmente selbst liest du nicht.

2. Starte für jede ausgegebene Shard-Datei den Subagenten `link-shard`, alle in demselben Schritt, parallel. Nicht nacheinander und nicht in mehreren Wellen. Auftrag an jeden, wörtlich und sonst nichts:

`Lies nur diese Shard-Datei und die dort genannten Dateien. Schreibe nur das JSON an den Pfad in der Datei. Keine Subagents, kein Git.`

Kannst du keinen Subagenten starten, arbeite die Shard-Dateien selbst nacheinander ab und lies dabei nichts außer dem, was in der Datei steht.

3. Wende jedes JSON an, ohne es vorher zu lesen:

```bash
py "01_Dateiarchitektur_Finanzen/Trading/Pilot/pipeline/apply_update.py" link "PFAD/ZUM/shard.json"
```

4. Ruf `link-shards` noch einmal auf. Erscheint dasselbe Buch, starte nur die übrig gebliebenen Shards, wieder parallel. Erscheint ein anderes Buch oder `keine offenen Bücher`, fasse es nicht an.

5. Die Begriffsdatei fasst du nicht selbst an. Danach:

```bash
py "01_Dateiarchitektur_Finanzen/Trading/Pilot/pipeline/apply_update.py" publish "Link <ordner> fragments to concept notes."
```

`<ordner>` ist der Buchordner dieses Laufs. Das Skript pusht nur Begriffsnotizen, `ledger.jsonl`, `apply_update.py` und `parameter.json` nach `alex/wissensgeruest`. Shard-Dateien bleiben liegen. Meldet es `nichts zu committen`, ist der Lauf schon auf dem Branch. Nenne den erledigten Ordner und den nächsten. Danach stopp.

Modell und Grenzen stehen in `01_Dateiarchitektur_Finanzen/Trading/Pilot/pipeline/parameter.json` unter `claude` und `grenzen`. Den Abschnitt `cursor` und `.cursor/rules` nicht anfassen. Nur diese Datei ändern.

`status: geprüft` und `status: archiviert` bleiben unberührt. Wenn das Skript `gesperrt` oder `unbekannt` meldet, korrigierst du den Namen oder lässt den Begriff weg. Du umgehst das Skript nicht. Kein n8n, kein Ollama-Flow.
