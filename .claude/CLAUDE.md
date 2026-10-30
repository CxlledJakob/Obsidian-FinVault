# Alex, Claude Code

Alex arbeitet hier mit Claude Code und seinem Claude-Abo. Cursor-Regeln unter `.cursor/rules` gehören Jakob. Die nicht löschen und nicht umschreiben.

Das Skript erkennt die Anwendung selbst. Claude setzt `CLAUDECODE` und pusht nach `alex/wissensgeruest`. Cursor setzt `CURSOR_AGENT` und pusht nach `jakob/features`. Beide Regelordner liegen im selben Repo.

Zwei getrennte Sitzungen. In jeder schreibt Alex nur `go`.

- Zuordnen: `claude --agent fragment-zuordnen`
- Ergänzen: `claude --agent begriff-ergaenzen`

Ist diese Sitzung keiner der beiden Agenten, und er schreibt `go`, frag nach, welche der zwei Aufgaben gemeint ist. Fang nicht von allein an.

Grenzen stehen in `01_Dateiarchitektur_Finanzen/Trading/Pilot/pipeline/parameter.json` unter `grenzen`. Modelle und Branch stehen unter `claude`. Zuordnung nutzt Sonnet, Ergänzung nutzt Opus. Die Pakete übernehmen `link-shard` und `fill-shard`.
