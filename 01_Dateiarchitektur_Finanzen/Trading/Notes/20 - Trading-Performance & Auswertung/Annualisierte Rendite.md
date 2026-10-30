---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/20 - Trading-Performance & Auswertung/20 - Trading-Performance & Auswertung|20 - Trading-Performance & Auswertung]]"
weitere_hauptthemen: []
unterthema: "Renditekennzahlen"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Annualisierte Rendite


## Kurzdefinition

- Die annualisierte Rendite ist der zeitgewichtete durchschnittliche Jahresertrag einschließlich Dividenden, Kupons und Kosten.

## Kernaussagen

- Das Performancemaß dieses Buches ist die annualisierte durchschnittliche Tagesrendite auf trendbereinigten, um null zentrierten Marktdaten.
- Die Leistung einer Regel lässt sich auf viele Arten definieren. Verbreitet sind die durchschnittliche Rendite, die Sharpe Ratio und der Profit Factor.
- Die Performancehistorie einer künstlichen Handelsregel wird mit der Statistik mittlere Monatsrendite, annualisiert, zusammengefasst.
- Eine künstliche Regel mit Gewinnwahrscheinlichkeit 1,0 hat eine erwartete Monatsrendite von +3,97 Prozent, entsprechend einer nicht aufgezinsten annualisierten Rendite von 47,6 Prozent.
- Eine Gewinnwahrscheinlichkeit von null ergibt −3,97 Prozent pro Monat oder −47,6 Prozent pro Jahr.
- Die in den Experimenten aufgetragenen Data-Mining-Verzerrungen sind annualisierte prozentuale Renditen; die Kurve gegen die Regelzahl gilt für eine 24-Monats-Historie, die Kurve gegen die Regelkorrelation für 100 Monatsbeobachtungen.
- In den früheren Abbildungen ist die senkrechte Achse der Data-Mining-Bias in annualisierter prozentualer Rendite pro Jahr.
- In Abbildung 6.43 ist die senkrechte Achse dagegen die wahre Güte, also die erwartete Rendite der Regel mit der höchsten beobachteten Performance.
- Wird die beste aus 256 Regeln mit 1.000 Monaten Historie gewählt, beträgt ihre erwartete Rendite +10 Prozent im Jahr, weit über dem Universumsmittel von +1,4 Prozent pro Jahr.
- Bei nur zwei Monaten überzeichnet die beobachtete Performance der besten von 256 ihre erwartete Rendite um über 200 Prozent pro Jahr; bei 100 Monaten beträgt der Bias etwa 18 Prozent und bei 1.000 Monaten weniger als 3 Prozent.
- In den Abbildungen zur beobachteten und erwarteten Performance ist die senkrechte Achse die annualisierte Rendite; der senkrechte Abstand ist der Data-Mining-Bias, im Beispiel der besten von 10 bei 400 Monatsbeobachtungen.
- Der Populationsparameter der Fallstudie ist die erwartete durchschnittliche annualisierte Rendite einer Regel in der unmittelbaren praktischen Zukunft.
- Die Stichprobenstatistik ist die durchschnittliche annualisierte Rendite, die eine Regel auf den trendbereinigten Kursen des S&P 500 vom 1. November 1980 bis zum 1. Juli 2005 erzielt.
- Die Performancestatistik, mit der jede Regel bewertet wird, ist ihre durchschnittliche Rendite über 1980 bis 2005 im Backtest auf trendbereinigten S&P-500-Daten.
- Praktische Signifikanz hängt von den Zielen des Händlers ab. Einer kann mit einer erwarteten Rendite von 5 Prozent zufrieden sein, ein anderer lehnt jede Regel ab, deren erwartete Rendite unter 20 Prozent liegt.
- In Michael Coopers Walk-forward-Simulation auf 300 Large-Cap-Aktien von 1978 bis 1993 erzielten die Long-Short-Portfolios eine annualisierte Rendite von 44,95 Prozent gegen 17,91 Prozent für Buy-and-hold.
- Die beste Regel E-12-28-10-30 erzeugte auf trendbereinigten Marktdaten eine mittlere annualisierte Rendite von 10,25 Prozent.
- Die Stichprobenverteilungen von White’s Reality Check und der Monte-Carlo-Permutation zentrieren beide bei etwa 11 Prozent mittlerer Rendite.
- Die erwartete Rendite der besten von 6.402 konkurrierenden Regeln ohne Vorhersagekraft beträgt unter den konkreten Bedingungen der Fallstudie etwa 11 Prozent und nicht 0 Prozent.
- Dieser Wert von etwa 11 Prozent folgt aus dem Satz von 6.402 Regeln, ihren Renditekorrelationen, der Zahl der Beobachtungen für die Mittelwerte und dem verwendeten S&P-Datensatz.
- Die annualisierte Rendite von 10,25 Prozent liegt unter dem Zentrum der Stichprobenverteilung von 11 Prozent und damit im Bereich gewöhnlicher Stichprobenschwankung.
- Die Stichprobenverteilung der mittleren Rendite der besten von N Regeln, zum Beispiel N gleich 6.402, ist nicht bei null zentriert, sondern bei einem positiveren Wert, der die Verteilung des Maximums von N Mitteln abbildet.
- Annualisierte Renditen über 15 Prozent wären beim Signifikanzniveau 0,05 signifikant gewesen.
- Annualisierte Renditen über 17 Prozent wären hochsignifikant gewesen, mit einem p-Wert unter 0,001.
- In einem gewöhnlichen Signifikanztest, der den Data-Mining-Bias ignoriert, wäre die mittlere Rendite der besten Regel mit einem p-Wert von 0,0005 hochsignifikant erschienen; diese Einzelregel-Verteilung ist bei null zentriert.
- Tabelle 9.1 listet die mittlere Rendite auf trendbereinigten S&P-Daten; die erste und höchste ausgewiesene Rendite ist 0,102501 für die Regel E-12-28-10-30.
- Die zweite in Tabelle 9.1 genannte Rendite ist 0,102395 für die Regel D-8-4-10-60.
- Die ersten in Tabelle 9.1 genannten Grenzen des 80-Prozent-Konfidenzintervalls sind −0,02932 und 0,23527, neben der Rendite 0,102501 der Regel E-12-28-10-30.

