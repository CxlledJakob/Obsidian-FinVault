---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/24 - Makroökonomie/24 - Makroökonomie|24 - Makroökonomie]]"
weitere_hauptthemen: ["[[Trading/Notes/15 - Intermarket-Analyse/15 - Intermarket-Analyse|15 - Intermarket-Analyse]]"]
unterthema: "Geldpolitik"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Zinsstrukturkurve


## Kurzdefinition

- Der Duration Spread, auch Steigung der Zinsstrukturkurve genannt, ist die Differenz der Renditen von Schuldpapieren gleicher Kreditqualität und verschiedener Duration, also verschiedener Restlaufzeit.

## Kernaussagen

- Die Steigung der Zinsstrukturkurve ist einer der Faktoren des Arbitrage-Pricing-Modells, neben der Inflationsrate und dem Spread zwischen Anleihen niedriger und hoher Qualität.
- Ein positiver Spread, bei dem die langfristigen Sätze höher sind als die kurzfristigen, ist oft ein bullischer Indikator für künftige Änderungen der Aktienkurse, besonders bei Aktienindizes, die nicht inflationsbereinigt sind.
- Bei den Zinsreihen sind die Stichprobenmittel proportional zur Laufzeit, die Stichprobenstandardabweichungen umgekehrt proportional zur Laufzeit.
- Bei den Anleiherenditen steigen die Stichprobenstandardabweichungen mit der Laufzeit, während die Stichprobenmittel über alle Laufzeiten stabil bleiben.
- Die zehnjährigen und einjährigen Treasury-Constant-Maturity-Sätze bewegen sich im Gleichlauf, die Einjahressätze wirken aber volatiler. Der Text datiert die Monatsplots von April 1954 bis Februar 2009, Bildunterschrift und Tabelle 1.3 von April 1953 bis Februar 2009.
- Die meisten betrachteten Reihen haben positive Exzess-Kurtosis. Die Zinsen stammen von der Federal Reserve Bank of St. Louis, die monatlichen Anleiherenditen sind Fama-Bond-Portfolio-Renditen aus CRSP.
- Die Zinsstruktur ist das Beispiel, in dem die zeitliche Entwicklung der Beziehung zwischen Zinssätzen verschiedener Fälligkeit untersucht wird.
- Verwendet werden die einjährige und die dreijährige Treasury Constant Maturity Rate, 2467 Wochenwerte vom 5. Januar 1962 bis 10. April 2009, in Prozent, von der Federal Reserve Bank of St. Louis.
- Streng genommen wären die beiden Reihen gemeinsam multivariat zu modellieren; die Regression lässt die Gleichzeitigkeit aus.
- Die Niveauregression r3t gleich 0,832 plus 0,930 mal r1t plus et hat die residuale Standardabweichung 0,523, das Bestimmtheitsmaß 96,5 Prozent und die Standardfehler 0,024 und 0,004, ist aber unzureichend.
- Unter Einheitswurzeln sind die beiden Sätze nicht kointegriert, ein langfristiges Gleichgewicht wird nicht gestützt.
- Eine invertierte Zinsstrukturkurve bedeutet, dass die Zinssätze umgekehrt zu ihrer Restlaufzeit verlaufen; dieses Muster kam im Stichprobenzeitraum vor.
- Die Änderungen c1t und c3t sind die ersten Differenzen; ihre Regression lautet c3t gleich 0,792 mal c1t plus et, residuale Standardabweichung 0,0690, Bestimmtheitsmaß 82,5 Prozent, Standardfehler 0,0073.
- Mit MA(1)-Fehler gilt c3t gleich 0,794 mal c1t plus et und et gleich at plus 0,1823 mal at minus 1, residuale Standardabweichung 0,0678, Bestimmtheitsmaß 83,1 Prozent, Standardfehler 0,0075 und 0,0196.
- Daraus folgt r3t gleich r3,t minus 1 plus 0,794 mal (r1t minus r1,t minus 1) plus at plus 0,182 mal at minus 1.
- Der t-Quotient der Steigung in der Änderungsregression fällt von 107,91 auf 48,44 mit dem heteroskedastizitätskonsistenten und auf 39,92 mit dem Newey-West-Schätzer.
- Die wöchentlichen Renditen der Moody's-Aaa- und -Baa-Anleihen derselben Spanne sind Durchschnitte der Tagesrenditen und stammen ebenfalls von der Federal Reserve Bank of St. Louis.
- Wegen invertierter Zinsstrukturkurven soll der Spread der Zinssätze nichtlinear sein.
- Der Wochen-Spread s_t = r_{3t} − r_{1t} verwendet die konstanten Laufzeiten der einjährigen und der dreijährigen US-Treasury von 5. Januar 1962 bis 10. April 2009; der Text nennt s_t den Spread der Log-Zinssätze.
- Die Änderung des Spreads ist s*_t = (r_{3t} − r_{3,t−1}) − (r_{1t} − r_{1,t−1}) = s_t − s_{t−1}.
- Linearität von {s_t} und von {s*_t} ist auf dem 5-Prozent-Niveau mit Nichtlinearitätstests zu prüfen, und für beide Reihen ist ein Schwellenmodell zu bauen und zu prüfen.
- Die Reihen stammen aus w-gs1yr.txt und w-gs3yr.txt beziehungsweise von der Federal Reserve Bank of St. Louis.
- Die monatlichen Logrenditen von US-Anleihenindizes mit Laufzeiten 30, 20, 10, 5 und 1 Jahr umfassen Januar 1942 bis Dezember 1999 und 696 Beobachtungen.
- Die ersten zwei gemeinsamen Faktoren erklären mehr als 90 Prozent der Variabilität, 95,7 Prozent mit der Hauptkomponentenmethode und 90,5 Prozent mit Maximum Likelihood. Die spezifischen Varianzen der fünf Indizes sind sehr klein.
- Unrotiert laden alle fünf Laufzeiten ungefähr gleich auf den ersten Faktor, der die allgemeinen US-Anleihenrenditen darstellt. Die Ladungen auf den zweiten Faktor sind positiv mit der Restlaufzeit korreliert, in der Hauptkomponentenlösung 0,253, 0,240, 0,140, minus 0,142 und minus 0,585, und summieren sich ungefähr auf null.
- Dieser zweite Faktor ist der Laufzeiteffekt und zugleich der Kontrast zwischen langfristigen Anleihen, Laufzeit 10 Jahre oder länger, und kurzfristigen Anleihen.
- Nach der Rotation sind die Ladungen des ersten Faktors proportional zur Restlaufzeit und die des zweiten umgekehrt proportional zur Restlaufzeit.
- Ein VARMA(2,1) entfernt die serielle Abhängigkeit, verändert die gleichzeitige Korrelationsmatrix aber kaum. Die Korrelation zwischen 30- und 20-jährigem Index ist 0,98, zwischen 30- und 1-jährigem Index 0,63 vor und 0,66 nach dem VARMA. Die Faktorenanalyse wird deshalb direkt auf die Renditen angewendet.

