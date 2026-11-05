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

# Korrelation


## Kurzdefinition

- Die Korrelation zum Underlying ist die Korrelation der Strategierenditen mit den Renditen des zugrunde liegenden Anlageuniversums.
- Die Konditionszahl einer Korrelationsmatrix ist der Betrag des Verhältnisses aus betragsmäßig größtem und kleinstem Eigenwert.
- Zeitreihenmomentum bedeutet, dass vergangene Renditen einer Preisreihe positiv mit künftigen Renditen korreliert sind.
- Zeitreihenmomentum bezeichnet die positive Korrelation der vergangenen und der künftigen Renditen einer Preisreihe.
- Cross-Sectional Momentum bezeichnet die positive Korrelation der vergangenen und der künftigen relativen Renditen einer Preisreihe gegenüber den anderen Preisreihen eines Portfolios.
- Eine illusorische Korrelation ist die falsche Wahrnehmung einer Beziehung zwischen zwei Variablen und ein erhebliches Problem für subjektive Praktiker der technischen Analyse.
- Zwei Variablen sind korreliert, wenn der Prädiktor das Ergebnis, also die abhängige Variable, vorhersagen kann.
- Das Gütemaß zum Vergleich der Prognoseverfahren ist der Korrelationskoeffizient zwischen prognostiziertem und tatsächlichem Ergebnis. Er reicht von 0, wertlose Prognosen, bis 1,0, vollkommene prognostische Treffgenauigkeit.
- Der Korrelationskoeffizient zweier Zufallsvariablen ist Cov(X, Y) geteilt durch die Wurzel aus Var(X) mal Var(Y), vorausgesetzt die Varianzen existieren. Er misst die Stärke der linearen Abhängigkeit.
- Es gilt −1 ≤ ρx,y ≤ 1 und ρx,y = ρy,x. Die Variablen heißen unkorreliert, wenn ρx,y = 0.
- Die Korrelation zweier Reihen wird konsistent durch die Stichprobenkorrelation geschätzt: Zähler ist die Summe der Produkte der Abweichungen vom jeweiligen Stichprobenmittel, Nenner die Wurzel aus dem Produkt der beiden Summen quadrierter Abweichungen.
- Die gleichzeitige Kreuzkorrelation ist ρij(0) gleich Cov(rit, rjt) geteilt durch das Produkt der Standardabweichungen; es gilt ρij(0) gleich ρji(0), minus 1 ≤ ρij(0) ≤ 1 und ρii(0) gleich 1, sodass ρ0 symmetrisch mit Einsen auf der Diagonale ist.
- Die Lag-ℓ-Kreuzkorrelation ist ρij(ℓ) gleich Cov(rit, rj,t minus ℓ) geteilt durch das Produkt der Standardabweichungen von rit und rjt.

## Kernaussagen

