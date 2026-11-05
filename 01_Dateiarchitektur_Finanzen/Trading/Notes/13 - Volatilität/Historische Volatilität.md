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

# Historische Volatilität


## Kurzdefinition

- Chang und Osler definieren die Volatilität V eines Marktes als die Standardabweichung der täglichen prozentualen Preisänderungen über die jüngsten 100 Handelstage.

## Kernaussagen

- Die herkömmliche Varianz ist σ²_t = E[(C_t − C_{t−1})² | F_{t−1}], mit C_t als Schlusskurs des t-ten Handelstags und F_{t−1} als der öffentlich verfügbaren Information.
- French, Schwert und Stambaugh (1987) schätzen die Volatilität niederfrequenter Renditen aus hochfrequenten Daten.
- Sind die Tages-Logrenditen weißes Rauschen, ist die bedingte Monatsvarianz n mal die Varianz einer Tagesrendite. Der Schätzer lautet σ̂²_m = [n/(n−1)] Σ_{i=1}^{n} (r_{t,i} − r̄_t)².
- Folgen die Tagesrenditen einem MA(1), kommt 2(n−1) Cov(r_{t,1}, r_{t,2}) hinzu. Geschätzt wird das durch die Summe der Produkte benachbarter, um den Monatsmittelwert zentrierter Tagesrenditen.
- Ein Monat hat grob 21 Handelstage. Die Stichprobe für Varianz und Kovarianz ist klein, und die Genauigkeit hängt von der Dynamik und der Verteilung der Tagesrenditen ab.
- Wird der Stichprobenmittelwert der Tagesrenditen null gesetzt, schätzt die Summe der quadrierten Tages-Logrenditen eines Monats die Monatsvolatilität.
- Für die Logrenditen des S&P 500 von Januar 1980 bis Dezember 1999 liegen die aus Tagesrenditen geschätzten Monatsvolatilitäten deutlich über denen eines GARCH(1,1) auf Monatsrenditen von Januar 1962 bis Dezember 1999. Für Oktober 1987 beträgt die Schätzung aus Tagesrenditen etwa 680.
- Garman und Klass (1980) definieren den Effizienzfaktor eines historischen Schätzers als das Verhältnis der Varianz des Schluss-zu-Schluss-Schätzers zur Varianz des jeweiligen Schätzers. Unter einem einfachen Diffusionsmodell ohne Drift beträgt er näherungsweise 2, 5,2, 6,2, 7,4 und 8,4 für ihre Schätzer i = 1, 2, 3, 5 und 6.
- Die gleichgewichtete Schätzung der Kovarianz vergangener Innovationen gibt jedem äußeren Produkt das Gewicht 1 durch (t minus 1) und setzt den Mittelwert der Innovationen auf null.
- Die exponentiell gewichtete Glättung verlagert das Gewicht auf die jüngeren Innovationen und dient als Benchmark der multivariaten Volatilitätsschätzung. Für Hang Seng und Nikkei 225 ist der Glättungsparameter etwa 0,9305. Die resultierenden Volatilitätsreihen sind glatter als die univariaten GARCH(1,1)-Reihen, bei ähnlichem Muster.
- Die rollierende Kovarianzschätzung im Beispiel von Euro, Yen, IBM und Dell benutzt ein Fenster von 69 Tagen, ungefähr die Zahl der Handelstage eines Quartals. Sie reagiert auf große Innovationen langsamer als das DCC-Modell: Anstieg und Abklingen der Modellvolatilität sind schneller.
- Die Stichprobenkorrelation der monatlichen Logrenditen von IBM und dem S&P 500 wird mit einem gleitenden Fenster von 120 Beobachtungen, also 10 Jahren, von Januar 1926 bis Dezember 1999 berechnet. Sie verändert sich über die Zeit und fällt in den jüngeren Jahren.

## Funktionsweise