## Funktionsweise

- Die Gesamtrendite einer Messperiode umfasst realisierte und nicht realisierte Gewinne und Verluste sowie aufgelaufene Zinsen, gezahlte Kupons und Dividenden.
- Nach den GIPS-Regeln wird die zeitgewichtete Rendite um externe Mittelzuflüsse und Mittelabflüsse bereinigt.
- Die Renditen der Teilperioden werden geometrisch verknüpft.
- Für Perioden seit Beginn des Jahres 2005 schreiben die GIPS-Regeln eine Bereinigung um täglich gewichtete externe Cashflows vor.
- Die Rendite einer Teilperiode ist der Mark-to-Market-Gewinn geteilt durch das in dieser Teilperiode gebundene Vermögen.
- Im Zähler stehen die Preisänderung und der aufgelaufene Ertrag auf den Anfangsbestand sowie das Ergebnis der Bestandsänderung.
- Im Nenner der Teilperiodenrendite steht der Marktwert des verwalteten Vermögens, und zusätzliche Käufe erhöhen diese Basis, damit ein Aufstocken finanziert ist.
- Zuflüsse werden am Tagesbeginn angesetzt und Abflüsse am Tagesende.
- Das Produkt aus eins plus Teilperiodenrendite ist der Endwert eines über die ganze Laufzeit investierten Dollars.
- Die annualisierte Rendite rechnet diesen Wachstumsfaktor auf die Jahre zwischen der ersten und der letzten Teilperiode um.

## Voraussetzungen

- Externe Cashflows sind Vermögen, das dem Portfolio zufließt oder es verlässt.
- Dividenden und Zinszahlungen gelten nicht als externe Cashflows.

