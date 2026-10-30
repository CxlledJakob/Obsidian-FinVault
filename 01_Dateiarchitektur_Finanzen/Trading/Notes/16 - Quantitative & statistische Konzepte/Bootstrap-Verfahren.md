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
- Der Bootstrap heißt so, weil er sich scheinbar an den eigenen Stiefelschlaufen hochzieht, um die Form der Stichprobenverteilung anzunähern.
- Das Bootstrap-Verfahren wurde zuerst 1979 von Efron beschrieben und in späteren Arbeiten verfeinert, die Eric Noreen in Computer Intensive Methods for Testing Hypotheses zitiert.
- Es leitet die Stichprobenverteilung der Teststatistik ab, indem aus einer Originalstichprobe mit Zurücklegen neu gezogen wird.
- White's Reality Check, erfunden und patentiert von Halbert White an der University of California in San Diego, nutzt den Bootstrap, um die Stichprobenverteilung zu erzeugen, mit der die statistische Signifikanz der besten durch Data Mining gefundenen Regel geprüft wird.

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
- Bis vor etwa dreißig Jahren, so der Text, gab es keine Alternative zum klassischen Ansatz, die Stichprobenverteilung aus einer einzigen Stichprobe abzuleiten. Jetzt nähert systematisches, vielfaches Resampling dieser einen Stichprobe die Form der Stichprobenverteilung an.
- Das folgende Kapitel stellt zwei computergestützte Verfahren vor, Bootstrap-Resampling und Monte-Carlo-Permutation. Jedes hat Grenzen, wie jede statistische Methode, aber beide sind nützliche Alternativen zum klassischen Ansatz.
- In diesem Buch wird der Bootstrap verwendet, um die Form der Stichprobenverteilung der durchschnittlichen Rendite für Regeln ohne Vorhersagekraft anzunähern.
- Der Autor wählt die Computersimulation, weil der traditionelle Ansatz eine normal geformte Stichprobenverteilung voraussetzt. Trifft das nicht zu, werden die Schlüsse ungenau.
- Monte-Carlo-Permutation und Bootstrap werden beide in der Fallstudie von Teil 2 verwendet.
- Das Bootstrap-Theorem sichert unter vernünftigen Bedingungen zu, dass das Verfahren mit gegen unendlich wachsender Stichprobengröße gegen die richtige Stichprobenverteilung konvergiert.
- Praktisch genügt damit eine einzige Stichprobe, um die Signifikanz einer Regel der technischen Analyse zu prüfen.
- In der Grundform eignet sich der Bootstrap nicht dazu, die statistische Signifikanz von Regeln zu bewerten, die durch Data Mining entdeckt wurden.
- Halbert White, Professor für Wirtschaft an der University of California in San Diego, erweiterte den Bootstrap dafür patentiert; die Software heißt Forecaster's Reality Check, wird in Kapitel 6 besprochen und in Kapitel 9 auf über 6.000 Regeln für den S&P 500 angewandt.
- Die für Regeltests geeignete Bootstrap-Methode ist nur bei ihrem Entwickler Quantmetrics erhältlich.
- Die vom Bootstrap geprüfte Nullhypothese besagt, dass der Erwartungswert der Regelrenditen in der Grundgesamtheit null oder kleiner ist.
- Der Bootstrap nutzt eine tägliche Historie der Regelrenditen.
- Die Stichprobenverteilung von White’s Reality Check für die beste von 6.402 wertlosen Regeln entstand aus 1.999 Wiederholungen des Bootstrap-Verfahrens.
- Eine größere Zahl von Wiederholungen hätte die Form der Verteilung glatter gemacht, die Schlussfolgerung aber nicht geändert, dass die Leistung der Regel nicht reichte, die Nullhypothese zu verwerfen.
- Figur 9.1 zeigt diese Bootstrap-Verteilung; die beste Regel E-12-28-10-30 mit 10,25 Prozent annualisierter Rendite hat darin den p-Wert 0,8164.
- Die Stichprobenverteilung in Figur 9.3, passend zum Backtest einer einzelnen Regel bei ignoriertem Data-Mining-Bias, ist eine Bootstrap-Verteilung und bei null zentriert.
- Der Pfeil in dieser Figur ist die mittlere Rendite der besten Regel E-12-28-10-30, und der zugehörige p-Wert beträgt 0,0005.
- Die Spalte SR Boot in Tabelle 9.1 ist der Einzelregel-p-Wert per Bootstrap und berücksichtigt den Data-Mining-Bias nicht.
- B, als boot bezeichnet, ist eine verbesserte Fassung von White’s Reality Check und übernimmt die Erweiterung von Wolf und Romano, die die Power des Tests erhöhen und die Chance eines Fehlers zweiter Art senken soll.
- RC ist die bei Quantmetrics verfügbare Fassung des Reality Check ohne die Erweiterung von Wolf und Romano.
- Die Grenzen der 80-Prozent-Konfidenzintervalle wurden mit einem Algorithmus berechnet, den Wolf und Romano beschreiben; den Computercode implementierte Tim Masters.

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
- Womit die Stichprobenverteilung auch erzeugt wird, sie sagt, wie weit die gebacktestete Rendite einer nicht vorhersagenden Regel durch Zufallseffekte der Stichprobe über oder unter null schwanken kann, und dient als Maßstab. Ist die mittlere Rendite zu hoch für diese Stichprobenvariabilität, wird der Regel Vorhersagekraft zugesprochen.
- Vor dem Ziehen werden die Tagesrenditen nullzentriert: Der mittlere Tagesertrag wird von jedem Tagesertrag abgezogen, damit der Mittelwert null ist und die Daten der Nullhypothese entsprechen.
- Die Nullzentrierung ist nicht die Trendbereinigung.
- Jede Resample muss exakt so viele Beobachtungen enthalten wie die Originalstichprobe, sonst gilt das Bootstrap-Theorem nicht; in der Abbildung sind das 1.231 Beobachtungen.
- Gezogen wird mit Zurücklegen: Ein gezogener Tagesertrag wird notiert und zurückgelegt, sodass er in einer Resample mehrfach oder gar nicht vorkommen kann.
- Es werden 5.000 Resamples gebildet, für jede der Mittelwert berechnet, und aus diesen 5.000 Mittelwerten entsteht die Stichprobenverteilung des Mittelwerts.
- Der p-Wert ist der Anteil dieser 5.000 Mittelwerte, die den beobachteten mittleren Ertrag der Regel erreichen oder übertreffen.
- Bei der Perzentilmethode werden die Regelrenditen 5.000 Mal neu gezogen und für jede Ziehung ein Mittelwert berechnet.
- Die 5.000 Mittelwerte werden vom höchsten zum niedrigsten geordnet, und es werden die höchsten x Prozent und die niedrigsten x Prozent entfernt, wobei x die Differenz aus 100 und dem gewünschten Konfidenzniveau ist, geteilt durch 2.
- Für ein 90-Prozent-Intervall werden die 250 höchsten und die 250 niedrigsten der 5.000 Mittelwerte entfernt; der höchste verbleibende Mittelwert ist die Obergrenze, der niedrigste die Untergrenze.
- Für ein 99-Prozent-Intervall werden nur die höchsten 25 und die niedrigsten 25 Werte entfernt, also je 0,5 Prozent von 5.000.
- Ist die Stichprobenverteilung schief, gibt es Bootstrap-Verfahren, die sie schwenken, um den Widerspruch zum Hypothesentest zu mildern; diese anderen Methoden können eigene Probleme haben.
- Vor diesem Verfahren konnte der Bootstrap nur die Signifikanz einer einzelnen Regel prüfen; Whites patentierte Neuerung erzeugt die Stichprobenverteilung der besten von N Regeln unter der Annahme, dass alle Regeln eine erwartete Rendite von null haben.
- Die Software ist bei Quantmetrics erhältlich, der Firma von White.
- Im vereinfachten Beispiel werden zwei Regeln über 10 Handelstage getestet: Regel 1 mit mittlerer Tagesrendite 1 Prozent und Regel 2 mit 2 Prozent; gewählt wird Regel 2.
- Zehn nummerierte Zettel werden mit Zurücklegen zehnmal gezogen, weil das die Länge jeder Performancehistorie ist und das Bootstrap-Theorem das verlangt; ein Beispielzug ist 5, 3, 5, 5, 7, 2, 5, 8, 1, 2.
- Aus den tatsächlichen Tagesrenditen dieser Daten wird für jede Regel eine zufällige Pseudo-Historie der Länge 10 gebildet.
- White's Reality Check zieht von jeder Tagesrendite die mittlere Tagesrendite der jeweiligen Regel ab, im Beispiel 1 Prozent bei Regel 1 und 2 Prozent bei Regel 2, und zentriert so die Verteilung der Tagesrenditen über null.
- Die adjustierten Renditen beider Regeln an den gezogenen Tagen werden gemittelt, und der größere der beiden Mittelwerte ist der erste Wert der Stichprobenverteilung der maximalen mittleren Rendite von N Regeln.
- Die Ziehung und Auswertung werden viele Male wiederholt, zum Beispiel 500-mal oder öfter, und aus diesen Werten entsteht die Stichprobenverteilung der maximalen mittleren Rendite in einem Universum von N Regeln mit erwarteter Rendite null.
- Der p-Wert ist der Anteil dieser Werte, der die durchschnittliche Rendite der getesteten Regel übersteigt.
- Das Beispiel ist absichtlich stark vereinfacht; ein realistischer Fall würde viel mehr Regeln über einen viel längeren Zeitraum prüfen.
- Bei mehr Regeln und längerer Historie bleibt das Verfahren zur Stichprobenverteilung dasselbe; die Software von White's Reality Check erledigt es automatisch, sobald sie die Intervallrenditen aller getesteten Regeln erhält, zum Beispiel die Tagesrenditen.
- Dieser Datensatz enthält alles, was das Verfahren für die zu diesem Data-Mining-Vorhaben passende Stichprobenverteilung braucht.
- Bei vielen Regeln ist das eine beträchtliche Datenmenge, und derzeit speichern wenige Data Miner oder Data-Mining-Systeme diese Information.
- Der Bootstrap verwendet die Intervallrenditen der Regel, die Monte-Carlo-Permutation dagegen die historische Reihe der Regelausgaben +1 und −1 sowie die rohen Marktrenditen.
- Damit die Null erwarteter Rendite null gilt, bestimmt White's Reality Check die mittlere Tagesrendite jeder Regel und zieht sie von jeder einzelnen Tagesrendite ab; im Beispiel werden bei Regel 1 ein Prozent und bei Regel 2 zwei Prozent abgezogen, sodass die Verteilung der Tagesrenditen über null zentriert ist.

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
- Hansen zeigt, dass White's Reality Check und in der Folge die Monte-Carlo-Permutation an Power verlieren, wenn das Universum Regeln enthält, die schlechter als die Benchmark sind.
- Eine kommerzielle Version von White's Reality Check mit der Erweiterung von Romano und Wolf gibt es derzeit nicht.

