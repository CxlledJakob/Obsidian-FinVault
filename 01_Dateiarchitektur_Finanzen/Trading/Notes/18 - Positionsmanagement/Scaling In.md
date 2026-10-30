---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/18 - Positionsmanagement/18 - Positionsmanagement|18 - Positionsmanagement]]"
weitere_hauptthemen: []
unterthema: "Trade Management"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Scaling In


## Kurzdefinition

- Scaling-in, in der Tradersprache auch Averaging-in, heißt bei einem linearen mean-revertierenden Modell, bei jedem Preisschritt zu kaufen oder zu verkaufen.
- Scaling-in, auch averaging-in, vergrößert das investierte Kapital, je weiter der Preis eines Assets, eines Spreads oder eines Portfolios vom Mittel abweicht, weil der mögliche Gewinn aus der späteren Umkehr mitwächst.
- Genau das tut die lineare Mean-Reversion-Strategie.

## Kernaussagen

- Die Vor- und Nachteile des Scaling-in werden erörtert.
- Der Kontext ist der Handel mean-revertierender Portfolios.
- Besonders bei Mean-Reversion-Strategien, die mit Spreads arbeiten, wird die Gefahr von Datenfehlern hervorgehoben.

## Funktionsweise

- Der gesamte Marktwert ist dann ungefähr proportional zur negativen Abweichung vom Mittel.
- Die zugrunde liegende Dynamik ist die Ornstein-Uhlenbeck-Formel dy(t) = (λy(t−1) + μ)dt + dε, also eine Preisänderung proportional zur Differenz aus Mittelpreis und aktuellem Preis.
- Das Bollinger-Band handelt dagegen erst, wenn der Preis eine Schwelle über- oder unterschreitet.
- Die Technik wird in Kapitel 3 behandelt.
- Mit Bollinger-Bändern wird Scaling-in über mehrere Einstiege umgesetzt, entryZscore gleich 1, 2, 3 bis N und exitZscore gleich 0, 1, 2 bis N minus 1, und N wird auf Trainingsdaten optimiert.
- Dieselben Strategien skalieren auch schrittweise aus und müssen den Gewinn nicht bis zur vollen Rückkehr zum Mittel aufschieben.
- In der Modellrechnung gibt es zwei Kontrakte Kaufkraft und drei Verfahren: beide bei L1, beide bei L2, oder einer bei L1 und einer bei L2.
- Die erwarteten Gewinne, bei Ausstieg erst in F, sind 2 mal (F minus L1), 2 mal p mal (F minus L2) und (F minus L1) plus p mal (F minus L2).

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Ist p gleich 0, ist all-in bei L1 am besten, ist p gleich 1, ist all-in bei L2 am besten.
- Die Schwelle p-Dach ist (F minus L1) geteilt durch (F minus L2); darunter schlägt all-in bei L1 sowohl all-in bei L2 als auch average-in, darüber schlägt all-in bei L2 die beiden anderen.
- Es gibt damit keinen Fall, in dem average-in bei konstantem p den höchsten erwarteten Gewinn hat.
- Die Rechnung nimmt an, dass die Rückkehr nach F auf die eine oder andere Weise sicher ist.

## Risiken und Grenzen

- Die implizite Annahme ist, dass die Wahrscheinlichkeit, vor F noch nach L2 zu fallen, über die Zeit konstant ist; in der Realität ist die Volatilität meist nicht konstant, also auch p nicht.
- Dann liefert Scaling-in voraussichtlich eine bessere realisierte Sharpe Ratio, wenn schon nicht mehr Gewinn.
- In der Stichprobe ist Scaling-in nie optimal, außer Stichprobe kann es die All-in-Methode übertreffen (Schoenberg und Corwin, 2010).
- Bei großen Größen verringert Scaling-in zusammen mit Scaling-out die Marktauswirkung der Trades.
- Der Vorteil des schrittweisen Ausstiegs bleibt auch, wenn die Reihe nicht wirklich stationär ist und nie zum Mittel zurückkehrt, weil kleine Gewinne fortlaufend realisiert werden.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]

## Verwandte Themen