## Anwendung im Trading

- Die lineare Mean-Reversion-Strategie auf dem CL-12-Monats-Kalenderspread erzielt vom 2. Januar 2008 bis zum 13. August 2012 eine ungehebelte annualisierte Rendite von 8,3 Prozent bei einer Sharpe Ratio von 1,3.
- Die übliche lineare Mean-Reversion-Strategie auf dem VX-Kalenderspread, mit dem Ratio als Signal und einem Lookback von 15 Tagen für gleitenden Durchschnitt und Standardabweichungen, erzielt vom 27. Oktober 2008 bis zum 23. April 2012 eine annualisierte Rendite von 17,7 Prozent bei einer Sharpe Ratio von 1,5.
- Dieselbe VX-Kalenderspread-Strategie schnitt vor Oktober 2008 deutlich schlechter ab.
- Die Bollinger-Band-ähnliche Mean-Reversion-Strategie auf dem stationären Portfolio aus ES und VX erzielt auf dem Testset vom 29. Juli 2010 bis zum 8. Mai 2012 eine annualisierte Rendite von 12,3 Prozent bei einer Sharpe Ratio von 1,4.
- Der Populationsparameter einer technischen Regel ist ihre erwartete Leistung über die unmittelbare praktische Zukunft. Gemessen wird sie in diesem Buch als annualisierte durchschnittliche Tagesrendite auf trendbereinigten, um null zentrierten Daten.

## Regeln und Kriterien

- Eine erwartete APR von 10 Prozent, die auf 1 Prozent statistisch signifikant ist, bedeutet hier: Unter 10.000 simulierten Preisreihen gleicher Länge und mit denselben ersten drei Momenten wie die historische Preisreihe erreichen nur 100 Reihen eine APR von mindestens 10 Prozent.
- Dieselbe Aussage bedeutet alternativ: Bei randomisierten Einstiegstagen erreicht nur eine von 100 Zufallspermutationen eine APR von mindestens 10 Prozent.
- Ein Buy-and-Hold in einem Marktindex ist für einen Timing-Dienst, der Long- und Short-Positionen eingeht, möglicherweise kein geeigneter Vergleichsmaßstab.
- Ein Maßstab, der die Nullhypothese für den Signifikanztest der Renditen von Long-Short-Signalen darstellt, ist ein Zufallssignal mit demselben Anteil von Long- und Short-Positionen.

## Risiken und Grenzen


## Beispiele

