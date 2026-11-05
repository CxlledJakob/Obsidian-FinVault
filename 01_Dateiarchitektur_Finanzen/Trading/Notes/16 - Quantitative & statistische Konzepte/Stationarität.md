---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Zeitreihen"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Stationarität


## Kurzdefinition

- Nichtstationarität entsteht hier durch Gedächtnis, also durch eine lange Historie früherer Niveaus, die den Mittelwert der Reihe über die Zeit verschiebt.
- Renditen sind stationär, aber gedächtnislos; Preise haben Gedächtnis, sind aber nicht stationär. Gesucht ist die kleinste Differenzierung, die die Preisreihe stationär macht und möglichst viel Gedächtnis behält.
- Box-Jenkins behandelt Renditen als stationär, aber gedächtnislos. Engle-Granger behandelt Log-Preise als gedächtnisbehaftet, aber nicht stationär.
- Notwendig und hinreichend für die Stationarität des diskreten Ornstein-Uhlenbeck-Prozesses ist ein Koeffizient phi im offenen Intervall von minus 1 bis 1.
- Werden Rohpreise im ADF getestet und die Null verworfen, gelten die Preise als stationär mit endlicher Varianz.
- Die wenigen Preisreihen, die mean-reverting gefunden werden, heißen stationär.
- Stationarität heißt, dass die Varianz der Logpreise langsamer wächst als bei einem geometrischen Random Walk, also sublinear in der Zeit, angenähert durch τ hoch 2H mit H kleiner als 0,5.
- Stationarität ist ein irreführender Name: sie bedeutet nicht, dass die Preise notwendig in einer Spanne liegen und die Varianz zeitunabhängig mit Hurst-Exponent null ist, sondern nur, dass die Varianz langsamer wächst als normale Diffusion.
- Stationarität bedeutet, dass Preise langsamer diffundieren als ein geometrischer Random Walk.
- Es gibt eine strenge mathematische Definition einer stationären Zeitreihe; hier wird das Wort lockerer benutzt für eine Reihe mit über die Zeit relativ stabilem Durchschnitt und mit Schwankungen, die in einer ungefähr horizontalen Spanne bleiben.
- Praktiker der technischen Analyse nennen solche Reihen oft Oszillatoren.
- Probleme, deren statistische Eigenschaften über die Zeit stabil bleiben, heißen stationär. Probleme, in denen sich die statistischen Eigenschaften über die Zeit ändern, heißen nichtstationär.
- Statistische Probleme, in denen der Populationsparameter fest bleibt, heißen stationär. Ändert sich der Populationsparameter, ist er instabil oder nichtstationär.
- In dem Beispiel wird angenommen, das zugrunde liegende Phänomen sei stationär, das heißt, es bleibe über die Zeit unverändert.
- Die dort verwendete Definition von stationär ist nicht streng richtig, aber für die Zwecke der Diskussion nahe genug.
- Eine Zeitreihe {rt} ist streng stationär, wenn die gemeinsame Verteilung von (rt1, …, rtk) für jedes t identisch mit der von (rt1+t, …, rtk+t) ist. Die gemeinsame Verteilung ist dann invariant gegen Zeitverschiebung. k ist eine beliebige positive ganze Zahl.
- Strenge Stationarität ist eine starke Bedingung und empirisch schwer zu prüfen.
- {rt} ist schwach stationär, wenn der Mittelwert E(rt) = µ konstant ist und die Kovarianz Cov(rt, rt−ℓ) = γℓ nur von ℓ abhängt.
- Schwache Stationarität eines AR(1) bedeutet, dass der Mittelwert konstant ist, die Varianz γ0 konstant ist und die Kovarianz von rt und rt−j nur von j abhängt, nicht von t.
- Schwache Stationarität einer k-dimensionalen Reihe bedeutet, dass die ersten und zweiten Momente zeitlich unveränderlich sind; Mittelwertvektor und Kovarianzmatrix sind konstant.
- Der Extremalindex und Leadbetters Sätze sind für streng stationäre Reihen formuliert, nicht nur für schwach stationäre.
- Notwendig und hinreichend für die schwache Stationarität eines VAR(1) ist, dass alle Eigenwerte von Φ betragsmäßig kleiner als 1 sind, sofern die Kovarianzmatrix von at existiert. Im univariaten AR(1) reduziert sich das auf den Betrag von φ kleiner als 1.
- Eine Reihe heißt Unit-Root-stationär und I(0), also nicht integriert, wenn alle Nullstellen der Determinante |Φ(B)| außerhalb des Einheitskreises liegen.

## Kernaussagen

