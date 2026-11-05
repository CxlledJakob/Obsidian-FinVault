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
aktualisiert: 2026-11-05
---

# Tail Risk


## Kurzdefinition

- Mit Extremen einer Renditereihe sind die großen positiven oder großen negativen Renditen gemeint.

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
- Zusammenbrüche großer Finanzinstitute in der Krise zeigen, dass Extremereignisse in Clustern auftreten und nicht unabhängig sind.
- Der Extremal Index in Kapitel 7 behandelt diese Abhängigkeit in den Extremen und ihren Einfluss auf den Value at Risk.
- Kapitel 7 behandelt Extreme-Value-Theorie, Verteilungen mit schweren Rändern und ihre Anwendung im Risikomanagement, insbesondere die Berechnung von Value at Risk und Expected Shortfall einer Finanzposition.
- Eine Verteilung mit positiver Exzess-Kurtosis legt mehr Masse auf die Ränder als eine Normalverteilung, und eine Zufallsstichprobe daraus enthält tendenziell mehr Extremwerte; sie heißt leptokurtisch.
- Die Exzess-Kurtosis der täglichen einfachen IBM-Renditen ist hoch und zeigt schwere Ränder.
- Tabelle 1.2 zeigt, dass Minimum und Maximum einer Renditereihe erheblich sein können.
- Negative Extremrenditen sind für das Risikomanagement wichtig, positive Extremrenditen für das Halten einer Short-Position.
- Kapitel 7 untersucht Eigenschaften und Anwendungen extremer Renditen: die Häufigkeit ihres Auftretens, die Größe eines Extremums und den Einfluss ökonomischer Variablen auf die Extreme.
- Die Kapitel 2 bis 4 konzentrieren sich auf die ersten vier Momente einer Renditereihe, Kapitel 7 auf das Verhalten von Minimum und Maximum.
- Die empirische Dichte der monatlichen IBM-Renditen von 1926 bis 2008 hat dickere Ränder und einen höheren Gipfel als die Normaldichte mit dem Stichprobenmittel und der Stichprobenstandardabweichung.
- Die Cauchy-Verteilung, ein Beispiel einer nichtnormalen stabilen Verteilung, ist symmetrisch bezüglich ihres Medians, hat unendliche Varianz und dickere Ränder als die in Abbildung 1.1 gezeigte endliche Normalmischung.
- Die aus dem Sprungdiffusionsprozess abgeleitete Renditeverteilung hat dickere Ränder und einen höheren Gipfel als die Normalverteilung mit Mittel 0 und Varianz 2,0572×10^−4.
- Die Wahrscheinlichkeit genau eines Sprungs im Intervall (t, t + Δt] ist λ Δt; die Wahrscheinlichkeit mehrerer Sprünge ist o(Δt) und wird für kleines Δt vernachlässigt.
- Bei λ = 10, κ = −0,02 und η = 0,02 werden etwa 10 Tagessprünge pro Jahr mit mittlerer Sprunggröße −2 Prozent und Standardfehler der Sprunggröße 2 Prozent unterstellt; diese Werte gelten als vernünftig für eine US-Aktie.
- Bei Sprüngen ist der Markt unvollständig, und die Standard-Hedge-Argumente gelten für die Optionsbewertung nicht.
- Extreme Kursbewegungen sind selten, aber wichtig; genannt werden der Börsenkrach an der Wall Street im Oktober 1987, Long-Term Capital Management und die Insolvenz von Lehman Brothers.
- Der VaR beschreibt den oberen Schwanz der Verlustverteilung nicht vollständig und unterschätzt den tatsächlichen Verlust tendenziell, wenn ein Extremereignis eintritt.
- Zwei Positionen können denselben VaR haben und bei Überschreitung dennoch unterschiedliche Verluste erleiden.
- Schwere Ränder führen dazu, dass die Normalannahme den VaR oft unterschätzt.
- Für das Risikomanagement interessiert vor allem die Fréchet-Familie, weil sie schwere Schwänze wie stabile Verteilungen und die Student-t enthält; Gumbel umfasst die dünnen Schwänze von Normal- und Lognormalverteilung.
- Der Tail-Index ξ beziehungsweise α = 1/ξ hängt nicht vom Zeitintervall der Rendite ab und ist unter Zeitaggregation invariant.
- Die empirische Quantilmethode kann keinen Verlust prognostizieren, der größer ist als der größte historische Verlust, obwohl der VaR gerade die Schwanzwahrscheinlichkeit betrifft.
- Blockmaxima übersehen das Volatility Clustering und können den VaR der täglichen IBM-Logrenditen bei 5 und 1 Prozent unter das empirische Quantil drücken. Peaks over Thresholds verwendet die Höhe der Überschreitung über eine hohe Schwelle.
- Bei kleiner Schwanzwahrscheinlichkeit zeigt sich der schwere Schwanz: Student-t und Extremwertverteilung liefern dann einen höheren VaR als die Normalannahme.
- Der Effekt extremer Werte, also schwerer Ränder, auf den VaR ist stärker, wenn die verwendete Tail-Wahrscheinlichkeit klein ist.
- Im inhomogenen Poisson-Modell der IBM-Logrenditen hat der Formparameter einen negativen Jahrestrend; die Logrenditen entfernen sich damit im Zeitverlauf von der Normalität. Lage- und Skalenparameter der Intensität steigen über die Zeit.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- In der Anwendung spielt die Volatilität eine wichtige Rolle in der Optionsbewertung und im Risikomanagement; die negativen Extreme einer Renditereihe sind der für das Risikomanagement wesentliche Teil der Extreme.