- µ und σ der geometrischen Brownschen Bewegung werden aus n + 1 gleichabständigen Preisen geschätzt; Δ wird in Jahren gemessen, und rt = ln(Pt) − ln(Pt−1) ist die stetig verzinste Rendite im t-ten Intervall.
- Unter der geometrischen Brownschen Bewegung ist rt normal mit Mittel (µ − σ²/2)Δ und Varianz σ²Δ und nicht seriell korreliert.
- Mit Stichprobenmittel r̄ und Stichproben-Standardabweichung sr gilt σ̂ = sr/√Δ; der Standardfehler dieser Schätzung ist ungefähr σ̂/√(2n).
- Der Drift wird geschätzt als µ̂ = r̄/Δ + σ̂²/2 = r̄/Δ + sr²/(2Δ); r̄ und sr sind konsistente Schätzer von Mittel und Standardabweichung der Rendite.
- Ist rt seriell korreliert oder folgt der Preis nicht der geometrischen Brownschen Bewegung, sind andere Schätzverfahren für Drift und Volatilität nötig.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Die zehn Zigzag-Schwellen entstehen, indem V mit den Koeffizienten 1,5, 2,0, 2,5, 3,0, 3,5, 4,0, 4,5, 5,0, 5,5 und 6,0 multipliziert wird.
- Eine Schwellenmenge, die für ein Instrument gut ist, muss für ein anderes nicht gut sein, weil die Instrumente unterschiedliche Volatilität haben.
- Die Kopplung der Schwellen an V erlaubt, den Schulter-Kopf-Schulter-Algorithmus über Märkte mit verschiedener Volatilität zu verallgemeinern.
- Die Tauglichkeit der gewählten Koeffizienten wurde durch Sichtprüfung von Charts durch Praktiker der Technischen Analyse bestätigt, die übereinstimmten, dass die zehn Filter Schulter-Kopf-Schulter-Muster vernünftig erkennen.

## Risiken und Grenzen


## Beispiele

- Für IBM 1998, 252 Tagesrenditen, r̄ = 0,002276 und sr = 0,01915, bei Δ = 1/252, ergeben sich σ̂ = 0,3040 und µ̂ = 0,6198, also 30,4 Prozent Standardabweichung und 61,98 Prozent erwartete Rendite pro Jahr.
- Für Cisco Systems 2007, 251 Beobachtungen, Mittel −3,81×10^−5 und Standardabweichung 0,0174, ergeben sich σ̂ = 0,0174 / √(1/251) = 0,275 und µ̂ = −0,0094.
- Für Cisco Systems 2007 beträgt die aus den Tages-Logrenditen geschätzte Standardabweichung 27,5 Prozent pro Jahr, bei einer geschätzten erwarteten Logrendite von −0,94 Prozent pro Jahr.
- Die Stichproben-Standardabweichung der stetig verzinsten Tagesrendite des Wechselkurses D-Mark/US-Dollar betrug im Juni 1997 etwa 0,53 Prozent und wird dort als Volatilität in die VaR-Rechnung eingesetzt.
- Für die täglichen IBM-Logrenditen 1997 gibt Übung 6.3 eine durchschnittliche Rendite von 0,00131 und eine Stichproben-Standardabweichung von 0,02215 an, bei 252 Handelstagen.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 153–172 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-009-p153-p172|S. 153–172]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 191–210 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-011-p191-p210|S. 191–210]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 305–324 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-017-p305-p324|S. 305–324]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 324–343 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-018-p324-p343|S. 324–343]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 343–362 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-019-p343-p362|S. 343–362]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 514–533 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-028-p514-p533|S. 514–533]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 533–552 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-029-p533-p552|S. 533–552]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 552–571 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-030-p552-p571|S. 552–571]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 381–400 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-021-p381-p400|S. 381–400]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 457–476 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-025-p457-p476|S. 457–476]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 609–628 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-033-p609-p628|S. 609–628]]

## Verwandte Themen
