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
aktualisiert: 2026-10-30
---

# Konfidenzintervall


## Kurzdefinition

- Ein Konfidenzintervall ist ein Bereich, der den wahren Wert des Populationsparameters mit einem festgelegten Konfidenzniveau enthält.
- Ein Konfidenzintervall ist eine Intervallschätzung: eine Spanne um die Punktschätzung mit einer Unter- und einer Obergrenze und einer Wahrscheinlichkeit, dass der wahre Parameterwert darin liegt.
- Die Wahrscheinlichkeit wird üblicherweise als Prozentzahl genannt; ein 90-Prozent-Intervall für den Mittelwert schließt den wahren Mittelwert der Grundgesamtheit mit Wahrscheinlichkeit 0,90 ein.
- Die oberen und unteren Grenzen der 80-Prozent-Konfidenzintervalle beruhen auf der mathematischen Theorie, die White zuerst vorschlug, und auf einem Algorithmus, den Wolf und Romano beschreiben.
- Den Computercode für diese Intervalle implementierte Tim Masters.
- Der Standardfehler ist die Standardabweichung der Stichprobenmittel um den Populationsmittelwert, wenn viele unabhängige Stichproben aus derselben Population gezogen werden.

## Kernaussagen

- Die Schlussstufe der hypothetisch-deduktiven Methode entscheidet anhand des Grades der Übereinstimmung von Beobachtung und Vorhersage über Wahrheit oder Falschheit der Hypothese und verwendet dafür statistische Inferenz, darunter Konfidenzintervalle und Hypothesentests.
- Die Parameterschätzung ist neben dem Hypothesentest die zweite Form statistischer Inferenz. Sie nutzt die Stichprobe, um den ungefähren Wert eines Populationsparameters zu bestimmen. Der Test sagt, ob ein Effekt vorliegt, die Schätzung etwas über seine Größe.
- Schätzung und Test springen beide vom sicheren Stichprobenwert zum unsicheren Populationsparameter und können beide irren. Die Schätzung ist kühner und potenziell nützlicher, weil sie nicht nur eine konkrete Behauptung annimmt oder verwirft, sondern den Parameter annähert und einen Bereich zu einer festgelegten Wahrscheinlichkeit angibt.
- Eine solche Aussage enthält zwei Schätzungen: eine Punktschätzung und eine Intervallschätzung.
- Die Breite des Konfidenzintervalls wird aus derselben Stichprobenverteilung abgeleitet, die für den Hypothesentest verwendet wird.
- Die Regelstudien in Teil 2 verwenden die Schätzung als Ergänzung zu den Hypothesentests.
- Statt nur zu sagen, ob eine durchschnittliche Rendite kleiner oder gleich null anzunehmen oder zu verwerfen ist, nähert die Schätzung die durchschnittliche Rendite an und nennt einen Bereich, in dem die wahre Rendite mit einer festgelegten Wahrscheinlichkeit liegen soll.
- Bildet man viele 90-Prozent-Intervalle aus unabhängigen Stichproben, umschließen etwa 90 Prozent den Parameter und etwa 10 Prozent verfehlen ihn.
- In der Abbildung mit zehn solchen Intervallen verfehlt eines den mit μ bezeichneten wahren Mittelwert der Grundgesamtheit.
- Das Niveau ist wählbar; ein 99-Prozent-Intervall enthält den wahren Mittelwert mit Wahrscheinlichkeit 0,99, ist aber breiter, höhere Sicherheit kostet also Präzision.
- Das breitere 99-Prozent-Intervall beseitigt in der Abbildung den Fehler, den das 90-Prozent-Intervall gemacht hat.
- Eine Punktschätzung zeigt die Unsicherheit durch den Stichprobenfehler nicht; das Konfidenzintervall verbindet sie mit der Stichprobenverteilung des Schätzers.
- Der Stichprobenmittelwert ist der unbekannte Mittelwert der Grundgesamtheit plus oder minus den Stichprobenfehler, und der Mittelwert der Grundgesamtheit ist der bekannte Stichprobenmittelwert plus oder minus den Stichprobenfehler.
- Wird 1.000 Mal ein Stichprobenmittelwert mit einem 90-Prozent-Intervall gebildet, liegt der Mittelwert der Grundgesamtheit in ungefähr 900 der 1.000 Intervalle.
- Die Breite des Intervalls wird aus der Breite der Stichprobenverteilung abgeleitet, derselben Verteilung, aus der die p-Werte des Hypothesentests kommen.
- Beim Hypothesentest ist diese Verteilung auf den hypothetischen Mittelwert zentriert, etwa auf null; beim Konfidenzintervall ist sie auf den Stichprobenmittelwert zentriert, etwa auf 7 Prozent.
- Bootstrapping kann Konfidenzintervalle erzeugen, und die Prozedur gleicht fast derjenigen für die Stichprobenverteilung eines Hypothesentests.
- Zur Berechnung gibt es zahlreiche Bootstrap-Methoden; die hier vorgestellte Perzentilmethode ist verbreitet, leicht anzuwenden und im Allgemeinen gut, anspruchsvollere Methoden liegen außerhalb dieses Textes.
- Die Monte-Carlo-Permutation kann keine Konfidenzintervalle erzeugen.
- Die Monte-Carlo-Permutation kann keine Konfidenzintervalle bilden, weil sie keinen Populationsparameter schätzt, sondern prüft, ob die langen und kurzen Positionen der Regel Information über künftige Marktänderungen enthalten.
- Hypothesentest und Konfidenzintervall können widersprechen, weil der Test den rechten und das Intervall den linken Schwanz betrachtet.
- Es ist möglich, dass die Untergrenze eines 90-Prozent-Intervalls eine Wahrscheinlichkeit von 5 Prozent für eine erwartete Rendite unter null anzeigt und ein Test zum Niveau 0,05 die Null zugleich verwirft.
- Theoretisch sollten beide zum selben Schluss kommen: Eine Untergrenze unter 0 Prozent beim 90-Prozent-Intervall ginge mit einem Nichtverwerfen zum Niveau 0,05 einher.
- Der Widerspruch entsteht bei schiefer Stichprobenverteilung.
- Nach dem Zentralen Grenzwertsatz ist die Stichprobenverteilung des Mittelwerts bei großer Stichprobe nicht ernsthaft schief, sodass dieses Problem die hier mit dem Stichprobenmittelwert geführte Forschung nicht trifft.
- Bei anderen Kennzahlen können schwenkende Bootstrap-Verfahren den Widerspruch bei Asymmetrie mildern, haben aber eigene Probleme; die mittlere Rendite bleibt deshalb eine attraktive Kennzahl.
- Der Schluss von der Backtest-Leistung auf die erwartete Leistung wird entweder als Konfidenzintervall oder als Hypothesentest gezogen.
- Seine Genauigkeit hängt davon ab, ob der Fehler unverzerrt oder systematisch ist, und von seiner Größe.
- Beim Backtest einer einzelnen Regel ist die mittlere Rendite unverzerrt, ein Konfidenzintervall unterliegt dann nur der Stichprobenvariabilität.
- Die Stichprobenverteilung, die für einen einzelnen Stichprobenmittelwert oder für sein Konfidenzintervall richtig wäre, ist falsch, wenn die Statistik das Maximum vieler Mittelwerte ist.
- Werden die fünf Faktoren berücksichtigt, die die Zufälligkeit eines Data-Mining-Vorhabens festlegen, lässt sich ein Konfidenzintervall für eine durch Data Mining entdeckte Regel berechnen.
- Diese Verfahren mildern das Kernproblem objektiver Techniker, die Data Mining zur Erkenntnisgewinnung nutzen.
- Randomisierungsmethoden erlauben Signifikanztests, und manchmal lassen sich näherungsweise Konfidenzintervalle erzeugen.
- Weil ein Walk-Forward typischerweise viele Folds und damit viele Out-of-Sample-Schätzungen liefert, lässt sich die Varianz der Performancestatistik bestimmen und daraus ein Konfidenzintervall berechnen.

