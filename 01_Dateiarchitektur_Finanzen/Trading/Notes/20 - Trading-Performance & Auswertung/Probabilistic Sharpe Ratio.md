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

# Probabilistic Sharpe Ratio


## Kurzdefinition

- Die Probabilistic Sharpe Ratio ist die geschätzte Wahrscheinlichkeit, dass die beobachtete Sharpe Ratio über einer Benchmark-Sharpe-Ratio liegt.

## Kernaussagen

- Die Probabilistic Sharpe Ratio entfernt den inflationären Effekt kurzer Reihen mit schiefen oder dickschwänzigen Renditen.
- Die Benchmark kann auf null gesetzt werden, als Vergleich mit fehlendem Anlageskill.
- Die Probabilistic Sharpe Ratio steigt mit der beobachteten Sharpe Ratio in der ursprünglichen Beobachtungsfrequenz, vor einer Annualisierung.
- Die Probabilistic Sharpe Ratio steigt mit der Zahl der beobachteten Renditen.
- Die Probabilistic Sharpe Ratio steigt mit positiver Schiefe der Renditen.
- Die Probabilistic Sharpe Ratio sinkt mit höherer Kurtosis.
- Berechnet wird sie mit der Verteilungsfunktion der Standardnormalverteilung aus dem Abstand zur Benchmark, der Reihenlänge, der Schiefe und der Kurtosis.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Für das übliche Signifikanzniveau von 5 Prozent soll die Probabilistic Sharpe Ratio über 0,95 liegen.
- Die Probabilistic Sharpe Ratio kann auf absoluten oder auf relativen Renditen berechnet werden.

## Risiken und Grenzen

- In die Probabilistic Sharpe Ratio gehen die vom Portfoliomanager gesetzten Parameter und die vom Markt bestimmten Parameter gemeinsam ein.
- Die Ausfallwahrscheinlichkeit der Strategie ergänzt die Probabilistic Sharpe Ratio, weil der Manager damit die Lebensfähigkeit unter seinen Schwellen und seiner Wettfrequenz prüfen kann.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]

## Verwandte Themen
