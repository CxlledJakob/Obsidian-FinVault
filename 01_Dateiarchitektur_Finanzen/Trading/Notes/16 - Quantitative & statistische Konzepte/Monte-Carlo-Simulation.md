---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Modelle"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Monte-Carlo-Simulation


## Kurzdefinition

- Die numerische Bestimmung der Handelsregel zieht sehr viele künstliche Gewinnpfade aus den geschätzten Prozessparametern.
- Die Monte-Carlo-Simulation vergleicht hier die Performance von Hierarchical Risk Parity, dem Minimum-Varianz-Portfolio des Critical Line Algorithm und dem Inverse-Varianz-Portfolio außer Stichprobe.
- Snippet 16.5 setzt Monte-Carlo-Experimente für Hierarchical Risk Parity, den Critical Line Algorithm und das Inverse-Varianz-Portfolio um.
- Die Monte-Carlo-Permutation ist nach dem bekannten europäischen Spielkasino benannt, weil sie den Computer wie ein Roulette verwendet.
- Die Monte-Carlo-Simulation, von Stanislaw Ulam (1909 bis 1984) eingeführt, löst mathematische Probleme durch zufälliges Ziehen von Stichproben.
- Die Monte-Carlo-Permutation zum Prüfen von Regeln stammt von Timothy Masters; er schlug sie als Erster vor, um die Stichprobenverteilung der gebacktesteten Regelleistung zu erzeugen, als Alternative zu Whites Reality Check.
- MCMC-Verfahren gewinnen die Verteilung P(θ|X), indem sie einen Markov-Prozess auf dem Parameterraum simulieren, dessen stationäre Übergangsverteilung gleich P(θ|X) ist.

## Kernaussagen

