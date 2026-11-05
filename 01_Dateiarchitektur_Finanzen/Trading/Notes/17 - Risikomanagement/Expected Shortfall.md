---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/17 - Risikomanagement/17 - Risikomanagement|17 - Risikomanagement]]"
weitere_hauptthemen: []
unterthema: "Risikomessung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Expected Shortfall


## Kurzdefinition

- Die dritte Auflage nimmt den Expected Shortfall, auch Conditional Value at Risk, zur Messung des finanziellen Risikos in das neu gefasste Kapitel 7 auf.
- Der Expected Shortfall ist der Erwartungswert der Verlustfunktion, gegeben dass der Value at Risk überschritten wird.
- Der Expected Shortfall heißt auch Conditional Value at Risk.
- Der Expected Shortfall zu einem gegebenen VaR ist der erwartete Verlust gegeben, dass der VaR überschritten wird.

## Kernaussagen

- Kapitel 7 gibt einen einheitlichen Zugang zum Value at Risk über eine Verlustfunktion und behandelt den Expected Shortfall, gleichbedeutend mit dem Conditional Value at Risk.
- Kapitel 7 behandelt Methoden zur Berechnung des Value at Risk und des Expected Shortfall einer Finanzposition, zusammen mit Extreme-Value-Theorie und Verteilungen mit schweren Rändern im Risikomanagement.
- Der tatsächliche Verlust kann größer als der VaR sein; der Expected Shortfall bewertet den Verlust gerade für den Fall, dass der VaR überschritten wird.
- Unter RiskMetrics ist die Verlustfunktion normalverteilt, sodass die bedingte Verteilung gegeben einer VaR-Überschreitung eine von unten gestutzte Normalverteilung ist.
- Für die Standardnormalverteilung X und die obere Schwanzwahrscheinlichkeit p ist E(X gegeben X > VaRq) = f(VaRq) / p, mit q = 1 minus p und f als Dichte von X.
- Für eine Logrendite mit bedingter Verteilung N(0, σ zum Quadrat von t) ist der Expected Shortfall ESq = [f(VaRq) / p] mal σt.
- Bei p = 0,05 ist VaR0,95 ungefähr 1,645 und f(VaRq) / p = 2,0627, also beträgt ES0,95 = 2,0627 σt.
- Bei p = 0,01 beträgt ES0,99 = 2,6652 σt.

## Funktionsweise

- Ist die Logrendite bedingt N(μt, σ zum Quadrat von t), gilt ESq = μt plus [f(xq) / p] mal σt, wobei q = 1 minus p und xq das q-Quantil der Standardnormalverteilung ist.
- Für p = 0,01 wird daraus μt plus 2,6652 σt.
- Der empirische Expected Shortfall ist der Mittelwert aller Stichprobenwerte, die über dem empirischen Quantil x Dach q liegen.
- Für die verallgemeinerte Pareto-Verteilung mit 0 < ξ < 1 ist ESq = VaRq / (1 minus ξ) plus [ψ(η) minus ξ η] / (1 minus ξ).
- Der bedingte Exzess über den VaR ist [ψ(η) plus ξ mal (VaRq minus η)] geteilt durch (1 minus ξ).

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Für die negativen täglichen IBM-Logrenditen, in Prozent gerechnet, ist bei p = 0,01 das empirische Quantil 3,630 und der Expected Shortfall 5,097.
- Für die negativen IBM-Tageslogrenditen bei Schwelle 2,5 Prozent liefert riskmeasures der GPD die Expected Shortfalls 0,03162619, 0,05075390 und 0,09699565 zu den Wahrscheinlichkeiten 0,95, 0,99 und 0,999.
- Auf eine Position von 10 Millionen Dollar sind das 316.272 Dollar bei Schwanzwahrscheinlichkeit 0,05 und 507.576 Dollar bei 0,01.
- Dieselben Shortfalls aus dem pot-Befehl lauten 0,03162728, 0,05075740 und 0,09699513 zu denselben drei Wahrscheinlichkeiten.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 1–20 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-001-p001-p020|S. 1–20]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 20–39 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-002-p020-p039|S. 20–39]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 343–362 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-019-p343-p362|S. 343–362]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 362–381 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-020-p362-p381|S. 362–381]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 381–400 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-021-p381-p400|S. 381–400]]

## Verwandte Themen
