---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/20 - Trading-Performance & Auswertung/20 - Trading-Performance & Auswertung|20 - Trading-Performance & Auswertung]]"
weitere_hauptthemen: []
unterthema: "Risikoadjustierte Kennzahlen"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Information Ratio


## Kurzdefinition

- Die Information Ratio ist das Gegenstück zur Sharpe Ratio für eine Performance gegenüber einer Benchmark.

## Kernaussagen

- Montiers künstliches Universum besteht aus 100 Fondsmanagern mit echtem Alpha von 3 Prozent und einem Tracking Error von 6 Prozent, also einer Information Ratio von 0,5.
- Nach Grinold und Kahn (2000) liegt eine Information Ratio von 0,5 im oder nahe am oberen Viertel aktiver US-Aktienmanager.
- Die Perzentile der Information Ratio US-amerikanischer aktiver Aktien-Publikumsfonds lauten vor und nach Gebühren: 90. Perzentil 1,33 und 1,08, 75. Perzentil 0,78 und 0,58, 50. Perzentil 0,32 und 0,12, 25. Perzentil minus 0,08 und minus 0,33, 10. Perzentil minus 0,47 und minus 0,72.
- Dieselben Perzentile für institutionelle Portfolios lauten vor und nach Gebühren: 90. Perzentil 1,25 und 1,01, 75. Perzentil 0,63 und 0,48, 50. Perzentil minus 0,01 und minus 0,15, 25. Perzentil minus 0,56 und minus 0,72, 10. Perzentil minus 1,03 und minus 1,25.
- Kahn (2002): Plan-Sponsoren brauchen, im Unterschied zu dem, was sie sich wünschen, beständige Outperformance, gemessen an der Information Ratio.
- Wenig Erkenntnis über ein weites Universum und mit vernünftiger Häufigkeit übersetzt sich in eine hohe Information Ratio. Kombinationen aus Informationskoeffizient und Breite, die eine Information Ratio von 0,5 erzeugen, entsprechen einem Manager im oberen Viertel.
- Ein Manager mit Informationskoeffizient 0,035, also rund 51 Prozent richtigen Calls, der 200 Aktien folgt und etwa einmal je Quartal eine neue Entscheidung trifft, hat 800 Sichten im Jahr und eine Information Ratio von 0,99, oberes Zehntel.
- Die Cheap-Country-Strategie erzeugte einen Informationskoeffizienten von etwa 0,17, gleich ob das untere Tritil oder der Markt die Basis war. Die Ex-post-Information-Ratio lag bei 1,05 für das Long-only-Portfolio und bei 0,8 für das Long-Short-Portfolio, beide deutlich über den Ex-ante-Maßen.
- Das taktische Allokationsmodell hat eine Ex-ante-Information-Ratio von 0,42 und eine realisierte von 1,1.
- Shorten kann die Information Ratio der Strategie erhöhen. Wie eng die Long-only-Beschränkung bindet, hängt vom erlaubten Tracking Error ab. Bei 3 Prozent Tracking Error kann der Manager in keine Richtung große Wetten eingehen.
- US-Aktien gegenüber Cash haben eine Information Ratio von 0,37. In den dismal years lagen die Information Ratios bei 0,24 für Value plus Momentum, bei −0,07 für nur Value und bei 0,73 für nur Momentum.
- Shorten verbessert potenziell die Information Ratio, weil die volle Informationsmenge genutzt wird. Bei 3 Prozent Tracking Error kann der Manager in keine Richtung große Wetten eingehen, deshalb muss die Benchmark-Fixierung enden.
- Die Ex-ante-Information-Ratio wird hier als Anteil richtiger Calls mal der Wurzel der Breite beschrieben. Billige Länder hatten einen Informationskoeffizienten von etwa 0,17. Ex post lag die Information Ratio bei 1,05 long only und bei 0,8 long/short, beide deutlich darüber. Das taktische Modell hat ex ante 0,42 und realisiert 1,1.
- Die Breite einer Buch-zu-Preis-Strategie über 800 Aktien mit vierteljährlicher Neugewichtung ist nicht 800, weil die Sichten je Aktie nicht unabhängig sind. Sie ist größer als vier, die Zahl der Neugewichtungen im Jahr.
- Dieselbe Erkenntnis in vielen Märkten erhöht die gezählte Breite und ist trotzdem keine Diversifikation, wie LTCM zeigte, das eine Konvergenzidee geografisch vervielfachte.
- US-Aktien gegenüber Cash haben eine Information Ratio von 0,37, billige Länder eine Haltedauer von sechs Jahren und das taktische Modell von sieben Jahren, bis die Ex-ante-Information-Ratio 90 Prozent Sicherheit gegenüber der Benchmark bedeutet. Für Aktien gegen Cash sind es 14 Jahre.