- Eine deutlich positive oder deutlich negative Korrelation zum Underlying bedeutet, dass die Strategie das Anlageuniversum im Wesentlichen hält oder leerverkauft und darüber hinaus wenig eigenen Wert hinzufügt.
- Eine diagonale Korrelationsmatrix hat die niedrigste Konditionszahl und ist ihre eigene Inverse.
- Kommen korrelierte, multikollineare Anlagen hinzu, steigt die Konditionszahl, der größte Eigenwert wächst und der kleinste sinkt.
- Ab einer hohen Konditionszahl machen numerische Fehler die Inverse instabil, sodass eine kleine Änderung eines Eintrags eine ganz andere Inverse ergibt.
- Eine Korrelationsmatrix misst die Kosinus der Winkel zwischen je zwei Vektoren im Raum der Renditezeitreihen.
- Korrelationsmatrizen kennen keine Hierarchie, denn jede Anlage ist ein potenzieller Ersatz für jede andere.
- Pearsons Korrelation ist nicht die einzige, die erfüllt, dass die Kovarianz gleich Korrelation mal den beiden Standardabweichungen ist.
- Die Distanz als Quadratwurzel aus der Hälfte der Differenz von eins und der Korrelation ist eine echte Metrik, weil sie ein Vielfaches des euklidischen Abstands nach Z-Standardisierung ist.
- Die Quadratwurzel aus der Differenz von eins und dem Betrag der Korrelation ist eine echte Metrik auf dem Quotienten der ganzen Zahlen modulo 2.
- Korrelationsstrukturen bleiben über lange Zeiträume nicht invariant.
- Volatilität ist mit dem Aktienindex antikorreliert: fällt der Markt, schießt die Volatilität nach oben, und in geringerem Maß gilt auch das Umgekehrte.
- Das Streudiagramm der Frontmonatskurse von ES gegen die Frontmonatskurse von VX zeigt diese inverse Beziehung.
- Im Regime von August 2008 bis 2012 ist die Volatilität bei gegebenem Indexstand deutlich niedriger als im Regime von 2004 bis Mai 2008, die Spannweite der Volatilitäten aber größer, mit extremeren Volatilitätstagen als zuvor.
- Das Vertrauen steigt mit der Übereinstimmung mehrerer Inputs.
- Mehr Vertrauen ist gerechtfertigt, wenn die Inputs unabhängig, also unkorreliert, sind und Prognoseinformation enthalten; bei redundanten Inputs ist es nicht gerechtfertigt.
- Viele Indikatoren der technischen Analyse wirken wegen Namen und spezieller Berechnungen verschieden, messen aber ähnliche Markteigenschaften.
- Jede subjektive Methode lässt sich als Behauptung einer Korrelation lesen: Prädiktor ist ein Muster oder Signal, Ergebnis die Preisbewegung danach.
- Die gesamte technische Analyse, objektiv wie subjektiv, ist die Suche nach solchen Korrelationen, einzeln oder häufiger in Kombination, um Markttrends zu prognostizieren.
- Bei subjektiven Mustern sind Prädiktor und Ergebnis binär: Das Muster ist entweder vorhanden oder nicht, und die vorhergesagte Bewegung tritt entweder ein oder nicht.
- Von vier Ergebnistypen sind das gemeinsame Auftreten von Muster und vorhergesagtem Ergebnis sowie das gemeinsame Ausbleiben richtige Prognosen, das gemeinsame Ausbleiben allerdings ohne Gelegenheit; ein vorhandenes Muster ohne das Ergebnis ist ein falsches Signal, ein ausbleibendes Muster bei dennoch eintretendem Ergebnis ist ein unterlassenes Signal.
- Menschen achten zu stark auf die bestätigenden Fälle und zu wenig auf die Fälle, die die vermutete Beziehung nicht bestätigen oder ihr widersprechen.
- In der Vierfeldertafel fällt diese Aufmerksamkeit auf die linke obere Zelle; die drei anderen Zellen werden nicht richtig berücksichtigt, und die Subjektivität der Muster verhindert oft schon die nötigen Zählungen.
- Bestätigende Fälle sind notwendig, aber allein nicht hinreichend; für eine gültige Korrelation müssen die Besetzungen aller vier Zellen zählen.
- Weil das nicht erkannt wird, erscheint der Glaube als vernünftiger Schluss aus objektiven Belegen statt als Meinung.
- David Hume hielt die Überzeugung, A verursache B oder sei auch nur mit B korreliert, allein weil auf A stets B folgte, für nichts weiter als eine Denkgewohnheit und eine schlechte Gewohnheit.
- Wird nur behauptet, X sei mit Y korreliert und sage Y vorher, lautet die bedingte Aussage: Wenn X das Y vorhersagt, dann werden künftige Fälle von X von Fällen von Y gefolgt.
- Beim Anpassen zweier Funktionen an dieselben Daten beschreibt die einfache lineare Funktion die allgemeine Tendenz, dass steigende Werte von X mit steigenden Werten von Y einhergehen.
- Die komplexe Funktion mit vielen Koeffizienten ist höchstwahrscheinlich eine detaillierte Beschreibung der zufälligen Schwankungen der Daten zusätzlich zur positiven Korrelation zwischen X und Y.
- Einer der fünf Faktoren des Data-Mining-Bias ist die Korrelation der Regelrenditen, also das Ausmaß, in dem die Leistungshistorien der geprüften Regeln miteinander korrelieren.
- Je weniger sie korrelieren, desto größer ist der Data-Mining-Bias.
- Diese Korrelation ist einer von fünf unabhängigen Faktoren, die bestimmen, wie viel Zufall ein bestimmtes Data-Mining-Vorhaben enthält.
- Regeln gelten als ähnlich, wenn ihre Monats- oder Tagesrenditen stark korreliert sind; je stärker diese Korrelation, desto kleiner der Data-Mining-Bias, und je größer die statistische Unabhängigkeit, desto größer der Bias.
- Höhere Korrelation schrumpft die wirksame Zahl der getesteten Regeln; völlig identische Regeln erzeugen perfekt korrelierte Historien, sind faktisch eine Regel, und der Bias schrumpft auf null.
- Sind die Regeln sehr ähnlich, sinkt die Chance einer außergewöhnlich glücklichen Performance; je unähnlicher sie sind, desto größer die Gelegenheit für eine zufällig gute Passung an die historischen Daten.
- Praktisch ist die Regelkorrelation am ehesten hoch, wenn die Parameter einer bestimmten Regelform optimiert werden.
- In den Gleichwertigkeitsexperimenten waren alle Regeln auf unabhängige Renditen ohne Korrelation gesetzt.
- Jede Regel lief in den Korrelationstests über 100 Monate, getrennt für die beste von 10, von 100 und von 1.000, alle mit erwarteter Rendite null, und die Korrelation wurde von 0 bis 1,0 variiert.
- Der Bias bleibt hoch, bis die Korrelationen sich 1,0 nähern, und er ist für die beste von 1.000 Regeln höher als für die beste von 10.
- Sind die Renditen der Kandidatenregeln korreliert, sinkt der Data-Mining-Bias, weil die Korrelation die wirksame Zahl der geprüften Regeln verringert.
- Im Extrem perfekt korrelierter Renditen wird faktisch nur eine Regel getestet, es findet kein Data Mining statt, und der Bias schrumpft auf null; das galt zuvor für Regeln gleicher Güte mit erwarteter Rendite null und wird hier für ein Universum unterschiedlicher Güte gezeigt.
- Abbildung 6.55 trägt die erwartete Rendite der besten Regel gegen die Zahl der geprüften Regeln von 1 bis 256 auf, bei den Korrelationen 0,0, 0,3, 0,6 und 0,9 und bei 100 Monatsbeobachtungen.
- Je höher die Korrelation, desto geringer die erwartete Rendite der besten Regel, weil effektiv ein kleineres Universum durchsucht wird als die nominale Regelzahl vermuten lässt.
- Bei Korrelation 0,9 ist die erwartete Rendite der besten von 256 nur +1,4 Prozent pro Jahr, gleich einer Zufallsregel; bei Korrelation null fast 4 Prozent, deutlich über dem Universumsmittel von +1,4 Prozent.
- Bei der Monte-Carlo-Permutation müssen dieselben Paarungen von Regelausgabe und verwürfelter künftiger Marktrendite für alle Regeln gelten, damit eine vorhandene Korrelationsstruktur der Regeln erhalten bleibt; sie ist einer der fünf Faktoren des Data-Mining-Bias.
- Die zweite EMH-Annahme lautet, die Bewertungsfehler einzelner Investoren seien unkorreliert: bewertet einer ein Papier zu hoch, gleicht ein anderer das durch eine zu niedrige Bewertung aus, die Fehler heben sich auf und haben im Mittel den Wert null.
- Das wird unterstellt, weil die fehleranfälligen Investoren wahrscheinlich verschiedene, aber nutzlose Strategien benutzen und ihre Handlungen deshalb unkorreliert sein sollten.
- Autokorrelationsstudien messen, wie stark Kursänderungen linear mit früheren Änderungen bei verschiedenen Lags korreliert sind; sie bestätigten, dass Renditen linear unabhängig sind, eine lineare Funktion aktueller und vergangener Renditen künftige Renditen also nicht vorhersagen kann.
- Solche Studien sind schwache Tests, weil sie nur lineare Abhängigkeiten entdecken.
- Die Annahme der Effizienzmarkthypothese, die Fehler der Anleger seien unkorreliert, widerspricht der psychologischen Forschung: Unter Unsicherheit weichen Menschen nicht zufällig von der Rationalität ab.
- Die meisten Menschen machen in solchen Situationen ähnliche Fehler, deshalb sind ihre Abweichungen von der Rationalität korreliert.
- Viele Anleger werden versucht sein, dieselbe Aktie zu kaufen, weil sie dieselbe Urteilsheuristik anspricht, etwa drei positive Gewinnquartale, die als Wachstumswert mit hohem Kurs-Gewinn-Verhältnis wahrgenommen werden.
- Soziale Interaktion, das Herdenverhalten, verschärft diese Fehlerkorrelation: Anleger folgen den Fehlern der anderen, hören auf Gerüchte und ahmen die Handlungen ihrer Mittrader nach.
- Sind zwei Zeitreihen negativ korreliert und bewegen sich in ihren Kanälen gegenläufig, nimmt der Divergenzindikator den Wert null an, sobald sich die kanalnormierten Werte kreuzen.
- In diesem Fall wäre ein Indikatorwert von null eine fehlerhafte Anzeige, die beiden Reihen liefen im Trend zusammen.
- Die Kointegration kann den Fall stark negativer Korrelation abbilden, in dem das Paar 180 Grad außer Phase ist, und vermeidet damit dieses Problem des kanalnormierten Divergenzindikators.
- Das Zentrum der Stichprobenverteilung bei etwa 11 Prozent mittlerer Rendite hängt unter anderem von den Renditekorrelationen der 6.402 Regeln ab.
- Eine Begleitreihe mit geringem Gleichlauf zum S&P 500 lässt den einfachen Divergenzindikator viel weiter schwanken als eine mit hohem Gleichlauf, sodass eine für das erste Paar passende hohe Schwelle beim zweiten nie ein Signal erzeugt.
- Über neun Felder betrug die mittlere Korrelation des statistischen Modells 0,64 und die der Experten 0,33.
- Gemessen am quadrierten Korrelationskoeffizienten, also am Informationsgehalt, waren die Prognosen des Modells im Mittel 3,76-mal so informativ wie die der Experten.
- Bei der Vorhersage der Gewalttendenz aus 19 Eingaben lag die mittlere Korrelation der Experten bei 0,12, die des besten Experten bei 0,36 und die des linearen statistischen Modells bei 0,82.
- In diesem Gewaltbeispiel waren die Prognosen des Modells nahezu 50-mal informativer als die der Experten.
- Für die Diskussion fehlerhafter Wahrnehmung zählen die subjektiven Wahrnehmungen illusorischer Korrelationen durch den Analysten, nicht ein objektiv festgestellter Zusammenhang.
- Ein falsch positives Signal liegt vor, wenn das Signal auftritt, das erwartete Ergebnis aber nicht eintritt.
- Ein falsch negatives Signal, ein ausgebliebenes Signal, liegt vor, wenn das Muster oder Signal nicht auftritt, das Ergebnis, das es vorhersagen soll, aber trotzdem eintritt.
- Die meiste Aufmerksamkeit gilt den Fällen der linken oberen Zelle. Manche Studien zeigen, dass Menschen auch die rechte untere Zelle beachten, also die richtige Erkennung von Nicht-Ereignissen.
- Vage Definitionen von Mustern und Signalen und das Fehlen objektiver Bewertungskriterien erleichtern das Auffinden scheinbar bestätigender Fälle.
- In den Experimenten zur informellen Beurteilung der Kovariation waren die Variablen stetig und konnten jeden Wert innerhalb einer Spanne annehmen, etwa die Temperatur.
- Zuvor waren binäre Variablen gemeint, die nur zwei Werte annehmen: Muster vorhanden oder Muster nicht vorhanden.
- Die mittlere Korrelation zwischen Prognose und Ergebnis betrug auf einer Skala von 0 bis 1,0 beim Expertenurteil 0,33 und beim objektiven Modell 0,64.
- In einer Metaanalyse von über 100 begutachteten Studien, die Expertenurteil und statistische Regeln vergleichen, waren die statistischen Regeln in 96 Prozent der Fälle genauer.
- Der Aktienindex steht invers zur Volatilität: fällt der Markt, steigt die Volatilität stark, und in geringerem Maß gilt das auch umgekehrt.
- Sichtbar wird das als Streudiagramm der Front-Month-Preise von ES gegen die Front-Month-Preise von VX in Abbildung 5.10.
- In diesem Streudiagramm liegen 2004 bis Mai 2008 und August 2008 bis 2012 als zwei getrennte Regime.
- Für TU hat das Renditepaar mit Lookback 250 und Haltedauer 25 einen Korrelationskoeffizienten von 0,27 bei einem p-Wert von 0,02.
- Die höchste ausgewiesene Korrelation in Tabelle 6.1 ist 0,5112 für Lookback 250 und Haltedauer 120, bei einem p-Wert von 0,0617; das Paar 250 und 250 hat 0,4873, aber einen p-Wert von 0,3269.
- Kurze Lags können schwach oder negativ sein: Lookback 25 und Haltedauer 1 hat minus 0,0140 bei einem p-Wert von 0,5353.
- VX und ES sind stark antikorreliert; der Korrelationskoeffizient der Tagesrenditen erreicht minus 75 Prozent.
- Für die Extraktion der Rollrendite genügt ein Instrument mit hoher Korrelation oder Antikorrelation zur Spotrendite; ein exakter Nachbau des Spots ist nicht nötig, und für VIX erfüllt SPY das.
- Die Rollrendite von ES beträgt etwa 1 Prozent annualisiert, deshalb hat ES fast dieselben Renditen wie der Basiswert.
- Die Hoffnung des querschnittlichen Futures-Portfolios ist, dass die Spotpreise positiv mit Wirtschaftswachstum oder anderen Makroindizes korrelieren und sich die Spot-Renditen daher aufheben.
- In der linearen Zeitreihenanalyse stehen die Korrelationen der interessierenden Variable mit ihren Vergangenheitswerten im Mittelpunkt; sie heißen serielle Korrelationen oder Autokorrelationen.
- Ist die lineare Abhängigkeit zwischen rt und den eigenen Vergangenheitswerten rt−i von Interesse, wird die Korrelation zur Autokorrelation verallgemeinert; der Korrelationskoeffizient zwischen rt und rt−l heißt Lag-l-Autokorrelation.
- Für eine schwach stationäre lineare Reihe mit Gewichten ψi, ψ0 gleich 1, gilt ρl gleich der Summe ψi mal ψ(i plus l) geteilt durch 1 plus die Summe der ψi zum Quadrat ab i gleich 1.
- Bei einer schwach stationären Reihe geht ρl mit wachsendem l gegen null, weil die ψ-Gewichte gegen null gehen; die lineare Abhängigkeit der aktuellen Rendite von einer weit zurückliegenden Rendite verschwindet damit für großes l.
- Die wöchentliche einjährige und die dreijährige US-Treasury-Constant-Maturity-Rendite von 2467 Beobachtungen, 5. Januar 1962 bis 10. April 2009, sind hoch korreliert.
- Das Bestimmtheitsmaß von 96,5 Prozent und der Koeffizient 0,930 der Niveauregression sind irreführend, weil die Residuen starke serielle Korrelationen zeigen.
- Die Änderungen bleiben stark linear abhängig: c3t gleich 0,792 mal c1t plus et, residuale Standardabweichung 0,0690, Bestimmtheitsmaß 82,5 Prozent, Standardfehler des Koeffizienten 0,0073.
- Mit MA(1)-Fehler lautet die Beziehung r3t gleich r3,t minus 1 plus 0,794 mal (r1t minus r1,t minus 1) plus at plus 0,182 mal at minus 1; die Zinsen sind gleichzeitig und seriell korreliert.
- Das Bestimmtheitsmaß steigt durch den MA(1)-Fehler nur von 82,5 auf 83,1 Prozent, weil der MA-Koeffizient 0,1823 numerisch klein ist, obwohl er statistisch hoch signifikant ist.
- Nichtsynchroner Handel kann zwischen zwei unabhängigen Aktien eine signifikante Lag-1-Kreuzkorrelation erzeugen: die häufiger gehandelte Aktie zeigt eine Nachricht nahe dem Schluss noch am selben Tag, die seltener gehandelte erst am nächsten Tag und scheint deshalb nachzulaufen.
- In einem Portfolio aus beiden Aktien wird aus dieser Kreuzkorrelation eine signifikante Lag-1-Autokorrelation der Portfoliorendite.
- Sind die Auftragsindikatoren zweier Wertpapiere kontemporär positiv korreliert, können ihre Bid-Ask-Spreads negative Lag-1-Kreuzkorrelationen einführen.
- Die Wirkung nichtsynchronen Handels auf die Rendite eines einzelnen Papiers entspricht in der Zeitreihenliteratur einer zufälligen zeitlichen Aggregation, wobei die Handelswahrscheinlichkeit π den Aggregationsmechanismus steuert.
- Im k-dimensionalen Ito-Prozess ist ρij die Korrelation der Wiener-Zuwächse dwit und dwjt und zugleich die Korrelation der zugehörigen standardnormalverteilten ϵi und ϵj.
- Im Grenzwert Δt gegen 0 gilt (Δxit)(Δxjt) → σi(xt) σj(xt) ρij dt und (Δxit)² → σi²(xt) dt.
- Im Sprungdiffusionsmodell von Kou sind der Poisson-Prozess nt, der Wiener-Prozess wt und die Sprunggrößen Ji unabhängig, sodass zwischen diesen Zufallsquellen kein Zusammenhang besteht.
- Im RiskMetrics-Ansatz für mehrere Positionen ist ρ12 der Kreuzkorrelationskoeffizient der beiden Renditen, also die Kovarianz geteilt durch die Wurzel aus dem Produkt der beiden Varianzen.
- Der Gesamt-VaR zweier Positionen ist die Wurzel aus VaR1 zum Quadrat plus VaR2 zum Quadrat plus 2 mal ρ12 mal VaR1 mal VaR2.
- Bei m Instrumenten gehen zusätzlich alle Paarterme 2 mal ρij mal VaRi mal VaRj ein.
- Für i ungleich j gilt im Allgemeinen ρij(ℓ) ungleich ρji(ℓ), weil die beiden Koeffizienten verschiedene lineare Beziehungen messen; Γℓ und ρℓ sind dann nicht symmetrisch.
- Aus der schwachen Stationarität folgt Γij(ℓ) gleich Γji(minus ℓ), also Γℓ gleich der Transponierten von Γ mit Index minus ℓ und ρℓ gleich der Transponierten von ρ mit Index minus ℓ. Anders als univariat ist ρℓ ungleich ρ mit Index minus ℓ; praktisch genügen die Matrizen für ℓ ≥ 0.
- Die Diagonale ρii(ℓ) ist die Lag-ℓ-Autokorrelation von rit. Für ℓ größer als 0 misst das Nebendiagonalelement ρij(ℓ) die lineare Abhängigkeit von rit vom vergangenen rj,t minus ℓ.
- Zwei Komponenten haben keine lineare Beziehung, wenn ρij(ℓ) und ρji(ℓ) für alle ℓ ≥ 0 null sind. Sie sind gleichzeitig korreliert, wenn ρij(0) ungleich 0 ist. Sie sind entkoppelt, wenn beide Kreuzkorrelationen für alle ℓ größer als 0 null sind.
- Die Beziehung ist unidirektional von rit nach rjt, wenn ρij(ℓ) für alle ℓ größer als 0 null ist, aber ρji(v) für ein v größer als 0 ungleich 0 ist. Feedback liegt vor, wenn es in beiden Richtungen mindestens einen positiven Lag mit Kreuzkorrelation ungleich 0 gibt.
- Diese Bedingungen sind hinreichend. Aussagekräftiger ist ein multivariates Modell, das serielle Korrelationen und Kreuzkorrelationen gleichzeitig erfasst.
- Die geschätzte Kreuzkorrelationsmatrix ist konsistent, in endlichen Stichproben aber verzerrt. Bei Assetrenditen ist ihre endliche Verteilung wegen bedingter Heteroskedastizität und hoher Kurtosis kompliziert; oft genügt eine grobe Näherung der Varianz von ρ-Dach ij(ℓ).
- Das Nebendiagonalelement σ12 der Innovations-Kovarianzmatrix zeigt die gleichzeitige lineare Beziehung. Ist σ12 gleich 0, gibt es keine gleichzeitige lineare Beziehung zwischen den Komponenten.
- Gleichzeitige Korrelationen lassen sich nicht zur Prognose verwenden. Deshalb wird in der Zeitreihenanalyse meist die reduzierte Form genutzt, neben der einfacheren Schätzung.
- Für ℓ größer als 0 misst ρij(ℓ) die lineare Abhängigkeit von rit von rj,t minus ℓ. Die fünf hinreichenden Fälle sind: keine lineare Beziehung, nur gleichzeitige Korrelation, Entkopplung, unidirektionale Beziehung und Feedback.
- Die Komponenten von at sind oft korreliert; die Elemente der Impulsantwortmatrizen ψi lassen sich dann nicht unmittelbar als isolierte Schocks deuten. Die Cholesky-Transformation bt gleich L hoch minus 1 mal at macht die Komponenten unkorreliert.
- Eine Schwäche dieser Orthogonalisierung ist die Abhängigkeit von der Reihenfolge der Komponenten. b1t bleibt gleich a1t und wird nicht transformiert. Andere Reihenfolgen können andere Impulsantworten liefern.
- Im VMA ist die gleichzeitige Korrelation zwischen den rit dieselbe wie zwischen den ait.
- Im kointegrierten Beispiel sind die transformierten Reihen y1t und y2t entkoppelt; ihre gleichzeitige Korrelation ist die der Schocks b1t und b2t.
- Die Stichprobenkorrelation zwischen einer Unit-Root-nichtstationären und einer stationären Reihe konvergiert mit der Stichprobengröße gegen null.
- Im Johansen-Test sind die Größen λ̂i die quadrierten kanonischen Korrelationen zwischen den Residuen der beiden multivariaten Regressionen von Δxt und xt−1 auf den deterministischen Term und die verzögerten Differenzen; sie sind zugleich die partiellen kanonischen Korrelationen zwischen Δxt und xt−1.
- Im bivariaten Normalmodell ist der Korrelationskoeffizient ρ = σ12 / (σ1 σ2) mit σi = Wurzel aus σii, und die Determinante der Kovarianzmatrix ist σ11 σ22 (1 − ρ²).
- Für eine Zerlegung des multivariat normalverteilten Vektors gilt Σ12 = 0 genau dann, wenn die beiden Blöcke unabhängig sind.
- Die Hauptkomponentenanalyse lässt sich auf die Kovarianzmatrix oder auf die Korrelationsmatrix anwenden. Die Korrelationsmatrix ist die Kovarianzmatrix des standardisierten Vektors r∗ = S hoch −1 r, wobei S die Diagonale der Standardabweichungen ist.
- Bei der Korrelationsmatrix ist die Spur gleich k, und der vom i-ten Hauptkomponenten erklärte Varianzanteil ist λi / k.
- Ein Eigenwert null der Korrelationsmatrix zeigt eine exakte lineare Beziehung zwischen den Renditekomponenten an.
- Bei den monatlichen Logrenditen von IBM, Hewlett-Packard, Intel, J.P. Morgan Chase und Bank of America, Januar 1990 bis Dezember 2008, erklären die ersten zwei Hauptkomponenten der Stichproben-Korrelationsmatrix etwa 74 Prozent der Gesamtvariabilität. Die erste ist eine ungefähr gleich gewichtete Linearkombination und steht für die allgemeine Marktbewegung.
- Die zweite Hauptkomponente dieser Korrelationsmatrix hat den Eigenwert 1,072 und den Eigenvektor (0,341, 0,356, 0,385, minus 0,469, minus 0,623)′. Sie bildet den Unterschied zwischen Technologie- und Finanzdienstleistungswerten ab.
- Die Eigenwerte der Korrelationsmatrix sind 2,607, 1,072, 0,569, 0,451 und 0,301 mit kumulierten Varianzanteilen 0,522, 0,736, 0,850, 0,940 und 1,000. Die der Kovarianzmatrix sind 284,17, 112,93, 57,43, 46,81 und 29,87 mit kumulierten Anteilen 0,535, 0,748, 0,856, 0,944 und 1,000. Die Kovarianzmatrix liefert ähnliche Komponentendeutungen.
- Bei vielen Renditereihen liegt die Korrelationsmatrix der Residuen eines linearen Modells sehr nahe an der Korrelationsmatrix der Originaldaten, sodass der Effekt dynamischer Abhängigkeit auf die Faktorenanalyse vernachlässigbar ist.
- Bei den monatlichen Logrenditen der US-Anleihenindizes verändert ein VARMA(2,1) die gleichzeitige Korrelationsmatrix kaum. Die Korrelation von 30- und 20-jährigem Index bleibt 0,98, die von 30- und 1-jährigem Index geht von 0,63 auf 0,66.
- Die aus einem statistischen Dreifaktorenmodell zurückgerechneten Korrelationen von zehn monatlichen Überschussrenditen liegen näher an den Stichprobenkorrelationen als die Korrelationen des industriellen Faktormodells.
- Im univariaten Ansatz für Cisco und Intel, Tagesrenditen vom 2. Januar 1991 bis 31. Dezember 1999, wird ρ durch die Stichprobenkorrelation geschätzt. Sie beträgt 0,473.
- Im bivariaten diagonalen GARCH(1,1) wird die Korrelation als zeitlich konstant angenommen und gemeinsam mit den übrigen Parametern geschätzt. Der Schätzwert ist 0,475.
- Im Cholesky-Modell mit zeitvariabler Korrelation ist die Ein-Schritt-Prognose von ρ am Ursprung t gleich 2275 gleich 0,345, bei σ̂21 gleich 1,791, σ̂²1 gleich 4,252 und σ̂²2 gleich 6,348.
- Die Korrelation des Faktormodells ist ρt gleich exp(qt) geteilt durch (1 plus exp(qt)), mit qt gleich minus 2,098 plus 4,120 mal ρt minus 1 plus 0,078 mal dem standardisierten Kreuzprodukt a1,t minus 1 mal a2,t minus 1. Die Standardfehler der drei Koeffizienten sind 0,025, 0,038 und 0,015.
- Die Korrelationsgleichungen des Faktormodells und des Modells mit zeitvariabler Korrelation in den Gleichungen (10.26) und (10.27) sind im Wesentlichen dieselben.
- Sind Gibbs-Parameter hoch korreliert, sollen sie gemeinsam gezogen werden; im Dreiparameterbeispiel über f(θ1, θ2 | θ3, X, M) und f3(θ3 | θ1, θ2, X, M).
- Alle Parameter univariaten bedingten Verteilungen zu unterwerfen ist oft ineffizient; die Wirkung der Parameterkorrelation auf die Konvergenzrate behandeln Liu, Wong und Kong (1994).
- Die drei bivariaten Modelle unterscheiden sich bei den bedingten Korrelationen der monatlichen IBM- und S&P-500-Logrenditen, 1962 bis 2009, erheblich.
- GARCH mit Cholesky-Zerlegung: die Korrelationen sind relativ glatt und stets positiv, Mittel 0,59, Standardabweichung 0,07, Spanne (0,411, 0,849).
- BEKK(1,1): Mittel 0,59, Standardabweichung 0,13, Spanne (−0,020, 0,877), mit kleinen negativen Werten um 1993.
- Stochastische Volatilität: Mittel 0,60, Standardabweichung 0,14, Spanne (−0,161, 0,839); die Korrelation schwankt von Monat zu Monat stark, und negative Werte treten in mehreren isolierten Perioden auf, weil q21,t den Schock ut enthält.
- ρ ist die Korrelation zwischen εt und ηt; die Kovarianzmatrix von (εt, ηt) hat Einsen auf der (1,1)-Stelle, ρ ση auf der Nebendiagonale und σ²η in der (2,2)-Stelle.
- Über die Cholesky-Zerlegung ist b1t = a1t und b2t = a2t − q21,t b1t, und b2t sowie q21,t sind Residuum und Kleinste-Quadrate-Koeffizient der Regression a2t = q21,t a1t + b2t.
- Die bedingte Kovarianzmatrix von at wird durch {g11,t, g22,t} und q21,t parametrisiert, mit gii,t = Var(bit | Ft−1) und b1t orthogonal zu b2t.
- Streudiagramme der Posteriormittel von ρ21,t aus zwei Gibbs-Läufen, 500+2000 gegen 500+1000 Iterationen, liegen nahe an der Geraden y = x.
- Die Quadrattransformation in Gleichung (12.42) erhält die Korrelation zwischen ηt und εt nicht, falls diese Korrelation existiert.
- Im zweiten stochastischen Volatilitätsmodell bezeichnet die Korrelation ρ zwischen den Störtermen den Leverage-Effekt; im ersten Modell sind {εt} und {ηt} unabhängig, die Korrelation ist also null.
- Für die monatlichen S&P-500-Logrenditen von Januar 1962 bis November 2004 ist das Posterior-Mittel von ρ gleich −0,3892 bei Standardfehler 0,0292, etwa −0,39 und nahe dem in der Literatur üblichen Wert.
- Carroll et al. (1988): Das Ranking des Bewährungsausschusses korrelierte zu 6 Prozent mit Rückfälligkeit, ein Dreifaktorenmodell aus Art der Straftat, Zahl früherer Verurteilungen und Zahl der Verstöße gegen Gefängnisregeln zu 22 Prozent.
- Von Oktober 1977 bis Mai 1987 wurden in Pennsylvania 1035 Verurteilte für Bewährung geprüft; 743 kamen vor den Ausschuss, und 85 Prozent von ihnen erhielten Bewährung.
- Die Entscheidungen folgten bis auf eine der Empfehlung des Bewährungsspezialisten.
- Von den auf Bewährung Entlassenen wurden 25 Prozent innerhalb eines Jahres wieder eingesperrt, flüchtig oder wegen einer weiteren Straftat verhaftet; der Ausschuss hatte keinen dieser Fälle vorhergesagt.
- Korrelationen ändern sich über die Zeit: nach Goetzmann et al. lag die Korrelation UK gegen USA seit den 1870er Jahren zu verschiedenen Zeiten zwischen 0,08 und 0,51.
- Eine Forschungsnotiz von Juni 1996 fand, dass Stilrenditen nicht einfach eine Funktion der Sektorrotation sind: Faktorportfolios innerhalb der Sektoren waren äquivalent und hoch korreliert mit marktweiten Faktorportfolios.
- Langfristig bestimmen Bewertungen die Renditen; die offene Frage ist der nötige Zeithorizont, um das auszunutzen, nicht die laufende Korrelation zum US-Markt.
- Die Long-Short-Betas der Länderstrategien sind im Allgemeinen negativ; beim Kurs-Gewinn beträgt das Long-Short-Beta minus 0,1 bei t minus 2,0, beim Momentum plus 0,1 bei t 2,0.
- Die Vertreter von Portable Alpha sagen, die Strategie arbeite am besten, wenn Alpha und Beta unkorreliert sind, etwa japanisches Alpha auf ein S&P-500-Beta.
- Portable Alpha ergibt nur Sinn, wenn das Alpha zu allen Elementen des schon bestehenden Portfolios unkorreliert ist; vorhandenes japanisches Beta macht dasselbe Problem wie ein überlappendes Long-Short.
- Russell 1000 und S&P 500 können sich als zwei Large-Cap-Inlandsindizes stark überlappen, sodass Portable Alpha dieselbe Aktie long und short hält.
- Für Aktienmärkte 1970 bis 2004 beträgt die mittlere Aufwärts-Aufwärts-Halbekorrelation 0,21 und die mittlere Abwärts-Abwärts-Korrelation 0,38. Die Aufwärtsphase steht als Näherung für ein Klima, in dem alle Märkte gemeinsam steigen; wickelt sich der Reflation-Trade ab, ist die Abwärtsphase der passendere Maßstab.
- Bei einem großen diversifizierten Portfolio ist das Risiko proportional zur Wurzel der Korrelation. Zur Korrektur der asymmetrischen Korrelation ist der VaR mit der Wurzel aus 0,38 geteilt durch 0,21 zu multiplizieren, also mit 1,35. Eine zu optimistische Korrelation unterschätzt das wahre Risiko damit um 35 Prozent.
- Für 1995 bis 2004 liegt die mittlere Aufwärts-Halbekorrelation bei 0,30 und die mittlere Abwärtskorrelation bei 0,44. Dieselbe Rechnung ergibt eine mögliche Unterschätzung des wahren Risikos um 21 Prozent, wenn der VaR auf Aufwärtskorrelationen beruht.
- Die Halbekorrelationen unterscheiden Phasen, in denen beide Märkte steigen, beide fallen oder die Phase gemischt ist. Die Stichprobe der Paare USA, Deutschland, Japan und Großbritannien läuft von 1970 bis 2004 beziehungsweise von 1995 bis 2004.
- Konfidenz ist keine Stellvertretergröße für Fähigkeit: Schlechte Denker waren genauso konfident wie gute, die vorgestellte Korrelation existiert nicht.
- Die Regression der aktuellen Lage auf neun einander sehr ähnliche Blasen leidet unter Multikollinearität; die Hauptkomponentenanalyse umgeht das, indem sie untereinander unkorrelierte Reihen extrahiert.
- Die Abweichung der US-Gewinne von ihrem Trend und die Serie der Nettorückkäufe sind leidlich korreliert.
- Die vorgestellte Korrelation zwischen Konfidenz und Fähigkeit existiert nicht; je selbstsicherer ein Vortragender klingt, desto eher glaubt das Publikum die Botschaft, auch wenn sie logisch fehlerhaft ist.
- Die mediane Korrelation zwischen Hedgefonds-Strategien liegt bei 0,56. Ohne Dedicated-Short-Fonds, die negativ zu Wetten auf steigende Märkte korrelieren sollten, steigt sie auf 0,65.
- Mitte der 1990er Jahre lag diese mediane Korrelation bei etwa 10 Prozent und ist auf 65 Prozent gestiegen, den Höchststand der Reihe.
- Strategien in Emerging-Market-Debt, Equity Long/Short und Global Macro erreichen diese Korrelation, weil sie dasselbe tun: Beta oder Momentum mitreiten oder Volatilität verkaufen.
- Fällt der Aktienmarkt oder steigt die Volatilität, verlieren alle Hedgefonds-Stile.
- Zwischen dem durchschnittlichen BIP-Wachstum und der durchschnittlichen Dollar-Aktienrendite von Schwellenländern, 1988 bis 2004, besteht der umgekehrte Zusammenhang zu dem, den viele Anleger erwarten: niedriges Wachstum geht mit hohen Renditen einher, hohes Wachstum mit niedrigen.
- Zwischen den KGVs von 1995 und den Dollar-Aktienmarktrenditen der folgenden zehn Jahre besteht ein Zusammenhang, in dem die billigsten Schwellenländer die höchsten und die teuersten die niedrigsten Renditen haben.
- Zwischen den BIP-Wachstumsraten von 1990 bis 1995 und den KGVs Ende 1995 besteht ein Zusammenhang, aber kein sehr starker. Er geht in die Richtung, dass für höheres Wachstum höhere Bewertungssätze gezahlt werden.
- Eine statistische Gruppe schlägt Einzelpersonen nur, wenn die Fehler unkorreliert sind: Niemand darf von den Entscheidungen der anderen beeinflusst sein, und die eigene Trefferwahrscheinlichkeit muss unabhängig davon sein, dass alle anderen richtig liegen.
- Menschen irren nach der Grundlage der Behavioral Finance im Allgemeinen auf ähnliche Weise. Ihre Fehler sind deshalb höchst unwahrscheinlich unkorreliert, und der Vorteil der statistischen Gruppe geht verloren.
- Das Argument, ein Überoptimist und ein Pessimist höben sich auf, setzt unkorrelierte Fehler voraus, die nach Montier gerade nicht vorliegen.
- Die Sichten einer Buch-zu-Preis-Strategie auf die einzelnen Aktien sind nicht unabhängig. Die Breite ist deshalb nicht die Zahl der Aktien, hier 800, auch wenn vierteljährlich neu gewichtet wird.
- Eine Erkenntnis, die über viele Märkte wiederholt wird, erzeugt korrelierte Wetten statt strategischer Diversifikation. Bei LTCM war fast jede Strategie Konvergenz, von US-Treasuries bis zu dänischen Mortgage-Backed Securities.
- Konvolution ist eine mathematische Operation auf zwei Funktionen, die eine dritte erzeugt; sie ähnelt der Kreuzkorrelation der beiden Eingangsfunktionen, mit einer Wendung. Ein alter Name ist Faltung, und gerade dieses Falten macht sie für das Trading nützlich.
- Am idealisierten Markttief fallen die Preise linear bis zum Tief und steigen danach linear; faltet man die Preise am Tief, sind die beiden Preissegmente perfekt korreliert.
- Die perfekte Korrelation tritt nur am idealisierten Tief auf; deshalb ist vor der Korrelationsberechnung eine Vorfilterung nötig, damit mit echten Daten eine relativ hohe Korrelation erreicht wird.
- Wird mitten in einem laufenden Trend gefaltet, sind die beiden Preissegmente danach nicht korreliert; wird genau am Hoch gefaltet, sind sie exakt korreliert. Liegt das Hoch nicht am Faltpunkt, sinkt die Korrelation.