- Alle mittleren Portfoliorenditen außer Stichprobe liegen im Wesentlichen bei 0.
- Die Varianzen der Renditen außer Stichprobe betragen 0,1157 für CLA, 0,0928 für das Inverse-Varianz-Portfolio und 0,0671 für Hierarchical Risk Parity.
- CLA hat die höchste Varianz außer Stichprobe, 72,47 Prozent über Hierarchical Risk Parity, obwohl minimale Varianz sein Optimierungsziel ist.
- Diese höhere Out-of-Sample-Varianz von CLA entspricht der historischen Evidenz von De Miguel und Koautoren (2009).
- Hierarchical Risk Parity würde die Sharpe-Ratio einer CLA-Strategie außer Stichprobe um etwa 31,3 Prozent verbessern.
- Die Varianz des Inverse-Varianz-Portfolios liegt noch 38,24 Prozent über Hierarchical Risk Parity.
- Der mathematische Beweis dieser Überlegenheit liegt außerhalb des Kapitels.
- Andere Parameterkonfigurationen führen zu ähnlichen Schlüssen, und die Überlegenheit wird bei größerem Universum, mehr Schocks, stärkerer Korrelation oder Rebalancing-Kosten noch deutlicher.
- Chu, Stinchcombe und White leiten per Monte Carlo die Konstante b bei Alpha 0,05 gleich 4,6 ab, die in den kritischen Wert ihres einseitigen CUSUM-Tests auf Niveaus eingeht.
- Monte-Carlo-Simulationen waren zuvor übergangen worden und werden hier als allgemeine Technik eingesetzt.
- Mit simulierten statt historischen Daten wird die statistische Signifikanz eines Backtests geprüft.
- Dieselben Simulationen dienen dazu, das Tail Risk einer Strategie einzuschätzen.
- Lässt sich keine analytische Lösung für den optimalen Hebel ableiten, helfen Monte-Carlo-Simulationen.
- Für Verteilungen mit endlich vielen Momenten folgt aus Thorps Herleitung ein anderer optimaler Hebel als die einfache Kelly-Formel; die Pareto-Levy-Verteilung hat nicht endlich viele Momente.
- Für manche Verteilungen gibt es gar keine analytische Antwort.
- Bei Fat Tails empfehlen die Key Points Monte Carlo statt der Kelly-Formel, um die Wachstumsrate zu optimieren.
- Das folgende Kapitel stellt zwei computergestützte Verfahren vor, Bootstrap-Resampling und Monte-Carlo-Permutation. Jedes hat Grenzen, beide sind aber nützliche Alternativen zum klassischen Ansatz, die Stichprobenverteilung aus einer einzigen Stichprobe abzuleiten.
- Es gibt zwei computergestützte Wege zur Stichprobenverteilung: Monte-Carlo-Permutation und Bootstrap. Beide werden in der Fallstudie von Teil 2 verwendet.
- Der Autor verwendet die Computersimulation, weil der klassische Ansatz eine normale Stichprobenverteilung voraussetzt und die Schlüsse ungenau werden, wenn diese Form nicht zutrifft.
- Womit die Verteilung auch erzeugt wird, sie sagt, wie weit die gebacktestete Rendite einer nicht vorhersagenden Regel zufallsbedingt über oder unter null schwanken kann, und sie ist der Maßstab, an dem Vorhersagekraft beurteilt wird.
- Die Monte-Carlo-Methode war lange bekannt, aber zuvor nicht auf Regeltests angewandt; Masters' Einsicht war, dass sie die Stichprobenverteilung einer Regel ohne Vorhersagekraft erzeugen kann.
- Die Null besagt, die Renditen der geprüften Regel seien eine Stichprobe aus einer Grundgesamtheit, die eine Regel ohne Vorhersagekraft erzeugt hat.
- Umgesetzt wird das, indem die Ausgaben plus 1 und minus 1 in ihrer ursprünglichen Reihenfolge zufällig mit künftigen Preisänderungen gepaart werden; die Ausgabe ist dann uninformatives Rauschen.
- Die Zufallspaarung zerstört jede Vorhersagekraft der Regel; der Text nennt das Ergebnis eine Rauschregel.
- Gezogen wird ohne Zurücklegen, anders als beim Bootstrap.
- Gebraucht werden die tägliche Reihe der Regelausgaben und die tägliche Reihe der Preisänderungen, nicht nur die Regelrenditen.
- Die Permutationsmethode ist gemeinfrei, während der für Regeltests geeignete Bootstrap nur von Quantmetrics kommt.
- Bootstrap und Monte-Carlo-Permutation können wegen ihrer verschiedenen Stichprobenverteilungen verschieden über die Null entscheiden; auf trendbereinigten Daten stimmen sie nach Masters' Simulationen in der Regel überein, und dieses Buch nutzt für beide solche Daten.
- Die Monte-Carlo-Permutation kann keine Konfidenzintervalle erzeugen.
- Die Monte-Carlo-Permutation hat mit dem Schätzen eines Populationsparameters oder mit dem Prüfen einer Behauptung über dessen Wert nichts zu tun und kann deshalb keine Konfidenzintervalle erzeugen.
- Ihre Nullhypothese besagt, dass die von der Regel diktierten langen und kurzen Positionen keine nützliche Information über künftige Marktänderungen enthalten.
- Weil kein Populationsparameter wie die mittlere Regelrendite vorkommt, gibt es nichts, worum ein Konfidenzintervall zu legen wäre.
- Ein Ansatz gegen den Data-Mining-Bias beruht auf Randomisierungsmethoden wie Bootstrap und Monte Carlo und wurde außerhalb der akademischen Literatur wenig diskutiert.
- Er erlaubt, so viele Regeln zu testen wie gewünscht, und eine größere Regelzahl erhöht die Chance, überlegene Regeln zu finden.
- Er verlangt nicht, Daten zurückzuhalten, sodass die gesamte verfügbare Historie für das Data Mining genutzt werden kann.
- Er erlaubt Signifikanztests und manchmal näherungsweise Konfidenzintervalle.
- Kapitel 5 führte Bootstrap und Monte-Carlo-Permutation ein; dort galten die Tests nur für eine einzelne Regel ohne Data Mining, mit den hier beschriebenen Änderungen auch für eine durch Data Mining gefundene Regel.
- Welche Informationen über jede getestete Regel aufbewahrt werden müssen, hängt davon ab, ob Monte Carlo oder Bootstrap benutzt wird.
- Die Fallstudie illustriert zwei Verfahren, die den Data-Mining-Bias berücksichtigen: eine erweiterte Fassung von Whites Reality Check und Masters Monte-Carlo-Permutationsmethode.
- Beide nutzen eine jüngere Verbesserung, die die Wahrscheinlichkeit senkt, eine gute Regel zu übersehen, den Fehler zweiter Art, und damit die Power der Tests erhöht.
- Die Nullhypothese der Monte-Carlo-Permutation lautet, alle betrachteten Regeln hätten ihre Long- und Short-Positionen auf zufällige Weise erzeugt.
- Long und Short werden zufällig mit der Ein-Tages-Vorwärts-Preisänderung des Marktes permutiert.
- Die Alternativhypothese von Masters lautet, die gebacktestete Profitabilität einer Regel sei das Ergebnis einer informativen Paarung ihrer Long- und Short-Positionen mit der Ein-Tages-Vorwärts-Preisänderung des Marktes. Mit anderen Worten hat die Regel Vorhersagekraft.
- Um die passende Stichprobenverteilung zu konstruieren, muss die Information über jede getestete Regel verfügbar sein. Fehlt sie, lässt sich die statistische Signifikanz nicht richtig beurteilen.
- Neben White’s Reality Check wurde die Monte-Carlo-Permutation verwendet, um Regeln zu bewerten, die durch Data Mining gefunden wurden, weil herkömmliche Signifikanztests den Data-Mining-Bias nicht berücksichtigen.
- Figur 9.2 legt die beste Regel E-12-28-10-30 auf die Stichprobenverteilung der Monte-Carlo-Permutation und weist den p-Wert 0,8194 aus.
- Auch diese Verteilung gehört zur besten von 6.402 wertlosen Regeln und zentriert bei etwa 11 Prozent mittlerer Rendite.
- Die annualisierte Rendite von 10,25 Prozent liegt unter diesem Zentrum und reicht nicht, die Nullhypothese bei 0,05 abzulehnen.
- Das Zentrum bei etwa 11 Prozent ist eine Folge des konkreten Satzes von 6.402 Regeln, ihrer Renditekorrelationen, der Beobachtungszahl und des verwendeten S&P-Datensatzes und nicht der Erwartungswert einer einzelnen Regel.
- MC ist die Monte-Carlo-Permutationsmethode, die Masters entwickelte, und sie übernimmt die Erweiterung von Wolf und Romano.
- Figur 9.2 zeigt die Stichprobenverteilung für die beste von 6.402 wertlosen Regeln unter der Monte-Carlo-Permutation.
- Die Spalte SR MC in Tabelle 9.1 ist der Einzelregel-p-Wert per Monte Carlo und rechnet den Data-Mining-Bias nicht ein.
- Die Spalte MC Sig prüft die Signifikanz auf dem Niveau 0,05 mit der Monte-Carlo-Permutation, die den Data-Mining-Bias berücksichtigt; keine Regel erhielt ein Sternchen.
- White’s Reality Check und die Monte-Carlo-Permutation zeigten beide, dass die beste der 6.402 getesteten Regeln nicht statistisch signifikant war.
- RC bezeichnet die bei Quantmetrics verfügbare Reality-Check-Fassung ohne die Wolf-Romano-Erweiterung, während MC diese Erweiterung enthält.
- Monte-Carlo-Simulationen waren eine zuvor übersehene allgemeine Technik.
- Wo der optimale Hebel bei einer nichtgaußschen Verteilung keine analytische Lösung hat, wird der Erwartungswert von log(1 plus f mal R) über Zufallsziehungen der ungehebelten Strategierendite je Bar maximiert, bei risikofreiem Zins null.
- Das Pearson-System baut die Verteilung aus den ersten vier Momenten als eine von sieben analytischen Formen, darunter Gauß, Beta, Gamma und Student-t; unendliche höhere Momente wie bei der Pareto-Levy-Verteilung bleiben draußen, weil ihre Schätzung Data-Snooping einlädt.
- Für die Mean-Reversion-Strategie aus Beispiel 5.1 ist der Kelly-Hebel 18,4. Aus den Tagesrenditen werden 100.000 Zufallsrenditen gezogen; der Verteilungstyp 4 ist keine Standardform wie die Student-t.
- g(f) von 0 bis 23 hat ein Maximum nahe 19, und die numerische Optimierung liefert den Hebel 19, nahe an 18,4. Ein anderer Zufallsstart kann einen etwas anderen Wert liefern.
- MATLAB hat kein fmaxbnd, deshalb wird das Negative der Wachstumsrate minimiert.
- Bei Hebel 31 ist die Wachstumsrate minus 1, also Ruin, weil die negativste Periodenrendite minus 0,0331 beträgt und jeder Hebel über 30,2 in dieser Periode zum Totalverlust führt.
- Die Optimierung auf den historischen statt den simulierten Renditen trifft ebenfalls 18,4, leidet aber am Data-Snooping-Bias und hat zu wenig Daten für viele Realisationen.
- Der maximale Drawdown der simulierten Reihe beim Hebel 19,2 ist minus 0,999. Simulierte Reihen haben höhere Signifikanz, ähnlich dem Value-at-Risk, können einen in einer Million Jahren kaum eintretenden Drawdown zeigen und verfehlen serielle Korrelationen.
- CPPI auf derselben Reihe über 100.000 Tage ergibt bei D gleich 0,5 eine tägliche Wachstumsrate von 0,002484 gegen 0,002525 beim Hebel f mal D; der CPPI-Drawdown bleibt unter 0,5, der alternative ohne Stop-Loss erreicht 0,9.
- Zur Schätzung eines stochastischen Volatilitätsmodells dient eine Quasi-Likelihood über Kalman-Filterung oder eine Monte-Carlo-Methode.
- Jacquier, Polson und Rossi (1994) vergleichen Quasi-Likelihood und Markov-Chain-Monte-Carlo bei stochastischen Volatilitätsmodellen. Eine MCMC-Schätzung wird in Kapitel 12 behandelt.
- Carlin, Polson und Stoffer (1992) schlagen einen Monte-Carlo-Zugang für nichtlineare Zustandsraummodelle vor, weil für ein nichtlineares System die gesamte bedingte Verteilung des Zustands gegeben dem Vorzustand gebraucht wird.
- McCulloch und Tsay (1994) schätzen ein allgemeines Markov-Switching-Modell mit Markov-Chain-Monte-Carlo. Die Ergebnisse für das US-GNP sind Posterior-Mittel und Posterior-Standardabweichungen eines Gibbs-Samplers mit 5000 Iterationen.
- Hamilton (1990) schätzt das Markov-Switching-Modell mit dem EM-Algorithmus, der zwischen Erwartungswertbildung und Maximierung iteriert. MCMC-Verfahren werden in Kapitel 12 behandelt.
- MCMC-Verfahren sind starke Werkzeuge für nichtlineare Zeitreihen. Ihr Potenzial ist noch nicht ausgeschöpft. Die Annahme, dass die Funktionen f_t und g_t des Zustandsraummodells bekannt sind, kann den praktischen Einsatz begrenzen.
- Montgomery et al. (1998) schätzen das Markov-Switching-Modell der Änderung der US-Arbeitslosenquote mit einem Markov-Chain-Monte-Carlo-Verfahren.
- Kritische Werte der Schwellen-Statistik l_max werden oft per Simulation gewonnen, weil die Schwelle unter der linearen Null ein störender Parameter ist; diese kritischen Werte hängen von den vorgegebenen Schranken v und u ab.
- Ein Simulationsvergleich lässt das 8–4–1-Feed-forward-Netz 500-mal laufen und zählt die Fehler bei der Richtungsprognose der monatlichen IBM-Logrenditen von Januar 1998 bis Dezember 1999.
- Über diese 500 Läufe sind Mittel und Median der Fehlerzahl 11,28 und 11, das Maximum 18 und das Minimum 4.
- Dieselbe Simulation mit einem Random Walk mit Drift, Aufwärtsbewegung wenn 1,19 + ε_t ≥ 0 mit ε_t iid N(0, 1), ergibt Mittel 10,53, Median 11, Maximum 17 und Minimum 5.
- Der Vergleich zeigt, dass das 8–4–1-Netz das einfache Modell eines Random Walk mit Drift für den monatlichen IBM-Logpreis nicht schlägt.
- Die Parameter des Ordered-Probit-Modells, also β, die Schwellen α_i und die Parameter der bedingten Varianz, lassen sich per Maximum-Likelihood oder per Markov-Chain-Monte-Carlo schätzen.
- Zur Illustration werden 500 Beobachtungen aus dem ACD(1,1) ψ_i = 0,3 + 0,2 x_{i−1} + 0,7 ψ_{i−1} erzeugt, mit x_i = ψ_i ε_i.
- Im ersten Fall folgt ε_i einer standardisierten Weibull-Verteilung mit Parameter α = 1,5, im zweiten einer standardisierten verallgemeinerten Gamma-Verteilung mit κ = 1,5 und α = 0,5.
- Die Histogramme der beiden simulierten Dauerreihen unterscheiden sich deutlich, und beide Stichproben-Autokorrelationen zeigen die serielle Abhängigkeit.
- Die sechs bedingten PCD-Modelle lassen sich gemeinsam per Maximum Likelihood oder per Markov-Chain-Monte-Carlo schätzen und wegen der Zerlegung der gemeinsamen Dichte auch getrennt.
- Für die 194 Preisänderungen von IBM am 21. November 1990 sind die berichteten Schätzungen Posterior-Mittel und Posterior-Standardabweichungen aus MCMC-Ziehungen mit 9500 Iterationen.
- Ist ein Dauer-Modell spezifiziert, kann Simulation die Referenzverteilung endlicher Stichproben für die interessierende Fragestellung liefern.
- Die kritischen Werte der Johansen-Statistiken LRtr(m) und LRmax(m) werden durch Simulation bestimmt, weil ihre asymptotische Verteilung wegen der Unit Roots eine Funktion von Standard-Brownschen Bewegungen ist.
- MCMC und Data Augmentation ermöglichen Inferenz, die wenige Jahre zuvor nicht durchführbar war, und sind auf die meisten, wenn nicht alle, Studien der Finanzökonometrie anwendbar.
- Der EM-Algorithmus von Dempster, Laird und Rubin (1977) schätzt im M-Schritt per Maximum-Likelihood und füllt im E-Schritt den fehlenden Wert durch seinen bedingten Erwartungswert, iteriert von einem beliebigen Start bis zur Konvergenz.
- Tanner und Wong (1987) ersetzen den bedingten Erwartungswert durch eine Zufallsziehung und erweitern das Verfahren durch Data Augmentation, also Hilfsvariablen.
- Ein fehlender Datenpunkt und eine unbeobachtbare Größe wie der wahre Preis gelten als Parameter; bei N Transaktionspreisen sind das N Parameter.
- Ein fehlender Wert in täglichen Renditen widerspricht der Annahme vollständiger Daten, unter der die meisten Verfahren des Buches entwickelt wurden.
- Prognosen im MCMC-Rahmen entstehen, indem das in jeder Gibbs-Iteration angepasste Modell Realisationen für den Prognosezeitraum simuliert.
- Von M + N Gibbs-Iterationen werden nur die letzten N für die Prognose verwendet; die Stichprobenmittel sind die Punktprognosen von Rendite und Volatilität, und die Stichproben-Standardabweichungen dienen als Varianzen der Prognosefehler.
- Die Effizienz der Volatilitätsprognose lässt sich mit Importance Sampling steigern, siehe Gelman, Carlin, Stern und Rubin (2003).
- Montier baut ein künstliches Universum aus 100 Fondsmanagern, jeder mit einem wahren Alpha von 3 Prozent und einem Tracking Error von 6 Prozent, und trifft sie mit zufälligen Schocks über 50 Jahre.
- Nach 50 Jahren zeigt der beste Manager ein Alpha von 5,2 Prozent und der schlechteste eines von 1 Prozent. In der Kapitelankündigung sind dieselben Enden auf 5 und 1 Prozent gerundet.
- An den Jahresrenditen ist kaum zu erkennen, wer der gute und wer der schlechte Manager ist, obwohl jeder per Konstruktion dasselbe wahre Alpha von 3 Prozent hat.
- Laut Ehlers ist die Monte-Carlo-Analyse der beste und verlässlichste Weg, die Performance einer Handelsstrategie zu beurteilen.
- Die Monte-Carlo-Analyse ist nach Ehlers der beste und verlässlichste Weg, die Performance einer Handelsstrategie zu beurteilen, sofern man programmieren kann; die Rechnungen sind relativ einfach.
- Zufall lässt sich nur in dem Sinn einführen, dass Gewinn oder Verlust je Trade über Trefferquote und Zufallszahl bestimmt und die Auszahlung zugewiesen wird; Gewinnen oder Verlieren an sich ist kein zufälliges Ereignis.

