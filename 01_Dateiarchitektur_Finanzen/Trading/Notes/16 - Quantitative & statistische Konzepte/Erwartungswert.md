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

# Erwartungswert


## Kurzdefinition

- Der erwartete Wert der zusammengesetzten Wachstumsrate als Funktion des Hebels f ist bei risikofreiem Zins null der Durchschnitt von log(1 plus f mal R).
- Die erwartete Rendite einer künstlichen Handelsregel ist der Erwartungswert einer Zufallsvariablen: Wahrscheinlichkeit eines profitablen Monats mal durchschnittlicher Gewinn minus Wahrscheinlichkeit eines Verlustmonats mal durchschnittlicher Verlust.
- Der Erwartungswert einer einzelnen Rohrendite, gezogen aus der Grundgesamtheit der historischen Rohrenditen, ist definitionsgemäß der Mittelwert dieser Renditen.
- Der Erwartungswert eines Spiels ist Gewinnwahrscheinlichkeit mal Gewinnbetrag minus Verlustwahrscheinlichkeit mal Verlustbetrag.
- Das ℓ-te Moment einer stetigen Zufallsvariablen ist m′ℓ = E(Xℓ) = Integral von −∞ bis ∞ von xℓ f(x) dx; E bezeichnet den Erwartungswert und f die Dichte.
- Das erste Moment heißt Mittelwert oder Erwartungswert, wird mit µx bezeichnet und misst die mittlere Lage der Verteilung.
- Das ℓ-te zentrale Moment ist mℓ = E[(X − µx)ℓ] = Integral (x − µx)ℓ f(x) dx, sofern das Integral existiert.

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
- Ein Backtest berechnet typischerweise eine erwartete Rendite und weitere statistische Leistungsmaße, deren statistische Signifikanz zu prüfen ist.
- Die Nullhypothese setzt die wahre durchschnittliche Tagesrendite auf einem unendlichen Datensatz auf null.
- Ist der Anteil der simulierten Preisreihen mit mindestens der Backtest-Rendite nicht klein, kann die Durchschnittsrendite der Strategie bloß von den Marktrenditen stammen.
- Die erwartete Lösung der Ornstein-Uhlenbeck-Gleichung ist E(y(t)) = y0 exp(λt) minus (μ/λ) mal (1 minus exp(λt)).
- Bei negativem λ fällt der erwartete Preis exponentiell auf den Wert minus μ/λ, und die Halbwertszeit dieses Abfalls ist minus log(2)/λ.
- Das Ziel des Traders ist, ob die erwartete Rendite oder die Sharpe Ratio einer Mean-Reversion-Strategie gut genug ist.
- g(f) mittelt log(1 plus f mal R) über eine Zufallsstichprobe der ungehebelten Rendite je Bar der Strategie, nicht der Marktpreise. Üblich sind Tagesbars, die Bar kann aber beliebig lang oder kurz sein.
- Das Pearson-System nimmt Mittelwert, Standardabweichung, Schiefe und Kurtosis und modelliert R als eine von sieben analytischen Verteilungen, darunter Gauß, Beta, Gamma und Student-t.
- Die empirische Verteilung kann höhere Momente haben, die das System nicht erfasst, oder unendliche höhere Momente wie bei der Pareto-Levy-Verteilung.
- Im Beispiel sind 100.000 Zufallsrenditen gezogen; pearsrnd liefert den Typ 4, also keine Standardverteilung wie die Student-t.
- Ist R gaußisch, ist g(f) gleich f mal m minus f zum Quadrat mal m zum Quadrat geteilt durch 2.
- Liegt die Hebelobergrenze weit unter dem Kelly-Hebel und sind die unabhängigen Wachstumsraten sehr verschieden, ist es oft wachstumsmaximal, die ganze Kaufkraft in die Strategie mit der höchsten mittleren Überschussrendite zu legen, statt alle Hebel proportional zu skalieren.
- Im Zahlenbeispiel fällt der Erwartungswert der annualisierten Wachstumsrate bei proportionaler Kürzung auf den Bruttohebel 2 von 2,1 auf 0,82 und steigt auf 0,96, wenn nur die zweite Strategie mit Hebel 2 gehalten wird.
- Die Erfahrung des Autors ist, dass Kelly auf jede Strategie einzeln praktischer ist als die Allokation über alle Strategien, sodass eine underperformende Strategie schnell eingeht, auch wenn die Mathematik die Gesamtallokation bei unveränderten erwarteten Renditen und Volatilitäten als optimal ausweist.
- Wie sich der bedingte Erwartungswert und die bedingte Kovarianzmatrix von rt über die Zeit entwickeln, ist der Hauptgegenstand der Kapitel 8 und 10.
- Der Mittelwert einer täglichen Renditereihe liegt nahe bei null, der einer monatlichen Renditereihe etwas höher.
- Bei den betrachteten Zinsreihen sind die Stichprobenmittel proportional zur Laufzeit. Bei den Anleiherenditen bleiben die Stichprobenmittel über alle Laufzeiten stabil.
- Für die prozentualen IBM-Logrenditen, n = 9845, lehnt der t-Test die Hypothese eines Erwartungswerts von null auf dem 5-Prozent- und auf dem 10-Prozent-Niveau nicht ab.
- Für die lineare Reihe rt gleich µ plus Summe von i gleich 0 bis unendlich von ψi mal a(t−i), mit ψ0 gleich 1 und weißem Rauschen at, gilt E(rt) gleich µ.
- Beim AR(1) ist der bedingte Erwartungswert E(rt gegeben rt−1) gleich phi0 plus phi1 mal rt−1, und gegeben rt−1 liegt rt um diesen Wert.
- Unter schwacher Stationarität ist der Mittelwert eines AR(1) gleich phi0 geteilt durch (1 minus phi1), sofern phi1 ungleich 1 ist; er ist genau dann null, wenn phi0 gleich 0 ist, und es gilt phi0 gleich (1 minus phi1) mal µ.
- Der Mittelwert eines stationären AR(2) ist phi0 geteilt durch (1 minus phi1 minus phi2), sofern phi1 plus phi2 ungleich 1 ist.
- Der Mittelwert eines stationären AR(p) ist phi0 geteilt durch 1 minus die Summe der phi-Koeffizienten, sofern der Nenner nicht null ist.
- Die Ein-Schritt-Punktprognose eines AR(p) unter quadratischem Fehlerverlust ist der bedingte Erwartungswert der nächsten Rendite gegeben der Information am Prognoseursprung und lautet phi0 plus die Summe phi-i mal der jeweils noch beobachteten verzögerten Rendite.
- Die l-Schritt-Prognose ist der bedingte Erwartungswert von r(h plus l) gegeben der Information bei h und wird rekursiv aus den kürzeren Prognosen berechnet; nichtpositive Horizonte werden durch die beobachtete Rendite ersetzt.
- Bei einem stationären AR(p) konvergiert die Mehrschritt-Punktprognose mit wachsendem Horizont gegen E(rt), die langfristige Punktprognose also gegen den unbedingten Mittelwert.
- Der Mittelwert eines MA-Modells ist die Konstante c0.
- Beim MA(1) ist jede Prognose ab dem zweiten Schritt, unabhängig vom Ursprung, gleich dem unbedingten Mittel c0; beim MA(q) erreichen die Mehrschrittprognosen den Mittelwert nach den ersten q Schritten.
- Der Mittelwert eines schwach stationären ARMA(1,1) ist phi0 geteilt durch (1 minus phi1), identisch zum AR(1).
- Der unbedingte Mittelwert eines schwach stationären ARMA(p, q) ist phi0 geteilt durch (1 minus die Summe der AR-Koeffizienten).
- Beim Random Walk ist die Punktprognose für jeden Horizont l größer als 0 der bedingte Erwartungswert gleich dem Wert der Reihe am Prognoseursprung; diese Prognose hat keinen praktischen Wert.
- Beim Random Walk mit Drift und festem Startwert p0 ist E(pt) gleich p0 plus µ mal t.
- Dieser bedingte Erwartungswert wächst schneller als die bedingte Standardabweichung Wurzel aus t mal σa.
- Beim trendstationären Modell pt gleich β0 plus β1 mal t plus einer stationären Reihe ist E(pt) gleich β0 plus β1 mal t und damit zeitabhängig, während die Varianz endlich und zeitlich invariant bleibt.
- Der Drift µ eines Random Walk mit Drift ist der Erwartungswert von pt minus pt−1.
- In der Moving-Average-Darstellung eines stationären ARMA ist der Mittelwert µ gleich phi0 geteilt durch (1 minus die Summe der AR-Koeffizienten), und die langfristige Prognose läuft gegen diesen Mittelwert.
- Die Konstante eines MA(q) ist der Mittelwert der Reihe; bei einem stationären AR(p) oder ARMA(p, q) hängt sie mit dem Mittel über µ gleich phi0 geteilt durch (1 minus Summe der phi) zusammen; beim Random Walk mit Drift wird die Konstante zur Zeitsteigung der Reihe.
- Der bedingte Mittelwert ist mü t gleich dem Erwartungswert von rt gegeben Ft minus 1, und die bedingte Varianz ist der Erwartungswert des quadrierten Abstands von diesem Mittelwert.
- Ft minus 1 besteht typischerweise aus allen linearen Funktionen der vergangenen Renditen.
- Im ARCH(1)-Modell bleibt der unbedingte Erwartungswert des Schocks null, weil der bedingte Erwartungswert sigma t mal Erwartungswert von epsilon t ist und epsilon t den Mittelwert null hat.
- Der gaußsche ARCH(1) für die monatlichen Intel-Logrenditen setzt die erwartete Monats-Logrendite auf etwa 1,26 Prozent, die Konstante ist 0,0126; die Spanne enthält die Zeit nach der Internetblase.
- Unter Student-t-Innovationen beträgt dieselbe Konstante 0,0169, mit Standardfehler 0,0053.
- Der unbedingte Erwartungswert von a t quadrat im GARCH-Modell ist alpha 0 geteilt durch 1 minus der Summe (alpha i plus beta i), sofern der Nenner positiv ist.
- Eta t gleich a t quadrat minus sigma t quadrat ist eine Martingaldifferenz: der Erwartungswert ist null und die Kovarianz mit eigenen Lags ab 1 ist null, die Folge ist aber im Allgemeinen nicht unabhängig und identisch verteilt.
- Die Mehrschrittprognose der GARCH(1,1)-Varianz konvergiert mit wachsendem Horizont gegen die unbedingte Varianz alpha 0 durch (1 minus alpha 1 minus beta 1), sofern alpha 1 plus beta 1 kleiner als 1 ist.
- Der bedingte Erwartungswert von a, h plus 1, quadrat ist die bedingte Varianz, das Quadrat ist also ein konsistenter, aber kein genauer Schätzer dieser Varianz, weil eine einzelne Beobachtung die Varianz nicht genau trifft.
- Beim EGARCH ist der unbedingte Erwartungswert von ln der bedingten Varianz gleich alpha 0, und der Erwartungswert der gewichteten Innovation g von epsilon t ist null.
- Für eine standardnormale Innovation ist der Erwartungswert des Absolutbetrags die Wurzel aus 2 durch pi.
- Im GARCH(1,1)-M hängt die Rendite linear von ihrer bedingten Varianz ab; ein positives c bedeutet, dass die Rendite positiv mit ihrer Volatilität zusammenhängt. Weitere Formen sind c mal sigma t und c mal ln der bedingten Varianz.
- Für die monatlichen S&P-500-Überschussrenditen von Januar 1926 bis Dezember 1991 ist das geschätzte c gleich 1,09 mit Standardfehler 0,818, positiv, aber auf dem 5-Prozent-Niveau nicht signifikant.
- Tabelle 3.1 prognostiziert am Ursprung Dezember 1991, h gleich 792, die mittlere Überschussrendite für die Horizonte 1 bis 5 und unendlich einheitlich mit 0,0076.
- Im GARCH(1,1) mit α₀ > 0, α₁ ≥ 0, β₁ ≥ 0 und α₁ + β₁ < 1 gilt Var(a_t) = E(σ²_t) = α₀ / [1 − (α₁ + β₁)].
- E(a⁴_t) = (K_ε + 3) E(σ⁴_t), sofern E(σ⁴_t) existiert. K_ε ist die Exzess-Kurtosis der Innovation, und E(ε⁴_t) = K_ε + 3 bei E(ε_t) = 0 und Var(ε_t) = 1.
- E(σ⁴_t) = α₀² (1 + α₁ + β₁) / {[1 − (α₁ + β₁)] [1 − α₁²(K_ε + 2) − (α₁ + β₁)²]}, sofern 1 > α₁ + β₁ ≥ 0 und der zweite Faktor im Nenner positiv ist.
- Im simulierten Zwei-Regime-TAR(1) gibt es keine Konstanten, aber E(x_t) ist nicht null. Der Stichprobenmittelwert einer Realisation mit 200 Beobachtungen ist 0,61 bei einer Standardabweichung von 0,07.
- Allgemein ist E(x_t) eines TAR ein gewichtetes Mittel der bedingten Mittelwerte der Regime. Das Gewicht eines Regimes ist seine Wahrscheinlichkeit unter der stationären Verteilung. Die bedingten Mittel der beiden Regime sind von null verschieden.
- Damit ein TAR den Mittelwert null hat, braucht es in einigen Regimes von null verschiedene Konstanten. Bei einem stationären linearen Modell bedeutet eine von null verschiedene Konstante, dass der Mittelwert von x_t nicht null ist.
- Im speziellen bilinearen Modell x_t = μ + Σ β_i a_{t−i} a_t + a_t mit weißem Rauschen ist der bedingte Erwartungswert E(x_t | F_{t−1}) = μ.
- In einem Markov-Switching-Modell ist 1/w_i die erwartete Verweildauer in Zustand i. Ein kleines w_i bedeutet, dass das Modell länger in diesem Zustand bleibt.
- Für die Wachstumsrate des realen US-GNP betragen die erwarteten Dauern näherungsweise 3,69 Quartale in der Kontraktion und 11,31 Quartale in der Expansion.
- Der mittlere Wachstumsbeitrag des Randmodells ist 0,965 im Expansionszustand und −1,288 im Kontraktionszustand.
- Der bedingte Mittelwert eines STAR-Modells ist eine stetig gewichtete Linearkombination zweier linearer AR-Gleichungen. Die Gewichte bestimmt F[(x_{t−d} − c)/s] mit 0 ≤ F ≤ 1.
- Für den wöchentlichen 3-Monats-Treasury-Bill-Satz ist μ(x_{t−1}) der bedingte Erwartungswert von y_t = x_t − x_{t−1} gegeben x_{t−1}. Die lokale Glättung ist im Wesentlichen null, auf feiner Skala positiv bei kleinem Zins und negativ bei großem Zins.
- Beim nichtparametrischen Glätten konvergiert der Mittelwert unabhängiger Wiederholungen an einer Stelle x nach dem Gesetz der großen Zahlen gegen m(x), weil der Mittelwert der Schocks gegen null geht.
- Prognosen eines Markov-Switching-Modells sind stets eine Linearkombination der Prognosen der einzelnen Zustände.
- Die Punktprognose des parametrischen Bootstrap für x_{T+ℓ} ist der Stichprobenmittelwert der M gezogenen Realisationen.
- Im Markov-Switching-Modell der Änderung der US-Arbeitslosenquote sind die bedingten Mittel von Δx_t gleich −0,10 im Expansionszustand s_t = 1 und 0,31 im Kontraktionszustand s_t = 2.
- Der Ein-Schritt-Benchmark für die IBM-Monatsprognosen 1998 und 1999 ist das Stichprobenmittel der ersten Teilstichprobe; die durchschnittliche monatliche Logrendite von Januar 1926 bis Dezember 1997 beträgt 1,19.
- Im Bispektrum ist g = E(a³_t); für eine lineare gaußsche Reihe ist g = 0, und das Bispektrum ist dann für alle Frequenzen null.
- Beim direktionalen Zufallsvergleich wird eine Aufwärtsbewegung prognostiziert, wenn 1,19 + ε_t ≥ 0 ist, mit ε_t unabhängig und identisch N(0, 1).
- Im Modell nichtsynchronen Handels bleibt der Erwartungswert der beobachteten Rendite gleich dem Erwartungswert der wahren Rendite: E(r^o_t) = μ, obwohl Varianz und Autokovarianzen sich ändern.
- Im Roll-Modell ist E(I_t) = 0 und deshalb E(ΔP_t) = 0, solange der Auftragsindikator unabhängig mit gleichen Wahrscheinlichkeiten ±1 ist.
- Die wahre stetige Rendite hat E(r_t) = μ und Var(r_t) = σ² und ist iid.
- Im ACD-Modell ist ψ_i = E(x_i | F_{i−1}) die bedingte erwartete bereinigte Dauer zwischen dem (i−1)-ten und dem i-ten Trade.
- Die Innovationen erfüllen E(ε_i) = 1; für die Standard-Exponentialverteilung gilt zusätzlich Var(ε_i) = 1 und E(ε²_i) = 2.
- Für das schwach stationäre EACD(1,1) ist der unbedingte Erwartungswert μ_x = E(x_i) = E(ψ_i) = ω / (1 − γ1 − ω1).
- Im Ordered Probit ist E(ε_i | x_i) = 0, während die bedingte Varianz eine positive Funktion der erklärenden Größen w_i ist.
- Für die 206.794 IBM-Trades von 1988 sind die Stichprobenmittel von Preisänderung, Dauer und Spread −0,0010, 27,21 Sekunden und 1,9470 Ticks.
- Die erwartete adjustierte Dauer im WACD(1,1) für IBM ist 0,169/(1 − 0,064 − 0,885) = 3,31 Sekunden und liegt nahe am Stichprobenmittel 3,29 der adjustierten Dauern.
- Die erwartete Dauer des GACD(1,1) für dieselben IBM-Daten beträgt 3,52 und liegt etwas über der des WACD(1,1).
- Mittelwert und Standardabweichung einer standardisierten Weibull-Verteilung mit α = 0,879 sind 1,00 und 1,14; Stichprobenmittel und Standardabweichung der zugehörigen êi sind 1,01 und 1,22.
- Für die Exponentialverteilung mit β > 0 gelten E(X) = β und Var(X) = β²; bei β = 1 liegt die Standard-Exponentialverteilung vor.
- Für die Gammaverteilung mit κ > 0 und β > 0 gelten E(X) = κβ und Var(X) = κβ²; die Momente sind E(X^m) = β^m Gamma(κ + m)/Gamma(κ).
- Für die Weibull-Verteilung mit Skala β und Form α gilt E(X) = β Gamma(1 + 1/α); die standardisierte Variable Y = X/[β Gamma(1 + 1/α)] hat E(Y) = 1.
- Der Erwartungswert der verallgemeinerten Gammaverteilung ist E(X) = β Gamma(κ + 1/α)/Gamma(κ); mit λ = Gamma(κ)/Gamma(κ + 1/α) und Y = λX/β gilt E(Y) = 1.
- Unter Regularitätsbedingungen sind die bedingten Maximum-Likelihood-Schätzer eines ACD-Modells asymptotisch normal.
- Der Zuwachs eines Wiener-Prozesses von 0 bis t hat Erwartungswert 0 und Varianz t, wenn w0 fest und oft gleich 0 ist.
- Beim verallgemeinerten Wiener-Prozess dxt = µ dt + σ dwt gelten E(xt − x0) = µt und Var(xt − x0) = σ²t; µ und σ heißen Drift- und Volatilitätsparameter.
- Folgt der Preis der geometrischen Brownschen Bewegung, ist die Logpreisänderung von t bis T normal mit Mittel (µ − σ²/2)(T − t) und Varianz σ²(T − t).
- Bedingt auf Pt gilt E(PT) = Pt exp[µ(T − t)]; dieser Erwartungswert bestätigt µ als erwartete Renditerate der Aktie.
- Für eine standardnormalverteilte Zufallsvariable gilt E(ϵ⁴) = 3; daraus folgt E(σ²ϵ² Δt) = σ² Δt, und σ²ϵ² Δt konvergiert mit Δt gegen 0 auf die nichtzufällige Größe σ² Δt.
- Für IBM 1998 ergeben r̄ = 0,002276, sr = 0,01915 und Δ = 1/252 die Schätzungen σ̂ = 0,3040 und µ̂ = 0,6198, also 61,98 Prozent erwartete Rendite und 30,4 Prozent Standardabweichung pro Jahr.
- Für Cisco Systems 2007, 251 Beobachtungen, Mittel −3,81×10^−5 und sr = 0,0174, ergeben sich σ̂ = 0,275 und µ̂ = −0,0094.
- Bei einer Aktie mit Preis 50 Dollar, erwarteter Rendite 15 Prozent und Volatilität 40 Prozent pro Jahr beträgt der erwartete Preis in sechs Monaten 50 exp(0,15 × 0,5) = 53,89 Dollar.
- Die geschätzte erwartete Logrendite von Cisco Systems 2007 beträgt −0,94 Prozent pro Jahr, die geschätzte Standardabweichung 27,5 Prozent pro Jahr.
- Die stetig verzinste Jahresrendite r von t bis T ist normalverteilt mit Mittel µ − σ²/2 und Standardabweichung σ/√(T − t).
- Bei erwarteter Rendite 15 Prozent und Volatilität 10 Prozent pro Jahr ist diese Rendite über zwei Jahre normal mit Mittel 0,15 − 0,01/2 = 0,145 und Standardabweichung 0,1/√2 = 0,071.
- In der risikoneutralen Welt ist die erwartete Rendite aller Titel der risikofreie Zins r, und der Barwert eines Zahlungsstroms ist sein mit r diskontierter Erwartungswert.
- Der Preis eines europäischen Calls zur Zeit t ist ct = exp[−r(T − t)] E*[max(PT − K, 0)]; in der risikoneutralen Welt gilt µ = r.
- Bedingt auf Pt bestätigt E(PT) = Pt exp[µ(T − t)], dass µ die erwartete Renditerate der Aktie ist.
- Für die doppelte Exponentialverteilung gelten E(X) = κ, Var(X) = 2η² und E(e^X) = e^κ/(1 − η²).
- Die angenäherte einfache Rendite im Sprungdiffusionsmodell hat E(G) = µ Δt + κ λ Δt und Var(G) = σ² Δt + λ Δt [2η² + κ²(1 − λ Δt)].
- Unter dem risikoneutralen Maß ist der Drift der Aktie r − λ E(J − 1) = r − λψ mit ψ = e^κ/(1 − η²) − 1.
- Der Expected Shortfall ist der Erwartungswert der Verlustfunktion, gegeben dass der Value at Risk überschritten wird.
- Für eine standardnormalverteilte Größe X gilt E(X gegeben X > VaRq) = f(VaRq) / p, wobei p die obere Schwanzwahrscheinlichkeit, VaRq das zugehörige Quantil und f die Dichte der Standardnormalverteilung ist.
- Der Preis einer europäischen Call-Option im Jump-Diffusion-Modell ist der Erwartungswert, unter dem Maß P*, des diskontierten Endpayoffs.
- Im Black-Scholes-Anhang ist ln(PT) normalverteilt mit Erwartungswert ln(Pt) plus (r minus σ zum Quadrat durch 2) mal (T minus t).
- Der bedingte Erwartungswert der k-Perioden-Logrendite am Prognoseursprung h ist die Summe der Ein-Schritt- bis k-Schritt-Prognosen der Rendite.
- Im Modell rt = μ plus at ist diese Punktprognose kμ, und der Prognosefehler ist die Summe der k folgenden Innovationen.
- Unter bedingter Normalität N(μt, σ zum Quadrat von t) ist der Expected Shortfall μt plus [f(xq) / p] mal σt; für p = 0,01 ist das μt plus 2,6652 σt.
- Für eine verallgemeinerte Pareto-Verteilung mit 0 < ξ < 1 ist der mittlere Exzess über eine hohe Schwelle ηo gleich der Skala ψ(ηo) geteilt durch (1 minus ξ).
- Für jede höhere Schwelle ist diese Mean-Excess-Funktion linear in dem Abstand zur Ausgangsschwelle.
- Der Expected Shortfall ist der bedingte Erwartungswert des Verlusts gegeben, dass der VaR überschritten wird, also VaR plus dem bedingten Erwartungswert des Exzesses über den VaR.
- Für die verallgemeinerte Pareto-Verteilung ist dieser bedingte Exzess [ψ(η) plus ξ mal (VaR minus η)] geteilt durch (1 minus ξ), sofern 0 < ξ < 1.
- Ist das Modell für die Überschüsse angemessen, sind die transformierten Größen wti unabhängig und exponentialverteilt mit Erwartungswert 1 (Smith 1999).
- Bei einer schwach stationären vektoriellen Reihe ist der Mittelwertvektor μ gleich E(rt) über die Zeit konstant; der Erwartungswert wird elementweise über die gemeinsame Verteilung gebildet.
- Die Schwellen un steigen so, dass die erwartete Zahl der Überschreitungen beschränkt bleibt: der Limes superior von n mal [1 minus F(un)] ist endlich.
- Für ein schwach stationäres VAR(1) ist der Mittelwertvektor μ gleich (I minus Φ) hoch minus 1 mal φ0, sofern I minus Φ invertierbar ist. Mit φ0 gleich (I minus Φ) mal μ lautet das mittelwertbereinigte Modell r-tilde_t gleich Φ mal r-tilde von t minus 1 plus at.
- Für ein schwach stationäres VAR(p) ist μ gleich [Φ(1)] hoch minus 1 mal φ0, sofern die Inverse existiert.
- Der Erwartungswert von at ist 0. at ist mit rt minus ℓ für alle ℓ größer als 0 unkorreliert und heißt Schock oder Innovation zur Zeit t. Dasselbe gilt für die Vergangenheit in allen hier betrachteten Zeitreihenmodellen.
- Ist rt schwach stationär, konvergiert die ℓ-Schritt-Prognose eines VAR(p) mit wachsendem Horizont gegen den Mittelwertvektor μ.
- Für einen VMA(q) ist der Mittelwertvektor μ gleich E(rt) gleich dem Konstantenvektor θ0, sofern die Kovarianzmatrix der Schocks existiert.
- Die MA-Darstellung eines VAR(p) hat den Mittelwert μ gleich [Φ(1)] hoch minus 1 mal φ0, sofern die Inverse existiert.
- Die bedingte Likelihood eines VMA(1) setzt a0 gleich 0. Die exakte Likelihood behandelt a0 als unbekannten Vektor, der aus den Daten geschätzt wird.
- μw = E(wt) ist der Mittelwert des stationären Logpreisspreads und im Pairs-Handel der Gleichgewichtswert, um den der Spread schwankt.
- Die Rendite eines Portfolios aus einer long Aktie 1 und γ short Aktien 2 über i Perioden ist wt+i minus wt und hängt nicht vom Mittelwert von wt ab.
- Bei restricted constant μt = α c0 sind die Komponenten I(1) ohne Drift, und der stationäre Spread wt hat den von null verschiedenen Mittelwert −c0.
- Im Fehlerkorrekturmodell der wöchentlichen US-Treasury-Bill-Zinsen ist der Mittelwert der stationären Reihe etwa −0,225; der geschätzte Intercept beträgt 0,2254 bei einem Standardfehler von 0,0545 und einer t-Statistik von 4,14.
- Im Maximum-Likelihood-Fehlerkorrekturmodell von BHP und VALE ist der Spread wt = p1t − 0,718 p2t stationär mit Mittelwert 1,81. Die drei Handelsgrenzen in der Abbildung sind dieser Mittelwert sowie Mittelwert plus und minus 0,045.
- Unter der Normalannahme beträgt die Wahrscheinlichkeit, dass der Spread um die gewählte Zielabweichung von 0,045 von seinem Mittel abweicht, etwa 30 Prozent.
- Bei multivariater Normalität ist der bedingte Erwartungswert von x1 gegeben x2 = b gleich μ1 + Σ12 Σ22 hoch −1 mal (b − μ2). Diese bedingte Verteilung ist die Grundlage für Zeitreihenprognosen unter Normalität und für rekursive Kleinste-Quadrate-Schätzung.
- Im Faktormodell für Assetrenditen hat der gemeinsame Faktorvektor den Erwartungswert μf, und jeder spezifische Faktor εit hat den Erwartungswert null.
- Der Stichprobenmittelwert einer Überschussrendite ist in der Praxis oft nicht signifikant von null verschieden. Vor der Anpassung eines BARRA-Modells muss der Stichprobenmittelwert deshalb nicht unbedingt entfernt werden.
- Im orthogonalen statistischen Faktormodell ist der Erwartungswert der gemeinsamen Faktoren ft gleich null und der Erwartungswert der spezifischen Fehler εt gleich null.
- Die bedingte Erwartung µt = E(rt gegeben Ft−1) ist der bedingte Mittelwert der multivariaten Rendite. Für die meisten Renditereihen genügt dafür ein vektorielles ARMA mit exogenen Variablen, und µt ist die Einschritt-Prognose dieses Modells.
- In der Maximum-Likelihood-Schätzung des Faktormodells wird der Mittelwert µ durch den Stichprobenmittelwert geschätzt.
- Die gleichgewichtete Kovarianzschätzung der Innovationen setzt voraus, dass der Mittelwert jeder Innovation aj null ist.
- Für die gemeinsame Maximum-Likelihood-Schätzung des EWMA-Parameters und der Mittelgleichung wird angenommen, dass die Innovation at gleich rt minus µt den Mittelwert null hat.
- Im GARCH(1,1) mit konstanter Korrelation existiert der Erwartungswert von a hoch 2 zur Zeit t, wenn alle Eigenwerte von alpha1 plus beta1 positiv und kleiner als 1 sind. Die unbedingten Varianzen der beiden Schocks sind dann (I minus alpha1 minus beta1) hoch minus 1 mal phi0.
- Unter derselben Eigenwertbedingung ist die unbedingte Kovarianz zwischen den beiden Schocks gleich der konstanten Korrelation mal dem Produkt der beiden unbedingten Standardabweichungen.
- Im lokalen Trendmodell ist der bedingte Erwartungswert der Beobachtung yt gegeben Ft minus 1 gleich dem bedingten Erwartungswert des Zustands, yt|t minus 1 gleich μt|t minus 1, weil der Messfehler bedingten Erwartungswert null hat.
- Der Ein-Schritt-Prognosefehler vt gleich yt minus μt|t minus 1 hat Erwartungswert null.
- Satz 11.1: Sind x, y und z gemeinsam multivariat normal und die blockdiagonalen Kovarianzen nichtsingulär, dann ist E(x|y) gleich μx plus Σxy mal Σyy hoch minus 1 mal (y minus μy).
- Ist zusätzlich Σyz gleich 0, dann ist E(x|y, z) gleich E(x|y) plus Σxz mal Σzz hoch minus 1 mal (z minus μz).
- Die Zustandsprognose des lokalen Trends ist μt plus 1 gegeben t gleich μt gegeben t, weil die Zustandsinnovation ηt Erwartungswert null hat.
- Der geglättete Zustand μt|T ist der bedingte Erwartungswert E(μt | FT) und gleich μt|t minus 1 plus Σt|t minus 1 mal qt minus 1.
- Unter Normalität ist jeder Ein-Schritt-Fehler vt normal mit Mittel null und Varianz Vt. Die Likelihood ist das Produkt dieser bedingten Dichten.
- Akaikes Zustandsvektor eines ARMA-Modells besteht aus den bedingten Erwartungen yt plus j gegeben t gleich E(yt plus j | Ft), j von 0 bis m minus 1.
- Der Kalman-Filter berechnet die bedingten Erwartungswerte des Zustands: st|t gleich E(st | Ft) und st plus 1 gegeben t gleich dt plus Tt mal st|t.
- Der geglättete Zustand st|T ist E(st | FT).
- Die Prognose mit minimalem mittlerem quadratischem Fehler ist der bedingte Erwartungswert yt(j) gleich E(yt plus j | Ft) gleich ct plus j plus Zt plus j mal st plus j gegeben t.
- Die geglätteten Störungen sind die bedingten Erwartungen et|T gleich E(et | FT) und ηt|T gleich E(ηt | FT).
- Koopman (1993) schreibt den geglätteten Zustand als st plus 1 gegeben T gleich dt plus Tt mal st|T plus Rt Qt Rt′ mal qt, mit Start s1|T gleich s1|0 plus Σ1|0 mal q0.
- Die Prognosen mit minimalem mittlerem quadratischem Fehler erfüllen yt(j) = E(yt+j | Ft).
- Die Ein-Schritt-Prognose ist yt(1) = E(yt+1 | Ft) = ct+1 + Zt+1 st+1|t, wobei st+1|t aus dem Kalman-Filter am Prognoseursprung t stammt.
- Allgemein ist yt(j) = ct+j + Zt+j st+j|t, und st+j|t ist der bedingte Mittelwert von st+j gegeben Ft.
- Der E-Schritt des EM-Algorithmus von Dempster, Laird und Rubin (1977) setzt den bedingten Erwartungswert des fehlenden Werts ein.
- Der Gibbs-Punktschätzer ist das Mittel der Ziehungen nach dem Burn-in: θ̂i = 1/(n − m) mal Summe von j = m+1 bis n von θi,j.
- Für die Gammaverteilung mit positiven Parametern α und β gilt E(η) = α/β.
- Für die Betaverteilung gilt E(θ) = α/(α + β).
- Bei normalem Prior und normaler Stichprobe ist der Posteriormittelwert ein gewichtetes Mittel aus Priormittel und Stichprobenmittel mit Gewichten proportional zur Präzision.
- Die Stichprobenmittel der Gibbs-Ziehungen sind die Punktschätzer der Parameter im Regressionsmodell mit zeitreihenkorrelierten Fehlern.
- Für die invertierte Chi-Quadrat-Verteilung mit v Freiheitsgraden gilt E(Y) = 1/(v − 2), sofern v > 2.
- Beim AR(1) ist der gefilterte Wert eines fehlenden xh gleich [φ1 / (1 + φ1²)] (xh−1 + xh+1); wegen Zeitumkehrbarkeit erhalten die beiden Nachbarn gleiches Gewicht.
- Die Zwei-Schritt-Prognose von hn+1 am Ursprung n − 1 ist α0 + α1(α0 + α1 ln hn−1); die Zwei-Schritt-Rückwärtsprognose von h0 bei t = 2 ist α1² (ln h2 − η) mit η = α0/(1 − α1).
- Der Kleinste-Quadrate-Schätzer des fehlenden ln ht ist [α0(1 − α1) + α1(ln ht+1 + ln ht−1)] / (1 + α1²) und genau der bedingte Mittelwert aus Gleichung (12.23).
- Im Kalman-Filter sind zj|i und Σj|i bedingter Erwartungswert und bedingte Varianz des Zustands zj gegeben Fi.
- Die Rückwärtsziehung hat den bedingten Mittelwert µ*t = zt|t + α Σt|t Σt+1|t hoch −1 mal (zt+1 − zt+1|t).
- Ein kleines ei bedeutet, dass die Renditereihe dazu neigt, im i-ten Zustand zu bleiben, mit erwarteter Dauer 1/ei.
- Im Markov-Switching-GARCH-M für die monatlichen GE-Logrenditen 1926 bis 1999 betragen die erwarteten Dauern der beiden Zustände etwa 11 und 9 Monate; die Posterior-Mittel der Übergangswahrscheinlichkeiten sind e1 = 0,089 und e2 = 0,112.
- Im Modell (12.55) ist die zustandsabhängige Risikoprämie βi√ht der von der Volatilität abhängige Bestandteil der Rendite; zur Identifizierbarkeit gilt β2 > β1, sodass Zustand 2 die höhere Risikoprämie trägt.
- Beim einfachen GARCH-M der monatlichen GE-Logrenditen ist die Risikoprämie positiv und signifikant, mit rt = 0,182√ht + at und p-Werten aller Parameterschätzungen unter 0,0006.
- Die MCMC-Punktprognosen von Rendite und Volatilität sind die Stichprobenmittel der in den letzten Gibbs-Iterationen simulierten Realisationen.

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
- Der Stichprobenmittelwert aus T Beobachtungen ist µ̂x = (1/T) mal der Summe der xt.
- Sind die Logrenditen iid normal mit Mittel µ und Varianz σ², dann sind die einfachen Renditen iid lognormal mit Erwartungswert E(Rt) = exp(µ + σ²/2) − 1.
- Sind m1 und m2 Mittelwert und Varianz der lognormalen einfachen Rendite Rt, dann ist der Erwartungswert der zugehörigen Logrendite ln[(m1 + 1) / Wurzel(1 + m2/(1 + m1)²)].
- Der Mittelwertvektor eines Zufallsvektors X = (X1, …, Xp) ist E(X) = [E(X1), …, E(Xp)]′.
- Der Stichprobenmittelvektor ist (1/T) mal der Summe der xt und, zusammen mit der Stichprobenkovarianzmatrix, ein konsistenter Schätzer der theoretischen Größe, sofern die Kovarianzmatrix existiert.
- Für die zur stationären Reihe gehörige iid-Folge gilt unter lim n[1 minus F(un)] gleich τ die Grenzbeziehung lim P(Maximum ≤ un) gleich exp(minus τ).

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
- Für die prozentualen täglichen einfachen IBM-Renditen, Beginn 2. Januar 1970, n = 9845, Ende 31. Dezember 2008, beträgt der Stichprobenmittelwert 0,040161.
- Tabelle 1.2, Mittelwerte der täglichen einfachen Renditen in Prozent: S&P 0,029, value-weighted 0,040, equal-weighted 0,076, IBM 0,040, Intel 0,108, 3M 0,045, Microsoft 0,123, Citigroup 0,067.
- Tabelle 1.2, Mittelwerte der monatlichen einfachen Renditen in Prozent: S&P 0,58 bei n = 996 ab Januar 1926, value-weighted 0,89, equal-weighted 1,22, IBM 1,35, Intel 2,21 bei n = 432 ab Januar 1973, 3M 1,24, Microsoft 2,62 bei n = 273 ab April 1986, Citigroup 1,17 bei n = 266 ab November 1986.
- Der t-Test der prozentualen IBM-Logrenditen ergibt t = 1,5126, df = 9844, p = 0,1304 und ein 95-Prozent-Intervall von −0,007641473 bis 0,059290531. R und S-Plus liefern dieselben Werte.
- Beim angepassten AR(3) der monatlichen einfachen Renditen des wertgewichteten Index ist phi-Dach 0 auf dem 1-Prozent-Niveau signifikant, die erwartete mittlere Rendite also positiv: µ-Dach gleich 0,0091 geteilt durch (1 minus 0,116 plus 0,019 plus 0,104) gleich 0,009.
- In R bezeichnet der Intercept des AR(3) der vierteljährlichen realen US-BSP-Wachstumsrate den Mittelwert der Reihe, geschätzt mit 0,0077; die Konstante ist (1 minus 0,348 minus 0,1793 plus 0,1423) mal 0,0077 gleich 0,0047355.
- Für die ersten 984 Monate des wertgewichteten Index sind Stichprobenmittel und Standardfehler 0,0095 und 0,0540; wegen der schwachen seriellen Abhängigkeit laufen Prognosen und Standardabweichungen der Prognosefehler des neu geschätzten AR(3) schnell auf diese Werte zu.
- In R ist der Intercept des AR(3) der Mittelwert, 0,0089; die Konstante phi0 beträgt (1 minus 0,1158 plus 0,0187 plus 0,1042) mal dem Mittel der Reihe, gleich 0,00896761.
- Im verfeinerten Modell ohne Lag 2 ist der in R ausgewiesene Intercept 0,0089, und phi0 gleich (1 minus 0,1136 plus 0,1063) mal 0,0089 gleich 0,00883503.
- Der Mittelwert der monatlichen Logrenditen von 3M, 0,0103, hat den Standardfehler 0,0023 und ist auf dem 1-Prozent-Niveau von null verschieden; der Einstichprobentest auf Mittel null hat die t-Ratio 4,44 und einen p-Wert nahe 0.
- Für einen US-Titel mit µ = 20 Prozent, σ = 20 Prozent, Δt = 1/252 Jahr, λ = 10, κ = −0,02 und η = 0,02 werden etwa 10 Tagessprünge pro Jahr mit mittlerer Sprunggröße −2 Prozent unterstellt; die Vergleichsverteilung hat Mittel 0.
- Der Text empfiehlt, vor dem Peaks-over-Thresholds-VaR das Stichprobenmittel zu entfernen. Bei den IBM-Tageslogrenditen ist es positiv; sein Abzug erhöht den VaR leicht und verändert die Parameterschätzungen wenig.
- Die monatlichen prozentualen Logrenditen von Januar 1926 bis Dezember 2008, 996 Beobachtungen inklusive Dividenden, haben den Mittelwert 1,089 für IBM und 0,430 für den S&P 500.
- Im vereinfachten VAR(5) sind beide Konstanten positiv und signifikant, 1,0 für IBM mit Standardfehler 0,22 und 0,4 für den S&P 500 mit Standardfehler 0,18. Die Logpreise hatten über die Stichprobe einen Aufwärtstrend.
- Die Stichprobenmittel der monatlichen einfachen Renditen fünf US-Anleiheindizes von Januar 1942 bis Dezember 1999, 696 Beobachtungen, sind 10 hoch minus 2 mal (0,43; 0,45; 0,45; 0,46; 0,44) für die Laufzeiten 30, 20, 10, 5 und 1 Jahr.
- Die 1- bis 6-Schritt-Prognosen des verfeinerten VAR(5) am Ursprung Dezember 2008, h gleich 996, lauten für IBM 1,95, 0,30, minus 0,82, 0,14, 1,16 und 1,29 sowie für den S&P 500 1,70, 0,17, minus 1,26, minus 0,49, 0,41 und 0,65, jeweils in Prozent.
- Die bedingte Likelihood des vereinfachten VAR(5) schätzt die Konstanten als 1,039 mit Standardfehler 0,223 für IBM und 0,390 mit Standardfehler 0,176 für den S&P 500.
- Im VAR(1) aus S-Plus sind die Achsenabschnitte 1,0614 für IBM, t-Statistik 4,7198, und 0,4087 für den S&P 500, t-Statistik 2,3053. Die 6-Schritt-Prognosen 1,0909 und 0,4280 liegen schon am Stichprobenmittel; sie konvergieren schneller als die des VAR(5).
- Im VARMA(2,1) der logarithmierten Treasury-Sätze sind die Konstanten 0,028 mit Standardfehler 0,014 für den 1-Jahres-Satz und 0,025 mit Standardfehler 0,011 für den 3-Jahres-Satz.
- Die 1- bis 6-Schritt-Prognosen der bedingten Likelihood am Ursprung 996 lauten für IBM 1,954, 0,304, minus 0,815, 0,138, 1,162 und 1,294 sowie für den S&P 500 1,698, 0,173, minus 1,263, minus 0,494, 0,408 und 0,649.
- Tabelle 9.1 gibt für Januar 1990 bis Dezember 2003 die monatlichen Überschussrenditen in Prozent als Mittelwert und, laut Fußnote, Standardfehler an: Alcoa 1,09 (9,49), A.G. Edwards 1,36 (10,2), Caterpillar 1,23 (8,71), Ford 0,97 (9,77), FedEx 1,14 (9,49), General Motors 0,64 (9,28), Hewlett-Packard 1,37 (11,8), Kimberly-Clark 0,78 (6,50), Mellon 1,36 (7,80), New York Times 0,81 (7,37), Procter & Gamble 1,08 (6,75), Chicago Tribune 0,95 (7,84), Texas Instruments 2,19 (13,8), S&P 500 0,42 (4,33).
- Die Stichprobenmittel der monatlichen Logrenditen in Prozent von IBM, Hewlett-Packard, Intel, J.P. Morgan Chase und Bank of America von Januar 1990 bis Dezember 2008, 228 Beobachtungen einschließlich Dividenden, sind 0,70, 0,99, 1,20, 0,82 und 0,41.
- Die Mittelwerte der Tagesrenditen in Prozent von Euro-Kurs, Yen-Kurs, IBM und Dell, Januar 1999 bis Dezember 2004, 1496 Beobachtungen, sind im Wesentlichen null: 0,0091, minus 0,0059, 0,0066 und 0,0028.
- Die Stichprobenmittel der Tageslogrenditen in Prozent von S&P 500, Cisco und Intel, 2. Januar 1991 bis 31. Dezember 1999, betragen 0,066, 0,257 und 0,156.
- Der gemeinsame Faktor xt gleich 0,796 mal der IBM-Logrendite plus 0,605 mal der S&P-500-Logrendite hat die Mittelgleichung xt gleich 1,317 plus 0,096 mal xt−1 plus at.
- In Tabelle 12.1, letzte 2000 von 2100 Gibbs-Iterationen, betragen die Posteriormittel β = 0,793, φ1 = 0,184, φ2 = −0,036 und σ² = 0,00479; der Posteriormittelwert von σ liegt bei etwa 0,069.
- Die klassischen Schätzer derselben Zinsregression sind 0,782 für die Steigung, 0,183 und −0,036 für die AR-Koeffizienten und σ̂a = 0,068.
- Für die wöchentlichen Dreijahreszinsänderungen liefert Gibbs nach 1050 Iterationen, davon 50 Burn-in, die Posteriormittel 0,252, 0,003 und 0,110 sowie σ̂² = 0,0118, nahe an den Maximum-Likelihood-Werten 0,227, 0,006, 0,114 und 0,0128.
- Der Posteriormittelwert der Ausreißergröße bei t = 323 ist −0,304, bei t = 201 ist er 0,176.
- Die Posteriormittel des univariaten SV-Modells sind µ = 0,409, α0 = 0,454, α1 = 0,837 und σ²v = 0,086.
- Die Posteriormittel des bivariaten Modells für IBM und S&P 500 sind β01 = 0,53, β02 = 0,51, α10 = 0,75, α11 = 0,80, σ²1v = 0,07, α20 = 0,43, α21 = 0,81, σ²2v = 0,07, γ0 = 0,38 und σ²u = 0,07.
- Der Startwert von µ ist das Stichprobenmittel der Logrenditen; die Startwerte von α und σ²v sind die Kleinste-Quadrate-Schätzung von ln(h0t) aus dem angepassten GARCH(1,1).

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
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 14–33 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-002-p014-p033|S. 14–33]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 52–71 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-004-p052-p071|S. 52–71]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 180–199 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-014-p180-p199|S. 180–199]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 199–214 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-015-p199-p214|S. 199–214]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 20–39 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-002-p020-p039|S. 20–39]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 39–58 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-003-p039-p058|S. 39–58]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 58–77 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-004-p058-p077|S. 58–77]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 77–96 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-005-p077-p096|S. 77–96]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 96–115 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-006-p096-p115|S. 96–115]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 134–153 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-008-p134-p153|S. 134–153]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 153–172 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-009-p153-p172|S. 153–172]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 191–210 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-011-p191-p210|S. 191–210]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 210–229 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-012-p210-p229|S. 210–229]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 229–248 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-013-p229-p248|S. 229–248]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 248–267 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-014-p248-p267|S. 248–267]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 267–286 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-015-p267-p286|S. 267–286]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 286–305 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-016-p286-p305|S. 286–305]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 305–324 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-017-p305-p324|S. 305–324]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 324–343 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-018-p324-p343|S. 324–343]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 343–362 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-019-p343-p362|S. 343–362]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 362–381 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-020-p362-p381|S. 362–381]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 381–400 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-021-p381-p400|S. 381–400]]
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
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 58–77 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-004-p058-p077|S. 58–77]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 77–96 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-005-p077-p096|S. 77–96]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 96–115 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-006-p096-p115|S. 96–115]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 438–457 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-024-p438-p457|S. 438–457]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 476–495 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-026-p476-p495|S. 476–495]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 514–533 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-028-p514-p533|S. 514–533]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 533–552 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-029-p533-p552|S. 533–552]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 571–590 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-031-p571-p590|S. 571–590]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 590–609 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-032-p590-p609|S. 590–609]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 609–628 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-033-p609-p628|S. 609–628]]

## Verwandte Themen
