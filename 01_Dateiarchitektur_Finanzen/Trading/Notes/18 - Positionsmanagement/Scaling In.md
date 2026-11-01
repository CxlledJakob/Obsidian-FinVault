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
aktualisiert: 2026-11-01
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
- Gleitender Durchschnitt und gleitende Standardabweichung sollen einen sich langsam ändernden Mittelwert und eine mit der Zeit steigende Varianz mitnehmen und den Gewinn schneller realisieren. Dieser Punkt wird in Kapitel 3 im Zusammenhang mit Scaling-in ausgeführt.
- Schoenberg und Corwin (2010) zeigen, dass Ein- oder Ausstieg an zwei oder mehr Bollinger-Bändern nie optimal ist. Ein einzelnes Niveau, all-in, erzielt im Backtest immer eine höhere durchschnittliche Rendite.
- Die erwarteten Punktgewinne sind 2(F minus L1) für all-in bei L1, 2p(F minus L2) für all-in bei L2 und (F minus L1) plus p(F minus L2) für average-in. Mit p-Dach gleich (F minus L1)/(F minus L2) ist average-in nie am profitabelsten, solange p konstant ist und die Rückkehr nach F sicher ist.
- Ist die Volatilität nicht konstant, ist auch p nicht konstant. Dann kann Scaling-in eine bessere realisierte Sharpe Ratio liefern, auch ohne den höchsten Gewinn, und out of sample das in-sample optimale all-in schlagen.
- Schrittweises Aussteigen muss nicht auf die volle Rückkehr warten. Selbst wenn die Reihe nicht stationär ist und den Mittelwert nie erreicht, lassen sich fortlaufend kleine Gewinne realisieren. Bei großen Größen sinkt zusätzlich der Market Impact.
- Im Zahlenbeispiel von Schoenberg und Corwin wird trotz average-in erst bei F alles geschlossen, und die Kaufkraft deckt genau zwei Kontrakte.

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
- Scaling-in ist im Backtest oft nicht optimal, im Live-Handel aber häufig nützlich, weil Volatilitäten und Wahrscheinlichkeiten sich ändern.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 1–13 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-001-p001-p013|S. 1–13]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 14–33 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-002-p014-p033|S. 14–33]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 52–71 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-004-p052-p071|S. 52–71]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 76–95 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-006-p076-p095|S. 76–95]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 95–98 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-007-p095-p098|S. 95–98]]

## Verwandte Themen
