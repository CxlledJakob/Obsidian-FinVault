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

# Lineare Regression


## Kurzdefinition

- Die wichtigste Art eines wissenschaftlichen Gesetzes ist die funktionale Beziehung: Die zu prognostizierende abhängige Variable Y ist eine Funktion eines oder mehrerer Prädiktoren X, geschrieben Y gleich f von Xi.

## Kernaussagen

- Die geschätzte Beziehung lautet ES mal 50 gleich minus 0,3906 mal VX mal 1.000 plus 77.150 Dollar, mit ES und VX als Settlement-Preisen.
- Die Standardabweichung der Residuen beträgt 2.047 Dollar.
- Aus der Regression folgt ein Portfolio long 0,3906 Kontrakte VX und long einen Kontrakt ES.
- Die Hedge Ratio der VX-ES-Rollrendite-Strategie stammt aus der Regression der Preise von VX gegen ES in Gleichung 5.11 und nicht aus der Regression ihrer Renditen wie im Original von Simon und Campasano, deshalb weicht sie leicht von deren Angabe ab.
- Wenn Experten mehrfaktorielle Entscheidungen subjektiv treffen, stützen sie sich vor allem auf eine lineare Kombinationsregel, aber weniger wirksam als formale lineare Regressionsmodelle.
- Sie sind weniger wirksam, weil sie die Information nicht so konsistent kombinieren wie ein formales mathematisches Modell.
- In einem sequenziellen Problem lässt sich jede Variable für sich deuten, und die Einzelbotschaften werden danach algebraisch addiert; die Botschaft einer Variable hängt dann nicht von den anderen ab.
- In einem konfigurativen Problem steckt die Information im Beziehungsgeflecht der Variablen, die sich nicht isoliert bewerten lassen: ein hoher Wert von A kann bei niedrigem B und hohem C etwas anderes bedeuten als bei hohem B und niedrigem C.
- Eine lineare Funktion ist vergleichsweise einfach, weil sie nur durch zwei Koeffizienten oder Freiheitsgrade definiert ist: ihre Steigung und den Schnitt mit der senkrechten Achse, den y-Achsenabschnitt. Verbessern lässt sich der Fit nur über diese beiden Größen.
- Eine Funktion lässt sich als mathematische Hypothese auffassen, die eine gegebene Menge von Beobachtungen erklärt.
- Wird eine Funktion mit der Methode der Kleinste-Quadrate-Regression an Daten angepasst, ist ein perfekter Fit garantiert, wenn sie so viele Freiheitsgrade, also Koeffizienten, enthalten darf, wie es Datenpunkte gibt.
- Die lineare Funktion berührt nicht jeden beobachteten Punkt, beschreibt aber die allgemeine Tendenz, dass steigende X-Werte mit steigenden Y-Werten einhergehen. Damit erfasst sie das wesentliche Merkmal und ist eher die echte Beziehung zwischen X und Y.
- Unter sonst gleichen Bedingungen ist die einfachere Erklärung eher richtig. Eine aufwendige Kurve kann gerechtfertigt sein, wenn genug Daten vorliegen und ein komplexer Prozess sie erzeugt hat.
- Bei Camerer waren die subjektiven Urteile der Experten am ungenauesten und die mit Regressionsanalyse geschätzten multivariaten linearen Modelle am genauesten, genauer auch als ein mathematisches Modell davon, wie die Experten ihre Urteile bildeten.
- Goldberg zeigte 1968, dass ein lineares Prognosemodell auf Persönlichkeitstestwerten neurotische von psychotischen Patienten besser trennte als erfahrene klinische Diagnostiker.
- Das Modell von Goldberg traf zu 70 Prozent, die Treffer der Experten lagen zwischen 52 und 67 Prozent.
- Lineare Modelle meinen hier nicht nur eine lineare Preisprognose, sondern auch eine lineare Kapitalallokation.
- Zu jedem nichtlinearen Modell gibt es über die Taylor-Entwicklung meist eine einfachere lineare Näherung; eine Begründung ist nötig, warum sie nicht genügt, außer wenn die Terme niedriger Ordnung verschwinden, was realistische Finanzzeitreihen selten beschreiben.
- Die ADF-Gleichung ist die lineare Regression Δy(t) = λ y(t minus 1) + μ + βt + α1 Δy(t minus 1) + … + αk Δy(t minus k) + εt. Die Teststatistik ist der Koeffizient von y(t minus 1), geteilt durch seinen Standardfehler.
- Für die Halbwertszeit werden Drift und verzögerte Differenzen weggelassen und Δy auf das verzögerte y plus eine Konstante regressiert. λ ist der erste Steigungskoeffizient, die Halbwertszeit ist minus log(2)/λ.
- Die Hedge Ratio eines Paares ist der Steigungskoeffizient der Kleinste-Quadrate-Regression der einen Preisreihe auf die andere plus Konstante. Sie ist nicht der genaue Kehrwert, wenn abhängige und unabhängige Variable getauscht werden.
- Im Mehrreihenfall ist Λ eine Matrix. Λ gleich 0 bedeutet, dass der nächste Schritt nicht vom aktuellen Preisniveau abhängt und keine Kointegration vorliegt.
- Die Halbwertszeit eines Portfolios wird bestimmt, indem die Änderung seines Nettomarktwerts yport auf den verzögerten yport und eine Konstante regressiert wird. Die Halbwertszeit ist minus log(2) geteilt durch den ersten Steigungskoeffizienten.
- yport ist die Summe aus Eigenvektor-Stückzahl mal Preis über alle ETFs. Für EWA, EWC und IGE ergibt diese Regression 23 Tage, gegen etwa 115 Tage bei USD.CAD.
- Für ein wirklich kointegrierendes Paar wird die Hedge Ratio mit OLS auf möglichst langer Historie oder mit dem Johansen-Test geschätzt.
- Für GLD und USO wird die Hedge Ratio täglich neu geschätzt: OLS von USO auf GLD plus Konstante über die letzten 20 Handelstage. Der Spread ist minus Hedge-Ratio mal GLD plus USO. Alternativ dient der erste Johansen-Eigenvektor.
- Dieselbe Regression auf Logpreisen liefert die Gewichte als Kapitalgewichte. Sie erreicht etwa 9 Prozent APR und eine Sharpe Ratio von 0,5, unter den etwa 10,9 Prozent und 0,59 des Preisspreads, und das vor den Rebalancing-Kosten.
- Der Kalman-Filter ist eine dynamische lineare Regression. δ gleich 0 setzt Steigung und Achsenabschnitt fest und fällt mit der OLS-Regression zusammen.
- Die Koeffizienten der ES-VX-Regression werden nur auf den ersten 500 Tagen nach August 2008 als Trainingsset geschätzt.
- Eine Regression auf der Mischung der Regime 2004 bis Mai 2008 und August 2008 bis 2012 wäre ein Fehler; verwendet wird das zweite Regime, das bis zum Schreibzeitpunkt reicht.
- Vor der Regression werden die VX-Preise mit 1.000 und die ES-Preise mit 50 multipliziert, weil ein Punkt VX 1.000 Dollar und ein Punkt ES 50 Dollar entspricht und die Hedge Ratio sonst nicht das Kontraktverhältnis trifft.
- Das AR(1) hat dieselbe Form wie die einfache lineare Regression, mit rt als abhängiger Variable und rt−1 als erklärender Variable; zwischen beiden Modellen bestehen dennoch bedeutsame Unterschiede.
- Das AR(p) hat die Form einer multiplen linearen Regression, in der die verzögerten Werte rt−i gemeinsam den bedingten Erwartungswert von rt bestimmen.
- Die aufsteigenden AR-Modelle zur partiellen Autokorrelation werden mit der Kleinste-Quadrate-Methode geschätzt und sind so angeordnet, dass die Idee des partiellen F-Tests der multiplen Regression anwendbar ist.
- Die bedingte Kleinste-Quadrate-Schätzung eines AR(p) startet bei der Beobachtung p plus 1 und ist, bedingt auf die ersten p Beobachtungen, eine multiple lineare Regression.
- Der Varianzschätzer dieser bedingten Kleinste-Quadrate-Methode ist die Summe der quadrierten Residuen von t gleich p plus 1 bis T, geteilt durch T minus 2p minus 1.
- Bei der bedingten Likelihood bleiben die Koeffizientenschätzungen unverändert, die Innovationsvarianz wird aber mit (T minus 2p minus 1) geteilt durch (T minus p) skaliert; in manchen Paketen steht im Nenner T statt T minus p.
- Das Bestimmtheitsmaß eines stationären AR(p) ist 1 minus die Summe der quadrierten Residuen von t gleich p plus 1 bis T, geteilt durch die Summe der quadrierten Abweichungen vom Mittel über denselben Bereich; es liegt zwischen 0 und 1.
- Ein größeres R² zeigt eine engere Anpassung nur bei einer stationären Reihe.
- Bei einer unit-root-nichtstationären Reihe konvergiert das R² einer AR(1)-Anpassung mit wachsendem Stichprobenumfang gegen 1, unabhängig vom wahren Modell von rt.
- R² fällt mit der Zahl der Parameter nicht; das adjustierte R² ist 1 minus die Varianz der Residuen geteilt durch die Stichprobenvarianz von rt und berücksichtigt die Parameterzahl, liegt aber nicht mehr zwingend zwischen 0 und 1.
- Für ein sinnvolles AR(1) muss der Betrag von phi1 höchstens 1 sein; der Steigungskoeffizient β1 einer einfachen linearen Regression yt gleich β0 plus β1 mal xt plus at darf jede feste reelle Zahl sein.
- Die Konstante bedeutet im MA(q) den Mittelwert, im stationären AR oder ARMA einen um die AR-Summe bereinigten Mittelwert und im Random Walk mit Drift die Zeitsteigung; diese unterschiedlichen Deutungen trennen dynamische Modelle von gewöhnlichen linearen Regressionen.
- Eine trendstationäre Reihe wird stationär, indem der lineare Zeittrend durch eine einfache lineare Regression entfernt wird.
- Der erweiterte Dickey-Fuller-Test ist die t-Ratio von β-Dach minus 1 in der Regression der Reihe auf ct, auf den verzögerten Stand und auf verzögerte Differenzen; ct kann null, konstant oder linear in der Zeit sein.
- Ist das Saisonmuster zeitlich stabil und nahe an einer deterministischen Funktion, können Dummy-Variablen die Saisonalität abbilden.
- Deterministische Saisonalität ist der Spezialfall Θ gleich 1 des multiplikativen saisonalen Modells; dann liefern Dummy-Variablen und das multiplikative Modell dieselben Prognosen.
- Ist das saisonale Muster nicht deterministisch, können Dummy-Variablen schlechtere Prognosen liefern als das multiplikative saisonale Modell.
- Im Regressionsmodell yt gleich alpha plus beta mal xt plus et liefert die Methode der kleinsten Quadrate konsistente Schätzungen, wenn der Fehler weißes Rauschen ist; ist der Fehler seriell korreliert, müssen die Schätzungen von alpha und beta nicht konsistent sein.
- Eine Regression mit Zeitreihenfehlern ist in Ökonomie und Finanzen weit verbreitet und wird häufig falsch benutzt, weil die serielle Abhängigkeit des Fehlers übersehen wird.
- Das Vorgehen ist: Regression schätzen und serielle Restkorrelation prüfen; ist das Residuum einheitswurzel-nichtstationär, beide Seiten einmal differenzieren und von vorn beginnen; ist es stationär, ein ARMA für die Residuen ansetzen; danach gemeinsam per Maximum-Likelihood schätzen und nachbessern.
- Ist das Zeitreihenmodell der Fehler stationär und invertierbar, kann das ganze Modell gemeinsam mit der Maximum-Likelihood-Methode geschätzt werden.
- Vor modernen Rechnern diente dafür unter anderem der Cochrane-Orcutt-Schätzer (Greene 2003, S. 273).
- Beispiele sind das Marktmodell, das die Überschussrendite einer Aktie mit der eines Marktindex verknüpft, und die Zinsstruktur über Laufzeiten.
- Für die wöchentlichen Treasury-Sätze, 2467 Beobachtungen vom 5. Januar 1962 bis 10. April 2009, lautet die Niveauregression r3t gleich 0,832 plus 0,930 mal r1t plus et, residuale Standardabweichung 0,523, Bestimmtheitsmaß 96,5 Prozent, Standardfehler 0,024 und 0,004; sie ist unzureichend, weil die Residuen ein Einheitswurzelmuster zeigen.
- Die Änderungsgleichung c3t gleich 0,792 mal c1t plus et hat die residuale Standardabweichung 0,0690, das Bestimmtheitsmaß 82,5 Prozent und den Standardfehler 0,0073; die Restkorrelation ist deutlich kleiner, aber noch signifikant.
- Mit MA(1)-Fehler gilt c3t gleich 0,794 mal c1t plus et und et gleich at plus 0,1823 mal at minus 1, residuale Standardabweichung 0,0678, Bestimmtheitsmaß 83,1 Prozent, Standardfehler 0,0075 und 0,0196.
- Nach diesem MA(1) ist die Lag-1-Restautokorrelation nicht mehr signifikant; kleinere Restkorrelationen bleiben auf den Lags 4, 6 und 7, zusätzliche MA-Glieder dort bringen nur einen kleinen, nicht ausgewiesenen Gewinn.
- Das hohe Bestimmtheitsmaß 96,5 Prozent und der Koeffizient 0,930 der Niveauregression sind irreführend; bei den Änderungen liegen Bestimmtheitsmaß und Koeffizient der einfachen und der MA(1)-Regression nahe beieinander.
- In R ist der Niveaukoeffizient 0,92955 mit Standardfehler 0,00357 und t-Wert 260,40, der Achsenabschnitt 0,83214 mit Standardfehler 0,02417, das Bestimmtheitsmaß 0,9649 und der residuale Standardfehler 0,5228 bei 2465 Freiheitsgraden.
- Die Differenzregression ohne Achsenabschnitt schätzt in R 0,791935 mit Standardfehler 0,007337 und t-Wert 107,9, residualer Standardfehler 0,06896, Bestimmtheitsmaß 0,8253; die gemeinsame ARIMA-Schätzung hat ma1 gleich 0,1823 und Steigung 0,7936, sigma quadrat 0,0046, Bestimmtheitsmaß 0,8310077.
- Eine Regression mit zusätzlichem Lag der abhängigen und der erklärenden Änderung hat das Bestimmtheitsmaß 0,8312, den residualen Standardfehler 0,06785 bei 2461 Freiheitsgraden, den Koeffizienten 0,7971 auf der gleichzeitigen Änderung, 0,1766 auf dem Lag der Dreijahresänderung und minus 0,1580 auf dem Lag der Einjahresänderung.
- Der Lagrange-Multiplikator-Test auf ARCH-Effekte ist der F-Test der linearen Regression der quadrierten Residuen auf eine Konstante und m eigene Lags.
- Die Quadrate folgen dieser Regression in der Form eines AR(m), der Fehler ist aber nicht unabhängig und identisch verteilt; die Kleinste-Quadrate-Schätzer sind konsistent, aber nicht effizient.
- Im CAPM kann die Mittelgleichung rt gleich phi 0 plus beta mal der Marktrendite plus at geschrieben werden.
- Die allgemeine Mittelgleichung mit erklärenden Variablen ist eine finanzwirtschaftliche Anwendung der Regression mit Zeitreihenfehlern; eine Dummy kann zum Beispiel den Montag und damit den Wochenendeffekt aufnehmen.
- Die bedingte Log-Likelihood eines normalen ARCH(m) summiert über t ab m plus 1 den Term ein halb ln von sigma t quadrat plus ein halb a t quadrat durch sigma t quadrat, mit sigma t quadrat gleich alpha 0 plus den gewichteten vergangenen Quadraten.
- Die lokale lineare Regression minimiert Σ [y_t − a − b(x − x_t)]² K_h(x − x_t) und schätzt m(x) durch das resultierende a. Das resultierende b schätzt die erste Ableitung von m an der Stelle x.
- Unter der Kleinste-Quadrate-Theorie ist das ein gewichtetes Kleinste-Quadrate-Problem mit geschlossener Lösung für a.
- Setzt man nur voraus, dass die erste Ableitung existiert, und minimiert die kerngewichtete Summe von (y_t − a)², ergibt sich der Nadaraya-Watson-Schätzer.
- Hat m(x) eine beschränkte k-te Ableitung, kann das lineare Polynom durch ein Polynom der Ordnung k−1 ersetzt werden. Fan (1993) zeigt unter Regularitätsbedingungen wichtige Stichprobeneigenschaften des lokalen linearen Schätzers.
- Das lineare Modell x_t = μ + Σ ψ_i a_{t−i} ist die Taylor-Entwicklung erster Ordnung der allgemeinen Funktion der Schocks. Das bilineare Modell nimmt die Terme zweiter Ordnung, also die Produkte x_{t−i} a_{t−j}, hinzu.
- Sind bei linearem Output direkte Verbindungen von der Eingabe zur Ausgabe erlaubt, verallgemeinert das neuronale Netz ein lineares Modell. Die direkten Verbindungen überspringen die verborgene Schicht.
- Für den 3-Monats-Treasury-Bill-Satz schätzt lowess den bedingten Mittelwert und die Volatilität als glatte Funktionen des vorherigen Satzes. Der geglättete Mittelwert ist im Wesentlichen null.
- Das Training eines Feed-forward-Netzes wählt Bias und Gewichte so, dass ein Anpassungskriterium minimal wird, im Beispiel die Kleinste-Quadrate-Summe S² = Σ_{t=1}^{T} (r_t − o_t)²; das ist ein nichtlineares Schätzproblem.
- Der RESET-Test von Ramsey (1969) ist ein Spezifikationstest der linearen Kleinste-Quadrate-Regression und lässt sich unmittelbar auf lineare AR-Modelle anwenden.
- Ist das lineare AR(p) angemessen, sollen die Koeffizienten einer ergänzenden Regression der Residuen auf die ursprünglichen Regressoren und auf Potenzen der angepassten Werte null sein; geprüft wird das mit der üblichen F-Statistik.
- Keenan (1985) zerlegt diesen zweiten Schritt, damit die Multikollinearität zwischen x̂²_t und X_{t−1} vermieden wird: zuerst wird x̂²_t auf X_{t−1} regressiert, danach das AR-Residuum nur noch auf das dabei entstehende Residuum.
- Der Ori-F-Test ist die partielle F-Statistik für α = 0 in der linearen Kleinste-Quadrate-Regression x_t = X′_{t−1} φ + M′_{t−1} α + e_t, wobei M_{t−1} die Produkte und Quadrate der verzögerten Beobachtungen enthält.
- Die geordnete Autoregression von Tsay (1989) schreibt das SETAR als lineare Regression im Schwellenraum: x_{(j)+d} hängt weiterhin von x_{(j)+d−i} ab, steht aber nach aufsteigendem x_{t−d}, und die Schwelle r1 ist dort der Änderungspunkt der Koeffizienten.
- Das Ordered-Probit-Modell setzt die unbeobachtete stetige Preisänderung als lineare Funktion an: y*_i = x_i β + ε_i, mit E(ε_i | x_i) = 0 und bedingter Varianz σ²_i = g(w_i).
- Die beobachtete diskrete Preisänderung y_i fällt in die Kategorie s_j, wenn die latente Größe zwischen den Schwellen α_{j−1} und α_j liegt.
- Die Koeffizienten der deterministischen Tageskomponente der Handelsdauer werden durch Kleinste Quadrate der linearen Regression von ln(Δt_i) auf die Funktionen f_j(t_i) geschätzt.
- Die angepasste Dauerngleichung für IBM hat den Achsenabschnitt 2,555 und die Steigungen 0,159, 0,270, 0,384, 0,061, −0,611, −0,157 und 0,073 auf f1 bis f7.
- Zu den Regressoren des IBM-Probit 1988 gehören die skalierte Dauer, drei Lags der Preisänderung, drei Lags der Fünf-Minuten-Rendite des nächstfälligen S&P-500-Indexfutures, drei Lags des Quote-Indikators IBS und drei Lags von Box-Cox-transformiertem Dollarvolumen mal IBS.
- Die Quantilregression schätzt das bedingte p-Quantil in rt = β Strich xt plus at, indem die Summe der Check-Funktion wp(rt minus β Strich xt) minimiert wird.
- Die Check-Funktion ist wp(z) = p mal z für z mindestens 0 und (p minus 1) mal z für z < 0. Dieselbe Funktion liefert ohne Regressoren das gewöhnliche empirische Quantil.
- Koenker und Bassett (1978) führen die Regressionsquantile ein; ein Programm steht bei Koenker und D'Orey (1987), in R im Paket quantreg.
- Für die Blockmaxima liefert die zweifache Logarithmierung der Extremwert-Verteilungsfunktion eine Regression der Ordnungsstatistiken auf Form-, Lage- und Skalenparameter. Die Kleinste-Quadrate-Schätzer minimieren die Summe der quadrierten Abweichungen ei, die als nicht seriell korreliert angenommen werden.
- Im Fall ξn = 0 wird diese Regression linear: der zweifache Logarithmus von i / (g plus 1), mit negativem Vorzeichen im inneren Logarithmus, ist gleich minus Blockmaximum geteilt durch αn plus βn geteilt durch αn plus ei.
- Diese Kleinste-Quadrate-Schätzer sind konsistent, aber weniger effizient als die Likelihood-Schätzer; das Kapitel verwendet die Likelihood-Schätzungen.
- Grundlage der Regressionsmethode ist, dass der Erwartungswert der Extremwert-Verteilungsfunktion an der i-ten Ordnungsstatistik der Blockmaxima gleich i / (g plus 1) ist.
- Das statistische Faktormodell rt minus µ gleich β ft plus εt sieht wie eine multivariate lineare Regression aus, ist aber keine, weil die gemeinsamen Faktoren und die Faktorladungen unbeobachtbar sind.
- In der Verfeinerung der asymptotischen Hauptkomponentenanalyse wird für jedes Asset die Regression der Rendite auf ein konstantes Glied und die geschätzten Faktoren per OLS geschätzt, und aus den Residuen wird die spezifische Varianz berechnet.
- Der Kalman-Gewinn Kt ist der Regressionskoeffizient von μt auf den Ein-Schritt-Prognosefehler vt.
- Die bedingten Momente in Satz 11.1 lassen sich über die multivariate lineare Regression oder über die Faktorisierung der gemeinsamen Dichte herleiten.
- Das CAPM rt gleich αt plus βt mal rM,t plus et ist eine lineare Regression mit zeitvariablem Achsenabschnitt und zeitvariabler Steigung. Die Beobachtungszeile des Zustandsraums ist Zt gleich (1, rM,t).
- Die Regressionskoeffizienten sind die Zustände und wandern als unabhängige Random Walks. Die Kovarianz der Zustandsinnovation ist diagonal mit σ²η und σ²ε, die Varianz des Messfehlers ist σ²e.
- Weil rM,t in der Systemmatrix zeitlich variiert, braucht die SsfPack-Spezifikation eine Datenmatrix X mit den Spalten 1 und Marktrendite und eine Indexmatrix, die diese Spalten der zeitvariablen Zeile zuordnet. Im GM-Beispiel hat X 168 Zeilen.
- Die multiple lineare Regression yt gleich x′t β plus et, et normal mit Varianz σ²e, hat die Zustandsraumform mit festem Zustand st gleich β für alle t.
- Die Systemmatrizen sind Tt gleich der Einheitsmatrix der Dimension p, Zt gleich x′t, dt und ct gleich null, Qt gleich null und Ht gleich σ²e. Weil der Zustand fest ist, wird diffus initialisiert.
- Die Erweiterung lässt βt zufällig sein: βt plus 1 gleich βt plus Rt ηt, ηt standardnormal, Rt der Vektor (σ1 bis σp) mit σi mindestens 0. Ist σi gleich 0, bleibt dieser Koeffizient zeitlich konstant.
- GetSsfReg baut diese Form aus der Matrix der Regressoren. Das Marktmodell rt gleich β0 plus β1 mal rM,t plus et, t von 1 bis 168, verwendet die Bindung aus Einserspalte und Marktrendite, zum Beispiel dem S&P-500-Composite.
- Eine Regression mit ARMA(p, q)-Fehlern ist yt gleich x′t β plus zt und φ(B) zt gleich θ(B) at, at normal mit Varianz σ²a. xt ist k-dimensional.
- Der Spezialfall mit xt gleich 1 für alle t und skalarem β ist das ARMA(p, q) mit von null verschiedenem Mittelwert.
- Der erweiterte Zustand stapelt den ARMA-Zustand von zt und den konstanten Koeffizienten β. Die Beobachtungszeile ist (1, 0, bis 0, x′t) der Länge m plus k, mit m gleich max(p, q plus 1).
- GetSsfRegArma baut diese Form. Im Beispiel yt gleich β0 plus β1 xt plus zt, t von 1 bis 168, folgt zt einem ARMA(2,1) mit Koeffizienten 1,2 und minus 0,35 sowie MA-Koeffizient minus 0,25 in der Darstellung at minus 0,25 at minus 1.
- Bei Handzic (2001) ist der optimale Fehler das Ergebnis einer Regressionsgleichung mit den drei Hinweisen Lufttemperatur, Sonnenschein und Besucherzahl. Ein ROE von 1 heißt, die Person verarbeitet die Information genau wie dieses Regressionsmodell. Ein Wert über 1 ist suboptimale Verarbeitung.
- Die Gruppe mit drei Hinweisen verarbeitete die Information deutlich schlechter als die Gruppe mit einem Hinweis.
- Die Entscheidungsgenauigkeit RNE setzt den absoluten Fehler der Person ins Verhältnis zum Fehler einer naiven Prognose. Ein RNE von 1 entspricht dieser naiven Prognose, ein Wert unter 1 ist eine Verbesserung.
- Die drei Hinweise galten nach Gesprächen mit Eisverkäufern am Bondi Beach als gleich zuverlässig für die Nachfrage des nächsten Tages. Unter- und Überschätzung verursachten gleiche Kosten.
- Eine Regression der aktuellen US-Lage auf neun frühere Blasen dient der Prognose des künftigen Aktienmarktpfads; die Zeitachse misst Monate, der Blasengipfel liegt bei Monat 60.
- Das R² beträgt 0,93, das adjustierte R² 0,926; die US-Aktienblase folgte dem Muster früherer Blasen bisher außerordentlich eng.
- Die Regression ist ökonometrisch problematisch, weil viele sehr ähnliche Blasen zugleich eingehen und Multikollinearität entsteht.
- Die anschließende Regression des S&P 500 auf die erste Hauptkomponente, die archetypische Blase, und die daraus erzeugten Prognosen stützen das erste Ergebnis.
- Auf Basis der vergangenen Blasen ist der Ausblick für den US-Aktienmarkt unangenehm.
- Die zyklischen Prognosetests sind Einfaktorregressionen. Die Renditen werden verzögert, damit nur zum Prognosezeitpunkt bekannte Information eingeht; berichtet werden t-Statistik und adjustiertes R², fette Werte sind signifikant, und die t-Statistiken verwenden wo nötig Newey-West.
- Auf Assetklassenebene bleiben die adjustierten R² meist bei 0,00. Ausnahmen sind das nachlaufende Gewinnwachstum mit 5 Prozent der US-Einjahres-Aktienrendite, der OECD-Frühindikator mit 2 Prozent der Dreimonats-Überrendite, die Zinskurve in den dismal years mit 15 Prozent und das Prognose-BIP in Japan nach der Blase mit 21 Prozent der Einjahres-Überrendite.
- Für die relative Rendite von US-Grundstoff gegen Versorger erklären ISM und MCI über zwölf Monate 22 beziehungsweise 21 Prozent, trotz nachlaufender Daten und nur einer Faktorvariablen.
- Von 36 solchen Regressionen auf US-Aktien und Überrenditen 1984–2003 war nur eine signifikant, und sie wird als Zufallsbefund des Data Minings behandelt.
- Mulligan und Hastie (2005) schätzen mittlere Regressionsgewichte der fünf Geschichtsbausteine Kontext, Problem, Reaktion, Plan und Ergebnis, getrennt danach, ob die Firmengeschichte in Reihenfolge oder verwürfelt erzählt wurde. In der richtigen Reihenfolge springt das Gewicht des Ergebnisbausteins nach oben.
- In der Bedingung mit Geschichtenreihenfolge stützten sich die Teilnehmer bei der Entscheidung vor allem auf den Ergebnisbaustein. Sie zerlegen die Geschichte nicht in ihre Teile und nutzen diese nicht unabhängig, selbst wo das rational wäre.