## Funktionsweise

- Hierarchical Risk Parity kodiert die Korrelation als Distanz und clustert darüber, statt bei der Inversion die partiellen Korrelationen des vollständigen Graphen auszuwerten.
- Das illustrierte Linkage-Kriterium ist der nearest-point-Algorithmus, also die kleinste Distanz zwischen einem Punkt und dem neuen Cluster.
- Auf einen idiosynkratischen Schock senkt Hierarchical Risk Parity die betroffene Anlage und erhöht eine korrelierte, nicht betroffene Anlage.
- Auf einen gemeinsamen Schock senkt es die betroffenen Anlagen und erhöht unkorrelierte Anlagen mit geringerer Varianz.
- Gemessen wird der Korrelationskoeffizient samt p-Wert für eine gewählte Verzögerung; die stärkste positive Korrelation kann zwischen Renditen verschiedener Lags liegen.
- Eintagesrenditen können negativ korrelieren, während die vergangene 20-Tage-Rendite mit der künftigen 40-Tage-Rendite stark positiv korreliert.
- Statt der Beträge kann die Korrelation der Vorzeichen getestet werden, wenn nur interessiert, dass eine Aufwärtsbewegung einer weiteren folgt.
- Überlappende Fenster werden ausgeschlossen: der Text rückt bei längerem Lookback um die Haltedauer und bei längerer Haltedauer um den Lookback vor.
- Illusorische Korrelationen entstehen besonders bei asymmetrischen binären Variablen, bei denen einer der beiden Werte das Fehlen eines Merkmals oder das Nichteintreten eines Ereignisses bedeutet.
- Eine symmetrische binäre Variable verknüpft dagegen jeden ihrer Werte mit dem Vorliegen eines Merkmals oder dem Eintreten eines Ereignisses, etwa rot gegen blau oder Regen gegen Schnee.
- Sind Prädiktor und Ergebnis beide asymmetrisch binär, werden die Bestätigungsfälle außerordentlich auffällig, und die drei anderen Zellen, in denen eines oder beide das Fehlen registrieren, treten zurück.
- Das Nichteintreten zu bewerten kostet mehr kognitive Anstrengung als das Eintreten; die Sätze, alle Menschen seien sterblich und alle Nichtsterblichen seien Nichtmenschen, sagen dasselbe, aber die verneinte Form braucht Nachdenken.
- Viele Sätze der subjektiven technischen Analyse behaupten genau eine solche Korrelation: ein Signal, das auf dem Chart entweder da ist oder nicht, und ein Ergebnis, das entweder eintritt oder nicht.
- Teilverstärkung, bei der nicht jede Handlung belohnt wird, erzeugt langsameres Lernen, aber stärkere Gewohnheiten als eine Belohnung bei jedem Mal.
- Eine gewünschte Korrelation von 0,7 wurde simuliert, indem ein Münzwurf mit Kopf-Wahrscheinlichkeit 0,70 entschied: bei Kopf übernahm der Monat die Rendite der ersten künstlichen Historie, und das wurde für die weiteren Historien fortgesetzt.
- Für die aktuelle Preisänderung und jede frühere Änderung, beginnend beim Lag 1 und dann Lag 2 und so fort, wird ein eigener Korrelationskoeffizient berechnet.
- In einer zufälligen Reihe fallen diese Korrelationen typischerweise sehr schnell mit dem Lag-Intervall.
- Ist die Zeitreihe der Preisänderungen linear nichtzufällig, weichen einige der Korrelationskoeffizienten signifikant vom Korrelationsmuster einer Zufallsfolge ab.
- Der Stichprobenkorrelationskoeffizient ist die Summe (xt − x̄)(yt − ȳ) geteilt durch die Wurzel aus dem Produkt der beiden Abweichungsquadratsummen, mit x̄ und ȳ als Stichprobenmitteln.
- Bei einer schwach stationären Reihe wird die Korrelation zur Autokorrelation verallgemeinert: die Korrelation von rt mit rt−ℓ hängt nur von ℓ ab.
- Die Stichproben-Kreuzkorrelation ist ρ-Dach ℓ gleich D-Dach hoch minus 1 mal Γ-Dach ℓ mal D-Dach hoch minus 1 für ℓ ≥ 0, mit D-Dach als Diagonalmatrix der Stichproben-Standardabweichungen.
- In der Notation von Tiao und Box steht Plus bei einem Koeffizienten von mindestens 2 durch Wurzel aus T, Minus bei höchstens minus 2 durch Wurzel aus T und ein Punkt dazwischen. Unter weißem Rauschen ist 1 durch Wurzel aus T der asymptotische 5-Prozent-kritische Wert.
- Die bedingte Kovarianz lässt sich schreiben als Dt mal ρt mal Dt. ρt ist die bedingte Korrelationsmatrix, symmetrisch mit Einsen auf der Diagonale, und Dt enthält die bedingten Standardabweichungen. Die zeitliche Entwicklung hängt damit nur von den bedingten Varianzen und den Korrelationen unterhalb der Diagonale ab.
- Über die Cholesky-Zerlegung ist die Korrelation ρ21,t gleich q21,t mal der Wurzel aus σ11,t, geteilt durch die Wurzel aus σ22,t. Sie ist zeitvariabel, sobald q21,t ungleich null ist. Selbst bei konstantem q21,t gleich c ungleich null bleibt sie zeitvariabel, solange das Varianzverhältnis σ11,t zu σ22,t nicht konstant ist. Das unterscheidet die Cholesky-Reparametrisierung von der direkten Modellierung der Korrelation.
- Im Constant-Correlation-Modell von Bollerslev (1990) ist die eine Korrelation ein zeitlich fester Parameter mit Betrag kleiner als 1. Die Mehrschritt-Prognose der Kovarianz ist diese geschätzte Korrelation mal der Wurzel aus dem Produkt der prognostizierten bedingten Varianzen.
- Für eine Korrelation, die positiv ist und in [0, 1] liegt, setzt das zeitvariable GARCH ρt gleich exp(qt) durch (1 plus exp(qt)). qt hängt von der vorherigen Korrelation und vom standardisierten Kreuzprodukt der vorherigen Schocks ab. Sind die beiden Steigungskoeffizienten null, bleibt die Korrelation konstant. Bei negativer Korrelation kann die Gleichung ein Minuszeichen erhalten.
- Bei unbekanntem Vorzeichen bildet die Fisher-Transformation qt gleich ln von (1 plus ρ) durch (1 minus ρ) die Korrelation auf die ganze Zahlengerade ab, mit der Umkehrung ρ gleich (exp(qt) minus 1) durch (exp(qt) plus 1).
- Tse und Tsui lassen die bedingte Korrelationsmatrix zu einer festen Matrix ρ, zur vorherigen Korrelationsmatrix und zur Stichprobenkorrelation der letzten m Schocks schrumpfen. Die Gewichte sind 1 minus θ1 minus θ2, θ1 und θ2, mit θ1 plus θ2 kleiner als 1.
- Engle modelliert eine Hilfsmatrix Qt als Schrumpfung zur unbedingten Kovarianz der standardisierten Innovationen plus einem äußeren Produkt der vorherigen standardisierten Innovationen plus der vorherigen Qt, und normiert Qt zeilen- und spaltenweise zu einer Korrelationsmatrix.
- Weil θ1 und θ2 bei Tse-Tsui und bei Engle Skalare sind, haben alle bedingten Korrelationen dieselbe Dynamik. Bei großer Dimension ist das schwer zu rechtfertigen.
- Über die Cholesky-Zerlegung ist die bedingte Korrelation q21,t mal der Wurzel aus g11,t, geteilt durch die Wurzel aus g22,t plus q21,t zum Quadrat mal g11,t.
- Im EasyLanguage-Code von Ehlers wird die Pearson-Korrelation aus den über die Mittelungslänge M aufsummierten Werten X, Y, X·X, X·Y und Y·Y berechnet: Corr = (M·Sxy − Sx·Sy) / Wurzel((M·Sxx − Sx·Sx) · (M·Syy − Sy·Sy)), nur wenn das Produkt unter der Wurzel größer als null ist.
- Die Korrelation von −1 bis +1 wird mit 0,5 · (Corr + 1) auf den Bereich 0 bis 1 umskaliert, etwa für die Farbdarstellung in einer Heatmap.
- Bei gleich langen Segmenten tritt die Spitzenkorrelation bei der halben Rückschauperiode auf: Bei 13 Balken erscheint das Hoch mit 7 Balken Verzögerung, bei 39 Balken mit 19 Balken.
- Wird ein Trend kurz unterbrochen und läuft weiter, entsteht eine hohe Korrelation bei der halben Rückschau, solange die Rückschau höchstens doppelt so lang ist wie der Abstand der Unterbrechung; bei längerer Rückschau geht das unkorrelierte Segment ein und senkt die Gesamtkorrelation.
- Im Konvolutionsindikator wird eine Lehrbuch-Pearson-Korrelation für jede Rückschauperiode von 1 bis 48 berechnet; X ist der Basisdatenstrom, Y der zurückgefaltete Datenstrom, und X, Y, X·X, X·Y und Y·Y werden über die Rückschaulänge summiert.
- Die Korrelationswerte von −1 bis +1 werden auf eine inverse Fisher-Transformation angewandt, um die Darstellung zu schärfen, und für die Darstellung auf 0 bis 1 umskaliert.
- Ist die Preissteigung über die Rückschau positiv, ist der Farbton der Heatmap rot, ist sie negativ, grün; die Sättigung bestimmt jeweils der Korrelationswert.

