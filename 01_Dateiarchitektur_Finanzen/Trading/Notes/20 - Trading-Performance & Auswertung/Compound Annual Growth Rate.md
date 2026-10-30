---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/20 - Trading-Performance & Auswertung/20 - Trading-Performance & Auswertung|20 - Trading-Performance & Auswertung]]"
weitere_hauptthemen: []
unterthema: "Renditekennzahlen"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Compound Annual Growth Rate


## Kurzdefinition


## Kernaussagen

- Das Ziel ist die Maximierung des langfristigen Eigenkapitalwachstums; Risiko wird nur vermieden, soweit es dieses Ziel stört.
- Der optimale Hebel maximiert das Nettovermögen oder gleichbedeutend die zusammengesetzte Wachstumsrate.
- Hebel null erzeugt weder Risiko noch Rendite.
- Drei Methoden berechnen diesen Hebel; jede hat eigene Annahmen und Nachteile.
- Ist der maximale Drawdown bei einem Hebel minus 100 Prozent, ist die zusammengesetzte Wachstumsrate ebenfalls minus 100 Prozent, und der Hebel ist nicht optimal.
- Der Hebel muss konstant gehalten werden, mit oder ohne Drawdown-Nebenbedingung, damit die Wachstumsrate optimiert wird.

## Funktionsweise

- Unter einer guten Gauß-Näherung erzeugt der Kelly-Hebel die höchste zusammengesetzte Wachstumsrate, wenn alle Gewinne reinvestiert werden.
- Bei risikofreiem Zins null ist der Erwartungswert der Wachstumsrate g(f) der Durchschnitt von log(1 plus f mal R).
- Ist R gaußisch, lässt sich dieses g(f) analytisch reduzieren, und das Maximum aus der Ableitung nach f gleich null reproduziert die Kelly-Formel.
- Bei optimalen Hebeln und risikofreiem Zins null ist die annualisierte zusammengesetzte Wachstumsrate g gleich F transponiert mal C mal F, geteilt durch 2.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Ein unterschätzter Hebel lässt nur eine untermaximale Wachstumsrate; ein überschätzter kann zum Ruin führen.
- CPPI erzeugt nicht dieselbe zusammengesetzte Rendite wie der Hebel f mal D auf dem Gesamtkonto, außer jede Periode ist positiv.
- Ob CPPI langfristig dieselbe Wachstumsrate wie der Hebel f mal D hat, ist dem Autor kein mathematischer Beweis bekannt.

## Beispiele

- Im Beispiel zweier unkorrelierter Strategien beträgt g bei den Kelly-Hebeln 2,1.
- Unter dem Höchsthebel 2 fällt g bei proportionaler Kürzung auf 0,82 und steigt auf 0,96, wenn die gesamte Kaufkraft auf die Strategie mit der höchsten Wachstumsrate geht.
- Für die Mean-Reversion-Strategie aus Beispiel 5.1 liegt das Monte-Carlo-Maximum von g nahe 19 und numerisch bei 19, gegenüber Kelly 18,4.
- Bei Hebel 31 ist die Wachstumsrate minus 1, also Ruin.
- Die historische Optimierung derselben Strategie ergibt ebenfalls den Hebel 18,4.
- Nach 100.000 Tagen liegen CPPI und die Alternative bei D gleich 0,5 in einer Simulation bei 0,002484 gegen 0,002525 Wachstumsrate pro Tag.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]

## Verwandte Themen
