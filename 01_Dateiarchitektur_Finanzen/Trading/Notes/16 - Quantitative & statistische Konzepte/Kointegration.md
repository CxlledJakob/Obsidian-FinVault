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

# Kointegration


## Kurzdefinition

- Kointegration ist im Engle-Granger-Sinn der Kunstgriff, der eine Regression auf nichtstationären Reihen ermöglicht und dabei das Gedächtnis erhält.
- Kointegration ist der Kunstgriff, der eine Regression auf nichtstationären Reihen ermöglicht, sodass das Gedächtnis erhalten bleibt.
- Preisreihen heißen kointegrierend, wenn sich eine stationäre lineare Kombination mehrerer nichtstationärer Preisreihen finden lässt, also ein Portfolio, dessen Marktwert mean-reverting ist.
- Die häufigste Kombination sind zwei Reihen: ein Asset long und ein anderes gleichzeitig short, mit passender Kapitalzuteilung; das ist Pairs Trading, und der Begriff trägt auch drei oder mehr Assets.
- Lassen sich zwei oder mehr nichtstationäre Preisreihen zu einem stationären Portfolio verbinden, heißen diese Reihen kointegrierend.
- Kointegration lässt sich mit dem CADF-Test oder mit dem Johansen-Test messen.
- Für eine k-dimensionale einheitswurzel-nichtstationäre Reihe mit h Einheitswurzeln im System liegt Kointegration vor, wenn 0 kleiner als h kleiner als k ist. Die Zahl der Kointegrationsfaktoren ist k minus h.
- Die Zahl der Kointegrationsfaktoren ist die Zahl verschiedener Linearkombinationen, die einheitswurzelstationär sind. Diese Linearkombinationen heißen Kointegrationsvektoren.
- Zwei Reihen sind kointegriert, wenn beide einheitswurzel-nichtstationär sind und es eine Linearkombination gibt, die einheitswurzelstationär ist.
- Zwei Reihen sind kointegriert, wenn beide Unit-Root-nichtstationär sind und eine Linearkombination Unit-Root-stationär ist. Im simulierten System ist y2t = 0,5 x1t + x2t frei von der Unit Root, der Kointegrationsvektor ist (0,5, 1)′, und y1t ist der gemeinsame Trend, der die Unit Roots beider Komponenten erzeugt.
- In einer k-dimensionalen Unit-Root-nichtstationären Reihe mit h Unit Roots im System liegt Kointegration vor, wenn 0 < h < k gilt. Die Zahl der Kointegrationsfaktoren ist k − h und zugleich die Zahl verschiedener Unit-Root-stationärer Linearkombinationen; diese Kombinationen heißen Kointegrationsvektoren.

## Kernaussagen