## Funktionsweise

- Bei der Bootstrap-Perzentilmethode entstehen 5.000 Mittelwerte aus wiederholtem Ziehen; sie werden vom höchsten zum niedrigsten geordnet.
- Entfernt werden die höchsten x Prozent und die niedrigsten x Prozent, mit x als Differenz aus 100 und dem gewünschten Konfidenzniveau, geteilt durch 2.
- Für 90 Prozent werden die 250 höchsten und die 250 niedrigsten von 5.000 Mittelwerten entfernt; der höchste verbleibende Wert ist die Obergrenze, der niedrigste die Untergrenze.
- Für 99 Prozent werden nur die höchsten 25 und die niedrigsten 25 Werte entfernt, also je das oberste und das unterste halbe Prozent.
- Die ausgewiesenen Konfidenzintervalle berücksichtigen den Data-Mining-Bias vollständig.
- Es sind gemeinsame Konfidenzintervalle, deren obere und untere Grenzen die wahre Rendite aller Regeln mit einer Wahrscheinlichkeit von 0,80 enthalten.
- Würde man die Fallstudie auf 1.000 unabhängigen Datensätzen wiederholen, was unpraktisch ist, weil es nur einen historischen Marktdatensatz gibt, enthielten in 800 dieser Tests die 6.402 Intervalle die erwarteten Renditen aller Regeln.
- Tabelle 9.1 gibt für die 100 Regeln mit der höchsten mittleren Rendite die untere und die obere 80-Prozent-Grenze in den Spalten 8 und 9 an.
- Die ersten dort genannten 80-Prozent-Grenzen sind −0,02932 und 0,23527, bei der Regel E-12-28-10-30 mit der Rendite 0,102501.
- Efron und Tibshirani behandeln Bootstrap-Verfahren für Standardfehler, Konfidenzintervalle und andere Maße der statistischen Genauigkeit.
- Efron wird mit Better Bootstrap Confidence Intervals als Quelle für Bootstrap-Konfidenzintervalle angeführt.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Die Monte-Carlo-Permutation kann im Vergleich zu White's Reality Check keine Konfidenzintervalle erzeugen, weil sie keine Hypothese über die mittlere Rendite der Regel testet; ihre Null lautet nur, dass die Ausgaben aller getesteten Regeln zufällig mit dem künftigen Marktverhalten korreliert sind.