## Funktionsweise

- Die Preisänderung wird als lineares Modell geschrieben: Δy(t) gleich λ mal y(t−1) plus μ plus βt plus den Lag-Differenzen α1 Δy(t−1) bis αk Δy(t−k) plus einem Störterm, mit Δy(t) gleich y(t) minus y(t−1).
- Die ADF-Statistik ist der Koeffizient λ aus der Regression von Δy(t) auf y(t−1), geteilt durch den Standardfehler dieses Fits.
- Ignoriert man Drift und Lag-Differenzen, trägt das in der diskreten Regression bestimmte λ in die stetige Ornstein-Uhlenbeck-Form hinüber.
- λ wird geschätzt, indem y(t) minus y(t−1) auf y(t−1) und eine Konstante regressiert wird; die Halbwertszeit ist minus log(2) geteilt durch den ersten Beta-Koeffizienten.
- Die optimale Hedge Ratio zweier Reihen ist der erste Koeffizient der Regression der abhängigen Reihe auf die unabhängige Reihe und eine Konstante.
- Die Halbwertszeit des Portfolios wird bestimmt, indem die Änderung des Nettomarktwerts auf dessen verzögertes Niveau und eine Konstante regressiert wird.
- Die Halbwertszeit ist minus log(2) geteilt durch den ersten Regressionskoeffizienten.
- Die Hedge Ratio eines Paares kommt aus einer gewöhnlichen Kleinste-Quadrate-Regression oder aus dem ersten Johansen-Eigenvektor.
- Für GLD und USO wird sie jeden Tag neu geschätzt, als Regression der letzten 20 Beobachtungen der einen Reihe auf die andere Reihe und eine Konstante.
- Für den Log-Preis-Spread wird dieselbe Regression auf den Logpreisen gerechnet, und der Portfoliowert ist die gewichtete Summe der Logpreise.
- Für ein wirklich kointegrierendes Paar wird die Regression einmal auf möglichst langer Historie gerechnet.
- Die Messgleichung des Kalman-Filters ist die lineare Beziehung y(t) gleich x(t) mal β(t) plus Rauschen, mit β aus Achsenabschnitt und Steigung.
- Unter der Annahme konstanter Spot- und Roll-Rendite schätzt eine lineare Regression beide: der Log des Spotpreises wird gegen die Zeit regressiert, und die annualisierte durchschnittliche Spot-Rendite ist 252 mal dem Mittel des Steigungskoeffizienten.
- Die Roll-Rendite verlangt einen festen Zeitpunkt und die Regression der Kontraktpreise gegen die Restlaufzeit; praktisch hängt der Koeffizient von diesem Zeitpunkt und von den dann verfügbaren Kontrakten ab, sodass das geschätzte γ trotz der Konstanzannahme langsam variiert.
- Im Programm werden je Tag die Logpreise der fünf nächsten Laufzeiten auf die Restlaufzeit in Monaten regressiert, sofern fünf aufeinanderfolgende Kontrakte vorliegen, und γ ist minus 12 mal dem Steigungskoeffizienten.
- Das Modell setzt F(t, T) gleich S(t) mal exp(γ mal (t minus T)), S(t) gleich c mal e hoch αt, und damit die Gesamtrendite ∂(log F)/∂t gleich α plus γ sowie die Roll-Rendite minus ∂(log F)/∂T gleich γ.
- Die Halbwertszeit von γ kommt aus der Regression der Änderung von γ auf den verzögerten γ-Wert und eine Konstante und ist minus log(2) geteilt durch den Steigungskoeffizienten.
- Typischerweise sind die Werte der Prädiktoren bekannt und der Wert von Y nicht, oft weil Y ein künftiges Ergebnis ist und die X-Werte aktuell bekannt sind.
- Ist die Beziehung einmal gewonnen, lassen sich Werte der abhängigen Variable prognostizieren, indem die bekannten Prädiktorwerte eingesetzt werden.
- Funktionale Beziehungen werden entweder aus erklärenden Theorien abgeleitet oder aus historischen Daten durch Funktionsanpassung geschätzt, zum Beispiel durch Regressionsanalyse.
- Kaufman diskutiert eine objektive Divergenzmethode, die die Steigungen der beiden verglichenen Zeitreihen per linearer Regression schätzt und die Divergenz als Differenz dieser Steigungen definiert.
- Er stellt Computercode dafür bereit, bietet aber keine Leistungsstatistiken.
- Die Kointegrationsmessung von Divergenzen nutzt eine Regressionsanalyse, um festzustellen, ob zwischen zwei Zeitreihen eine lineare Beziehung besteht.
- Das Error-Correction-Modell misst die Abweichung von dieser typischen linearen Beziehung; wird der Fehler extrem, soll er auf seinen normalen Wert null zurückkorrigieren.
- Der Fosback Index signalisiert, wenn die Cash-Quote der Fonds deutlich von dem Niveau abweicht, das die lineare Beziehung zu den kurzfristigen Zinsen vorhersagt.
- Neben der einfachen linearen Kombination gibt es anspruchsvollere lineare Kombinationen, in denen den Variablen Gewichte zugewiesen werden, also eine gewichtete algebraische Summe.
- Algebraisch meint hier, dass Zahlen mit positiven und mit negativen Werten kombiniert werden.
- Die extremste lineare Prognose gibt allen Faktoren betragsgleiche Gewichte: z(i) ist (f(i) minus Mittel von f) geteilt durch die Standardabweichung von f, geschätzt auf In-Sample-Daten, und die prognostizierte Rendite ist Mittel von R plus Standardabweichung von R mal dem Mittel der Produkte aus Vorzeichen der historischen Korrelation und z(i).
- Wer nur eine Rangfolge braucht, bildet je Faktor den Rang der Aktie, multipliziert mit dem Vorzeichen der Korrelation zur erwarteten Rendite und summiert diese vorzeichenbehafteten Ränge.
- Kahneman schreibt, Formeln mit gleichen Gewichten aller Prädiktoren seien oft überlegen, weil sie nicht von Zufällen der Stichprobe betroffen sind.
- Das Preismodell lautet F(t, T) = c mal e hoch αt mal exp(γ(t − T)). Die Gesamtrendite, die Ableitung des Log-Preises nach t, ist α plus γ. Die Rollrendite, minus die Ableitung nach der Fälligkeit T, ist γ.
- Die Spot-Rendite wird geschätzt, indem der Logarithmus des Spots gegen die Zeit regressiert wird. Annualisiert wird mit 252 mal dem Mittel des Steigungskoeffizienten.
- Die Rollrendite wird je Tag aus den Log-Preisen der fünf nächsten aufeinanderfolgenden Kontrakte gegen die Restlaufzeit in Monaten geschätzt. Gamma ist minus 12 mal dem Steigungskoeffizienten.
- Nur die fünf nächsten Kontrakte werden genommen, weil die Forward-Kurve weiter draußen von Contango in Backwardation oder umgekehrt wechseln kann.
- Trotz konstanter Gamma im Modell hängt der Koeffizient vom Tag und vom Kontraktsatz ab, das geschätzte Gamma variiert also langsam.
- Bei CL fallen die Log-Preise der fünf nächsten Kontrakte gegen die Restlaufzeit nahezu auf eine Gerade, gezeigt für die Kontrakte Januar bis Mai 2007. Entferntere Laufzeiten verlassen die Gerade, und die Gleichung bricht.
- Die annualisierten Mittel sind für den Real-Future −2,7 Prozent Spot und 10,8 Prozent Roll, für Mais 2,8 und −12,8, für WTI 7,3 und −7,1, für Kupfer 5,0 und 7,7 und für die zweijährige Note −0,0 und 3,2 Prozent.
- Positives Gamma bedeutet Backwardation, negatives Contango. Die geschätzte Rollrendite von CL läuft vom 22. November 2004 bis 13. August 2012.
- Erb und Harvey finden für Heizöl von Dezember 1982 bis Mai 2004 eine annualisierte Rollrendite von 4,6 Prozent gegen eine Spot-Rendite von 0,93 Prozent.
- Die logarithmierte Zeitdauer zwischen Preisänderungen wird als multiple lineare Regression mit verzögerten Variablen angesetzt: ln(Δti) = β0 + β1 ln(Δti−1) + β2 Si−1 + σ ϵi, wobei σ > 0 und {ϵi} unabhängig N(0, 1) ist.
- Die Log-Transformation sichert die Positivität der Zeitdauer; weitere erklärende Variablen können ergänzt werden.
- Die Parameter der aufeinanderfolgenden VAR-Modelle werden mit gewöhnlichen Kleinste-Quadraten geschätzt; das ist die multivariate lineare Regression (Johnson und Wichern 1998).
- Bei AR-Modellen sind die OLS-Schätzer von φ0 und der Φj gleich den bedingten Maximum-Likelihood-Schätzern. Die Schätzer der Innovations-Kovarianz unterscheiden sich: Maximum Likelihood teilt durch T, die Residual-Kovarianz der Ordnungsbestimmung durch T minus 2i minus 1.
- Die Strukturform entsteht aus der reduzierten Form durch Linksmultiplikation mit L hoch minus 1 aus der Cholesky-Zerlegung. Die k-te Gleichung zeigt dann ausdrücklich die gleichzeitige lineare Abhängigkeit von rkt von den rit mit i kleiner als k, weil der transformierte Schock mit den vorherigen Komponenten unkorreliert ist.
- In der exakten Likelihood eines VMA(1) ist a0 bei gegebenen θ0 und Θ eine lineare Funktion aller mittelwertbereinigten Beobachtungen. Nach Vormultiplikation mit Σ hoch minus 1/2 ist das System eine multiple lineare Regression in a0 und wird mit gewöhnlichen Kleinste-Quadraten geschätzt.
- Das VAR(1) im S-Plus-Beispiel wird als Regression auf eine Konstante und die eigenen gelagten Komponenten geschätzt. Die Residuen-Skalen sind 7,0078 für IBM und 5,5247 für den S&P 500, bei 995 Beobachtungen und 992 Rest-Freiheitsgraden.
- Die Maximum-Likelihood-Schätzung eines kointegrierten VAR(p) konzentriert die Likelihood für gegebenes m, indem Δxt und xt−1 jeweils multivariat linear auf den deterministischen Term dt und die verzögerten Differenzen regressiert werden. Aus den Residuen ût und ât werden die Stichproben-Kovarianzmatrizen S00, S01 und S11 gebildet.
- Der nicht normierte Maximum-Likelihood-Schätzer des Kointegrationsvektors β besteht aus den ersten m Eigenvektoren dieses Eigenwertproblems. Die übrigen Parameter folgen aus der multivariaten Regression von Δxt auf dt, die restringierte Kombination β̂′c xt−1 und die verzögerten Differenzen.
- Der maximierte Likelihood-Wert bei m Kointegrationsvektoren erfüllt L hoch −2/T proportional zu |S00| mal dem Produkt (1 − λ̂i) von i = 1 bis m und geht in den Maximum-Likelihood-Quotienten für den Rang von Π ein.
- Sind die gemeinsamen Faktoren beobachtet, ist die gestapelte Form des Faktormodells ein multivariates lineares Regressionsmodell. Die Kleinste-Quadrate-Schätzung ist ξ̂′ = (G′G) hoch −1 G′R, die Residuen sind R minus G ξ̂′, und die spezifischen Varianzen werden aus der Diagonale von Ê′Ê / (T − m − 1) gewonnen.
- Diese Kleinste-Quadrate-Schätzung erzwingt die Unkorreliertheit der spezifischen Faktoren nicht und ist im Allgemeinen nicht effizient. Die Nebendiagonalen von Ê′Ê / (T − m − 1) sollen nahe null sein, wenn das Modell passt.
- Im BARRA-Ansatz ist β gegeben, und zu jedem Zeitpunkt ist das Modell eine multiple lineare Regression mit k Beobachtungen und m Unbekannten. Schätzbar ist sie, wenn m kleiner als k ist. Weil die Störvarianzen vom Asset abhängen, wird mit gewichteten kleinsten Quadraten geschätzt; praktisch folgt auf eine gewöhnliche eine verallgemeinerte Kleinste-Quadrate-Schätzung.
- Bei Indikator-Betas der Branchen ist die gewöhnliche Kleinste-Quadrate-Schätzung der Faktorrealisation der Vektor der durchschnittlichen sektoralen Überschussrenditen. Der spezifische Faktor eines Assets ist die Abweichung seiner Überschussrendite vom Branchenmittel.
- Im Fama-French-Ansatz werden die Betas jedes Assets bei gegebenen Faktorrealisationen mit einer Zeitreihenregression geschätzt.
- Die bivariate Cholesky-Zerlegung der bedingten Kovarianz ist die Kleinste-Quadrate-Regression a2t gleich β mal a1t plus b2t. Der Koeffizient β gleich σ21,t durch σ11,t ist der Cholesky-Eintrag q21,t, die Residuenvarianz ist g22,t, und der Fehler b2t ist mit a1t unkorreliert.
- Im dreidimensionalen Fall werden die Schocks nacheinander orthogonalisiert: b1t gleich a1t, b2t gleich a2t minus β21 mal b1t, und b3t gleich a3t minus β31 mal b1t minus β32 mal b2t. Die βij sind die Koeffizienten der Kleinste-Quadrate-Regressionen und gleich den Einträgen qij,t.
- Allgemein ist bit für i größer als 1 der Residuenfehler der Regression von ait auf b1t bis b(i minus 1),t. Die Transformation lautet bt gleich L hoch minus 1 mal at, und die Inverse ist ebenfalls eine untere Dreiecksmatrix mit Einsen auf der Diagonale. Die transformierten Schocks sind untereinander unkorreliert.
- Die orthogonale Transformation des i-ten Schocks verwendet nur die bereits transformierten Schocks mit kleinerem Index. Das Volatilitätsmodell für die i-te Residuenvarianz hängt nur von Größen ab, die zu diesen früheren transformierten Schocks gehören. Deshalb wird ein hochdimensionales Modell schrittweise aufgebaut, indem jede neue Reihe nur gegen die schon orthogonalisierten Schocks regressiert wird.
- Im angepassten bivariaten Cholesky-Modell ist b1t gleich a1t und b2t gleich a2t minus q21,t mal b1t. Die Erweiterung um Intel setzt b3t gleich a3t minus q31,t mal b1t minus q32,t mal b2t.
- Ein Nachteil der Transformation ist, dass das angepasste Modell von der Reihenfolge der Komponenten in at abhängen kann, weil die erste Komponente nicht transformiert wird. Theoretisch sollte diese Reihenfolge keinen Einfluss auf die Volatilität haben.
- Das Modell mit seriell korrelierten Fehlern ist yt = β0 + β1 x1t + … + βk xkt + zt mit zt = φ zt−1 + at; die Regressoren dürfen verzögerte yt enthalten.
- In Vektorform gilt yt = x′t β + zt für t = 1 bis n, mit θ = (β′, φ, σ²)′.
- Gibbs iteriert zwischen Regression und Zeitreihe: bei bekanntem φ wird die Regression yo,t = β′ xo,t + at mit yo,t = yt − φ yt−1 und xo,t = xt − φ xt−1 per kleinsten Quadraten geschätzt.
- Bei bekanntem β ist zt = yt − x′t β eine AR(1)-Reihe, deren Kleinste-Quadrate-Schätzung φ̂ = (Summe z²t−1) hoch −1 mal Summe zt−1 zt ist.
- Ein fehlender Wert xh eines AR(p) genügt p + 1 Gleichungen yh+j = φj xh + bh+j, j = 0 bis p, mit φ0 = 1, also einer einfachen linearen Regression mit p + 1 Punkten.
- Der Kleinste-Quadrate-Schätzer ist x̂h = (Summe φj yh+j) / (Summe φj²).
- Aufeinanderfolgende Fehlwerte können gemeinsam als multiple Regression oder einzeln innerhalb einer Gibbs-Iteration gezogen werden; gemeinsam ist vorzuziehen, besonders bei langen Lücken.
- Liegt h nahe am Rand, muss die Zahl der Regressionspunkte angepasst werden.
- Gegeben H wird die Mittelgleichung durch Division mit sqrt(ht) zur inhomogenen linearen Regression ro,t = x′o,t β + εt, mit ro,t = rt/sqrt(ht) und xo,t = xt/sqrt(ht).
- Bei normaler Prior von β mit Mittel βo und Kovarianz Ao ist die Posterior multivariat normal; A* hoch −1 = Summe xo,t x′o,t + Ao hoch −1 und β* = A* (Summe xo,t ro,t + Ao hoch −1 βo).
- Beginnt die Summe bei verzögerten Renditen erst bei p + 1, wenn rt−p die höchste verwendete Verzögerung ist.
- Die zwei Nachbargleichungen des fehlenden ln ht bilden eine einfache lineare Regression mit zwei Beobachtungen; der Kleinste-Quadrate-Schätzer ist normal mit Mittel ln ht und Varianz σ²v / (1 + α1²).
- Im bivariaten Modell ist a2t = q21,t a1t + b2t eine lineare Regression, deren Koeffizient und Residuum q21,t und b2t sind.
- β0 und β1 werden zeilenweise mit dem Ergebnis (12.22) gezogen.