## Voraussetzungen

- Sind X und Y beide normalverteilt, gilt ρx,y = 0 genau dann, wenn X und Y unabhängig sind.

## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Je korrelierter die Anlagen sind, desto nötiger ist Diversifikation und desto wahrscheinlicher werden instabile Lösungen.
- Das Inverse-Varianz-Portfolio ignoriert die Korrelationsstruktur und ist dadurch anfällig für systemische Schocks.
- Schocks auf mehrere korrelierte Anlagen bestrafen genau diese Unkenntnis der Korrelationsstruktur.
- Eine Hauptkomponentenanalyse auf einem großen Rentenuniversum leidet unter denselben Nachteilen wie CLA, weil Verfahren für kleine Datenmengen die Hierarchie nicht erkennen.
- Dieselbe Reihe kann auf verschiedenen Zeitebenen Momentum und Mean Reversion zeigen; bei TU ist der Hurst-Exponent 0,44 und der Variance-Ratio-Test verwirft den Random Walk nicht, obwohl einzelne Lag-Paare positiv korrelieren.
- Korrelationsstrukturen der Rollrendite erklären das querschnittliche Momentum von Währungen und Aktien nicht; dort kommen serielle Korrelation des Weltwirtschafts- oder Zinswachstums beziehungsweise langsame Informationsdiffusion infrage.
- Informelle Analyse übersieht gültige Korrelationen selbst dann, wenn sie relativ stark sind, und sieht zugleich Korrelationen, die es nicht gibt; beide Fehler hängen an den Erwartungen aus Vorüberzeugungen.
- Werden zwei Variablen nicht als verbunden erwartet, erkennen Menschen die Beziehung in Experimenten erst, wenn die Korrelation ungefähr 0,70 übersteigt, auf einer Skala von 0 bis 1,0; 1,0 ist eine perfekte Korrelation und 0 keine.
- Eine Korrelation von 0,70 ist weit stärker als alles, was im Bereich der technischen Analyse wahrscheinlich vorkommt, deshalb übersehen subjektive Analysten mit informellen Methoden gültige Beziehungen, die sie nicht erwarten.
- Besteht eine Vorüberzeugung oder eine Motivation, eine Beziehung zu finden, wird eine Korrelation wahrscheinlich auch dann gesehen, wenn keine existiert.
- Auch ohne Vorüberzeugung und ohne Motivation besteht eine ausgeprägte Neigung, illusorische Korrelationen zu sehen.
- Ohne objektiv definierte Signale und ohne objektive Maßstäbe für ihre Ergebnisse sind die Zellzahlen nicht verfügbar, und die wahre Wirksamkeit lässt sich nicht bewerten, auch nicht zuverlässig für die bestätigenden Fälle.
- Objektive Definitionen sind die einzige Lösung dieses Problems fehlender Daten; bis die technische Analyse Objektivität übernimmt, arbeitet sie weiter auf der Basis magischen Denkens und von Mythen.
- Von den untersuchten Plänen teilweiser Verstärkung erzeugt zufällige Verstärkung die Gewohnheiten, die der Löschung am stärksten widerstehen, obwohl das Verhalten mit der Belohnung nicht wirklich verbunden ist.
- Zufällige Verstärkung ist die Belohnung bei einer illusorischen Korrelation der technischen Analyse: Ab und zu folgt auf das Signal durch Zufall das erwartete Ergebnis, und behavioristische Befunde sagen eine extrem löschungsresistente Überzeugung voraus.
- Aberglaube und zwanghaftes Spielen, zwei Gewohnheiten auf illusorischen Korrelationen, gelten als extrem schwer heilbar.
- Korrelationen direkt zu modellieren macht die Likelihood ab drei Dimensionen kompliziert und erzwingt eine beschränkte Maximierung, damit die Kovarianz positiv definit bleibt.