- Eine Strategie mit 30 Prozent annualisierter Backtest-Rendite, einer Sharpe Ratio von 0,3 und einer maximalen Drawdown-Dauer von zwei Jahren ist nicht konsistent. Die hohe Durchschnittsrendite kann ein Zufall sein und wiederholt sich live wahrscheinlich nicht.
- Eine Long-only-Strategie auf Rohöl-Futures rendierte 2007 mit 20 Prozent bei einer Sharpe Ratio von 1,5. Das Halten des Front-Month-Kontrakts brachte im selben Jahr 47 Prozent bei einer Sharpe Ratio von 1,7.
- Eine Strategie, die zu Jahresbeginn die zehn am niedrigsten bepreisten Aktien kauft und ein Jahr hält, zeigt für 2001 eine Backtest-Rendite von 388 Prozent.
- Eine Hochfrequenzstrategie auf den E-mini S&P 500 hat im Backtest 200 Prozent jährliche Durchschnittsrendite, eine Sharpe Ratio von 6 und eine durchschnittliche Haltedauer von 50 Sekunden.
- Die lineare Mean-Reversion-Strategie auf dem stationären Portfolio aus EWA, EWC und IGE erreicht eine annualisierte Rendite APR von 12,6 Prozent bei einer Sharpe Ratio von 1,4.
- Die Rendite einer Periode ist die P&L geteilt durch den Bruttomarktwert des Portfolios, also durch die Summe der absoluten Positionsmarktwerte.
- Der Paarhandel AUD.USD gegen CAD.USD mit Johansen-Eigenvektor hat, nach Ausschluss der ersten 250 Trainingstage, vom 18. Dezember 2009 bis 26. April 2012 eine APR von 11 Prozent.
- Dieselbe lineare Mean-Reversion auf dem fertigen Paar AUD.CAD mit Rollover-Zinsen hat eine APR von 6,2 Prozent; ohne Berücksichtigung der Rollover-Zinsen steigt die APR nur leicht auf 6,7 Prozent, obwohl der annualisierte durchschnittliche Rollover-Zins fast 5 Prozent ausmacht.
- Die lineare Mean-Reversion auf dem 12-Monats-Log-Kalender-Spread von CL hat vom 2. Januar 2008 bis 13. August 2012 eine ungehebelte APR von 8,3 Prozent.
- Die aufgeführten annualisierten Durchschnitte von Spot-Rendite α und Roll-Rendite γ sind für BR minus 2,7 und plus 10,8 Prozent, für Mais plus 2,8 und minus 12,8 Prozent, für CL plus 7,3 und minus 7,1 Prozent, für Kupfer plus 5,0 und plus 7,7 Prozent und für die zweijährige Treasury Note minus 0,0 und plus 3,2 Prozent.
- Bei BR, Mais und TU ist der Betrag der Roll-Rendite viel größer als der der Spot-Rendite; die annualisierte Roll-Rendite von Mais ist minus 12,8 Prozent gegenüber einer Spot-Rendite von 2,8 Prozent.
- Die durchschnittliche Roll-Rendite des VX-Future ist annualisiert sehr negativ, minus 50 Prozent (Simon und Campasano, 2012).
- Erb und Harvey berechnen für Heizöl eine annualisierte Roll-Rendite von 4,6 Prozent gegenüber einer Spot-Rendite von 0,93 Prozent, von Dezember 1982 bis Mai 2004.
- Die TU-Zeitreihen-Momentum-Strategie mit Lookback 250 und Haltedauer 25 erzielt vom 1. Juni 2004 bis zum 11. Mai 2012 eine annualisierte Rendite von 1,7 Prozent bei einer Sharpe Ratio von 1, gerechnet auf den Nominalwert von etwa 200.000 Dollar bei einer Margin von nur etwa 400 Dollar, mit einem maximalen Drawdown von 2,5 Prozent.
- In Tabelle 6.2 hat BR an der CME bei Lookback 100 und Haltedauer 10 eine annualisierte Rendite von 17,7 Prozent, eine Sharpe Ratio von 1,09 und einen maximalen Drawdown von minus 14,8 Prozent.
- Das überarbeitete TU-Signal auf der verzögerten Rollrendite mit einer Schwelle von 3 Prozent annualisierter Rollrendite erzielt vom 2. Januar 2009 bis zum 13. August 2012 eine annualisierte Rendite von 2,5 Prozent bei einer Sharpe Ratio von 2,1 und einem maximalen Drawdown von 1,1 Prozent.
- Die Kombination aus Mean-Reversion- und Momentum-Regel auf CL erzielt eine annualisierte Rendite von 12 Prozent bei einer Sharpe Ratio von 1,1.
- Long GLD und short GC erzielt vom 3. August 2007 bis zum 2. August 2010 eine annualisierte Rendite von 1,9 Prozent bei einem maximalen Drawdown von 0,8 Prozent; die Finanzierungskosten von GLD liegen nicht weit von 1,9 Prozent, sodass die Überschussrendite nahe null liegt.
- Die Rollrendite der Gold-Futures beträgt von Dezember 1982 bis Mai 2004 minus 4,9 Prozent annualisiert.
- Die Arbitrage short USO und long XLE bei Contango sowie long USO und short XLE bei Backwardation erzielt vom 26. April 2006 bis zum 9. April 2012 eine annualisierte Rendite von 16 Prozent bei einer Sharpe Ratio von etwa 1.
- Die VX-ES-Rollrendite-Strategie erzielt vom 29. Juli 2010 bis zum 7. Mai 2012 eine annualisierte Rendite von 6,9 Prozent bei einer Sharpe Ratio von 1; dieser Zeitraum wurde nicht zur Bestimmung der Hedge Ratio verwendet.
- Die vereinfachte querschnittliche Futures-Strategie erzielt vom 1. Juni 2005 bis zum 31. Dezember 2007 eine annualisierte Rendite von 18 Prozent bei einer Sharpe Ratio von 1,37 und vom 2. Januar 2008 bis zum 31. Dezember 2009 eine annualisierte Rendite von minus 33 Prozent.
- Beispiel 6.2 auf S&P-500-Aktien erzielt vom 15. Mai 2007 bis zum 31. Dezember 2007 eine annualisierte Rendite von 37 Prozent bei einer Sharpe Ratio von 4,1 und vom 2. Januar 2008 bis zum 31. Dezember 2009 eine annualisierte Rendite von minus 30 Prozent.
- Daniel und Moskowitz finden für dieselbe Aktienstrategie von 1947 bis 2007 eine annualisierte Durchschnittsrendite von 16,7 Prozent bei einer Sharpe Ratio von 0,83.
- Hafez und Xie erzielen mit RavenPack-Sentiment, je nach Zahl der Aktien, vor Transaktionskosten annualisierte Renditen von 52 bis 156 Prozent bei Sharpe Ratios von 3,9 bis 5,3.
- Das marktneutrale PRESSURE-Portfolio von Coval und Stafford erzielt vor Kosten etwa 17 Prozent annualisiert, das Front-Running der Fonds weitere 17 Prozent und die anschließende Mean Reversion weitere 7 Prozent, zusammen etwa 41 Prozent vor Transaktionskosten.
- Die Rollrendite von VX kann bis minus 50 Prozent annualisiert betragen, die von ES ist mit etwa 1 Prozent annualisiert unbedeutend.
- Die Regel TT-4-91 erzielte von November 1980 bis Juni 2005 auf trendbereinigten S&P-500-Daten eine annualisierte Rendite von 4,84 Prozent.
- Die erwartete Jahresrendite einer Regel ohne Vorhersagekraft ist auf trendbereinigten Daten null.
- Die mittlere Tagesrendite dieser Regel, die bei der Nullzentrierung von jedem Tagesertrag abgezogen wird, beträgt ungefähr 0,0192 Prozent.
- Im Beispiel einer traditionellen Signifikanzprüfung beträgt die Rendite der Regel plus 10 Prozent annualisiert.
- Die beste von 50 gebacktesteten Regeln erzielte eine annualisierte Rendite von plus 37 Prozent.
- Eine Leistungskennzahl, auf die ein Backtest verdichtet wird, ist die annualisierte Durchschnittsrendite.
- Nach den Langfristratings von Hulbert's Financial Digest vom Juli 2005 erzielte The Elliott Wave Financial Forecast mit Long- und Short-Signalen annualisierte Renditen von +1,1 Prozent über 5 Jahre, −28,2 Prozent über 10 Jahre, −25,9 Prozent über 15 Jahre und −18,2 Prozent über die Lebensdauer des Dienstes seit dem 31.12.1984.
- Für dieselben Zeiträume gibt Hulbert für den Dow Jones Wilshire 5000 mit reinvestierten Dividenden −1,3 Prozent über 5 Jahre, +10 Prozent über 10 Jahre und +10,7 Prozent über 15 Jahre an.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 20–39 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-002-p020-p039|S. 20–39]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 172–191 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-010-p172-p191|S. 172–191]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 229–248 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-013-p229-p248|S. 229–248]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 267–286 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-015-p267-p286|S. 267–286]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 286–305 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-016-p286-p305|S. 286–305]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 305–324 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-017-p305-p324|S. 305–324]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 381–400 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-021-p381-p400|S. 381–400]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 419–438 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-023-p419-p438|S. 419–438]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 476–495 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-026-p476-p495|S. 476–495]]

## Verwandte Themen
