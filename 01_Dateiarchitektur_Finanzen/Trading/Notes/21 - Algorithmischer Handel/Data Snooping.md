---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Validierung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Data Snooping


## Kurzdefinition

- Data Mining und Data Snooping werden in den sieben Sünden von Luo et al. 2014 als das Trainieren des Modells auf dem Testset gefasst.
- Über viele Versuche hinweg liegt der erwartete Höchstwert der geschätzten Sharpe Ratio selbst dann über null, wenn die wahre Sharpe Ratio null ist.
- Data-Snooping-Bias entsteht, wenn zu viele freie Parameter an zufällige, flüchtige Marktmuster der Vergangenheit angepasst werden, damit die historische Performance gut aussieht.
- Die Praxis, viele Regeln mit dem Ziel zu testen, die mit der besten Performance auszuwählen, heißt Data Mining.
- Der Data-Mining-Bias ist die erwartete Differenz zwischen der beobachteten Leistung der besten Regel und ihrer erwarteten Leistung; erwartet heißt der langfristige Mittelwert dieser Differenz über viele Experimente.
- Data Mining sucht in großen statistischen Datenbanken nach Mustern, Modellen und Vorhersageregeln; die beste Regel ist dabei die mit der höchsten beobachteten Leistung unter den verglichenen Backtests.
- Der Data-Mining-Bias ist die erwartete Differenz zwischen der beobachteten Leistung der Regel, die den Vergleich gewinnt, und ihrer wahren erwarteten Leistung.
- Data Snooping meint hier, die Ergebnisse früherer Regelstudien anderer Forscher zu verwenden. Diese Studien legen typischerweise nicht offen, wie viel Data Mining zu der Entdeckung geführt hat, deshalb lassen sich die Effekte nicht berücksichtigen und die statistische Signifikanz nicht richtig beurteilen.
- Data-Snooping-Bias, treffender als Prior-Research-Snooping-Bias bezeichnet, entsteht, wenn Data Miner die Ergebnisse früherer Forschung benutzen, um auszuwählen, welche Regeln sie testen, also Regeln, die zuvor erfolgreich waren.

## Kernaussagen

