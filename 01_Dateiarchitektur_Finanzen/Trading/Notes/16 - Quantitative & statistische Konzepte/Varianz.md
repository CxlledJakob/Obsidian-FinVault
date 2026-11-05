---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Statistik"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Varianz


## Kurzdefinition

- Varianz ist der Fehler aus der Empfindlichkeit gegen kleine Änderungen der Trainingsmenge. Ist sie hoch, hat der Algorithmus überangepasst und Rauschen mit Signal verwechselt.
- Noise ist die Varianz der beobachteten Werte, etwa durch unvorhersehbare Änderungen oder Messfehler, und lässt sich durch kein Modell erklären.
- Die Inverse-Varianz-Allokation ist optimal, wenn die Kovarianzmatrix diagonal ist: Das Gewicht ist dann proportional zum Kehrwert der eigenen Varianz.
- Für den charakteristischen Vektor aus Einsen ist die Lösung des quadratischen Programms das Minimum-Varianz-Portfolio.
- Die Varianz der Logpreisänderung über die Spanne τ ist das Mittel von |z(t+τ) minus z(t)| zum Quadrat, mit z gleich log(y).
- Das zweite zentrale Moment, bezeichnet mit σ²x, misst die Streuung von X und heißt Varianz. Die positive Quadratwurzel der Varianz ist die Standardabweichung.
- Die ersten zwei Momente einer Zufallsvariablen legen eine Normalverteilung eindeutig fest; für andere Verteilungen sind auch höhere Momente von Interesse.

## Kernaussagen