- Als Folge von Arbitrage haben Finanzreihen ein niedriges Signal-Rausch-Verhältnis; ganzzahlige Stationaritätstransformationen senken das Signal weiter, weil sie das Gedächtnis entfernen.
- Sind nach einer solchen Transformation nur Reste des Signals übrig, führen komplexe Verfahren auf den gedächtnislosen Reihen leicht zu Fehlentdeckungen.
- Preisreihen haben Gedächtnis, weil jeder Wert von einer langen Historie früherer Niveaus abhängt; ganzzahlig differenzierte Reihen wie Renditen schneiden diese Historie nach einem endlichen Fenster ab.
- Renditen sind nur eine und in den meisten Fällen suboptimale Preistransformation unter vielen möglichen.
- Null-Differenzierung ist ebenso willkürlich wie die Differenzierung um einen Schritt.
- Bei positivem ganzzahligem d sind alle Gewichte nach k größer als d null. Für d gleich 1, die übliche Renditenrechnung, bleibt die Gewichtsfolge 1, minus 1 und danach nur Nullen.
- Liegt d zwischen 0 und 1, sind alle Gewichte nach dem ersten negativ und größer als minus 1. Für d über 1 ist das zweite Gewicht kleiner als minus 1, und alle weiteren sind positiv.
- Die Gewichte konvergieren asymptotisch gegen null, von links, wenn der ganzzahlige Anteil von d gerade ist, und von rechts, wenn er ungerade ist.
- Im Sonderfall d zwischen 0 und 1 liegt jedes Gewicht nach dem ersten echt zwischen minus 1 und 0. Dieser Vorzeichenwechsel ist nötig, damit die transformierte Reihe stationär wird, während das Gedächtnis langfristig abklingt oder sich ausgleicht.
- Der minimale Fixed-Width-Koeffizient d* misst, wie viel Gedächtnis für Stationarität entfernt werden muss: 0, wenn die Reihe schon stationär ist, unter 1 bei einer Unit Root und über 1 bei explosivem Verhalten wie einer Blase.
- Im Fall einer nur milden Nichtstationarität, d* wenig über 0 und weit unter 1, entfernt die volle ganzzahlige Differenzierung zu viel Gedächtnis und Prognosekraft.
- Nahezu alle genannten Finanzarbeiten erzwingen Stationarität mit d gleich 1 und überdifferenzieren damit. Bei 87 der liquidesten Futures genügt in allen Fällen d unter 0,6, bei der großen Mehrheit schon d unter 0,3.
- Die Fixed-Width-Fracdiff-Methode zeigt, dass nicht das ganze Gedächtnis aufgegeben werden muss, um Stationarität zu gewinnen, und dass der Kointegrations-Kunstgriff für ML-Prognosen nicht nötig ist.
- Die Fixed-Width-Fracdiff-Methode zeigt, dass für Stationarität nicht das ganze Gedächtnis aufgegeben werden muss.
- Dieselbe Methode soll Stationarität sichern, ohne auf Gedächtnis und damit auf Prognosekraft zu verzichten.
- Ein Prozess aus unabhängigen identisch verteilten Gauß-Ziehungen wird als gedächtnislose stationäre Reihe beschrieben. Die kumulative Summe dieser Ziehungen wird als nichtstationäre Reihe ohne Gedächtnis beschrieben.
- Eine Sinusreihe wird als stationäre Reihe mit Gedächtnis beschrieben. Werden alle Werte um dieselbe positive Größe verschoben und danach kumulativ summiert, entsteht nach dem Text eine nichtstationäre Reihe mit Gedächtnis.
- Die zweifache Differenzierung der kumulativen Summe aus der Übung wird als überdifferenziert bezeichnet.
- Die Verteilung des diskreten Ornstein-Uhlenbeck-Prozesses ist gaußsch.
- Exponentielles Wachstum oder Kollaps ist mit einem stationären Prozess unvereinbar und auf Dauer unhaltbar.
- Ein Zyklus aus Blase, Platzen und neuer Blase lässt die Reihe für Tests mit nur einer Blase stationär erscheinen.
- Tests, die mehrere Blasen zulassen, sind deshalb robuster.
- Standard-Unit-Root- und Kointegrationstests können einen stationären Prozess nicht verlässlich von einem periodisch zusammenbrechenden Blasenmodell unterscheiden.
- Solche Muster sehen eher wie ein Unit-Root-Prozess oder eine stationäre Autoregression aus als wie ein explosiver Prozess.
- Im Null-Lag-Modell auf Logpreisen konvergiert der erwartete Logpreis bei Beta kleiner als 0, und bei Beta gleich 0 ist das System nichtstationär.
- Der Augmented-Dickey-Fuller-Test, der Hurst-Exponent, der Variance-Ratio-Test und die Half-Life dienen dazu, Time-Series-Mean-Reversion oder Stationarität zu erkennen.
- Über die mechanische Anwendung hinaus soll intuitiv klar werden, was diese Tests wirklich prüfen, samt der einfachen mathematischen Gleichungen dahinter.
- Als Eingaben kommen Rohpreise, Log-Preise oder Verhältnisse infrage, und es wird gezeigt, welche Wahl am sinnvollsten ist.
- Hurst-Exponent und Variance-Ratio-Test prüfen die Stationarität, der ADF-Test die Mean Reversion.
- Man ist nicht auf von sich aus stationäre Instrumente beschränkt, weil kointegrierende Reihen ein stationäres Portfolio ergeben.
- Der Eigenvektor mit dem größten Eigenwert bildet das stationäre Portfolio mit der kürzesten Halbwertszeit.
- Echte Stationarität ist für eine Mean-Reversion-Strategie nicht notwendig, wenn die Position vor dem nächsten Gleichgewicht geschlossen wird.
- Eine stationäre Reihe mit einer Halbwertszeit von zehn Jahren muss trotzdem keine großen Gewinne tragen.
- Der Spread aus Hedge Ratios der Regression oder des Johansen-Tests ist per Konstruktion eine stationäre Zeitreihe.
- Kointegrieren die Logpreise, bildet der Marktwert des kapitalgewichteten Portfolios samt impliziter Kasse eine stationäre Reihe, konstant ist er nicht.
- Tägliche Preisreihen einzelner Aktien erfüllen fast nie die in Kapitel 2 definierte Stationarität; der geometrische Random Walk beschreibt sie gut.
- Saisonale oder intraday Mean Reversion ist mit den üblichen Stationaritäts- oder Kointegrationstests schwer zu erkennen, kann aber sehr profitabel sein.
- Die statistischen Tests der Zeitreihen-Mean-Reversion sind für querschnittliche Mean Reversion weitgehend irrelevant.
- Nach dem Johansen-Eigenvektor wird aus den ausgewählten Aktien und SPY ein long-short-stationäres Portfolio gebildet.
- Die Grundidee eines stationären Portfolios ausländischer Währungen entspricht dem Handel von Aktienindex-ETF-Paaren verschiedener Länder mit ähnlichen ökonomischen Fundamentaldaten.
- Ein ADF-Test zeigt den VIX mit 99 Prozent Sicherheit als stationär.
- Die back-adjustierten Front-Month-Preise von VX mean-reverten laut ADF definitiv nicht.
- Der 12-Monats-Log-Kalender-Spread von CL ist im ADF mit 99 Prozent Wahrscheinlichkeit stationär und hat eine Halbwertszeit von 36 Tagen.
- Renditereihen mean-reverten im Gegensatz zu Preisreihen fast immer; wird nur die Roll-Return-Komponente betrachtet, kann das anders sein.
- Das Verhältnis Back zu Front von VX ist nach dem ADF-Test mit 99 Prozent Wahrscheinlichkeit stationär.
- Ein Portfolio long 0,3906 Kontrakte VX und long einen Kontrakt ES soll stationär sein.
- Der Crack Spread ist nach dem ADF-Test vom 20. Mai 2002 bis zum 4. Mai 2012 nicht mean-reverting.
- Der Spread aus CL und BZ im Verhältnis 1:1 ist weit von stationär entfernt.
- Die Log-Preise der VX-Futures als Funktion der Restlaufzeit fallen nicht auf eine Gerade, anders als bei einem Future auf einen gehandelten Basiswert.
- Subjektives Urteil ist oft nötig, weil die statistischen Eigenschaften finanzieller Zeitreihen nicht stationär sind.
- Wissenschaft kann eigentlich nur mit stationären Statistiken umgehen.
- Die Hebelverfahren unterstellen, dass die künftige Verteilung der Marktrenditen der vergangenen entspricht; das ist meist falsch.
- Noch restriktiver wird dasselbe für die Strategierenditen unterstellt, am restriktivsten eine Gauß-Verteilung.
- Es gibt keine Garantie, dass künftiger Mittelwert und künftige Varianz den historischen gleichen.
- Kelly über mehrere Strategien ist nur optimal, wenn erwartete Renditen und Volatilitäten unverändert bleiben; nach einem schweren Drawdown ist das zweifelhaft.
- Eine Preisreihe, die bisher mean-reverting war, kann künftig trendfolgen.
- Die Kelly-Optimalität über das Portfolio setzt unveränderte erwartete Renditen und Volatilitäten voraus.
- Nach einem schweren Drawdown ist zweifelhaft, ob diese Erwartungen noch gelten.
- Im Perlenbeispiel wird jede Stichprobe zurück in die Schachtel gelegt, bevor die nächste gezogen wird. Dadurch bleibt der Grauanteil F-G über die 50 Ziehungen konstant.
- Würden die Perlen nach jeder Ziehung nicht zurückgelegt, änderte sich F-G im Lauf der 50 Ziehungen, weil Gruppen von Perlen dauerhaft entnommen würden.
- Finanzmärkte können durchaus nichtstationär sein. Für die Lehre ist das Perlenproblem stationär angelegt.
- Es wäre unvernünftig, die Dynamik der Finanzmärkte als stationär anzunehmen, und deshalb unvernünftig, zu erwarten, dass die Profitabilität einer Regel ewig anhält.
- Die unmittelbare praktische Zukunft ist ein endlicher Zeitraum, über den die Profitabilität einer nützlichen Regel vernünftigerweise anhalten kann, obwohl die Märkte nichtstationär sind.
- Der Populationsmittelwert ist unbekannt und variiert in stationären Problemen nicht. Der Stichprobenmittelwert wird aus beobachteten Werten berechnet und variiert zufällig von Stichprobe zu Stichprobe.
- Es ist vernünftig anzunehmen, dass Finanzmärkte nichtstationäre Systeme sind.
- Es ist nicht vernünftig anzunehmen, dass jedes Scheitern außer Stichprobe daher kommt, dass sich die Marktdynamik geändert hat.
- Unplausibel ist, dass der Markt sein Verhalten jedes Mal ändert, wenn eine Regel aus dem Labor in den Handel übergeht, und zwar so häufig, wie Regeln außer Stichprobe scheitern.
- Ein Indikator, der als kumulative Summe einer Preis-Volumen-Funktion definiert ist, zeigt langfristige Trends wie Vermögenspreise und Zinsen und ist eine nichtstationäre Zeitreihe.
- Ein gleitender Durchschnitt einer Preis-Volumen-Funktion ist stationär: er zeigt keine Trends, betrachtet nur die Beobachtungen im Look-back und bleibt wegen positiver und negativer Werte in einer relativ engen Spanne nahe null.
- Kumulative Marktbreitenindikatoren zeigen langfristige Trends, während Breitenindikatoren als gleitende Durchschnitte eher stabile Mittelwerte und Schwankungsbreiten haben.
- Hohe und tiefe Extreme lassen sich über feste Wertschwellen definieren, wenn die Zeitreihe einen relativ stabilen Mittelwert und eine relativ stabile Schwankungsbreite hat, also stationär ist.
- Alle Eingabereihen der Extremwert-Regeln wurden durch den Kanalnormierungsoperator stationär gemacht.
- Zeigt der statistische Test, dass zwei Reihen kointegriert sind, fällt aus der Analyse ein stationärer Divergenzindikator; in der Kointegrationsterminologie ist das das Error-Correction-Modell.
- Der doppelt kanalnormierte Divergenzindikator hat eine mögliche Schwankungsbreite von 0 bis 100, ähnlich wie jede kanalnormierte Variable.
- Finanzmärkte sind höchstwahrscheinlich nichtstationäre Systeme.
- Statistische Inferenz ist im Allgemeinen nicht dafür gemacht, mit nichtstationären Phänomenen umzugehen.
- Nichtstationarität ist ein Risiko, das jeder Anlage auf Basis einer Regel innewohnt, ob die Regel statistisch abgeleitet wurde oder nicht.
- Der Grundsatz, dass größere Stichproben besser sind, gilt für stationäre Prozesse.
- Bei Finanzmarkt-Zeitreihen, die höchstwahrscheinlich nicht stationär sind, können alte Daten irrelevant oder sogar irreführend sein, und größere Stichproben sind dann nicht besser.
- Die Prognosekraft jedes Backtests ruht auf der Annahme, dass die statistischen Eigenschaften der Preisreihe unverändert bleiben, sodass früher profitable Regeln künftig profitabel bleiben.
- Stationäre Einzelreihen, die an öffentlichen Börsen gehandelt werden, sind selten. Stationäre Reihen lassen sich als Marktwert eines Portfolios aus nichtstationären, kointegrierenden Assets herstellen.
- USD.CAD besteht den ADF-Test nicht: die Statistik ist etwa minus 1,84 gegen den 90-Prozent-Wert minus 2,594. Der Variance-Ratio-Test ergibt pValue 0,367281, ein Random Walk bleibt möglich.
- Die Tests fordern mindestens 90 Prozent Sicherheit. Für den Handel genügt oft weniger; dann misst die Halbwertszeit minus log(2)/λ, ob die Rückkehr praktisch schnell genug ist. Bei USD.CAD sind das etwa 115 Tage, beim Portfolio aus EWA, EWC und IGE 23 Tage.
- Eine intradägliche Abtastung erhöht die Signifikanz des ADF-Tests nicht.
- Für Mean-Reversion-Strategien muss das einzelne Instrument nicht von sich aus stationär sein. Ein stationäres Portfolio lässt sich aus einer großen Vielfalt kointegrierender Aktien und ETFs bauen, und jährlich neu aufgelegte, nur geringfügig andere ETFs vergrößern diese Auswahl.
- Erfolgreiche Mean Reversion braucht keine echte Stationarität. Kurzfristige oder saisonale Rückkehr lässt sich handeln und vor dem nächsten Gleichgewicht schließen. Saisonal bedeutet Rückkehr nur in bestimmten Tagesabschnitten oder unter bestimmten Bedingungen.
- Eine stationäre Reihe mit einer Halbwertszeit von zehn Jahren führt nicht zu großen Gewinnen.
- Der Spread von USO gegen GLD mit täglich neu geschätzter Hedge Ratio sieht sehr stationär aus, obwohl GLD und USO nicht kointegriert sind. Die Ratio USO/GLD sieht dagegen kaum stationär aus.
- Wird bei jeder kleinen Rückkehr ausgestiegen, lassen sich kleine Gewinne auch dann mitnehmen, wenn die Reihe nicht stationär ist und den Mittelwert nie erreicht.
- Ob Preis- oder Logpreisspread benutzt wird, hängt davon ab, welche der beiden Reihen kointegriert. Die Ratio ist nur stationär, wenn die Beträge der Hedge Ratios gleich sind.
- Die täglichen Preisreihen einzelner Aktien erfüllen die Stationaritätsdefinition aus Kapitel 2 fast nie. Der geometrische Random Walk passt: einmal weggelaufen, kehren sie selten zurück.
- Das gilt bei Prüfung in regelmäßigen Abständen, etwa an den Tagesschlüssen. Dieselben Reihen können intraday und saisonal mean-reverten.
- Selbst branchenähnliche Paare sind out of sample selten kointegriert, weil sich Firmenschicksale schnell ändern. ETF-Paare halten die Beziehung eher, weil sich die Korbfundamentaldaten langsamer ändern.
- Der 12-Monats-Log-Kalenderspread von CL ist im ADF-Test mit 99 Prozent Wahrscheinlichkeit stationär. Die Halbwertszeit beträgt etwa 36 Tage.
- Der VIX ist im ADF-Test mit 99 Prozent stationär. Die back-adjustierten Frontmonatskurse des VX-Futures mean-reverten im ADF-Test definitiv nicht. Der Unterschied ist die Rollrendite.
- Kalenderspreads sind trotz desselben Basiswerts nicht allgemein stationär, weil das Signal von der Rollrendite und nicht vom Spot getrieben wird.
- Die Gleichung einer in der Restlaufzeit linearen Log-Preiskurve gilt nur, wenn der Basiswert gehandelt wird. Für VX liegen die Log-Preise nicht auf einer Geraden.
- Die meisten Währungs- und Future-Paare bilden kein stationäres Portfolio, weil sie nicht kointegrieren.
- Ein ADF-Test auf dem Verhältnis Back zu Front von VX zeigt Stationarität mit 99 Prozent Wahrscheinlichkeit.
- Ein ADF-Test auf CL und BZ im Verhältnis 1:1 zeigt, dass der Spread weit von stationär entfernt ist.
- Ein Portfolio long 0,3906 Kontrakte VX und long einen Kontrakt ES soll stationär sein; Abbildung 5.11 zeigt seinen Marktwert.
- Die Log-Preise der VX-Futures gegen die Restlaufzeit fallen nicht auf eine Gerade, anders als die Log-Preise von CL in Abbildung 5.4.
- Im Schlusskapitel heißt stationär, dass die Wahrscheinlichkeitsverteilung der Preise über die Zeit unverändert bleibt, und das ist ausdrücklich ein anderer Sinn als die Stationarität der Zeitreihe in Kapitel 2.
- Wissenschaft kommt eigentlich nur mit stationären Statistiken zurecht; weil finanzielle Zeitreihen in diesem Sinn nicht stationär sind, bleibt subjektives Urteil nötig.
- Bei T Beobachtungen zeigt sich schwache Stationarität darin, dass der Zeitplot mit konstanter Schwankung um ein festes Niveau pendelt.
- Schwache Stationarität erlaubt Schlüsse auf künftige Beobachtungen, etwa Prognosen.
- In der Finanzliteratur wird eine Asset-Renditereihe gewöhnlich als schwach stationär angenommen. Die Annahme lässt sich empirisch prüfen, indem man die Daten in Teilstichproben teilt und die Ergebnisse vergleicht, sofern genug historische Renditen vorliegen.
- Die Lag-ℓ-Autokovarianz γℓ = Cov(rt, rt−ℓ) erfüllt γ0 = Var(rt) und γ−ℓ = γℓ.
- Kapitel 2 behandelt neben der Stationarität auch Unit-Root-Nichtstationarität.
- Unter der Stationaritätsbedingung des AR(2) konvergiert die Autokorrelation mit wachsendem Lag gegen 0; diese Konvergenz ist eine notwendige Bedingung für eine stationäre Zeitreihe.
- Für den stationären AR(1) ist die charakteristische Wurzel gleich phi1 und muss im Betrag kleiner als 1 sein, damit ρl gleich phi1 hoch l mit wachsendem l gegen 0 geht.
- Weißes Rauschen ist eine Folge unabhängiger und identisch verteilter Zufallsvariablen mit endlichem Mittel und endlicher Varianz, und alle seine Autokorrelationen sind null; ist die Reihe normal mit Mittel null und Varianz σ zum Quadrat, heißt sie gaußsches weißes Rauschen.
- Liegen alle Stichprobenautokorrelationen nahe bei null, wird die Reihe praktisch als weißes Rauschen behandelt; die monatlichen IBM-Renditen liegen danach nahe an weißem Rauschen, die des wertgewichteten Index nicht.
- Moving-Average-Modelle sind immer schwach stationär, weil sie endliche Linearkombinationen einer weißrauschenden Folge sind, deren erste beide Momente zeitlich invariant sind.
- Für ein MA(1) ist der Erwartungswert gleich der Konstanten c0 und die Varianz gleich (1 plus θ1 zum Quadrat) mal σa zum Quadrat, beides zeitlich invariant; für ein MA(q) ist die Varianz (1 plus die Summe der quadrierten θ-Koeffizienten) mal σa zum Quadrat.
- Damit die als unendliches AR geschriebene Darstellung des MA(1) stationär bleibt, muss der Betrag von θ1 kleiner als 1 sein, sonst explodiert die Reihe.
- Ein AR ist stationär, wenn alle charakteristischen Wurzeln im Betrag kleiner als 1 sind.
- Die Stationaritätsbedingung eines ARMA(1,1) ist der Betrag von phi1 kleiner als 1, dieselbe wie beim AR(1); nur dann ist die Varianz (1 minus 2 phi1 θ1 plus θ1 zum Quadrat) mal σa zum Quadrat, geteilt durch (1 minus phi1 zum Quadrat), positiv und endlich.
- Ein allgemeines ARMA(p, q) ist schwach stationär, wenn alle Lösungen der charakteristischen Gleichung des AR-Polynoms im Betrag kleiner als 1 sind; AR- und MA-Polynom dürfen keine gemeinsamen Faktoren haben, sonst lässt sich die Ordnung reduzieren.
- Bei einer stationären Reihe konvergieren die Mehrschrittprognosen gegen den Mittelwert der Reihe und die Varianzen der Prognosefehler gegen die Varianz der Reihe, wenn der Horizont wächst.
- Invertierbarkeit ist von dieser Stationarität zu trennen: ein MA(1) ist invertierbar, wenn der Betrag von θ1 kleiner als 1 ist, und nicht invertierbar, wenn der Betrag von θ1 gleich 1 ist.
- Zinsreihen, Wechselkurse und Preisreihen sind tendenziell nichtstationär; bei einer Preisreihe fehlt ein festes Niveau, und eine solche Reihe heißt unit-root-nichtstationär.
- Für eine schwach stationäre ARMA-Reihe fallen die ψ-Gewichte der Moving-Average-Darstellung exponentiell, und ein Schock at−i hat keine dauerhafte Wirkung auf rt.
- Bei einer Einheitswurzel fallen diese ψ-Gewichte nicht gegen null, der vergangene Schock wirkt dauerhaft, und die Reihe hat starkes Gedächtnis.
- Differenzieren überführt die unit-root-nichtstationäre Reihe in eine stationäre: die erste Differenz eines ARIMA(p, 1, q) folgt einem stationären und invertierbaren ARMA(p, q).
- Logrenditen gelten als stationär, während die zugehörige Logpreisreihe unit-root-nichtstationär ist und als ARIMA-Prozess behandelt werden kann.
- Eine trendstationäre Reihe hat einen zeitabhängigen Mittelwert, aber eine endliche und zeitlich invariante Varianz; Entfernen des linearen Zeittrends per Regression macht sie stationär.
- Der Random Walk mit Drift hat dagegen den zeitabhängigen Mittelwert p0 plus µ t und die zeitabhängige Varianz t mal σa zum Quadrat.
- Eine hinreichende Bedingung für die Invertierbarkeit eines ARMA ist, dass alle Nullstellen des MA-Polynoms im Betrag größer als 1 sind; ein reines AR-Modell ist invertierbar, weil die π-Gewichte jenseits der Ordnung p null sind.
- Bei einem invertierbaren ARMA ist die laufende Rendite eine Linearkombination aus dem aktuellen Schock und einem gewichteten Mittel der Vergangenheit, wobei die Gewichte für weiter zurückliegende Werte exponentiell abfallen.
- Bei der stationären Moving-Average-Darstellung läuft die Varianz des l-Schritt-Prognosefehlers mit wachsendem Horizont gegen die Varianz von rt, weil die ψ-Gewichte gegen null gehen.
- Beim fraktional differenzierten Prozess (1 minus B) hoch d mal xt gleich at ist xt für d kleiner als 0,5 schwach stationär und besitzt eine unendliche MA-Darstellung.
- Für d größer als minus 0,5 ist derselbe Prozess invertierbar und besitzt eine unendliche AR-Darstellung.
- Die Autokorrelations- und Spektralformeln gelten im offenen Intervall minus 0,5 kleiner d kleiner 0,5.
- Eine stationäre Reihe hat eine exponentiell abfallende Autokorrelation; bei einer Einheitswurzel geht die Stichproben-Autokorrelation für feste Lags gegen 1; dazwischen liegt das polynomiale Abfallen des Langgedächtnisses.
- Die gemeinsame Maximum-Likelihood-Schätzung einer Regression mit Zeitreihenfehlern setzt voraus, dass das Modell der Fehler stationär und invertierbar ist.
- Ist die Residualreihe einheitswurzel-nichtstationär, werden abhängige und erklärende Variable einmal differenziert und die Regression neu angesetzt.
- Die Residuen der Niveauregression von Drei- auf Einjahres-Treasury-Rendite zeigen dieses Einheitswurzelmuster; die Regression der Änderungen ist der darauf folgende Schritt.
- Volatilität divergiert nicht gegen unendlich, sondern bewegt sich in einem festen Bereich; statistisch ist sie oft stationär.
- Beim ARCH(1) wird der Schock als stationär mit Erwartungswert null behandelt, deshalb sind die unbedingten Varianzen von at und at minus 1 gleich.
- Eine endliche positive unbedingte Varianz verlangt 0 kleiner oder gleich alpha 1 kleiner als 1.
- Stationarität vierter Ordnung mit endlichem viertem Moment verlangt zusätzlich, dass alpha 1 quadrat kleiner als 1/3 ist.
- Die Bedingung, dass die Summe alpha i plus beta i kleiner als 1 ist, macht die unbedingte Varianz eines GARCH-Schocks endlich, während die bedingte Varianz zeitlich verläuft.
- Das bereinigte GARCH(1,1) der monatlichen S&P-500-Überschussrenditen wird als einfaches stationäres Modell bezeichnet; seine unbedingte Varianz ist 0,00314.
- Unter einem IGARCH(1,1) ist die unbedingte Varianz von at und von rt nicht definiert.
- Nelson (1990) zeigt, dass der Varianzprozess unter einem IGARCH ein Martingal ist und unter bestimmten Bedingungen streng stationär, aber nicht schwach stationär, weil die ersten beiden Momente fehlen.
- Die AR- und MA-Polynome des EGARCH müssen Nullstellen außerhalb des Einheitskreises haben, also mit Betrag größer als 1, und dürfen keine gemeinsamen Faktoren haben.
- Das IGARCH-Phänomen kann theoretisch von gelegentlichen Niveausprüngen der Volatilität herrühren.
- Im stochastischen Volatilitätsmodell liegen alle Nullstellen des Polynoms 1 − Σ_{i=1}^{m} α_i B^i betragsmäßig über 1.
- Im Long-Memory-SV-Modell liegt der fraktionale Differenzparameter d im offenen Intervall von 0 bis 0,5. Dadurch fällt die ACF von u_t hyperbolisch statt exponentiell.
- Ist σ²_a mal der Summe der quadrierten MA-Gewichte endlich, ist x_t schwach stationär. Die ersten beiden Momente sind dann zeitlich invariant.
- Der ARMA-Prozess ist linear, weil er eine MA-Darstellung x_t = μ + Σ ψ_i a_{t−i} mit ψ_0 = 1 besitzt. Jeder Prozess, der diese Darstellung nicht erfüllt, heißt nichtlinear.
- Für das Zwei-Regime-TAR(1) mit Koeffizienten −1,5 und 0,5 ist geometrische Ergodizität notwendig und hinreichend an φ^{(1)} < 1, φ^{(2)} < 1 und ein Produkt der beiden Koeffizienten kleiner als 1 geknüpft. Der Prozess ist trotz des explosiven Koeffizienten −1,5 stationär.
- Der Satz, dass das Stichprobenmittel gegen den Mittelwert der Reihe konvergiert, heißt ergodischer Satz und wird als Gegenstück der zentralen Grenzwerttheorie im iid-Fall bezeichnet.
- Die US-Arbeitslosenquote von 1948 bis 2009 ist möglicherweise nicht einheitswurzelstationär. Sie zeigt einen langsamen Aufwärtstrend, ihre Autokorrelation fällt langsam, und sie ist nicht zeitumkehrbar.
- Ein SETAR ist nichtlinear, sobald mehr als ein Regime vorliegt. Die Schwellenvariable eines offenen TAR muss stationär sein und eine stetige Verteilung auf einer kompakten Menge besitzen.
- Eine Voraussetzung für die Stationarität eines STAR-Modells ist, dass alle Nullstellen beider AR-Polynome außerhalb des Einheitskreises liegen.
- Der Bandbreitenwähler nach der Normalreferenz nimmt an, dass die unabhängige Variable stationär ist. Der Referenzwert ist 1,06 s T^{−1/5} für den Gauß-Kern und 2,34 s T^{−1/5} für den Epanechnikov-Kern, mit s als Stichproben-Standardfehler.
- Schwache Stationarität des ACD(r, s) verlangt ω > 0 und 1 > Σ_j (γ_j + ω_j), damit die erwartete bereinigte Dauer E(x_i) = ω / [1 − Σ (γ_j + ω_j)] positiv und endlich ist.
- Für das EACD(1,1) folgt unter schwacher Stationarität μ_x = ω / (1 − γ1 − ω1).
- Eine zeitlich unveränderliche unbedingte Varianz des EACD(1,1) verlangt zusätzlich 1 > 2γ1² + ω1² + 2γ1 ω1.
- Unter dieser Bedingung ist Var(x_i) = μ_x² (1 − ω1² − 2γ1 ω1) / (1 − 2γ1² − ω1² − 2γ1 ω1).
- Berman (1964) verlangt stationäre normale Folgen mit quadratisch summierbarer Autokorrelationsfunktion, damit dieselbe Extremwert-Grenzverteilung wie im unabhängigen Fall gilt.
- Für streng stationäre Zeitreihen verweist der Text den Effekt der seriellen Abhängigkeit auf den Extremalindex in Abschnitt 7.8.
- Bei schwacher Stationarität ist die Kreuzkovarianzmatrix Γℓ eine Funktion des Lags ℓ und nicht des Zeitindex t.
- Sofern nicht ausdrücklich das Gegenteil gesagt wird, werden die Renditereihen finanzieller Assets als schwach stationär behandelt.
- Unter schnell abklingender Abhängigkeit und der Bedingung D(un) ist die Grenzverteilung des Maximums einer streng stationären Reihe ebenfalls eine Extremwertverteilung, ihre Lage- und Skalenparameter hängen aber vom Extremalindex ab.
- Äquivalent müssen alle Nullstellen der Determinante von I minus ΦB betragsmäßig größer als 1 sein, also außerhalb des Einheitskreises liegen. Die Eigenwerte von Φ sind die Kehrwerte dieser Nullstellen.
- Damit die Abhängigkeit von vergangenen Innovationen mit Koeffizienten Φ hoch j sinnvoll bleibt, muss Φ hoch j für j gegen unendlich gegen die Nullmatrix gehen. Andernfalls explodiert Φ hoch j oder konvergiert gegen eine von null verschiedene Matrix.
- Für ein VAR(p) ist notwendig und hinreichend, dass alle Eigenwerte der Begleitmatrix Φ* betragsmäßig kleiner als 1 sind. Das ist äquivalent dazu, dass alle Nullstellen der Determinante von Φ(B) außerhalb des Einheitskreises liegen. Es gilt die Determinante von I minus Φ* B gleich der Determinante von Φ(B).
- Ist rt schwach stationär, konvergiert die ℓ-Schritt-Prognose gegen den Mittelwertvektor und die Kovarianzmatrix des Prognosefehlers gegen die Kovarianzmatrix von rt.
- Ein VMA(q) ist schwach stationär, sobald die Kovarianzmatrix der Schocks existiert. Der Konstantenvektor θ0 ist dann der Mittelwertvektor.
- Notwendig und hinreichend für die schwache Stationarität eines VARMA(p, q) ist dieselbe Bedingung wie für das VAR(p) mit dem AR-Matrixpolynom Φ(B).
- Das bivariate Modell (8.31) ist nicht schwach stationär, weil die Eigenwerte der AR-Koeffizientenmatrix 0 und 1 sind.
- Jede Komponente von (8.31) ist einheitswurzel-nichtstationär, das Vektorsystem enthält aber nur eine Einheitswurzel. Eine Linearkombination kann einheitswurzelstationär sein, während die Komponenten es nicht sind.
- In der Fehlerkorrektur ist β′xt Unit-Root-stationär, und β′xt−1 kompensiert das überdifferenzierte System Δxt.
- Für das bivariate VAR(1) mit einem Kointegrationsvektor ist wt genau dann ein stationärer AR(1), wenn |1 + α1 + α2 β1| < 1 gilt.
- Im Cost-of-Carry-Modell muss z∗t schwach stationär und Unit-Root-stationär sein. Damit Arbitrage profitabel wird, muss der Betrag von z∗t zusätzlich eine Schwelle überschreiten, die von Transaktionskosten und weiteren ökonomischen und Risikofaktoren abhängt.
- Bei restricted constant sind die Komponenten I(1) ohne Drift, während wt einen von null verschiedenen Mittelwert −c0 hat. Bei μt = 0 hat die stationäre Reihe wt den Mittelwert null.
- Das Niveau μt des lokalen Trendmodells ist ein Random Walk. Die erste Differenz wt gleich (1 minus B) yt ist bei Messfehlern ein MA(1): gaußsch, Autokovarianz nur bei Lag 1 und dort minus σ²e, und für die MA-Darstellung wird die Lösung mit Betrag von θ kleiner 1 gewählt.
- Ohne Messfehler, σe gleich 0, ist auch die beobachtete Reihe yt ein ARIMA(0,1,0) und damit das integrierte Niveau selbst.
- Das AR(1) yt gleich 0,6 yt minus 1 plus at, at normal mit Varianz 0,4 zum Quadrat, ist stationär. Die Startvarianz des Zustands ist Var(yt) gleich 0,4 zum Quadrat geteilt durch (1 minus 0,6 zum Quadrat) gleich 0,25, der Startmittelwert ist 0.
- Die Trendkomponente des strukturellen Modells wird üblicherweise nichtstationär angesetzt und kann eine doppelte Einheitswurzel haben. Nur wenn σς und ση beide null sind, ist der Trend linear deterministisch.
- Ist die Varianz der Saisoninnovation gleich 0, ist das Saisonmuster deterministisch. Ist der Dämpfungsfaktor δ des Zyklus gleich 1, ist der Zyklus eine deterministische Sinus-Cosinus-Welle.
- Nach dem Satz von Cayley-Hamilton folgt die Beobachtung eines zeitinvarianten Zustandsraummodells einem ARMA(m, m), m die Dimension des Zustands.
- Hängt die Übergangswahrscheinlichkeit eines Markov-Prozesses von h − t ab, aber nicht von t, hat der Prozess eine stationäre Übergangsverteilung.
- Die Markov-Ketten-Simulation konstruiert einen Prozess, dessen stationäre Übergangsverteilung die gesuchte Posterior P(θ|X) ist.
- Im stochastischen Volatilitätsmodell wird |α1| < 1 angenommen, damit der Logvolatilitätsprozess ln ht stationär ist; nötigenfalls wird ein AR(p) für ln ht verwendet.
- Die Rückwärtsprognose nutzt die Zeitumkehrbarkeit (ln ht − η) = α1 (ln ht−1 − η) + vt mit η = α0/(1 − α1) und |α1| < 1; die umgekehrte Reihe hat dasselbe α1 und dieselbe Innovationsvarianz σ²v.
- Wegen einer Unit-Root-Nichtstationarität werden die Treasury-Zinsen als wöchentliche Änderungen c3t = r3t − r3,t−1 und c1t = r1t − r1,t−1 modelliert.
- In der alternativen Parametrisierung z*t = α0 + α z*t−1 + ηt ist der Erwartungswert E(z*t) = α0/(1 − α) und damit nicht null.
- Beim GE-GARCH faktorisiert das AR-Polynom (1 − 1,765B + 0,775B²) als (1 − 0,945B)(1 − 0,820B); beide charakteristischen Wurzeln sind reell und vom Betrag kleiner als 1, deshalb ist die unbedingte Varianz von rt endlich.
- Die Parameter αij erfüllen Regularitätsbedingungen, sodass die unbedingte Varianz von at existiert; im Gibbs-Lauf für das Markov-Switching-GARCH-M wird zusätzlich αi1 + αi2 < 1 erzwungen.
- Der Persistenzparameter αi1 + αi2 von Zustand 1 erreicht bei den GE-Monatsrenditen häufig die Grenze 1,0, der von Zustand 2 nicht.

