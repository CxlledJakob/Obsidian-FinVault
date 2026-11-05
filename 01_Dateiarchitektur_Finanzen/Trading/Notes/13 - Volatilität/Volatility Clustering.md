---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/13 - Volatilität/13 - Volatilität|13 - Volatilität]]"
weitere_hauptthemen: []
unterthema: "Volatilitätsdynamik"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Volatility Clustering


## Kurzdefinition

- Der Volatilitätsprozess betrifft die zeitliche Entwicklung der bedingten Varianz der Rendite.

## Kernaussagen

- Die Zeitplots der monatlichen einfachen und logarithmierten Renditen von IBM und des wertgewichteten Marktindex, Januar 1926 bis Dezember 2008, zeigen, dass die Schwankungen der Renditen über die Zeit variieren und in Clustern auftreten.
- Die Grundmuster der einfachen und der logarithmierten Renditen sind in diesen Plots ähnlich.
- Die zehnjährigen und einjährigen Treasury-Constant-Maturity-Sätze bewegen sich im Gleichlauf, die Einjahressätze wirken aber volatiler.
- Der tägliche Dollar-Yen-Kurs vom 4. Januar 2000 bis 27. März 2009 zeigt im Stichprobenzeitraum gelegentlich große Änderungen.
- Eine besondere Eigenschaft der Aktienvolatilität sind Volatilitätscluster: die Volatilität kann in manchen Zeiträumen hoch und in anderen niedrig sein.
- Im ARCH-Modell folgen auf große quadrierte Schocks tendenziell wieder große Schocks, weil die bedingte Varianz von diesen Quadraten abhängt; das entspricht den beobachteten Volatilitätsclustern.
- Eine große Varianz erzwingt keine große Realisation, sie macht sie nur wahrscheinlicher.
- Bei den zehnminütigen Mark-Dollar-Änderungen vom 5. bis 19. Juni 1989 treten große Prozentänderungen nur gelegentlich auf, dazwischen liegen ruhige Phasen; die Quadrate zeigen diese Cluster.
- Die Autokorrelation der quadrierten und der absoluten monatlichen Intel-Logrenditen von 1973 bis 2008 zeigt dieselbe Abhängigkeit, während die Renditen selbst fast unkorreliert sind.
- Im GARCH(1,1) zieht ein großes a, t minus 1, quadrat oder eine große vergangene bedingte Varianz ein großes sigma t quadrat nach sich, sodass auf ein großes Quadrat tendenziell wieder ein großes Quadrat folgt; das erzeugt die Volatilitätscluster von Finanzzeitreihen.
- Bei den monatlichen S&P-500-Überschussrenditen von 1926 bis 1991 zeigt die partielle Autokorrelation der Quadrate starke lineare Abhängigkeit, auch wenn die Renditen selbst nur auf den Lags 1 und 3 korreliert sind.
- Die Summe alpha 1 plus beta 1 liegt im angepassten S&P-GARCH(1,1) nach dem Text bei 0,9772 und damit nahe bei 1, die Cluster klingen also sehr langsam ab.
- Die Autokorrelationsfunktion der quadrierten oder absoluten Renditen eines Assets fällt oft langsam, obwohl die Renditereihe keine serielle Korrelation hat (Ding, Granger und Engle, 1993).
- Die Stichproben-ACF der täglichen absoluten Logrenditen von IBM und dem S&P 500 vom 3. Juli 1962 bis 31. Dezember 2003 ist positiv, von mäßiger Größe und fällt langsam.
- Im Long-Memory-SV-Modell erzeugt (1−B)^d mit 0 < d < 0,5 ein hyperbolisches statt exponentielles Abklingen der ACF von u_t. ln(a²_t) ist dann ein gaußsches Long-Memory-Signal plus nichtgaußsches weißes Rauschen.
- Bollerslev und Jubinski (1999) sowie Ray und Tsay (2000) schätzen den Median von d für den Logarithmus quadrierter Tagesrenditen von S&P-500-Unternehmen auf etwa 0,38.
- Unternehmen derselben Branche haben tendenziell mehr gemeinsame Long-Memory-Komponenten in den täglichen Aktienvolatilitäten, etwa große US-Banken und Finanzinstitute (Ray und Tsay, 2000).
- Im SV-Modell mit m = 1 ist die Korrelation quadrierter Schocks corr(a²_t, a²_{t−i}) = [exp(σ²_h α₁^i) − 1] / [3 exp(σ²_h) − 1].
- Stochastische Volatilitätsmodelle verbessern oft die Anpassung. Ihre Beiträge zu Volatilitätsprognosen außer Stichprobe sind gemischt.
- Für die tägliche Apple-Range sind die Formparameter von WACD(1,1) und GACD(1,1) größer als 1, α̂ = 2,377 beziehungsweise α̂ = 1,622 bei κ̂ = 2,104; die Hazard-Funktion der täglichen Range steigt damit monoton.
- Eine monoton steigende Hazard-Funktion der täglichen Range passt zum Volatility Clustering: große Volatilität folgt tendenziell auf große Volatilität.
- Die Volatilität der Apple-Range scheint von 2000 bis 2001 zu steigen, nach 2002 auf ein stabiles Niveau zu fallen und am Ende der Reihe bis November 2007 wieder etwas zuzunehmen.
- Die Stichproben-ACF der täglichen Range ist hochsignifikant und klingt langsam ab.
- Die Duration-Parameter der drei ACD-Modelle für die Apple-Range sind stabil: EACD hat α1 = 0,133 und β1 = 0,849, WACD α1 = 0,131 und β1 = 0,835, GACD α1 = 0,133 und β1 = 0,843; allein das konstante Glied des EACD fällt heraus.
- RiskMetrics lässt die bedingte Varianz von der vorherigen Varianz und vom quadrierten vorigen Schock abhängen: σ zum Quadrat von t = α mal σ zum Quadrat von t minus 1 plus (1 minus α) mal r zum Quadrat von t minus 1, mit typischem α von 0,94.
- Die Verwendung von Teilperioden-Maxima übersieht das Volatility Clustering der täglichen Logrenditen; der neuere Extremwertansatz überwindet diese Schwäche.
- Ein Cluster der Überschreitungszeitpunkte zeigt eine Phase großer Marktrückgänge.
- Extremereignisse treten wegen der seriellen Abhängigkeit in Clustern auf; nach Nachrichten sieht man oft mehrere große Renditen, positive wie negative.
- Der Blockschätzer G(un)/N(un) des Extremalindex ist der Kehrwert der mittleren Clustergröße des begrenzenden zusammengesetzten Poisson-Prozesses (Hsing, Hüsler und Leadbetter 1988).
- Die geschätzten Volatilitäten der univariaten GARCH(1,1)-Modelle für Hang Seng und Nikkei 225 bestätigen, dass beide Märkte 2008 ungewöhnlich volatil waren. Die Volatilitätsgleichungen liegen wegen der Subprime-Krise nahe an IGARCH(1,1).
- Der EWMA-Ansatz erzeugt für dieselben beiden Indexrenditen glattere Volatilitätsreihen als die univariaten GARCH(1,1)-Modelle. Das Muster der Volatilität bleibt ähnlich.
- Im Beispiel Januar 1999 bis Dezember 2004 schwanken die Aktienrenditen von IBM und Dell stärker als die Wechselkursrenditen von Euro und Yen. Die Variabilität der Aktienrenditen scheint in den späteren Jahren zu sinken.
- Die Korrelation zwischen zwei Renditereihen von S&P 500, Cisco und Intel steigt, wenn die Renditen volatil sind. Das stimmt damit überein, dass die Korrelation internationaler Aktienindizes in einer Finanzkrise zunimmt.
- Das DCC-Modell reagiert auf große Innovationen schneller als eine rollierende Schätzung mit 69 Tagen. Anstieg und Abklingen der Volatilität erfolgen rascher.
- Die angepasste Volatilität der S&P-500-Tageslogrendite ist von 1991 bis 1999 in den späteren Jahren gestiegen. Die Volatilität der Cisco-Rendite zeigt diesen Anstieg nicht. Die Indexvolatilität bleibt deutlich kleiner als die der beiden Einzelaktien.
- Das univariate stochastische Volatilitätsmodell setzt at = sqrt(ht) εt und ln ht = α0 + α1 ln ht−1 + vt, mit |α1| < 1.
- Die Logtransformation hält ht positiv; εt und vt sind unabhängig, εt mit Varianz 1 und vt mit Varianz σ²v.
- Erklärende Variablen xit stehen zur Zeit t − 1 bereit und dürfen verzögerte Renditen rt−i sein; für ln ht kann ein AR(p) höherer Ordnung nötig sein.
- GARCH, BEKK und das bivariate stochastische Volatilitätsmodell zeigen für die monatlichen IBM-Logrenditen 1962 bis 2009 Volatility Clustering und einen steigenden Volatilitätstrend.
- Die Posterior-Mittel von ht des univariaten SV-Modells und die angepassten GARCH(1,1)-Volatilitäten des S&P 500 zeigen ein ähnliches Muster.
- Der Koeffizient α1 mit Posteriormittel 0,837 und der GARCH-Koeffizient 0,837 von ht−1 quantifizieren diese Persistenz der Monatsvolatilität.
- Der zusätzliche Gipfel des bivariaten GARCH um 1993 beim S&P 500 erscheint im SV-Modell nicht.