- Kointegrationsverfahren sind unter anderem deshalb wichtig, weil sie Reihen mit Gedächtnis modellieren können.
- Der Text fragt, warum gerade die Null-Differenzierung die besten Ergebnisse liefern sollte, und hält sie für ebenso willkürlich wie die Differenzierung um einen Schritt.
- Zwischen keiner Differenzierung und voller Differenzierung liegt ein weiter Bereich, der sich mit fraktionaler Differenzierung für ein prognosestarkes Modell erkunden lässt.
- Log-Preise haben in diesem Paradigma Gedächtnis und sind nicht stationär.
- Für ML-Prognosen hält der Text den Kointegrations-Kunstgriff für unnötig, weil die Fixed-Width-Fracdiff-Methode Stationarität erreicht, ohne das Gedächtnis aufzugeben.
- Im Engle-Granger-Paradigma haben Log-Preise Gedächtnis und sind nicht stationär.
- Die Fixed-Width-Fracdiff-Methode braucht diesen Kunstgriff für ML-Prognosen nicht, weil Stationarität möglich ist, ohne Gedächtnis und Prognosekraft aufzugeben.
- Zur Erkennung der Kointegration eines Portfolios von Instrumenten dienen der kointegrierte Augmented-Dickey-Fuller-Test, CADF, und der Johansen-Test.
- Über die mechanische Anwendung dieser statistischen Tests hinaus soll intuitiv klar werden, was sie wirklich prüfen, samt der einfachen mathematischen Gleichungen dahinter.
- Es wird gezeigt, ob Rohpreise, Log-Preise oder Verhältnisse als Eingaben für diese Tests und Strategien am sinnvollsten sind.
- Mean-Reversion-Strategien sind oft leicht zu bauen, weil man nicht auf von sich aus stationäre Instrumente beschränkt ist und aus vielen kointegrierenden Aktien und ETFs wählen kann.
- Neue ETFs, die sich von bestehenden nur am Rand unterscheiden, vergrößern diese Auswahl jedes Jahr.
- Hinter einem kointegrierenden Paar steht oft eine fundamentale Geschichte, und auch wenn das Paar auseinanderfällt, ist der Grund häufig noch verständlich.
- Echte Stationarität oder Kointegration ist für eine erfolgreiche Mean-Reversion-Strategie nicht notwendig, wenn kurzfristige oder saisonale Rückkehr mitgenommen und die Position vor dem nächsten Gleichgewicht geschlossen wird.
- Umgekehrt trägt nicht jede stationäre oder kointegrierte Reihe, wenn die Halbwertszeit zehn Jahre beträgt.
- Der Spread y gleich h1 y1 plus weitere Glieder ist per Konstruktion stationär, wenn die hi aus Regression oder Johansen-Eigenvektoren stammen, und hi ist dann die Stückzahl.
- Kointegrieren die Logpreise, beschreiben die hi Kapitalgewichte eines Portfolios mit impliziter Kasse, und der Marktwert dieser Konstruktion ist stationär, aber nicht konstant.
- Theoretisch sollten Aktienpaare eines Sektors wegen gemeinsamer ökonomischer Faktoren kointegrieren; praktisch erfüllen tägliche Einzelaktien fast nie die Stationaritätsdefinition aus Kapitel 2, und auch sinnvolle Paare kointegrieren selten out of sample.
- Kointegrierende Aktienpaare lassen sich in einem gewählten Zeitraum leicht finden und verlieren die Kointegration in der folgenden Out-of-Sample-Periode ebenso leicht, weil sich die Lage einer Firma durch Management und Wettbewerb schnell ändert; dieselbe Branche garantiert nicht dasselbe Schicksal, Beispiel AAPL gegen BBRY.
- Einmal als kointegrierend gefundene ETF-Paare fallen out of sample seltener auseinander, weil sich die Fundamentaldaten eines Aktienkorbs viel langsamer ändern als die einer einzelnen Firma.
- Die statistischen Tests der Zeitreihen-Mean-Reversion sind für querschnittliche Mean Reversion weitgehend irrelevant.
- Ein gleichgewichtetes Long-only-Portfolio muss erneut gegen den ETF getestet werden: gleiche Kapitalgewichte erzeugen nicht automatisch eine Preisreihe, die mit SPY kointegriert, selbst wenn jede Einzelaktie mit SPY kointegriert.
- Die meisten Währungs- oder Future-Paare kointegrieren nicht, und die meisten Portfolios aus Währungen oder Futures zeigen keine querschnittliche Mean Reversion.
- Weil EWA und EWC kointegrieren, wäre zu erwarten, dass AUD mit CAD kointegriert; weil Australien und Südafrika große Mineneinnahmen haben, wäre außerdem Kointegration von AUD mit ZAR zu erwarten, und Händler nennen diese Währungen samt der norwegischen Krone Rohstoffwährungen.
- Ein ETF von Rohstoffproduzenten wie XLE kointegriert gewöhnlich mit dem Spot dieser Ware, wegen der Roll-Rendite aber nicht notwendig mit dem Future-Preis dieser Ware.
- Rohstoffwährungen als Gruppe bieten viele Gelegenheiten zur Kointegration.
- Ein Johansen-Test auf einer Mischung der beiden ES-VX-Regime wäre ein Fehler; der Text beschränkt sich auf das zweite Regime, das bis zum Zeitpunkt des Schreibens reicht.
- Bevor ein Johansen-Test auf den vier Kontrakten CL, BZ, RB und HO läuft, wird zuerst der Crack Spread geprüft, dessen ADF vom 20. Mai 2002 bis zum 4. Mai 2012 keine Mean Reversion zeigt.
- ETFs mit Rohstoffproduzenten kointegrieren oft mit dem Spotpreis dieser Rohstoffe, weil die Rohstoffe einen wesentlichen Teil ihrer Assets ausmachen, und dienen deshalb als Proxy des Spotpreises, um die Rollrendite zu extrahieren.
- Die Kointegration zwischen VX und ES wurde in Kapitel 5 für eine profitable Mean-Reversion-Strategie verwendet; hier wird daraus keine Mean-Reversion-, sondern eine Momentum-Strategie gebaut.
- Neben der mechanischen Anwendung von CADF- und Johansen-Test auf ein Portfolio wird ein intuitives Verständnis angestrebt, was diese Tests wirklich prüfen, samt der einfachen mathematischen Gleichungen dahinter.
- An öffentlichen Börsen gehandelte einzelne Preisreihen sind selten stationär. Stationäre Portfolios lassen sich herstellen, indem zwei oder mehr nicht mean-revertierende Reihen linear kombiniert werden.
- Der CADF-Test eignet sich nur für ein Paar, der Johansen-Test für beliebig viele Reihen.
- Kointegration bedeutet nicht, dass jede Linearkombination stationär ist. Die Hedge Ratios müssen erst bestimmt werden.
- Die CADF-Hedge-Ratio hängt von der Reihenfolge ab und ist nicht der genaue Kehrwert der vertauschten Regression. Oft ist nur eine Ordnung stationär; gewählt wird die negativste t-Statistik. Für EWA und EWC findet Johansen dagegen zwei Beziehungen.
- EWA und EWC werden geprüft, weil die kanadische und die australische Wirtschaft rohstoffbasiert sind. Das Streudiagramm fällt auf eine Gerade, und das Residuum EWC minus Hedge-Ratio mal EWA sieht stationär aus. CADF verwirft die Null auf 95 Prozent, etwa minus 3,64 gegen minus 3,359.
- Zwei kointegrierende Beziehungen bei nur zwei Reihen sind möglich, weil die beiden Hedge Ratios nicht notwendig Kehrwerte sind und zwei unabhängige stationäre Portfolios bilden. Johansen ist reihenfolgeunabhängig und liefert alle Beziehungen in einem Lauf.
- Mit IGE, einem ETF aus Rohstoffaktien, schließt der Text auf drei Beziehungen mit 95 Prozent Sicherheit. Die Eigenwerte sind 0,0112, 0,0087 und 0,0030. Der erste Eigenvektor minus 1,0460, 0,7600, 0,2233 hat die kürzeste Halbwertszeit, 23 Tage gegen etwa 115 Tage bei USD.CAD.
- ETFs sind ein ergiebiges Feld für kointegrierende Reihen und damit für Pair Trading. yport, der Nettomarktwert, ist die Summe aus Eigenvektor-Stückzahl mal Preis über alle ETFs und tritt an die Stelle der Einzelreihe in der Halbwertszeitregression.
- Der Johansen-Eigenvektor mit dem größten Eigenwert ist derjenige mit der kürzesten Halbwertszeit und wird als Hedge-Ratio-Vektor des stationären Portfolios benutzt.
- GLD und USO sind nicht kointegriert, obwohl die Vermutung lautet, steigendes Öl hebe über die Inflation auch Gold. Der Unterschied zwischen Kassaöl und den Futures, aus denen USO besteht, wird hier übergangen und in Kapitel 5 nachgeholt. Kurzfristige Mean Reversion kann trotzdem handelbar sein.
- Echte Kointegration ist ein Ideal, das wenige reale Preisreihen erreichen. Für ein wirklich kointegrierendes Paar genügen OLS oder Johansen auf langer Historie; sonst wird die Hedge Ratio dynamisch nachgeführt.
- Logpreis-Kointegration bedeutet, dass eine Linearkombination der Logpreise stationär ist. Ihre ersten Differenzen sind näherungsweise die Renditen eines Portfolios mit konstanten Kapitalgewichten, inklusive einer impliziten Kasse.
- Die Preisratio ist nur stationär, wenn die Hedge Ratios gleichen Betrag haben. Sind Preise und Logpreise kointegrierend, lassen sich beide Spreads theoretisch rechtfertigen; der Preisspread ist einfacher, weil er kein ständiges Rebalancing verlangt.
- EWA und EWC mit dynamischem Kalman-β erreichen eine APR von 26,2 Prozent und eine Sharpe Ratio von 2,4.
- Tägliche Preise einzelner Aktien erfüllen die Stationaritätsdefinition aus Kapitel 2 fast nie. Ein geometrischer Random Walk beschreibt sie: einmal weggelaufen, kehren sie selten zum Start zurück. Intraday- und saisonale Mean Reversion sind spätere Sonderfälle.
- Selbst Paare wie Exxon gegen Chevron oder Citibank gegen Bank of America kointegrieren out of sample selten. In einem gewählten Fenster findet man kointegrierende Paare leicht, im folgenden Fenster verlieren sie die Kointegration ebenso leicht.
- Das Schicksal einer Firma ändert sich durch Management und Wettbewerb schnell. Dieselbe Branche garantiert nicht dasselbe Schicksal, Beispiel AAPL gegen BBRY.
- EWA und EWC, genannt 2009, kointegrierten im November 2012 noch, weil sich die Fundamentaldaten eines Aktienkorbs langsamer ändern als die einer Firma. Mit mehr ETFs auf nahezu denselben Sektor nehmen die Paar-Gelegenheiten zu.
- GLD gegen GDX kointegriert im Johansen-Test vom 23. Mai 2006 bis 14. Juli 2008 mit 99 Prozent und verliert die Kointegration vom 15. Juli 2008 bis 9. April 2012.
- Am 14. Juli 2008 erreichte WTI etwa 145 Dollar je Barrel. Teures Öl verteuert die Goldförderung, die Gewinne der Minen sinken, und ihre Aktien bleiben hinter dem Goldpreis zurück.
- Mit dem Ölfonds USO kointegriert das Triplett über 2006 bis 2012. Der Johansen-Test zeigt mit 99 Prozent genau eine kointegrierende Beziehung.
- USO hält kein Öl, sondern Oil-Futures. Selbst wenn XLE mit dem Spot kointegriert, muss es das nicht mit USO. Das gilt für jeden Rohstoff-Futures-Fonds gegen einen Produzentenfonds.
- Im Trainingsjahr 2007 kointegrieren 98 S&P-500-Aktien im Johansen-Test einzeln mit mindestens 90 Prozent mit SPY.
- Das gleichgewichtete Long-only-Portfolio muss erneut gegen SPY getestet werden, weil gleiche Kapitalgewichte die Kointegration nicht garantieren, selbst wenn jede Aktie einzeln mit SPY kointegriert. Auf Log-Preisen liegt die Wahrscheinlichkeit über 95 Prozent.
- Die Trace-Statistik für höchstens null kointegrierende Relationen ist 15,869, über dem 95-Prozent-Wert 15,494 und unter dem 99-Prozent-Wert 19,935. Die Eigenwert-Statistik 9,671 bleibt unter dem 90-Prozent-Wert 12,297.
- Die Johansen-Implementierung, die der Autor kennt, nimmt höchstens 12 Symbole (LeSage, 1998).
- Die meisten Währungs- oder Future-Paare kointegrieren nicht, und die meisten Portfolios daraus zeigen keine querschnittliche Mean Reversion. Gelegenheiten bleiben begrenzt, sind aber nicht verschwunden, etwa bei Future-Kalenderspreads.
- Für den Test müssen die Reihen so aufbereitet sein, dass ein Punkt in beiden Instrumenten denselben Dollarwert hat. AUD gegen CAD wird deshalb als AUD.USD gegen CAD.USD getestet.
- Währungen mit ähnlichen Fundamentaldaten sind die Kandidaten, analog zu Länder-ETFs. Weil Australien und Südafrika große Mineneinnahmen haben, ist neben AUD gegen CAD auch AUD gegen ZAR ein Kandidat. Der Markt nennt solche Währungen, darunter die norwegische Krone, Rohstoffwährungen.
- Kalenderspreads mean-reverten im Allgemeinen nicht, obwohl beide Beine denselben Basiswert abbilden, weil die Rollrendite das Signal vom Spot abkoppelt.
- Der 12-Monats-Log-Kalenderspread von CL ist im ADF-Test mit 99 Prozent stationär, bei einer Halbwertszeit von etwa 36 Tagen.
- Gleichung F(t, T) = S(t) mal exp(γ(t − T)) gilt nur für einen Future, dessen Basiswert gehandelt wird. VIX ist keiner, die Log-Preise von VX gegen die Restlaufzeit liegen nicht auf einer Geraden, und die Formeln von Dupoyet, Daigler und Chen (2011) erklären die Mean Reversion der VX-Kalenderspreads nicht.
- Für einzelne Märkte mean-reverten nur Kalenderspreads bestimmter Monate und bestimmter Abstände. Diesen Details geht der Text nicht nach.
- Eine Produzenten-ETF kointegriert oft mit dem Spot und wegen der Rollrendite nicht mit dem Future.
- Mean-revertierende Intermarket-Futures-Spreads, also Paare von Futures verschiedener Basiswerte, sind schwer zu finden.
- Der naheliegende Kandidat vor einem Johansen-Test ist der Energiekomplex aus CL, BZ, RB und HO an der NYMEX.
- Eine lineare Regression oder ein Johansen-Test auf der Mischung der Regime 2004 bis Mai 2008 und August 2008 bis 2012 wäre ein Fehler.
- Ein Portfolio long 0,3906 Kontrakte VX und long einen Kontrakt ES soll stationär sein.
- Findet sich ein Instrument, etwa ein ETF oder ein anderer Future, das mit dem Spotpreis oder der Spotrendite eines Rohstoffs kointegriert oder korreliert, lässt sich die Rollrendite des Rohstoff-Futures extrahieren, indem dieses Instrument in Backwardation geshortet und in Contango gekauft wird.
- Das ETF-Paar GLD gegen GDX hörte 2008 auf zu kointegrieren.
- Die dazu gebildete Hypothese betraf den hohen Rohölpreis; nachdem der Ölpreis als Eingabe ergänzt wurde, funktionierte das Kointegrationsmodell wieder.
- Dieser Vorgang, einen fundamentalen Grund zu suchen und quantitativ zu prüfen, wird dem blinden Ergänzen weiterer Regeln vorgezogen, wenn eine Strategie den Backtest underperformt.
- Unterstellt man für die wöchentliche einjährige und die dreijährige Treasury-Constant-Maturity-Rendite je eine Einheitswurzel, dann zeigen die Residuen der Niveauregression, dass die beiden Zinsen nicht kointegriert sind.
- Die Daten stützen damit nicht die Hypothese eines langfristigen Gleichgewichts zwischen diesen beiden Zinssätzen.
- Die naive Regression lautet r3t gleich 0,832 plus 0,930 mal r1t plus et, mit residualer Standardabweichung 0,523, einem Bestimmtheitsmaß von 96,5 Prozent und Standardfehlern 0,024 und 0,004.
- Die Stichproben-Autokorrelation dieser Residuen ist hoch signifikant, fällt langsam und zeigt das Muster einer einheitswurzel-nichtstationären Reihe.
- Eine invertierte Zinsstruktur, also Zinssätze, die umgekehrt zur Restlaufzeit verlaufen, kam im Stichprobenzeitraum tatsächlich vor.
- Die Reihen haben 2467 Wochenbeobachtungen vom 5. Januar 1962 bis 10. April 2009, gemessen in Prozent, von der Federal Reserve Bank of St. Louis.
- Im Beispiel (8.31) sind beide Komponenten einheitswurzel-nichtstationär, das System hat aber nur eine Einheitswurzel. Die Einheitswurzeln von x1t und x2t werden durch die Einheitswurzel des gemeinsamen Trends y1t eingeführt.
- Die Linearkombination y2t gleich 0,5 mal x1t plus x2t hat keine Einheitswurzel. Der Kointegrationsvektor ist (0,5; 1)′.
- Nach der Transformation mit L gleich [[1, minus 2], [0,5, 1]] sind y1t und y2t entkoppelt. y1t folgt einem ARIMA(0,1,1), y2t ist weißes Rauschen. Die gleichzeitige Korrelation von y1t und y2t ist die der transformierten Schocks.
- Die Eigenwerte der AR-Koeffizientenmatrix in (8.31) sind 0 und 1; das Modell ist nicht schwach stationär. Die Kovarianzmatrix der Schocks ist positiv definit.