## Funktionsweise

- Im Beispiel werden 100000 Pfade erzeugt.
- Startwerte sind der beobachtete Einstiegspreis und die Prognose der jeweiligen Gelegenheit.
- Jeder Schritt setzt den Prozess mit einem unabhängigen standardnormalen Schock fort, skaliert mit Sigma.
- Dieselben Pfade werden auf jeden Knoten eines Gitters aus Stop und Gewinnziel gelegt.
- Jeder Gitterknoten liefert aus den auf ihm ausgewerteten Pfaden eine Sharpe Ratio.
- In den berichteten Simulationen wird Sigma auf 1 gesetzt.
- Der Einstiegspreis wird auf 0 gesetzt, weil allein die Distanz zur Prognose die Konvergenz treibt.
- Ein Pfad endet beim ersten Erreichen von Gewinnziel, Stop oder maximaler Haltedauer.
- Erzeugt werden zehn Reihen zufälliger Gauß-Renditen mit 520 Beobachtungen, Mittelwert 0 und einer willkürlichen Standardabweichung von 10 Prozent, entsprechend zwei Jahren Tagesdaten.
- Weil reale Preise häufig springen und Renditen nicht querschnittlich unabhängig sind, kommen zufällige Schocks und eine zufällige Korrelationsstruktur hinzu.
- Die Portfolios werden auf 260 Beobachtungen geschätzt, also ein Jahr, und alle 22 Beobachtungen neu geschätzt und rebalanciert, also monatlich.
- Der Ablauf wird 10.000-mal wiederholt.
- Die Datenerzeugung simuliert korrelierte Reihen mit zwei Schockarten, gemeinsam für mehrere Anlagen und spezifisch für eine Anlage.
- Von jeder Schockart gibt es einen positiven und einen negativen Schock.
- Die Argumente von hrpMC sind willkürlich gewählt: 10.000 Iterationen, 520 Beobachtungen, je fünf unkorrelierte und fünf korrelierte Reihen, Mittelwert 0, Sigma 0,01, sigma1F 0,25, Rückblick 260 und Rebalancing alle 22 Beobachtungen.
- Je Iterationsschritt werden die Portfolios auf dem Rückblickfenster geschätzt und die folgende Rebalancing-Strecke bewertet.
- Gespeichert wird die kumulierte Rendite am Pfadende minus eins, berichtet werden Standardabweichung, Varianz und die Varianz im Verhältnis zu Hierarchical Risk Parity.
- Monte Carlo erzeugt simulierte historische Preisdaten und speist sie in die Strategie, um die empirische Verteilung der Gewinne zu bestimmen.
- Die Annahme ist, dass die Profitabilität subtile Muster oder Korrelationen der Preisreihe erfasst und nicht nur die ersten Momente der Preisverteilungen.
- Erzeugt werden viele simulierte Preisreihen mit denselben ersten Momenten und derselben Länge wie die echten Daten. Der Anteil p, in dem die durchschnittlichen Renditen mindestens die Backtest-Rendite erreichen, soll klein sein, damit die Null verworfen werden kann. Sonst kann die durchschnittliche Rendite allein an den Marktrenditen liegen.
- Die simulierten Tagesrenditen werden so gezogen, dass Mittelwert, Standardabweichung, Schiefe und Kurtosis den beobachteten Futures-Renditen entsprechen, die eingebetteten Korrelationen aber nicht. In MATLAB dient dafür pearsrnd aus der Statistics Toolbox.
- Aus den simulierten Renditen wird eine Preisreihe als kumuliertes Produkt aus eins plus Rendite, minus eins, gebaut. Long ist der simulierte Kurs über seinem um die Lookback-Spanne verschobenen Wert, Short darunter. Das wird 10.000-mal wiederholt.
- g(f) ist der Durchschnitt von log(1 plus f mal R) über Zufallsziehungen der ungehebelten Bar-Rendite R.
- Die unbekannte Verteilung von R wird mit dem Pearson-System aus Mittelwert, Standardabweichung, Schiefe und Kurtosis als eine von sieben analytischen Verteilungen modelliert, darunter Gauß, Beta, Gamma und Students t.
- Im Beispiel der Mean-Reversion-Strategie aus Beispiel 5.1 erzeugt pearsrnd 100.000 Zufallsrenditen aus den ersten vier Momenten; der Code steht in monteCarloOptimLeverage.m.
- Der zurückgegebene Typ war 4, also keine Standardverteilung wie Students t.
- g ist die Summe von log(1 plus f mal R) geteilt durch die Länge von R; das Maximum wird über die Minimierung von minus g mit fminbnd zwischen 0 und 24 gesucht, weil MATLAB kein fmaxbnd hat.
- Die trendbereinigten Preisänderungen eines Tages liegen in einem Behälter, werden ohne Zurücklegen mit den Regelausgaben gepaart, und jede Rendite ist das Produkt aus Ausgabe und der Preisänderung einen Tag voraus.
- Der Mittelwert dieser Renditen ist ein permutierter Mittelwert; das wird viele Male wiederholt, im Beispiel 5.000 Mal, und aus diesen Mittelwerten entsteht die Stichprobenverteilung der mittleren Rendite einer Rauschregel.
- Der p-Wert ist der Anteil der Zufallsregel-Renditen, die die Rendite der geprüften Regel erreichen oder übertreffen.
- Die Performancehistorien der künstlichen Handelsregeln wurden per Monte-Carlo-Simulation erzeugt.
- Die absoluten monatlichen Änderungen des S&P 500 wurden mit Zurücklegen aus der rund 900 Monate langen Historie von August 1928 bis April 2003 gezogen.
- Ein Monat ohne Vorzeichen wurde zufällig gewählt, und ein per Computer simuliertes Roulette entschied Gewinn oder Verlust; die Wahrscheinlichkeit setzte der Experimentator, 0,70 entspricht 70 Gewinn- und 30 Verlustfächern von 100.
- Das Verfahren wurde für eine festgelegte, ebenfalls gesteuerte Zahl von Monaten wiederholt, und die Historie wurde als annualisierte mittlere Monatsrendite zusammengefasst.
- Die Monte-Carlo-Permutation erzeugt die Stichprobenverteilung für die statistische Signifikanz von Regeln, die durch Data Mining gefunden wurden; sie nutzt andere Daten als der Bootstrap und testet eine andere Formulierung der Nullhypothese.
- Sie verwendet die historische Zeitreihe der Regelausgaben, also +1 und −1, sowie die rohen Marktrenditen, während der Bootstrap die Intervallrenditen der Regel verwendet.
- Um eine Regel ohne Prognosekraft zu simulieren, paart sie die Regelausgaben zufällig mit den täglichen Marktpreisänderungen, und zwar ohne Zurücklegen.
- Die Rendite einer Paarung ist der Regelwert mal der diesem Tag zufällig zugeordneten Marktänderung: +1 an einem Aufwärtstag verdient die Marktänderung, −1 an einem Abwärtstag verdient diesen positiven Betrag, und Verluste entstehen, wenn das Vorzeichen der Ausgabe dem der Preisänderung entgegensteht.
- Nach der Paarung der gesamten Ausgabehistorie wird für jede der N Regeln die mittlere Rendite berechnet, die maximale mittlere Rendite wird der erste Wert der Stichprobenverteilung, und der Vorgang wird viele Male mit anderen Paarungen wiederholt, mehr als 500-mal.
- Zuerst werden die täglichen Ausgabezustände aller N Regeln beschafft, dann jede Ausgabe zufällig mit einer verwürfelten Version der tatsächlichen künftigen Marktpreisänderungen gepaart, wobei dieselben Paarungen für alle Regeln gelten müssen.
- Ist die Ausgabe von Tag 7 mit der Marktrendite von Tag 15 gekoppelt, muss dieselbe Kopplung für alle konkurrierenden Regeln gelten, damit die Korrelationsstruktur erhalten bleibt.
- Aus den N mittleren Renditen wird die höchste gewählt; die Schritte werden M-mal wiederholt, wobei M gleich 500 oder eine große Zahl ist, und aus den M Höchstwerten entsteht die Stichprobenverteilung der besten mittleren Rendite unter N nutzlosen Regeln.
- Anders als bei White's Reality Check muss die Renditeverteilung nicht auf null zentriert werden, weil die Null hier nicht lautet, alle Regeln hätten die erwartete Rendite null.
- Der Mittelwert der so erzeugten Stichprobenverteilung ist die erwartete Rendite einer nutzlosen Regel in einem Data-Mining-Vorhaben; liegt sie nach der Zufallszuordnung über null, bleibt das so.
- Der p-Wert ist die Fläche im rechten Rand bei oder jenseits der mittleren Rendite der gebacktesteten Regel, gleich dem Anteil der M Werte, die größer oder gleich dieser mittleren Rendite sind.
- Zur Schätzung der Nullverteilung werden viele simulierte Preisreihen mit denselben ersten Momenten und derselben Länge wie die echten Daten erzeugt und durch die Strategie geschickt; p ist der Anteil, in dem die Durchschnittsrendite mindestens die Backtest-Rendite erreicht.
- Ein dritter Weg nach Lo, Mamaysky und Wang 2000 randomisiert die Einstiege auf der echten Preisreihe bei gleicher Zahl von Long- und Short-Trades und gleicher mittlerer Haltedauer.
- Ein Prozess {Xt} ist ein Markov-Prozess, wenn gegeben Xt die künftigen Xh, h > t, nicht von den früheren Xs, s < t, abhängen: P(Xh | Xs, s ≤ t) = P(Xh | Xt).
- In diskreter Zeit gilt P(Xh | Xt, Xt−1, …) = P(Xh | Xt); die Übergangswahrscheinlichkeit ist Pt(θ, h, A) = P(Xh ∈ A | Xt = θ).
- Die Simulation muss lang genug laufen, damit die Verteilung der aktuellen Werte nahe an der stationären Übergangsverteilung liegt; zu einem gegebenen P(θ|X) lassen sich viele solche Ketten bauen.
- Gibbs-Sampling nach Geman und Geman (1984) und Gelfand und Smith (1990) ist das wohl verbreitetste MCMC-Verfahren und zerlegt ein hochdimensionales Problem in volle bedingte Verteilungen.
- Im Dreiparameterfall wird nacheinander aus f1(θ1 | θ2, θ3, X, M), f2(θ2 | θ3, θ1, X, M) und f3(θ3 | θ1, θ2, X, M) gezogen; nötig ist nur die Fähigkeit, aus jeder bedingten Verteilung zu ziehen, nicht ihre geschlossene Form.
- Unter schwachen Regularitätsbedingungen ist (θ1,m, θ2,m, θ3,m) für großes m näherungsweise eine Ziehung aus der gemeinsamen Verteilung; von jedem Startwert aus müssen die Iterationen den ganzen Parameterraum erreichen können (Tierney, 1994).
- Die ersten m Ziehungen heißen Burn-in und werden verworfen; die Gibbs-Stichprobe besteht aus den Ziehungen m+1 bis n.
- Alternativ lassen sich viele kurze Ketten mit verschiedenen Startwerten laufen, von denen jeweils nur die letzte Ziehung behalten wird.
- Ein Problem mit N Parametern lässt sich iterativ mit N univariaten bedingten Verteilungen lösen; bei hoher Korrelation ist gemeinsames Ziehen effizienter.
- Die Theorie nennt kein konkretes m; keines der Konvergenzkontrollverfahren garantiert die Konvergenz in allen Anwendungen, deshalb wird der Sampler mit verschiedenen Startwerten wiederholt (Carlin und Louis, 2000; Gelman et al., 2003).
- Der Metropolis-Algorithmus, Metropolis und Ulam (1949) sowie Metropolis et al. (1953), zieht aus einer Verteilung, deren Normierungskonstante eine direkte Ziehung verhindert, über eine symmetrische Sprungverteilung Jt(θi|θj) = Jt(θj|θi).
- Ein Kandidat θ* wird mit Wahrscheinlichkeit min(r, 1) akzeptiert, r = f(θ*|X) / f(θt−1|X); steigt die Posteriordichte, wird angenommen, sonst mit Wahrscheinlichkeit r.
- Die Normierungskonstante fällt heraus, weil nur das Verhältnis gebraucht wird; nötig sind das Verhältnis, Ziehungen aus der Sprungverteilung und eine uniforme Ziehung für Annahme oder Ablehnung.
- Symmetrische Sprungverteilungen sind unter anderem Normal- und Student-t-Verteilungen für den Mittelwert; bei fester Kovarianz ist die multivariate Normaldichte in den beiden Argumenten symmetrisch.
- Hastings (1970) lässt eine unsymmetrische Sprungverteilung zu und setzt r = [f(θ*|X) Jt(θt−1|θ*)] / [f(θt−1|X) Jt(θ*|θt−1)]; Tierney (1994) behandelt die Recheneffizienz.
- Griddy Gibbs nach Tanner (1996) wertet die univariate bedingte Posterior auf einem Gitter aus, nähert die inverse Verteilungsfunktion und transformiert eine uniforme (0,1)-Ziehung.
- Die Normierungskonstante wird nicht gebraucht; eine einfache Näherung ist die diskrete Verteilung p(θij) = wj / Summe wv.
- Zeigt das Histogramm der Ziehungen erhebliche Wahrscheinlichkeit an den Rändern des Gitters, muss das Intervall erweitert werden; ist es zu weit, sind die meisten wj null und der Sampler ineffizient.
- Griddy Gibbs oder Metropolis–Hastings können innerhalb eines Gibbs-Samplers für einzelne Parameter eingesetzt werden.
- Unter Regularitätsbedingungen konvergiert die Metropolis-Folge in Verteilung gegen f(θ|X) (Gelman et al., 2003).
- ht wird elementweise mit Griddy Gibbs gezogen; im S&P-Beispiel mit 400 Gitterpunkten, im bivariaten Modell mit 500.
- Die Spanne der j-ten Iteration ist [η1t, η2t] mit η1t = 0,6 mal max(hj−1,t, h0t) und η2t = 1,4 mal min(hj−1,t, h0t).
- Forward Filtering and Backward Sampling zieht die ganze Logvolatilität gemeinsam und nutzt dafür eine Mischung von Normalverteilungen; das senkt die Rechenzeit deutlich.
- Die Mischung aus sieben Normalverteilungen macht das Beobachtungsrauschen bedingt gaußsch, sodass der Kalman-Filter die gemeinsame Ziehung trägt.
- Konditioniert auf {zt} wird der Mischungsindikator It aus seiner Posterior gezogen und damit ct und Ht für den Filter gesetzt.
- Im univariaten stochastischen Volatilitätsmodell wird vn+1 aus N(0, σ²v,j) gezogen und die logarithmierte Varianz als ln ht = α0,j + α1,j ln ht−1 + vt mit Var(vt) = σ²v,j fortgeschrieben.
- Anschließend wird εn+1 aus N(0,1) gezogen, an+1 = √hn+1 εn+1 gesetzt und die Rendite aus rt = β0,j + β1,j x1t + … + βp,j xpt + at berechnet; beide Schritte werden für die Horizonte 2 bis ℓ wiederholt.
- Die erklärenden Variablen xjt müssen im Prognosezeitraum vorliegen oder sich der Reihe nach prognostizieren lassen.
- In der Tabellenkalkulation stehen in B1 die Trefferquote (Startwert 55) und in B2 der Profit Factor (Startwert 1,5); beide Werte gelten als repräsentativ für ein gutes System.
- In A5 erzeugt =RAND() eine gleichverteilte Zufallszahl zwischen 0 und 1. B5 enthält =IF(A4<$B$1/100,$B$2,−1): Liegt die Zufallszahl innerhalb der Gewinnwahrscheinlichkeit, erhält der Trade den Profit Factor als Auszahlung, sonst −1.
- Spalte C kumuliert die Trade-Gewinne, Spalte D zählt die Trades, Spalte E enthält =D5*(($B$2+1)*$B$1/100 −1) als kumulierten Durchschnittsgewinn; die Zeilen werden bis Zeile 504 kopiert, was 500 Trades ergibt.
- Mit F9 wird neu berechnet und eine neue zufällige Equity-Kurve erzeugt; durch Ändern von B1 und B2 lässt sich der Einfluss der Grundparameter auf den Erfolg beurteilen.

