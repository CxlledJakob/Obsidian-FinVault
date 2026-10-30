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
aktualisiert: 2026-10-30
---

# Monte-Carlo-Simulation


## Kurzdefinition

- Die numerische Bestimmung der Handelsregel zieht sehr viele künstliche Gewinnpfade aus den geschätzten Prozessparametern.
- Die Monte-Carlo-Simulation vergleicht hier die Performance von Hierarchical Risk Parity, dem Minimum-Varianz-Portfolio des Critical Line Algorithm und dem Inverse-Varianz-Portfolio außer Stichprobe.
- Snippet 16.5 setzt Monte-Carlo-Experimente für Hierarchical Risk Parity, den Critical Line Algorithm und das Inverse-Varianz-Portfolio um.
- Die Monte-Carlo-Permutation ist nach dem bekannten europäischen Spielkasino benannt, weil sie den Computer wie ein Roulette verwendet.
- Die Monte-Carlo-Simulation, von Stanislaw Ulam (1909 bis 1984) eingeführt, löst mathematische Probleme durch zufälliges Ziehen von Stichproben.
- Die Monte-Carlo-Permutation zum Prüfen von Regeln stammt von Timothy Masters; er schlug sie als Erster vor, um die Stichprobenverteilung der gebacktesteten Regelleistung zu erzeugen, als Alternative zu Whites Reality Check.

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

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


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

## Verwandte Themen