## Beispiele

- Drei Labels hängen an den Renditen von 0 bis 3, von 2 bis 4 und von 4 bis 6. Startwahrscheinlichkeit ist jeweils ein Drittel; nach erstem Zug der 2 sind die Wahrscheinlichkeiten der zweiten Ziehung 5/14, 3/14 und 6/14.
- Die kleinste Wahrscheinlichkeit trifft das schon gezogene Feature, weil die Überlappung dort am größten wäre; unter den übrigen erhält das zur bisherigen Sequenz nicht überlappende dritte Label die größte Wahrscheinlichkeit.
- Ein Monte Carlo mit einer Million Iterationen, 10 Beobachtungen, 100 Bars und maximaler Weite 5 dauert auf einem Server mit 24 Kernen etwa sechs Stunden und ohne Parallelisierung etwa sechs Tage.
- Bei TT-4-91 wird der mittlere Tagesertrag von ungefähr 0,0192 Prozent von jedem Tagesertrag abgezogen, danach wird mit Zurücklegen genau 6.800 Mal gezogen, und das Bilden von Resample und Mittelwert wird 5.000 Mal wiederholt.
- Der p-Wert 0,0692 bedeutet, dass 0,069 der 5.000 Bootstrap-Mittelwerte mindestens plus 4,84 Prozent betrugen; wäre die erwartete Rendite wirklich null, träte das etwa 7 von 100 Mal allein durch Zufall auf.
- Für TT-4-91 liegt das 80-Prozent-Intervall auf der bei der beobachteten Rendite von plus 4,84 Prozent positionierten Bootstrap-Verteilung zwischen plus 0,62 und plus 9,06 Prozent.
- Würde TT-4-91 auf 100 unabhängigen Stichproben gebacktestet und um jede mittlere Rendite ein 80-Prozent-Intervall gelegt, schlösse das Intervall in ungefähr 80 Stichproben die wahre erwartete Rendite ein.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 77–96 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-005-p077-p096|S. 77–96]]
- Advances in Financial Machine Learning.pdf, S. 115–134 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-007-p115-p134|S. 115–134]]
- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 210–229 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-012-p210-p229|S. 210–229]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 229–248 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-013-p229-p248|S. 229–248]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 248–267 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-014-p248-p267|S. 248–267]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 305–324 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-017-p305-p324|S. 305–324]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 324–343 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-018-p324-p343|S. 324–343]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 419–438 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-023-p419-p438|S. 419–438]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]

## Verwandte Themen