## Voraussetzungen


## Anwendung im Trading

- Die technische Analyse ist derzeit vor allem auf die Schätzung aus historischen Daten beschränkt, weil Theorien der technischen Analyse gerade erst formuliert werden.
- Fosback entfernte mit einer Regression den störenden Einfluss der Kurzfristzinsen auf die Barreserven, als er Optimismus und Pessimismus von Fondsmanagern maß, und erhielt so den Fosback-Index als unverfälschtes Maß der Managerpsychologie.
- Jacobs und Levy nutzten multiple Regression, um die Störeinflüsse mehrerer Variablen zu mindern, und leiteten daraus bereinigte Indikatoren für die Prognose der relativen Aktienperformance ab.
- Alpha im Capital-Asset-Pricing-Modell ist der Achsenabschnitt aus der Regression der Strategierenditen auf die Renditen eines Marktindex.
- Kaufman vergleicht die Steigung der linearen Regression als Trendfolge-Methode mit Channel-Breakout, exponentieller Glättung, Swing-Breakout und Point-and-Figure. An Eurodollars von 1985 bis 1994 hatte Channel-Breakout die höchste risikobereinigte Performance.
- Das Arbitrage-Pricing-Modell sagt, ein lineares Modell verknüpfe die Rendite einer Aktie mit einer Reihe von Faktoren, und diese Beziehung entstehe, weil Arbitrageure nach risikolosen Gelegenheiten mit Investment null suchen.
- Der Indikator der Beziehung zweier Reihen ist die Zeitreihe der Residuen der linearen Beziehung zwischen ihnen.
- Der Operator YY normiert seine Werte mit dem Standardfehler der Regression und führte keinen expliziten Test auf die Stationarität der Residuen durch.
- Die absolute Renditeprognose des gleichgewichteten Faktormodells kann ungenau sein, die relative zwischen Aktien ist oft gut genug, sodass Long das obere Dezil und Short das untere Dezil oft eine positive Durchschnittsrendite liefert.

