# Alex

Dieser Checkout gehört Alex. Alle Arbeit bleibt auf `alex/wissensgeruest`. Leg keinen neuen Branch an und öffne keinen Pull Request.

Alex nutzt Claude Code mit seinem Claude-Abo, in zwei getrennten Sitzungen. In jeder schreibt er nur `go`.

- Zuordnen: `claude --agent fragment-zuordnen`
- Ergänzen: `claude --agent begriff-ergaenzen`

Ist diese Sitzung keiner der beiden Agenten, und er schreibt `go`, frag nach, welche der zwei Aufgaben gemeint ist. Fang nicht von allein an.

Grenzen und Modelle stehen in `01_Dateiarchitektur_Finanzen/Trading/Pilot/pipeline/parameter.json`. Zuordnung arbeitet mit Sonnet, Ergänzung mit Opus. Die Pakete übernehmen `link-shard` und `fill-shard`.