- Der mittlere quadratische Fehler zerlegt sich in den quadrierten Bias, die Varianz des Schätzers und die Rauschvarianz. Wegen des Rauschens kann er nicht null werden.
- Der Hauptvorteil von Bagging ist, die Varianz der Prognosen zu senken und damit Overfitting zu begegnen.
- Die Varianz des Mittelwerts von N Einzelprognosen ist die mittlere Einzelvarianz mal (mittlere Korrelation plus (1 minus diese Korrelation) geteilt durch N).
- Diese Varianz sinkt nur, solange die mittlere Korrelation unter 1 liegt, und geht gegen die Einzelvarianz, wenn die Korrelation gegen 1 geht.
- Sequenzielles Bootstrap soll möglichst unabhängige Stichproben liefern, die Korrelation senken und damit die Varianz von Bagging-Klassifikatoren verringern.
- Werden richtige Prognosen als 1 gezählt, ist ihre Zahl im Mittel N mal p und ihre Varianz N mal p mal (1 minus p).
- Bei schlechten Einzellernern, deren Trefferquote weit unter 1/k liegt, bleibt das Mehrheitsvotum schlecht, die Varianz ist aber geringer.
- Bagging senkt eher die Varianz als den Bias, weil eine sehr kleine Korrelation leichter zu erreichen ist als eine Trefferquote über 1/k.
- Redundante Beobachtungen machen die Bootstrap-Ziehungen nahezu gleich und treiben die Korrelation gegen 1. Dann sinkt die Varianz nicht, unabhängig von N.
- Entscheidungsbäume erhöhen die Prognosevarianz durch Overfitting. Der Random Forest ist darauf angelegt, sie zu senken, und tut das ohne Overfitting, solange die Korrelation unter 1 bleibt.
- Frühes Stoppen schlecht skalierender Basisschätzer erhöht die Varianz der Einzelergebnisse. Zusätzliche unabhängige Schätzer im Bagging können diesen Anstieg mehr als ausgleichen.
- CLA minimiert die Varianz in der Stichprobe und hat dort die geringere Standardabweichung, 0,4486 gegen 0,4640.
- Außer Stichprobe hat CLA trotzdem die höchste Varianz der drei Verfahren.
- Die Varianzen der Portfoliorenditen außer Stichprobe betragen 0,1157 für CLA, 0,0928 für das Inverse-Varianz-Portfolio und 0,0671 für Hierarchical Risk Parity.
- CLA liegt damit 72,47 Prozent und das Inverse-Varianz-Portfolio 38,24 Prozent über der Varianz von Hierarchical Risk Parity.
- Bei mittleren Renditen nahe 0 verbessert diese Varianzreduktion die Sharpe-Ratio einer CLA-Strategie um etwa 31,3 Prozent.
- Die Annahme einer diagonalen Kovarianzmatrix stabilisiert das Inverse-Varianz-Portfolio, seine Varianz bleibt aber deutlich höher.
- Wird die ADF-Null auf Rohpreisen verworfen, haben die Preise eine endliche Varianz, und die Renditevolatilität muss mit steigenden Preisen fallen und mit fallenden steigen.
- Bei Logpreisen bedingen die Preisniveaus den Renditemittelwert, nicht die Renditevolatilität.
- Ist die Renditevarianz invariant zum Preisniveau, wird ein ADF auf Rohpreisen strukturell heteroskedastisch.
- Beim geometrischen Random Walk ist diese Varianz proportional zu τ, bei Mean Reversion oder Trend proportional zu τ hoch 2H.
- Stationarität heißt, dass die Varianz sublinear in der Zeit wächst und nicht, dass sie zeitunabhängig ist.
- Auch für 0 kleiner H kleiner 0,5 steigt die Varianz mit der Zeit, nur langsamer als bei einem geometrischen Random Walk.
- Manager, deren einziges Ziel das langfristige Nettovermögen ist, achten nicht auf Drawdowns und auf die Volatilität der Renditen.
- Varianz, mittlere absolute Abweichung und Standardabweichung sind weit verbreitete Streuungsmaße und im klassischen statistischen Ansatz wichtig.
- Streuungsmaße beschreiben, wie weit die Beobachtungen einer Stichprobe um ihre zentrale Tendenz liegen, und quantifizieren damit die Breite einer Häufigkeitsverteilung.
- Zentrale Tendenz und Variation sind unabhängige Merkmale einer Häufigkeitsverteilung. Dieselbe Streuung kann mit verschiedenen Mittelwerten einhergehen, derselbe Mittelwert mit verschiedener Streuung, und beides kann zugleich verschieden sein.
- Die Streuung der Stichprobenverteilung des Mittelwerts hängt von der Variation in den Daten der Elternpopulation ab. Je größer diese Variation, desto größer die Streuung der Stichprobenverteilung.
- Ist die Variation in der Population null, ist auch die Variation der Stichprobenmittel null, und die Stichprobenverteilung hat keinerlei Streuung.
- Ist die Variation zwischen den Individuen der Population groß, variieren die Stichprobenmittel stärker, und die Stichprobenverteilung wird breit.
- Varianz, mittlere absolute Abweichung und Standardabweichung sind weit verbreitete Streuungsmaße der klassischen Statistik. Sie quantifizieren die Breite einer Häufigkeitsverteilung.
- Die Varianz ist neben Mittelwert, Median und Standardabweichung ein gebräuchlicher Punktschätzer aus einer Stichprobe.
- Je größer die Variabilität der täglichen Regelrenditen in der Grundgesamtheit, desto breiter ist die Stichprobenverteilung der mittleren Rendite, und je mehr Beobachtungen, desto schmaler ist sie.
- Die Reduktion einer großen Stichprobe liefert zusammenfassende Statistiken, darunter den Stichprobenmittelwert, die Stichprobenvarianz und weitere Maße, die die gesamte Menge beschreiben.
- Ein Faktor für die Größe des Data-Mining-Bias ist die Variation der erwarteten Renditen unter den gebacktesteten Regeln.
- Je geringer diese Variation des wahren Verdienstes, desto größer der Bias; Regeln mit ähnlicher Vorhersagekraft erzeugen einen größeren Bias.
- Der fünfte Faktor des Data-Mining-Bias ist die Variation der erwarteten Renditen unter den getesteten Regeln: je niedriger die Variation der wahren Güte, desto größer der Bias.
- Haben die Regeln ähnliche Grade von Prognosekraft, ist der Data-Mining-Bias größer.
- Abbildung 6.25 stellt niedrige Varianz, alle Regeln gleiche Güte, der hohen Varianz gegenüber, bei der eine Regel deutlich überlegen ist.
- Bei gleicher erwarteter Rendite entstehen alle Unterschiede der beobachteten Performance nur durch Glück; unterscheiden sich die erwarteten Renditen, wird der Bias tendenziell kleiner und unter bestimmten Bedingungen sehr klein.
- Die Zahl der Beobachtungen beeinflusst sowohl die Breite als auch die Randdicke der Stichprobenverteilung der Performancestatistik, mit der die beste Regel ausgewählt wird.
- Je mehr Beobachtungen, desto schmaler die Stichprobenverteilung und desto kleiner der Data-Mining-Bias; je mehr Beobachtungen, desto leichter die Ränder und desto kleiner der Bias.
- Aus den vielen Out-of-Sample-Schätzungen eines Walk-Forward mit zahlreichen Folds lässt sich die Varianz der Performancestatistik bestimmen.
- Der Schrumpfungsgrad bei Markowitz und Xu hängt unter anderem davon ab, wie stark die Tagesrenditen jeder Regel um das große Mittel aller Regeln streuen und wie stark die mittlere Rendite jeder Regel um die mittlere Rendite aller Regeln streut.
- Je kleiner die Variabilität der wahren Qualität, also der erwarteten Rendite, unter den getesteten Regeln, desto größer der Data-Mining-Bias; die Zusammenfassung sagt, dieser Punkt sei experimentell nicht untersucht worden.
- Sind die Beobachtungen seriell korreliert, wie es in einer Zeitreihe vorkommen kann, sinkt die Varianz langsamer, als die Quadratwurzelregel nahelegt.
- Diese Aussage gilt, wenn die Teststatistik der Stichprobenmittelwert ist, aber sie gilt nicht allgemein.
- Bei normalverteilten Preisänderungen ist die Unsicherheit mit 10 Beobachtungen zehnmal so groß wie mit 1.000 Beobachtungen.
- Beim geometrischen Random Walk ist das Mittel von |z(t+τ) minus z(t)| zum Quadrat proportional zu τ. Für großes τ wird daraus eine Gleichheit mit Proportionalitätskonstante, für kleines τ kann die Beziehung von der Geraden abweichen.
- Bei Mean Reversion oder bei positiver Korrelation aufeinanderfolgender Preisbewegungen gilt stattdessen die Proportionalität zu τ hoch 2H, mit Hurst-Exponent H.
- Der Variance-Ratio-Test prüft, ob das Varianzverhältnis Var(τ) geteilt durch τ mal die Varianz des Einsschritts gleich 1 ist. Für USD.CAD wird die Null nicht verworfen, pValue 0,367281.
- Auch eine stationäre Reihe mit 0 < H < 0,5 hat eine Varianz, die mit der Zeit steigt, nur langsamer als beim geometrischen Random Walk. Deshalb wird eine gleitende Standardabweichung benutzt.
- Der Variance-Ratio-Test prüft die Null, dass der Hurst-Exponent wirklich 0,5 ist, also dass das Varianzverhältnis gleich 1 ist.
- Für TU verwirft dieser Test die Random-Walk-Hypothese nicht, obwohl der Hurst-Exponent 0,44 beträgt.
- Der Test kann nicht die einzelnen Zeitrahmen prüfen, in denen die Korrelationen der Renditen stärker als im Durchschnitt sind.
- Unter der Gauß-Annahme ist der Kelly-Hebel f gleich dem mittleren Excess Return m geteilt durch die Varianz s hoch 2 der Excess Returns.
- Eine unterschätzte Varianz überschätzt diesen Hebel und kann bei ausreichender Höhe zum Ruin führen; eine überschätzte Varianz führt nur zu einer untermaximalen Wachstumsrate.
- Im Allokationsbeispiel hat Strategie 1 eine annualisierte Volatilität von 26 Prozent bei 30 Prozent mittlerer Überschussrendite und Strategie 2 eine von 35 Prozent bei 60 Prozent; bei Korrelation null sind die Kelly-Hebel 4,4 und 4,9.
- Für mehrere Portfolios geht die Kovarianzmatrix der Renditen als C in F gleich C hoch minus 1 mal M ein.
- Nichtnormale stabile Verteilungen haben keine endliche Varianz; das steht im Konflikt mit den meisten Finanztheorien. Die Cauchy-Verteilung ist ein Beispiel: symmetrisch zum Median und mit unendlicher Varianz.
- Mischungen von Normalverteilungen behalten die Handhabbarkeit der Normalverteilung, haben endliche höhere Momente und können die Exzess-Kurtosis erfassen.
- Schwache Stationarität setzt endliche erste und zweite Momente voraus; dann ist γ0 = Var(rt) über die Zeit konstant.
- Die Schwankungen der Renditen ändern sich über die Zeit und treten in Clustern auf. Der Volatilitätsprozess beschreibt die Entwicklung der bedingten Varianz.
- Bei den Zinsreihen sind die Stichprobenstandardabweichungen umgekehrt proportional zur Laufzeit. Bei den Anleiherenditen steigen sie mit der Laufzeit, während die Stichprobenmittel stabil bleiben.
- Die Varianz einer schwach stationären linearen Reihe ist σa zum Quadrat mal der Summe aller quadrierten ψ-Gewichte ab i gleich 0; damit sie endlich bleibt, muss diese Summe konvergieren.
- Für ein schwach stationäres AR(1) gilt Var(rt) gleich σa zum Quadrat geteilt durch (1 minus phi1 zum Quadrat), sofern phi1 zum Quadrat kleiner als 1 ist.
- Die bedingte Varianz eines AR(1) gegeben rt−1 ist die Varianz des Schocks at und hängt nicht von rt−1 ab.
- Der bedingte Kleinste-Quadrate-Schätzer der Innovationsvarianz ist die Summe der quadrierten Residuen von t gleich p plus 1 bis T, geteilt durch T minus 2p minus 1.
- Bei der bedingten Likelihood bleibt die Koeffizientenschätzung gleich, und die Varianzschätzung wird mit (T minus 2p minus 1) geteilt durch (T minus p) multipliziert; manche Pakete teilen durch T.
- Weißes Rauschen hat endliche Varianz; gaußsches weißes Rauschen hat zusätzlich Mittel null und eine Normalverteilung mit Varianz σ zum Quadrat.
- Die Varianz eines MA(1) ist (1 plus θ1 zum Quadrat) mal σa zum Quadrat, die eines MA(q) (1 plus die Summe der quadrierten MA-Koeffizienten) mal σa zum Quadrat.
- Die Varianz eines schwach stationären ARMA(1,1) ist (1 minus 2 mal phi1 mal θ1 plus θ1 zum Quadrat) mal σa zum Quadrat, geteilt durch (1 minus phi1 zum Quadrat).
- Die Varianz des Ein-Schritt-Prognosefehlers ist σa zum Quadrat; die des Zwei-Schritt-Fehlers eines AR mit dem führenden Koeffizienten phi1 ist (1 plus phi1 zum Quadrat) mal σa zum Quadrat und damit mindestens so groß.
- Die Varianz des Zwei-Schritt-Prognosefehlers eines MA(1) ist (1 plus θ1 zum Quadrat) mal σa zum Quadrat, gleich der Varianz des Modells und mindestens so groß wie die Ein-Schritt-Varianz.
- Bei einem stationären AR(p) nähert sich die Varianz des Prognosefehlers mit wachsendem Horizont der unbedingten Varianz von rt.
- Beim MA(2) gehen die Varianzen der Prognosefehler nach zwei Schritten auf die Varianz der Reihe; beim MA(q) nach den ersten q Schritten.
- Die Varianz des l-Schritt-Prognosefehlers eines Random Walk ist l mal σa zum Quadrat und divergiert mit dem Horizont gegen unendlich; die unbedingte Varianz von pt ist deshalb unbeschränkt.
- Beim Random Walk mit Drift ist die Varianz der Summe der Schocks bis t gleich t mal σa zum Quadrat.
- Die trendstationäre Reihe hat die Varianz der stationären Restreihe, endlich und zeitlich invariant, während der Random Walk mit Drift die zeitabhängige Varianz t mal σa zum Quadrat hat.
- In der Moving-Average-Darstellung ist die Varianz des l-Schritt-Prognosefehlers (1 plus die Summe der quadrierten ψ-Gewichte von ψ1 bis ψ(l−1)) mal σa zum Quadrat und eine nichtfallende Funktion von l.
- Die Varianz von rt in derselben Darstellung ist (1 plus die Summe aller quadrierten ψ-Gewichte ab i gleich 1) mal σa zum Quadrat, und die Prognosevarianz läuft mit dem Horizont gegen diese Varianz, sobald die Reihe stationär ist und die ψ-Gewichte gegen null gehen.
- Für das multiplikative saisonale Moving-Average-Modell ist die Varianz von wt gleich (1 plus θ zum Quadrat) mal (1 plus Θ zum Quadrat) mal σa zum Quadrat.
- Die bedingte Varianz der Logrendite ist sigma t quadrat gleich dem Erwartungswert von (rt minus mü t) quadrat gegeben Ft minus 1 und gleich der bedingten Varianz des Schocks at.
- Beim ARCH(1) ist die unbedingte Varianz alpha 0 durch (1 minus alpha 1), sofern 0 kleiner oder gleich alpha 1 kleiner als 1.
- Unter Normalität ist das bedingte vierte Moment 3 mal dem Quadrat der bedingten Varianz; das unbedingte vierte Moment ist 3 alpha 0 quadrat mal (1 plus alpha 1) durch [(1 minus alpha 1) mal (1 minus 3 alpha 1 quadrat)], sofern alpha 1 quadrat kleiner als 1/3.
- Eine große bedingte Varianz erzeugt nicht notwendig eine große Realisation, sie erhöht nur die Wahrscheinlichkeit einer großen Ausprägung gegenüber einer kleineren Varianz.
- Alpha i mindestens 0 sichert, dass die bedingte Varianz für alle t positiv ist; alternativ leistet das eine quadratische Form mit nichtnegativ definiter Matrix.
- Beim Intel-ARCH(1) beträgt die unbedingte Varianz 0,0111 durch (1 minus 0,356); unter Student-t ist sie 0,0120 durch (1 minus 0,2845).
- Die unbedingte Varianz eines GARCH-Schocks ist alpha 0 geteilt durch 1 minus der Summe (alpha i plus beta i), sofern der Nenner positiv ist.
- Beim GARCH(1,1) der S&P-500-Überschussrenditen beträgt sie 0,000086 durch (1 minus 0,8511 minus 0,1216) gleich 0,00314; das vorher geschätzte AR(3) hatte die Residualvarianz 0,00333, das gemeinsame Modell vor dem Streichen der AR-Glieder die implizite Varianz 0,00317.
- Unter dem geschätzten IGARCH(1,1) derselben Reihe ist die unbedingte Varianz nicht definiert.
- Ein einzelnes künftiges Quadrat a, h plus 1, quadrat ist ein konsistenter Schätzer der bedingten Varianz, weil sein bedingter Erwartungswert diese Varianz ist, aber kein genauer Schätzer.
- Die Mehrschrittprognose der bedingten Varianz läuft gegen diese unbedingte Varianz, wenn alpha 1 plus beta 1 kleiner als 1 ist, und gegen eine Gerade mit Steigung alpha 0, wenn die Summe gleich 1 ist.
- Die bedingte Varianz eines CHARMA ist σ²_t = σ²_η + (a_{t−1}, …, a_{t−m}) Ω (a_{t−1}, …, a_{t−m})′. Sie ist automatisch positiv, weil Ω nichtnegativ definit und σ²_η positiv ist.
- Die bedingte Varianz der Monats-Logrendite zerlegt sich in die Summe der bedingten Tagesvarianzen und das Zweifache der bedingten Tageskovarianzen, sofern diese Momente existieren.
- Der Effizienzfaktor eines Volatilitätsschätzers ist das Verhältnis der Varianz des Schluss-zu-Schluss-Schätzers (C_t − C_{t−1})² zur Varianz des jeweiligen Schätzers.
- Yang und Zhang wählen k = 0,34 / [1,34 + (n+1)/(n−1)] so, dass die Varianz ihres linear kombinierten Schätzers minimal wird.
- Im RCA-Modell ist die bedingte Varianz σ²_t = σ²_a + (r_{t−1}, …, r_{t−p}) Ω_δ (r_{t−1}, …, r_{t−p})′, also eine quadratische Funktion der beobachteten verzögerten Renditen.
- Für das SV-Modell mit m = 1 hat ln(σ²_t) die Varianz σ²_v / (1 − α₁²), und E(a²_t) = exp(μ_h + σ²_h/2).
- Im GARCH(1,1) ist die Varianz von a_t gleich α₀ / [1 − (α₁ + β₁)], unter α₀ > 0, α₁ ≥ 0, β₁ ≥ 0 und α₁ + β₁ < 1.
- Die bedingte Varianz des speziellen bilinearen Modells ist [1 + Σ_{i=1}^{s} β_i a_{t−i}]² σ²_a.
- Im SETAR hat jedes Regime eine eigene Innovationsvarianz σ²_j. Die Regimeinnovationen sind unabhängig.
- Für die Existenz von E(σ⁴_t) im GARCH(1,1) muss 1 − α₁²(K_ε + 2) − (α₁ + β₁)² > 0 sein. Dann ist E(σ⁴_t) = α₀²(1 + α₁ + β₁) / {[1 − (α₁ + β₁)][1 − α₁²(K_ε + 2) − (α₁ + β₁)²]}.
- Bei normalen Innovationen existiert die Kurtosis von a_t nur, wenn 1 − 2α₁² − (α₁ + β₁)² > 0. Für ARCH(1) lautet die entsprechende Schranke 1 > 3α₁².
- Im TAR der US-Arbeitslosenänderung werden die Standardfehler der Regimeinnovationen mit 0,180 und 0,217 angegeben. Jedes Regime hat eine eigene Innovationsvarianz.
- Die Innovationen der Zustände eines Markov-Switching-Modells haben Mittel null und endliche Varianz und sind voneinander unabhängig.
- Im nichtlinearen Zustandsraummodell hat das Zustandsrauschen eine nichtnegativ definite Kovarianzmatrix Σ_u, das Beobachtungsrauschen die Varianz σ²_v, und die beiden Folgen sind unabhängig.
- Die Bandbreite der Kernregression minimiert asymptotisch den mittleren integrierten quadratischen Fehler. Dessen Integrand ist der punktweise mittlere quadratische Fehler von m̂(x).
- Für den wöchentlichen Treasury-Bill-Satz ist die geglättete Volatilität, genähert durch |y_t|, eine steigende Funktion des vorherigen Satzes und wird steiler, wenn dieser sich 10 Prozent nähert.
- Im Markov-Switching-Modell des US-GNP betragen die geschätzten Innovations-Standardabweichungen 0,816 in der Expansion und 1,017 in der Kontraktion.
- Die beiden Regime des TAR-Modells der Arbeitslosenänderung haben die Innovationen-Varianzen 0,76 und 0,165.
- Im Markov-Switching-Modell derselben Reihe sind die Innovationen-Varianzen 0,031 im Expansionszustand und 0,192 im Kontraktionszustand.
- Das lineare saisonale Benchmark derselben Reihe hat die Residualvarianz σ̂²_a = 0,090.
- Im Bispektrum geht die Innovationen-Varianz als σ²_a in die Spektraldichte p(w) = σ²_a |Γ(w)|² / (2π) ein.
- Nichtsynchroner Handel vergrößert die Varianz der beobachteten Rendite auf Var(r^o_t) = σ² + 2π μ² / (1−π).
- Im Roll-Modell ohne Änderung des fundamentalen Preises ist die Varianz der beobachteten Preisänderung S²/2.
- Folgt der fundamentale Preis einem Random Walk mit Varianz σ², ist die Varianz der beobachteten Preisänderung σ² + S²/2.
- Der Auftragsindikator hat Varianz 1.
- Die bedingte Varianz im Ordered Probit für IBM 1988 ist σ²_i = 1,0 + 0,40² Δt*_i + 0,52² AB_{i−1}.
- Für die Standard-Exponentialverteilung der EACD-Innovation gilt Var(ε_i) = 1 und E(ε²_i) = 2, und daraus folgt E(x²_i) = 2 E(ψ²_i).
- Die unbedingte Varianz des schwach stationären EACD(1,1) ist μ_x² (1 − ω1² − 2γ1 ω1) / (1 − 2γ1² − ω1² − 2γ1 ω1), mit μ_x = ω / (1 − γ1 − ω1).
- Diese Varianz ist nur zeitlich invariant, wenn 1 > 2γ1² + ω1² + 2γ1 ω1.
- Die Stichproben-Standardabweichungen der IBM-Trades 1988 implizieren Varianzen der Preisänderung, der Dauer und des Spreads von 0,753², 34,13² und 1,4625².
- Die Varianz der Exponentialverteilung mit Parameter β ist β², der Erwartungswert ist β.
- Die Varianz der Gammaverteilung mit Parametern κ und β ist κβ², der Erwartungswert ist κβ.
- Die Varianz der Weibull-Verteilung ist β² {Gamma(1 + 2/α) − [Gamma(1 + 1/α)]²}, der Erwartungswert ist β Gamma(1 + 1/α); bei α = 1 fällt sie mit der Exponentialverteilung zusammen.
- Die Varianz der standardisierten Weibull-Verteilung ist Gamma(1 + 2/α)/[Gamma(1 + 1/α)]² − 1 bei Erwartungswert 1.
- Die Momente der verallgemeinerten Gammaverteilung sind E(X^m) = β^m Gamma(κ + m/α)/Gamma(κ).
- Im PCD-Modell gilt ln(σi) = β |Di−1 + Di−2 + Di−3 + Di−4|; für IBM ist der Koeffizient 0,244 mit Standardfehler 0,182 und marginal signifikant.
- Für einen Wiener-Prozess gilt Var(wt − w0) = t.
- Für den verallgemeinerten Wiener-Prozess gilt Var(xt − x0) = σ²t bei E(xt − x0) = µt.
- Im Beweis von Itos Lemma gilt Var(σ²ϵ² Δt) = 2σ⁴ (Δt)², und (Δx)² konvergiert gegen σ² dt, wenn Δt gegen 0 geht.
- Die Varianz der Logpreisänderung von t bis T ist σ²(T − t), wenn der Preis einer geometrischen Brownschen Bewegung folgt.
- Bedingt auf Pt gilt Var(PT) = Pt² exp[2µ(T − t)] {exp[σ²(T − t)] − 1}.
- Im Beispiel mit Pt = 50, µ = 0,15 und σ = 0,40 beträgt die Preisvarianz nach sechs Monaten 2500 exp(0,3 × 0,5) [exp(0,16 × 0,5) − 1] = 241,92.
- Bedingt auf Pt gilt Var(PT) = Pt² exp[2µ(T − t)] {exp[σ²(T − t)] − 1}, wenn der Preis einer geometrischen Brownschen Bewegung mit Drift µ und Volatilität σ folgt.
- Die Varianz der angenäherten einfachen Rendite im Kou-Modell ist σ² Δt + λ Δt [2η² + κ²(1 − λ Δt)], der Erwartungswert µ Δt + κ λ Δt.
- Die Varianz der doppelten Exponentialverteilung ist 2η², bei E(X) = κ und E(e^X) = e^κ/(1 − η²).
- Die Dichten in der Sprung-Normal-Vergleichsabbildung haben beide die Varianz 2,0572×10^−4; die doppelte Exponentialverteilung und die Normalverteilung der früheren Abbildung haben beide die Varianz 0,0008.
- Im Preisbeispiel mit Pt = 50, µ = 0,15 und σ = 0,40 beträgt die Varianz nach sechs Monaten 241,92.
- Unter dem IGARCH(1,1) ohne Drift von RiskMetrics ist die bedingte Varianz der k-Perioden-Logrendite das k-fache der Ein-Schritt-Varianz σ zum Quadrat von t+1.
- Ist der bedingte Mittelwert nicht null, bleibt in dem einfachen Modell die bedingte Varianz der k-Perioden-Rendite k mal σ zum Quadrat von t+1, während der bedingte Mittelwert kμ wird.
- Die asymptotische Varianz der Ordnungsstatistik zum Anteil p ist p(1 minus p) geteilt durch n mal der quadrierten Dichte am theoretischen Quantil.
- Die asymptotische Varianz des mit der Wurzel aus q skalierten Hill-Schätzers ist ξ zum Quadrat; die des Pickands-Schätzers ist ξ zum Quadrat mal (2 hoch (2ξ plus 1) plus 1) geteilt durch [2 mal (2ξ minus 1) mal ln(2)] zum Quadrat.
- Für ein GARCH(1,1) mit φ = α1 plus β1 < 1 und ohne MA-Teil hat die k-Perioden-Varianz die geschlossene Form über α0 / (1 minus φ) und die Ein-Schritt-Varianzprognose.
- In der gleichzeitigen Kovarianzmatrix Γ0 einer schwach stationären vektoriellen Renditereihe ist das i-te Diagonalelement die Varianz der Komponente rit.
- Die bedingte Varianz des gaußschen GARCH(1,1) für die mittelwertbereinigten IBM-Logrenditen ist σ²t gleich 0,04565 plus 0,0807 mal a² von t minus 1 plus 0,9031 mal σ² von t minus 1.
- Steigt die GARCH-Volatilität, steigt die Variabilität der Logrenditen; Lage- und Formparameter der Extremwertintensität reagieren darauf positiv.
- Das i-te Diagonalelement von Γ0 ist die Varianz von rit. Für ein stationäres VAR(1) ist diese Kovarianz die Summe Φ hoch i mal Σ mal (Φ hoch i)′ über i von 0 bis unendlich.
- Für viele Anwendungen genügt eine grobe Näherung der Varianz des Stichproben-Kreuzkorrelationskoeffizienten ρ-Dach ij(ℓ).
- Die Varianz des 1-Schritt-Prognosefehlers ist die Innovations-Kovarianz Σ. Die Varianz des 2-Schritt-Fehlers ist Σ plus Φ1 Σ Φ1′. Bei Stationarität geht die Varianz des ℓ-Schritt-Fehlers gegen die Varianz von rt.
- Die orthogonalen Innovationen bt lassen sich so normieren, dass die Varianz jeder Komponente bit gleich 1 ist. Vor dieser Normierung ist ihre Kovarianz die Diagonalmatrix G aus der Cholesky-Zerlegung von Σ.
- Die gleichzeitige Varianz-Kovarianz eines VMA(q) ist Σ plus die Summe Θj Σ Θj′ von j gleich 1 bis q. Ab Lag q plus 1 sind die Kreuzkovarianzen 0.
- Für x aus der multivariaten Normalverteilung Nk(μ, Σ) hat die Linearkombination c′x die Varianz c′Σc. Die quadratische Form (x − μ)′ Σ hoch −1 (x − μ) folgt einer Chi-Quadrat-Verteilung mit m Freiheitsgraden, so wie der Text die Freiheitsgrade angibt.
- Die bedingte Varianz von x1 gegeben x2 = b ist der Schur-Block Σ11 − Σ12 Σ22 hoch −1 Σ21.
- Die geschätzte Innovationsvarianz des AR(2) auf den BHP-VALE-Spreadresiduen beträgt 0,0003326. Die Residualskalen der Fehlerkorrektur, 0,0193 und 0,0224, sind die Standardfehler der beiden Innovationen.
- Die Varianz einer Hauptkomponente yi = w′i r ist w′i Σr wi. Die i-te Hauptkomponente maximiert diese Varianz unter Einheitsnorm der Gewichte und unter Unkorreliertheit mit den vorherigen Komponenten. Ihre Varianz ist der Eigenwert λi.
- Der Anteil der i-ten Hauptkomponente an der Gesamtvarianz ist λi geteilt durch die Summe aller Eigenwerte. Bei der Korrelationsmatrix ist der Anteil λi / k. Die Summe der Komponentenvarianzen gleich der Summe der Eigenwerte gleich der Spur.
- Das globale Minimum-Varianz-Portfolio minimiert ω′Σω unter der Nebenbedingung, dass die Gewichte sich zu eins summieren. Die Lösung ist Σ hoch −1 eins, normiert durch die quadratische Form 1′ Σ hoch −1 1.
- Im Einfaktor-BARRA-Fall minimiert das Factor-Mimicking-Portfolio ein Halb ω′ D ω unter ω′β = 1. D ist die Diagonalmatrix der spezifischen Varianzen.
- Im orthogonalen Faktormodell ist die Varianz der i-ten Rendite die Summe der quadrierten Ladungen auf die m gemeinsamen Faktoren plus der spezifischen Varianz. Die Summe der quadrierten Ladungen heißt Kommunalität, die spezifische Varianz heißt Eindeutigkeit.
- Die ersten i Hauptkomponenten geben die Gesamtvarianz nur näherungsweise wieder, außer wenn alle nachfolgenden Eigenwerte null sind.
- Die Summe der quadrierten Elemente der Fehler-Matrix aus geschätzter Kovarianz minus Ladungsanteil minus spezifischen Varianzen ist höchstens die Summe der Quadrate der vernachlässigten Eigenwerte.
- Eine orthogonale Faktorrotation lässt Kommunalitäten und spezifische Varianzen unverändert.
- Connor und Korajczyk (1993) wählen die Faktorzahl danach, ob die Querschnittsvarianz des spezifischen Fehlers beim Schritt von m auf m plus 1 signifikant sinkt. Bai und Ng bilden das Mittel der Residuenvarianzen über die Assets und bestrafen es in Cp1 und Cp2 mit einem Term, der in m wächst.
- Im Dreifaktorenmodell von zehn monatlichen Überschussrenditen, Januar 1990 bis Dezember 2003, betragen die Eindeutigkeiten unter anderem 0,885 für Procter and Gamble, 0,690 für Dell, 0,638 für IBM und 0,000 für Caterpillar. Die Varianzanteile der drei Faktoren sind 0,264, 0,183 und 0,133, zusammen 0,579.
- Bei den fünf US-Anleihenindizes sind die spezifischen Varianzen sehr klein. Die Kommunalitäten der Hauptkomponentenmethode liegen zwischen 0,931 und 0,982, und die ersten zwei Faktoren erklären 95,7 Prozent der Variabilität.
- Der erste Eigenwert der Kovarianz der Innovationen von IBM und dem S&P 500 erklärt 82,2 Prozent der verallgemeinerten Varianz. Die beiden Eigenwerte sind 63,373 und 13,489.
- Die univariate GARCH-Varianz des gemeinsamen Faktors ist σ²t gleich 3,834 plus 0,110 mal dem quadrierten Schock plus 0,825 mal der vorherigen Varianz. Alle Parameterschätzungen sind auf dem 1-Prozent-Niveau hochsignifikant.
- Die Ein-Schritt-Prognosen der bedingten Varianzen von IBM und S&P 500 am Ursprung 888 liegen in den drei Modellen nah beieinander: 71,09 und 17,79 im konstanten Modell, 75,15 und 24,70 im logistischen Modell, 73,45 und 17,87 im Cholesky-Modell. Die prognostizierte Kovarianz fällt im Cholesky-Modell auf 7,34, gegenüber 21,83 und 23,48.
- Im DCC der Aktien IBM und Dell ist die Varianzdynamik nahezu integriert. Die Summe der GARCH-Koeffizienten ist 0,9975, und die Konstanten unterscheiden sich nicht signifikant von null.
- Im dreidimensionalen Modell ist die Residuenvarianz von Intel g33,t gleich 1,188 plus 0,053 mal dem quadrierten transformierten Schock plus 0,687 mal g33,t−1 minus 0,019 mal g22,t−1. Die Indexvarianz hängt nicht von den vergangenen Aktienvarianzen ab, die Aktienvarianzen dagegen von der vergangenen Marktvarianz.
- Im lokalen Trendmodell hat die erste Differenz wt gleich (1 minus B) yt die Varianz 2σ²e plus σ²η.
- Die Varianz des Ein-Schritt-Prognosefehlers ist Vt gleich Σt|t minus 1 plus σ²e. Sie fällt mit der unbedingten Varianz zusammen, weil vt von Ft minus 1 unabhängig ist.
- Die gefilterte Zustandsvarianz ist Σt|t gleich Σt|t minus 1 mal (1 minus Kt). Die prognostizierte Zustandsvarianz ist Σt plus 1 gegeben t gleich Σt|t plus σ²η.
- In der einfachen multivariaten Student-t mit v Freiheitsgraden, Mittel null und Einheitsmatrix ist die Varianz jeder Komponente v geteilt durch (v minus 2).
- Die erste Hauptkomponente erklärt 82,2 Prozent der verallgemeinerten Varianz der Innovationen von IBM und S&P 500 und etwa 82,5 Prozent der verallgemeinerten Varianz der Renditen selbst.
- Bei diffuser Initialisierung, Σ1|0 gegen unendlich, ist Σ2|1 gleich σ²e plus σ²η, und die geglättete Varianz am ersten Zeitpunkt geht gegen σ²e minus σ⁴e mal M1.
- Die geglättete Zustandsvarianz folgt rückwärts aus Mt minus 1 gleich 1/Vt plus Lt zum Quadrat mal Mt und Σt|T gleich Σt|t minus 1 minus (Σt|t minus 1) zum Quadrat mal Mt minus 1, mit MT gleich 0.
- Fehlen Beobachtungen, ist die Varianz des Zustands gegeben Fℓ gleich Σℓ plus 1|ℓ plus (t minus ℓ minus 1) mal σ²η.
- Für Alcoa sind die geschätzten Varianzen der Zustandsinnovation 0,0054035 und des Messfehlers 0,2306524.
- Die Log-Likelihood hängt von den Prognosefehlervarianzen Vt ab: sie enthält die Summe von ln(Vt) plus v²t geteilt durch Vt.
- Im stationären AR(1) mit Koeffizient 0,6 und Innovationsvarianz 0,16 ist die Zustandsstartvarianz 0,4 zum Quadrat geteilt durch (1 minus 0,6 zum Quadrat) gleich 0,25.
- Im zeitkonstanten Filter konvergiert die Prognosevarianz des Zustands gegen die Steady-State-Lösung Σ-Stern der Gleichung Σ-Stern gleich T Σ-Stern T′ minus T Σ-Stern Z V hoch minus 1 Z Σ-Stern T′ plus R Q R′, mit V gleich Z Σ-Stern Z′ plus H.
- Die Varianz der geglätteten Messstörung liegt um Ht mal (Vt hoch minus 1 plus Kt′ Mt Kt) mal Ht unter Ht. Die Varianz der geglätteten Zustandsinnovation liegt um Qt Rt′ Mt Rt Qt unter Qt.
- Im GetSsfStsm-Beispiel mit irregular gleich 0,4 und level gleich 0,2 stehen in der Innovationsvarianzmatrix die Werte 0,04 und 0,16.
- Die Varianz des j-Schritt-Prognosefehlers ist Zt plus j mal Σt plus j gegeben t mal Zt plus j′ plus Ht plus j.
- Für die Gammaverteilung gilt Var(η) = α/β², für die Betaverteilung Var(θ) = αβ / [(α + β)² (α + β + 1)].
- Die Varianzschätzung aus der Gibbs-Stichprobe ist σ̂²i = 1/(n − m − 1) mal Summe (θi,j − θ̂i)².
- In Result 12.1 ist die Varianz der Daten bekannt und die Posteriorvarianz von µ gleich σ²* = σ² σ²o / (σ² + n σ²o).
- Die Kovarianz des Prognosefehlers Var[et(j)] = Zt+j Σt+j|t Z′t+j + Ht+j enthält die Zustands- und die Beobachtungsunsicherheit.
- Die Stichprobenkovarianz von x̄ im multivariaten Normalmodell ist Σ/n.
- Die Varianz der invertierten Chi-Quadrat-Verteilung ist 2 / [(v − 2)² (v − 4)] für v > 4, der Erwartungswert 1/(v − 2) für v > 2.
- Die Posterior von σ² bei bekannten β und φ ist (vλ + Summe a²t)/σ² ∼ χ² mit v + (n − 1) Freiheitsgraden.
- Im Volatilitätsmodell hat εt die Varianz 1 und vt die Varianz σ²v; bedingt auf ht ist at normal mit Varianz ht.
- Die bedingte Varianz von ln ht gegeben den Nachbarn ist σ²v / (1 + α1²).
- Die Varianz des Kleinste-Quadrate-Schätzers eines fehlenden AR(p)-Werts ist σ² / Summe φj².
- Die Volatilität der umparametrisierten Form ist σ0 exp(zt/2) und damit stets positiv; σ²0 = exp{E[ln(ht)]} und zt = ln(ht) − ln(σ²0).
- gii,t = Var(bit | Ft−1) sind die bedingten Varianzen der Cholesky-Innovationen.
- Var(η*t) = σ²η(1 − ρ²), und ω = σ²η(1 − ρ²) ist der entsprechende Varianzfaktor der Umparametrisierung.
- Die Varianz der Ein-Schritt-Prognosefehler im angenäherten Filter ist Vt = Σt|t−1 + Ht.
- Die Parameter αij erfüllen Regularitätsbedingungen, sodass die unbedingte Varianz von at existiert.
- Der Text nennt die unbedingte Varianz der GE-Monatsrendite im angegebenen GARCH-Modell endlich und gleich 0,546/(1 − 1,765 + 0,775) ≈ 49,64.
- Die unbedingte Varianz des GARCH(1,1) für die monatlichen S&P-500-Logrenditen beträgt 3,349/(1 − 0,086 − 0,735) = 18,78; die Volatilitätsprognosen steigen mit dem Horizont auf diesen Wert zu.
- Im Leverage-Modell ist η*t unabhängig von εt und hat die Varianz σ²η(1 − ρ²).
- Die Anfangsvolatilität h1 wird auf die Stichprobenvarianz von rt gesetzt.
- Die Volatilität in Abbildung 12.6 ist die bedingte Varianz der prozentualen Logrenditen.
- Im Prognosemodell der stochastischen Volatilität gilt Var(vt) = σ²v,j für die Innovation der logarithmierten Varianz, und die Renditestörung εt hat Varianz 1.