## Regeln und Kriterien

- Werden die Rollen von EWA und EWC vertauscht, ist die neue Hedge Ratio nicht der genaue Kehrwert der alten.
- Für das Johansen-Portfolio wird die Halbwertszeit mit derselben Regression bestimmt, nur dass yport an die Stelle von y tritt.
- Ein kurzes gleitendes Regressionsfenster ändert den Koeffizienten abrupt, wenn eine alte Beobachtung herausfällt und eine neue hinzukommt.
- Der exponentielle gleitende Durchschnitt gewichtet neue Daten stärker, aber es ist nicht klar, warum gerade ein exponentieller Abfall optimal ist.
- δ gleich 0 im Kalman-Filter reduziert die fortlaufende Schätzung auf OLS mit festem Offset und fester Steigung.
- Die Regressionskoeffizienten werden nur für die ersten 500 Tage der Daten nach August 2008 geschätzt.
- Vor der Regression werden die VX-Preise mit 1.000 und die ES-Preise mit 50 multipliziert, weil ein Punkt VX 1.000 Dollar und ein Punkt ES 50 Dollar bewegt.
- Eine lineare Regression auf der Mischung der Regime 2004 bis Mai 2008 und August 2008 bis 2012 wäre ein Fehler.
- Serielle Restkorrelation ist mit der Ljung-Box-Statistik zu prüfen und nicht nur mit Durbin-Watson, das allein Lag 1 sieht.
- Der Bau eines VAR umfasst drei Schritte: Ordnung über M(i) oder ein Informationskriterium, Schätzung per Kleinste Quadrate und gegebenenfalls Neuschätzung nach Streichen insignifikanter Parameter, dann Prüfung der Residuen mit Qk(m).

