---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/13 - Volatilität/13 - Volatilität|13 - Volatilität]]"
weitere_hauptthemen: []
unterthema: "Volatilitätsmessung"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Parkinson-Volatilität


## Kurzdefinition

- Die Parkinson-Volatilität ist der Hoch-Tief-Schätzer von Parkinson (1980) für fortlaufend beobachtete Preise, die einer geometrischen Brownschen Bewegung folgen.

## Kernaussagen

- Beckers (1983) zeigt, dass Volatilitätsschätzer auf Hoch- und Tiefkursen genauer sind als die üblichen Schätzer auf Schlusskursen.
- Der Erwartungswert des mittleren quadrierten Logarithmus von Hoch zu Tief ist k1 σ²HL mit k1 = 4 log(2).
- Der Erwartungswert des mittleren Logarithmus von Hoch zu Tief ist k2 σHL mit k2 = √(8/π).
- Das Volatilitätsfeature σHL lässt sich robust aus den beobachteten Hoch- und Tiefkursen schätzen.
- Als Nebenprodukt des Corwin-Schultz-Modells lässt sich die Becker-Parkinson-Volatilität aus denselben Hoch-Tief-Größen ableiten.
- In den finalen Corwin-Schultz-Gleichungen für den Spread erscheint die Volatilität nicht mehr, weil sie durch ihren Hoch-Tief-Schätzer ersetzt wurde.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Die gezeigte Implementierung der Becker-Parkinson-Volatilität setzt negative Sigmawerte auf 0.

## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 191–210 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-011-p191-p210|S. 191–210]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 286–305 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-016-p286-p305|S. 286–305]]

## Verwandte Themen
