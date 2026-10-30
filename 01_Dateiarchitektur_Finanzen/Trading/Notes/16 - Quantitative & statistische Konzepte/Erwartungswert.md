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

# Erwartungswert


## Kurzdefinition

- Der erwartete Wert der zusammengesetzten Wachstumsrate als Funktion des Hebels f ist bei risikofreiem Zins null der Durchschnitt von log(1 plus f mal R).
- Die erwartete Rendite einer künstlichen Handelsregel ist der Erwartungswert einer Zufallsvariablen: Wahrscheinlichkeit eines profitablen Monats mal durchschnittlicher Gewinn minus Wahrscheinlichkeit eines Verlustmonats mal durchschnittlicher Verlust.
- Der Erwartungswert einer einzelnen Rohrendite, gezogen aus der Grundgesamtheit der historischen Rohrenditen, ist definitionsgemäß der Mittelwert dieser Renditen.
- Der Erwartungswert eines Spiels ist Gewinnwahrscheinlichkeit mal Gewinnbetrag minus Verlustwahrscheinlichkeit mal Verlustbetrag.

## Kernaussagen

- Der Kalman-Filter ist optimal, weil er unter gaußschem Rauschen der beste Schätzer ist und den mittleren quadratischen Fehler der geschätzten Variablen minimiert.
- Der Erwartungswert der verborgenen Variable zur Zeit t ist eine lineare Funktion ihres Erwartungswerts vor der Beobachtung und des beobachteten Werts zur Zeit t.
- Die mathematische Optimalität der Kelly-Allokation über das Gesamtportfolio setzt voraus, dass die erwarteten Renditen und die Volatilitäten der Strategien unverändert bleiben.
- Nach einem jüngeren schweren Drawdown ist zweifelhaft, ob diese Erwartungen noch unverändert sind.
- Die erwartete Rendite einer Regel ohne Prognosekraft ist nicht grundsätzlich null; sie kann stark von null abweichen, weil die Performance von Faktoren abhängt, die nichts mit der Prognosekraft zu tun haben.
- Die erwartete Rendite hängt von drei Größen ab: dem Zeitanteil long p(L), dem Zeitanteil short p(S) und der durchschnittlichen täglichen Preisänderung ADC des gehandelten Marktes, mit ER = [p(L) × ADC] − [p(S) × ADC].
- Ist die durchschnittliche tägliche Marktänderung null, ist die erwartete Rendite unabhängig von den Positionsanteilen immer null.
- Hat die Regel Prognosekraft, ist ihre erwartete Rendite auf detrendeten Daten größer als null, weil die Long- und Short-Positionen intelligent sind und nicht zufällig.
- Die bei fehlender Vorhersagebeziehung erwartete Zellzahl ist die Besetzung, die sich ergäbe, wenn die Fälle zufällig auf die vier Zellen verteilt wären.
- In der gezeigten Tafel einer bestehenden Beziehung sind die erwarteten Besetzungen 37,8, 16,2, 32,2 und 13,8 in den Zellen A bis D, gegenüber beobachteten 47, 7, 23 und 23.
- Der erwartete Anteil von Kopf ist in jeder Stichprobe 0,50, auch bei nur zwei Würfen.
- Der Anteil, der in einer kleinen Stichprobe tatsächlich erscheint, kann davon stark abweichen: Bei zehn Würfen können leicht drei Kopf, also 0,30, oder sieben Kopf, also 0,70, vorkommen.
- Bei 100.000 Würfen liegt der Kopfanteil extrem nahe bei 0,50, und bei vielen Wiederholungen wäre es unwahrscheinlich, dass er aus dem Bereich 0,497 bis 0,503 fällt.
- Bei 100.000 Würfen wären 0,30 Kopf, also 30.000, oder 0,70 Kopf, also 70.000, mit einer fairen Münze praktisch unmöglich.
- Je größer die Zahl der Würfe, desto genauer spiegelt der Kopfanteil die Wahrscheinlichkeit 0,50 einer fairen Münze, und Schlüsse aus großen Stichproben verdienen mehr Vertrauen als Schlüsse aus kleinen.
- Hat eine TA-Regel keine Vorhersagekraft, ist ihre erwartete Rendite auf trendbereinigten Daten null.
- In jeder kleinen Stichprobe kann die Profitabilität einer Regel ohne Vorhersagekraft erheblich von null abweichen; diese Abweichungen sind gutes oder schlechtes Glück.
- Meist sind die Zufallsabweichungen einer nutzlosen Regel von der Rendite null klein, manchmal erzeugt sie durch bloßes Glück erhebliche Gewinne.
- Die Dichtekurve der Zufallsperformance ist bei null zentriert, weil die Nullhypothese eine erwartete Rendite von null behauptet.
- Die Frage an einen Backtest lautet, ob die beobachtete positive Rendite positiv genug ist, um die Nullhypothese zu verwerfen, die wahre Rendite sei null.
- Fällt die beobachtete Performance gut in den Bereich wahrscheinlich zufälliger Abweichungen, hat die Annahme einer erwarteten Rendite von null der empirischen Herausforderung standgehalten.
- Ist die erwartete Rendite gleich null oder kleiner, sollte ein Backtest Gewinne erzeugen, die vernünftig nahe bei null liegen.
- Lag die gebacktestete Performance deutlich über null, ist die Behauptung, die erwartete Rendite sei null oder kleiner, wahrscheinlich falsch.
- Die ausgewiesene Wahrscheinlichkeit betrifft die Wahrscheinlichkeit des Belegs unter der Annahme, die erwartete Rendite sei null, nicht die Wahrscheinlichkeit, dass diese Annahme wahr ist.
- Die ziemlich hohe Performance der besten von 1.000 Regeln rechtfertigt auf der zum Mehrfachtest passenden Dichte nicht den Schluss, die erwartete Rendite sei größer als null.
- Für jede getestete Regel wird anfangs angenommen, sie habe keine Vorhersagekraft. Die erwartete Rendite wird gleich null gesetzt, und in statistischen Begriffen ist der Populationsparameter damit null.
- Der Populationsparameter einer technischen Regel ist ihre erwartete Leistung über die unmittelbare praktische Zukunft.
- Lässt sich eine positive vergangene Leistung vernünftig der Stichprobenvariabilität zuschreiben, ist der vernünftige Schluss eine erwartete Rendite von null oder weniger über die unmittelbare praktische Zukunft.
- Ist die positive Leistung zu hoch, um vernünftig als Glück zu gelten, lautet der vernünftige Schluss, die Regel habe echte Vorhersagekraft und eine positive erwartete Rendite über die unmittelbare praktische Zukunft.
- Das Gesetz der großen Zahlen sagt, dass die relative Häufigkeit von Kopf mit wachsender Wurfzahls gegen den erwarteten Wert 0,50 konvergiert. Die wahrscheinliche Größe der Abweichungen von 0,50 nimmt dabei ab, auch wenn Abweichungen selbst bei vielen Würfen noch vorkommen.
- Bei kleinen Stichproben kann die relative Häufigkeit stark vom erwarteten Wert abweichen. Bei nur drei Würfen kann leicht dreimal Kopf auftreten, also der Wert 1,0.
- Der Mittelwert einer großen Stichprobe ist eine gute Schätzung des Mittelwerts der Population, aus der sie stammt. Je größer die Stichprobe, desto enger liegt der Stichprobenmittelwert am Populationsmittelwert. Daran hängen einschränkende Bedingungen, die hier nicht weiter zu beachten sind.
- Bei vier Würfen sind Kopfanteile von 0,75 oder 0,25 nicht die wahrscheinlichsten Ergebnisse, aber durchaus häufig. Erreicht die Zahl der Würfe 60, ist die Wahrscheinlichkeit für 0,75 oder 0,25 kleiner als 1 zu 1.000.
- Die Lehre daraus ist, dass eine größere Stichprobe die Rolle des Zufalls verkleinert.
- Null ist die Rendite, die von einer Regel ohne Vorhersagekraft erwartet wird. Die Alternativhypothese behauptet für die geprüften Regeln eine erwartete Rendite größer als null, die Nullhypothese eine erwartete Rendite von null oder weniger.
- Die Stichprobenverteilung wird so gelegt, dass der wahrscheinlichste Wert der Rendite null ist. Das gibt den von der Nullhypothese behaupteten Wert des Populationsparameters wieder.
- Die Alternativhypothese lässt unendlich viele positive Werte zu. Die erwartete Rendite über die unmittelbare praktische Zukunft könnte plus 0,1 Prozent, plus 2 Prozent, plus 6 Prozent oder jeder andere positive Wert sein.
- Die Nullhypothese behauptet, die durchschnittliche Rendite sei null oder ein Wert darunter. Relevant für die Widerlegung ist nur die positivste dieser Behauptungen, die Rendite sei gleich null. Wird sie durch die Backtest-Profitabilität infrage gestellt, sind geringere Behauptungen in noch stärkerem Maß widersprochen.
- Ein Beispiel für eine geringere Behauptung ist eine Rendite von minus 1,3 Prozent. So reduziert sich die Nullhypothese auf die eine Behauptung, die Rendite der Regel sei null.
- Eine Schätzung kann eine Punktschätzung und eine Intervallschätzung liefern. Im Beispiel beträgt die geschätzte Rendite 10 Prozent, und die Wahrscheinlichkeit, dass sie zwischen 5 und 15 Prozent liegt, beträgt 95 Prozent.
- Die Nullhypothese behauptet, die erwartete Rendite der Regel sei null oder kleiner; ist sie falsch, ist die erwartete Rendite größer als null, weil die Regel Vorhersagekraft besitzt.
- Die vom Bootstrap geprüfte Null besagt, der Erwartungswert der Regelrenditen in der Grundgesamtheit sei null oder kleiner.
- Schätzen soll den Wert eines Parameters der Grundgesamtheit annähern; hier ist das die erwartete Rendite einer Regel.
- Eine Punktschätzung ist ein einzelner Näherungswert, zum Beispiel eine erwartete Rendite von 10 Prozent.
- Eine Intervallschätzung ist eine Spanne, in der der Parameter mit einer angegebenen Wahrscheinlichkeit liegt, zum Beispiel von 5 bis 15 Prozent mit Wahrscheinlichkeit 0,95.
- Ein Schätzer ist unverzerrt, wenn sein Erwartungswert gleich dem Wert der Grundgesamtheit ist, die Abweichungen vom wahren Wert also im Mittel null sind.
- Die mittlere Rendite einer Regel in einer historischen Stichprobe ist eine unverzerrte Schätzung ihrer mittleren Rendite in der unmittelbar praktischen Zukunft.
- Ein Schätzer ist konsistent, wenn er mit wachsender Stichprobe gegen den Parameter der Grundgesamtheit konvergiert; das Gesetz der großen Zahlen sagt das für den Stichprobenmittelwert.
- Nach den vier Kriterien unverzerrt, konsistent, effizient und suffizient ist der Stichprobenmittelwert der beste Schätzer des Mittelwerts der Grundgesamtheit.
- Ein Schätzer ist suffizient, wenn er die Stichprobendaten so ausschöpft, dass kein anderer Schätzer weitere Information über den Parameter liefert; der Stichprobenmittelwert ist suffizient.
- Der bekannte Stichprobenmittelwert ist der unbekannte Mittelwert der Grundgesamtheit plus oder minus den Stichprobenfehler; umgekehrt ist der Mittelwert der Grundgesamtheit der Stichprobenmittelwert plus oder minus den Stichprobenfehler.
- Erwartete Leistung ist die erwartete Rendite einer Regel in der unmittelbar praktischen Zukunft und heißt auch wahre Leistung, soweit sie auf legitimer Vorhersagekraft beruht.
- Der Data-Mining-Bias ist die erwartete Differenz zwischen der beobachteten Leistung der besten Regel und ihrer erwarteten Leistung, als langfristiger Mittelwert über viele Experimente.
- Die beobachtete Leistung zerfällt in Zufall und die der Vorhersagekraft zuzurechnende erwartete Leistung; der Zufallsanteil wiederholt sich in der unmittelbar praktischen Zukunft nicht.
- Die Leistung der besten Regel außer Stichprobe fällt wahrscheinlich auf ein Niveau zurück, das ihre innewohnende Vorhersagekraft abbildet.
- Bei schiefer Stichprobenverteilung kann ein 90-Prozent-Konfidenzintervall eine Wahrscheinlichkeit von mehr als 0,05 anzeigen, dass die erwartete Rendite unter null liegt, während ein Test zum Niveau 0,05 die Null zugunsten einer erwarteten Rendite über null verwirft.
- Erwartete Leistung ist der Teil der beobachteten Leistung, der auf echter Vorhersagekraft beruht: ein wiederkehrendes Marktmerkmal, das die Regel ausnutzt und das sich in der unmittelbar praktischen Zukunft fortsetzen sollte.
- Der andere Teil ist Zufall, als Glück oder Pech; Glück hebt die beobachtete Leistung über die erwartete, Pech drückt sie darunter, und dieser Teil ist in der unmittelbar praktischen Zukunft nicht zu erwarten.
- Beobachtete Leistung ist gleich erwartete Leistung plus oder minus Zufall.
- Beim Backtest einer einzelnen Regel ist die mittlere Rendite eine unverzerrte Schätzung der erwarteten künftigen Rendite.
- Die Backtest-Leistung der besten Regel ist eine positiv verzerrte Schätzung ihrer erwarteten Leistung, weil ein erheblicher Glücksanteil darin steckt.
- In der Abbildung hat jede der 50 Regeln die erwartete Rendite null; der höchste beobachtete Mittelwert von 37 Prozent bildet diese erwartete Rendite nicht ab.
- Die traditionelle Null behauptet eine erwartete Rendite von null oder weniger; die bei Verwerfung angenommene Alternative eine erwartete Rendite größer als null.
- Die richtige Stichprobenverteilung des Maximums von 50 Mittelwerten ist bei plus 33 Prozent zentriert und nicht bei null.
- Wäre die erwartete Rendite jeder Regel null, betrüge die Wahrscheinlichkeit 0,45, dass die mittlere Rendite der besten Regel durch Glück mindestens 37 Prozent erreicht.
- Geht die Zahl der Beobachtungen gegen unendlich, geht die Wahrscheinlichkeit gegen 1, dass die Regel mit der höchsten erwarteten Rendite die beste beobachtete Leistung zeigt.
- Bei genügend vielen Beobachtungen gehört die höchste beobachtete Leistung einer Regel mit höherer erwarteter Rendite als der einer zufällig aus der geprüften Menge gezogenen Regel.
- Bei zwölf Regeln mit erwarteter Rendite null setzt eine beobachtete Rendite von plus 60 Prozent den Bias auf plus 60 Prozent.
- Die überlegene Regel ist die mit der höchsten erwarteten Rendite; sie muss nicht gewählt werden, wenn eine schwächere Regel durch Glück gewinnt.
- Je größer der Unterschied der erwarteten Renditen zwischen der wirklich besten und der nächstbesten Regel, desto eher setzt sich das Verdienst gegen den Zufall durch.
- Der Data Miner beobachtet die wahre erwartete Rendite nie, weil sie ein Parameter der Grundgesamtheit ist.
- Je geringer die Variation der wahren erwarteten Renditen unter den geprüften Regeln, desto größer ist der Data-Mining-Bias.
- Ein unverzerrter Schätzer trägt nur Zufallsfehler, ein verzerrter Zufallsfehler und systematischen Fehler; der unverzerrte Fehler hat den Erwartungswert null.
- Mit der mittleren absoluten Monatsrendite des S&P 500 von 3,97 Prozent über fast 900 Monate von August 1928 bis April 2003 lautet die Formel ER gleich ppm mal 3,97 minus (1 minus ppm) mal 3,97.
- Bei Gewinnwahrscheinlichkeit 1,0 beträgt der Erwartungswert +3,97 Prozent pro Monat, bei 0,63 beträgt er +12,4 Prozent, bei 0,50 ist er null, und bei null beträgt er −3,97 Prozent pro Monat.
- Diese Erwartungswerte werden über eine sehr große Zahl von Monaten verdient; über wenige Monate kann die beobachtete mittlere Rendite davon abweichen, und je weniger Monate, desto größer die zufällige Abweichung.
- Die gesetzte Wahrscheinlichkeit eines profitablen Monats manifestiert sich über eine sehr große Zahl von Monaten, eine Erscheinung des Gesetzes der großen Zahlen.
- Die erwartete Rendite einer künstlichen Regel wird vollständig durch ihre festgelegte Wahrscheinlichkeit eines profitablen Monats bestimmt.
- Bei erwarteter Rendite null für alle Regeln ist der Data-Mining-Bias gleich der über die Wiederholungen gemittelten beobachteten Rendite der besten Regel.
- Die erwartete Rendite einer künstlichen Regel wird vollständig durch ihre Wahrscheinlichkeit eines profitablen Monats bestimmt, und Abbildung 6.41 zeigt diesen Zusammenhang spezifisch für die monatlichen S&P-Renditen der Simulationen.
- Die Wahrscheinlichkeit eines profitablen Monats wurde jeder Regel zufällig aus einer Verteilung gezogen, deren Form der Vermögensverteilung ähnelt: ein langer rechter Rand, extrem Reiche wie Bill Gates sehr selten und viele arm.
- Eine Regel mit erwarteter Jahresrendite von 19 Prozent oder mehr trat etwa einmal unter 10.000 auf, und die erwartete Rendite der durchschnittlichen Regel im Universum betrug +1,4 Prozent pro Jahr.
- Die konkreten Annahmen dieser Verteilung sind vielleicht nicht genau, aber vermutlich auf eine Größenordnung richtig, gestützt auf die Performance der besten Hedgefonds, die technische Analyse nutzen; für die Experimente sind die Details nicht entscheidend.
- Bei genügend Beobachtungen ist die beobachtete Rendite ein nützlicher, aber positiv verzerrter Indikator der erwarteten Rendite; bei zu wenigen Beobachtungen ist sie praktisch nutzlos.
- Die beste von 256 Regeln mit 1.000 Monaten hat eine erwartete Rendite von +10 Prozent im Jahr gegenüber +1,4 Prozent im Universumsdurchschnitt; bei nur zwei Monaten bleibt die erwartete Rendite der besten Regel auf diesem Durchschnitt von +1,4 Prozent stehen.
- Bei Korrelation 0,9 und 100 Monaten ist die erwartete Rendite der besten von 256 nur +1,4 Prozent, bei Korrelation null fast 4 Prozent.
- Der Markowitz-Xu-Faktor schätzt die erwartete Rendite der besten Regel als H′ gleich R plus B mal (H minus R), und dieser Wert liegt zwischen der beobachteten Performance der besten Regel und dem Durchschnitt aller getesteten Regeln.
- Nach der Erwartungsnutzentheorie von Neumann und Morgenstern wählt ein vollkommen rationaler Entscheider die Option mit dem höchsten Erwartungswert; der ist die Summe der Produkte aus der Wahrscheinlichkeit jedes Ergebnisses und dem Nutzen dieses Ergebnisses.
- Menschen verhalten sich nicht so; die Forschung zeigt zahlreiche systematische Fehler bei der Risikobewertung und bei Entscheidungen.
- Die EMH schließt Handelssysteme auf verfügbarer Information aus, deren erwartete Gewinne oder Renditen die gleichgewichtige erwartete Rendite übersteigen.
- Unter der EMH sind positive Renditen einer Strategie weiter möglich, nach Risikoadjustierung aber nicht besser als Kaufen und Halten des Marktindex.
- Bei White's Reality Check hat eine nutzlose Regel die erwartete Rendite null; der Mittelwert der Monte-Carlo-Stichprobenverteilung ist die erwartete Rendite einer nutzlosen Regel in einem Data-Mining-Vorhaben und darf nach der Zufallszuordnung über null liegen.
- Anleger, die auf irrelevante Signale reagieren, können dieselbe Rendite erwarten wie jemand, der nach einem Münzwurf kauft und verkauft.
- Im Arbitragebeispiel haben zwei gleich teure und gleich riskante Aktien unterschiedliche erwartete künftige Renditen, sodass eine von beiden falsch bepreist ist.
- Der Populationsparameter der Fallstudie ist die erwartete durchschnittliche annualisierte Rendite der Regel in der unmittelbaren praktischen Zukunft.
- Data Mining verzerrt die Performance der ausgewählten Regel nach oben: Die im Backtest beobachtete Performance überschätzt die künftig erwartete Performance.
- Die Nullhypothese von Whites Reality Check lautet, alle getesteten Regeln hätten erwartete Renditen gleich null oder kleiner.
- Die Alternativhypothese von Whites Reality Check lautet, mindestens eine Regel im getesteten Universum habe eine erwartete Rendite größer als null.
- White behauptet nicht, die Regel mit der höchsten beobachteten Performance sei notwendig die beste Regel, also die mit der höchsten erwarteten Rendite. Unter recht vernünftigen Bedingungen sind sie aber ein und dieselbe.
- Bei großen Stichproben, hier über 6000 Tage, kann die Nullhypothese verworfen werden, auch wenn die Rendite einer Regel nur um einen sehr geringen Betrag positiv ist. Statistische Signifikanz und praktischer Wert fallen dann auseinander.
- Praktische Bedeutung hängt von den Zielen ab. Ein Händler kann mit einer Regel zufrieden sein, deren erwartete Rendite 5 Prozent beträgt, ein anderer kann jede Regel ablehnen, deren erwartete Rendite unter 20 Prozent liegt.
- Die erwartete Rendite der besten von 6.402 konkurrierenden Regeln ohne Vorhersagekraft beträgt unter den Bedingungen der Fallstudie etwa 11 Prozent und nicht 0 Prozent.
- Beide Stichprobenverteilungen, Reality Check und Monte-Carlo-Permutation, zentrieren bei etwa 11 Prozent mittlerer Rendite.
- Dieser Erwartungswert ist die Folge des konkreten Satzes von 6.402 Regeln, der Korrelationen ihrer Renditen, der Zahl der Beobachtungen, aus denen die Mittelwerte berechnet wurden, und des verwendeten S&P-Datensatzes.
- Die Stichprobenverteilung der mittleren Rendite der besten von N Regeln ist nicht bei null zentriert, sondern bei einem positiveren Wert; sie ist die Verteilung einer Statistik, die als Maximum der Mittel von N Mitteln definiert ist.
- Würde die Fallstudie auf 1.000 unabhängigen Datensätzen wiederholt, enthielten in 800 dieser Tests die 6.402 gemeinsamen 80-Prozent-Konfidenzintervalle die erwarteten Renditen aller Regeln.
- Die im Testsatz erreichte Leistung der Regel mit optimaler Komplexität ist positiv verzerrt, weil der Testsatz wiederholt besucht wurde, um diese Komplexität zu finden; das ist der Data-Mining-Bias.
- Weil der Validierungssatz weder bei der Suche nach den Parameterwerten noch bei der Suche nach dem Komplexitätsgrad benutzt wurde, ist die Leistung der besten Regel dort eine unverzerrte Schätzung ihrer künftig erwarteten Leistung.
- Im Beispiel verdient die beste Regel aus zwei gleitenden Durchschnitten 30 Prozent annualisiert im Training und 15 Prozent im Test; die 15 Prozent sind eine unverzerrte Schätzung der künftigen Leistung, solange der Testsatz nur einmal benutzt wird.
- Die anschließend geprüfte Vier-Parameter-Regel verdient im unterstellten Beispiel 50 Prozent im Training und 20 Prozent im Test, gegenüber 30 und 15 Prozent der einfacheren Regel.
- Nach Whites Proposition 2.1 geht mit gegen unendlich wachsendem Stichprobenumfang die Wahrscheinlichkeit gegen 1,0, dass die Regel mit der höchsten erwarteten Rendite auch die höchste beobachtete Performance hat.
- Der getrimmte Mittelwert wird berechnet, nachdem die größten 5 Prozent der Gewinne und der Verluste entfernt wurden, und kann den Populationsmittelwert genauer schätzen, weil Ausreißer die Ergebnisse verzerren können.
- Die Bedingung dafür, dass der Mittelwert einer Stichprobe sich dem Mittelwert der Elternpopulation annähert, ist, dass der Mittelwert in der Elternpopulation endlich ist.
- Das Gesetz der großen Zahlen bezeichnet die Konvergenz zwischen einem Stichprobenmittel und einem Populationsmittel.
- Eine relative Häufigkeit ist dasselbe wie ein Mittelwert, wenn das Eintreten eines Ereignisses den Wert 1 und das Nichteintreten den Wert 0 erhält.