- Unter der Nullhypothese einer wahren Sharpe Ratio von null ist der erwartete Höchstwert der geschätzten Sharpe Ratios die Vergleichsschwelle der Deflated Sharpe Ratio.
- Die Schwelle steigt schnell mit der Zahl unabhängiger Versuche und mit der Varianz der in diesen Versuchen geschätzten Sharpe Ratios.
- Jedes Backtestergebnis muss zusammen mit allen Versuchen berichtet werden, die zu seiner Erstellung geführt haben.
- Fehlt die Angabe aller Versuche, lässt sich die Wahrscheinlichkeit einer Fehlentdeckung nicht beurteilen.
- Die Überschrift des dritten Gesetzes des Backtesting lautet, dass die meisten Entdeckungen in der Finanzwelt falsch sind, weil die Versuche nicht mitberichtet werden.
- Die Deflated Sharpe Ratio korrigiert die Sharpe Ratio um nichtnormale Renditen, um die Länge der Historie und um Mehrfachtests sowie Selection Bias.
- Der durchgehende Schwerpunkt liegt auf einfachen und linearen Strategien als Gegenmittel gegen die Overfitting- und Data-Snooping-Verzerrungen, die komplexe Strategien oft plagen.
- Möglichst viele technische Handelsindikatoren oder Regeln auf eine Preisreihe zu werfen, um zu sehen, welcher Indikator oder welche Regel profitabel ist, lädt Data-Snooping-Bias ein.
- Stattdessen wird die grundlegende Eigenschaft der Preisreihe mit einem einfachen mathematischen Modell herausgearbeitet und dieses Modell dann finanziell ausgenutzt.
- Diese zufälligen Muster kehren in der Zukunft wahrscheinlich nicht wieder, sodass ein daran angepasstes Modell wenig Vorhersagekraft hat.
- Der bekannte Nachweis ist ein Test auf Out-of-Sample-Daten und die Verwerfung eines Modells, das ihn nicht besteht.
- Wer das Modell nachjustiert, bis In-Sample- und Out-of-Sample-Ergebnis beide annehmbar aussehen, hat die Out-of-Sample-Daten in In-Sample-Daten verwandelt.
- Zur Eingrenzung wird das Modell so einfach wie möglich und mit so wenigen Parametern wie möglich gebaut.
- Am Ende schleicht sich der Bias dennoch ein. Deshalb ist ein Walk-Forward-Test der abschließende echte Out-of-Sample-Test.
- Dieser Walk-Forward kann als Paper Trading laufen. Besser wird das Modell mit echtem Geld bei minimalem Hebel gehandelt, um Aspekte zu prüfen, die selbst dem Paper Trading entgehen.
- Die meisten Trader wären zufrieden, wenn der Live-Handel eine Sharpe Ratio besser als die Hälfte des Backtest-Wertes erzeugt.
- Die lineare Mean-Reversion-Strategie hat keinen Data-Snooping-Bias, weil sie keine Parameter besitzt, die optimiert werden.
- Selbst der Lookback wird nicht an der Strategie optimiert, sondern gleich der Halbwertszeit gesetzt, einer Eigenschaft der Preisreihe und nicht der konkreten Handelsregel.
- Die lineare Strategie wird gewählt, weil sie praktisch parameterfrei ist und deshalb am wenigsten unter Data-Snooping-Bias leidet.
- Sie eignet sich, um zu zeigen, ob Mean-Reversion-Handel für ein Portfolio profitabel sein kann, ist aber unpraktisch, weil die Abweichung vom Mittel und damit das gebundene Kapital nicht begrenzt ist.
- Alle höheren Momente zu erfassen lädt wegen der meist geringen empirischen Datenmenge zu Data-Snooping-Bias ein.
- Praktisch werden deshalb für die Monte-Carlo-Verteilung nur die ersten vier Momente über das Pearson-System verwendet.
- Die Hebeloptimierung an der einen historischen Backtest-Renditereihe leidet unter dem üblichen Data-Snooping-Bias der Parameteroptimierung.
- Der so gefundene Hebel ist für eine andere künftige Realisierung im Allgemeinen nicht optimal.
- Weil Finanzpaniken und Krisen selten sind, ist es leicht, beim Test eines führenden Risikoindikators dem Data-Snooping-Bias zu erliegen.
- Data Mining ist, richtig durchgeführt, die beste Methode des modernen Technikers zur Wissensentdeckung, doch auf die so gewonnenen Ergebnisse sind spezialisierte statistische Tests anzuwenden.
- Eine Form des Backtestings, Data Mining genannt, erzeugt eine Aufwärtsverzerrung; günstige historische Performance kann daraus stammen statt aus einer tragfähigen Methode.
- Profitable Backtests können das Narrengold eines Data Miners sein.
- Die evidenzbasierte technische Analyse setzt rechenintensive statistische Verfahren ein, die die Probleme aus dem Data-Mining-Bias mindern.
- Teil 2 testet 6.402 binäre Kauf- und Verkaufsregeln auf dem S&P 500 über 25 Jahre historischer Daten und bewertet sie auf statistische Signifikanz mit Tests, die den Data-Mining-Bias bewältigen sollen.
- Kapitel 6 behandelt den Data-Mining-Bias unter dem Titel The Fool's Gold of Objective TA.
- Rechenintensive Modellierung mit neuronalen Netzen, genetischen Algorithmen und anderen Verfahren des statistischen Lernens und der künstlichen Intelligenz hat profitable Muster in technischen Indikatoren gefunden.
- Wird nach einer unbefriedigenden ersten Regel weitergesucht, indem Parameter, Logik und Indikatoren verändert werden, bis eine gut abschneidende Regel gefunden ist, ist das Data Mining.
- Weil allein der Analyst entscheidet, wann diese Suche endet, ist ihr Umfang unbegrenzt, und am Ende ist eine Regel mit guter vergangener Performance garantiert.
- Die vergangene Performance einer durch Data Mining entdeckten Regel überzeichnet ihre wahrscheinliche künftige Performance; diese Überzeichnung heißt Data-Mining-Bias.
- Data Mining an sich ist nicht der Fehler; richtig betrieben ist es eine produktive Forschungsmethode.
- Der Fehler ist, die durch das Data Mining erzeugte Aufwärtsverzerrung nicht zu berücksichtigen.
- Wird das Ausmaß der Suche berücksichtigt, die zur Entdeckung der Regel geführt hat, lassen sich stichhaltige Schlüsse über ihr künftiges Gewinnpotenzial ziehen.
- Objektive Forschung zur Technischen Analyse ist für eine besondere Art systematischen Fehlers anfällig, den Data-Mining-Bias, wenn nicht sorgfältige Schritte dagegen unternommen werden.
- Erklärungen einer guten Backtest-Performance, die nichts mit der Vorhersagekraft der Regel zu tun haben, sind Glück durch Stichprobenfehler und systematischer Fehler durch Data-Mining-Bias.
- Eine wissenschaftliche Haltung gegenüber einem außerordentlich profitablen Regel-Backtest zieht die Möglichkeit einer bedeutenden TA-Entdeckung erst in Betracht, nachdem diese gewöhnlicheren Erklärungen verworfen wurden.
- Das Prinzip der einfacheren Erklärung, im Text Okams Razor genannt, nimmt erstaunliche Hypothesen erst ernst, nachdem alltäglichere verworfen sind.
- Data Mining ist eine wirksame Forschungsmethode, erhöht aber die Chance auf eine glückliche Performance.
- Deshalb muss die Leistungsschwelle, ab der die Nullhypothese verworfen wird, höher und unter Umständen viel höher gesetzt werden.
- Die höhere Schwelle gleicht die größere Wahrscheinlichkeit aus, auf eine nutzlose Regel zu stoßen, die im Backtest Glück hatte.
- Preiswerte Rechenleistung, vielseitige Backtest-Software und reichlich historische Daten machen es leicht, fast einladend, viele Regeln zu testen.
- Dieselbe beobachtete Performance kann auf der Dichte eines Einzeltests weit im rechten Schwanz liegen und signifikant wirken, auf der Dichte für die beste von 1.000 Regeln aber nicht statistisch signifikant sein.
- Bewertet mit der passenden Dichte rechtfertigt die ziemlich hohe Performance der besten dieser 1.000 Regeln nicht den Schluss auf Vorhersagekraft oder auf eine erwartete Rendite größer als null.
- Kapitel 6 wird zeigen: Wurde eine Regel ausgewählt, weil sie die beste aus einem großen Universum gebacktesteter Regeln war, also durch Data Mining entdeckt wurde, gibt es noch weniger Grund, über ihre künftige Leistung optimistisch zu sein.
- Das gilt zusätzlich zu dem schon schwachen Fall einer Regel mit nur fünf historischen Signalen, die alle richtig waren. Das Gesetz der großen Zahlen macht Optimismus dort höchstwahrscheinlich unberechtigt, und die Auswahl als beste aus vielen Regeln schwächt ihn weiter.
- Der Bootstrap in Grundform eignet sich nicht, die statistische Signifikanz von durch Data Mining entdeckten Regeln zu bewerten.
- Whites patentierte Erweiterung in der Software Forecaster's Reality Check dehnt den Bootstrap auf durch Data Mining entdeckte Regeln aus.
- Diese Erweiterung wird in Kapitel 6 besprochen und in Kapitel 9 genutzt, um die statistische Signifikanz von über 6.000 Regeln für den Handel des S&P 500 zu bewerten.
- Die hier beschriebene Bootstrap-Prozedur für eine einzelne Regel behandelt das Data Mining nicht.
- Wie viel Suche zur Entdeckung der Regel führte, insbesondere ob sie unter einer großen Gruppe gebacktesteter Regeln gefunden wurde, kann p-Wert und Signifikanz verändern.
- Die Ergebnisse zu TT-4-91 setzen voraus, dass dies die einzige zum Backtest vorgeschlagene Regel war.
- Die beobachtete Leistung, mit der eine Regel den Vergleich gewinnt, überzeichnet systematisch, wie gut sie künftig wahrscheinlich abschneidet.
- Trotzdem lohnt Data Mining: Bei genügend vielen Beobachtungen ist die Regel mit der höchsten beobachteten Leistung am ehesten künftig die beste, auch wenn diese beobachtete Leistung positiv verzerrt ist.
- Die beobachtete Leistung zerfällt in Zufall und echte Vorhersagekraft, und der Zufall ist bei Weitem der größere Teil.
- Wer die Regel mit der höchsten beobachteten Leistung wählt, wählt meist eine Regel mit großem Glücksanteil; weil Glück sich nicht wiederholt, fällt die Leistung außer Stichprobe wahrscheinlich auf das Niveau der echten Vorhersagekraft zurück.
- Dieser Rückgang ist am ehesten der Fall von einer unrealistisch hohen Erwartung und kein echter Verlust an Vorhersagekraft.
- Die Bias-Erklärung passt dazu, dass die Leistung außer Stichprobe tendenziell schlechter ist, ohne eine geänderte Marktdynamik anzunehmen, und ist nach Occams Rasiermesser vorzuziehen, wenn die Erklärungen gleich gut passen.
- Objektive technische Analyse umfasst nur Verfahren, die bestimmt genug sind, um als Computeralgorithmus zu laufen und gebacktestet zu werden; alles Übrige ist subjektive technische Analyse.
- Objektive Verfahren können gültiges Wissen sein, aber nur wenn Backtests im Licht der Zufallsvariation und des Data-Mining-Bias beurteilt werden; wer diese Wirkungen ignoriert, sammelt auch dort Irrtümer an.
- Data Mining ist ein Mehrfachvergleich mit einem klar definierten Problem, einer Menge von Kandidatenlösungen und einer Gütefunktion; gewählt wird die höchste Punktzahl.
- Beim Regel-Data-Mining ist das Problem das Timing langer und kurzer Positionen, um Gewinne zu erzielen; die Kandidaten sind die vorgeschlagenen Regeln, und das Gütemaß kann die mittlere Rendite, die Sharpe Ratio oder die Rendite zum Ulcer-Index sein.
- Jede Suchbreite unterliegt dem Bias: Parameteroptimierung, Regelsuche und Regelinduktion.
- Die Parameteroptimierung hält die Regelform fest und sucht nur Parameterwerte; eine erschöpfende Suche umfasst das Produkt der je Parameter geprüften Werte.
- Ein genetischer Algorithmus, lose an die biologische Evolution angelehnt, nutzt frühe Ergebnisse, um spätere Kombinationen zu wählen, findet relativ schnell nahe am Optimum liegende Parameter und bleibt brauchbar, wenn Zufall eine kalkülbasierte Suche unpraktisch macht.
- Die Regelsuche ändert begriffliche Form und Parameter, hält die Komplexität, also die Zahl der Parameter, fest und kombiniert einfache Regeln nicht zu komplexeren.
- Die Regelinduktion lässt die Komplexität während der Suche wachsen und nutzt maschinelles Lernen, um die leistungsstärkste Komplexität zu finden, von einzelnen Regeln über Paare bis zu reicheren Verbindungen.
- Leinweber fand unter mehreren hundert Zeitreihen einer UN-Datenbank die höchste Korrelation zum S&P 500 bei der Butterproduktion Bangladeschs, etwa 0,70; wird die Zahl der geprüften Reihen berücksichtigt, ist die Korrelation nicht statistisch signifikant.
- Die Chance, dass eine bestimmte Person die Lotterie zweimal gewinnt, ist 1 zu 17 Billionen; Diaconis und Mosteller schätzen die Chance, nachträglich irgendjemanden mit zwei Gewinnen zu finden, auf etwa 1 zu 30.
- Fünfundvierzig Statistiker, die die Bibelcode-Arbeit von Eliyahu Rips prüften, fanden sie völlig unüberzeugend; der Data-Mining-Bias ist im Kern fehlerhafte statistische Inferenz.
- Die beobachtete Leistung der besten im Data Mining gefundenen Regel ist positiv verzerrt; ihre erwartete Leistung außer Stichprobe liegt unter der In-Sample-Leistung, mit der sie die anderen Regeln schlug.
- Der Bias ist die gemeinsame Wirkung von Zufall und der Auswahlregel jedes Mehrfachvergleichs, den Kandidaten mit der besten beobachteten Leistung zu nehmen.
- Er zeigt sich im Allgemeinen über viele Data-Mining-Fälle; man kann nicht sagen, dass ein bestimmtes einzelnes Ergebnis verzerrt ist.
- Statistische Aussagen gelten für eine große Zahl von Beobachtungen, etwa eine große Zahl von Schätzungen.
- Der Fehler ist beobachtet minus wahr; zeigt eine Waage 140 Pfund bei einem wahren Gewicht von 150 Pfund, ist der Fehler minus 10 Pfund.
- Ein unverzerrter Fehler hat den Erwartungswert null; über viele nur damit behaftete Beobachtungen liegt der mittlere Fehler ungefähr bei null, und die Werte streuen um die Wahrheit.
- Systematischer Fehler liegt tendenziell auf einer Seite der Wahrheit; der Mittelwert vieler solcher Fehler ist deutlich von null verschieden, und in der Abbildung sind die Beobachtungen positiv verzerrt.
- Die beobachtete Durchschnittsrendite der besten Regel ist positiv verzerrt, Schlüsse daraus sind systematisch falsch.
- Ein Hypothesentest verwirft die Null häufiger, als das Signifikanzniveau sagt; zum Niveau 0,05 erwartet man nur 5 irrtümliche Verwerfungen von 100, bei positiver Verzerrung sind es mehr, möglicherweise weit mehr, und Regeln ohne Vorhersagekraft werden gehandelt.
- Im Beispiel haben alle Regeln die erwartete Rendite null, die beste von 50 zeigt aber plus 37 Prozent; auf einer bei null zentrierten Verteilung liegt der p-Wert unter 0,05, und die Verwerfung ist falsch.
- Auf der Stichprobenverteilung des maximalen Mittelwerts unter 50 Mittelwerten, zentriert bei plus 33 Prozent, ist der Anteil bei 37 Prozent oder darüber fast die Hälfte, 0,45; 37 Prozent sind nicht signifikant.
- Wäre die erwartete Rendite jeder der 50 Regeln null, betrüge die Wahrscheinlichkeit 0,45, dass die mittlere Rendite der besten Regel durch Glück mindestens 37 Prozent erreicht.
- Je größer der Anteil des Glücks gegenüber dem Verdienst an der beobachteten Leistung, desto größer der Bias; wo die beobachtete Leistung streng oder vor allem wahres Verdienst ist, ist der Bias null oder sehr klein.
- Finanzmärkte sind äußerst schwer vorherzusagen, sodass der größte Teil der beobachteten Regelleistung Zufall und nicht Vorhersagekraft ist; selbst die wirksamsten Regeln sind nur schwach prädiktiv, und der Bias beim Data Mining solcher Regeln ist groß.
- Von zwei oft unterstellten Versprechen des Mehrfachvergleichs gilt das erste, dass der Kandidat mit der besten beobachteten Leistung künftig am ehesten der beste ist; das zweite, dass diese beobachtete Leistung die künftige verlässlich schätzt, gilt für Regeln der technischen Analyse nicht.
- Bei zwölf Regeln mit erwarteter Rendite null kann eine beobachtete Rendite von plus 60 Prozent entstehen, und der Bias beträgt dann plus 60 Prozent; bei 30 Regeln kann eine beobachtete Leistung von 100 Prozent gewählt werden, deren künftige Leistung sehr wahrscheinlich enttäuscht.
- Hoher Zufall hat die weitere Folge, dass die überlegene Regel mit der höchsten erwarteten Rendite gegen die Glücksleistung einer schwächeren Regel verlieren kann; der Data Miner kennt dieses Risiko nicht, weil die wahre erwartete Rendite ein unbekannter Populationsparameter ist, und sieht die vollen Folgen erst, wenn die Zukunft vergangen ist.
- Ist der Abstand der erwarteten Rendite zwischen der besten und der nächstbesten Regel groß genug, zeigt die beste beobachtete Leistung verlässlicher auf die überlegene Regel; ist er klein, überlappen die Verteilungen stark.
- Fünf Faktoren bestimmen die Größe des Bias: die Zahl der geprüften Regeln, die Zahl der Beobachtungen in der Kennzahl, die Korrelation der Regelrenditen, das Vorliegen großer positiver Ausreißer-Renditen und die Variation der erwarteten Renditen.
- Fünf Faktoren bestimmen das Ausmaß des Data-Mining-Bias: die Zahl der gebacktesteten Regeln, die Zahl der Beobachtungen für die Performancestatistik, die Korrelation der Regelrenditen, das Vorhandensein positiver Ausreißer-Renditen und die Variation der erwarteten Renditen unter den Regeln.
- Je mehr Regeln getestet werden, desto größer der Bias; je mehr Beobachtungen, desto kleiner; je geringer die Korrelation der Regelrenditen, desto größer der Bias; positive Ausreißer vergrößern ihn, der Effekt sinkt aber, wenn ihre Zahl klein relativ zur Beobachtungszahl ist; je geringer die Variation der wahren erwarteten Renditen, desto größer der Bias.
- Diese Beziehungen gelten speziell, wenn die Performancestatistik die mittlere Rendite der Regel ist; bei anderen Statistiken wie der Sharpe Ratio kann der Zusammenhang anders sein, weil deren Stichprobenverteilung von der der mittleren Rendite abweicht.
- Der Data-Mining-Bias ist für echte Regeln nie bekannt, weil die erwartete Performance ein Populationsparameter ist; messbar ist er an künstlichen Regeln, deren Anteil richtiger Signale experimentell gesetzt und deren erwartete Rendite damit bekannt ist.
- Wird nur eine Regel gebacktestet, gibt es kein Data Mining und keinen Data-Mining-Bias.
- Bei künstlichen Regeln mit Gewinnwahrscheinlichkeit 0,50, erwarteter Rendite null, 24 Monaten und unkorrelierten Renditen beträgt der über 10.000 Wiederholungen gemittelte Bias +8,5 Prozent für die beste von 2, +22 Prozent für die beste von 10, +33 Prozent für die beste von 50 und +48 Prozent für die beste von 400.
- Die Beziehung zwischen Regelzahl und Bias ist nahezu linear, wenn die Zahl der getesteten Regeln im Logarithmus zur Basis 10 aufgetragen wird.
- Von allen Faktoren ist die Stichprobengröße womöglich der wichtigste: bei nur 10 Monaten beträgt der Bias für die beste von 1.024 Regeln etwa 84 Prozent, bei 1.000 Monaten schrumpft er auf unter 12 Prozent.
- Ab etwa 600 Beobachtungen wird der Bias-Unterschied zwischen der besten von 10 und der besten von 100 winzig; bei genügend Beobachtungen lässt sich eine viel größere Regelzahl durchsuchen, ohne den Bias wesentlich zu erhöhen.
- Alles, was den Zufall in der beobachteten Performance verringert, verringert den Data-Mining-Bias; bei 48 statt 24 Monaten lägen die mittleren Renditen enger um die erwartete Rendite null, und der Bias der besten Regel wäre kleiner.
- Stärkere Korrelation der Regelrenditen verkleinert den Bias, weil sie die wirksame Regelzahl schrumpft; völlig identische Regeln sind faktisch eine einzige Regel, und der Bias schrumpft auf null.
- Der Bias bleibt hoch, bis die Korrelation der Regelrenditen sich 1,0 nähert; erst ein hohes Korrelationsniveau mindert ihn wesentlich.
- Wenige extrem große positive Beobachtungen können einen großen Bias erzeugen; bei kleiner Beobachtungszahl hebt ein einziger Extremwert den Stichprobenmittelwert dramatisch, viele Beobachtungen mildern den Effekt.
- Haben alle Regeln dieselbe erwartete Rendite, stammen die Unterschiede der beobachteten Performance nur aus Glück, der Sieger ist die glücklichste Regel und der Bias ist groß; unterscheiden sich die erwarteten Renditen, wird der Bias tendenziell kleiner und unter bestimmten Bedingungen sehr klein.
- Ist eine Regel mit erwarteter Rendite +20 Prozent den übrigen mit null wirklich überlegen, erzeugt sie meist die höchste beobachtete Performance, ohne dass das in jedem einzelnen Test garantiert ist, und der zugehörige Bias bleibt klein, weil die Leistung aus Prognosekraft und nicht aus Glück stammt.
- Die Renditen von Aktien und anderen Finanzanlagen haben relativ schwere Ränder gegenüber der Normalverteilung; eine Regel, die im Crash zufällig short war, kann den Data-Mining-Wettbewerb aus dem falschen Grund gewinnen.
- Bei künstlichen Regeln auf einer absichtlich leichtschwänzigen Renditeverteilung war der Bias deutlich schwächer als auf den S&P-500-Monatsrenditen; praktisch nutzbar ist das nur, wenn Regeln an festen Zielen aussteigen und extreme Ergebnisse damit wegfallen.
- Data Mining muss mindestens besser sein als die Zufallsauswahl einer Regel aus dem Universum, sonst ist es kein vernünftiger Forschungsansatz.
- Im zweiten Experiment haben die meisten künstlichen Regeln eine erwartete Rendite von null oder nahe null, und nur wenige mit deutlich positiver Rendite sind eingestreut, weil Regeln mit hoher erwarteter Rendite als selten angenommen werden.
- Die genannten Bias-Größen gelten nur für diesen Test mit bestimmten monatlichen S&P-500-Renditen, 24 Monaten, unabhängigen Renditen und erwarteter Rendite null; das Prinzip mehr Regeln, größerer Bias bleibt, die konkreten Niveaus ändern sich.
- Ob Data Mining auf einer tragfähigen Prämisse ruht, sind zwei Fragen: Hat die Regel mit der höchsten beobachteten mittleren Rendite eine höhere erwartete Rendite als eine zufällig gezogene, und führt das Testen von mehr Regeln zu einer Regel mit höherer erwarteter Rendite.
- Die Antwort auf beide Fragen ist ein eingeschränktes Ja; die Einschränkung ist die Zahl der Beobachtungen, aus denen die mittlere Rendite oder eine andere Performancestatistik berechnet wird.
- Bei genügend Beobachtungen lautet die Antwort ja; bei kleiner Beobachtungszahl funktioniert Data Mining nicht, eine geratene Regel ist genauso gut, und mehr Regeln liefern keine besseren.
- Wie viele Beobachtungen genügen, hat keine einfache Antwort; die nötige Zahl hängt von der Performancestatistik und von der Beschaffenheit der Rohdaten ab.
- Mit 100 oder 1.000 Monatsbeobachtungen steigt die erwartete Rendite der besten Regel, wenn mehr Regeln geprüft werden, und die Kurve für 1.000 steigt steiler als die für 100; bei nur zwei Monaten bleibt die Kurve flach.
- Bei nur zwei Monaten ist die erwartete Rendite der besten von 256 nicht höher als die der besten von einer Regel, also ohne Data Mining, und die Kurve bleibt bei +1,4 Prozent, der erwarteten Rendite der durchschnittlichen Regel im Universum.
- Die beste von 256 mit 1.000 Monaten Historie hat eine erwartete Rendite von +10 Prozent im Jahr, weit über dem Universumsmittel von +1,4 Prozent.
- Bei genügend Beobachtungen ist die beobachtete Rendite ein nützlicher, aber positiv verzerrter Indikator der erwarteten Rendite; bei zu wenigen Beobachtungen ist sie praktisch nutzlos.
- Im Universum unterschiedlicher Güte überzeichnet die beste von 256 bei nur zwei Monaten ihre erwartete Rendite um über 200 Prozent pro Jahr; bei 100 Monaten beträgt der Bias etwa 18 Prozent, bei 1.000 Monaten weniger als 3 Prozent.
- Bei großer Beobachtungszahl ebnet sich der Bias schnell ein: bei Historien von 1.000 Monaten ist der Bias der besten von 16 nicht viel schlimmer als der der besten von 256, und nach etwa 30 geprüften Regeln bei 100 Monaten hat eine weitere Erhöhung der Regelzahl nur noch einen minimalen Effekt auf den Bias.
- Mehr Regeln zu testen ist dann etwas Gutes, und die Strafe dafür fällt schnell ab, sofern die zur Auswahl genutzte Performancestatistik aus genügend Beobachtungen berechnet wird.
- Die beobachtete Performance der besten Regel liegt immer über ihrer erwarteten, weil ein Best-of-Kriterium immer einen positiven Bias erzeugt, solange Glück mitspielt; der Abstand schrumpft mit mehr Beobachtungen und ist bei der besten von 500 größer als bei der besten von 10.
- Bei einer Korrelation von 0,9 und 100 Monaten beträgt die erwartete Rendite der besten von 256 nur +1,4 Prozent, gleich einer zufällig gezogenen Regel; bei Korrelation null liegt sie bei fast 4 Prozent, über dem Universumsmittel von +1,4 Prozent.
- Die beobachtete Performance der durch Data Mining gefundenen besten Regel ist positiv verzerrt: ihre erwartete künftige Rendite liegt unter der historischen, und in einer künftigen Stichprobe wird sie wahrscheinlich schlechter abschneiden als in dem Backtest, der sie gewinnen ließ.
- Je mehr Beobachtungen, desto schmaler die Stichprobenverteilung und desto leichter ihre Ränder und desto kleiner der Bias; je mehr Regeln durchsucht werden, desto größer der Bias; je kleiner die Variation der wahren Qualität, desto größer der Bias.
- Die Zusammenfassung sagt, der Punkt zur kleineren Variation der wahren Qualität sei experimentell nicht untersucht worden.
- Data Mining funktioniert bei großer Stichprobe, je mehr Regeln desto höher die erwartete Performance der gewählten Regel, und es funktioniert nicht, wenn die Stichprobe zu klein ist.
- Enthält die Kandidatenmenge Regeln mit überlegener erwarteter Rendite, kann Data Mining sie finden, ihre künftige Performance liegt aber aller Wahrscheinlichkeit nach unter der gebacktesteten; diese Verschlechterung außer Stichprobe ist eine Tatsache des Data Mining.
- Sind alle Kandidaten wertlos, mit erwarteter Rendite null oder weniger, läuft der Data Miner Gefahr, vom Bias getäuscht zu werden und eine Regel mit erwarteter Rendite null zu wählen; das ist das Katzengold des objektiven Technikers.
- Drei vorgeschlagene Gegenmittel sind Out-of-Sample-Tests, der Data-Mining-Korrekturfaktor von Markowitz und Xu und Randomisierungsmethoden wie Bootstrap und Monte Carlo.
- White's Reality Check und die Monte-Carlo-Permutation prüfen beide, dass alle beim Data Mining untersuchten Regeln keine Prognosekraft haben, formulieren die Null aber verschieden.
- Bei White's Reality Check hat eine nutzlose Regel die erwartete Rendite null; bei der Monte-Carlo-Permutation sind die Ausgaben zufällig mit der künftigen Marktänderung gekoppelt.
- Ein Fehler erster Art ist das Katzengold des Data Miners: die Null ist wahr, alle Regeln sind nutzlos, wird aber verworfen, weil eine nutzlose Regel durch Glück eine hohe mittlere Rendite und einen kleinen p-Wert erzielt hat.
- Ein Fehler zweiter Art lässt echtes TA-Gold im Boden: die Regel hat Prognosekraft, ihre Tugend bleibt aber unerkannt, weil sie im Backtest Pech hatte und die Performance zu niedrig zum Verwerfen der Null ist.
- Hansen kritisiert, dass beide Verfahren an Power verlieren, wenn Regeln schlechter als die Benchmark im Universum liegen, also erwartete Renditen unter null haben, etwa durch Umkehren des Ausgangssignals einer Regel mit wirklich positiver erwarteter Rendite.
- Etwa die Hälfte der in Teil 2 getesteten Regeln sind solche inversen Regeln, deshalb ist diese Untersuchung für Hansens Problem anfällig.
- Timothy Masters prüfte die Power beider Verfahren an künstlichen Regeln, die besser und schlechter als die Benchmark waren; die Sorge ist berechtigt, wenn eine Regel mit negativer erwarteter Rendite eine extrem große Renditevarianz hat, denn dann kann die Power drastisch sinken.
- In Fällen, die beim Data Mining von Regeln der technischen Analyse wahrscheinlicher sind, sind beide Verfahren gegen dieses Problem einigermaßen robust, und gibt es mindestens eine überlegene Regel, haben beide eine vernünftige Chance, sie zu entdecken.
- Romano und Wolf empfehlen eine Änderung, die die Power von White's Reality Check erhöht und anscheinend auch die der Monte-Carlo-Permutation, also die Wahrscheinlichkeit eines Fehlers zweiter Art senkt; sie ist in den Versionen der Fallstudie von Teil 2 umgesetzt.
- Dieselbe Zufallspaarung von Regelausgabe und Marktrendite muss für alle Regeln gelten, damit die Korrelationsstruktur erhalten bleibt, einer der fünf Faktoren des Data-Mining-Bias.
- Data-Mining-Bias entsteht, wenn die Profitabilität vieler Regeln verglichen wird, um überlegene auszuwählen: Die beobachtete Performance der besten Regeln überschätzt die künftig erwartete. Data Snooping ist ein noch schwereres Problem, weil das Ausmaß des fremden Minings unbekannt bleibt.
- Je nachdem, welches Verfahren benutzt wird, Whites Reality Check oder die Monte-Carlo-Permutationsmethode, muss die Information über jede getestete Regel verfügbar sein, um die passende Stichprobenverteilung zu konstruieren.
- Als Beispiel dient die Double-9:1-Aufwärts-Abwärts-Volumenregel von Martin Zweig. Sie signalisiert Long, wenn das tägliche Verhältnis von Aufwärts- zu Abwärtsvolumen an der NYSE innerhalb eines Zeitfensters von drei Monaten zweimal einen Schwellenwert von 9 überschreitet.
- Die Regel hat drei freie Parameter: den Schwellenwert des Verhältnisses, 9, die Zahl der Fälle, in denen das Verhältnis die Schwelle überschreitet, 2, und den maximalen zeitlichen Abstand zwischen den Schwellenverletzungen, 3 Monate.
- Nach Tests von Studenten in der Vorlesung des Autors hat das Signal Vorhersagekraft über die folgenden 3, 6, 9 und 12 Monate. Die Regel ist statistisch signifikant nur unter der Annahme, Zweig habe kein Data Mining betrieben, um die empfohlenen Parameterwerte 9, 2 und 3 zu finden.
- Zweig hat nicht berichtet, ob er andere Versionen der Regel mit anderen Parameterkombinationen getestet hat oder, falls ja, wie viele Kombinationen versucht wurden, um den Satz zu finden, der seine Regel definiert.
- Wäre Zweigs Regel in die Fallstudie aufgenommen und als beste Regel ausgewählt worden, wäre es unmöglich, das wahre Ausmaß des Data Mining zu berücksichtigen, das zu ihrer Entdeckung geführt hat.
- Die Fallstudie hat deshalb keine von anderen Forschern diskutierten Regeln ausdrücklich eingeschlossen. Mögliche Ähnlichkeiten entstanden zufällig, nicht absichtlich. Diese Vorsicht milderte den Data-Snooping-Bias, konnte ihn aber nicht ganz beseitigen, weil der Autor beim Vorschlagen der 6402 Regeln von früher gelesenen Regelstudien beeinflusst war.
- Herkömmliche Signifikanztests eignen sich nicht für durch Data Mining gefundene Regeln, weil sie die verzerrende Wirkung des Data Mining nicht berücksichtigen.
- Das Hauptziel der Fallstudie war, mit White’s Reality Check und der Monte-Carlo-Permutation zu zeigen, wie dieser Data-Mining-Bias bei der Bewertung zu behandeln ist.
- Die Fallstudie zeigte nachdrücklich, wie wichtig Signifikanztests sind, die mit dem Data-Mining-Bias umgehen können.
- Keine der 6.402 Regeln hatte eine Backtest-Mittelrendite, die bei einem Signifikanzniveau von 0,05 die Nullhypothese verwerfen ließ.
- Der erwartete Höchstwert der mittleren Rendite unter 6.402 Regeln ohne Vorhersagekraft liegt unter diesen Bedingungen bei etwa 11 Prozent und nicht bei 0 Prozent.
- Die beste Regel lag mit 10,25 Prozent annualisierter Rendite unter diesem Zentrum; die p-Werte waren 0,8164 beim Reality Check und 0,8194 bei der Monte-Carlo-Permutation.
- Wiederholte Besuche des Testsets, um die Regel optimaler Komplexität zu finden, erzeugen eine positive Verzerrung, den Data-Mining-Bias.
- Die technische Analyse hat nur einen Bestand an Markthistorie, der immer wieder benutzt wird, und kann anders als experimentelle Wissenschaften keine neuen Beobachtungsstichproben erzeugen. Das trägt zum Data-Mining-Bias bei.
- Je mehr Regeln an einem gegebenen Datenbestand getestet werden, desto wahrscheinlicher passt eine Regel nur zufällig zu den Daten.
- Wegen dieses Problems sind Inferenzverfahren nötig, die den Data-Mining-Bias berücksichtigen.
- Whites Reality Check for Data Snooping, Proposition 2.1, zeigt: Geht der Stichprobenumfang gegen unendlich, geht die Wahrscheinlichkeit gegen 1,0, dass die Regel mit der höchsten erwarteten Rendite auch die höchste beobachtete Performance hat.
- Kidd und Borsen untersuchen das Nachlassen der Performance technischer Systeme im Verlauf der Out-of-Sample-Daten und schließen, dass dieses Nachlassen nicht am Data-Mining-Bias liegen kann.
- Frühere Beobachtungen lassen sich immer im Nachhinein durch unendlich viele Hypothesen oder Regeln erklären. Welche davon stimmen könnte, zeigen erst Prognosen, die mit neuen Beobachtungen verglichen werden.
- Zufall wird beim Entwurf einiger der stärksten Data-Mining-Algorithmen für komplexe Regelsynthese genutzt. Ein Beispiel sind Random Forests von Leo Breiman.
- Die bias-kompensierten p-Werte waren schlechter als p gleich 0,5, unter anderem weil die Hälfte der 6.402 Regeln inverse Regeln waren.
- Die inversen Regeln garantierten, dass die Hälfte der konkurrierenden Regeln eine negative Rendite hatte und deshalb keine Chance, ein echter Wettbewerber zu sein. Effektiv wurden doppelt so viele Regeln getestet, wie wirklich im Wettbewerb standen.
- Der Test war dadurch übermäßig konservativ: Die Chance eines Fehlers erster Art, also eines fälschlichen Ablehnens der Null, lag unter 0,10, und die Power des Tests, die Null korrekt abzulehnen, war geringer, als wenn die inversen Regeln weggelassen worden wären.
- Die inversen Regeln wurden einbezogen, weil nicht bekannt war, ob die traditionelle Interpretation der technischen Analyse richtig ist.
- Komplexität meint bei der Suche nach Regeln der technischen Analyse die Zahl der getrennten Parameter und der bedingten Anweisungen, die die Regel definieren. Regeln höherer Komplexität haben mehr Parameter und mehr Bedingungen.

