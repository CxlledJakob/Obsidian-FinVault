---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Systementwicklung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Out-of-Sample-Test


## Kurzdefinition

- Ein Backtest bewertet out-of-sample die Leistung einer Anlagestrategie anhand vergangener Beobachtungen.
- In-sample sind die Gelegenheiten von 1 bis I, und out of sample sind die späteren Gelegenheiten von I plus 1 bis J.
- Der Out-of-Sample-Test prüft, ob das Portfolio mit minimaler Varianz in der Stichprobe auch außer Stichprobe die geringste Varianz hat.

## Kernaussagen

- Ein in der Stichprobe optimales Verfahren kann außerhalb der Stichprobe schlecht abschneiden.
- Für Anlageerfolg gibt es keinen mathematischen Beweis.
- Die Forschung soll sich auf experimentelle Methoden stützen.
- Die Branche bezahlt nur für Out-of-Sample-Renditen.
- Erfolg tritt erst ein, nachdem für die Anleger substanzielles Vermögen entstanden ist.
- Mittel sind den Strategien mit einem robusten Verfahren zuzuweisen, das außerhalb der Stichprobe gut funktioniert.
- Robuste Allokation darf In-Sample-Signale nicht auf Kosten der Out-of-Sample-Performance überanpassen.
- Die Machine-Learning-Asset-Allokation umfasst als eigenen Abschnitt Out-of-Sample-Monte-Carlo-Simulationen.
- Gesucht ist ein echtes Out-of-Sample-Verfahren, das das Modell an den Beobachtungen bewertet, die am wenigsten mit den zum Training verwendeten Beobachtungen korreliert oder redundant sind.
- Beim Walk-Forward ist Geschichte eine Filtration, und nachlaufende Daten garantieren ein Out-of-Sample-Testset ohne Leakage, sofern das Purging korrekt umgesetzt ist.
- Das Ziel der Backtest-Cross-Validation ist, künftige Leistung aus einer Reihe von Out-of-Sample-Szenarien zu erschließen, nicht eine historisch genaue Performance abzuleiten.
- Für jeden Zeitraum wird die Leistung eines Klassifikators simuliert, der alles außer diesem Zeitraum kannte.
- Jede Beobachtung gehört bei dieser Cross-Validation zu genau einem Testset, es gibt kein Aufwärm-Subset, und die Out-of-Sample-Simulation wird so lang wie möglich.
- Das CV-Ergebnis simuliert nicht, wie die Strategie in der Vergangenheit gelaufen wäre, sondern wie sie künftig unter verschiedenen Stressszenarien abschneiden kann.
- Eine in-sample optimale Handelsregel ist überangepasst, wenn ihre erwartete Out-of-Sample-Sharpe-Ratio unter dem Median der alternativen Regeln liegt.
- Der Backtest verdient dann am Rauschen der Stichprobe, und die Regel ist für die späteren Gelegenheiten ungeeignet.
- Serielle Abhängigkeit der Gewinnänderungen dreht das Overfitting in eine negative Out-of-Sample-Performance.
- Synthetische Testmengen bleiben für die Regel ungesehen und binden sie weniger an eine bestimmte Stichprobe.
- Das Minimum-Varianz-Portfolio in der Stichprobe ist nicht notwendig das mit minimaler Varianz außer Stichprobe.
- Im Zahlenbeispiel hat CLA in der Stichprobe die geringere Standardabweichung, 0,4486 gegen 0,4640, außer Stichprobe aber die höchste Varianz.
- CLA erzeugt das Minimum-Varianz-Portfolio in der Stichprobe, weil das seine Zielfunktion ist.
- Monte-Carlo-Experimente zeigen für Hierarchical Risk Parity eine geringere Varianz außer Stichprobe als für CLA und für das Inverse-Varianz-Portfolio.
- Die Varianzen außer Stichprobe betragen 0,1157 für CLA, 0,0928 für das Inverse-Varianz-Portfolio und 0,0671 für Hierarchical Risk Parity.
- Damit verbessert Hierarchical Risk Parity die Sharpe-Ratio einer CLA-Strategie außer Stichprobe um etwa 31,3 Prozent, weil die mittleren Renditen im Wesentlichen 0 sind.
- Naive gleichgewichtete Portfolios haben nach De Miguel und Koautoren (2009) Mean-Variance- und risikobasierte Optimierung außer Stichprobe geschlagen.
- Gespeichert wird je Iteration die kumulierte Rendite außer Stichprobe am Pfadende minus eins.
- Berichtet werden Standardabweichung, Varianz und die Varianz im Verhältnis zu Hierarchical Risk Parity.

