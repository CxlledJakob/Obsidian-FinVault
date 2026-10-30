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

# Bootstrap-Verfahren


## Kurzdefinition

- Bootstrap meint hier Ziehen mit Zurücklegen; der sequenzielle Bootstrap ändert die Ziehungswahrscheinlichkeiten nach jeder Ziehung, damit überlappende Outcomes unwahrscheinlicher werden.
- Bootstrap-Aggregation erzeugt N Trainingsmengen durch zufälliges Ziehen mit Zurücklegen und passt auf jede Menge einen eigenen Schätzer an.
- Die Verteilung der Trefferwahrscheinlichkeit wird durch Ziehen mit Zurücklegen aus den historischen Wettenergebnissen geschätzt.

## Kernaussagen

- Die Wahrscheinlichkeit, ein bestimmtes Element nach I Ziehungen mit Zurücklegen aus I Elementen nicht zu treffen, geht mit wachsender Stichprobe gegen e hoch minus 1; erwartet werden damit etwa zwei Drittel eindeutige Beobachtungen.
- Gibt es höchstens K nicht überlappende Outcomes und ist K kleiner oder gleich I, sinkt die erwartete Zahl eindeutiger Ziehungen auf 1 minus e hoch minus K/I und liegt damit höchstens bei 1 minus e hoch minus 1.
- Die fälschliche Annahme identisch und unabhängig verteilter Ziehungen führt deshalb zu Oversampling.
- Ist die mittlere durchschnittliche Eindeutigkeit weit unter 1, werden die gezogenen Beobachtungen redundant zueinander und den nicht gezogenen sehr ähnlich.
- Der Bootstrap wird dadurch ineffizient: In einem Random Forest sind die Bäume im Wesentlichen Kopien eines einzelnen überangepassten Entscheidungsbaums, und die Out-of-Bag-Genauigkeit wird stark überschätzt.
- Überlappende Outcomes vor dem Ziehen zu verwerfen, wird nicht empfohlen, weil die Überlappung unvollständig ist und der Informationsverlust extrem wäre.
- Besser ist, nur einen Anteil in Höhe der mittleren Eindeutigkeit oder ein kleines Vielfaches davon zu ziehen.
- Random Forests bieten dafür keinen max_samples-Parameter; als Ausweg nennt der Text, eine große Zahl von Entscheidungsbäumen zu baggen.
- Rao, Pathak und Koltchinskii schlagen 1997 sequenzielles Resampling mit Zurücklegen vor, bis K verschiedene Originalbeobachtungen erscheinen; dieses Schema passt auf überlappende Finanz-Outcomes nicht vollständig.
- Beim sequenziellen Bootstrap bleiben Überlappungen und Wiederholungen erlaubt, werden aber immer unwahrscheinlicher, sodass die Stichprobe näher an unabhängigen Ziehungen liegt als der gewöhnliche Bootstrap.
- Das zeigt sich an einer höheren mittleren durchschnittlichen Eindeutigkeit gegenüber dem Standard-Bootstrap.
- Im Monte-Carlo-Vergleich liegt der Median dieser Eindeutigkeit beim Standardverfahren bei 0,6 und beim sequenziellen Verfahren bei 0,7.
- Ein ANOVA-Test der Mittelwertdifferenz hat eine verschwindend kleine Wahrscheinlichkeit; die erwartete Eindeutigkeit des sequenziellen Bootstrap ist damit auf jedem vernünftigen Konfidenzniveau höher.
- Die Schätzer werden unabhängig voneinander angepasst und können deshalb parallel trainiert werden. Die Ensemble-Prognose ist der einfache Durchschnitt der einzelnen Prognosen.
- Bei kategorialen Variablen ist die Klassenwahrscheinlichkeit der Anteil der Schätzer, die so klassifizieren. Kann der Basisschätzer Wahrscheinlichkeiten liefern, darf stattdessen deren Mittel verwendet werden.
- Die Varianz der gebaggten Prognose ist die mittlere Einzelvarianz mal (mittlere Korrelation plus (1 minus diese Korrelation) geteilt durch N).
- Bagging senkt diese Varianz nur, solange die mittlere Korrelation unter 1 liegt. Geht die Korrelation gegen 1, geht die Varianz gegen die eines einzelnen Schätzers.
- Der sequenzielle Bootstrap aus Kapitel 4 soll möglichst unabhängige Stichproben erzeugen, die mittlere Korrelation senken und damit die Varianz von Bagging-Klassifikatoren verringern.
- Redundante Beobachtungen machen Ziehungen mit Zurücklegen nahezu identisch, auch wenn nicht dieselben Beobachtungen gezogen werden. Dann liegt die Korrelation nahe 1, und die Varianz sinkt unabhängig von N nicht.
- Dieselbe Redundanz bläht die Out-of-Bag-Genauigkeit auf, weil die Trainingsziehung den nicht gezogenen Beobachtungen sehr ähnlich ist.
- Eine stratifizierte k-Fold-Prüfung ohne Mischen vor der Aufteilung zeigt dann eine deutlich niedrigere Testgenauigkeit als die Out-of-Bag-Schätzung.
- Anders als allgemeines Bagging setzt der Random Forest die Größe jeder Bootstrap-Stichprobe immer gleich der Größe der Trainingsmenge.
- Sind viele Stichproben redundant, entstehen so zahlreiche im Wesentlichen gleiche Bäume, und jeder einzelne Baum ist überangepasst.
- Beim BaggingClassifier von sklearn ist die Berechnung der Out-of-Bag-Genauigkeit von einem Fehler betroffen. Ein Workaround ist, die Labels in fortlaufende ganze Zahlen umzubenennen.