## Funktionsweise

- Die Hedge Ratio eines Assets ist die Zahl der Einheiten, die im Portfolio long oder short gehalten werden; bei einer Aktie sind das Stücke, und eine negative Hedge Ratio bedeutet eine Short-Position.
- Kointegration bedeutet nicht, dass eine beliebige Linearkombination ein stationäres Portfolio ergibt.
- Engle und Granger (1987) bestimmen die optimale Hedge Ratio durch eine lineare Regression zweier Preisreihen, bilden damit das Portfolio und testen dann dessen Stationarität; die Funktion cadf führt diese Schritte aus.
- Der CADF-Test gilt nur für ein Paar, der Johansen-Test für beliebig viele Reihen.
- Im Johansen-Test ist der Rang r von Λ die Zahl der unabhängigen Portfolios aus Linearkombinationen der kointegrierenden Reihen; die Eigenvektoren dienen als Hedge Ratios.
- Der Johansen-Test hängt nicht von der Reihenfolge der Preisreihen ab und liefert in einem Lauf alle unabhängigen kointegrierenden Beziehungen.
- Zwei kointegrierende Beziehungen bei nur zwei Reihen sind zwei verschiedene Hedge Ratios, die nicht notwendig Kehrwerte voneinander sind, und damit zwei unabhängige stationäre Portfolios.
- Die Eigenvektoren sind nach absteigenden Eigenwerten geordnet; der erste, zum größten Eigenwert, ist der stärkste und hat die kürzeste Halbwertszeit.
- Die Eigenvektoren des Johansen-Tests dienen als Hedge Ratios, und der Eigenvektor mit dem größten Eigenwert hat die kürzeste Halbwertszeit.
- Der Nettomarktwert des Portfolios ist Stückzahl mal Kurs, über die ETFs summiert, und tritt an die Stelle der Einzelreihe in der Halbwertszeit-Regression.
- Das Problem des kanalnormierten Divergenzindikators bei negativ korrelierten Reihen ließe sich mit einer Formulierung auf Basis der Kointegration vermeiden, die Engle und Granger 1987 vorschlugen.
- Dieses Verfahren nutzt eine Regressionsanalyse, um festzustellen, ob zwischen zwei Zeitreihen eine lineare Beziehung besteht.
- Es verkraftet auch Paare, die stark negativ korreliert und damit 180 Grad außer Phase sind, und löst so das Problem falscher Gleichlaufanzeigen bei einem Indikatorwert von null.
- Zuerst wird statistisch geprüft, ob die beiden Reihen verbundene Trends haben; sind sie kointegriert, fällt ein stationärer Divergenzindikator aus der Analyse.
- Dieser Indikator heißt Error-Correction-Modell und misst, wie weit eine Reihe von der typischen linearen Beziehung der beiden Reihen abgewichen ist.
- In den meisten Anwendungen soll die Divergenz zum gemeinsamen Trend zurückkehren, wenn das Error-Correction-Modell extrem positiv oder extrem negativ wird; der Fehler soll auf seinen normalen Wert null zurückkorrigieren.
- Der Indikator einer solchen Beziehung ist eine Zeitreihe der Fehler, also der Residuen, der linearen Beziehung zwischen den zwei Reihen.
- Ein Testtyp, mit dem festgestellt wird, dass eine Zeitreihe stationär ist, ist der Unit-Root-Test, beschrieben bei Alexander, Market Models, Seiten 324–328 und 353–361.
- Einzelnes Differenzieren jeder Komponente eines kointegrierten Systems überdifferenziert und legt Unit Roots in das MA-Matrixpolynom, sodass die vektorielle Reihe nichtinvertierbar wird. Die Fehlerkorrekturdarstellung von Engle und Granger (1987) umgeht die Schätzung nichtinvertierbarer VARMA-Modelle.
- Für ein kointegriertes VARMA(p, q) mit m Kointegrationsfaktoren und m < k ist die Fehlerkorrektur Δxt = αβ′ xt−1 plus Summe der Γ∗i Δxt−i plus at minus die MA-Summe. α und β sind k×m-Matrizen vollen Rangs, β′xt ist Unit-Root-stationär, und die Spalten von β sind die Kointegrationsvektoren. Es gilt αβ′ = −Φ(1) = Φp + … + Φ1 − I.
- β′xt−1 kompensiert die überdifferenzierte Reihe. Weil die Stichprobenkorrelation einer Unit-Root-nichtstationären mit einer stationären Reihe gegen null geht, kann Δxt nur über diese stationäre Kombination sinnvoll an xt−1 hängen.
- Ist der Rang von Π = αβ′ = −Φ(1) gleich 0, gibt es keine Kointegration und Δxt folgt einem VAR(p−1) mit deterministischem Trend μt. Rang k bedeutet, xt ist I(0) und enthält keine Unit Root; die Fehlerkorrektur ist dann uninformativ. Bei 0 < Rang m < k gibt es m linear unabhängige Kointegrationsvektoren wt = β′xt und k−m gemeinsame stochastische Trends.
- Ein orthogonales Komplement α⊥, also eine k×(k−m)-Matrix mit α′⊥ α = 0, liefert über yt = α′⊥ xt eine Darstellung der k−m gemeinsamen Trends; in der resultierenden Gleichung fehlt der Fehlerkorrekturterm. Im bivariaten Beispiel ist α = (−1, −0,5)′ und α⊥ = (1, −2)′, also yt = x1t − 2 x2t.
- Die Zerlegung Π = αβ′ ist nicht eindeutig, weil jede orthogonale m×m-Matrix die Faktoren dreht. Zur Identifikation wird β′ = [Im, β′1] verlangt, nötigenfalls nach Umsortierung, sodass die ersten m Komponenten eine Unit Root haben. Im bivariaten VAR(1) mit einem Kointegrationsvektor muss |1 + α1 + α2 β1| < 1 gelten, damit wt ein stationärer AR(1) ist.
- Der Rang von Π ist die Zahl der Kointegrationsvektoren. Johansen (1988, 1995) und Reinsel und Ahn (1992) prüfen die Kointegration über diesen Rang. Ist m vorgegeben, lässt sich die Fehlerkorrektur mit Likelihood-Methoden schätzen; αβ′ xt−v darf für jedes v zwischen 1 und p stehen, bei entsprechender Anpassung der AR-Matrizen.

