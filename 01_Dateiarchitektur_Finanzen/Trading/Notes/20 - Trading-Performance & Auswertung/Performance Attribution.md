---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/20 - Trading-Performance & Auswertung/20 - Trading-Performance & Auswertung|20 - Trading-Performance & Auswertung]]"
weitere_hauptthemen: []
unterthema: "Trade-Auswertung"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Performance Attribution


## Kurzdefinition

- Performance-Attribution zerlegt den PnL nach Risikoklassen.

## Kernaussagen

- Ein Manager von Unternehmensanleihen will beispielsweise wissen, welcher Teil der Performance aus Duration, Kredit, Liquidität, Sektor, Währung, Emittentenstaat und Emittent stammt.
- Die Risikoklassen überlappen einander.
- Sehr liquide Anleihen haben häufig kurze Duration und hohes Rating, werden von großen Emittenten mit großem ausstehendem Volumen begeben und lauten oft auf US-Dollar.
- Wegen der Überlappung weicht die Summe der zugeordneten Teil-PnLs vom gesamten PnL ab.
- Je Risikoklasse lässt sich dennoch eine Sharpe Ratio oder eine Information Ratio berechnen.
- Das verbreitetste Beispiel einer solchen PnL-Zerlegung ist die Mehrfaktorenmethode von Barra.
- Der PnL lässt sich innerhalb einer Klasse zusätzlich auf Kategorien verteilen.

## Funktionsweise

- Jedes Instrument gehört zu jedem Zeitpunkt zu genau einer Kategorie einer Risikoklasse, die Kategorien einer Klasse sind also disjunkt.
- Je Kategorie wird ein Index aus den neu skalierten Portfoliogewichten gebildet, die zusammen eins ergeben.
- Derselbe Index wird mit den neu skalierten Gewichten des Anlageuniversums gebildet, die ebenfalls zusammen eins ergeben.
- Die Überschussrendite einer Kategorie ist die Rendite mit den Portfoliogewichten minus der Rendite mit den Universumsgewichten.
- Auf die Renditen und die Überschussrenditen der Kategorieindizes werden die Performance-Kennzahlen des Kapitels angewendet.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Duration lässt sich in kurz unter 5 Jahren, mittel von 5 bis 10 Jahren und lang über 10 Jahre teilen.
- Als Anlageuniversum wird unter anderem Markit iBoxx Investment Grade genannt.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]

## Verwandte Themen
