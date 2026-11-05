---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Modelle"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# ARIMA


## Kurzdefinition

- Lässt man im AR-Polynom eines ARMA-Modells die charakteristische Wurzel 1 zu, entsteht das autoregressive integrierte Moving-Average-Modell; es ist unit-root-nichtstationär, weil das AR-Polynom eine Einheitswurzel hat.
- McLeod und Li (1983) prüfen ein ARMA(p, q), indem sie die Ljung-Box-Statistik auf die Autokorrelationen der quadrierten Residuen anwenden.
- Das lokale Trendmodell ohne Messfehler, σe gleich 0, ist ein ARIMA(0,1,0), weil dann yt gleich dem Random Walk μt ist. Mit Messfehler, σe größer 0, ist yt ein ARIMA(0,1,1).

## Kernaussagen

- Wie ein Random Walk hat ein ARIMA-Modell starkes Gedächtnis: die ψ-Koeffizienten seiner Moving-Average-Darstellung fallen nicht gegen null, und ein vergangener Schock wirkt dauerhaft auf die Reihe.
- Der übliche Umgang mit dieser Unit-Root-Nichtstationarität ist das Differenzieren.
- yt ist ein ARIMA(p, 1, q)-Prozess, wenn die Änderung ct gleich yt minus yt−1, also (1 minus B) yt, einem stationären und invertierbaren ARMA(p, q) folgt.
- In der Finanzwirtschaft gelten Preisreihen gewöhnlich als nichtstationär, die Logrendite ln(Pt) minus ln(Pt−1) aber als stationär; die Logpreisreihe ist dann unit-root-nichtstationär und kann als ARIMA-Prozess behandelt werden.
- Die erste Differenz ct gleich yt minus yt−1 heißt erste differenzierte Reihe; eine Reihe in eine stationäre zu überführen, indem man ihre Änderungen betrachtet, heißt Differenzieren.
- Sind yt und seine erste Differenz unit-root-nichtstationär, die zweite Differenz st gleich yt minus 2 yt−1 plus yt−2 aber schwach stationär, hat yt eine doppelte Einheitswurzel; folgt st einem ARMA(p, q), ist yt ein ARIMA(p, 2, q).
- Hat diese zweite Differenz einen von null verschiedenen Mittelwert, trägt yt eine quadratische Zeitfunktion, deren quadratischer Koeffizient mit dem Mittelwert der zweiten Differenz zusammenhängt.
- Die saisonbereinigte Reihe des impliziten Preisdeflators des vierteljährlichen US-Bruttoinlandsprodukts könnte doppelte Einheitswurzeln haben; der Mittelwert der zweiten Differenz ist aber nicht signifikant von null verschieden.
- Box, Jenkins und Reinsel (1994) behandeln viele Eigenschaften allgemeiner ARIMA-Modelle.
- Ein GARCH-Modell lässt sich als Anwendung der ARMA-Idee auf die quadrierte Schockreihe a t quadrat lesen: die Darstellung mit dem Martingaldifferenz-Fehler eta t ist eine ARMA-Form für diese Quadrate.
- Die Mehrschrittprognose der bedingten Varianz eines GARCH(1,1) stimmt mit der eines ARMA(1,1) überein, dessen AR-Polynom 1 minus (alpha 1 plus beta 1) mal B ist.
- Hat dieses AR-Polynom eine Einheitswurzel, liegt ein IGARCH-Modell vor; analog zu ARIMA-Modellen bleibt die Wirkung vergangener quadrierter Schocks eta, t minus i, gleich a, t minus i, quadrat minus sigma, t minus i, quadrat auf a t quadrat dauerhaft.
- Begrenzte Erfahrung zeigt, dass ln(RV_t), der Logarithmus der realisierten Volatilität, oft näherungsweise einem gaußschen ARIMA(0,1,q) folgt, das für Prognosen verwendet werden kann.
- Für die erste Differenz der saisonbereinigten monatlichen US-Arbeitslosenquote lautet das ARIMA (1 − 1,13B + 0,27B²)(1 − 0,51B¹²) y_t = (1 − 1,12B + 0,44B²)(1 − 0,82B¹²) a_t, mit σ̂_a = 0,187.
- Alle Schätzungen außer dem AR(2)-Koeffizienten sind auf dem 5-Prozent-Niveau signifikant. Dessen t-Ratio beträgt −1,66. Die Residuen ergeben Q(12) = 12,3 und Q(24) = 25,5 mit p-Werten 0,056 und 0,11, bei χ² mit 6 und 18 Freiheitsgraden. Das Modell beschreibt die serielle Abhängigkeit angemessen.
- Die saisonalen AR- und MA-Koeffizienten sind hoch signifikant, Standardfehler 0,049 und 0,035, obwohl die Reihe saisonbereinigt ist.
- Die Einschrittprognose dieses ARIMA für die Arbeitslosenquote im April 2009 beträgt 8,8 und liegt nahe am späteren Wert 8,9.
- Die MA-Darstellung ist näherungsweise ψ(B) = 1 + 0,01B + 0,18B² + 0,20B³ + 0,18B⁴ + 0,15B⁵ + ⋯. Deshalb erscheint im anschließenden TAR kein Term in y_{t−1}.
- Ein rein stochastischer Prozess ist linear, wenn er die MA-Darstellung x_t = μ + Σ_{i=0}^{∞} ψ_i a_{t−i} mit ψ_0 = 1 besitzt. Der ARMA-Prozess ist linear, weil er diese Darstellung hat. Ist σ²_a Σ ψ²_i endlich, ist x_t schwach stationär.
- Q(m) = T(T+2) mal die Summe von i = 1 bis m von ρ̂²_i(a²_t)/(T−i); bei angemessenem linearem Modell ist Q(m) asymptotisch chi-quadrat-verteilt mit m−p−q Freiheitsgraden.
- Die Nullhypothese lautet β1 = … = βm = 0 in der Regression a²_t = β0 + β1 a²_{t−1} + … + βm a²_{t−m} + e_t für t = m+1, …, T.
- Weil Q(m) aus Residuen und nicht direkt aus den beobachteten Renditen berechnet wird, betragen die Freiheitsgrade m−p−q.
- Diese Q-Statistik erkennt bedingte Heteroskedastizität von a_t und ist asymptotisch äquivalent zum Lagrange-Multiplikator-Test von Engle (1982) für ARCH-Modelle.
- Für die monatlichen IBM-Logrenditen von Januar 1926 bis Dezember 1997 lautet das angepasste AR-Modell r_t = 1,101 + 0,077 r_{t−1} + a_t mit σ_a = 6,61.
- Für die monatlichen Logrenditen des CRSP equal-weighted Index von 1926 bis 1997 mit 864 Beobachtungen lautet das lineare Modell (1 − 0,180 B + 0,099 B³ − 0,105 B⁹) r_{3t} = 0,0086 + a_{3t}.
- Für den CRSP value-weighted Index im selben Zeitraum lautet das Modell (1 − 0,098 B + 0,111 B³ − 0,088 B⁵) r_{4t} = 0,0078 + a_{4t}.
- Für die monatlichen IBM-Logrenditen 1926 bis 1997 im Nichtlinearitätstest lautet das Modell (1 − 0,077 B) r_{5t} = 0,011 + a_{5t}, ebenfalls mit 864 Beobachtungen.
- Montgomery et al. (1998) modellieren die Änderung der vierteljährlichen US-Arbeitslosenquote als (1 − 0,31 B⁴)(1 − 0,65 B) Δx_t = (1 − 0,78 B⁴) a_t mit σ̂²_a = 0,090; die Standardfehler der drei Koeffizienten sind 0,11, 0,06 und 0,07.
- Dieses Arbeitslosenmodell bleibt saisonal, obwohl die Reihe saisonbereinigt wurde; die Saisonbereinigung hat die Saisonalität nicht entfernt.
- Bei Finanzzeitreihen wird zuerst ein angemessenes lineares Modell gebaut; Ljung-Box-Statistiken und Engles Test prüfen darauf bedingte Heteroskedastizität, bevor eine nichtlineare Modellklasse gewählt wird.
- Das ACD(r, s)-Modell für bereinigte Handelsdauern lässt sich als ARMA-Prozess mit nicht-gaußschen Innovationen schreiben: x_i = ω + Σ_{j=1}^{max(r,s)} (γ_j + ω_j) x_{i−j} − Σ_{j=1}^{s} ω_j η_{i−j} + η_i.
- Dabei ist η_i = x_i − ψ_i eine Martingaldifferenzfolge, also E(η_i | F_{i−1}) = 0, und Koeffizienten jenseits der Ordnungen r und s sind null.
- Aus dieser Darstellung folgt bei schwacher Stationarität E(x_i) = ω / [1 − Σ (γ_j + ω_j)]; verlangt werden ω > 0 und Σ (γ_j + ω_j) < 1, damit die erwartete Dauer positiv ist.
- Für die mittelwertbereinigten täglichen IBM-Logrenditen wird keine ARMA-Mittelgleichung angesetzt, weil die seriellen Korrelationen im angepassten AR(2)–GARCH(1,1) von Beispiel 7.3 schwach sind.
- Im bivariaten Beispiel (8.31) ist jede Komponente einheitswurzel-nichtstationär und folgt einem ARIMA(0,1,1). Das transformierte y1t folgt ebenfalls einem univariaten ARIMA(0,1,1), während y2t weißes Rauschen ist, y2t gleich b2t.
- Das Randmodell eines VMA(q) ist ein univariates MA(q), weil die Autokorrelationsfunktion der Komponente nach Lag q verschwindet.
- Für ein k-dimensionales VAR(p) sind die Randmodelle höchstens ARMA der Ordnungen kp und (k minus 1) mal p. Für ein k-dimensionales VARMA(p, q) ist die Obergrenze ARMA[kp, (k minus 1)p plus q]; die tatsächliche Randordnung kann deutlich niedriger sein.
- Mit Messfehler erfüllt yt die Gleichung (1 minus B) yt gleich (1 minus θ B) at, wobei at gaußsches weißes Rauschen mit Mittel null und Varianz σ²a ist. θ und σa werden durch σe und ση bestimmt.
- Für wt gleich (1 minus B) yt gilt: wt ist gaußsch, Var(wt) gleich 2σ²e plus σ²η, Cov(wt, wt minus 1) gleich minus σ²e, und Cov(wt, wt minus j) gleich 0 für j größer 1. Damit ist wt ein MA(1).
- Gleichsetzen von Varianz und Lag-1-Autokovarianz liefert (1 plus θ²) σ²a gleich 2σ²e plus σ²η und θ σ²a gleich σ²e. Die quadratische Gleichung in θ hat zwei Lösungen; gewählt wird die mit Betrag von θ kleiner 1.
- Das Zustandsraummodell der Gleichungen (11.1) und (11.2) ist zugleich das einfache exponentielle Glättungsmodell aus Kapitel 2.
- Für ein ARIMA(0,1,1) mit positivem θ lassen sich σ²e und σ²η aus diesen Identitäten lösen und ein lokales Trendmodell gewinnen. Ist θ negativ, bleibt die Zustandsraumform ohne Beobachtungsfehler, also σe gleich 0.
- Ein ARIMA-Modell lässt sich auf viele Arten in ein Zustandsraummodell überführen. Allein aus den Daten ist die Wahl zwischen ARIMA und linearem Zustandsraum nicht entscheidend; Ziel, Sachfrage und Erfahrung spielen mit.
- Für die logarithmierte realisierte Intraday-Volatilität von Alcoa, 2. Januar 2003 bis 7. Mai 2004, 340 Beobachtungen, lautet das ARIMA(0,1,1): (1 minus B) yt gleich (1 minus 0,858 B) at, geschätzte Standardabweichung von at 0,5184, Standardfehler von θ-Dach 0,028.
- Die Residuen dieses ARIMA(0,1,1) haben Q(12) gleich 12,4 bei einem p-Wert von 0,33, also keine signifikante serielle Korrelation. Die quadrierten Residuen haben Q(12) gleich 8,2 bei einem p-Wert von 0,77, also keine ARCH-Effekte.
- Weil θ-Dach positiv ist, wird das Modell in ein lokales Trendmodell überführt. Die Maximum-Likelihood-Schätzungen sind ση-Dach gleich 0,0735 und σe-Dach gleich 0,4803. Aus den Relationen (11.4) und (11.5) folgen σe gleich 0,480 und ση gleich 0,0736.
- Ein mittelwertfreies ARMA(p, q) lautet φ(B) yt gleich θ(B) at, at normal mit Mittel null und Varianz σ²a. Mit m gleich max(p, q plus 1) werden φi für i größer p und θj für j größer q gleich null gesetzt, insbesondere θm gleich 0.
- Akaike (1975) nimmt als Zustand die kleinste Menge von Variablen, die am Prognoseursprung t alle nötige Information enthält: st gleich (yt|t, yt plus 1|t, bis yt plus m minus 1|t)′, wobei yt plus j gegeben t der bedingte Erwartungswert E(yt plus j | Ft) ist.
- Weil yt|t gleich yt ist, lautet die Beobachtungsgleichung yt gleich Z st mit Z gleich (1, 0, bis 0) der Länge m.
- Die MA-Gewichte erfüllen ψ0 gleich 1, ψ1 gleich φ1 minus θ1 und ψ2 gleich φ1 ψ1 plus φ2 minus θ2. Allgemein ist ψ m minus 1 die Summe i von 1 bis m minus 1 von φi ψ m minus 1 minus i, minus θ m minus 1.
- Die Prognoseaktualisierung lautet für j größer 0: yt plus j gegeben t plus 1 gleich yt plus j gegeben t plus ψ j minus 1 mal at plus 1. Die neue Information steckt in der Innovation at plus 1, das Gewicht ist ψ j minus 1.
- Die Übergangsgleichung nach Akaike ist st plus 1 gleich T st plus R ηt, ηt gleich at plus 1 und normal mit Varianz σ²a. Die letzte Zeile von T enthält φm bis φ1, darüber eine Verschiebung. R enthält 1, ψ1, bis ψ m minus 1.
- Harvey (1993, Abschnitt 4.4) beginnt mit einem Zustand, dessen erstes Element yt ist, und zerlegt das ARMA(m, m minus 1) so, dass yt plus 1 gleich φ1 s1t plus s2t plus ηt mit ηt gleich at plus 1.
- Harvey (1993, Abschnitt 4.4) stellt ein ARMA mit m gleich max(p, q plus 1) als Zustandsraum ohne Messfehler dar. Das erste Zustandselement ist yt. dt, ct und Ht sind null. AR- und MA-Koeffizienten stehen direkt in den Systemmatrizen.
- Die Gleichungen sind st plus 1 gleich T st plus R ηt, ηt normal mit Varianz σ²a, und yt gleich Z st mit Z gleich (1, 0, bis 0). R ist der Spaltenvektor (1, minus θ1, bis minus θ m minus 1). Die erste Spalte von T enthält φ1 bis φm, rechts daneben eine Verschiebung.
- Aoki (1987) schreibt ein reines MA-Modell mit dem Zustand (at minus q, bis at minus 1). Die Innovation at steht dann sowohl in der Zustandsgleichung als auch in der Beobachtungsgleichung yt gleich (minus θq, bis minus θ1) mal st plus at.
- Für ein reines AR definiert Aoki den Zustand einmal als (zt minus p plus 1, bis zt) und einmal so, dass at aus dem letzten Element entfernt ist. In der zweiten Form steht at wieder in Übergangs- und Beobachtungsgleichung.
- Für ein ARMA(p, q) mit q kleiner p setzt Aoki eine Hilfsreihe zt gleich at geteilt durch φ(B), also φ(B) zt gleich at und yt gleich θ(B) zt, und baut daraus die Beobachtungsgleichung.
- Es gibt viele Zustandsraumdarstellungen eines ARMA-Modells. Für Schätzung und Prognose genügt eine beliebige davon.
- Für ein zeitinvariantes Zustandsraummodell folgt aus dem Satz von Cayley-Hamilton, dass die Beobachtung yt einem ARMA(m, m) folgt, wobei m die Dimension des Zustandsvektors ist.
- GetSsfArma verwendet Harveys Darstellung. Für das stationäre AR(1) yt gleich 0,6 yt minus 1 plus at, at normal mit Varianz 0,4 zum Quadrat, setzt das Programm die Startvarianz gleich Var(yt) gleich 0,4 zum Quadrat geteilt durch (1 minus 0,6 zum Quadrat) gleich 0,25 und den Startmittelwert gleich 0.
- Das Beispiel-ARMA(2,1) ist yt gleich 1,2 yt minus 1 minus 0,35 yt minus 2 plus at minus 0,25 at minus 1, at normal mit Varianz 1,1 zum Quadrat. T hat die erste Zeile 1,2 und 1 und die zweite Zeile minus 0,35 und 0, Z ist (1, 0).
- In SsfPack lautet das MA-Polynom 1 plus θ1 B plus bis plus θq B hoch q, nicht die literaturübliche Form 1 minus θ1 B minus bis minus θq B hoch q.
- Im ARMA(2,1)-Beispiel ist s1t gleich yt und s2t gleich minus 0,35 yt minus 1 minus 0,25 yt minus 2. Die Kovarianz von (s1t, s2t)′ steht in mSigma.
- Aufgabe 11.2 verlangt, an die Logarithmen der realisierten Tagesvolatilität von Alcoa vom 2. Januar 2003 bis 7. Mai 2004 ein ARIMA(0,1,1)-Modell anzupassen; die Reihe ist aus 20-Minuten-Intraday-Logrenditen konstruiert.
- Die j-Schritt-Prognose eines Zustandsraummodells ist analog zu ARMA-Modellen der bedingte Erwartungswert yt(j) = E(yt+j | Ft).
- Moving-Average-Parameter eines ARMA-Modells sind nichtlineare Parameter; ihre bedingte Posterior hat keine geschlossene Form, sodass Gibbs-Sampling selbst mit Metropolis–Hastings aufwendig wird.
- Für die wöchentlichen US-Treasury-Zinsänderungen wurde in Kapitel 2 eine lineare Regression mit MA(1)-Fehler verwendet; hier wird stattdessen ein AR(2)-Fehlerprozess angesetzt.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- Im Vergleich der VaR-Verfahren für die täglichen IBM-Logrenditen werden ein gaußsches AR(2)–GARCH(1,1) und ein AR(2)–GARCH(1,1) mit standardisierter Student-t-Verteilung mit 5 Freiheitsgraden verwendet.

