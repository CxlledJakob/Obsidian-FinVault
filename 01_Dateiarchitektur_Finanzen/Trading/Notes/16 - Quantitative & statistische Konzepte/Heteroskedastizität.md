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

# Heteroskedastizität


## Kurzdefinition

- Strukturelle Heteroskedastizität liegt vor, wenn die Renditevarianz nicht vom Preisniveau abhängt, ein ADF auf Rohpreisen aber eine davon unabhängige, endliche Preisvarianz unterstellt.
- Heteroskedastizität von Intraday-Zeitbars entsteht aus der ungleichmäßigen Natur von Tickdaten.
- Der Volatilitätsprozess betrifft die zeitliche Entwicklung der bedingten Varianz der Rendite.

## Kernaussagen

- Wird die Null des ADF auf Rohpreisen verworfen, gelten die Preise als stationär mit endlicher Varianz.
- Damit die Preisvarianz konstant bleibt, muss die Renditevolatilität bei steigenden Preisen fallen und bei fallenden Preisen steigen.
- Ein ADF auf Rohpreisen nimmt damit an, dass die Renditevarianz nicht invariant zum Preisniveau ist.
- Ist die Renditevarianz tatsächlich invariant zum Preisniveau, ist das Modell auf Rohpreisen strukturell heteroskedastisch.
- Bei Logpreisen bedingen die Preisniveaus den Mittelwert der Renditen, nicht ihre Volatilität.
- Wenn der Renditebetrag viele Ausgänge annehmen kann, verwirft Binärcodierung Information, besonders bei Intraday-Zeitbars.
- Ein teilweiser Ausgleich ist die Abtastung nach einem subordinierten stochastischen Prozess.
- Trade Bars und Volume Bars enthalten eine feste Zahl von Trades oder Trades für ein festes Volumen.
- In dieser marktgesteuerten, nicht chronologischen Uhr wird in aktiven Phasen häufiger und in ruhigen Phasen seltener gesampelt.
- Diese Abtastung regularisiert die Verteilung des Renditebetrags und senkt den Bedarf an einem großen Alphabet.
- Die Zeitplots der monatlichen IBM-Renditen und des wertgewichteten Index von Januar 1926 bis Dezember 2008 zeigen, dass die Schwankungen der Renditen über die Zeit variieren und in Clustern auftreten.
- Ist die bedingte Verteilung der Logrendite normal mit Mittel µt und Varianz σ²t, dann hängen diese bedingten Momente von t ab; die Parameter in µt und σ²t bilden den Parametervektor θ der Likelihood.
- GARCH bezeichnet das generalized autoregressive conditional heteroscedastic model und wird als nichtstandardisiertes ARMA-Modell für die quadrierten Schocks a zum Quadrat zur Zeit t aufgefasst.
- Haben die Regressionsfehler serielle Korrelation oder bedingte Heteroskedastizität, ist der übliche Schätzer der Kovarianzmatrix der Kleinste-Quadrate-Koeffizienten inkonsistent und bläht die t-Quotienten oft auf.
- Der heteroskedastizitätskonsistente Schätzer von Eicker (1967) und White (1980) und der heteroskedastizitäts- und autokorrelationskonsistente Schätzer von Newey und West (1987) liefern dann eine konsistente Kovarianzmatrix, sofern die Kleinste-Quadrate-Koeffizienten selbst konsistent bleiben.
- Bei den ersten Differenzen der wöchentlichen US-Treasury-Renditen fällt der t-Quotient des Koeffizienten der Einjahresänderung von 107,91, wenn serielle Korrelation und Heteroskedastizität ignoriert werden, auf 48,44 mit dem White-Schätzer und auf 39,92 mit dem Newey-West-Schätzer.
- Newey und West wählen die Trunkierungslänge als ganzzahligen Teil von 4 mal (T durch 100) hoch 2/9; die Bartlett-Gewichte sind 1 minus j durch (ell plus 1).
- Bedingt heteroskedastische Modelle beschreiben die Volatilität einer Anlagerendite; Volatilität meint hier die bedingte Standardabweichung dieser Rendite.
- Die bedingte Varianz ist sigma t quadrat gleich Var von at gegeben Ft minus 1; die Art, wie sie sich über die Zeit entwickelt, unterscheidet die Volatilitätsmodelle.
- Zwei Klassen werden unterschieden: eine exakte Funktion für die bedingte Varianz, dazu gehört GARCH, und eine stochastische Gleichung, dazu gehört die stochastische Volatilität.
- Der Aufbau hat vier Schritte: eine Mittelgleichung festlegen und lineare Abhängigkeit entfernen, die Residuen auf ARCH-Effekte testen, bei Signifikanz ein Volatilitätsmodell gemeinsam schätzen, dann prüfen und nachbessern.
- Bei den meisten Renditereihen ist die Mittelgleichung nur die Subtraktion des Mittelwerts, wenn er signifikant von null abweicht; manchmal braucht es ein einfaches AR oder eine Dummy für Wochenende oder Januar.
- Zwei Tests auf ARCH-Effekte stehen bereit: die Ljung-Box-Statistik Q(m) auf die quadrierten Residuen nach McLeod und Li (1983), mit der Null, dass die ersten m Autokorrelationen der Quadrate null sind, und der Lagrange-Multiplikator-Test von Engle (1982).
- Engles Test ist die übliche F-Statistik für alpha 1 bis alpha m gleich null in der Regression der quadrierten Residuen auf eine Konstante und m eigene Lags.
- Diese F-Statistik ist (SSR0 minus SSR1) durch m, geteilt durch SSR1 durch (T minus 2m minus 1), und unter der Null asymptotisch chi-quadrat mit m Freiheitsgraden; abgelehnt wird, wenn sie das Quantil überschreitet oder der p-Wert unter dem Fehler 1. Art liegt.
- Bei den monatlichen Intel-Logrenditen 1973 bis 2008 ist Q(12) der Renditen 18,26 mit p-Wert 0,11, der LM-Test etwa 53,62 mit p-Wert nahe null und die Ljung-Box-Statistik der Quadrate 89,85 mit p-Wert nahe null; in R ist die Quadrat-Statistik 89,8509 mit p-Wert 5,274e-14.
- Ein ARCH(m) setzt at gleich sigma t mal epsilon t und sigma t quadrat gleich alpha 0 plus der Summe alpha i mal a, t minus i, quadrat, mit epsilon t unabhängig und identisch verteilt, Mittelwert null und Varianz 1, alpha 0 größer 0 und alpha i mindestens 0.
- Epsilon t wird in der Praxis oft als standardnormal, als standardisierte Student-t oder als verallgemeinerte Fehlerverteilung angenommen.
- Beim ARCH(1) ist die unbedingte Varianz alpha 0 durch (1 minus alpha 1), was 0 kleiner oder gleich alpha 1 kleiner als 1 verlangt; unter Normalität existiert das vierte Moment nur für alpha 1 quadrat kleiner als 1/3.
- Schwächen des ARCH sind: positive und negative Schocks wirken gleich, weil nur Quadrate eingehen; die Restriktionen begrenzen bei gaußschen Innovationen die erfassbare Excess-Kurtosis; das Modell erklärt die Ursache der Schwankung nicht; es überzeichnet die Volatilität, weil es auf große isolierte Schocks langsam reagiert.
- Die Ordnung wird aus der partiellen Autokorrelation der Quadrate gelesen, weil die Quadrate eine AR-Form plus einen unkorrelierten, aber nicht identisch verteilten Fehler eta t gleich a t quadrat minus sigma t quadrat haben; die Kleinste-Quadrate-Schätzung ist konsistent, aber nicht effizient, und bei kleiner Stichprobe wenig trennscharf.
- Für Intel genügt nach einem nicht signifikanten ARCH(3) auf dem 5-Prozent-Niveau das gaußsche ARCH(1) rt gleich 0,0126 plus at und sigma t quadrat gleich 0,0111 plus 0,3560 mal a, t minus 1, quadrat, mit Standardfehlern 0,0053, 0,0010 und 0,0761.
- Die Ljung-Box-Statistik der standardisierten Residuen dieses ARCH(1) ist Q(10) gleich 12,64 mit p-Wert 0,24, die der Quadrate Q(10) gleich 14,75 mit p-Wert 0,14; auf dem 5-Prozent-Niveau gilt das Modell damit als angemessen. Die Zusammenfassung weist für zwölf Lags der Quadrate zugleich 32,11 mit p-Wert 0,001329 aus.
- Unter Student-t lautet das ARCH(1) rt gleich 0,0169 plus at und sigma t quadrat gleich 0,0120 plus 0,2845 mal a, t minus 1, quadrat, Freiheitsgrade 6,01 mit Standardfehler 1,50; die Mittelgleichung ist mit Q(12) gleich 14,88 und p-Wert 0,25 angemessen, die Volatilitätsgleichung mit Q(12) gleich 35,42 und p-Wert 0,0004 auf dem 1-Prozent-Niveau nicht, wegen einer Lag-12-Autokorrelation der Quadrate von 0,188.
- Eine dicke Randverteilung senkt den ARCH-Koeffizienten; der Unterschied der beiden Intel-Modelle bleibt in diesem Beispiel klein, passender wäre ein GARCH(1,1).
- Die Positivität der bedingten Varianz lässt sich statt über alpha i mindestens 0 auch als alpha 0 plus einer quadratischen Form mit nichtnegativ definiter Matrix schreiben; Engles Modell verlangt, dass diese Matrix diagonal ist.
- Zur Modellprüfung sollen die standardisierten Residuen at durch sigma t unabhängig und identisch verteilt sein: die Ljung-Box-Statistik der Residuen prüft die Mittelgleichung, die der Quadrate die Volatilitätsgleichung, Schiefe, Kurtosis und QQ-Plot die Verteilungsannahme.
- Das ARCH-Modell braucht oft viele Parameter; für die monatlichen S&P-500-Überschussrenditen wäre ein ARCH(9) nötig, Bollerslevs GARCH ist die sparsamere Erweiterung.
- Im GARCH bleibt die unbedingte Varianz endlich, solange die Summe aus ARCH- und GARCH-Koeffizienten kleiner als 1 ist, während die bedingte Varianz sich mit den vergangenen Quadraten und Varianzen bewegt.
- Beim geschätzten IGARCH(1,1) der S&P-500-Überschussrenditen ist die unbedingte Varianz von at und damit von rt nicht definiert.
- EGARCH modelliert den Logarithmus der bedingten Varianz und lockert damit die Positivitätsbedingung an die Koeffizienten; die Funktion g der Innovationen lässt positive und negative Schocks ungleich wirken.
- Für den S&P 500 von 1926 bis 1991 zeigt die partielle Autokorrelation der quadrierten Überschussrenditen starke lineare Abhängigkeit, und das GARCH(1,1) entfernt sie: Q(12) und Q(24) der quadrierten standardisierten Residuen haben die p-Werte 0,36 und 0,33.
- Bei den Intel-Logrenditen lehnt ein gaußsches ARCH(1) in fGarch die Quadrate auf längeren Lags ab, Q(15) gleich 36,08022 mit p-Wert 0,001721 und LM-Statistik 26,57744 mit p-Wert 0,008885, während das GARCH(1,1) mit alpha 1 gleich 0,08742 und beta 1 gleich 0,85118 keine verbliebene bedingte Heteroskedastizität mehr zeigt.
- Für die zehnminütigen Mark-Dollar-Änderungen lautet ein ARCH(3) rt gleich 0,0018 plus sigma t mal epsilon t und sigma t quadrat gleich 0,22 mal 10 hoch minus 2 plus 0,322, 0,074 und 0,093 mal den Quadraten der Lags 1 bis 3; die Standardfehler der Varianzparameter sind 0,47 mal 10 hoch minus 6, 0,017, 0,016 und 0,014, alle auf dem 5-Prozent-Niveau signifikant, und die standardisierten Residuen weisen das Modell als angemessen aus.
- Das CHARMA-Modell erzeugt bedingte Heteroskedastizität durch zufällige Koeffizienten. Es ist nicht dasselbe wie ARCH, hat aber ähnliche bedingte Eigenschaften zweiter Ordnung (Tsay, 1987).
- Die bedingte Varianz eines CHARMA ist σ²_t = σ²_η + a′_{t−1} Cov(δ_t) a_{t−1}. Für m = 1 wird daraus ein ARCH(1), σ²_t = σ²_η + ω_{11} a²_{t−1}. Für m = 2 tritt zusätzlich der Kreuzterm 2ω_{12} a_{t−1}a_{t−2} auf.
- Ist die Kovarianzmatrix Ω der zufälligen Koeffizienten diagonal, ist die bedingte Varianz eines CHARMA(m) äquivalent zu der eines ARCH(m). Weil Ω nichtnegativ definit und σ²_η positiv ist, gilt automatisch σ²_t ≥ σ²_η > 0.
- Die Kreuzprodukte verzögerter Innovationen im CHARMA stehen für Wechselwirkungen früherer Renditen. Die Aktienvolatilität kann von solchen Wechselwirkungen abhängen. Die Zahl der Kreuzterme wächst schnell mit der Ordnung m, deshalb sind Einschränkungen nötig.
- Beim RCA-Modell ist die Volatilität eine quadratische Funktion der beobachteten verzögerten Werte r_{t−i}, beim CHARMA eine quadratische Funktion der verzögerten Innovationen a_{t−i}.
- Haben die täglichen Logrenditen hohe Exzess-Kurtosis und serielle Korrelationen, können die Stichprobenschätzer der Monatsvolatilität in den Gleichungen (3.49) und (3.50) inkonsistent sein (Bai, Russell und Tiao, 2004).
- Im AR(1)–EGARCH(1,1) für die monatlichen IBM-Logrenditen 1926 bis 1997 bleibt in den standardisierten Residuen keine bedingte Heteroskedastizität: Q(10) = 4,13 (p = 0,90) und Q(20) = 15,93 (p = 0,66) für den quadrierten Prozess.
- Ist die bedingte Varianzfunktion h(·) zeitabhängig, heißt die Reihe in der Varianz nichtlinear. Die bedingt heteroskedastischen Modelle von Kapitel 3 sind in der Varianz nichtlinear, weil σ²_t sich über die Zeit entwickelt.
- Außer bei GARCH-M, wo der bedingte Mittelwert von σ²_t abhängt, konzentrieren sich die Volatilitätsmodelle von Kapitel 3 auf die bedingte Varianzgleichung.
- Eine Verallgemeinerung des bilinearen Modells hat bedingte Heteroskedastizität. Für x_t = μ + Σ β_i a_{t−i} a_t + a_t mit weißem Rauschen ist die bedingte Varianz [1 + Σ β_i a_{t−i}]² σ²_a, ähnlich dem RCA- oder CHARMA-Modell.
- Nach der Wold-Zerlegung ist eine schwach stationäre, rein stochastische Reihe eine lineare Funktion unkorrelierter Schocks. Bei stationären Volatilitätsreihen sind diese Schocks unkorreliert, aber abhängig.
- Im GARCH(1,1) existiert das vierte Moment von σ_t nur, wenn 1 − α₁²(K_ε + 2) − (α₁ + β₁)² > 0 ist, zusätzlich zu α₁ + β₁ < 1.
- Das TGARCH für die täglichen IBM-Renditen von 1962 bis 2003 scheitert an der bedingten Heteroskedastizität: Q(10) = 97,07 und Q(20) = 170,3 für die quadrierten standardisierten Residuen, beide mit p = 0,00.
- Das AR(2)–TAR–GARCH(1,1) ist dafür angemessen: Q(10) = 13,54 (0,20) und Q(20) = 19,56 (0,49) für die quadrierten standardisierten Residuen.
- In diesem TAR-GARCH hängt auch das Gewicht der verzögerten bedingten Varianz vom Vorzeichen des vorherigen Schocks ab: der Zusatz ist (0,030 a²_{t−1} + 0,062 σ²_{t−1}) N_{t−1}.
- Für den wöchentlichen 3-Monats-Treasury-Bill-Satz von 1970 bis 1997, 1461 Beobachtungen, steigt die mit |y_t| genäherte Volatilität mit dem Zinsniveau. Die Steigung scheint sich zu beschleunigen, wenn der Satz sich 10 Prozent nähert.
- Das ARCH(2) der monatlichen 3M-Renditen lässt die bedingte Varianz von a²_{t−1} und a²_{t−2} abhängen, bildet die asymmetrische Reaktion auf das Vorzeichen des Schocks aber nicht ab. Das STAR-Modell ergänzt genau diese Abhängigkeit.
- McLeod und Li (1983) nutzen die Ljung-Box-Statistik der quadrierten Residuen, um bedingte Heteroskedastizität von a_t zu erkennen.
- Die Null dieser Prüfung ist β1 = … = βm = 0 in a²_t = β0 + β1 a²_{t−1} + … + βm a²_{t−m} + e_t.
- Die Statistik ist asymptotisch äquivalent zum Lagrange-Multiplikator-Test von Engle (1982) für ARCH-Modelle.
- Für Finanzzeitreihen werden Ljung-Box-Statistiken und Engles Test üblicherweise eingesetzt, um bedingte Heteroskedastizität zu entdecken, ehe Nichtlinearitätstests der übrigen Art oder eine nichtlineare Modellklasse folgen.
- Im AR(2)–TAR–GARCH(1,1) für die täglichen IBM-Logrenditen hängt die bedingte Varianz vom Vorzeichen des vorherigen Schocks ab: der Zusatz a2 a²_{t−1} + b2 h_{t−1} wird nur gesetzt, wenn a_{t−1} < 0.
- Im geglätteten Schwellen-IGARCH für GE gewichtet die logistische Funktion 1 / (1 + exp(−10 a_{t−1})) einen zusätzlichen Varianzterm, sodass ein negativer und ein positiver Schock derselben Größe die bedingte Varianz verschieden fortschreiben.
- Das Markov-Switching-Beispiel lässt die bedingte Varianz zwischen einem Zustand ohne Konstante und einem Zustand mit Konstante 4,24 wechseln.
- Im Ordered Probit ist die bedingte Varianz σ²_i = g(w_i) eine positive Funktion erklärender Größen; w_i kann das Zeitintervall t_i − t_{i−1} und bedingt heteroskedastische Variablen enthalten.
- Für IBM 1988 lautet die Spezifikation σ²_i(w_i) = 1,0 + γ1² Δt*_i + γ2² AB_{i−1}, mit γ1 = 0,40 (t = 15,6) und γ2 = 0,52 (t = 71,1).
- Die Transaktionsdauer beeinflusst sowohl den bedingten Mittelwert als auch die bedingte Varianz der Preisänderung.
- Der Bid-Ask-Spread zum Zeitpunkt t_{i−1} beeinflusst die bedingte Varianz signifikant.
- Δt*_i = (t_i − t_{i−1})/100 ist die in Sekunden gemessene und durch 100 skalierte Dauer zwischen den Trades.
- Der ökonometrische VaR-Ansatz modelliert die Volatilität mit bedingt heteroskedastischen Modellen; dargestellt wird das mit GARCH, zulässig sind auch die nichtlinearen Volatilitätsmodelle.
- RiskMetrics nimmt eine bedingt normale Tagesrendite rt gegeben Ft minus 1 an, mit bedingter Varianz σ zum Quadrat von t = α mal σ zum Quadrat von t minus 1 plus (1 minus α) mal r zum Quadrat von t minus 1.
- Die Volatilitätsprognose der k-Perioden-Rendite ist die bedingte Varianz des Prognosefehlers der k-Perioden-Rendite gegeben der Informationsmenge am Prognoseursprung und wird aus den schrittweisen GARCH-Prognosen zusammengesetzt.
- Die endliche Stichprobenverteilung der geschätzten Kreuzkorrelationen von Assetrenditen ist unter anderem wegen bedingter Heteroskedastizität und hoher Kurtosis kompliziert.
- Die univariaten Renditereihen von IBM und S&P 500 dürften bedingte Heteroskedastizität haben; multivariate Volatilität wird in Kapitel 10 behandelt.
- Die BARRA-Querschnittsregression ist nicht homogen, weil die Kovarianz der spezifischen Faktoren die Diagonalmatrix D mit assetspezifischen Varianzen σ²i ist. Die Faktorrealisation wird deshalb mit gewichteten kleinsten Quadraten geschätzt, wobei die Standardfehler der spezifischen Faktoren die Gewichte sind.
- D ist unbekannt. Im ersten Schritt liefert die gewöhnliche Kleinste-Quadrate-Schätzung konsistente, aber nicht effiziente Faktorrealisationen; die Residuen werden über t = 1 bis T gepoolt und die Diagonale ihrer mittleren äußeren Produkte, geteilt durch T−1, schätzt D. Im zweiten Schritt geht diese Schätzung in die verallgemeinerte Kleinste-Quadrate-Formel ein.
- Multivariate Volatilitätsmodellierung betrifft die zeitliche Entwicklung der bedingten Kovarianzmatrix Σt gleich Cov(at gegeben Ft−1).
- Für eine k-dimensionale Renditereihe enthält diese bedingte Kovarianz k mal (k plus 1) durch 2 zeitveränderliche zweite Momente. Bei fünf Dimensionen sind das 15 bedingte Varianzen und Kovarianzen.
- Im DVEC-Modell folgt jedes Element der bedingten Kovarianz einem eigenen GARCH-artigen Prozess. Dynamische Abhängigkeit zwischen den Volatilitätsreihen ist damit ausgeschlossen, und die Kovarianz muss nicht positiv definit sein.
- Das BEKK-Modell lässt dynamische Abhängigkeit zwischen den Volatilitätsreihen zu und ist fast sicher positiv definit, wenn AA′ positiv definit ist.
- Sind im Constant-Correlation-GARCH(1,1) die Matrizen alpha1 und beta1 beide diagonal, sind die beiden Volatilitätsprozesse dynamisch nicht verbunden.
- Die univariaten GARCH(1,1)-Gleichungen von Hang Seng und Nikkei 225 liegen nahe an IGARCH(1,1): Die Summe der Koeffizienten ist 0,143 plus 0,855 für Hongkong und 0,127 plus 0,861 für Japan. Das passt zur durch die Subprime-Krise erhöhten Volatilität.
- Beim Constant-Correlation-GARCH(1,1) für IBM und den S&P 500 haben die standardisierten Residuen auf dem 5-Prozent-Niveau keine bedingte Heteroskedastizität. Für die Quadrate ist Q2(4) gleich 18,00 mit p gleich 0,16 und Q2(8) gleich 39,09 mit p gleich 0,10.
- Die standardisierten Residuen des zeitvariablen Korrelations-GARCH(1,1) für IBM und den S&P 500 haben keine signifikante bedingte Heteroskedastizität. Für die Quadrate ist Q2(4) gleich 16,69 mit p gleich 0,27 und Q2(8) gleich 36,71 mit p gleich 0,19.
- Dasselbe gilt für das Cholesky-Modell dieser Reihe: Q2(4) der quadrierten standardisierten Residuen ist 15,34 mit p gleich 0,36 und Q2(8) ist 31,87 mit p gleich 0,37.
- Beim univariaten GARCH des S&P 500, Tageslogrenditen 1991 bis 1999, ist Q(10) der quadrierten standardisierten Residuen 3,14 mit p gleich 0,98. Im dreidimensionalen Modell mit Cisco und Intel ist Q3(4) der quadrierten Residuen 28,71 mit p gleich 0,58 und Q3(8) gleich 52,00 mit p gleich 0,91.
- Im DCC-Modell der zwei Aktienrenditen von IBM und Dell ist die Varianzdynamik nahezu integriert: Die Summe der GARCH-Koeffizienten beträgt 0,9975, und die konstanten Terme unterscheiden sich nicht signifikant von null.
- Der Hebelterm macht die bedingte Varianz asymmetrisch: Ein negativer vorheriger Schock geht in die Varianzgleichung ein, ein nichtnegativer nicht. Im Vier-Asset-Beispiel ist dieser Hebel nur bei den Aktien signifikant.
- Das Faktor-Volatilitätsmodell (10.39) erfasst die bedingte Heteroskedastizität der monatlichen IBM- und S&P-500-Logrenditen vor allem bei höheren Lags nicht ausreichend, weil der eine gemeinsame Faktor nur etwa 82,5 Prozent der verallgemeinerten Varianz erklärt.
- Die quadrierten standardisierten Residuen dieses Modells haben Q-Stern-2(4) gleich 20,25 bei einem p-Wert von 0,09 und Q-Stern-2(8) gleich 61,95 bei einem p-Wert von 0,0004.
- Bei der logarithmierten realisierten Alcoa-Volatilität haben die quadrierten Residuen des ARIMA(0,1,1) Q(12) gleich 8,2 bei einem p-Wert von 0,77, also keine erkennbaren ARCH-Effekte.
- Für die standardisierten Ein-Schritt-Prognosefehler der logarithmierten realisierten Alcoa-Volatilität ist die LM-Statistik auf ARCH über 25 Lags gleich 18,48 bei einem p-Wert von 0,82. Das lokale Trendmodell zeigt danach keine bedingte Heteroskedastizität in diesen Residuen.
- Im univariaten stochastischen Volatilitätsmodell ist at = sqrt(ht) εt, sodass die bedingte Varianz der Renditeinnovation die latente Größe ht ist und nicht konstant.
- Die Logvolatilität folgt ln ht = α0 + α1 ln ht−1 + vt; die Logtransformation hält ht für alle t positiv, und |α1| < 1 macht ln ht stationär.
- εt ist gaußsches weißes Rauschen mit Mittel 0 und Varianz 1, vt ebensolches mit Varianz σ²v, und beide Folgen sind unabhängig.
- Die Likelihood ist ein Gemisch über die n-dimensionale Verteilung von H und deshalb per Maximum-Likelihood schwer; unter Bayes ist H ein Vektor augmentierter Parameter.
- GARCH mit zeitvariablen Korrelationen, BEKK(1,1) und das bivariate stochastische Volatilitätsmodell liefern für die monatlichen IBM-Logrenditen 1962 bis 2009 ähnliche Verläufe der bedingten Varianz, mit Clustering und steigendem Trend.
- Das bivariate GARCH erzeugt für den S&P 500 um 1993 einen zusätzlichen Varianzgipfel, der univariaten, BEKK- und SV-Verläufen fehlt und als scheinbar, induziert durch die Abhängigkeit von IBM, beschrieben wird.
- GARCH erzeugt zudem höhere Spitzenwerte der bedingten Varianz und für IBM einen zusätzlichen Gipfel 1993.
- Die angepassten Volatilitäten des S&P 500 im bivariaten SV-Modell ähneln der univariaten Analyse.