## Funktionsweise

- Im GARCH(1,1) geht die ℓ-Schritt-Volatilitätsprognose mit dem Faktor φ = α1 plus β1 in die vorherige Prognose ein; die geschlossene k-Perioden-Formel setzt φ < 1 voraus.
- Das qualitative Volatilitätsmaß x3t zählt, an wie vielen der Tage von t minus 1 bis t minus 5 einschließlich der Betrag der mittelwertbereinigten Logrendite mindestens 2,5 Prozent war.
- Der Runs-Schätzer des Extremalindex zählt Überschreitungen, auf die ein Lauf von k Beobachtungen unter der Schwelle folgt, und teilt diese Zahl durch die Gesamtzahl der Überschreitungen.

## Voraussetzungen


## Anwendung im Trading

- In der Anwendung spielt Volatilität eine wichtige Rolle bei der Optionsbewertung und im Risikomanagement.

## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Das an die IBM-Tageslogrenditen angepasste IGARCH(1,1) ohne Drift wird von Q(10) = 56,19 der quadrierten standardisierten Residuen verworfen.
- Das homogene Poisson-Modell für die negativen IBM-Renditen bei Schwelle 2,5 Prozent lässt in den Prüfgrößen der Dauern und der Exzesse signifikante serielle Korrelationen zurück und besteht die Unabhängigkeitsprüfung nicht.
- Für die negativen täglichen IBM-Logrenditen von 1962 bis 1998 wird wegen schwacher serieller Abhängigkeit die Blockgröße k gleich 10 gewählt; bei Schwelle 0,025 ist der Extremalindex-Schätzer 0,823.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 39–58 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-003-p039-p058|S. 39–58]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 134–153 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-008-p134-p153|S. 134–153]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 153–172 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-009-p153-p172|S. 153–172]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 286–305 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-016-p286-p305|S. 286–305]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 343–362 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-019-p343-p362|S. 343–362]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 362–381 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-020-p362-p381|S. 362–381]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 381–400 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-021-p381-p400|S. 381–400]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 400–419 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-022-p400-p419|S. 400–419]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 533–552 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-029-p533-p552|S. 533–552]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 552–571 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-030-p552-p571|S. 552–571]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 647–666 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-035-p647-p666|S. 647–666]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 666–685 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-036-p666-p685|S. 666–685]]

## Verwandte Themen