## Funktionsweise

- In der Fallstudie ist der Duration Spread die Rendite der zehnjährigen Treasury Note minus die Rendite der Dreimonats-T-Bills.
- Er wurde so und nicht als Dreimonatsrendite minus Zehnjahresrendite definiert, damit ein Aufwärtstrend des Spreads voraussichtlich bullische Folgen für den Aktienmarkt, den S&P 500, hat.
- Tabelle 8.2 führt ihn als Duration Spread (10 Year minus 3 Month) mit dem Kürzel DURSPD und der Nummer 39.
- Dieselbe Fallstudie verwandelte die Dreimonats-T-Bill-Rendite und die Zehnjahres-Treasury-Rendite über den Kehrwert in preisähnliche Reihen, neben den Renditen von Moodys AAA- und BAA-Anleihen.
- Im Arbitrage-Pricing-Modell entsteht die lineare Beziehung zu diesen Faktoren, weil Arbitrageure nach risikolosen Gelegenheiten mit einem Investment von null suchen.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Monatliche Treasury-Sätze, April 1953 bis Februar 2009, T = 671, in Prozent, als Mittel, Standardabweichung, Schiefe, Exzess-Kurtosis, Minimum und Maximum: 1 Jahr 5,59, 2,98, 1,02, 1,32, 0,44, 16,72; 3 Jahre 5,98, 2,85, 0,95, 0,95, 1,07, 16,22; 5 Jahre 6,19, 2,77, 0,97, 0,82, 1,52, 15,93; 10 Jahre 6,40, 2,69, 0,95, 0,61, 2,29, 15,32.
- Wöchentliche Treasury-Bill-Sätze, Ende 27. März 2009: 3 Monate ab 8. Januar 1954, n = 2882, Mittel 5,07, Standardabweichung 2,82, Schiefe 1,08, Exzess-Kurtosis 1,80, Minimum 0,02, Maximum 16,76; 6 Monate ab 12. Dezember 1958, n = 2625, Mittel 5,52, Standardabweichung 2,73, Schiefe 0,99, Exzess-Kurtosis 1,53, Minimum 0,20, Maximum 15,76.
- Monatliche Fama-Bond-Portfolio-Renditen, Januar 1952 bis Dezember 2008, T = 684, in Prozent, als Mittel, Standardabweichung, Schiefe, Exzess-Kurtosis, Minimum und Maximum: 1–12 Monate 0,45, 0,35, 2,47, 13,14, −0,40, 3,52; 12–24 Monate 0,49, 0,67, 1,88, 15,44, −2,94, 6,85; 24–36 Monate 0,52, 0,98, 1,37, 12,92, −4,90, 9,33; 48–60 Monate 0,53, 1,40, 0,60, 4,83, −5,78, 10,06; 61–120 Monate 0,55, 1,69, 0,65, 4,79, −7,35, 10,92.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 400–419 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-022-p400-p419|S. 400–419]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 39–58 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-003-p039-p058|S. 39–58]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 115–134 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-007-p115-p134|S. 115–134]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 248–267 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-014-p248-p267|S. 248–267]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 514–533 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-028-p514-p533|S. 514–533]]

## Verwandte Themen
