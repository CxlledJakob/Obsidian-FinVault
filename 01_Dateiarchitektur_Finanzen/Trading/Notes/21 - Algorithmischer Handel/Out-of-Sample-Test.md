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
- Der Backtest einer veröffentlichten Strategie erlaubt einen echten Out-of-Sample-Test in der Zeit nach der Veröffentlichung. Fällt er schwach aus, besteht die Sorge, dass die Strategie nur auf einem begrenzten Datensatz funktioniert hat. Dieser Punkt ist wichtiger, als viele annehmen.
- Viele Autoren schreiben, die Backtest-Ergebnisse seien mit Out-of-Sample-Daten verifiziert. Waren diese Ergebnisse schwach, konnten sie Parameter ändern oder das Modell so nachziehen, dass es auf den sogenannten Out-of-Sample-Daten gut aussieht. Echter Out-of-Sample-Test beginnt erst, wenn die Strategie veröffentlicht und festgeschrieben ist.
- Data-Snooping wird erkannt, indem das Modell auf Out-of-Sample-Daten getestet und bei Misserfolg verworfen wird. Nachjustieren, bis beide Teile gut aussehen, verwandelt die Out-of-Sample-Daten in In-Sample-Daten.
- Wer ein Modell wegen eines festen Out-of-Sample-Satzes nicht verwerfen will, weil die schwache Leistung Pech sein kann, oder wer einen kleinen Datensatz fast vollständig zum Justieren braucht, soll Cross-Validation erwägen.
- Der abschließende echte Out-of-Sample-Test ist ein Walk-Forward-Test. Er kann als Paper Trading laufen, besser aber mit echtem Geld bei minimalem Hebel.
- Die meisten Trader wären zufrieden, wenn der Live-Handel eine Sharpe Ratio besser als die Hälfte des Backtest-Wertes erzeugt.
- Out-of-Sample-Tests, Cross-Validation und hohe Sharpe Ratios sind gute Praktiken, um Data-Snooping-Bias zu mindern. Maßgeblicher ist der Walk-Forward-Test.
- Dass eine Momentum-Strategie vor 2008 gut abschnitt, bedeutet nicht, dass sie danach gut abschneidet, selbst wenn der Backtest ohne erkennbare Fallstricke ist.
- Weil das Backtest-Ergebnis vom konkreten Parametersatz abhängt, ist eine Reihe, die den Stationaritätstest besteht oder eine kurze Halbwertszeit hat, die sicherere Grundlage dafür, dass sich überhaupt eine profitable Strategie finden lässt.
- Schoenberg und Corwin zeigen, dass Scaling-in in der Stichprobe nie optimal ist, außer Stichprobe aber besser abschneiden kann als die All-in-Methode.
- entryZscore, der Lookback und die Zahl N der Bänder sind freie Parameter, die auf einem Trainingsset optimiert werden; der Lookback kann stattdessen gleich der Halbwertszeit gesetzt werden.
- Das optimale δ des Kalman-Filters wird aus Trainingsdaten bestimmt, analog zum optimalen Lookback einer gleitenden Regression.
- Aktienpaare kointegrieren selten out of sample: in einem gewählten Zeitraum ist Kointegration leicht zu finden und in der folgenden Out-of-Sample-Periode leicht wieder zu verlieren.
- Das Gesetz der großen Zahlen hilft einem Portfolio vieler Paare nur, wenn die erwartete Rendite eines einzelnen Paars in der Out-of-Sample-Periode positiv ist; der Autor hat das bei Aktienpaaren nicht gefunden.
- ETF-Paare, die einmal kointegrieren, fallen in Out-of-Sample-Daten seltener auseinander als Aktienpaare, weil sich die Ökonomie eines Korbs langsamer ändert als die einer einzelnen Firma.
- Wegen weniger Trades und langer Haltedauern droht in diesen Momentum-Ergebnissen Data Snooping, und der eigentliche Test ist echtes Out-of-Sample-Testing.

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

- Auf dem Testset vom 29. Juli 2010 bis zum 8. Mai 2012 beträgt die annualisierte Rendite der Bollinger-Band-ähnlichen Mean-Reversion-Strategie 12,3 Prozent bei einer Sharpe Ratio von 1,4.

## Regeln und Kriterien

- Statt eines einzelnen historischen Datensatzes folgt der Test dem Backtesting-Paradigma aus Kapitel 13, um Selection Bias aus Kapitel 11 zu vermeiden.
- Die Regressionskoeffizienten von ES auf VX werden nur auf den ersten 500 Tagen nach August 2008 geschätzt, damit die daraus gewonnenen Statistiken anschließend das Handelsmodell bauen.