## Risiken und Grenzen

- Ohne geeignete Restriktionen ist die Likelihood eines VARMA(1,1) nicht eindeutig bestimmt. Das entspricht der exakten Multikollinearität in einer Regression: im Beispiel heben sich die freien Parameter ω und η zwischen AR- und MA-Teil auf, sobald r2t gleich a2t gilt.

## Beispiele

- Die Regression auf USD.CAD liefert eine Halbwertszeit von etwa 115 Tagen.
- Dieselbe Regression auf dem EWA-EWC-IGE-Portfolio des ersten Eigenvektors liefert eine Halbwertszeit von 23 Tagen.
- Für das Portfolio aus dem ersten Eigenvektor von EWA, EWC und IGE beträgt die so geschätzte Halbwertszeit 23 Tage, gegenüber etwa 115 Tagen bei USD.CAD.
- Der Lookback von 20 Handelstagen für GLD gegen USO ist mit Wissen im Nachhinein nahe am Optimum gewählt.
- Dieselbe Preis-Spread-Regression arbeitet im Beispiel deutlich besser als die Regression der Logpreise und als das einfache Verhältnis.
- Die Log-Future-Preise von CL gegen die Restlaufzeit fallen zu einem festen Zeitpunkt, hier die Kontrakte Januar bis Mai 2007 und nur die fünf nächsten, recht sauber auf eine Gerade; weiter entfernte Laufzeiten können von Gleichung 5.7 abweichen.
- Positive γ zeigen Backwardation, negative Contango; für CL sind die annualisierten γ vom 22. November 2004 bis 13. August 2012 geplottet.
- Haben von sieben Variablen mit den Werten +1 oder −1 fünf den Wert +1 und zwei den Wert −1, ist die lineare Kombination +3, also (+5) + (−2).
- Eine lineare Kombination dreier binärer Variablen kann nur vier verschiedene Werte annehmen, während drei binäre Variablen acht verschiedene Konfigurationen bilden.
- Greenblatts Magic Formula nutzt Kapitalrendite und Earnings Yield, kauft die 30 bestplatzierten Aktien und hält sie ein Jahr; die APR war 30,8 Prozent von 1988 bis 2004 gegen 12,4 Prozent des S&P 500.
- Beispiel 4.2 ist eine lineare Mean-Reversion zwischen einem ETF und seinen Bestandteilaktien, die Beispiele 4.3 und 4.4 sind zwei lineare Long-Short-Statistical-Arbitrage-Strategien auf Aktien.
- Das bedingt angepasste AR(3) der monatlichen einfachen Renditen des wertgewichteten Index lautet rt gleich 0,0091 plus 0,116 rt−1 minus 0,019 rt−2 minus 0,104 rt−3 plus Residuum, mit Residualstandardabweichung 0,054.
- Im S-Plus-AR(3) der monatlichen wertgewichteten Einfachrenditen betragen R² 0,0246 und das adjustierte R² 0,0216, bei einer Durbin-Watson-Statistik von 1,9913 und 989 Freiheitsgraden des Residualstandardfehlers.
- Die Januar-Regression der monatlichen Decile-1-Renditen lautet Rt gleich 0,0029 plus 0,1253 mal der Januar-Dummy plus Fehler, mit Standardfehlern 0,0033 und 0,0115.
- Im S&P-500-ADF mit Konstante und Zeittrend von Januar 1950 bis April 2008 beträgt R² 0,0081 und das adjustierte R² 0,0070, bei Durbin-Watson 1,9995 und Residualstandardfehler 0,008981 auf 14643 Freiheitsgraden.
- Für IBM am 21. November 1990 lautet die angepasste Gleichung ln(Δti) = 4,023 + 0,032 ln(Δti−1) − 0,025 Si−1 + 1,403 ϵi, mit Standardabweichungen 0,415, 0,073, 0,384 und 0,073; das Modell zeigt keine dynamische Abhängigkeit der Zeitdauer.
- Im transformierten Beispiel 8.3 lautet die Strukturgleichung r2t gleich 0,3 plus 0,5 mal r1t minus 0,7 mal r1,t minus 1 plus 0,95 mal r2,t minus 1 plus b2t.
- Nach Vertauschung der Reihenfolge lautet die andere Strukturgleichung r1t gleich minus 0,2 plus 1,0 mal r2t minus 0,8 mal r2,t minus 1 plus 0,8 mal r1,t minus 1 plus c2t.
- Die Bestimmtheitsmaße des VAR(1) sind 0,0101 für IBM und 0,0075 für den S&P 500, adjustiert 0,0081 und 0,0055.
- Für die täglichen Logschlusskurse von BHP und VALE lautet die einfache lineare Regression p1t = β0 + β1 p2t + wt mit dem Ergebnis p1t = 1,823 + 0,717 p2t + ŵt und σw = 0,044. Die Residualreihe dient der Prüfung, ob die Logpreise für Pairs Trading kointegriert sind.
- Die Kleinste-Quadrate-Regression der täglichen BHP-Logpreise auf die VALE-Logpreise vom 1. Juli 2002 bis zum 31. März 2006 schätzt den Intercept mit 1,822648, Standardfehler 0,003662, t-Wert 497,7, und die Steigung mit 0,716664, Standardfehler 0,002354, t-Wert 304,4.
- Der Residualstandardfehler dieser Regression beträgt 0,04421 bei 944 Freiheitsgraden. Das multiple und das adjustierte R² betragen jeweils 0,9899. Die F-Statistik ist 9,266 mal 10 hoch 4 auf 1 und 944 Freiheitsgraden, der p-Wert liegt unter 2,2 mal 10 hoch −16.
- Das feste Marktmodell rt = α + β rM,t + et, et ∼ N(0, σ²e), für 168 Monate wird mit gewöhnlichen kleinsten Quadraten geschätzt.
- OLS für General Motors gegen den S&P 500 liefert den Achsenabschnitt 0,1982 (Standardfehler 0,6302, t 0,3145, p 0,7535) und die Steigung 1,0457 (Standardfehler 0,1453, t 7,1962, p 0,0000).
- Die angepasste Gleichung ist rt = 0,20 + 1,0457 rM,t + et mit σ̂e = 8,13 und Residualstandardfehler 8,13 bei 166 Freiheitsgraden.
- R² beträgt 0,2378, das adjustierte R² 0,2332 und die Durbin-Watson-Statistik 2,0290.
- Jarque-Bera der Residuen ist 2,5348 (p 0,2816), Ljung-Box 24,2132 (p 0,3362); das Modell erscheint angemessen bei einem adjustierten R² von 23,3 Prozent.
- Als Zustandsraummodell geschätzt stimmen die Zustände 0,1982025 und 1,045702 sowie σ̂e = 8,130114 mit OLS überein.
- Für die wöchentlichen Änderungen der dreijährigen und einjährigen US-Treasury Constant-Maturity-Zinsen, 5. Januar 1962 bis 10. April 2009, lautet die klassische Schätzung c3t = 0,782 c1t + zt mit zt = 0,183 zt−1 − 0,036 zt−2 + at und σ̂a = 0,068.
- Die Standardfehler dieser drei Koeffizienten sind 0,0075, 0,0201 und 0,0201; der Stichprobenumfang ist 2466.
- Die Gibbs-Posteriormittel aus den letzten 2000 von 2100 Iterationen sind β = 0,793, φ1 = 0,184, φ2 = −0,036 und σ² = 0,00479, mit Standardfehlern 0,008, 0,019, 0,021 und 0,00013.
- Die Startwerte stammen aus einem zweistufigen OLS, erst die Regression, dann ein AR(2) auf den Residuen; bei n = 2466 liegen sie nahe an Gleichung (12.12), und andere Startwerte liefern ähnliche Ergebnisse.
- Für das AR(3) der 600 wöchentlichen Dreijahresänderungen vom 18. März 1988 bis 10. September 1999 gibt der Text c3t = 0,227 c3,t−1 + 0,006 c3,t−2 + 0,114 c3,t−2 + at mit σ̂² = 0,0128 und Standardfehlern 0,041, 0,042 und 0,041.
- Gibbs mit 1050 Iterationen und 50 Burn-in liefert 0,252, 0,003 und 0,110 sowie σ̂² = 0,0118, mit posterioren Standardabweichungen 0,046, 0,045, 0,046 und 0,0008.
- Das Gauß-GARCH(1,1) hat die Mittelgleichung rt = 0,552 + at; das SV-Modell derselben Reihe hat rt = µ + at mit Posteriormittel µ = 0,409 und Standardfehler 0,157.
- BEKK(1,1) schätzt β̂0 = (0,70, 0,54)′; die Mittelgleichungen von GARCH, BEKK und SV sind im Wesentlichen identisch.
- Die bivariaten SV-Posteriormittel sind β01 = 0,53 (Standardfehler 0,26) und β02 = 0,51 (Standardfehler 0,17).

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 39–58 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-003-p039-p058|S. 39–58]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 96–115 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-006-p096-p115|S. 96–115]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 210–229 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-012-p210-p229|S. 210–229]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 419–438 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-023-p419-p438|S. 419–438]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 457–476 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-025-p457-p476|S. 457–476]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 14–33 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-002-p014-p033|S. 14–33]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 52–71 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-004-p052-p071|S. 52–71]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 71–75 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-005-p071-p075|S. 71–75]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 76–95 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-006-p076-p095|S. 76–95]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 119–138 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-009-p119-p138|S. 119–138]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 138–143 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-010-p138-p143|S. 138–143]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 58–77 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-004-p058-p077|S. 58–77]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 77–96 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-005-p077-p096|S. 77–96]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 96–115 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-006-p096-p115|S. 96–115]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 115–134 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-007-p115-p134|S. 115–134]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 134–153 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-008-p134-p153|S. 134–153]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 210–229 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-012-p210-p229|S. 210–229]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 229–248 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-013-p229-p248|S. 229–248]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 267–286 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-015-p267-p286|S. 267–286]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 286–305 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-016-p286-p305|S. 286–305]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 362–381 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-020-p362-p381|S. 362–381]]
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
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 153–172 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-009-p153-p172|S. 153–172]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 210–229 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-012-p210-p229|S. 210–229]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 286–305 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-016-p286-p305|S. 286–305]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 533–552 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-029-p533-p552|S. 533–552]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 590–609 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-032-p590-p609|S. 590–609]]

## Verwandte Themen