## Funktionsweise

- Die extremste lineare Prognose gibt allen Koeffizienten denselben Betrag, nicht notwendig dasselbe Vorzeichen. Faktoren werden zuerst mit In-Sample-Daten in Z-Scores verwandelt, z(i) = (f(i) − Mittelwert von f) / Standardabweichung von f.
- Die Prognose der morgigen Rendite ist der historische Mittelwert der Ein-Tages-Renditen plus ihre historische Standardabweichung mal dem Mittel der mit dem Vorzeichen der historischen Korrelation gewichteten Z-Scores. Das ist Gleichung 1.2, eine vereinfachte Fassung des üblichen Faktormodells.
- Kahneman schreibt 2011 in Thinking, Fast and Slow, Formeln mit gleichem Gewicht für alle Prädiktoren seien oft überlegen, weil Zufälle der Stichprobe sie nicht treffen.
- Die Prognose der absoluten Renditen kann ungenau sein. Die der relativen Renditen zwischen Aktien ist oft gut genug: Long die oberste Dezile, Short die unterste, und die durchschnittliche Portfoliorendite ist oft positiv.
- Geht es nur um die Rangfolge, werden je Faktor die Ränge einer Aktie mit dem Vorzeichen der Korrelation zwischen Faktor und erwarteter Aktienrendite multipliziert und über die Faktoren summiert. Die Gleichungen 1.1 und 1.2 entfallen dann.