## Funktionsweise

- Hierarchical Risk Parity definiert die Varianz einer zusammenhängenden Teilmenge als Varianz einer Inverse-Varianz-Allokation.
- Von oben nach unten werden die Gewichte umgekehrt proportional zu den aggregierten Varianzen der benachbarten Teilmengen geteilt.
- Der Splitfaktor ist eins minus der Bruch aus der Varianz der ersten Hälfte und der Summe beider Teilvarianzen und liegt zwischen 0 und 1.
- Für zwei Anlagen ist das Minimum-Varianz-Gewicht der ersten Anlage eins minus der Bruch aus ihrer Varianz und der Summe beider Varianzen, und Stufe 3 von Hierarchical Risk Parity teilt genauso.
- Ist die Kovarianzmatrix diagonal, ist das Gewicht einer Anlage ihr inverser Varianzterm geteilt durch die Summe aller inversen Varianzen.
- Bei zwei Anlagen ist das Gewicht der ersten Anlage eins minus der Bruch aus ihrer Varianz und der Summe beider Varianzen.
- Stufe 3 von Hierarchical Risk Parity setzt den Anteil der ersten Hälfte auf eins minus den Bruch aus ihrer Varianz und der Summe beider Varianzen.
- Die Cluster-Varianz im Code ist die quadratische Form der Kovarianzscheibe mit Inverse-Varianz-Gewichten.
- Der Variance-Ratio-Test prüft, ob das Verhältnis der Varianz über die Spanne τ zur τ-fachen Ein-Schritt-Varianz gleich 1 ist (Lo, 2001).
- Die Proportionalität zur Zeitspanne wird für großes τ zur Gleichheit und kann für kleines τ von der Geraden abweichen.
- Der Kalman-Filter minimiert den mittleren quadratischen Fehler der geschätzten Variablen und ist unter gaußschem Rauschen der beste Schätzer.
- Q(t) ist die Varianz des Prognosefehlers e(t) und wird als x transponiert mal R mal x plus Ve prognostiziert.
- R ist die Kovarianz des Fehlers der verborgenen Variable; die Varianz des Prognosefehlers ist davon zu unterscheiden.
- Im Market-Making-Modell ist die Prognosevarianz die Varianz des Mittelpreisschätzers plus Ve, und das Zustandsvarianz-Update multipliziert die alte Varianz mit 1 minus dem Kalman-Gain.
- In der Kelly-Formel ist s hoch 2 die Varianz der Excess Returns, und der optimale Hebel ist der mittlere Excess Return geteilt durch diese Varianz.
- Das Pearson-System nimmt neben dem Mittelwert die Standardabweichung sowie Schiefe und Kurtosis als Input der Monte-Carlo-Verteilung.
- Die Varianz des Prognosefehlers im Market-Making-Kalman-Filter ist Q(t) = Var(m(t)) + Ve.
- Der Kalman-Gain ist K(t) = R(t|t − 1) geteilt durch (R(t|t − 1) + Ve), und die aktualisierte Zustandsvarianz ist R(t|t) = (1 − K(t)) mal R(t|t − 1).
- Die Messfehlervarianz Ve wird klein, wenn die Handelsgröße gegenüber einer Benchmark groß ist. Bei T gleich Tmax ist Ve null und der neue Mittelwert gleich dem beobachteten Preis.
- Die Stichprobenvarianz ist 1/(T − 1) mal der Summe der quadrierten Abweichungen vom Stichprobenmittel.
- Sind die Logrenditen iid normal mit Mittel µ und Varianz σ², ist die Varianz der zugehörigen einfachen Rendite exp(2µ + σ²) mal [exp(σ²) − 1].
- Sind m1 und m2 Mittelwert und Varianz der einfachen Rendite, ist die Varianz der zugehörigen Logrendite ln[1 + m2/(1 + m1)²].
- Ist die bedingte Verteilung der Logrendite normal mit Mittel µt und Varianz σ²t, geht σ²t in die Log-Likelihood als ln(σ²t) und als Nenner von (rt − µt)² ein.
- In der Cholesky-Zerlegung ist der erste Diagonaleintrag von Gt die bedingte Varianz von a1t. Der zweite ist die Residuenvarianz der Regression von a2t auf a1t.
- Daraus folgt σ11,t gleich g11,t und σ22,t gleich g22,t plus q21,t zum Quadrat mal g11,t. Allgemein ist die bedingte Varianz der i-ten Komponente die Summe der Produkte aus quadriertem Regressionskoeffizienten qiv,t und Varianz gvv,t für v von 1 bis i.
- Die Varianzprognosen des Constant-Correlation-GARCH betreffen die marginalen bedingten Varianzen der einzelnen Schocks. Die Ein-Schritt-Prognose ist alpha0 plus alpha1 mal den aktuellen quadrierten Schocks plus beta1 mal dem aktuellen Varianzvektor.
- Im stationären Fall sind die unbedingten Varianzen (I minus alpha1 minus beta1) hoch minus 1 mal phi0, vorausgesetzt alle Eigenwerte von alpha1 plus beta1 sind positiv und kleiner als 1.