## Regeln und Kriterien


## Risiken und Grenzen

- Ohne Berücksichtigung des Extremalindex, also der Clusterbildung extremer Renditen, wird der VaR tendenziell unterschätzt.

## Beispiele

- Tabelle 1.2, Minimum und Maximum der täglichen einfachen Renditen in Prozent: S&P −20,47 und 11,58, value-weighted −17,13 und 11,52, equal-weighted −10,39 und 10,74, IBM −22,96 und 13,16, Intel −29,57 und 26,38, 3M −25,98 und 11,54, Microsoft −30,12 und 19,57, Citigroup −26,41 und 57,82.
- Tägliche Logrenditen, Minimum und Maximum: S&P −22,90 und 10,96, IBM −26,09 und 12,37, Intel −35,06 und 23,41, Microsoft −35,83 und 17,87, Citigroup −30,66 und 45,63.
- Monatliche einfache Renditen, Minimum und Maximum: equal-weighted −31,28 und 66,59, Intel −44,87 und 62,50, Microsoft −34,35 und 51,55, Citigroup −39,27 und 26,08. Monatliche Logrenditen: Intel −59,54 und 48,55, Citigroup −49,87 und 23,18, Microsoft −42,09 und 41,58.
- Im IBM-Beispiel erhöht eine Student-t mit 5 Freiheitsgraden gegenüber der Normalverteilung den 1-Prozent-VaR einer Long-Position von 10 Millionen Dollar von 409.738 auf 475.943 Dollar.
- Bei 0,1 Prozent beträgt der VaR von 10 Millionen Dollar long in IBM 836.341 Dollar mit Student-t und 5 Freiheitsgraden und 666.590 Dollar mit der klassischen Extremwerttheorie bei Blocklänge 21, gegenüber 546.641 Dollar im gaußschen AR(2)–GARCH(1,1) und 566.443 Dollar bei RiskMetrics.
- Am 31. Dezember 1998 beträgt das VaR einer IBM-Long-Position von 10 Millionen Dollar bei Tail-Wahrscheinlichkeit 0,05 genau 303.756 Dollar und bei Tail-Wahrscheinlichkeit 0,01 genau 497.425 Dollar.
- Am 30. Dezember 1998, nach einem Tag mit großer Bewegung, beträgt dasselbe 5-Prozent-VaR 269.139 Dollar und das 1-Prozent-VaR 448.323 Dollar.
- Mit Extremalindex 0,823 liegt das 1-Prozent-VaR der negativen IBM-Logrenditen bei Teilperiode n gleich 63 bei 3,2714, ohne Extremalindex bei 3,0497.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 1–13 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-001-p001-p013|S. 1–13]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 163–165 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-012-p163-p165|S. 163–165]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 180–199 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-014-p180-p199|S. 180–199]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 1–20 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-001-p001-p020|S. 1–20]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 20–39 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-002-p020-p039|S. 20–39]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 39–58 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-003-p039-p058|S. 39–58]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 324–343 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-018-p324-p343|S. 324–343]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 343–362 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-019-p343-p362|S. 343–362]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 362–381 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-020-p362-p381|S. 362–381]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 381–400 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-021-p381-p400|S. 381–400]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 400–419 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-022-p400-p419|S. 400–419]]

## Verwandte Themen
