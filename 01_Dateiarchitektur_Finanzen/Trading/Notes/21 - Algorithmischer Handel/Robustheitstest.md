---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Validierung"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Robustheitstest


## Kurzdefinition


## Kernaussagen

- Die Analyse wurde sowohl in Preisen als auch in Gesamtrenditen gerechnet, und die Ergebnisse waren gegenüber dieser Spezifikation invariant.
- Ähnliche Muster zeigten sich in den regionalen Aufteilungen; Abbildung 26.2 zeigt eine stark konsistente Value-Prämie über die untersuchten Länder und Regionen beim Kauf der untersten 20 Prozent nach trailing PE.
- Der Anteil der niedrigsten KGV-Aktien mit relativer Underperformance beträgt global 30 Prozent, in den USA 57 Prozent, in Europa 32 Prozent und in Japan 35 Prozent.
- Keines der Value-Portfolios erzeugt eine negative absolute Rendite; Tabelle 26.3 weist für Global, USA, Europa und Japan jeweils 0 Prozent aus.
- Die gleich gewichtete Low-PE-Outperformance von 9,7 Prozent pro Jahr bleibt bestehen, wenn die Renditen mit der tatsächlichen Verteilung der Firmen gewichtet werden; dann liegt die Outperformance bei fast 6 Prozent pro Jahr.
- Vom erreichbaren Wachstum der Perfect-Foresight-Strategie fangen hohe Analystenprognosen global 24 Prozent, in Europa 41 Prozent, in den USA 70 Prozent und in Japan minus 220 Prozent ein.
- Nur in den USA übersteigt die Rendite aus den Wachstumsprognosen der Analysten die Rendite aus billigen Aktien; risikobereinigt schlägt Value dort trotzdem, weil die Standardabweichung 17,7 Prozent gegen 25,1 Prozent beträgt.
- Die Little-Book-Strategie wird in den USA, in Europa ohne Großbritannien, in Großbritannien und in Japan von 1993 bis 2005 geprüft und ist damit kein reiner US-Befund: sie schlägt den Markt in allen vier Regionen bei niedrigerer Volatilität.
- Das gleich gewichtete Long/Short-Portfolio auf das zehnjährige Graham-und-Dodd-Kurs-Gewinn-Verhältnis hat selbst in der Technologieblase kein einziges negatives Jahr.
- Die Differenz zwischen niedrigem und hohem Kurs-Gewinn-Dezil steigt über die Fenster von einem, drei, fünf, sieben und zehn Jahren monoton auf 11, 15, 18, 22 und 25 Prozentpunkte p.a. und hängt damit nicht an einem einzelnen Fenster.
- Der Test in Europa ohne Großbritannien, in Großbritannien und in Japan ist ausdrücklich ein Robustheitscheck dafür, ob der Little-Book-Screen außerhalb der USA trägt.
- Die Nachbildung mit Standard-Earnings-Yield und Rendite auf die Aktiva liefert eine ähnliche Größenordnung und lässt die Little-Book-Befunde robust erscheinen.
- Die US-Dezilreihenfolge ist nicht monoton wie bei Greenblatt. Das kleinere Universum von rund 750 Titeln und einzelne Titel in einem Jahr schränken die glatte Dezilgeschichte ein.
- Ähnliche Renditen in Europa seit 1995, Value-Rückkäufe mit 5 % p.a. Überschuss und Growth-Emittenten mit 5 % p.a. Underperformance, stützen den US-Befund von Bali, Demirtas und Hovakimian und sprechen gegen einen reinen statistischen Zufall der europäischen Horizontverlängerung.
- Eine einfache Strategie mit wenigen Parametern ist eher über mehrere Symbole und mehrere Zeitebenen robust.
- Ein fest eingebauter Stop-Loss zerstört nach Ehlers' Erfahrung die Robustheit einer Strategie; nur als Schutz vor extrem großen Verlusten eingesetzt, bleibt die Robustheit der Kernstrategie erhalten.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Eine Faustregel verlangt mindestens 30 Trades pro Parameter der Strategie, bei vier Parametern also mindestens 120 Trades; Ehlers hält diese Zahl für eher zu niedrig.
- Liefert die Optimierung keinen sanften Gipfel über einen Bereich von Parametereinstellungen, ist die Strategie garantiert nicht robust.
- Bringt der Out-of-Sample-Test ohne Parameteränderung zufriedenstellende Ergebnisse, ist die Strategie robust.

## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 324–343 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-018-p324-p343|S. 324–343]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 343–362 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-019-p343-p362|S. 343–362]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 362–381 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-020-p362-p381|S. 362–381]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 216–235 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-016-p216-p235|S. 216–235]]

## Verwandte Themen