## Voraussetzungen

- Der Johansen-Eigenvektor ist nur dann als Kapitalgewicht lesbar, wenn beide Preisreihen dieselbe Quotierungswährung haben; sonst haben Punktbewegungen nicht denselben Wert, und der Test ist bedeutungslos.
- Deshalb läuft der Test auf AUD.USD und CAD.USD und nicht auf USD.AUD gegen USD.CAD.
- Die Darstellung nimmt Unit Roots der Vielfachheit 1 an; der Begriff lässt sich auf abweichende Vielfachheiten erweitern. Für den VAR(p) wird höchstens I(1) angenommen, die Innovation gaußsch, und μt = μ0 + μ1 t.
- Bei μt = 0 sind alle Komponenten I(1) ohne Drift und wt hat Mittel null. Bei restricted constant μt = α c0 bleiben die Komponenten I(1) ohne Drift, wt hat Mittel −c0. Bei freiem μ0 sind die Komponenten I(1) mit Drift, und wt kann einen von null verschiedenen Mittelwert haben. Bei restricted trend μt = μ0 + α c1 t haben die Komponenten Drift und wt einen linearen Trend in c1 t. Bei unrestringiertem μ0 + μ1 t haben die Komponenten einen quadratischen Zeittrend und wt einen linearen Trend; dieser letzte Fall ist empirisch unüblich. Der erste Fall ist für ökonomische Reihen ungewöhnlich, kann aber Logpreisreihen mancher Assets treffen; der dritte Fall ist für Assetpreise ebenfalls brauchbar.