## Voraussetzungen


## Anwendung im Trading

- Ist die bedingte Verteilung der Innovation nicht gaußsch, zum Beispiel eine Student-t oder eine generalized error distribution, kann der Mehrperioden-VaR durch Simulation bestimmt werden.

## Regeln und Kriterien

- Eine erwartete APR von 10 Prozent, signifikant innerhalb von 1 Prozent, bedeutet, dass unter 10.000 simulierten Preisreihen derselben Länge und mit denselben ersten drei Momenten nur 100 eine APR von mindestens 10 Prozent haben.
- Dieselbe Aussage bedeutet alternativ, dass nur eine von 100 Permutationen der Einstiegstage eine APR von mindestens 10 Prozent erreicht.

## Risiken und Grenzen

- Andere Eingabewerte würden andere Zahlen liefern, und die gewählten Kombinationen sollen die allgemeinen Fälle abdecken.
- Fehlt in der simulierten Performance ein stabiles Muster, existiert keine optimale Handelsregel.
- Die Varianzreduktion außer Stichprobe ist für Risk-Parity-Investoren wegen ihres erheblichen Hebels entscheidend.
- Ein einzelner historischer Datensatz, in dem Hierarchical Risk Parity gewinnt, wäre wegen Selection Bias zu leicht gewählt.
- Simulierte Renditen haben deutlich bessere statistische Signifikanz und ähneln dem Value-at-Risk großer Banken und Hedgefonds.
- Ihr Nachteil ist, dass der simulierte Maximal-Drawdown seltener sein kann als einmal in einer Million Jahren und dass serielle Korrelationen der Historie fehlen.
- Die Drawdown-Schätzung dieses Abschnitts beruht auf der simulierten Strategiereihe, nicht auf den historischen Backtest-Renditen.
- Das Verfahren kann keine Konfidenzintervalle erzeugen, weil es keine Hypothese über die mittlere Rendite der Regel testet.
- Masters prüfte seine Power gemeinsam mit White's Reality Check an künstlichen Regeln beiderseits der Benchmark; bei extrem großer Varianz einer Regel mit negativer erwarteter Rendite kann die Power drastisch sinken, in wahrscheinlicheren Fällen der technischen Analyse sind beide Verfahren einigermaßen robust.
- Die Erweiterung von Romano und Wolf scheint auch die Power dieses Verfahrens zu steigern; die erweiterte Fassung wird gemeinfrei gestellt, der Code auf www.evidencebasedta.com.
- Verschiedene Nullhypothesen liefern verschiedene Signifikanzschätzungen, weil jede simulierte Verteilung die Strategie mit einem anderen Zufalls-Benchmark vergleicht.
- Gibbs-Ausreißererkennung rechnet aufwendig, schätzt aber Parameter und Ausreißer gemeinsam; das traditionelle Verfahren trennt Schätzung und Erkennung, ist schneller und kann bei mehreren Ausreißern Scheintreffer liefern.
- Ergebnis und Effizienz des Griddy Gibbs hängen von der gewählten Spanne für ht ab.
- Hohes Alpha und eine hohe Information Ratio verhindern nicht, dass fast jeder dieser Manager irgendwann in den 50 Jahren von seinen Kunden gefeuert worden wäre.