## Funktionsweise

- Die Gewichte beginnen bei 1 und entstehen iterativ, indem das vorige Gewicht mit minus (d minus k plus 1) durch k multipliziert wird.
- Beim Expanding Window hängt der relative Gewichtsverlust vom Tempo ab, mit dem die Gewichte gegen null laufen. Zu einer Toleranz wird der Anfang verworfen, dessen Gewichtsverlust die Schwelle überschreitet.
- Bei d gleich 1 genügt es, den ersten Punkt zu streichen. Geht d gegen 0, wird dieser zu verwerfende Vorspann länger.
- Der negative Drift dieses Fensters kommt von negativen Gewichten, die mit der Verbreiterung auf die frühen Beobachtungen gelegt werden. Ohne Kontrolle des Gewichtsverlusts bleibt im Wesentlichen nur dieser Trend sichtbar; mit Kontrolle ist der Drift schwächer, aber immer noch erheblich.
- Das feste Fenster schneidet Gewichte ab, sobald ihr Betrag unter eine Schwelle fällt, und verwendet für alle Zeitpunkte denselben Gewichtsvektor.
- Das Ergebnis ist eine driftfreie Mischung aus Niveau und Rauschen. Wegen Schiefe und Excess-Kurtosis aus dem Gedächtnis ist die Verteilung nicht mehr gaußsch, aber stationär.
- Praktisch wird erst die kumulative Summe gebildet, damit eine Differenzierung nötig ist, dann die Fixed-Width-Reihe für mehrere d zwischen 0 und 1 berechnet und das kleinste d gewählt, dessen ADF-p-Wert unter 5 Prozent liegt.
- Zuerst wird die kumulative Summe gebildet, damit überhaupt eine Differenzierung nötig ist. Dann wird die Fixed-Width-Reihe für mehrere d zwischen 0 und 1 berechnet, und es wird das kleinste d gewählt, bei dem der p-Wert der ADF-Statistik unter 5 Prozent fällt.
- Mean Reversion und Stationarität sind äquivalente Sichtweisen, aber der ADF-Test prüft die Mean Reversion und Hurst-Exponent sowie Variance-Ratio-Test die Stationarität.
- Für einen geometrischen Random Walk ist H gleich 0,5 und die Varianz linear in τ; der Variance-Ratio-Test prüft die Null, dass H wirklich 0,5 ist.
- Feste Schwellenregeln passen zu Reihen, die in diesem lockeren Sinn stationär sind, also keinen Trend zeigen.
- Reihen mit Trend lassen sich detrendieren und dadurch in eine stationäre Reihe überführen; häufig geschieht das durch Differenzen oder durch Verhältnisse.
- Das Verhältnis einer Zeitreihe zu ihrem gleitenden Durchschnitt erzeugt eine stationäre Version der ursprünglichen Reihe.
- Nach dem Detrending schwankt die Reihe in einer relativ klar begrenzten horizontalen Spanne um einen relativ stabilen Mittelwert, und dann lassen sich feste Schwellen verwenden.
- Das Detrending für die Renditerechnung erzeugt eine neue Marktreihe, deren durchschnittliche tägliche Preisänderung null ist, indem diese durchschnittliche Änderung von jedem Tag abgezogen wird.
- Ein Testtyp, mit dem festgestellt wird, dass eine Zeitreihe stationär ist, heißt Unit-Root-Test und wird bei Alexander, Market Models, auf den Seiten 324–328 und 353–361 beschrieben.
- Der Operator YY normierte seine Werte mit dem Standardfehler der Regression und machte, anders als die Kointegrationsanalyse, keinen expliziten Test auf die Stationarität der Residuen.