## Anwendung im Trading

- Findet sich ein Instrument, etwa ein ETF oder ein anderer Future, das mit dem Spotpreis oder der Spot-Rendite eines Rohstoffs kointegriert oder korreliert, lässt sich die Rollrendite des Rohstoff-Futures extrahieren, indem dieses Instrument bei Backwardation geshortet und bei Contango gekauft wird.
- Aus Gründen der Einfachheit wurde die Kointegration für die Divergenzindikatoren der Fallstudie nicht verwendet.
- Es wurde angenommen, eine nicht mit dem S&P 500 verbundene Begleitreihe zeige sich an der schlechten finanziellen Leistung der Divergenzregel.
- Der Autor hält die Kointegrationsmethodik für weiter untersuchenswert bei der Entwicklung von Indikatoren.
- Als mögliche Verbesserung der Indikatorspezifikation nennt der Text, Divergenzen könnten besser mit Indikatoren auf Basis der Kointegration gemessen werden; das Wort steht dort als conintegration.
- Diese Anregung steht neben dem Vorschlag, Extremindikatoren mit der von Ehlers diskutierten Fisher-Transformation zu untersuchen.

## Regeln und Kriterien

- Im CADF-Test ist die Hedge Ratio nicht der genaue Kehrwert, wenn abhängige und unabhängige Variable getauscht werden; oft ist nur eine der beiden Ordnungen stationär, und man nimmt die Ordnung mit der negativsten t-Statistik.
- Für EWA und EWC gilt diese Ein-Ordnungs-Einschränkung nicht, was der Johansen-Test später bestätigt.
- Für den Johansen-Test wird p gleich 0 gesetzt, also ein konstanter Offset M ungleich 0, aber kein konstanter Drift, und die Lag-Zahl k gleich 1; ein konstanter Drift im Preis eines stationären Portfolios gilt als unpraktisch.
- Der Nettomarktwert yport ist die über alle ETFs summierte Stückzahl mal dem jeweiligen Kurs.
- Preis-Spreads sind einfacher als Log-Preis-Spreads; beide sind theoretisch gerechtfertigt, wenn sowohl Preise als auch Logpreise kointegrieren.
- Das Verhältnis y1/y2 ist nur stationär, wenn die Hedge Ratios betragsgleich sind; das ist ein Sonderfall und nicht die normale Erwartung.
- Für ein wirklich kointegrierendes Paar genügen möglichst lange Historie und eine einmalige OLS- oder Johansen-Schätzung.
- Für Paare, die nicht wirklich kointegrieren, braucht der Spread oft eine dynamische Hedge Ratio; das Verhältnis als Signal erspart das.
- Für ein mean-revertierendes Portfolio mit fester Stückzahl je Bestandteil während des Trades kommen die Hedge Ratios aus den Preisreihen, für feste Marktwerte je Bestandteil aus den Log-Preisreihen.
- Der hier beschriebene Kalman-Filter sucht nicht die Hedge Ratio zweier kointegrierender Preisreihen, sondern Mittel und Streuung einer einzelnen mean-revertierenden Reihe.