## Voraussetzungen

- Die Quadratwurzel-Senkung der Varianz des Mittelwerts setzt unabhängige Beobachtungen voraus.
- Der Zentrale Grenzwertsatz verlangt, dass die Varianz der Elternpopulation endlich ist, neben einem endlichen Mittelwert und unabhängigen Beobachtungen aus derselben Population.
- Der Grundsatz, dass größere Stichproben besser sind, gilt für stationäre Prozesse. Bei höchstwahrscheinlich nichtstationären Finanzzeitreihen können größere Stichproben nicht besser sein.

## Anwendung im Trading

- Bei Finanzbeobachtungen, die nicht unabhängig sind, nennt der Text den sequenziellen Bootstrap als Mittel, die Korrelation und damit die Varianz der gebaggten Prognose zu senken.
- Werden Labels aus der Rendite über 100 Bars gebildet, soll je Schätzer nur 1 Prozent der Beobachtungen gezogen werden, damit die Ziehungen nicht redundant werden und die Varianz nicht stehen bleibt.
- Die Varianzreduktion außer Stichprobe ist für Risk-Parity-Investoren wegen ihres hohen Hebels entscheidend.

## Regeln und Kriterien


## Risiken und Grenzen

- Liegt die mittlere Korrelation der Ensemble-Prognosen nahe 1, verändert Bagging die Varianz praktisch nicht, auch wenn sehr viele Schätzer verwendet werden.
- Bei Labels mit geringer Eindeutigkeit bleibt die Varianzreduktion aus, solange mit Zurücklegen nahezu dieselben Informationen gezogen werden.
- Eine unterschätzte Varianz führt zu einem überschätzten optimalen Hebel und kann zum Ruin führen.
- Schätzfehler der Varianz sind unvermeidlich, und die künftige Varianz muss nicht der historischen entsprechen.
- Kelly über mehrere Strategien ist nur optimal, wenn auch die Volatilitäten unverändert bleiben.
- Die Parameter einer Normalmischung, etwa der Bernoulli-Anteil α, sind schwer zu schätzen. Die statistische Modellierung mit nichtnormalen stabilen Verteilungen ist schwierig.

