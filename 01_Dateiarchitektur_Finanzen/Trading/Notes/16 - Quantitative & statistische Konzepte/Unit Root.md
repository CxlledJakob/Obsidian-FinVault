---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Zeitreihen"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Unit Root


## Kurzdefinition

- Right-Tail-Unit-Root-Tests prüfen exponentielles Wachstum oder Kollaps unter einer autoregressiven Spezifikation.
- Ein Unit-Root-Test ist ein Testtyp, mit dem festgestellt wird, dass eine Zeitreihe stationär ist.
- Eine Preisreihe ohne festes Niveau heißt unit-root-nichtstationäre Zeitreihe; das bekannteste Beispiel ist der Random Walk.
- Ein ARIMA-Modell ist unit-root-nichtstationär, weil sein AR-Polynom die charakteristische Wurzel 1 hat.
- Kointegration einer k-dimensionalen einheitswurzel-nichtstationären Reihe liegt vor, wenn die Zahl h der Einheitswurzeln im System 0 kleiner als h kleiner als k erfüllt. Die Zahl der Kointegrationsfaktoren ist k minus h.
- Liegen alle Nullstellen von |Φ(B)| außerhalb des Einheitskreises, ist xt Unit-Root-stationär und ein I(0)-Prozess, also nicht integriert. |Φ(1)| = 0 bedeutet, dass xt Unit-Root-nichtstationär ist.
- Höchstens I(1) heißt: ist die Komponente xit selbst nicht Unit-Root-stationär, dann ist ihre erste Differenz (1 − B)xit Unit-Root-stationär.

## Kernaussagen

