---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/02 - Trendanalyse/02 - Trendanalyse|02 - Trendanalyse]]"
weitere_hauptthemen: []
unterthema: "Trendmodelle"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Trend-Stationarität


## Kurzdefinition

- Eine trendstationäre Zeitreihe hat die Form pt gleich β0 plus β1 mal t plus rt, wobei rt stationär ist, zum Beispiel eine stationäre AR(p)-Reihe.
- Ein linearer deterministischer Trend liegt im strukturellen Komponentenmodell vor, wenn die Innovationsvarianzen von Niveau und Steigung beide null sind. Andernfalls ist der Trend nichtstationär und kann eine doppelte Einheitswurzel haben.

## Kernaussagen

- pt wächst linear in der Zeit mit der Rate β1 und kann sich ähnlich verhalten wie ein Random Walk mit Drift.
- Bei festem Startwert p0 hat der Random Walk mit Drift den Mittelwert p0 plus µ t und die Varianz t mal σa zum Quadrat; beide hängen von der Zeit ab.
- Das trendstationäre Modell hat den zeitabhängigen Mittelwert β0 plus β1 mal t und die Varianz von rt, die endlich und zeitlich invariant ist.
- Eine trendstationäre Reihe wird stationär, indem der Zeittrend durch eine einfache lineare Regression entfernt wird.
- Die Analyse trendstationärer Zeitreihen folgt der Methode in Abschnitt 2.9.
- Die übliche Trendkomponente ist μt plus 1 gleich μt plus βt plus ηt, ηt normal mit Varianz σ²η, und βt gleich βt minus 1 plus ςt, ςt normal mit Varianz σ²ς.
- Die Startwerte μ1 und β1 sind normal mit Mittel null und großer Varianz ξ, zum Beispiel 10 hoch 8. So zitiert der Text Kitagawa und Gersch (1996).
- Ist σς gleich 0, folgt μt einem Random Walk mit Drift β1. Sind σς und ση beide null, stellt μt einen linearen deterministischen Trend dar.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Für den Logarithmus des S&P 500 vom 3. Januar 1950 bis 16. April 2008 werden eine Einheitswurzel und ein positiver Drift nicht verworfen, ein zusätzlicher linearer Zeittrend aber auf dem 5-Prozent-Niveau schon nicht bestätigt; der Zeitkoeffizient 0,0020 hat den p-Wert 0,0642.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 96–115 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-006-p096-p115|S. 96–115]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 609–628 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-033-p609-p628|S. 609–628]]

## Verwandte Themen