## Funktionsweise

- Die erste Ziehung ist gleichverteilt, jeder Index hat anfänglich die Wahrscheinlichkeit 1/I.
- Für jede weitere Ziehung wird die durchschnittliche Eindeutigkeit jedes Kandidaten neu berechnet, die entstünde, wenn man ihn zur bisherigen Sequenz hinzunähme, und daraus werden Wahrscheinlichkeiten gebildet, die sich zu 1 addieren.
- Das wird wiederholt, bis I Ziehungen stattgefunden haben.
- Die Indikator-Matrix ist binär und zeigt, welche Preisbars das Label einer Beobachtung beeinflussen.
- Die Gleichzeitigkeit einer Bar ist die Spaltensumme dieser Matrix; die Eindeutigkeit teilt den Indikator durch diese Summe, und die durchschnittliche Eindeutigkeit ist der Mittelwert der positiven Werte.
- Dieselbe durchschnittliche Eindeutigkeit lässt sich als Kehrwert des harmonischen Mittels der Zahl gleichzeitiger Labels über die Lebensdauer des Events lesen.
- Der Eindeutigkeitsscore liegt zwischen 0 und 1 und misst den Anteil nicht überlappender Outcomes.
- Er benutzt das erst später bekannte Label-Ende, wird aber nur zusammen mit den Labels im Training verwendet und nicht zur Prognose des Labels; deshalb sieht der Text darin kein Informationsleck.
- Zuerst werden N Trainingsmengen mit Zurücklegen gezogen, dann wird auf jede Menge ein Schätzer angepasst, und zuletzt werden die Prognosen gemittelt oder per Mehrheitsvotum zusammengefasst.
- Eine der genannten Abhilfen ersetzt im Random Forest den gewöhnlichen Bootstrap durch den sequenziellen Bootstrap.
- In jedem Durchlauf wird eine abgerundete Zahl von Ergebnissen gezogen, nämlich jährliche Wettfrequenz mal Beurteilungsdauer in Jahren.
- Die Beurteilungsdauer ist der Horizont, über den Investoren eine Strategie beurteilen, im Beispiel zwei Jahre.
- Die Trefferwahrscheinlichkeit eines Durchlaufs ist der Anteil der gezogenen Ergebnisse mit positivem Gewinn.
- Auf die so gewonnenen Trefferwahrscheinlichkeiten wird ein Kerndichteschätzer angepasst.
- Für eine hinreichend lange Beurteilungsdauer nähert der Text die Dichte der gezogenen Trefferwahrscheinlichkeiten durch eine Normalverteilung an, mit Mittelwert gleich der beobachteten Trefferquote und zweitem Parameter gleich dem Produkt aus dieser Quote und eins minus der Quote.
- Die Implementierung ersetzt die Ziehungsschleife durch die Normalnäherung und wertet diese an der kritischen Trefferwahrscheinlichkeit mit Mittelwert p und dem Argument p mal (1 minus p) aus.