## Voraussetzungen

- Für Inferenz werden invariante Prozesse gebraucht, etwa Renditen, Änderungen von Log-Preisen, Änderungen von Yields oder Änderungen der Volatilität.
- Überwachte Lernverfahren brauchen stationäre Features, sonst lässt sich eine ungesehene Beobachtung nicht auf viele bekannte Beispiele abbilden.
- Stationarität ist für hohe ML-Leistung notwendig und nicht hinreichend, weil sie allein keine Prognosekraft sichert.
- Die Formel für die Halbwertszeit verlangt zusätzlich phi zwischen 0 und 1.
- Schwache Stationarität setzt implizit voraus, dass die ersten zwei Momente von rt endlich sind.
- Ist rt streng stationär und sind die ersten zwei Momente endlich, dann ist rt auch schwach stationär. Die Umkehrung gilt im Allgemeinen nicht.
- Ist rt normalverteilt, sind schwache und strenge Stationarität äquivalent.
- Das Buch befasst sich vor allem mit schwach stationären Reihen.
- Notwendig und hinreichend für die schwache Stationarität des AR(1) ist, dass der Betrag von phi1 kleiner als 1 ist.
- Die Forderung phi1 zum Quadrat kleiner als 1 folgt daraus, dass die Varianz einer Zufallsvariablen beschränkt und nichtnegativ ist; dann sind Mittelwert und Varianz endlich und zeitlich invariant, und alle Autokovarianzen sind endlich.
- Der Mittelwert eines AR(1) existiert, wenn phi1 ungleich 1 ist.
- Ein AR(2) ist stationär, wenn beide charakteristischen Wurzeln im Betrag kleiner als 1 sind, gleichbedeutend damit, dass beide Lösungen der charakteristischen Gleichung im Betrag größer als 1 sind.
- Ein AR(p) ist stationär, wenn alle Lösungen der Gleichung 1 minus phi1 x minus phi2 x zum Quadrat bis minus phip x hoch p im Betrag größer als 1 sind, also alle charakteristischen Wurzeln im Betrag kleiner als 1.
- Für eine schwach stationäre lineare Reihe muss die Summe der quadrierten ψ-Gewichte konvergieren, also ψi zum Quadrat gegen 0 gehen, wenn i gegen unendlich geht; der Einfluss eines weit zurückliegenden Schocks auf rt verschwindet damit.
- Die Mittelwertdarstellung μ gleich (I minus Φ) hoch minus 1 mal φ0 setzt voraus, dass I minus Φ nicht singulär ist. Für das VAR(p) muss Φ(1) invertierbar sein.
- Für die VARMA-Darstellung wird angenommen, dass die beiden Matrixpolynome Φ(B) und Θ(B) keine linken gemeinsamen Faktoren haben; andernfalls lässt sich das Modell vereinfachen.
- Für Assetrenditen wird der gemeinsame Faktor ft als m-dimensionaler stationärer Prozess angesetzt, mit Erwartungswert μf und Kovarianzmatrix Σf.
- Die Stichprobenkovarianz und die Stichprobenkorrelation des Renditevektors sind unter Regularitätsbedingungen konsistent, wenn die Renditen schwach stationär sind und die Daten aus rt für t = 1 bis T bestehen.
- Das statistische Faktormodell setzt voraus, dass die Renditereihe rt schwach stationär ist, mit Mittelwert µ und Kovarianzmatrix Σr.

