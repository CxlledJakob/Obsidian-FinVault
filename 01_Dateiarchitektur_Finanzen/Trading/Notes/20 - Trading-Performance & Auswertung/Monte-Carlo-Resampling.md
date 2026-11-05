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
aktualisiert: 2026-11-01
---

# Monte-Carlo-Resampling


## Kurzdefinition

- Monte-Carlo-Resampling meint hier das zufällige Neuordnen der Einstiegstage bei derselben Zahl von Long- und Short-Trades, um die Verteilung der Strategierendite unter der Null zu schätzen.

## Kernaussagen


## Funktionsweise

- Long- und Short-Signale werden mit derselben Permutation der Zeitachse vertauscht, die Haltedauer bleibt über verzögerte Signale erhalten, und gezählt wird, wie oft die durchschnittliche Strategierendite mindestens die beobachtete erreicht.
- Bei der TU-Strategie mit festem Halt über einen Monat genügt die Randomisierung der Starttage; unter 100.000 Permutationen erreicht keine die beobachtete Durchschnittsrendite.
- Der Text nennt diesen dritten Test für die TU-Strategie viel schwächer.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Eine erwartete APR von 10 Prozent, signifikant innerhalb von 1 Prozent, bedeutet in dieser Lesart, dass nur eine von 100 Zufallspermutationen der Einstiegstage eine APR von mindestens 10 Prozent erreicht.

## Risiken und Grenzen

- Weil die Null nicht eindeutig ist, können die Randomisierung der Einstiege und andere Nullverteilungen verschiedene Signifikanzschätzungen liefern.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 33–51 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-003-p033-p051|S. 33–51]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 216–235 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-016-p216-p235|S. 216–235]]

## Verwandte Themen