## Voraussetzungen


## Anwendung im Trading

- Überlappende Labels sind der im Text genannte Grund, in Finanzdaten nicht unverändert mit dem Standard-Bootstrap zu baggen, sondern die Stichprobe nach der Eindeutigkeit zu begrenzen oder sequenziell zu ziehen.

## Regeln und Kriterien

- Im BaggingClassifier von sklearn kann max_samples auf die mittlere Eindeutigkeit out['tW'].mean() gesetzt werden, damit nicht deutlich häufiger gezogen wird, als die Beobachtungen eindeutig sind.
- Wird jede Beobachtung zum Zeitpunkt t nach der Rendite bis t plus 100 gelabelt, soll je gebaggtem Schätzer 1 Prozent der Beobachtungen gezogen werden, aber nicht mehr.
- Für die Kreuzvalidierung wird StratifiedKFold mit shuffle gleich False empfohlen; die Out-of-Bag-Genauigkeit soll ignoriert werden.
- Ein kleines k ist einem großen vorzuziehen, weil eine zu feine Aufteilung erneut zu ähnliche Beobachtungen in Training und Test legt.
- max_samples kann auf die mittlere Eindeutigkeit gesetzt werden, sowohl beim Bagging von Entscheidungsbäumen als auch beim Bagging von Random Forests mit einem Baum je Ziehung.
- max_features niedriger zu setzen, zwingt die Bäume auseinander. Ein min_weight_fraction_leaf von etwa 5 Prozent soll die Out-of-Bag-Genauigkeit an die k-Fold-Genauigkeit außerhalb der Stichprobe heranführen.

## Risiken und Grenzen

- Bei redundanten Finanzbeobachtungen bleibt die Varianzreduktion des Bootstrap aus, und die Out-of-Bag-Genauigkeit ist nach oben verzerrt.
- Der Random Forest kann die Ziehung nicht kleiner machen als das Trainingsset; bei niedriger Eindeutigkeit überanpasst er deshalb weiterhin.

## Beispiele

- Drei Labels hängen an den Renditen von 0 bis 3, von 2 bis 4 und von 4 bis 6. Startwahrscheinlichkeit ist jeweils ein Drittel; nach erstem Zug der 2 sind die Wahrscheinlichkeiten der zweiten Ziehung 5/14, 3/14 und 6/14.
- Die kleinste Wahrscheinlichkeit trifft das schon gezogene Feature, weil die Überlappung dort am größten wäre; unter den übrigen erhält das zur bisherigen Sequenz nicht überlappende dritte Label die größte Wahrscheinlichkeit.
- Ein Monte Carlo mit einer Million Iterationen, 10 Beobachtungen, 100 Bars und maximaler Weite 5 dauert auf einem Server mit 24 Kernen etwa sechs Stunden und ohne Parallelisierung etwa sechs Tage.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 77–96 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-005-p077-p096|S. 77–96]]
- Advances in Financial Machine Learning.pdf, S. 115–134 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-007-p115-p134|S. 115–134]]
- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]

## Verwandte Themen