## Beispiele

- Aus den Korrelationen 0,7, 0,2 und minus 0,2 werden die Distanzen 0,3873, 0,6325 und 0,7746.
- Eine dargestellte Korrelationsmatrix von Rentenpapieren umfasst nach dem Clustering über 2,1 Millionen Einträge.
- Zwischen dem ersten und zweiten Rebalancing trifft eine Anlage ein idiosynkratischer Schock, zwischen dem fünften und sechsten zwei Anlagen ein gemeinsamer Schock.
- Für TU hat das Paar 250 zu 25 einen Korrelationskoeffizienten von 0,27 bei einem p-Wert von 0,02.
- Die besten Kompromisse aus Koeffizient und p-Wert sind (60, 10), (60, 25), (250, 10), (250, 25), (250, 60) und (250, 120).
- Die Korrelation der Tagesrenditen von VX und ES erreicht minus 75 Prozent.
- Die Hoffnung der querschnittlichen Rollrendite-Strategie ist, dass die Spotpreise der Rohstoffe positiv mit Wirtschaftswachstum oder anderen Makroindizes korrelieren und sich deshalb gegenseitig aufheben.
- Im Versuch von Smedslund 1963 hielten über 85 Prozent der Krankenschwestern das Symptom für mit der Krankheit korreliert, überzeugt von 37 bestätigenden Fällen in Zelle A; die Zellen waren A 37, B 17, C 33 und D 13 bei 100 Karten, und eine Auswertung aller Zellen zeigt keine Korrelation.
- Im Smedslund-Beispiel hatten etwa 0,69 der Patienten mit Symptom die Krankheit, nämlich 37 geteilt durch 54 gleich 0,685, und etwa 0,72 der Patienten ohne Symptom, nämlich 33 geteilt durch 46 gleich 0,717; die Krankheitswahrscheinlichkeit war also nahezu gleich, ob das Symptom vorlag oder nicht.
- Wäre das Symptom wirklich mit der Krankheit korreliert gewesen, hätten die Anteile deutlich auseinanderliegen müssen, zum Beispiel 0,90 mit Symptom gegen 0,40 ohne; das zeigte einen gültigen Prädiktor, nicht notwendig eine Ursache.
- Obwohl schon diese Verhältnisse keine Korrelation zeigen, hielten 85 Prozent der Schwestern das Symptom für einen verlässlichen Prädiktor.
- Über die weiteren Datensätze hinweg erklärte die Zahl der Bestätigungsfälle in Zelle A am besten, ob eine Korrelation gesehen wurde; die relativen Anteile aus den anderen drei Zellen beeinflussten das Urteil nicht.
- Eine Taube, die 60 Sekunden lang zufällig für Picken verstärkt wurde, pickte danach noch 3,5 Stunden weiter, also 210-mal so lange wie die Verstärkungsperiode.
- Am Floor der American Stock Exchange trug ein Händler täglich dieselbe Krawatte, einer bestand auf einer bestimmten Tür und einer verweigerte einen roten Stift; solche Gewohnheiten entstanden wahrscheinlich durch eine zufällige Paarung mit einem erwünschten oder unerwünschten Ergebnis und wurden durch Zufallsverstärkung aufrechterhalten.
- David J. Leinweber prüfte mehrere hundert ökonomische Zeitreihen einer UN-Datenbank auf die höchste prädiktive Korrelation zum S&P 500.
- Die höchste Korrelation hatte die Butterproduktion in Bangladesch, etwa 0,70, ungewöhnlich hoch für ökonomische Prognosen.
- Wird die Gesamtzahl der untersuchten Zeitreihen berücksichtigt, ist diese Korrelation nicht statistisch signifikant.
- Die Intuition erkennt den Zusammenhang von bangladeschischer Butter und S&P 500 als scheinbar; hätte die höchstkorrelierte Reihe eine plausible Verbindung, würde die Intuition nicht warnen.
- Die neun Felder sind Studienerfolg von Graduierten, Lebenserwartung von Krebspatienten, Änderungen von Aktienkursen, psychische Krankheit anhand von Persönlichkeitstests, Noten und Einstellungen in einem Psychologieseminar, Firmenpleiten anhand von Finanzkennzahlen, studentische Bewertungen der Lehrqualität, Leistung von Lebensversicherungsverkäufern und IQ anhand von Rorschach-Tests.
- Russo und Schoemaker fassen zehn Studien zum Vergleich intuitiver Expertenprognosen mit objektiven linearen Modellen zusammen. Die mittlere Korrelation betrug 0,33 für das Expertenurteil und 0,64 für das objektive Modell.
- Die monatlichen Logrenditen von IBM und S&P 500, Januar 1926 bis Dezember 2008, 996 Beobachtungen in Prozent inklusive Dividenden, haben die gleichzeitige Stichprobenkorrelation 0,65, signifikant zum Niveau 5 Prozent. Die Kreuzkorrelationen bei Lag 1 sind schwach, falls überhaupt vorhanden.
- Signifikante Kreuzkorrelationen der monatlichen IBM- und S&P-500-Logrenditen erscheinen zum ungefähren 5-Prozent-Niveau vor allem bei den Lags 1 und 3.
- Die IBM-Monatsrenditen hängen schwach von vorherigen S&P-500-Renditen ab; das folgt aus der Signifikanz des Elements (1, 2) der Kreuzkorrelationsmatrizen bei Lag 1, Lag 2 und Lag 5.
- Die dynamische Beziehung der beiden Monatsreihen ist schwach, ihre gleichzeitige Korrelation ist aber statistisch signifikant.
- Die gleichzeitige Korrelation der beiden Innovationsreihen im vereinfachten VAR(5) ist 24 geteilt durch die Wurzel aus 48 mal 30, also 0,63, nahe an der Stichprobenkorrelation von 0,65 zwischen den Renditen.
- Die fünf monatlichen Anleiherenditen von 1942 bis 1999 haben hohe gleichzeitige Korrelationen, und die Korrelationen langer Laufzeiten sind höher als die kurzer. Paare mit der 30-jährigen Reihe: 0,98 zur 20-jährigen, 0,92 zur 10-jährigen, 0,85 zur 5-jährigen und 0,63 zur 1-jährigen. Die 5-jährige und die 1-jährige korrelieren mit 0,82.
- Die meisten signifikanten Kreuzkorrelationen der fünf Anleihen liegen bei Lag 1, und die fünf Reihen erscheinen miteinander korreliert. Bei Lag 2 ist in der vereinfachten Matrix nur die Autokorrelation der 1-Jahres-Reihe markiert.
- Die beiden logarithmierten US-Monatssätze sind stark gleichzeitig korreliert. Der Koeffizient ist 2,5 geteilt durch die Wurzel aus 3,58 mal 2,19, also 0,893. Die Kovarianzmatrix der Schocks, mal 10 hoch 3, hat die Einträge 3,58 und 2,50 sowie 2,50 und 2,19.
- Das VAR(1) für IBM und S&P 500 hat Bestimmtheitsmaße 0,0101 und 0,0075, adjustiert 0,0081 und 0,0055. Die dynamische Abhängigkeit ist schwach, und die Impulsantworten klingen schnell ab.
- Die Fehler-Kovarianzmatrix der bedingten Likelihood des vereinfachten VAR(5) ist 48,328570 auf der IBM-Varianz, 30,027406 auf der S&P-Varianz und 24,361464 auf der Kovarianz.
- Die Stichproben-Autokorrelationsfunktion der geschätzten BHP-VALE-Spreadresiduen fällt exponentiell und stützt die Stationarität des Spreads.
- Im Marktmodell für 13 monatliche Überschussrenditen bleiben große Residuenkorrelationen, darunter 0,45 zwischen Caterpillar und Alcoa und 0,48 zwischen General Motors und Ford. Die Residuenkovarianz wird durch 168 − 2 geteilt.
- Die vom Zwei-Faktor-Modell mit CPI- und Beschäftigungsüberraschung implizierte Korrelationsmatrix der 13 Überschussrenditen liegt sehr nahe an der Einheitsmatrix. Die Korrelation der Residuen dieses Modells liegt nahe an der Korrelation der ursprünglichen Überschussrenditen.
- Im BARRA-Branchenmodell sind die modellbasierten Korrelationen innerhalb einer Branche größer als die Stichprobenkorrelationen. Zwischen Caterpillar und Procter & Gamble beträgt die Stichprobenkorrelation nur 0,1, die Korrelation aus dem angepassten Modell 0,6.
- Für die Korrelationsmatrix der fünf Monatsrenditen von IBM, Hewlett-Packard, Intel, J.P. Morgan Chase und Bank of America sind die Eigenwerte 2,607, 1,072, 0,569, 0,451 und 0,301, die Anteile 0,522, 0,214, 0,114, 0,090 und 0,060 und die kumulierten Anteile 0,522, 0,736, 0,850, 0,940 und 1. Der Text rundet den ersten Eigenwert auf 2,608 und den gemeinsamen Anteil der ersten beiden Komponenten auf etwa 74 Prozent; die Tabelle weist für diese beiden 0,736 aus.
- Der erste Eigenvektor der Korrelationsmatrix ist ungefähr (0,428, 0,460, 0,451, 0,479, 0,416)′ und wird als Marktkomponente gelesen. Der zweite ist ungefähr (0,341, 0,356, 0,385, −0,469, −0,623)′ und trennt Technologie von Finanzwerten.
- Für die Tageslogrenditen von Hang Seng und Nikkei 225 schätzt das diagonale Constant-Correlation-GARCH(1,1) die Korrelation auf 0,668. Die Volatilitäten der beiden Märkte sind nicht dynamisch gekoppelt, aber zeitgleich korreliert.
- Für die monatlichen Logrenditen von IBM und dem S&P 500, Januar 1926 bis Dezember 1999, ist die konstante Korrelation 0,614 bei einem Standardfehler von 0,020. Die Volatilitäten zeigen eine Feedback-Beziehung.
- Im DVEC(1,1) für die monatlichen Renditen von Pfizer und Merck, Januar 1965 bis Dezember 2008, liegen die zeitvariablen Korrelationen zwischen 0,37 und 0,83. Im BEKK(1,1) derselben Reihe wirken die Korrelationen volatiler.
- Die Stichprobenkorrelation der monatlichen Logrenditen von IBM und dem S&P 500, gerechnet in einem Fenster von 120 Monaten, verändert sich von 1926 bis 1999 und fällt in den jüngeren Jahren. Eine über etwa 70 Jahre konstante Korrelation ist schwer zu halten, weil der S&P 500 ein gewichtetes Mittel ist und sich der Rang der IBM-Marktkapitalisierung verändert hat.
- Im logistischen Modell schwankt die angepasste Korrelation und wird in den jüngeren Jahren kleiner, im Einklang mit dem gleitenden Fenster. Ihr Mittel ist 0,612 gegenüber dem konstanten Schätzwert 0,614. Die Log-Likelihood verbessert sich von minus 3691,21 auf minus 3679,64. Die Ein-Schritt-Prognose der Korrelation am Ursprung 888 ist 0,545, gegenüber 0,614 im konstanten Modell.
- Die Cholesky-Korrelation derselben Reihe ist glatter, fällt ebenfalls und liegt in den jüngeren Jahren unter den anderen Modellen. Die Ein-Schritt-Prognose am Ursprung 888 hat die Korrelation 0,203. Die Likelihood von etwa minus 3672 ist mit dem logistischen Modell vergleichbar. Der AR-Koeffizient von q21,t ist 0,9915.
- Die Stichprobenkorrelationen der Tageslogrenditen, 2. Januar 1991 bis 31. Dezember 1999, sind 0,52 zwischen S&P 500 und Cisco, 0,50 zwischen S&P 500 und Intel und 0,47 zwischen Cisco und Intel.
- In diesem dreidimensionalen Modell steigt die Korrelation zweier Renditereihen, wenn die Renditen volatil sind. Das stimmt mit dem Befund überein, dass die Korrelation internationaler Aktienmarktindizes in einer Finanzkrise zunimmt. Die Größen qij,t haben hohe AR(1)-Koeffizienten: 0,790 schon im bivariaten Cisco-Modell und 0,824, 0,973 und 0,981 im dreidimensionalen Modell.
- Im Vier-Asset-DCC von Euro, Yen, IBM und Dell, Januar 1999 bis Dezember 2004, sind die Korrelationen des Modells glatter als die einer rollierenden Schätzung mit 69 Tagen.
- Ohne Leverage liegen die übrigen Posterior-Mittel nahe bei denen mit Leverage: σo 0,0775 gegen 0,0764, α −0,0613 gegen −0,0616 und ση 2,5827 gegen 2,5639; die beiden geschätzten Volatilitätsreihen sind sehr nah beieinander.
- 1970 bis 2004 betragen die Korrelationen USA/Deutschland gesamt 0,45, Abwärts 0,55, Aufwärts 0,18 und gemischt minus 0,62.
- 1995 bis 2004 liegen die Aufwärts- und Abwärtskorrelationen bei USA/Deutschland 0,44 und 0,67, bei USA/Japan 0,31 und 0,24, bei USA/Großbritannien 0,36 und 0,58, bei Deutschland/Großbritannien 0,54 und 0,71, bei Deutschland/Japan 0,05 und 0,06 und bei Großbritannien/Japan 0,07 und 0,35.
- Der Text schließt, Abwärtskorrelationen lägen stets über Aufwärtskorrelationen. In der Tabelle 1995 bis 2004 ist USA/Japan die Ausnahme: Aufwärts 0,31 gegen Abwärts 0,24.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Advances in Financial Machine Learning.pdf, S. 248–267 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-014-p248-p267|S. 248–267]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 39–58 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-003-p039-p058|S. 39–58]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 58–77 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-004-p058-p077|S. 58–77]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 77–96 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-005-p077-p096|S. 77–96]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 115–134 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-007-p115-p134|S. 115–134]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 210–229 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-012-p210-p229|S. 210–229]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 248–267 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-014-p248-p267|S. 248–267]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 267–286 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-015-p267-p286|S. 267–286]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 286–305 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-016-p286-p305|S. 286–305]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 305–324 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-017-p305-p324|S. 305–324]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 324–343 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-018-p324-p343|S. 324–343]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 343–362 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-019-p343-p362|S. 343–362]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 419–438 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-023-p419-p438|S. 419–438]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 457–476 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-025-p457-p476|S. 457–476]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 476–495 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-026-p476-p495|S. 476–495]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 138–143 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-010-p138-p143|S. 138–143]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 144–163 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-011-p144-p163|S. 144–163]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 163–165 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-012-p163-p165|S. 163–165]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 39–58 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-003-p039-p058|S. 39–58]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 58–77 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-004-p058-p077|S. 58–77]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 115–134 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-007-p115-p134|S. 115–134]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 248–267 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-014-p248-p267|S. 248–267]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 324–343 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-018-p324-p343|S. 324–343]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 343–362 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-019-p343-p362|S. 343–362]]
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
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 628–647 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-034-p628-p647|S. 628–647]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 666–685 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-036-p666-p685|S. 666–685]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 685–704 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-037-p685-p704|S. 685–704]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 210–229 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-012-p210-p229|S. 210–229]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 229–248 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-013-p229-p248|S. 229–248]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 267–286 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-015-p267-p286|S. 267–286]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 286–305 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-016-p286-p305|S. 286–305]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 419–438 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-023-p419-p438|S. 419–438]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 438–457 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-024-p438-p457|S. 438–457]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 457–476 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-025-p457-p476|S. 457–476]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 533–552 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-029-p533-p552|S. 533–552]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 552–571 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-030-p552-p571|S. 552–571]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 609–628 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-033-p609-p628|S. 609–628]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 97–116 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-009-p097-p116|S. 97–116]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 159–178 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-013-p159-p178|S. 159–178]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 178–197 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-014-p178-p197|S. 178–197]]

## Verwandte Themen