## Voraussetzungen


## Anwendung im Trading

- Die Fallstudie milderte den Prior-Research-Snooping-Bias, indem sie keine Regeln ausdrücklich aufnahm, die andere Forscher entdeckt hatten.
- Viele der 6.402 Regeln ähneln vermutlich früher untersuchten, die Ähnlichkeit war aber zufällig und nicht das Ergebnis eines Durchsehens der früheren Forschung.
- Der Regelsatz entstand durch kombinatorische Aufzählung aller Regeln, die innerhalb festgelegter Parameterwerte möglich waren.
- Bei den Trendregeln wurden alle 429 Kombinationen aus 11 möglichen Look-backs des Channel Breakout und 39 Zeitreihen aufgenommen, 11 mal 39.
- Traf eine dieser Regeln zufällig eine früher entdeckte Regel, war die Aufnahme Zufall; so wurde die volle Zahl der bis zur besten Regel untersuchten Regeln berücksichtigt.
- Das Ausbleiben statistisch signifikanter Renditen nach Bereinigung um den Data-Mining-Bias unterstreicht, wie wichtig Inferenzmethoden sind, die die verzerrende Wirkung des Data Mining einrechnen.

## Regeln und Kriterien

- Out-of-Sample-Tests, Cross-Validation und hohe Sharpe Ratios mindern Data-Snooping-Bias. Keine dieser Praktiken ist maßgeblicher als der Walk-Forward-Test.
- Einfache Modelle sind ein einfaches Heilmittel gegen Data-Snooping-Bias.
- Strategien mit hoher Rendite und niedriger Sharpe Ratio lohnen den Backtest nicht, weil die hohe Rendite wahrscheinlich auf Data-Snooping beruht.
- Die Key Points mahnen, den Data-Snooping-Bias im Blick zu behalten, wenn der Hebel direkt an der zusammengesetzten Wachstumsrate der Backtest-Renditen optimiert wird.
- Dieselbe Mahnung gilt für den Test, ob führende Risikoindikatoren wirken.

