---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/17 - Risikomanagement/17 - Risikomanagement|17 - Risikomanagement]]"
weitere_hauptthemen: []
unterthema: "Verlustrisiko"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Risk of Ruin


## Kurzdefinition


## Kernaussagen

- Ein optimaler Hebel impliziert, dass das Konto historisch nie ruiniert wird, das Eigenkapital also nie null erreicht.
- Ist der maximale Drawdown minus 100 Prozent, ist auch die zusammengesetzte Wachstumsrate minus 100 Prozent; dieser Hebel ist nicht optimal.
- Ein überschätzter Kelly-Hebel, durch überschätzten Mittelwert oder unterschätzte Varianz, führt bei ausreichender Höhe schließlich zum Ruin.
- Nichtgaußische Renditen können den Kelly-Hebel schon im Backtest auf einen maximalen Drawdown von minus 1 bringen.
- Half-Kelly wird gewählt, weil die Folge eines zu hohen Hebels der Ruin sein kann und die Folge eines zu niedrigen nur eine geringere Wachstumsrate ist.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Ein Stop-Loss über dem maximalen Intraday-Drawdown des Backtests kann ein künftiges Black-Swan-Ereignis am Weg in den Ruin hindern.
- Ohne diesen Schutz kann ein Wechsel von Mean Reversion zu einem anhaltenden Trend einen Verlust von 100 Prozent erzeugen.
- Bei CPPI wird die Strategie aufgegeben, wenn das Handels-Subkonto vollständig verloren ist; der Drawdown des Gesamtkontos ist dann auf minus D begrenzt.

## Risiken und Grenzen


## Beispiele

- Im Monte-Carlo-Beispiel ist bei Hebel 31 die Wachstumsrate minus 1, weil die schlechteste Periodenrendite minus 0,0331 beträgt und jeder Hebel über 1 geteilt durch 0,0331 gleich 30,2 in dieser Periode zum Totalverlust führt.
- Die dreifach gehebelten ETFs BGU und TNA liegen über dem Kelly-Hebel von etwa 1,8 der Russell-Indizes; ihr Nettoinventarwert kann auf null gehen.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]

## Verwandte Themen