## Risiken und Grenzen

- Die Zahl kointegrierter Variablen ist begrenzt, und die kointegrierenden Vektoren sind notorisch instabil.
- Der Handel von USD.NOK und USD.MXN erzeugt P&L in NOK und in MXN, der direkte Handel von MXN.NOK nur P&L in NOK; die beiden Wege sind nicht identisch.
- Log-Preis-Kointegration hält den Marktwert nur stationär, wenn fortlaufend rebalanciert und dabei Gewinn oder Verlust in die Kasse gebucht wird.
- Die dem Autor bekannte Johansen-Implementierung akzeptiert höchstens 12 Symbole (LeSage, 1998).
- Mean-Reversion-Handel eines Commodity-Fonds gegen den Produzentenfonds wäre weniger riskant, wenn der Fonds die physische Ware hält und nicht die Futures.
- Die Schwierigkeit liegt in der richtigen Aufbereitung der Reihen für den Kointegrationstest und in der richtigen Renditeformel.
- Dass ein Produzenten-ETF mit dem Spot kointegrieren und mit dem Future trotzdem auseinanderlaufen kann, kostete den Autor mehr als 100.000 Dollar und ruinierte 2006.
- Überdifferenzierung kann auftreten, wenn einzelne Komponenten eines kointegrierten Systems differenziert werden. Die exakte Maximum-Likelihood-Methode wird wichtig, wenn man Overdifferencing vermutet.
- Für Kointegration und Kointegrationstests verweist der Text auf Box und Tiao (1977), Engle und Granger (1987), Stock und Watson (1988) sowie Johansen (1988).
- Das Testen auf Kointegration bereitet Schwierigkeiten.
- Kointegrationstests übersehen die Skalierungseffekte der Komponentenreihen; der Autor verweist auf Cochrane (1988) sowie Tiao, Tsay und Wang (1993) und hat Vorbehalte gegen den praktischen Wert der Tests, hält die Kointegrationsidee für Finanzreihen aber für hoch relevant.

## Beispiele