## Funktionsweise

- Im PCD-Modell für die Richtung gilt ln(σi) = β |Di−1 + Di−2 + Di−3 + Di−4|; die Varianz der Preisrichtung steigt, wenn die vergangenen Richtungen einen lokalen Trend anzeigen.
- Bei festem Mittelwert macht eine größere Varianz der Normalverteilung eine Ziehung mit gleicher Chance positiv oder negativ und erhöht so die Chance einer Folge gleichgerichteter Ziehungen, die einen lokalen Preistrend erzeugt.
- Für IBM am 21. November 1990 lautet die Varianzgleichung ln(σi) = 0,244 |Di−1 + Di−2 + Di−3 + Di−4|, mit Standardfehler 0,182; der Parameter ist marginal signifikant.

## Voraussetzungen


## Anwendung im Trading

- Für Strukturbruchtests auf langen Reihen mit Blasen und Einbrüchen sind Logpreise den Rohpreisen vorzuziehen.
- Der Unterschied fällt bei kleinen Stichproben mit einem Niveau-Faktor nahe 1 oft kaum ins Gewicht, SADF regressiert aber über Jahrzehnte, und Blasen erzeugen zwischen Regimes deutlich verschiedene Niveaus.
- Im inhomogenen Poisson-Modell für Extremwerte ist die Volatilität σ zum Quadrat von t der Rendite ein Beispiel für eine erklärende Variable, die Form, Skala und Lage zeitabhängig machen kann.