## Risiken und Grenzen

- Die Varianzreduktion außer Stichprobe ist für Risk-Parity-Investoren wegen erheblichen Hebels kritisch.
- Jedes CLA-Rebalancing verursacht Transaktionskosten, die sich zu prohibitiven Verlusten summieren können.
- Bailey und Koautoren (2014) diskutieren den Unterschied zwischen Performance in und außer Stichprobe breiter.
- Werden In-Sample-Daten zugleich zur Optimierung der Parameter und zur Messung der Performance verwendet, blähen sich die Ergebnisse auf.
- Dieser Fallstrick steht in den Beispielen, weil die vereinfachte Fassung anschaulicher und lesbarer ist. Solche Prototyp-Strategien sind nicht zum Handel unverändert gedacht.
- Die Halbwertszeit und damit der Lookback der linearen USD.CAD-Strategie werden an denselben In-Sample-Daten bestimmt, auf denen die Strategie ausgewertet wird.
- Dieselben Daten für diese Optimierung und für den Backtest zu verwenden, ist Look-ahead Bias.
- Die im Text gesetzten Werte, 20 Tage für GLD und USO sowie δ gleich 0,0001 und Ve gleich 0,001, sind mit Wissen im Nachhinein gewählt.
- Die Aufgabe des Traders ist, besondere Bedingungen oder Perioden zu finden, in denen Mean Reversion regelmäßig auftritt, und dabei Data-Snooping-Bias zu vermeiden.

## Beispiele

- Abbildung 11.1 stellt die In-Sample-Sharpe-Ratio der besten ausgewählten Strategie der Out-of-Sample-Sharpe-Ratio derselben Strategie gegenüber und zeigt einen starken, anhaltenden Abfall durch Backtest-Overfitting.
- In dieser Abbildung beträgt die Wahrscheinlichkeit, dass die Out-of-Sample-Sharpe-Ratio negativ ist, 0,74.
- Die Anpassung in der Abbildung lautet: die Out-of-Sample-Sharpe-Ratio ist 0,87 minus 0,75 mal die In-Sample-Sharpe-Ratio plus einen Fehler, bei einem adjustierten R² von 0,17.
- Abbildung 11.2 weist für diese Strategieauswahl eine Probability of Overfit von 0,74 aus.
- Trainiert man auf 2009 bis 2017 und testet auf 2008, ist die Leistung für 2008 kein historisch genauer Out-of-Sample-Pfad, weil der Klassifikator Daten verwendet, die erst nach 2008 verfügbar waren.
- GLD gegen GDX kointegriert vom 23. Mai 2006 bis 14. Juli 2008 mit 99 Prozent und hat die Kointegration vom 15. Juli 2008 bis 9. April 2012 verloren.
- Die SPY-Komponenten-Arbitrage trainiert vom 1. Januar 2007 bis 31. Dezember 2007 und testet vom 2. Januar 2008 bis 9. April 2012.
- Die Performance des linearen Long-Short seit Anfang 2008 ist ein echter Out-of-Sample-Test, weil die Strategie 2007 veröffentlicht wurde.
- Der Look-back von 5 für Mittel und Standardabweichung der SPY-Arbitrage ist mit dem Vorteil des Hindsight festgelegt.
- Die annualisierte Rendite von 6,9 Prozent und die Sharpe Ratio von 1 der VX-ES-Rollrendite-Strategie gelten für den 29. Juli 2010 bis zum 7. Mai 2012, und dieser Zeitraum wurde nicht zur Bestimmung der Hedge Ratio verwendet.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 20–39 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-002-p020-p039|S. 20–39]]
- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 248–267 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-014-p248-p267|S. 248–267]]
- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 1–20 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-001-p001-p020|S. 1–20]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 58–77 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-004-p058-p077|S. 58–77]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 115–134 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-007-p115-p134|S. 115–134]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 134–153 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-008-p134-p153|S. 134–153]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 248–267 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-014-p248-p267|S. 248–267]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 267–286 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-015-p267-p286|S. 267–286]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 286–305 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-016-p286-p305|S. 286–305]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 305–324 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-017-p305-p324|S. 305–324]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 381–400 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-021-p381-p400|S. 381–400]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 457–476 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-025-p457-p476|S. 457–476]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 476–495 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-026-p476-p495|S. 476–495]]

## Verwandte Themen