- ETFs sind ein ergiebiges Feld für kointegrierende Reihen; die kanadische und die australische Wirtschaft sind rohstoffbasiert, deshalb werden EWA und EWC als Kandidaten geprüft, und ihr Streudiagramm liegt auf einer Geraden.
- Mit EWA als unabhängiger und EWC als abhängiger Variable ist die CADF-Statistik etwa minus 3,64 und damit negativer als der 95-Prozent-Wert minus 3,359, das Paar kointegriert also mit 95 Prozent Sicherheit.
- Für EWA und EWC schließen Trace- und Eigen-Test auf zwei kointegrierende Beziehungen: die Trace-Null r gleich 0 wird auf 99 Prozent verworfen, r kleiner oder gleich 1 auf 95 Prozent, und beide Eigen-Nullen auf 95 Prozent.
- Mit dem Rohstoffaktien-ETF IGE zusätzlich verwirft der Trace-Test r ≤ 0, r ≤ 1 und r ≤ 2 auf 95 Prozent, Statistiken 34,429, 17,532 und 4,471 gegen 29,796, 15,494 und 3,841; die Eigen-Statistik für r ≤ 0 ist 16,897 und liegt unter dem 90-Prozent-Wert 18,893.
- Die Eigenwerte des Tripels sind 0,0112, 0,0087 und 0,0030; die zugehörigen Eigenvektoren, in der Ordnung EWC, EWA, IGE, lauten minus 1,0460, 0,7600 und 0,2233 für den ersten, minus 0,5797, minus 0,1120 und 0,5316 für den zweiten, sowie minus 0,2647, minus 0,0790 und 0,0952 für den dritten.
- Die Halbwertszeit des Portfolios aus dem ersten Eigenvektor beträgt 23 Tage und ist damit deutlich kürzer als die 115 Tage von USD.CAD.
- EWA kointegriert mit EWC, weil die kanadische und die australische Wirtschaft von Rohstoffen dominiert werden.
- GDX kointegriert mit GLD, weil der Wert der Goldbergbauunternehmen stark vom Goldwert abhängt.
- GDX und GLD fielen Anfang 2008 auseinander, weil hohe Energiepreise den Goldbergbau ungewöhnlich teuer machten; die Erklärung steht in Kapitel 4.
- Das Portfolio aus dem stärksten Eigenvektor von EWA, EWC und IGE hat 23 Tage Halbwertszeit, gegenüber 115 Tagen bei USD.CAD.
- Steigen zwei Preise von 10 und 5 auf 100 und 50, bleibt das Verhältnis 2, während der Spread von 5 auf 50 steigt und dann wahrscheinlich nicht stationär ist.
- GLD und USO sind nicht kointegriert, obwohl hohe Ölpreise über die Inflation mit dem Goldpreis begründet werden; der Unterschied von Spotöl und den Öl-Futures in USO wird auf Kapitel 5 verschoben.
- Trotzdem erreicht der Preis-Spread mit adaptiver Hedge Ratio etwa 10,9 Prozent APR und eine Sharpe Ratio von etwa 0,59, der Log-Preis-Spread 9 Prozent und 0,5, und das Verhältnis eine negative APR.
- Der Preis-Spread mit wechselnder Hedge Ratio sieht sehr stationär aus, das Verhältnis USO zu GLD nicht.
- EUR.GBP ist ein Verhältnis aus EUR.USD und GBP.USD; für ein nicht wirklich stationäres Kreuz wie MXN.NOK kann das Verhältnis wirksamer sein als der Spread, auch wenn man USD.NOK und USD.MXN handeln muss.
- EWA und EWC sind Kandidaten, weil Australien und Kanada rohstoffbasierte Ökonomien sind; ihre Kointegration wurde in Kapitel 3 bestätigt, 2009 im Blog genannt und bestand beim Schreiben im November 2012 weiter.
- Neben Länder-ETFs sind Sektor-ETFs ergiebig; der Retail-Fonds RTH kointegriert mit dem Consumer-Staples-Fonds XLP, und mit mehr ETFs auf denselben Sektor nehmen die Gelegenheiten zu.
- GLD gegen GDX kointegriert im Johansen-Test vom 23. Mai 2006 bis 14. Juli 2008 mit 99 Prozent Wahrscheinlichkeit und verliert die Kointegration vom 15. Juli 2008 bis 9. April 2012.
- Am 14. Juli 2008 erreichte WTI etwa 145 Dollar je Barrel, ein Allzeithoch; teures Öl verteuert die Goldförderung, senkt die Gewinne der Minen und lässt deren Aktien gegenüber dem Gold-Spot underperformen.
- Das Triplet GLD, GDX und USO kointegriert über 2006 bis 2012 laut Johansen mit 99 Prozent Wahrscheinlichkeit für eine kointegrierende Beziehung.
- USO gegen XLE ist kein sauberes Ware-gegen-Produzent-Paar: GLD hält Gold und spiegelt den Spot, USO hält kein Öl, sondern Öl-Futures; selbst wenn XLE mit dem Öl-Spot kointegriert, muss es nicht mit USO kointegrieren, und das gilt für jeden Commodity-Futures-Fonds gegen einen Produzentenfonds.
- Im Training vom 1. Januar 2007 bis 31. Dezember 2007 kointegrieren 98 SPX-Aktien im Johansen-Test jeweils einzeln mit SPY bei mindestens 90 Prozent Wahrscheinlichkeit; der zweite Test auf Logpreisen, wegen täglichen Rebalancings auf konstantes Kapital je Aktie, zeigt Kointegration des Long-only-Portfolios mit SPY mit besser als 95 Prozent, und es gibt zwei kointegrierende Relationen.
- Das ETF-Paar GLD gegen GDX hörte 2008 auf zu kointegrieren, verwiesen auf Kapitel 4.
- Die Hypothese führte den Stopp auf den hohen Rohölpreis zurück.
- Wurde der Ölpreis als Inputvariable ergänzt, funktionierte das Kointegrationsmodell wieder.
- Ein typisches Beispiel ist Pairs Trading: Sind die Aktien von Ford und GM kointegriert und Ford relativ zu GM zu hoch, wird Ford short und GM long gestellt.
- Der Paartrade gewinnt unabhängig davon, wie die Divergenz korrigiert wird, ob Ford fällt, GM steigt oder eine Kombination aus beidem eintritt.
- Fosback nutzte die Kointegrationsanalyse innovativ, um eine dritte Variable, den S&P 500, vorherzusagen, statt das Verhalten des Spreads zwischen den kointegrierten Reihen.
- Sein Fosback Index nutzt, dass Zinssätze und die Cash-Quoten von Fonds kointegrierte Reihen sind, und entstand mehr als ein Jahrzehnt vor der Veröffentlichung von Engle und Granger.
- Der Index signalisiert, wenn die Cash-Quote der Fonds deutlich von dem Niveau abweicht, das ihre lineare Beziehung zu den kurzfristigen Zinsen vorhersagt.
- Übermäßiger Pessimismus heißt, die Fondsmanager halten deutlich mehr Cash, als die kurzfristigen Zinsen vorhersagen, und übermäßiger Optimismus ist der umgekehrte Fall.
- Fosback fand, dass sowohl übermäßiger Pessimismus als auch übermäßiger Optimismus, so gemessen, mit künftigen Renditen des Aktienmarkts korrelierten.
- Der Index entfernt den Einfluss der kurzfristigen Zinsen aus den Cash-Quoten und misst die Stimmung der Fondsmanager reiner als die rohe Cash-Quote, die von den Zinsen verfälscht ist.
- Der Autor entwickelte 1983 zusammen mit der Raden Research Group den Zeitreihenoperator YY, der im Konzept der Kointegrationsanalyse ähnlich ist, mit der Ausnahme, dass die YY-Werte durch den Standardfehler der Regression normiert wurden und kein expliziter Test auf die Stationarität der Residuen gemacht wurde.
- Die Entwicklung von YY wurde angeregt durch Arthur Merrill, DFE: Deviation from Expected (Relative Strength Corrected for Beta), Market Technician Journal, August 1982, Seiten 21–28.
- Die auf YY beruhenden Indikatoren dienten als Kandidateneingaben für verschiedene Prognosemodelle. Ein Beispiel war ein Sentiment-Indikator auf der Beraterstimmung zu T-Bonds.
- Die Prognosekraft der rohen Konsensinformation wurde durch eine YY-Transformation verbessert, die vergangene Marktänderungen als Regressorvariable nutzte.
- Der Return-Reversal-Effekt ähnelt dem Residual-Reversal-Effekt, der auf der Kointegrationsanalyse beruht.
- Die simulierte Reihe zu (8.31) hat 200 Punkte und die Einheitsmatrix als Schockkovarianz. Beide Komponenten zeigen hohe Autokorrelationen und das Erscheinungsbild von Einheitswurzel-Nichtstationarität, obwohl im Vektor nur eine Einheitswurzel steckt.
- Die logarithmierten 1- und 3-jährigen US-Treasury-Sätze, April 1953 bis Januar 2001, 574 Beobachtungen der Federal Reserve Bank of St. Louis, laufen eng zusammen und erscheinen einheitswurzel-nichtstationär. Näherungsweise trägt der 3-Jahres-Satz einen Faktor (1 minus B) und der 1-Jahres-Satz (1 minus B)(1 minus 0,82 B).
- Der Kurs der Nokia-Aktie in Helsinki und der Kurs ihrer American Depositary Receipts in New York müssen sich gemeinsam bewegen, sonst besteht eine Arbitragemöglichkeit. Hat der Aktienkurs eine Unit Root, müssen die beiden Preisreihen kointegriert sein; in der Praxis nach Anpassung um Transaktionskosten und Wechselkursrisiko.
- Die wöchentlichen 3- und 6-Monats-Treasury-Bill-Zinsen des Sekundärmarkts vom 12. Dezember 1958 bis zum 6. August 2004, 2383 Beobachtungen der Federal Reserve Bank of St. Louis, laufen eng zusammen. Das BIC wählt ein VAR(3). Mit restricted constant, weil für den US-Zins a priori kein Drift angenommen wird, bestätigen beide Johansen-Tests genau einen Kointegrationsvektor.
- Der geschätzte Kointegrationsvektor der Treasury-Bill-Zinsen ist 1 und −1,0124 für den 6-Monatszins, Standardfehler 0,0086, t-Statistik −118,2799, Intercept 0,2254 mit Standardfehler 0,0545 und t-Statistik 4,1382. Die stationäre Reihe ist ungefähr die Differenz der beiden Zinsen und hat einen Mittelwert von etwa −0,225. Die Ladungen auf den Fehlerkorrekturterm sind −0,0949 (Standardfehler 0,0199, t −4,7590) für den 3-Monatszins und −0,0211 (Standardfehler 0,0179, t −1,1775) für den 6-Monatszins.
- Die angepasste Fehlerkorrektur der Zinsen hat R² 0,1081 und 0,0913 sowie adjustierte R² 0,1066 und 0,0898; die Standardfehler der Innovationen betragen 0,2009 und 0,1807. Große Kointegrationsresiduen treten Anfang der 1980er auf, als die Zinsen hoch und volatil waren.
- Prognosen aus der angepassten Fehlerkorrektur erzwingen die Kointegrationsbeziehungen; darin unterscheiden sie sich von gewöhnlichen VAR-Prognosen.
- Im Cost-of-Carry-Modell sind Logpreis des Indexfutures und Logpreis der Kassaindexaktien nach Zins und Dividendenrendite mit dem Vektor (1, −1) kointegriert, und die kointegrierte Reihe ist z∗t. Im dreiregimen Schwellenmodell sind die Kointegrationseffekte in den beiden äußeren Regimen signifikant und im mittleren Regime insignifikant; das heißt Schwellenkointegration nach Balke und Fomby (1997).
- Für zwei Aktien mit ähnlichen Risikofaktoren ist der Logpreisspread wt = p1t − γ p2t Unit-Root-stationär und damit mean-reverting, und die Logrenditen hängen über eine Fehlerkorrektur von der Abweichung wt−1 − μw ab. Für BHP und VALE lautet die Kleinste-Quadrate-Regression der täglichen Logpreise p1t = 1,823 + 0,717 p2t + ŵt mit σw = 0,044.
- Die Kleinste-Quadrate-Residuen der BHP-VALE-Logpreisregression haben Mittel null und schwanken in einer festen Spanne um diesen Mittelwert. Ein AR(2) ist stationär, und der Augmented-Dickey-Fuller-Test verwirft die Unit Root mit Statistik −6,04 und p-Wert 0,01.
- Der Johansen-Test mit restricted constant bestätigt die Kointegration von xt = (Logpreis BHP, Logpreis VALE)′. Für H(0) ist der Eigenwert 0,0415, die Trace-Statistik 47,74 und die Maximum-Eigenvalue-Statistik 39,965, beide auf dem 1-Prozent-Niveau signifikant. Für H(1) ist der Eigenwert 0,0082 und die Trace-Statistik 7,7748, unter den 5- und 1-Prozent-Werten 9,24 und 12,97.
- Die Maximum-Likelihood-Fehlerkorrektur hat den Kointegrationsvektor 1 und −0,7177 für VALE, Standardfehler 0,0112, t-Statistik −64,0913, sowie den Intercept −1,8144, Standardfehler 0,0169, t-Statistik −107,0430. Der Spread wt = p1t − 0,718 p2t ist stationär mit Mittel 1,81 und liegt nahe an der Kleinste-Quadrate-Schätzung. Der Pairs-Parameter ist γ̂ = 0,718.
- Die Ladungen auf (wt−1 − 1,81) sind −0,067 für BHP und 0,026 für VALE, mit Standardfehlern 0,0145 und 0,0168 sowie t-Statistiken −4,6462 und 1,5659. α1 ist negativ und α2 positiv, wie für die Rückkehr zum Gleichgewicht erwartet. Die Standardfehler der Innovationen sind 0,019 und 0,022; die R² betragen 0,0370 und 0,0104.
- In der urca-Normierung auf die erste Spalte lautet der Kointegrationsvektor für VALE −0,717704 und die Konstante −1,828460. Die Ladungen sind −0,06731196 für die BHP-Differenz und 0,02545606 für die VALE-Differenz.