## Anwendung im Trading

- Stationäre Gleichgewichtsmodelle brauchen etwas Gedächtnis, um zu beurteilen, wie weit der Preis vom langfristigen Erwartungswert abgedriftet ist, bevor eine Prognose entsteht.
- Die Fixed-Width-Reihe zum kleinsten d mit ADF-p-Wert unter 5 Prozent wird als prognostisches Feature empfohlen.
- Die so gewählte Fixed-Width-Reihe soll als prognostisches Feature verwendet werden.
- Walk-Forward-Tests sind besonders attraktiv für nichtstationäre Phänomene wie Finanzmärkte, weil das wandernde Datenfenster eine dynamische Anpassung hinzufügt und in jedem neuen Fenster eine neue Regel formuliert werden kann.

## Regeln und Kriterien

- In den Beispielen liegt der kritische Wert des ADF-Tests bei 95 Prozent Konfidenz bei minus 2,8623.
- Als Schwelle für das minimale d dient ein ADF-p-Wert unter 5 Prozent.
- Die Auswahlregel für d ist ein ADF-p-Wert unter 5 Prozent.
- Die SADF-Null Beta kleiner oder gleich 0 umfasst den nicht-explosiven Bereich, die Alternative ist Beta größer als 0.
- Fertige stationäre Reihen öffentlich gehandelter Assets sind selten; stationäre Portfolios lassen sich aus kointegrierenden, einzeln nichtstationären Reihen herstellen.
- Eine Stichprobe auf Intraday-Frequenz erhöht die Signifikanz des ADF-Tests nicht.
- Im praktischen Handel kann eine Reihe auch dann mit Mean Reversion gehandelt werden, wenn die 90-Prozent-Sicherheit des Stationaritätstests fehlt, solange die Halbwertszeit für den Horizont kurz genug ist.
- Hat die Reihe den Stationaritätstest bestanden oder ist die Halbwertszeit kurz genug, lässt sich schließlich eine profitable Strategie finden, möglicherweise nicht die gebacktestete.
- Sind alle Eigenwerte von alpha1 plus beta1 positiv und kleiner als 1, ist das bivariate ARMA(1,1) für die quadrierten Schocks des Constant-Correlation-GARCH(1,1) schwach stationär. Dann existiert der Erwartungswert der quadrierten Schocks, und die Renditeschocks haben eine positiv definite unbedingte Kovarianzmatrix.
- Bei Tse und Tsui sichern 0 kleiner oder gleich θi kleiner als 1 und θ1 plus θ2 kleiner als 1, dass die bedingte Korrelationsmatrix für alle t positiv definit bleibt. Bei Engle gilt 0 kleiner als θ1 plus θ2 kleiner als 1.
- Im Hebel-DCC sichert die Bedingung, dass die Summe der drei Steigungskoeffizienten je Asset größer oder gleich null und kleiner als 1 ist und die Konstante positiv ist, die Existenz der Volatilitäten.
- Die Aktienvolatilitäten von IBM und Dell liegen mit der Koeffizientensumme 0,9975 nahe an der IGARCH-Grenze. Die Konstanten ihrer Varianzgleichungen unterscheiden sich nicht signifikant von null.