## Funktionsweise

- Die erwartete Lösung des Ornstein-Uhlenbeck-Prozesses ist E(y(t)) gleich y0 mal exp(λt) minus (μ/λ) mal (1 minus exp(λt)).
- Ist λ für einen mean-reverting Prozess negativ, fällt der erwartete Preis exponentiell auf den Wert minus μ/λ.
- Die Halbwertszeit dieses Abfalls ist minus log(2) geteilt durch λ.
- Werden immer zwei Kontrakte gehalten und erst bei F vollständig geschlossen, ist der erwartete Gewinn von all-in bei L1 gleich 2 mal (F minus L1).
- Der erwartete Gewinn von all-in bei L2 ist 2 mal p mal (F minus L2), weil nur mit Wahrscheinlichkeit p investiert wird.
- Der erwartete Gewinn von average-in ist (F minus L1) plus p mal (F minus L2).
- Die Schwelle ist p-Dach gleich (F minus L1) geteilt durch (F minus L2): darunter ist all-in bei L1 besser als all-in bei L2 und besser als average-in, darüber ist all-in bei L2 besser als die beiden anderen.
- Bei p gleich 0 ist all-in bei L1 am profitabelsten, bei p gleich 1 ist all-in bei L2 am profitabelsten, und average-in ist in keinem Fall das profitabelste Verfahren, solange p konstant ist.
- Market Maker aktualisieren mit diesem Modell ihre Schätzung des mittleren Preises eines Assets.
- Ist die Trade-Größe T gleich der Benchmark Tmax, ist der Kalman-Gain 1, und die neue Schätzung des mittleren Preises m(t) ist genau der beobachtete Preis.
- Gemittelt wird über eine Zufallsstichprobe der ungehebelten Rendite pro Bar R(t) der Strategie, nicht der Marktpreise, aus einer Wahrscheinlichkeitsverteilung von R.
- Üblich sind Tagesbars; der Bar kann aber beliebig lang oder kurz sein.
- Ist R gaußisch, lässt sich g(f) analytisch reduzieren, und die Ableitung nach f gleich null reproduziert die Kelly-Formel sowie im Ein-Strategie-Fall die maximale Wachstumsrate.
- Ohne Gauß-Annahme wird dieser Erwartungswert mit einer nichtgaußischen Verteilung per Monte Carlo berechnet.
- Die wahre Verteilung von R ist unbekannt; das Pearson-System modelliert sie aus Mittelwert, Standardabweichung, Schiefe und Kurtosis.
- Im Beispiel dienen 100.000 Zufallsrenditen aus diesem System dazu, den Durchschnitt von g(f) zu berechnen.
- Die erwartete Rendite eines Handelssystems mit zufälligen Positionen ist die erwartete Summe der Rohrenditen in den Long-Phasen minus die erwartete Summe der Rohrenditen in den Short-Phasen.
- Die Gesamtrendite des Kandidatensystems ist die Summe der Rohrenditen zu den Zeiten, in denen es long ist, minus die Summe der Rohrenditen, in denen es short ist.
- Die um das Long-Short-Vorurteil korrigierte Rendite entsteht, indem die Erwartung eines ebenso voreingenommenen Zufallssystems von der Gesamtrendite des Kandidatensystems abgezogen wird.
- Nach dem Verteilen der Subtraktion über die Summen unterscheidet sich die korrigierte Rendite von der unkorrigierten nur dadurch, dass der Mittelwert der Rohrenditen von jeder einzelnen Rohrendite abgezogen wird.
- Das Abziehen der durchschnittlichen Tagesrendite von jeder einzelnen Tagesrendite kann auch vor dem Bootstrapping erfolgen. In der Darstellung des Textes wurde es danach vorgenommen.