## Unterschiedliche Quellenpositionen

- Box-Jenkins behandelt Renditen als stationär, aber gedächtnislos; Engle-Granger behandelt Log-Preise als gedächtnisbehaftet, aber nicht stationär, und nutzt Kointegration, damit die Regression trotzdem geht.
- Der Text stellt Engle-Granger, wo Log-Preise Gedächtnis behalten und nicht stationär sind, dem Box-Jenkins-Bild gegenüber, in dem Renditen stationär und gedächtnislos sind.
- Weiterführend genannt werden Box und Tiao (1977), Engle und Granger (1987), Stock und Watson (1988) und Johansen (1988); kointegrierte VAR-Modelle werden in Abschnitt 8.6 behandelt.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 96–115 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-006-p096-p115|S. 96–115]]
- Advances in Financial Machine Learning.pdf, S. 115–134 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-007-p115-p134|S. 115–134]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 419–438 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-023-p419-p438|S. 419–438]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 1–13 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-001-p001-p013|S. 1–13]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 52–71 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-004-p052-p071|S. 52–71]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 71–75 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-005-p071-p075|S. 71–75]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 76–95 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-006-p076-p095|S. 76–95]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 95–98 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-007-p095-p098|S. 95–98]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 99–118 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-008-p099-p118|S. 99–118]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 119–138 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-009-p119-p138|S. 119–138]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 138–143 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-010-p138-p143|S. 138–143]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 163–165 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-012-p163-p165|S. 163–165]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 199–214 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-015-p199-p214|S. 199–214]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 115–134 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-007-p115-p134|S. 115–134]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 438–457 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-024-p438-p457|S. 438–457]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 457–476 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-025-p457-p476|S. 457–476]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 476–495 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-026-p476-p495|S. 476–495]]

## Verwandte Themen

- Engle und Granger, Co-integration and Error-Correction: Representation, Estimation and Testing, Econometrica 55 (1987), Seiten 251–276, ist die angeführte Grundlage der Kointegration.