- Enthält die Reihe eine Unit Root, dann ist der kleinste Fixed-Width-Fracdiff-Koeffizient d*, der sie stationär macht, kleiner als 1.
- Ist die Reihe bereits stationär, gilt d* gleich 0. Zeigt sie explosives Verhalten wie in einer Blase, gilt d* größer als 1.
- Der besonders interessierende Fall ist d* wenig über 0 und weit unter 1. Die Originalreihe ist dann nur mild nichtstationär: Differenzierung ist nötig, eine volle ganzzahlige Differenzierung entfernt aber zu viel Gedächtnis und Prognosekraft.
- Die Null des Chow-Typ-Dickey-Fuller-Tests ist ein Unit Root mit Rho gleich 1, die Alternative ein explosiver Prozess mit Rho größer als 1 nach dem Bruch.
- Standard-Unit-Root- und Kointegrationstests erkennen Blasen schlecht, weil periodisch zusammenbrechende Blasen eher wie ein Unit-Root- oder stationärer autoregressiver Prozess aussehen.
- Im Null-Lag-Modell auf Logpreisen ist Beta gleich 0 der Unit-Root-Zustand: das System ist nichtstationär und verhält sich als Martingal.
- Der gewöhnliche ADF-Test ist der Spezialfall von SADF, bei dem die minimale Fensterlänge gleich Endpunkt minus 1 ist.
- SADF testet auf der ADF-Regression mit Konstante und Lag-Differenzen die Null Beta kleiner oder gleich 0 gegen die Alternative Beta größer als 0.
- Für USD.CAD wird die Unit-Root-Null nicht verworfen: ADF-Statistik minus 1,840744, kritischer 10-Prozent-Wert minus 2,594, AR(1)-Schätzung 0,994120. λ ist negativ, ein Trend liegt damit nicht vor.
- Der Drift β wird null gesetzt, der Offset μ nicht, weil der Mittelwert selten null ist und ein konstanter Drift klein gegen die täglichen Schwankungen ist. Oft ist Lag 1 nötig, damit die Null verworfen werden kann.
- Der CADF-Test auf EWC gegen EWA verwirft die Unit Root des Spreads auf 95 Prozent: t-Statistik minus 3,64346635 gegen minus 3,359, AR(1)-Schätzung minus 0,020411.
- Im Vektorfall ist Λ gleich 0 der Zustand ohne Kointegration, analog zur univariaten Unit Root λ gleich 0.
- Ein ADF-Test auf dem Verhältnis Back zu Front von VX zeigt Stationarität mit 99 Prozent Wahrscheinlichkeit.
- Ein ADF-Test auf dem Crack Spread vom 20. Mai 2002 bis zum 4. Mai 2012 zeigt keine Mean Reversion.
- Ein ADF-Test auf CL gegen BZ im Verhältnis 1:1 zeigt, dass der Spread weit von stationär entfernt ist.
- Als AR(1) gelesen hat der Random Walk den Koeffizienten 1 und verletzt die schwache Stationarität.
- Die ψ-Gewichte der Moving-Average-Darstellung eines ARIMA fallen nicht gegen null, deshalb hat ein vergangener Schock eine dauerhafte Wirkung und die Reihe starkes Gedächtnis.
- yt ist ein ARIMA(p, 1, q), wenn die erste Differenz einem stationären und invertierbaren ARMA(p, q) folgt; Logpreise werden so behandelt, die Logrendite ln(Pt) minus ln(Pt−1) als stationär.
- Eine doppelte Einheitswurzel liegt vor, wenn auch die erste Differenz unit-root-nichtstationär ist, die zweite Differenz yt minus 2 yt−1 plus yt−2 aber schwach stationär ist; folgt diese einem ARMA(p, q), ist yt ein ARIMA(p, 2, q).
- Der Dickey-Fuller-Test prüft H0: phi1 gleich 1 gegen Ha: phi1 kleiner als 1 über die t-Ratio des Kleinste-Quadrate-Schätzers; ist der Fehler weißes Rauschen mit endlichen Momenten der Ordnung etwas über 2, konvergiert die Statistik gegen eine Funktion der standardisierten Brownschen Bewegung.
- Die kritischen Werte werden simuliert, weil die Grenzverteilung nicht die Standardnormalverteilung ist; nur wenn eine von null verschiedene Konstante mitgeschätzt wird, ist die t-Ratio asymptotisch normal, und auch das erst bei großen Stichproben.
- Ist die wahre Konstante null und wird trotzdem eine Konstante geschätzt, konvergiert die t-Ratio gegen eine andere nichtstandardisierte Verteilung.
- Der erweiterte Dickey-Fuller-Test prüft H0: β gleich 1 gegen Ha: β kleiner als 1 in einer Regression mit Deterministik ct und verzögerten Differenzen, gleichwertig H0: β minus 1 gleich 0 gegen die negative Alternative; ct kann null, konstant oder linear in t sein.
- Mit wachsender Stichprobe gehen die Stichprobenautokorrelationen einer Unit-Root-Reihe gegen 1.
- Für eine einheitswurzel-nichtstationäre Reihe konvergiert die Stichproben-Autokorrelation auf jedem festen Lag mit wachsender Stichprobe gegen 1 (Chan und Wei 1988; Tiao und Tsay 1983).
- Die Residuen der Regression der wöchentlichen Dreijahres- auf die Einjahres-Treasury-Rendite sind hoch signifikant autokorreliert, fallen langsam und zeigen das Muster einer Einheitswurzel.
- Das Einheitswurzelverhalten beider Zinssätze und dieser Residuen führt zur Regression der ersten Differenzen.
- Ist die Residualreihe einheitswurzel-nichtstationär, schreibt das Vorgehen vor, abhängige und erklärende Variable einmal zu differenzieren und die Regression erneut zu prüfen.
- Unter der Annahme, dass beide Zinsreihen Einheitswurzeln haben, sind sie nicht kointegriert; ein langfristiges Gleichgewicht wird von den Daten nicht gestützt.
- Hat das AR-Polynom der ARMA-Darstellung eines GARCH eine Einheitswurzel, liegt ein IGARCH vor; IGARCH-Modelle sind GARCH-Modelle mit Einheitswurzel.
- Ein IGARCH(1,1) lautet sigma t quadrat gleich alpha 0 plus beta 1 mal sigma, t minus 1, quadrat plus (1 minus beta 1) mal a, t minus 1, quadrat, mit beta 1 zwischen 0 und 1 ausschließlich.
- Für die monatlichen S&P-500-Überschussrenditen lautet ein geschätztes IGARCH(1,1) rt gleich 0,0067 plus at und sigma t quadrat gleich 0,000119 plus 0,8059 mal sigma, t minus 1, quadrat plus 0,1941 mal a, t minus 1, quadrat; die Standardfehler in der Volatilitätsgleichung werden mit 0,0017, 0,000013 und 0,0144 angegeben.
- Die unbedingte Varianz ist unter diesem IGARCH nicht definiert, was sich für eine Überschussrendite schwer rechtfertigen lässt.
- Liegt alpha 1 plus beta 1 nahe bei 1, wird die Restriktion gleich 1 gesetzt; im gaußschen S&P-GARCH(1,1) nennt der Text die Summe 0,9772, im Student-t-Modell mit 5 Freiheitsgraden etwa 0,95.
- Die Varianzprognose eines IGARCH ist sigma h von 1 plus (ell minus 1) mal alpha 0, die Wirkung der aktuellen Prognose bleibt also dauerhaft.
- Der Varianzprozess ist nach Nelson (1990) ein Martingal und unter bestimmten Bedingungen streng, aber nicht schwach stationär.
- Die saisonbereinigte monatliche US-Arbeitslosenquote von Januar 1948 bis März 2009 ist möglicherweise nicht einheitswurzelstationär: die Autokorrelation fällt langsam, es gibt einen langsamen Aufwärtstrend, und die Reihe ist nicht zeitumkehrbar.
- Deshalb wird die erste Differenz y_t = (1−B) u_t mit einem saisonalen ARIMA und anschließend mit einem TAR untersucht.
- Das ARIMA der Differenz enthält die Faktoren (1 − 1,13B + 0,27B²) und (1 − 0,51B¹²) und beschreibt die serielle Abhängigkeit der Änderungen angemessen: Q(12) = 12,3 (p = 0,056) und Q(24) = 25,5 (p = 0,11).
- Im Modell (8.31) sind die Eigenwerte der AR-Matrix 0 und 1, das Modell ist also nicht schwach stationär. Jede Komponente ist einheitswurzel-nichtstationär und folgt einem ARIMA(0,1,1), im System gibt es aber nur eine Einheitswurzel.
- y1t ist der gemeinsame Trend von x1t und x2t. Die Einheitswurzeln der beiden Komponenten werden durch die Einheitswurzel von y1t eingeführt.
- Die Linearkombination y2t gleich 0,5 x1t plus x2t hat keine Einheitswurzel. Damit sind x1t und x2t kointegriert, und (0,5; 1)′ ist ein Kointegrationsvektor.
- Differenziert man einzelne Komponenten eines kointegrierten Systems, kann Overdifferencing entstehen.
- Im simulierten zweidimensionalen System gibt es nur eine Unit Root. Sie sitzt im gemeinsamen Trend y1t und erzeugt die Unit Roots von x1t und x2t. Die Linearkombination y2t = 0,5 x1t + x2t hat keine Unit Root.
- Die Stichprobenkorrelation einer Unit-Root-nichtstationären Reihe mit einer stationären Reihe geht mit der Stichprobengröße gegen null.
- Die Darstellung nimmt Unit Roots der Vielfachheit 1 an und lässt sich auf andere Vielfachheiten erweitern.
- Im Cost-of-Carry-Modell muss der Prozess z∗t Unit-Root-stationär sein, sonst gibt es anhaltende Arbitrage. Für Future und Kasse des S&P 500 wird eine Unit Root angenommen; nach Zins und Dividendenrendite bleibt der Kointegrationsvektor (1, −1).
- Für Aktien-Logpreise wird ein Unit-Root-nichtstationärer Random Walk pit = pi,t−1 + rit mit unkorrelierten Renditeinnovationen angesetzt.
- Ohne Messfehler ist yt ein ARIMA(0,1,0). Mit Messfehler bleibt der Differenzoperator erhalten: (1 minus B) yt gleich (1 minus θ B) at, mit Betrag von θ kleiner 1.
- Ist θ negativ, lässt sich das ARIMA(0,1,1) immer noch als Zustandsraum schreiben, dann aber ohne Beobachtungsfehler, σe gleich 0.
- Im zeitvariablen CAPM sind die Übergänge von Alpha und Beta Random Walks ohne zusätzlichen stationären AR-Term: αt plus 1 gleich αt plus ηt und βt plus 1 gleich βt plus εt.
- Für die Trendkomponente wird üblicherweise ein nichtstationäres Modell verwendet, das eine doppelte Einheitswurzel haben kann: μt plus 1 gleich μt plus βt plus ηt und βt gleich βt minus 1 plus ςt.
- Ist nur die Varianz der Steigungsinnovation null, bleibt eine einfache Einheitswurzel: μt ist ein Random Walk mit Drift β1.
- Sind die Varianzen von Steigungs- und Niveauinnovation beide null, entfällt die Einheitswurzel und μt ist ein linearer deterministischer Trend.
- Die Startwerte μ1 und β1 sind normal mit Mittel null und Varianz ξ, wobei ξ eine große reelle Zahl ist, zum Beispiel 10 hoch 8.
- Wegen Unit-Root-Nichtstationarität sind die abhängige und die unabhängige Variable die wöchentlichen Änderungen der dreijährigen und der einjährigen Treasury Constant Maturity Rate, nicht die Zinsniveaus.
- Die Originalzinsen rit werden in Prozent gemessen; die Änderungen laufen vom 5. Januar 1962 bis zum 10. April 2009.