## Regeln und Kriterien

- Nach dem Bau eines VAR-Modells können an den Residuen auch bedingte Heteroskedastizität und Ausreißer geprüft werden, nicht nur die Portmanteau-Statistik auf serielle und Kreuzkorrelationen.

## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]
- Advances in Financial Machine Learning.pdf, S. 286–305 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-016-p286-p305|S. 286–305]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 39–58 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-003-p039-p058|S. 39–58]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 77–96 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-005-p077-p096|S. 77–96]]
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
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 343–362 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-019-p343-p362|S. 343–362]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 362–381 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-020-p362-p381|S. 362–381]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 381–400 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-021-p381-p400|S. 381–400]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 400–419 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-022-p400-p419|S. 400–419]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 419–438 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-023-p419-p438|S. 419–438]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 495–514 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-027-p495-p514|S. 495–514]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 514–533 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-028-p514-p533|S. 514–533]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 533–552 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-029-p533-p552|S. 533–552]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 552–571 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-030-p552-p571|S. 552–571]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 571–590 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-031-p571-p590|S. 571–590]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 590–609 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-032-p590-p609|S. 590–609]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 647–666 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-035-p647-p666|S. 647–666]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 666–685 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-036-p666-p685|S. 666–685]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 685–704 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-037-p685-p704|S. 685–704]]

## Verwandte Themen
