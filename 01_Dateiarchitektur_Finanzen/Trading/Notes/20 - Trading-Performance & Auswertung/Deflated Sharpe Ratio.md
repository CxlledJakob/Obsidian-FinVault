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
aktualisiert: 2026-10-30
---

# Deflated Sharpe Ratio


## Kurzdefinition

- Die Deflated Sharpe Ratio ist eine Probabilistic Sharpe Ratio, deren Vergleichsschwelle aus der Zahl und der Streuung der Versuche geschätzt wird.

## Kernaussagen

- Die Deflated Sharpe Ratio korrigiert inflationäre Effekte aus nichtnormalen Renditen, aus der Länge der Historie und aus Mehrfachtests oder Selection Bias.

## Funktionsweise

- Die Vergleichsschwelle wird aus der Varianz der versuchsweisen Sharpe Ratios, der Zahl der unabhängigen Versuche und der Euler-Mascheroni-Konstante über die inverse Verteilungsfunktion der Standardnormalverteilung bestimmt.
- Die Vergleichsschwelle steigt schnell, wenn mehr unabhängige Versuche unternommen werden oder die Varianz der versuchsweisen Sharpe Ratios größer ist.
- Auch bei einer wahren Sharpe Ratio von null liegt der erwartete Höchstwert der Schätzungen über null, und genau dieser Höchstwert dient als Vergleichsschwelle.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Für das übliche Signifikanzniveau von 5 Prozent soll die Deflated Sharpe Ratio über 0,95 liegen.
- Die Deflated Sharpe Ratio kann auf absoluten oder auf relativen Renditen berechnet werden.

## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]

## Verwandte Themen