## Funktionsweise

- Der ADF-Test ist ein Unit-Root-Test: die Null ist λ gleich 0, und nur ein hinreichend negativer Wert von λ/SE(λ) verwirft sie.
- Die kritischen Werte hängen vom Stichprobenumfang ab und davon, ob ein von null verschiedener Mittelwert oder ein stetiger Drift angenommen wird.
- Im praktischen Handel wird der Driftterm β gleich 0 gesetzt, weil ein konstanter Drift meist klein gegen die täglichen Schwankungen ist.
- Der zweite adf-Parameter 0 bedeutet einen von null verschiedenen Offset und einen Drift von null, der dritte Parameter ist die Lag-Zahl.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Ein VAR(1) ist genau dann schwach stationär, wenn alle Nullstellen der Determinante von I minus ΦB außerhalb des Einheitskreises liegen, also betragsmäßig größer als 1 sind. Dasselbe gilt für ein VAR(p) mit der Determinante des Matrixpolynoms Φ(B).
- Liegt ein Eigenwert von Φ nicht betragsmäßig unter 1, konvergiert Φ hoch j nicht gegen null: die Potenz explodiert oder läuft gegen eine von null verschiedene Matrix.

## Risiken und Grenzen

- Phillips, Wu und Yu (2011) sagen, Standard-Unit-Root-Tests können einen stationären Prozess und ein periodisch zusammenbrechendes Blasenmodell nicht wirksam unterscheiden.
- Bei einer unit-root-nichtstationären Reihe konvergiert das R² einer AR(1)-Anpassung mit wachsendem Stichprobenumfang gegen 1, unabhängig vom wahren Modell von rt; ein größeres R² bedeutet eine engere Anpassung nur bei einer stationären Zeitreihe.

