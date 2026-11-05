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
- In den Abbildungen der Stichprobenautokorrelation monatlicher IBM- und CRSP-Renditen von 1926 bis 2008 markieren zwei waagerechte gestrichelte Linien die zweifachen Standardfehlergrenzen; Werte innerhalb dieser Grenzen gelten auf dem 5-Prozent-Niveau als nicht von null verschieden.
- Die gepunkteten Linien der partiellen Autokorrelation der vierteljährlichen realen US-BSP-Wachstumsrate von 1947.II bis 1991.I sind die ungefähren zweifachen Standardfehlergrenzen plus oder minus 2 geteilt durch die Wurzel aus 176 und geben ein punktweises 95-Prozent-Konfidenzintervall an.
- Mit T gleich 996 ist der asymptotische Standardfehler der Stichproben-PACF des monatlichen wertgewichteten CRSP-Index ungefähr 0,032.
- Ist der Schock at normalverteilt, lautet die 95-Prozent-Ein-Schritt-Intervallprognose eines AR(p) die Punktprognose plus oder minus 1,96 mal σa; die Varianz des Ein-Schritt-Prognosefehlers ist σa zum Quadrat.
- Intervallprognosen für den Zwei-Schritt-Horizont werden auf dieselbe Weise aus der Varianz des Zwei-Schritt-Prognosefehlers gebildet.
- Werden geschätzte Parameter für Punkt- und Intervallprognosen verwendet, entsteht eine bedingte Prognose, die die Unsicherheit der Parameterschätzer nicht berücksichtigt; bei hinreichend großem Schätzsample liegt sie nahe an der unbedingten Prognose.
- Parameter- und Modellunsicherheit lassen sich über Bayes-Prognosen mit Markov-Chain-Monte-Carlo einbeziehen; in diesem Kapitel wird das Modell der Einfachheit halber als gegeben behandelt.
- Abbildung 11.3 zeigt die gefilterte Zustandsvariable der logarithmierten realisierten Tagesvolatilität von Alcoa und ihr punktweises 95-Prozent-Konfidenzintervall.
- Abbildung 11.4 zeigt die geglättete Zustandsvariable und ihr punktweises 95-Prozent-Intervall. Die Intervalle der geglätteten Zustände sind schmaler als die der gefilterten.
- Die Breite des 95-Prozent-Intervalls von μ1|1 hängt vom Startwert Σ1|0 ab.
- Die gezeichneten Grenzen sind die Zustandsschätzung plus und minus 2 mal der Wurzel der zugehörigen Zustandsvarianz, für gefilterte und für geglättete Zustände, über 340 Tage.
- Für die geglätteten unbeobachteten Komponenten der logarithmierten Quartalsgewinne von Johnson & Johnson werden punktweise 95-Prozent-Konfidenzbereiche als geglätteter Zustand plus oder minus zwei Standardabweichungen gezeichnet.
- Werden zu einer Prognose 98-Prozent-Konfidenzintervalle abgefragt, sollte die wahre Antwort nur in 2 Prozent der Fälle außerhalb liegen; tatsächlich liegt sie in 30 bis 40 Prozent der Fälle außerhalb.
- Im Test von Russo und Schoemaker (1989) geben die Teilnehmer zu zehn Fragen einen 90-Prozent-Konfidenzbereich an. Bei guter Kalibrierung liegt nur eine Antwort außerhalb der eigenen Grenzen.
- Von über 1000 Teilnehmern bei Russo und Schoemaker hatten weniger als 1 Prozent neun oder mehr Antworten innerhalb ihrer Grenzen; die meisten verfehlten vier bis sieben Fragen.
- Die Auflösungen des Tests sind: Martin Luther King starb mit 39 Jahren, der Nil ist 4187 Meilen lang, die OPEC hat 13 Mitglieder, das Alte Testament hat 39 Bücher, der Monddurchmesser beträgt 2160 Meilen, eine leere Boeing 747 wiegt 390000 Pfund, Mozart wurde 1756 geboren, die Tragzeit des asiatischen Elefanten beträgt 645 Tage, die Luftlinie London–Tokio beträgt 5959 Meilen, der tiefste bekannte Meerespunkt liegt bei 36198 Fuß.
- Perfekte statistische Kalibrierung liegt auf der 45-Grad-Linie, wenn die genannte Wahrscheinlichkeit gegen die tatsächliche Häufigkeit steht.
- Bei Plous (1991) lagen Ärzte, die zu 90 Prozent sicher waren, in weniger als 15 Prozent der Fälle richtig. Wettervorhersager liegen nahe an der perfekten Kalibrierung.
- Bei guter Kalibrierung sollte etwa eine von zehn Antworten außerhalb der Grenzen liegen. Bei Glaser, Langer und Weber (2005) hatten professionelle Investoren einen Median von fast acht solchen Ausreißern von zehn, Studierende einen Median von sechs. Allgemeinwissen und Finanzfragen wurden zu einem Score von zehn gemittelt.
- Tyszka und Zielonka (2002) bauten drei einander ausschließende und erschöpfende Ausgänge mit je etwa 0,33 Wahrscheinlichkeit. Gut kalibriert wäre eine Konfidenz von 33 Prozent. Analysten nannten im Schnitt knapp über 58 Prozent, Wettervorhersager knapp über 50 Prozent.
- In derselben Studie lag nur etwa ein Drittel der Analysten richtig und etwa zwei Drittel der Wettervorhersager.
- Bei Torngren und Montgomery (2004) lagen professionelle Aktienwähler, die zu 100 Prozent sicher waren, in weniger als 15 Prozent der Fälle richtig.
- Graham und Harvey werten die Duke-CFO-Umfrage aus. Die Manager nennen zu ihren Renditeprognosen 80-Prozent-Konfidenzintervalle. Nur in 30,5 Prozent der Fälle lag die tatsächliche Rendite innerhalb dieser Intervalle.
- Bei Davis et al. (1994) steigerte redundante Information die selbst berichtete Konfidenz der Gewinnprognose signifikant über die Basis aus drei Quartalen EPS, Nettoumsatz und Kurs. Nicht-redundante Information steigerte die Konfidenz noch einmal deutlich über die redundante Information. In allen drei Bedingungen war die Überkonfidenz massiv.

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
- Die Standardfehler der Impulsantworten im S-Plus-Beispiel werden asymptotisch berechnet. Bei Lag 0 betragen sie 0,1569 für die IBM-Antwort auf den eigenen orthogonalen Schock, 0,1558 für die S&P-Antwort auf den IBM-Schock und 0,0948 für die S&P-Antwort auf den eigenen Schock.

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
- Für die prozentualen täglichen einfachen IBM-Renditen, n = 9845, gibt basicStats die Grenzen des 95-Prozent-Konfidenzintervalls für den Mittelwert als 0,006724 und 0,073599 an.
- Derselbe Output nennt den Standardfehler des Stichprobenmittelwerts mit 0,017058 und den Stichprobenmittelwert mit 0,040161.
- Der t-Test der prozentualen IBM-Logrenditen, n = 9845, liefert ein 95-Prozent-Konfidenzintervall für den Mittelwert von −0,007641473 bis 0,059290531. R und S-Plus weisen dieselben Grenzen aus.
- Die Hypothese, der Erwartungswert dieser Logrenditen sei null, wird auf dem 5-Prozent- und auf dem 10-Prozent-Niveau nicht verworfen; t = 1,5126, df = 9844, p = 0,1304.
- In der Prognose des wertgewichteten Index ab dem Ursprung t gleich 984, Dezember 2007, markieren zwei gestrichelte Linien die zweifachen Standardfehlergrenzen; außer der Rendite vom Oktober 2008 liegen alle tatsächlichen Monatsrenditen 2008 innerhalb der 95-Prozent-Prognoseintervalle.
- In der Stichproben-ACF des gleichgewichteten CRSP-Index von 1926 bis 2008 bezeichnen die zwei gestrichelten Linien die zweifachen Standardfehlergrenzen.
- Für die vierteljährlichen Gewinne von Johnson & Johnson werden am Prognoseursprung des vierten Quartals 1978, nach Schätzung auf den ersten 76 Beobachtungen, Ein- bis Acht-Schritt-Prognosen mit 95-Prozent-Intervallprognosen berechnet; in der Abbildung sind das die gestrichelten Linien.
- Die Punktprognosen der Gewinne je Aktie entstehen durch eine Antilog-Transformation aus den Prognosen der Loggewinne und nutzen den in Kapitel 1 angegebenen Zusammenhang von Normal- und Lognormalverteilung.
- Beim Random Walk divergiert die Varianz des l-Schritt-Prognosefehlers mit l mal σa zum Quadrat, und die Länge einer Intervallprognose von p(h plus l) geht mit wachsendem Horizont gegen unendlich.
- Für die stetig verzinste Jahresrendite mit Mittel 0,145 und Standardabweichung 0,071 ist ein 95-Prozent-Konfidenzintervall 0,145 ± 1,96 × 0,071 pro Jahr, also von 0,6 Prozent bis 28,4 Prozent.
- Abbildung 7.4 zeigt den Hill-Schätzer der täglichen IBM-Logrenditen von 1962 bis 1998 mit punktweisem 95-Prozent-Konfidenzintervall gegen q; die Schätzung ist stabil, außer bei kleinem q.
- Die Standardfehler des Hill-Schätzers stehen für q = 190, 200 und 210 bei den Renditen bei 0,022, 0,021 und 0,021 und bei den negativen Renditen bei 0,021, 0,021 und 0,020.
- Die Prognoseplots des angepassten VAR(1) für die monatlichen prozentualen Logrenditen von IBM und S&P 500 zeigen die Punktprognosen zusammen mit punktweisen 95-Prozent-Konfidenzintervallen und den letzten 12 Beobachtungen.
- Die Prognoseplots des Fehlerkorrekturmodells der wöchentlichen Treasury-Bill-Zinsen zeigen punktweise 95-Prozent-Konfidenzintervalle. Ursprung ist der 6. August 2004, der Horizont reicht von 1 bis 10 Schritten.
- Wegen der Unit-Root-Nichtstationarität sind diese Intervalle breit und nicht informativ. Die Standardfehler der Niveau- und der Differenzprognosen stimmen überein und wachsen vom 1-Schritt-Wert 0,2009 und 0,1807 über den 2-Schritt-Wert 0,3222 und 0,2927 auf den 10-Schritt-Wert 0,8460 und 0,8157.
- Die Niveau-Punktprognosen bleiben eng beieinander: 1 Schritt 1,4501 und 1,7057, 10 Schritte 1,4722 und 1,7078 für 3- und 6-Monatszins. Die Differenzprognosen lauten 1 Schritt −0,0378 und −0,0642 sowie 10 Schritte −0,2276 und −0,1314.
- Für die Trendkomponente reicht die obere Grenze bis 2,795702 und die untere bis −0,5948943.
- Für die saisonale Komponente reicht die obere Grenze bis 0,3788652 und die untere bis −0,3552441.
- Aufgabe 11.2 verlangt Zeitplots der gefilterten und geglätteten Zustände der Alcoa-Logvolatilität mit punktweisem 95-Prozent-Konfidenzintervall.

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
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 20–39 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-002-p020-p039|S. 20–39]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 39–58 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-003-p039-p058|S. 39–58]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 58–77 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-004-p058-p077|S. 58–77]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 77–96 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-005-p077-p096|S. 77–96]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 96–115 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-006-p096-p115|S. 96–115]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 324–343 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-018-p324-p343|S. 324–343]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 343–362 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-019-p343-p362|S. 343–362]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 362–381 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-020-p362-p381|S. 362–381]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 438–457 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-024-p438-p457|S. 438–457]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 457–476 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-025-p457-p476|S. 457–476]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 590–609 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-032-p590-p609|S. 590–609]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 628–647 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-034-p628-p647|S. 628–647]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 115–134 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-007-p115-p134|S. 115–134]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 134–153 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-008-p134-p153|S. 134–153]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 153–172 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-009-p153-p172|S. 153–172]]

## Verwandte Themen

- Konfidenzintervalle und Hypothesentests werden für die Kapitel 4 und 5 angekündigt.