## Risiken und Grenzen

- Ganzzahlige Differenzierung mit d gleich 1 entfernt in den untersuchten Log-Preis-Reihen mehr Gedächtnis, als für die üblichen ökonometrischen Annahmen nötig ist.
- Das Expanding Window erzeugt einen negativen Drift, der auch nach Kontrolle des Gewichtsverlusts erheblich bleibt, weil jede Schätzung auf einem weiter wachsenden Fenster beruht.
- Auch eine stationäre Reihe mit Hurst-Exponent zwischen 0 und 0,5 hat eine mit der Zeit steigende Varianz, nur langsamer als ein geometrischer Random Walk.
- Auch eine Reihe, die auf kurzer Frist mean-reverting wirkt, muss nicht im strengen Sinn stationär sein; gleitender Durchschnitt, gleitende Standardabweichung oder ein Verhältnis passen die Schwellen dann an das wandernde Niveau an.
- Diese Annahme wird oft entwertet: die Wirtschaftsaussichten eines Landes, das Management eines Unternehmens und die Struktur eines Finanzmarkts ändern sich.
- Komponentenweises Differenzieren eines kointegrierten Systems überdifferenziert und erzeugt Unit Roots im MA-Matrixpolynom.
- Fourier-Transformationen setzen voraus, dass die Daten über die Stichprobe stationär sind, also unveränderliche Eigenschaften haben; flüchtige Marktzyklen, die kommen, gehen und ihre Periode ändern, verletzen diese Voraussetzung.
- Eine längere Datenstichprobe verbessert die Auflösung der Fourier-Analyse, verschärft aber die Probleme mit der Stationarität.