## Risiken und Grenzen

- Data Snooping gehört zu den Grundfehlern, die die meisten in Zeitschriften veröffentlichten Arbeiten routinemäßig begehen.
- Der Lookback von 20 Handelstagen für die gleitende Hedge Ratio von GLD und USO ist mit dem Wissen im Nachhinein nahe am Optimum gesetzt.
- δ gleich 0,0001 und Ve gleich 0,001 für den Kalman-Filter sind ebenfalls mit dem Wissen im Nachhinein gewählt; das optimale δ lässt sich aus Trainingsdaten bestimmen.
- Dieselben Daten für die Parameteroptimierung und für den Backtest zu verwenden, ist ein Look-ahead Bias, vor dem Kapitel 1 warnt.
- Im Währungspaar-Beispiel wird ein festes Trainingsfenster von 250 Tagen verwendet, weil es im Nachhinein bessere Ergebnisse liefert, während der Look-back für Mittel und Standardabweichung 20 Tage bleibt.
- Weil die langen Haltedauern in der begrenzten Testhistorie nur wenige Trades erzeugen, besteht in diesen Momentum-Ergebnissen das Risiko eines Data-Snooping-Bias.
- Der eigentliche Test der Strategie ist echtes Out-of-Sample-Testing.
- Das Problem ist heimtückisch, weil unbekannt bleibt, wie viele Regeln getestet wurden, um die erfolgreichen Regeln zu finden.
- Weil die Zahl der getesteten Regeln die Größe des Data-Mining-Bias wesentlich mitbestimmt, lässt sich die tatsächliche statistische Signifikanz einer Regel nicht bewerten, die nur wegen früherem Erfolg in ein neues Data Mining aufgenommen wurde.
- Hätte der Autor NASDAQ oder Russell 2000 als Zielmarkt gewählt, weil eine größere Studie dort nützliche Regeln fand, wäre das Snooping früherer Forschung gewesen und hätte die Gültigkeit der erhaltenen p-Werte beeinträchtigt.
- Ohne Kenntnis dieser Studie wären auf NASDAQ oder Russell 2000 gefundene erfolgreiche Regeln legitim entdeckt worden, und die berichteten p-Werte wären zutreffend gewesen.
- Ein gewöhnlicher Signifikanztest, der den Data-Mining-Bias ignoriert, hätte die beste Regel mit einem p-Wert von 0,0005 hochsignifikant erscheinen lassen.
- Etwa 320 der 6.402 Regeln wären konventionell bei 0,05 signifikant erschienen, genau die Zufallserwartung; ein so betriebenes Mining hätte nichts als Narrengold ergeben.
- Nach Wissen des Autors gibt es kein verfügbares Produkt, das komplexe nichtlineare Regeln erzeugt und dabei einen Signifikanztest enthält, der gegen den Data-Mining-Bias robust ist.
- Ohne diesen Schutz bleibt als Schutz nur eine anspruchsvolle Form des Out-of-Sample-Tests mit drei Datensätzen, Training, Test und Evaluation.
- Darf die Suche die Komplexität einer Regel optimieren, steigt die Zahl der betrachteten Regeln stark, und damit die Chance, dass die beste Regel überangepasst ist; das ist ein Beispiel für Data-Mining-Bias.