## Beispiele

- Untersucht werden die Prognosen 10, 5, 0, minus 5 und minus 10 zusammen mit den Halbwertszeiten 5, 10, 25, 50 und 100.
- Die maximale Haltedauer in diesen Simulationen beträgt 100 Beobachtungen.
- Ein idiosynkratischer Schock bestraft die Konzentration von CLA, ein Schock auf mehrere korrelierte Anlagen bestraft die ignorierte Korrelationsstruktur des Inverse-Varianz-Portfolios.
- Kolanovic und Koautoren (2017) bestätigen die Robustheit zusätzlich mit eigenen Simulationsstudien.
- Der gemeinsame Schock setzt an zwei Zeitpunkten die Werte minus 0,5 und 2 auf zwei Reihen, der spezifische Schock dieselben Werte auf eine Reihe.
- Von 10.000 Zufallsreihen haben 1.166 eine durchschnittliche Strategierendite mindestens so hoch wie die beobachtete. Die Nullhypothese wird nur mit 88 Prozent Wahrscheinlichkeit verworfen.
- Die Form der Renditeverteilung hat etwas mit dem Erfolg der Strategie zu tun. Der Mittelwert ist die weniger wahrscheinliche Ursache, weil die Position zu verschiedenen Zeiten long oder short sein kann.
- Eine erwartete APR von 10 Prozent, auf 1 Prozent statistisch signifikant, bedeutet: Von 10.000 simulierten Preisreihen mit derselben Länge und denselben ersten drei Momenten wie die historische Preisreihe haben nur 100 eine APR von mindestens 10 Prozent.
- Im zweiten Test des TU-Beispiels haben 1.166 von 10.000 Zufallsreihen eine mindestens ebenso hohe durchschnittliche Strategierendite. Die Null wird nur mit 88 Prozent Wahrscheinlichkeit verworfen.
- Die Form der Renditeverteilung hat etwas mit dem Erfolg zu tun. Jede zufällige Renditeverteilung mit hoher Kurtosis kann Momentum-Strategien begünstigen.
- Der Plot von f gleich 0 bis 23 zeigt ein Maximum nahe 19; fminbnd liefert 19, nahe dem Kelly-Wert 18,4.
- Ein anderer Zufallsstart liefert einen etwas anderen optimalen f, idealerweise nicht weit davon entfernt.
- Bei f gleich 31 ist die Wachstumsrate minus 1, weil die negativste Periodenrendite minus 0,0331 ist und jeder Hebel über 1 geteilt durch 0,0331 gleich 30,2 in dieser Periode zum Totalverlust führt.
- Dieselbe Reihe hat bei f gleich 19,2 den maximalen Drawdown minus 0,999, bei 9,6 noch minus 0,963, und bei etwa 2,7 einen Betrag von etwa 0,5.
- Nach 100.000 Tagen liegt die CPPI-Wachstumsrate bei 0,002484 pro Tag gegen 0,002525 der Alternative, bei D gleich 0,5; der CPPI-Drawdown bleibt unter 0,5, der andere ohne Stop-Loss beträgt 0,9 selbst bei halbem Optimalhebel.
- Bei TT-4-91 werden 6.800 tägliche Ausgaben von plus 1 oder minus 1 ohne Zurücklegen mit 6.800 trendbereinigten Ein-Tages-Vorwärtsänderungen des S&P 500 gepaart, multipliziert und gemittelt, und das 5.000 Mal.
- Der Monte-Carlo-p-Wert ist fast identisch mit dem Bootstrap-p-Wert, die Regel hat also möglicherweise Vorhersagekraft.
- Um die Auswahl der besten von 10 zu simulieren, wurden zehn Historien erzeugt, die höchste mittlere Rendite notiert und das 10.000-mal wiederholt; aus den 10.000 Werten entstand die Stichprobenverteilung dieser Statistik.
- Für den Fall ohne Data Mining wurden 1.000 Historien von je 24 Monaten erzeugt.
- Der Bias für die beste von 2, 10, 50 und 400 wurde jeweils über 10.000 Wiederholungen gemessen, alle Historien 24 Monate lang, Gewinnwahrscheinlichkeit 0,50 und Renditen unkorreliert.
- Die Monatszahl wurde von einem Monat bis 1.000 in Schritten von 50 Monaten variiert, und der Bias wurde bei jedem Schritt für die beste von 10 und die beste von 100 berechnet, alle mit erwarteter Rendite null.
- Im TU-Beispiel erzeugt pearsrnd 10.000 Renditepfade mit demselben Mittelwert, derselben Standardabweichung, Schiefe und Kurtosis, aber ohne die eingebetteten Korrelationen; die Preise sind das kumulative Produkt aus eins plus der simulierten Rendite, minus eins.
- Davon haben 1.166 eine mindestens so hohe durchschnittliche Strategierendite wie die beobachtete Reihe, die Null wird nur mit 88 Prozent verworfen.
- Unter 100.000 Zufallsanordnungen der Long- und Short-Einstiegstage der TU-Strategie erreicht keine die beobachtete Durchschnittsrendite.
- Von 10.000 Zufallsreihen der TU-Renditen mit denselben Momenten erreichen 1.166 mindestens die beobachtete Strategierendite, die Null wird nur mit 88 Prozent verworfen.
- Die bedingte Likelihood einer simulierten WACD(1,1)-Reihe mit 500 Beobachtungen schätzt ω = 0,364 (wahr 0,3), γ1 = 0,100 (wahr 0,2), ω1 = 0,767 (wahr 0,7) und α = 1,477 (wahr 1,5), mit Standardfehlern 0,139, 0,025, 0,060 und 0,052.
- Für die simulierte GACD(1,1)-Reihe lauten die Schätzungen ω = 0,401 (wahr 0,3), γ1 = 0,343 (wahr 0,2), ω1 = 0,561 (wahr 0,7), α = 0,436 (wahr 0,5) und κ = 2,077 (wahr 1,5), mit Standardfehlern 0,117, 0,074, 0,065, 0,078 und 0,653.
- Die Schätzungen der simulierten Reihen erscheinen vernünftig; die standardisierten Reihen êi = xi/ψ̂i zeigen keine signifikanten seriellen Korrelationen.
- Die Zinsregression wird mit 2100 Gibbs-Iterationen geschätzt, die ersten 100 werden verworfen; die Zeitplots der 2000 behaltenen Ziehungen sind stabil, und ein zweiter Lauf mit anderen Startwerten konvergiert ähnlich.
- Die Ausreißerschätzung des AR(3) läuft über 1050 Iterationen mit 50 Burn-in, Startwerte ϵ = 0,05, σ² = 0,012, φ1 = 0,2, φ2 = 0,02 und φ3 = 0,1.
- Jacquier, Polson und Rossi (1994) ziehen ht mit dem Metropolis-Algorithmus; dieser Abschnitt benutzt dafür Griddy Gibbs, mit einem Gitterbereich als Vielfachem der unbedingten Stichprobenvarianz von rt.
- Die bedingte Posterior von ht für 1 < t < n ist proportional zu ht hoch −1,5 mal exp[−(rt − x′t β)²/(2 ht) − (ln ht − µt)²/(2 σ²)], mit µt = [α0(1 − α1) + α1(ln ht+1 + ln ht−1)] / (1 + α1²) und σ² = σ²v / (1 + α1²).
- Das univariate SV-Modell läuft über 2500 Gibbs-Iterationen, die ersten 500 werden verworfen; die Dichten in Abbildung 12.5 beruhen auf 2000 Iterationen.
- Das bivariate Modell läuft ebenfalls über 2500 Iterationen mit 500 Burn-in; die Tabellenwerte beruhen auf den letzten 2000 Iterationen.
- Zur Konvergenzprüfung werden mehrere Läufe mit anderen Startwerten und Iterationszahlen verglichen; ein zweiter Lauf mit 500 + 1000 statt 500 + 2000 Iterationen liefert nahe beieinander liegende Posteriormittel.
- Die Dichten von log(χ² mit 1 Freiheitsgrad) und der Sieben-Normal-Mischung in Abbildung 12.12 beruhen auf 100.000 simulierten Beobachtungen; die Näherung ist sehr gut.
- Startwerte von {g11,t, g22,t, q21,t} stammen aus dem BEKK(1,1); die Werte bei t = 1 werden als gegeben gesetzt, und BEKK wird in Matlab geschätzt.
- Die Schätzung des stochastischen Volatilitätsmodells für die S&P-500-Monatsrenditen von Januar 1962 bis November 2004 verwendet Gibbs-Sampling mit Forward-Filtering-Backward-Sampling über 2000 plus 8000 Iterationen, die ersten 2000 als Burn-in.
- Die Prognosen des stochastischen Volatilitätsmodells in Tabelle 12.6, Ursprung Dezember 1999, stammen aus einem Gibbs-Lauf mit 2000 plus 2000 Iterationen: die Renditeprognosen der Horizonte 1 bis 5 sind 0,53, 0,78, 0,92, 0,88 und 0,84, die Volatilitätsprognosen 19,31, 19,36, 19,35, 19,65 und 20,13.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 248–267 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-014-p248-p267|S. 248–267]]
- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 210–229 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-012-p210-p229|S. 210–229]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 229–248 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-013-p229-p248|S. 229–248]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 248–267 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-014-p248-p267|S. 248–267]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 286–305 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-016-p286-p305|S. 286–305]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 305–324 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-017-p305-p324|S. 305–324]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 324–343 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-018-p324-p343|S. 324–343]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 381–400 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-021-p381-p400|S. 381–400]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 419–438 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-023-p419-p438|S. 419–438]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 1–13 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-001-p001-p013|S. 1–13]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 14–33 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-002-p014-p033|S. 14–33]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 33–51 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-003-p033-p051|S. 33–51]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 180–199 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-014-p180-p199|S. 180–199]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 210–229 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-012-p210-p229|S. 210–229]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 229–248 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-013-p229-p248|S. 229–248]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 267–286 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-015-p267-p286|S. 267–286]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 286–305 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-016-p286-p305|S. 286–305]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 362–381 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-020-p362-p381|S. 362–381]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 457–476 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-025-p457-p476|S. 457–476]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 628–647 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-034-p628-p647|S. 628–647]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 647–666 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-035-p647-p666|S. 647–666]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 666–685 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-036-p666-p685|S. 666–685]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 685–704 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-037-p685-p704|S. 685–704]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 191–210 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-011-p191-p210|S. 191–210]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 216–235 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-016-p216-p235|S. 216–235]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 235–239 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-017-p235-p239|S. 235–239]]

## Verwandte Themen