## Beispiele

- Für USD.CAD mit einem Lag ist die ADF-t-Statistik minus 1,840744, die AR(1)-Schätzung 0,994120, und die kritischen Werte sind minus 3,458, minus 2,871 und minus 2,594; die Unit-Root-Null wird nicht verworfen.
- λ ist trotzdem negativ, die Reihe trendet also zumindest nicht.
- Im CADF-Test von EWC auf EWA ist die t-Statistik minus 3,64346635 und die AR(1)-Schätzung minus 0,020411; die Null λ gleich 0 wird auf 95 Prozent verworfen, der kritische Wert ist minus 3,359.
- Der augmentierte Dickey-Fuller-Test weist den VIX mit 99 Prozent Sicherheit als stationär aus.
- Der ADF-Test weist die back-adjustierten Front-Month-Kurse von VX als definitiv nicht mean-reverting aus.
- Der ADF-Test des 12-Monats-Log-Kalender-Spreads von CL findet Stationarität mit 99 Prozent Wahrscheinlichkeit und eine Halbwertszeit von 36 Tagen.
- Ein ADF-Test zeigt den VIX mit 99 Prozent Sicherheit als stationär. Derselbe Test zeigt, dass die back-adjustierten Frontmonatskurse von VX definitiv nicht mean-reverten.
- Der 12-Monats-Log-Kalenderspread von CL ist im ADF-Test mit 99 Prozent stationär, bei einer Halbwertszeit von etwa 36 Tagen.
- Die Halbwertszeit kommt aus der Regression der Änderung der Rollrendite auf ihren verzögerten Wert und ist minus log(2) geteilt durch den Steigungskoeffizienten.
- Für das logarithmierte vierteljährliche US-BIP von 1947.I bis 2008.IV wird die Einheitswurzel nicht verworfen: ADF minus 1,701, p-Wert 0,4297, Lagordnung 10, geschätztes β gleich 0,9992.
- In R beträgt die Dickey-Fuller-Statistik dieser Reihe minus 1,6109 mit p-Wert 0,4569.
- Für den Logarithmus des täglichen S&P 500 vom 3. Januar 1950 bis 16. April 2008, 14462 Beobachtungen, mit Konstante, linearem Trend und 15 Lags beträgt die ADF-Statistik minus 1,998 mit p-Wert 0,602; die Einheitswurzel wird nicht verworfen.
- In diesem S&P-Test ist die Konstante signifikant, der Zeittrend auf dem 5-Prozent-Niveau nicht und auf dem 10-Prozent-Niveau signifikant; die Reihe hat damit eine Einheitswurzel und einen positiven Drift, aber keinen starken Beleg für einen Zeittrend.
- In R ist die Statistik bei 2 Lags minus 2,0179 mit p-Wert 0,5708 und bei 15 Lags minus 1,9946 mit p-Wert 0,5807; S-Plus gibt Lag 1 als minus 0,0005 mit t-Wert minus 1,9977, die Konstante 0,0019 mit p-Wert 0,0168 und den Zeitkoeffizienten 0,0020 mit p-Wert 0,0642.
- Der saisonbereinigte implizite Preisdeflator des vierteljährlichen US-BIP könnte doppelte Einheitswurzeln haben; der Mittelwert der zweiten Differenz ist nicht signifikant von null verschieden.
- Die logarithmierten 1- und 3-jährigen Treasury-Sätze erscheinen einheitswurzel-nichtstationär. Näherungsweise gilt (1 minus B) r3t gleich 0,03 plus (1 plus 0,47 B) a3t und (1 minus B)(1 minus 0,82 B) r1t gleich 0,03 minus 0,97 B mal (1 minus B) r3t plus (1 minus 0,9 B) a1t plus 1,66 B a3t.
- Die Simulation von (8.31) mit 200 Beobachtungen und Einheits-Schockkovarianz zeigt in beiden Komponenten hohe Autokorrelationen und das Erscheinungsbild einer Einheitswurzel, obwohl nur eine Einheitswurzel im System liegt.
- Augmented-Dickey-Fuller-Tests verwerfen die Unit Root der wöchentlichen 3- und 6-Monats-Treasury-Bill-Zinsen nicht. Bei einem AR(3) sind die Teststatistiken −2,34 und −2,33, der p-Wert liegt etwa bei 0,16.
- Auf den Residuen der Regression der BHP-Logpreise auf die VALE-Logpreise verwirft ein Augmented-Dickey-Fuller-Test mit AR(2) die Unit-Root-Hypothese: die Statistik ist −6,04, der p-Wert 0,01.
- Dieselbe Residualreihe ist als stationäres AR(2) mit den Faktoren (1 − 0,935 B) und (1 − 0,130 B) darstellbar. Der Johansen-Test findet anschließend genau einen Kointegrationsvektor der beiden Logpreise.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 96–115 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-006-p096-p115|S. 96–115]]
- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 52–71 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-004-p052-p071|S. 52–71]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 119–138 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-009-p119-p138|S. 119–138]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 138–143 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-010-p138-p143|S. 138–143]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 77–96 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-005-p077-p096|S. 77–96]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 96–115 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-006-p096-p115|S. 96–115]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 115–134 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-007-p115-p134|S. 115–134]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 153–172 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-009-p153-p172|S. 153–172]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 191–210 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-011-p191-p210|S. 191–210]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 419–438 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-023-p419-p438|S. 419–438]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 438–457 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-024-p438-p457|S. 438–457]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 457–476 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-025-p457-p476|S. 457–476]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 476–495 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-026-p476-p495|S. 476–495]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 571–590 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-031-p571-p590|S. 571–590]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 590–609 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-032-p590-p609|S. 590–609]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 609–628 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-033-p609-p628|S. 609–628]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 628–647 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-034-p628-p647|S. 628–647]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 647–666 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-035-p647-p666|S. 647–666]]

## Verwandte Themen

- Alexander beschreibt diesen Test in Market Models auf den Seiten 324–328 und 353–361.
- Der Operator YY machte, im Unterschied zur Kointegrationsanalyse, keinen expliziten Test darauf, ob die Residuen stationär sind.