## Beispiele

- Ein Beispielfaktor für ein positives morgiges Indexvorzeichen ist die heutige Rendite: eine positive heutige Rendite sagt eine positive künftige Rendite voraus. Ein weiterer ist die heutige Änderung des VIX: eine negative Änderung sagt eine positive künftige Rendite voraus.
- Greenblatts Zwei-Faktor-Modell von 2006, die Magic Formula, setzt f(1) auf die Kapitalrendite und f(2) auf die Earnings Yield, kauft die 30 bestplatzierten Aktien und hält sie ein Jahr. Die jährliche Prozentrendite war von 1988 bis 2004 30,8 Prozent, gegenüber 12,4 Prozent für den S&P 500.
- Die hohe Durchschnittsrendite einer Strategie mit Sharpe Ratio 0,3 und zwei Jahren Drawdown-Dauer ist wahrscheinlich das Ergebnis von Data-Snooping-Bias. Die lange Drawdown-Dauer macht es außerdem unwahrscheinlich, dass sie eine Cross-Validation besteht.
- Bei einem neuronalen Netz ist die Zahl der mit In-Sample-Daten anzupassenden Parameter proportional zur Zahl der Knoten. Mit etwa 100 Knoten und damit mindestens 100 Parametern lässt sich jede Zeitreihe anpassen und eine Sharpe Ratio von 6 im Backtest erzielen, vorwärts aber mit wenig oder keiner Vorhersagekraft wegen Data-Snooping-Bias.
- Eine extreme Regel vom Typ 12 beruht auf der Eingabereihe 28, dem 10-Tage-Durchschnitt des Auf-Ab-Volumenverhältnisses, mit einem Schwellenversatz von 10, also oben 60 und unten 40, und einem Look-back der Kanalnormalisierung von 30 Tagen.
- Typ 12 ist short, obwohl der Indikator über der oberen Schwelle liegt, und long zu allen anderen Zeiten.
- Zufall wird in einigen der stärksten Data-Mining-Algorithmen für komplexe Regelsynthese genutzt. Ein Beispiel sind Random Forests von Leo Breiman.

