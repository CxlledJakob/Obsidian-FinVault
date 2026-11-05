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
aktualisiert: 2026-11-05
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
- Der Parkinson-Schätzer mit f = 0 lautet σ̂²_{2,t} = (H_t − L_t)² / (4 ln 2) ≈ 0,3607 (H_t − L_t)².
- Garman und Klass (1980) finden für diesen Schätzer unter einem einfachen Diffusionsmodell ohne Drift einen Effizienzfaktor von etwa 5,2 gegenüber dem Schluss-zu-Schluss-Schätzer (C_t − C_{t−1})².
- Weil Aktienkurse nur zu diskreten Zeitpunkten beobachtet werden, liegt das beobachtete Tageshoch tendenziell unter dem wahren Hoch und das Tagestief über dem wahren Tief. Die beobachtete Spanne unterschätzt die wahre Spanne und kann die Volatilität unterschätzen.
- Diese Verzerrung hängt von der Handelsfrequenz und der Tickgröße ab und sollte bei intensiv gehandelten Aktien vernachlässigbar sein.
- Die tägliche Spanne der Logpreise wird in der Literatur als robuste Alternative zur Volatilitätsmodellierung verwendet (Chou 2005).
- Für Apple vom 4. Januar 1999 bis 20. November 2007, 2235 Beobachtungen, betragen Mittelwert, Standardabweichung, Minimum und Maximum der Logpreis-Range 0,0407, 0,0218, 0,0068 und 0,1468.
- Die zwei 2:1-Splits von Apple am 21. Juni 2000 und am 28. Februar 2005 erfordern keine Anpassung, weil die tägliche Spanne der Logpreise verwendet wird.

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