## Beispiele

- Ist die beobachtete mittlere Rendite einer Regel 15 Prozent, könnte das 95-Prozent-Konfidenzintervall anzeigen, dass die wahre Rendite zwischen 5 und 25 Prozent liegt. Die Breite beträgt in diesem Fall 20 Prozentpunkte.
- Ein anderes Beispiel nennt eine geschätzte Rendite von 10 Prozent und eine Wahrscheinlichkeit von 95 Prozent, dass sie im Bereich von 5 bis 15 Prozent liegt.
- Bei einer Backtest-Rendite von 7 Prozent kann mit Wahrscheinlichkeit 0,90 gesagt werden, dass die erwartete Rendite zwischen 2 und 12 Prozent liegt.
- Wird eine Regel auf hundert unabhängigen Stichproben gebacktestet und um jede mittlere Rendite ein 90-Prozent-Intervall gelegt, enthalten ungefähr 90 Prozent der Intervalle die wahre oder erwartete Rendite.
- In der nach links schiefen Abbildung ist der Test zum Niveau 0,05 signifikant, die Untergrenze des 90-Prozent-Intervalls liegt aber unter einer Rendite von null.
- Für TT-4-91 liegt die Untergrenze des 80-Prozent-Intervalls bei plus 0,62 Prozent und die Obergrenze bei plus 9,06 Prozent, bei beobachteter Backtest-Rendite von plus 4,84 Prozent.
- Würde die Regel auf 100 unabhängigen Stichproben gebacktestet und je ein 80-Prozent-Intervall um die mittlere Rendite gelegt, wäre die wahre erwartete Rendite in ungefähr 80 Stichproben eingeschlossen.
- Das im Text gemeinte Intervall ist das Konfidenzintervall von zwei Standardabweichungen für den Anteil von Kopf bei 100.000 Münzwürfen.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 134–153 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-008-p134-p153|S. 134–153]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 210–229 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-012-p210-p229|S. 210–229]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 229–248 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-013-p229-p248|S. 229–248]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 248–267 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-014-p248-p267|S. 248–267]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 267–286 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-015-p267-p286|S. 267–286]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 305–324 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-017-p305-p324|S. 305–324]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 324–343 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-018-p324-p343|S. 324–343]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 476–495 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-026-p476-p495|S. 476–495]]

## Verwandte Themen

- Konfidenzintervalle und Hypothesentests werden für die Kapitel 4 und 5 angekündigt.