## Unterschiedliche Quellenpositionen

- Gegen den Einwand, Handelsregeln müssten einfach bleiben, um Data-Snooping-Bias zu vermeiden, sagen Anhänger des Complex Event Processing, sie schürften nicht nach beliebigen Regeln, sondern setzten Regeln um, von denen erfahrene Trader bereits wissen, dass sie profitabel sind. Der Autor ist davon nicht völlig überzeugt.
- Hsu und Kuan prüfen 2005 die Profitabilität der technischen Analyse mit Data-Snooping-Kontrollen, Band 3, Nr. 4, Seiten 606–628.
- Markowitz und Xu schlagen 1994 einfache und plausible Korrekturen für Data Mining vor, Journal of Portfolio Management, Herbst 1994, Seiten 60–69.
- Romano und Wolf sowie viele andere Arbeiten verwenden den Begriff Data Snooping für das, was Aronson als Data-Mining-Bias bezeichnet. Ihre Arbeit Stepwise Multiple Testing as Formalized Data Snooping erschien 2005 in Econometrica.
- White verwendet in A Reality Check for Data Snooping den Begriff Data Snooping in der Bedeutung von Data-Mining-Bias, wie das Buch den Begriff benutzt.
- Hsu und Kuan verwenden Data Snooping so, wie Aronson Data Mining verwendet, und justieren den Data-Mining-Bias mit einer Fassung von Whites Reality Check, ohne die von Wolf und Romano vorgeschlagenen Erweiterungen.
- Hansen kommentiert Whites Reality Check und legt einen Test auf überlegene Prognosefähigkeit vor, A Test for Superior Predictive Ability, Journal of Business and Economic Statistics 23 (2005), Seiten 365–380.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 134–153 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-008-p134-p153|S. 134–153]]
- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]
- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 1–20 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-001-p001-p020|S. 1–20]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 58–77 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-004-p058-p077|S. 58–77]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 115–134 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-007-p115-p134|S. 115–134]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 134–153 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-008-p134-p153|S. 134–153]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 153–172 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-009-p153-p172|S. 153–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 191–210 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-011-p191-p210|S. 191–210]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 229–248 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-013-p229-p248|S. 229–248]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 248–267 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-014-p248-p267|S. 248–267]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 267–286 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-015-p267-p286|S. 267–286]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 286–305 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-016-p286-p305|S. 286–305]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 305–324 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-017-p305-p324|S. 305–324]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 324–343 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-018-p324-p343|S. 324–343]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 381–400 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-021-p381-p400|S. 381–400]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 419–438 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-023-p419-p438|S. 419–438]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 457–476 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-025-p457-p476|S. 457–476]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 476–495 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-026-p476-p495|S. 476–495]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]

## Verwandte Themen

- Der Data-Mining-Bias wird für Kapitel 6 angekündigt.
- Der Stichprobenfehler wird in den Kapiteln 4 und 5 behandelt, der Data-Mining-Bias in Kapitel 6.
- Der Data-Mining-Bias wird in Kapitel 6 behandelt.
- Hsu und Kuan untersuchen die Profitabilität der technischen Analyse mit Data-Snooping-Prüfungen in einer 2005 genannten Arbeit, Band 3, Nr. 4, Seiten 606–628.