## Voraussetzungen


## Anwendung im Trading

- Der erwartete Preis eines Instruments lässt sich anhand des letzten Trades, also Preis und Größe, mit dem Kalman-Filter dynamisch aktualisieren.

## Regeln und Kriterien

- Ist λ positiv, ist die Reihe überhaupt nicht mean-reverting, und eine Mean-Reversion-Strategie soll nicht angesetzt werden.
- Liegt λ sehr nahe bei null, wird die Halbwertszeit sehr lang, und die Strategie ist wenig profitabel, weil in der gegebenen Zeit wenige Round-Trips abgeschlossen werden.

## Risiken und Grenzen

- Die Rangfolge der erwarteten Gewinne gilt nur, wenn p über die Zeit konstant ist; ist die Volatilität nicht konstant, ist auch p nicht konstant, und Scaling-in kann außer Stichprobe besser abschneiden.

## Beispiele

- Auf den S&P-500-Daten vom 1. Januar 1976 bis Dezember 2004 ist die erwartete Rendite bei 90 Prozent long und 10 Prozent short 0,028 Prozent pro Tag oder 7,31 Prozent annualisiert.
- Bei 60 Prozent long und 40 Prozent short beträgt sie 0,007 Prozent pro Tag oder 1,78 Prozent annualisiert.
- Bei 60 Prozent long, 40 Prozent short und einer durchschnittlichen Tagesrendite von null gilt 0 = [0,60 × 0] − [0,40 × 0].
- Ein Roulette mit 75 von 100 Feldern auf +1 und 25 auf −1 erzeugt bei positiver durchschnittlicher Tagesänderung eine positive erwartete Rendite, obwohl die Signale keine Prognoseinformation enthalten.
- Beim Münzwurf kann der Anteil Kopf bei wenigen Würfen erheblich von 0,50 abweichen, und 0,50 ist der erwartete Anteil Kopf bei einer sehr großen Zahl von Würfen.
- Im Münzexperiment mit bis zu tausend Würfen gab es unter zehn Würfen zwei große Abweichungen vom erwarteten Wert 0,50: bei 3 Würfen einen Kopfanteil von 0,66, also 2 von 3, und bei 8 Würfen einen Anteil von 0,375, also 3 von 8.
- Ist die beobachtete mittlere Rendite einer Regel 15 Prozent, könnte das 95-Prozent-Konfidenzintervall anzeigen, dass die wahre Rendite zwischen 5 und 25 Prozent liegt.
- Ein 90-Prozent-Konfidenzintervall schließt den wahren Mittelwert mit Wahrscheinlichkeit 0,90 ein; wird das Bilden von Mittelwert und Intervall 1.000 Mal wiederholt, liegt der Mittelwert der Grundgesamtheit in ungefähr 900 der 1.000 Intervalle.
- Im Beispiel einer Backtest-Rendite von 7 Prozent liegt die erwartete Rendite mit Wahrscheinlichkeit 0,90 zwischen 2 und 12 Prozent.
- Bei hundert unabhängigen Backtests und je einem 90-Prozent-Intervall um die mittlere Rendite enthalten ungefähr 90 Intervalle die wahre oder erwartete Rendite der Regel.
- Für TT-4-91 läge die wahre erwartete Rendite in ungefähr 80 von 100 unabhängigen Stichproben innerhalb eines 80-Prozent-Intervalls; die Grenzen um die beobachteten plus 4,84 Prozent sind plus 0,62 und plus 9,06 Prozent.
- In dem angeführten Spiel beträgt der Erwartungswert je gesetztem Dollar plus 50 Cent.
- In der Sprache der Anlagestrategie entspräche dieser Vorteil einem Profit Factor von 2,0. Sehr wenige Anlagestrategien haben einen so günstigen Vorteil.
- Ein Geldverwalter ohne jedes Können hat in einer gegebenen Periode, zum Beispiel einem Jahr, eine Wahrscheinlichkeit von 0,5, den Markt zu schlagen. Taleb nahm ein Universum von Verwaltern mit dieser Wahrscheinlichkeit 0,50 an.

## Unterschiedliche Quellenpositionen

- Die Optimierung dieses Erwartungswerts über eine analytische Verteilung wird der Optimierung der einen historischen Wachstumsrate gegenübergestellt.
- Für Manager eigenen Geldes ist das alleinige Ziel die Maximierung des langfristigen Nettovermögens; Drawdowns und Volatilitäten sind ihnen gleichgültig.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 20–39 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-002-p020-p039|S. 20–39]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 77–96 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-005-p077-p096|S. 77–96]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 96–115 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-006-p096-p115|S. 96–115]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 115–134 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-007-p115-p134|S. 115–134]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 134–153 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-008-p134-p153|S. 134–153]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 153–172 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-009-p153-p172|S. 153–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 172–191 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-010-p172-p191|S. 172–191]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 191–210 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-011-p191-p210|S. 191–210]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 210–229 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-012-p210-p229|S. 210–229]]
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