## Funktionsweise

- In der combinatorially symmetric cross-validation ist der relative Rang der out-of-sample Performance jener Variante, die in-sample als beste gewählt wurde, eine Zahl in (0, 1).
- Ohne Overfitting sollte diese Variante out-of-sample systematisch besser abschneiden als die übrigen Testvarianten, so wie sie es in-sample tat.
- Der Logit dieses Rangs ist 0, wenn die in-sample beste Variante dem Median der Out-of-Sample-Performances entspricht.
- Hohe Logits bedeuten Übereinstimmung zwischen In-Sample- und Out-of-Sample-Leistung und damit geringes Backtest-Overfitting.
- Die Probability of Backtest Overfitting ist die Wahrscheinlichkeit, dass in-sample optimale Strategien out-of-sample unter dem Median liegen, also das Integral der Logit-Dichte von minus unendlich bis 0.
- Im Monte-Carlo-Code werden die Portfolios auf dem Fenster vor dem Zeiger in der Stichprobe geschätzt.
- Die Renditen außer Stichprobe werden auf den folgenden Rebalancing-Beobachtungen berechnet.
- Die Zeiger laufen vom Ende des Rückblicks bis zum Stichprobenende in Schritten der Rebalancing-Länge, sodass der erste Abschnitt nur der Schätzung dient.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Statt eines einzelnen historischen Datensatzes folgt der Test dem Backtesting-Paradigma aus Kapitel 13, um Selection Bias aus Kapitel 11 zu vermeiden.

## Risiken und Grenzen

- Die Varianzreduktion außer Stichprobe ist für Risk-Parity-Investoren wegen erheblichen Hebels kritisch.
- Jedes CLA-Rebalancing verursacht Transaktionskosten, die sich zu prohibitiven Verlusten summieren können.
- Bailey und Koautoren (2014) diskutieren den Unterschied zwischen Performance in und außer Stichprobe breiter.

## Beispiele

- Abbildung 11.1 stellt die In-Sample-Sharpe-Ratio der besten ausgewählten Strategie der Out-of-Sample-Sharpe-Ratio derselben Strategie gegenüber und zeigt einen starken, anhaltenden Abfall durch Backtest-Overfitting.
- In dieser Abbildung beträgt die Wahrscheinlichkeit, dass die Out-of-Sample-Sharpe-Ratio negativ ist, 0,74.
- Die Anpassung in der Abbildung lautet: die Out-of-Sample-Sharpe-Ratio ist 0,87 minus 0,75 mal die In-Sample-Sharpe-Ratio plus einen Fehler, bei einem adjustierten R² von 0,17.
- Abbildung 11.2 weist für diese Strategieauswahl eine Probability of Overfit von 0,74 aus.
- Trainiert man auf 2009 bis 2017 und testet auf 2008, ist die Leistung für 2008 kein historisch genauer Out-of-Sample-Pfad, weil der Klassifikator Daten verwendet, die erst nach 2008 verfügbar waren.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 20–39 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-002-p020-p039|S. 20–39]]
- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 248–267 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-014-p248-p267|S. 248–267]]
- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]

## Verwandte Themen