## Funktionsweise

- Die Information Ratio ist das annualisierte Verhältnis der mittleren Überschussrendite zum Tracking Error.
- Die Überschussrendite ist die Portfoliorendite abzüglich der Benchmarkrendite.
- Der Tracking Error ist die Standardabweichung der Überschussrenditen.
- Der Informationskoeffizient misst die Korrelation zwischen den Prognosen des Modells und den Ergebnissen und ist definiert als 2 mal (f minus 0,5), wobei f der Anteil der richtig vorhergesagten Calls ist.
- Die Information Ratio verbindet den Informationskoeffizienten, die Erkenntnis des Modells oder Managers, mit der Zahl der Gelegenheiten, diese Erkenntnis anzuwenden.
- Technisch ist die Information Ratio der Informationskoeffizient mal der Quadratwurzel der Breite.
- Die Ex-post-Information-Ratio ist das Verhältnis der annualisierten Residualrendite zum annualisierten Residualrisiko, gleich dem Verhältnis von Alpha zu seinem Standardfehler, geteilt durch die Wurzel aus der Zahl der Beobachtungsperioden T.
- Grinold (1989) nennt das Fundamentalgesetz des aktiven Managements: Die Information Ratio ist der Informationskoeffizient mal der Wurzel aus der Breite. Die Breite hat zwei Dimensionen und ist das Produkt aus der Zahl der abgedeckten Assets und der Zahl der unabhängigen Entscheidungen.
- Die Ex-ante-Information-Ratio wird in der Länderstudie als Anteil richtiger Calls mal der Wurzel der Breite beschrieben. Sie lag dort deutlich unter den realisierten Information Ratios.

## Voraussetzungen


## Anwendung im Trading

- In der Attribution kann je Risikoklasse eine Sharpe Ratio oder eine Information Ratio berechnet werden.
- Der passende Vergleichsmaßstab einer Long-only-Strategie ist die Rendite einer Buy-and-hold-Position, also die Information Ratio und nicht die Sharpe Ratio.
- Die Long-only-Rohöl-Futures-Strategie von 2007 mit 20 Prozent Rendite und einer Sharpe Ratio von 1,5 war dem Halten des Front-Month-Kontrakts mit 47 Prozent und einer Sharpe Ratio von 1,7 nicht überlegen.

## Regeln und Kriterien

- Kahn (2002): eine Information Ratio über 0,5 liegt im oberen Viertel aktiver Manager, eine Information Ratio über 1 im oberen Zehntel.
- Alle ausgewiesenen Information Ratios der Länderstrategien gelten als höchst respektabel.

## Risiken und Grenzen


## Beispiele

- Das gleich gewichtete Long/Short-Portfolio auf das zehnjährige Graham-und-Dodd-Kurs-Gewinn-Verhältnis hat 1980 bis 2005 eine Information Ratio von 1,4 gegen den Markt und von 1,3 gegen den Value-Index und läge damit im obersten Dezil aktiver Manager.
- Das Long-only-Portfolio derselben Kennzahl hat eine Information Ratio von 0,8 gegen den Markt und von 0,7 gegen den Value-Index und läge damit im obersten Quartil aktiver Aktienmanager.
- Der Dividendenrendite-Länderkorb 1975 bis 2003 hat einen Anteil richtiger Calls von 0,59, einen Informationskoeffizienten von 0,17 und eine Information Ratio von 0,60.
- Der Kurs-Buchwert-Länderkorb hat einen Anteil richtiger Calls von 0,56, einen Informationskoeffizienten von 0,13 und eine Information Ratio von 0,44.
- Der Momentum-Länderkorb hat eine Information Ratio von 1,19, einen Informationskoeffizienten von 0,34 und 67 Prozent richtige Calls.
- Der Kurs-Gewinn-Länderkorb hat eine Information Ratio von 0,46, einen Informationskoeffizienten von 0,13 und 57 Prozent richtige Calls.
- Die erneut ausgewiesene Dividendenrendite hat eine Information Ratio von 0,60, einen Informationskoeffizienten von 0,17 und 59 Prozent richtige Calls.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 33–51 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-003-p033-p051|S. 33–51]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 191–210 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-011-p191-p210|S. 191–210]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 248–267 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-014-p248-p267|S. 248–267]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 267–286 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-015-p267-p286|S. 267–286]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 343–362 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-019-p343-p362|S. 343–362]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 419–438 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-023-p419-p438|S. 419–438]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 438–457 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-024-p438-p457|S. 438–457]]

## Verwandte Themen