## Beispiele

- Abbildung 6.1 zeigt die Standardabweichung der gebaggten Prognose für N zwischen 5 und 30, mittlere Korrelation zwischen 0 und 1 und mittlere Einzelstandardabweichung 1.
- Die simulierten Gauß-Renditen haben Mittelwert 0 und eine willkürlich gesetzte Standardabweichung von 10 Prozent.
- Für die Logpreise von USD.CAD ist h gleich 0 und pValue gleich 0,367281, das Varianzverhältnis ist also mit dem Random Walk vereinbar.
- Im EWA-EWC-Beispiel wird Ve gleich 0,001 gesetzt, und bei δ gleich 0,0001 ändert sich Q nur langsam.
- Gehandelt wird, wenn der Prognosefehler betragsmäßig größer ist als die Wurzel dieser Prognosevarianz.
- Strategie 1 im Kapitalbeispiel hat 26 Prozent annualisierte Volatilität bei 30 Prozent mittlerem Excess Return, Strategie 2 hat 35 Prozent Volatilität bei 60 Prozent.
- Wägen alle Personen 150 Pfund, hat jede Stichprobe den Durchschnitt 150 Pfund, und die Stichprobenverteilung des Mittelwerts hat keine Streuung.
- Für die prozentualen täglichen einfachen IBM-Renditen, n = 9845, beträgt die Stichprobenvarianz 2,864705.
- Abbildung 1.1 verwendet als varianzreiche Komponente N(0, 16) neben N(0, 1), mit Bernoulli-Wahrscheinlichkeit 0,05 für die Komponente mit Varianz 16.
- Für das AR(3) der BSP-Wachstumsrate schätzt R die Residualvarianz auf 9,427 mal 10 hoch minus 5.
- Ist {rt} unabhängig und identisch verteilt mit endlichem zweiten Moment, ist die asymptotische Varianz jeder festen Stichprobenautokorrelation gleich 1/T.
- Für die IBM-Reihe ist σ zum Quadrat von 9190 = 0,0003472 und die Ein-Schritt-Prognose 0,000336; die 95- und 99-Prozent-Quantile der nächsten Rendite sind 0,03025 und 0,04265.
- Im gaußschen AR(2)–GARCH(1,1) für die negativen IBM-Renditen ist die Varianzprognose für den nächsten Tag 0,0003211, im Student-t-Modell mit 5 Freiheitsgraden 0,0003386.
- Im IBM-Beispiel beträgt die bedingte Varianz der 15-Tages-Logrendite ab Prognoseursprung 9190 gleich 0,0047948.
- Die Innovations-Kovarianz des VAR(5) für die prozentualen Monatsrenditen hat die Varianzen 48 für die IBM-Innovation und 30 für die S&P-Innovation, bei einer Kovarianz von 24.
- In der SCA-Ordnungsbestimmung starten die Residualvarianzen des bivariaten Modells bei Lag 1 mit 0,492 mal 10 hoch 2 und 0,306 mal 10 hoch 2 und liegen bei Lag 5 bei 0,480 mal 10 hoch 2 und 0,299 mal 10 hoch 2.
- Die Residualvarianzen der bedingten Likelihood des vereinfachten VAR(5) sind 48,328570 für die IBM-Gleichung und 30,027406 für die S&P-Gleichung, bei einer Kovarianz von 24,361464.
- Im VAR(1) betragen die Residualskalen 7,0078 und 5,5247. Das sind zugleich die Standardfehler der 1-Schritt-Prognose; die Varianz des Prognosefehlers steigt bis zum 3. Schritt nur noch wenig, auf Standardfehler 7,0436 und 5,5454.
- Die Schock-Kovarianz des Zins-VARMA, mal 10 hoch 3, hat die Diagonaleinträge 3,58 und 2,19 und die Kovarianz 2,50.
- Auf der Kovarianzmatrix der fünf Monats-Logrenditen erklären die Eigenwerte 284,17, 112,93, 57,43, 46,81 und 29,87 die Anteile 0,535, 0,213, 0,108, 0,088 und 0,056 der Gesamtvarianz. Die ersten beiden kumulieren auf 0,748.
- Auf der Korrelationsmatrix erklären die ersten beiden Eigenwerte 2,607 und 1,072 zusammen den kumulierten Anteil 0,736; der Text spricht von etwa 74 Prozent. Die übrigen Eigenwerte sind 0,569, 0,451 und 0,301.
- Das globale Minimum-Varianz-Portfolio aus der Marktmodell-Kovarianz und das aus der Stichprobenkovarianz legen beide höheres Gewicht auf Kimberly-Clark, New York Times und Procter & Gamble. Das Gewicht von Chicago Tribune beträgt im Modell 0,1400 und in den Daten 0,0168.
- Die univariaten Varianzgleichungen für die prozentualen Tageslogrenditen lauten für Hongkong 0,038 plus 0,143 mal dem quadrierten Schock plus 0,855 mal der vorherigen Varianz und für Japan 0,044 plus 0,127 mal dem quadrierten Schock plus 0,861 mal der vorherigen Varianz.
- Im GM-Marktmodell beträgt die Residualstandardabweichung σ̂e = 8,13, im zeitvariablen Modell die Beobachtungs-Standardabweichung 8,125213.
- Die Störungskovarianz mOmega des angepassten Johnson-&-Johnson-Modells hat die Diagonaleinträge 0,005284788, 0,000859481, 0, 0 und 4,180047 × 10 hoch −12.
- Der klassische Residualstandardfehler der Zinsregression ist σ̂a = 0,068; das Posteriormittel von σ² ist 0,00479 bei Standardfehler 0,00013, und das Posteriormittel von σ liegt bei etwa 0,069.
- Das AR(3) hat σ̂² = 0,0128, die Gibbs-Schätzung σ̂² = 0,0118 bei posteriorer Standardabweichung 0,0008.
- Die Prior der Ausreißergröße ist βt ∼ N(0, ξ²) mit ξ² = 0,1, etwa 9 σ̂².
- Das GARCH(1,1) setzt ht = 0,878 + 0,125 a²t−1 + 0,837 ht−1.
- Das Posteriormittel von σ²v im univariaten SV-Modell ist 0,086 bei Standardfehler 0,007.
- Im bivariaten SV-Modell sind die Posteriormittel σ²1v = 0,07, σ²2v = 0,07 und σ²u = 0,07, jeweils mit Standardfehler 0,01.
- Das bivariate GARCH schätzt α10 = 3,98, α20 = 10,67, α12 = 0,12 und α22 = 0,12 als Koeffizienten der bedingten Varianzgleichungen.
- Für IBM liegen die bedingten Varianzen von GARCH, BEKK und SV ähnlich, GARCH aber mit höheren Spitzen und einem zusätzlichen Gipfel 1993; für den S&P 500 fehlt dieser Gipfel um 1993 in BEKK, SV und der univariaten Analyse.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 115–134 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-007-p115-p134|S. 115–134]]
- Advances in Financial Machine Learning.pdf, S. 248–267 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-014-p248-p267|S. 248–267]]
- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 172–191 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-010-p172-p191|S. 172–191]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 191–210 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-011-p191-p210|S. 191–210]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 229–248 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-013-p229-p248|S. 229–248]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 267–286 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-015-p267-p286|S. 267–286]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 286–305 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-016-p286-p305|S. 286–305]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 305–324 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-017-p305-p324|S. 305–324]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 476–495 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-026-p476-p495|S. 476–495]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 1–13 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-001-p001-p013|S. 1–13]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 52–71 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-004-p052-p071|S. 52–71]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 95–98 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-007-p095-p098|S. 95–98]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 144–163 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-011-p144-p163|S. 144–163]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 180–199 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-014-p180-p199|S. 180–199]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 20–39 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-002-p020-p039|S. 20–39]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 39–58 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-003-p039-p058|S. 39–58]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 58–77 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-004-p058-p077|S. 58–77]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 77–96 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-005-p077-p096|S. 77–96]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 96–115 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-006-p096-p115|S. 96–115]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 115–134 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-007-p115-p134|S. 115–134]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 134–153 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-008-p134-p153|S. 134–153]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 153–172 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-009-p153-p172|S. 153–172]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 191–210 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-011-p191-p210|S. 191–210]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 210–229 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-012-p210-p229|S. 210–229]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 229–248 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-013-p229-p248|S. 229–248]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 248–267 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-014-p248-p267|S. 248–267]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 267–286 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-015-p267-p286|S. 267–286]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 286–305 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-016-p286-p305|S. 286–305]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 305–324 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-017-p305-p324|S. 305–324]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 324–343 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-018-p324-p343|S. 324–343]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 343–362 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-019-p343-p362|S. 343–362]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 362–381 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-020-p362-p381|S. 362–381]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 381–400 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-021-p381-p400|S. 381–400]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 400–419 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-022-p400-p419|S. 400–419]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 419–438 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-023-p419-p438|S. 419–438]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 438–457 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-024-p438-p457|S. 438–457]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 457–476 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-025-p457-p476|S. 457–476]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 476–495 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-026-p476-p495|S. 476–495]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 495–514 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-027-p495-p514|S. 495–514]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 514–533 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-028-p514-p533|S. 514–533]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 533–552 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-029-p533-p552|S. 533–552]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 552–571 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-030-p552-p571|S. 552–571]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 571–590 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-031-p571-p590|S. 571–590]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 590–609 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-032-p590-p609|S. 590–609]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 609–628 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-033-p609-p628|S. 609–628]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 628–647 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-034-p628-p647|S. 628–647]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 647–666 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-035-p647-p666|S. 647–666]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 666–685 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-036-p666-p685|S. 666–685]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 685–704 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-037-p685-p704|S. 685–704]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 438–457 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-024-p438-p457|S. 438–457]]

## Verwandte Themen