## Beispiele

- Bei den täglich heruntergebrochenen Log-Preisen der E-mini-S&P-500-Futures, fortgeschrieben mit dem ETF-Trick, hat die Originalreihe eine ADF-Statistik von minus 0,3387 und die Renditenreihe eine von minus 46,9114.
- Die ADF-Statistik unterschreitet den kritischen Wert minus 2,8623 in der Nähe von d gleich 0,35. Dort beträgt die Korrelation zur Originalreihe noch 0,995, während sie zwischen Originalreihe und Renditen nur 0,03 beträgt.
- Trade-Bars dieser Futures der Größe 10.000, fraktional differenziert mit d gleich 0,4, zeigen ohne Gewichtsverlustkontrolle einen extremen negativen Drift, mit Expanding Window und Toleranz 0,01 einen gemäßigten Drift und mit festem Fenster bei Toleranz 10 hoch minus 5 eine driftfreie Reihe.
- Bei Orangensaft (JO1 Comdty) und Lebendrind (LC1 Comdty) war nach dem Text gar keine Differenzierung nötig.
- USD.CAD sieht nicht stationär aus; die ADF-Statistik von etwa minus 1,84 verwirft die Null auf 90 Prozent nicht, der kritische Wert ist minus 2,594, der Hurst-Exponent ist 0,49, und der Variance-Ratio-Test lässt den Random Walk mit pValue 0,367281 zu.
- Das Regressionsresiduum von EWC minus Hedge Ratio mal EWA sieht sehr stationär aus, und der CADF-Test verwirft die Null auf 95 Prozent.
- Der erste Johansen-Eigenvektor von EWA, EWC und IGE bildet ein stationäres Portfolio mit 23 Tagen Halbwertszeit, gegenüber etwa 115 Tagen bei USD.CAD.
- Das mit dem besten Eigenvektor gebildete Portfolio aus EWA, EWC und IGE ist die Grundlage der linearen Strategie und hat 23 Tage Halbwertszeit, gegenüber 115 Tagen bei USD.CAD.
- Der Preis-Spread von USO und GLD mit täglicher Hedge Ratio sieht sehr stationär aus, obwohl GLD und USO nicht kointegriert sind.
- Das Verhältnis USO zu GLD sieht daneben nicht stationär aus, und die lineare Strategie darauf hat eine negative APR.
- Das Verhältnis zweier Preise ist nur im Sonderfall betragsgleicher Hedge Ratios stationär; im Beispiel 10 zu 5 gegen 100 zu 50 bleibt das Verhältnis 2, während der Spread von 5 auf 50 steigt.
- Nimmt ein unsichtbarer Dämon zwischen den Ziehungen heimlich graue Perlen weg oder hinzu, ist der Populationsparameter F-G nicht mehr konstant, sondern nichtstationär.
- Indikatoren, die auf dem Leerverkaufsvolumen der NYSE-Spezialisten beruhen, scheinen an Prognosekraft verloren zu haben.
- Die erste Differenz der US-BIP-Logreihe von 1947.I bis 2008.IV, also die Wachstumsrate, schwankt um ein festes Mittelniveau, auch wenn die Schwankung in den jüngeren Jahren kleiner wirkt.
- Die Kleinste-Quadrate-Residuen des BHP-VALE-Spreads haben Mittel null und schwanken innerhalb einer festen Spanne um diesen Mittelwert. Die Stichproben-Autokorrelation fällt exponentiell.
- Das angepasste AR(2) (1 − 0,805 B − 0,122 B²) ŵt = at faktorisiert zu (1 − 0,935 B)(1 − 0,130 B) ŵt = at. Daraus folgt, dass ŵt stationär ist.
- Der Augmented-Dickey-Fuller-Test auf diesen Residuen mit AR(2) verwirft die Unit Root: Statistik −6,04, p-Wert 0,01.
- Der Maximum-Likelihood-Spread wt = p1t − 0,718 p2t wird als stationär mit Mittel 1,81 angegeben.
- Der Text setzt die endliche unbedingte Varianz von rt gleich 0,546/(1 − 1,765 + 0,775) ≈ 49,64.

