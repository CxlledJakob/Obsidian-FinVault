---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/17 - Risikomanagement/17 - Risikomanagement|17 - Risikomanagement]]"
weitere_hauptthemen: []
unterthema: "Risikomessung"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-01
---

# Tail Risk


## Kurzdefinition


## Kernaussagen

- Monte-Carlo-Simulationen auf simulierten statt historischen Daten schätzen das Tail Risk einer Strategie.
- Dieselben Simulationen prüfen die statistische Signifikanz eines Backtests.
- Das Risikomanagement bezieht schwarze Schwäne ein und mildert damit die Kelly-Formel, zusammen mit Constant Proportion Portfolio Insurance und Stop-Losses.
- Je häufiger Black-Swan-Ereignisse auftreten, desto wahrscheinlicher profitiert eine Momentum-Strategie.
- Je dicker die Ränder der Renditeverteilung oder je höher ihre Kurtosis, desto besser ist der Markt für Momentum-Strategien.
- Beispiel 1.1 erzeugt mit der Kurtosis der TU-Futures und ohne serielle Autokorrelation in 12 Prozent der Ziehungen dieselben Renditen wie die TU-Momentum-Strategie.
- Momentum kann in Risiken gedeihen, schnitt aber in der Folge riskanter Ereignisse schlecht ab.
- Das Abwärtspotenzial einer Mean-Reversion-Strategie kann unbegrenzt sein, das einer einzelnen Momentum-Position ist durch Zeitausstieg oder Stop begrenzt.
- Momentum-Modelle haben nicht dasselbe Tail Risk wie Mean-Reversion-Modelle, weil ein fortlaufend aktualisiertes Momentum-Signal als faktischer Stop-Loss wirkt.
- Ein Stop-Loss über dem maximalen Intraday-Drawdown des Backtests lässt die Backtest-Performance unverändert und kann ein künftiges Black-Swan-Ereignis am Weg in den Ruin hindern.
- Die Pearson-Simulation erfasst nur die ersten vier Momente; die wahre Verteilung kann unendliche höhere Momente haben wie die Pareto-Levy-Verteilung.
- Bei Hebel 31 wird die Wachstumsrate minus 1, weil die schlechteste Periodenrendite von minus 0,0331 jeden Hebel über 30,2 in den Totalverlust dieser Periode führt.
- Der simulierte maximale Drawdown kann so selten sein, dass er in einer Million Jahren kaum eintritt; das ist eine beliebte Entschuldigung von Fondsmanagern nach einem Verlust.
- Ein plötzlich stark negativer Orderflow eines riskanten Assets, etwa Aktien, Rohstoffe oder riskante Währungen, und ein positiver Orderflow bei US-Treasuries, USD, JPY oder CHF kann ein kurzfristiger führender Indikator des Tail-Risikos sein, bevor die Information den Preis weiter bewegt.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 1–13 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-001-p001-p013|S. 1–13]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 163–165 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-012-p163-p165|S. 163–165]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 180–199 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-014-p180-p199|S. 180–199]]

## Verwandte Themen