## Regeln und Kriterien


## Risiken und Grenzen

- Überdifferenzierung kann entstehen, wenn einzelne Komponenten eines kointegrierten Systems differenziert werden. Vermutet man das, wird die exakte Maximum-Likelihood-Methode wichtig.

## Beispiele

- Die Logarithmen der 1- und 3-jährigen US-Treasury-Constant-Maturity-Sätze, April 1953 bis Januar 2001, lassen sich näherungsweise mit Differenzen schreiben: (1 minus B) r3t gleich 0,03 plus (1 plus 0,47 B) a3t, und (1 minus B)(1 minus 0,82 B) r1t gleich 0,03 minus 0,97 B mal (1 minus B) r3t plus (1 minus 0,9 B) a1t plus 1,66 B a3t.
- Die Residuen der Kleinste-Quadrate-Regression der BHP- auf die VALE-Logpreise werden als AR(2) ohne Mittelwert angepasst, im Code als arima mit Ordnung (2, 0, 0): (1 − 0,805 B − 0,122 B²) ŵt = at mit σa = 0,018.
- Die Code-Schätzung lautet ar1 = 0,8051 mit Standardfehler 0,0322 und ar2 = 0,1219 mit Standardfehler 0,0325; die geschätzte Innovationsvarianz ist 0,0003326.
- Das AR(2) faktorisiert zu (1 − 0,935 B)(1 − 0,130 B) ŵt = at. Die Kehrwerte der Beträge der charakteristischen Wurzeln sind 0,9353661 und 0,1302870.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 58–77 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-004-p058-p077|S. 58–77]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 96–115 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-006-p096-p115|S. 96–115]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 153–172 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-009-p153-p172|S. 153–172]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 191–210 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-011-p191-p210|S. 191–210]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 229–248 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-013-p229-p248|S. 229–248]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 267–286 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-015-p267-p286|S. 267–286]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 381–400 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-021-p381-p400|S. 381–400]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 400–419 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-022-p400-p419|S. 400–419]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 438–457 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-024-p438-p457|S. 438–457]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 476–495 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-026-p476-p495|S. 476–495]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 514–533 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-028-p514-p533|S. 514–533]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 571–590 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-031-p571-p590|S. 571–590]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 590–609 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-032-p590-p609|S. 590–609]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 609–628 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-033-p609-p628|S. 609–628]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 628–647 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-034-p628-p647|S. 628–647]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 647–666 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-035-p647-p666|S. 647–666]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 666–685 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-036-p666-p685|S. 666–685]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 685–704 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-037-p685-p704|S. 685–704]]

## Verwandte Themen