## Unterschiedliche Quellenpositionen

- Fast die ganze Literatur macht nichtstationäre Reihen per ganzzahliger Transformation stationär, wie bei Hamilton 1994. Der Text fragt, warum gerade die Ordnung 1 optimal sein soll und ob Überdifferenzierung die Literatur zur Effizienzmarkthypothese hin verzerrt.
- Hosking verallgemeinert 1981 ARIMA auf eine bruchweise Differenzenordnung. Solche Prozesse zeigen langfristige Persistenz und Antipersistenz und sollen gegenüber dem üblichen ARIMA besser prognostizieren.
- Hosking hält fest, dass fraktionale Differenzierung in der Zeitreihenanalyse zuvor, abgesehen von einem Hinweis bei Granger 1978, nicht vorkam. Danach zählt der Text acht Aufsätze von neun Autoren, meist zu technischen Fragen wie schnellen Algorithmen.
- Box-Jenkins: Renditen sind stationär, aber ohne Gedächtnis. Engle-Granger: Log-Preise haben Gedächtnis, sind aber nicht stationär; Kointegration erhält das Gedächtnis, lässt aber nur wenige Variablen zu, und die Vektoren sind instabil.
- Gegenüber Box-Jenkins und Engle-Granger hält der Text fest, dass Stationarität und Gedächtnis nicht gegeneinander aufgegeben werden müssen und dass Kointegration für ML-Prognosen nicht erforderlich ist.
- Stationär bedeutet im Schlusskapitel, dass die Wahrscheinlichkeitsverteilung der Preise über die ganze Zeit unverändert bleibt, und ist ausdrücklich ein anderer Sinn als die Stationarität von Zeitreihen in Kapitel 2.
- Stationär heißt hier, dass die Wahrscheinlichkeitsverteilung der Preise über die Zeit unverändert bleibt, und unterscheidet sich von der Stationarität von Zeitreihen in Kapitel 2.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 96–115 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-006-p096-p115|S. 96–115]]
- Advances in Financial Machine Learning.pdf, S. 115–134 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-007-p115-p134|S. 115–134]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 20–39 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-002-p020-p039|S. 20–39]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 172–191 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-010-p172-p191|S. 172–191]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 248–267 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-014-p248-p267|S. 248–267]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 305–324 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-017-p305-p324|S. 305–324]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 400–419 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-022-p400-p419|S. 400–419]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 419–438 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-023-p419-p438|S. 419–438]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 476–495 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-026-p476-p495|S. 476–495]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 1–13 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-001-p001-p013|S. 1–13]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 33–51 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-003-p033-p051|S. 33–51]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 52–71 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-004-p052-p071|S. 52–71]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 71–75 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-005-p071-p075|S. 71–75]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 76–95 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-006-p076-p095|S. 76–95]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 99–118 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-008-p099-p118|S. 99–118]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 119–138 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-009-p119-p138|S. 119–138]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 138–143 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-010-p138-p143|S. 138–143]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 199–214 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-015-p199-p214|S. 199–214]]
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
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 267–286 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-015-p267-p286|S. 267–286]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 286–305 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-016-p286-p305|S. 286–305]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 362–381 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-020-p362-p381|S. 362–381]]
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
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 121–140 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-011-p121-p140|S. 121–140]]

## Verwandte Themen
