---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/13 - Volatilität/13 - Volatilität|13 - Volatilität]]"
weitere_hauptthemen: []
unterthema: "Volatilitätsmessung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Intraday-Volatilität


## Kurzdefinition


## Kernaussagen

- Die Aktienvolatilität besteht aus Intraday-Volatilität und Overnight-Volatilität; letztere ist die Schwankung zwischen den Handelstagen.
- Hochfrequente Intraday-Renditen enthalten nur sehr begrenzte Information über die Overnight-Volatilität.
- Liegen Intraday-Daten vor, etwa Zehn-Minuten-Renditen, lässt sich die tägliche Volatilität schätzen; die Genauigkeit dieser Schätzung verdient eine sorgfältige Prüfung.
- Die zehnminütigen prozentualen Mark-Dollar-Änderungen vom 5. bis 19. Juni 1989 umfassen 2488 Beobachtungen, mit gelegentlich großen Änderungen und dazwischen ruhigen Abschnitten.
- Die Tages-Logrendite ist die Summe von n gleichabständigen Intraday-Logrenditen, r_t = Σ r_{t,i}. Die realisierte Volatilität ist RV_t = Σ r²_{t,i} und setzt eine iid-Folge mit Mittelwert null und endlicher Varianz voraus.
- Bei kleinem Abstand der Intraday-Renditen verzerren Mikrostruktureffekte, etwa der Bid-Ask-Bounce, die Volatilitätsschätzung. Für stark gehandelte US-Assets wird oft ein Intervall von 4 bis 15 Minuten verwendet.
- Die Overnight-Rendite vom Schluss von Tag t−1 zur Eröffnung von Tag t ist bei Aktien oft beträchtlich. Sie zu ignorieren kann die Volatilität ernsthaft unterschätzen. Begrenzte Erfahrung zeigt, dass Overnight-Renditen bei Index- und Devisenrenditen klein erscheinen.
- French, Schwert und Stambaugh (1987) berechnen die Volatilität niederfrequenter Renditen aus hochfrequenten Daten. Unter weißem Rauschen ist die bedingte Monatsvarianz n mal die Tagesvarianz; unter einem MA(1) kommt die Kovarianz benachbarter Tage hinzu.
- Für den S&P 500 von Januar 1980 bis Dezember 1999 sind die aus Tagesrenditen geschätzten Monatsvolatilitäten deutlich höher als ein GARCH(1,1) auf Monatsrenditen. Im Oktober 1987 liegt die Schätzung aus Tagesdaten bei etwa 680.
- Barndorff-Nielsen und Shephard (2004) nutzen Hochfrequenzrenditen für Bi-Power-Variationen und entwickeln Methoden, um Sprünge in der Volatilität zu erkennen.
- Haben die täglichen Logrenditen hohe Exzess-Kurtosis und serielle Korrelationen, können die Stichprobenschätzer der Monatsvolatilität aus den Tagesrenditen inkonsistent sein (Bai, Russell und Tiao, 2004). Ein Monat hat grob 21 Handelstage.
- Ein normaler Handelstag enthält 77 Fünf-Minuten-Renditen.
- Manche Forscher verwenden die Summe der Quadrate der Intraday-Fünf-Minuten-Renditen als Maß der Tagesvolatilität.
- Der Aktienpreis eines Fünf-Minuten-Intervalls kann als einfacher Durchschnitt aller Transaktionspreise in dem Intervall oder als letzter Transaktionspreis in dem Intervall gebildet werden.
- In der Konstruktion der Fünf-Minuten-Renditen aus den Boeing-Geschäften vom 1. bis 5. Dezember 2008 werden Übernachtrenditen ausgelassen; behalten werden nur Geschäfte von 9:30 bis 16:00 Uhr Eastern Time.
- Die tägliche realisierte Volatilität von Alcoa ist die Summe der quadrierten Logrenditen aus Intraday-Intervallen von 10 Minuten, gemessen in Prozent, vom 2. Januar 2003 bis 7. Mai 2004, 340 Tage.
- Übernachtrenditen und die Rendite der ersten 10 Minuten des Handelstags werden nicht verwendet. Die Transaktionen stammen aus der TAQ-Datenbank der NYSE.
- Die verwendete Reihe ist der Logarithmus dieser täglichen realisierten Volatilität. Sie wird aus Hochfrequenzdaten gebaut und ist Markt-Mikrostrukturrauschen ausgesetzt.
- Die Standardabweichung des Messfehlers et ist die Skala für die Wirkung dieses Mikrostrukturrauschens.
- Im angepassten lokalen Trendmodell ist die Messfehlerstreuung σe-Dach gleich 0,4803 größer als die Zustandsinnovation ση-Dach gleich 0,0735. Das bestätigt Messfehler in den hochfrequenten Intraday-Renditen.

## Funktionsweise

- Die Bekanntgabe läuft in sehr kurzer Zeit über die erste Zahl, oft eine Revision früherer Perioden und danach die Komponenten.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Eine große Meldung erzeugt oft eine heftige Reflexbewegung. Inhalt und Wirkung auf die Stimmung vorwegzunehmen ist ein hochriskantes Glücksspiel.
- Ist die Zahl draußen, läuft der Preis so heftig und schnell, dass eine rationale Entscheidung oder die gewünschte Location kaum noch möglich ist.
- Die daraus entstehenden vereinzelten Preissprünge können in Minuten einen beträchtlichen Teil des Kapitals vernichten.
- Während der Volatilität einer Meldung ist der Handel extrem schwierig.
- Im Niedrigvolumen der ein bis zwei Tage davor können Gerüchte und Prognosen den Preis wild rotieren lassen.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Mind Over Markets_ Power Trading with Market Generated Information, Updated Edition.pdf, S. 288–296 → [[Trading/Pilot/blocks/mind-over-markets/mind-over-markets-block-018-p288-p296|S. 288–296]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 134–153 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-008-p134-p153|S. 134–153]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 305–324 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-017-p305-p324|S. 305–324]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 571–590 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-031-p571-p590|S. 571–590]]

## Verwandte Themen
