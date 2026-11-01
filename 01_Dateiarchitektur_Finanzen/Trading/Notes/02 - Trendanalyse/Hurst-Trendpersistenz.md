---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/02 - Trendanalyse/02 - Trendanalyse|02 - Trendanalyse]]"
weitere_hauptthemen: []
unterthema: "Trendmodelle"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-01
---

# Hurst-Trendpersistenz


## Kurzdefinition

- Der Hurst-Exponent H misst den Grad von Mean Reversion oder Trend einer Logpreisreihe: H gleich 0,5 ist ein geometrischer Random Walk, H größer als 0,5 ist ein Trend, und je näher H an 1 liegt, desto stärker ist der Trend.

## Kernaussagen

- Bei positiver Korrelation aufeinanderfolgender Preisbewegungen ist das Mittel von |z(t+τ) minus z(t)| zum Quadrat proportional zu τ hoch 2H und nicht proportional zu τ. z ist der Logpreis.
- Je weiter H gegen null sinkt, desto stärker ist die Mean Reversion. Auf USD.CAD ist H gleich 0,49, die Reihe ist also schwach mean-reverting und nicht trendend.
- Der Variance-Ratio-Test prüft die Null, dass H wirklich 0,5 ist. Für USD.CAD ist h gleich 0 und pValue gleich 0,367281, ein Random Walk bleibt möglich.
- Stationarität bedeutet hier nicht, dass die Varianz zeitunabhängig und H gleich null ist, sondern nur, dass die Varianz langsamer wächst als bei normaler Diffusion.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 52–71 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-004-p052-p071|S. 52–71]]

## Verwandte Themen
