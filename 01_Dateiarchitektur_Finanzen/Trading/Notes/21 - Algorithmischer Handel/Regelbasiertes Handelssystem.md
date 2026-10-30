---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Systementwicklung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Regelbasiertes Handelssystem


## Kurzdefinition

- Eine Investmentstrategie ist ein Algorithmus, der eine Marktunvollkommenheit behauptet, und die Handelsregel ist die Taktik für Ein- und Ausstieg.
- Eine Regel ist eine Funktion, die eine oder mehrere Informationseinheiten, die Eingabe, in eine empfohlene Marktposition verwandelt, etwa long, short oder neutral.
- Objektive Methoden heißen auch mechanische Handelsregeln oder Handelssysteme; in diesem Buch heißen alle objektiven Methoden einfach Regeln.
- Eine Methode ist genau dann objektiv, wenn sie als Computerprogramm eindeutige Marktpositionen long, short oder neutral erzeugen kann; alles, was sich nicht so reduzieren lässt, ist subjektiv.
- Eine künstliche Handelsregel ist ein computersimuliertes Handelssignal, dessen Genauigkeit, der Anteil richtiger Signale, experimentell gesetzt werden kann, sodass die erwartete Rendite bekannt ist.
- Eine Regel ist ein Eingabe-Ausgabe-Prozess. Sie verwandelt eine oder mehrere Zeitreihen in eine neue Zeitreihe aus +1 und −1, die Long- und Short-Positionen im gehandelten Markt, dem S&P 500, anzeigen.

## Kernaussagen

- Strategien können sehr unterschiedlich sein, während die Taktiken vergleichsweise einheitlich sind.
- Es gibt Dutzende Hedgefonds-Stile, und jeder Stil betreibt Dutzende eigener Strategien.
- Eine Position wird eröffnet, wenn das Signal der Strategie einen festgelegten Wert erreicht.
- Der Ausstieg wird oft durch ein Gewinnziel und einen Stop-Loss festgelegt.
- Die Handelsregel ist das Paar aus Stop-Schwelle und Gewinnschwelle.
- Die rohe Kalibrierung definiert alternative Paare, testet jedes historisch und wählt das Paar mit der höchsten Sharpe Ratio.
- Die bei der Auswahl maximierte Sharpe Ratio ist der mittlere Gewinn der Regel geteilt durch die Standardabweichung des Gewinns.
- Trotz des Bemühens, den Handelsprozess wissenschaftlich und regelbasiert zu machen, bleiben Bereiche, in denen subjektives Urteil wichtig ist.
- Dass manchmal Urteil nötig ist, macht quantitative Regeln nicht nutzlos und algorithmische Händler nicht weniger fähig als diskretionäre.
- Kahneman schreibt, Experten seien Algorithmen in jedem Bereich mit erheblicher Unsicherheit einheitlich unterlegen, vom Sieger von Fußballspielen bis zur Lebenserwartung von Krebspatienten.
- Man kann hoffen, dass der Finanzmarkt keine Ausnahme dieser Regel ist.
- Fondsmanager behalten eine aktive Rolle: Sie urteilen, ob die Modelle nach einem Strukturwandel noch gültig sind.
- Objektive Signalmethoden haben einen klaren Endpunkt, das nachfolgende Signal zum Schließen der Position, und der Gewinn oder Verlust wird vom Kaufsignal bis zu diesem Verkaufssignal gerechnet.
- Nur objektive Methoden erzeugen Signale ausschließlich aus Information, die zum jeweiligen Zeitpunkt bekannt war, und bewerten diese Signale objektiv.
- Vorhersageregeln, oft wissenschaftliche Gesetze genannt, sagen einen wiederkehrenden Prozess aus, etwa dass Ereignis A dazu neigt, Ereignis B vorherzusagen, und sie erklären nicht, warum das geschieht.
- Erklärende Theorien gehen weiter und sagen, warum B auf A zu folgen tendiert; Theorien der Behavioral Finance versuchen zu erklären, warum Finanzmärkte zeitweise nichtzufällig sind, und können erklären, warum bestimmte Methoden der technischen Analyse funktionieren können.
- Gesetze und Theorien unterscheiden sich in ihrer Reichweite: Eine Regel, die auf allen Märkten und allen Zeitskalen wirkt, hätte höheren wissenschaftlichen Rang als eine, die nur bei Kupfer-Futures auf Stundendaten funktioniert.
- In Wissenschaft und Geschäftswelt übernimmt eine neue Praktikergruppe, die Quants, einen wissenschaftlichen Ansatz, und einige der erfolgreichsten Hedgefonds nutzen Strategien, die sich wissenschaftliche technische Analyse nennen ließen.
- Objektive und subjektive Wahrnehmungen sind wesentlich verschieden: Objektive Beobachtungen lassen sich teilen und von anderen bestätigen, subjektive Deutungen und Gefühle nicht, und dieser Mangel allein disqualifiziert subjektive technische Analyse als legitime Erkenntnis.
- Beobachtungen müssen auf Zahlen gebracht werden, wenn sie rational und streng analysiert werden sollen; wer sein Tun nicht in mathematischen Begriffen beschreiben kann, betreibe nach der Mehrheit der Wissenschaftler keine Wissenschaft.
- Als Beispiel für neu zu etablierendes Wissen nennt der Text, dass eine TA-Regel wirksamer vorhersagt als ein zufällig erzeugtes Signal.
- Hat die TA-Regel Vorhersagekraft, dann sollte sie im Backtest Gewinne erzeugen; aus diesen Gewinnen folgt die Vorhersagekraft nicht.
- Ein profitabler Backtest kann ebenso damit verträglich sein, dass die Regel nur Glück hatte.
- Übernähme die Technische Analyse die wissenschaftliche Methode, wäre die wichtigste Folge die Beseitigung subjektiver Ansätze, weil sie nicht prüfbar, vor empirischer Herausforderung geschützt und damit bedeutungslose Aussagen ohne Information sind, schlimmer als falsch.
- Ihre Beseitigung machte die Technische Analyse zu einer vollständig objektiven Praxis.
- Subjektive Ansätze würden entweder in objektive Methoden umgewandelt oder aufgegeben.
- Gann-Linien, subjektive Divergenzen, Trendkanäle und viele subjektive Muster mögen gültige Aspekte des Marktverhaltens enthalten, doch in subjektiver Form bleibt dieses Wissen versagt.
- Die Umwandlung eines subjektiven Verfahrens in ein objektives ist nicht trivial; als Beispiel dient ein Algorithmus zur automatischen Erkennung von Schulter-Kopf-Schulter-Mustern.
- Wer subjektiv weiterarbeitet, sollte künftig nur falsifizierbare Prognosen abgeben, damit das Gelieferte gehaltvoll ist; gehaltvoll heißt hier nicht richtig, sondern dass der Wahrheitsgehalt an der nachfolgenden Marktaktion klar entscheidbar ist.
- Eine Prognose, die nicht klar macht, welche künftigen Ereignisse Vorhersagefehler sind, sagt im Kern, dass jedes Ergebnis eintreten kann.
- Die meisten subjektiven Marktaufrufe sind derzeit bedeutungslos, wahrscheinlich weder den Abnehmern noch den Analysten offensichtlich.
- Die Technische Analyse wird in vier Teilmengen geteilt: subjektive TA, objektive TA mit unbekannter statistischer Signifikanz, objektive TA ohne statistischen Wert und objektive TA mit statistischer Signifikanz.
- Subjektive TA sind Methoden, die sich nicht auf einen backtestbaren Algorithmus reduzieren lassen.
- Die zweite Teilmenge besteht aus objektiven Methoden von unbekanntem Wert: Sie sind objektiv und können gebacktestet sein, ihre Ergebnisse wurden aber nicht auf statistische Signifikanz geprüft.
- Die dritte Teilmenge, nutzlose TA, sind objektive Regeln, die umfassend gebacktestet und statistisch bewertet wurden und weder allein noch in Kombination mit anderen Methoden einen Mehrwert liefern.
- Die Mehrheit der objektiven TA-Methoden fällt vermutlich in diese dritte Teilmenge, weil Finanzmärkte wegen Komplexität und Zufall extrem schwer vorhersagbar sind und in allen Wissenschaften die meisten vorgeschlagenen Ideen nicht funktionieren.
- Fehlschläge werden typischerweise weder in der Laienpresse noch in wissenschaftlichen Zeitschriften berichtet; am wichtigsten ist ein Verfahren, das Methoden entfernt, die nicht funktionieren.
- Die vierte Teilmenge, nützliche TA, sind objektive Methoden mit statistisch signifikanten oder, besser, ökonomisch signifikanten Ergebnissen.
- Einige Regeln sind für sich nützlich; wegen Komplexität und Zufälligkeit der Märkte ist es wahrscheinlich, dass die meisten erst in Kombination mit anderen Regeln, als komplexe Regeln, einen Mehrwert liefern.
- Evidence-based Technical Analysis bezeichnet die dritte und vierte Teilmenge, also objektive TA, die gebacktestet und einer statistischen Analyse unterzogen wurde.
- Auf Währungen wurde der verhältnismäßig komplizierte Schulter-Kopf-Schulter-Algorithmus von einem viel einfacheren objektiven Zigzag-Signal deutlich übertroffen, und als bestätigendes oder widerlegendes Signal fügte das Muster keinen Wert hinzu.
- Informelle Datenanalyse kann gültiges Wissen aus Finanzmärkten nicht ziehen, weil Scheinmuster zahlreich und gültige Muster von Rauschen verhüllt sind; strenge statistische Verfahren sind dafür deutlich besser geeignet.
- Wenn die Technische Analyse ihre Ansprüche einlösen soll, muss sie auf einem wissenschaftlichen Vorgehen mit formaler statistischer Analyse ruhen.
- Ist eine Regel in einer Stichprobe historischer Daten profitabel gewesen, ist diese Stichprobenstatistik eine unbestreitbare Tatsache. Offen bleibt, ob die künftige Leistung wahrscheinlich profitabel ist, weil echte Vorhersagekraft vorliegt, oder unwahrscheinlich, weil die vergangenen Gewinne Zufall waren.
- Der Hypothesentest ist ein formales und strenges Schlussverfahren, das entscheidet, welche dieser Alternativen eher richtig ist, und kann damit helfen zu entscheiden, ob es rational wäre, die Regel künftig im echten Handel zu verwenden.
- Die Studien zu Regeln in Teil 2 verwenden die Schätzung als Ergänzung zu den Hypothesentests.
- Die Ausgaben einer Regel sind plus 1 für long und minus 1 für short.
- Die Rendite eines Tages ist das Produkt aus dieser Ausgabe und der Preisänderung des Marktes einen Tag voraus.
- Eine Rauschregel paart die Ausgaben zufällig mit den Preisänderungen und zerstört damit jede Vorhersagekraft.
- Die Nullhypothese lautet, die Regel habe keine Vorhersagekraft und ihre erwartete Rendite sei null oder kleiner; die Alternative behauptet eine erwartete Rendite größer als null.
- Die mittlere Rendite in der historischen Stichprobe ist eine unverzerrte Schätzung der mittleren Rendite in der unmittelbar praktischen Zukunft.
- Ein Fehler erster Art führt zum Einsatz einer wertlosen Regel und setzt Kapital einem Risiko ohne Ausgleichsaussicht aus; ein Fehler zweiter Art lässt eine nützliche Regel ungenutzt.
- Der Fehler erster Art wiegt schwerer, weil erschöpftes Kapital aus dem Spiel wirft, während verpasste Gelegenheiten nachkommen.
- Vor dem Bootstrap werden die Tagesrenditen der Regel nullzentriert, indem der mittlere Tagesertrag von jedem Tag abgezogen wird; das ist von der Trendbereinigung zu unterscheiden, die den mittleren täglichen Marktänderungssatz bereits auf null setzt.
- Die Spezifikationen einer Regel sind die mathematischen oder logischen Operationen auf einer oder mehreren Marktreihen, die daraus eine Zeitreihe von Positionen machen.
- Data Mining sucht die Spezifikationen mit der höchsten Leistung.
- Bei der Kreuzung zweier Durchschnitte kauft die Regel, wenn der kurze Durchschnitt den längeren nach oben kreuzt, und verkauft, wenn er ihn nach unten kreuzt; die Parameter sind die beiden Rückblickfenster.
- Trendfolge, einschließlich Kanalausbrüchen und Bändern um gleitende Durchschnitte, ist eine Klasse neben Mean-Reversion, Extremwertregeln, Divergenzregeln und Diffusionsregeln.
- Teil Zwei untersucht drei Themen, Trends, Extremwerte und Übergänge sowie Divergenz, jedes mit einer in Kapitel 8 definierten Regelform.
- Bei der Regelsuche bleibt die Komplexität, die Zahl der Parameter, fest, und einfache Regeln werden nicht zu komplexeren verbunden.
- Die Regelinduktion sucht die Komplexität mit der besten Leistung und lernt, Regeln mit logischen Operatoren oder mathematischen Funktionen zu verbinden.
- Der objektive Techniker sucht eine künftig profitable Regel; der Schluss von der Backtest-Kennzahl auf die erwartete Leistung ist der Kern der objektiven technischen Analyse.
- Unter ziemlich allgemeinen Bedingungen erhöht mehr gebacktestete Regeln die Chance, eine gute Regel zu finden.
- Noch vor einem Jahrzehnt begrenzten die Kosten das Data Mining auf Institutionen; Rechner, Software und Datenbanken machen es für Einzelne praktikabel.
- Scheitert die einzige geprüfte Regel, endet die Forschung; beim Data Mining wird die Regel verfeinert oder neu definiert, über Zehner, Hunderte, Tausende oder mehr Regeln.
- Die beobachtete Leistung einer Regel besteht aus echter Vorhersagekraft, falls vorhanden, und aus Zufall.
- Vorhersagekraft ist ein wiederkehrendes Merkmal des Marktverhaltens, das die Regel ausnutzt und das in der unmittelbar praktischen Zukunft anhalten sollte; der Zufallsanteil sollte das nicht.
- Selbst die wirksamsten Regeln der technischen Analyse haben relativ wenig Vorhersagekraft, weil Finanzmärkte komplex und hochgradig zufällig sind.
- Für eine Regel mit erwarteter Rendite null ist null die wahrscheinlichste Rendite, deutlich höhere oder niedrigere Renditen bleiben durch Glück oder Pech möglich.
- Glück auf einer wertlosen Regel erzeugt eine positive Rendite und kann wie ein Fund wirken; die Signale trafen die Marktschwankungen nur zufällig.
- Eine extrem hohe oder niedrige Durchschnittsrendite ist für eine einzelne Regel unwahrscheinlich und wird wahrscheinlicher, je mehr Regeln gebacktestet werden; der Data Miner wählt diese glückliche Regel.
- Die überlegene Regel mit der höchsten erwarteten Rendite wird nicht immer gewählt, weil eine schwächere Regel durch eine glückliche beobachtete Leistung gewinnen kann.
- Ist der Merit-Abstand zum nächsten Konkurrenten groß, weist die beste beobachtete Leistung verlässlicher auf die überlegene Regel; ist er klein, lässt die Überlappung eine erhebliche Chance, dass die schwächere gewählt wird.
- Von zwei oft unterstellten Leistungen eines Mehrfachvergleichs trifft zu, dass die Regel mit der besten beobachteten Leistung künftig am ehesten die beste ist, sofern viele Beobachtungen eingehen; eine verlässliche Schätzung ihrer künftigen Leistung liefert er bei Backtests der technischen Analyse nicht.
- White zeigt, dass die Wahrscheinlichkeit gegen 1 geht, dass die Regel mit der höchsten erwarteten Rendite die beste beobachtete Leistung hat, wenn die Stichprobengröße gegen unendlich geht.
- Experimente später im Kapitel zeigen außerdem, dass die Regel mit der höchsten beobachteten Leistung bei genügend Beobachtungen eine höhere erwartete Rendite hat als eine zufällig gezogene Regel.
- Wo Zufall das Ergebnis kaum beeinflusst, wie beim Vomblattspiel um eine erste Geige, sagt die vergangene Leistung die künftige voraus, und selbst ein unglücklicher besserer Kandidat schlägt einen glücklichen schwächeren, weil die Verteilungen sich nicht überlappen.
- Die Performancehistorien dieser Regeln bestehen aus Monatsrenditen, und die erwartete Rendite wird über die Wahrscheinlichkeit eines profitablen Monats gesteuert.
- Wird nur eine Regel gebacktestet, gibt es kein Data Mining und keinen Data-Mining-Bias.
- Beim Optimieren einer Crossover-Regel aus zwei gleitenden Durchschnitten unterscheiden sich die Regeln nur in der Tageszahl des kurzfristigen und des langfristigen Durchschnitts; 26 und 55 Tage sind mit 27 und 55 hoch korreliert.
- Im Walk-Forward heißt der In-Sample-Abschnitt Trainingsdatensatz, weil dort die besten Parameterwerte der Regel gelernt werden, und der Out-of-Sample-Abschnitt Testdatensatz, weil die gelernten Parameter dort auf Performance geprüft werden.
- In jeder neuen Realisierung des Datenfensters kann eine neue Regel formuliert werden.
- Hsu und Kuan fanden adaptive Handelsregeln, von ihnen Lernstrategien genannt, in einem Test von über 36.000 objektiven Regeln wirksam.
- Die Verwandlung ist durch einen oder mehrere mathematische, logische oder Zeitreihen-Operatoren definiert, die auf die Eingabe-Zeitreihen angewendet werden. Eine Regel ist also durch eine Menge von Operationen definiert.
- Die Fallstudie testet 6402 einzelne Regeln aus drei Themen. Trendregeln erzeugen Long und Short anhand des aktuellen Trends der untersuchten Reihe. Extrem- und Übergangsregeln erzeugen Long und Short, wenn die Reihe ein extremes Hoch oder Tief erreicht oder zwischen Extremwerten wechselt.
- Divergenzregeln erzeugen Signale, wenn der S&P-500-Index in die eine Richtung trendet, während eine begleitende Datenreihe in die andere trendet.
- Die Regeln nutzen mehrere geläufige Analysemethoden, darunter gleitende Durchschnitte, Kanalausbrüche und Stochastics, die der Text Kanalnormierung nennt.
- Um den Umfang handhabbar zu halten, wurden nur einzelne Regeln getestet. Komplexe Regeln aus der Verbindung von zwei oder mehr Einzelregeln mit mathematischen oder logischen Operatoren wurden nicht betrachtet.
- Das ist aus zwei Gründen nachteilig. Wenige Praktiker verlassen sich auf eine einzelne Regel, und komplexe Regeln nutzen Informationssynergien. Mindestens eine Studie zeigt gute Performance komplexer Regeln, selbst wenn die einfachen Bestandteile einzeln unprofitabel sind. Intuitives Kombinieren ist extrem schwierig, automatisierte Verfahren existieren.
- Die Performancestatistik ist die durchschnittliche Rendite jeder Regel über 1980 bis 2005 auf trendbereinigten S&P-500-Daten. Die Trendbereinigung setzt die durchschnittliche tägliche Preisänderung auf null und entfernt den Effekt eines Long- oder Short-Bias.
- Ist die Long-Bedingung schwerer zu erfüllen als die Short-Bedingung, verbringt die Regel die meiste Zeit short. Auf Daten mit positiver durchschnittlicher Tagesänderung würde ihre Durchschnittsrendite bestraft, ohne dass diese Strafe ihre Vorhersagekraft misst.
- Die Nullhypothese der Fallstudie lautet, keine der 6402 Regeln habe Vorhersagekraft. Das Signifikanzniveau für die Verwerfung ist 5 Prozent.
- Manche Regeln nutzen rohe Zeitreihen, die vor der Positionslogik nicht transformiert werden, etwa den S&P-500-Schluss. Andere nutzen Indikatoren, etwa den Negative Volume Index aus S&P-500-Schluss und gesamtem täglichem NYSE-Volumen.
- Bei wiederkehrenden Prognoseproblemen sind subjektive Prognosen über viele Felder selten besser als Prognosen auf Basis selbst einfacher statistischer Regeln.
- Ein wiederkehrendes Prognoseproblem ist eines, bei dem dieselbe Art von Prognose wiederholt auf einem ähnlichen Informationssatz zu stellen ist. Technische Analyse ist ein solches Problem.
- Ist die Beziehung komplex und umfasst sie mehr als nur wenige Faktoren, steht der Entscheider vor einem konfiguralen Denkproblem, das die menschlichen Grenzen übersteigt, und der subjektive Experte fällt auf Intuition zurück.
- Meehls Metaanalyse von 1954 über 20 Studien fand in jedem Fall, dass das statistische Modell genauere Prognosen lieferte oder beide Methoden gleichauf lagen.
- Die von Meehl zusammengefassten Studien betrafen Studienerfolg, die Wahrscheinlichkeit erneuter Straffälligkeit und die Ergebnisse von Elektroschocktherapie.
- Sawyers Metaanalyse von 45 Studien fand keine einzige Studie, in der das klinische Globalurteil der statistischen Prognose, von Sawyer mechanische Kombination genannt, überlegen war.
- Das galt auch in Studien, in denen der menschliche Experte Zugang zu Information hatte, die das statistische Modell nicht berücksichtigte.
- Die Studienleistung von 37.500 Matrosen in einer Marineausbildung wurde durch ein Modell auf Testwerten genauer vorhergesagt als durch Urteiler, die die Testwerte hatten und persönliche Interviews geführt hatten.
- Die Urteiler gaben der nuancierten Information aus den Interviews zu viel Gewicht und den objektiv messbaren Fakten zu wenig.
- Bei Camerer waren die subjektiven Expertenurteile am ungenauesten und das lineare Regressionsmodell am genauesten. Die mittlere Korrelation betrug 0,64 für das Modell und 0,33 für die Experten.
- Im Informationsgehalt, gemessen am quadrierten Korrelationskoeffizienten, waren die Modellprognosen im Mittel 3,76-mal so informativ wie die der Experten.
- Bei der Prognose der Gewalttendenz neu aufgenommener männlicher psychiatrischer Patienten aus 19 Eingaben lag 1983 die mittlere Expertenkorrelation bei 0,12, der beste Experte bei 0,36 und ein lineares Modell auf denselben Eingaben bei 0,82, nahezu 50-mal informativer.
- Meehl schloss 1986, dass bei damals gegen 90 und inzwischen mehr als 150 Untersuchungen, von Fußballspielausgängen bis zur Leberdiagnose, kaum ein halbes Dutzend Studien auch nur eine schwache Tendenz zugunsten des Klinikers zeigt.
- Grove und Meehl fanden 1996 über 136 Studien, dass die Regeln in 96 Prozent der Studien die Experten übertrafen oder ihnen gleichkamen.
- Swets, Monahan und Dawes verglichen 2000 subjektives Expertenurteil, statistische Regeln und eine Kombination, in der der Experte die Ausgabe der statistischen Regel abändert. Weiter allein subjektiv zu urteilen sei nicht nur prognostisch falsch, sondern vielleicht auch ethisch falsch.
- Tetlock findet den subjektiven Stil des Fuchses den anderen menschlichen Stilen überlegen, zeigt aber, dass alle menschlichen Prognosen gegenüber formalen Modellen verblassen.
- Formale Modelle auf verallgemeinerten autoregressiven verteilten Lags übertreffen menschliche Experten in der zweidimensionalen Bewertung aus Diskrimination und Kalibrierung deutlich.
- Cowles zeigte, dass von 1902 bis 1929 die Hälfte der Prognosen von Hamilton, dem Herausgeber des Wall Street Journal, zur Richtungsänderung falsch war. Auch 20 Versicherungen, 16 Finanzdienste und 24 Finanzpublikationen hatten unscheinbare Ergebnisse.
- In einer Hulbert-Studie wurden 57 Newsletter von August 1987 bis August 1998 verfolgt. Weniger als 10 Prozent schlugen die zusammengesetzte Rendite des Wilshire 5000.

## Funktionsweise

- Der numerische Weg schätzt zuerst Sigma und phi des Ornstein-Uhlenbeck-Prozesses.
- Danach wird ein Gitter aus Stop- und Gewinnschwellen gebildet, im Beispiel 20 mal 20 Knoten vom halben Sigma bis zum zehnfachen Sigma.
- Auf jedem Knoten werden die künstlichen Pfade ausgewertet und eine Sharpe Ratio berechnet.
- Gewählt wird das beste Paar, oder der beste Stop zu einem vorgegebenen Gewinnziel, oder das beste Gewinnziel zu einem vorgegebenen maximalen Stop.
- Die lineare Regel setzt die gehaltenen Einheiten proportional zum negativen Z-Score des Einheitsportfolios, mit Lookback gleich der Halbwertszeit.
- Es gibt dabei keine Strategieparameter, die anhand der Performance optimiert werden.
- Ein- und Ausstieg laufen fortlaufend mit dem Z-Score, nicht über selektive Schwellen.
- Die Eingabe besteht aus einer oder mehreren Finanzmarkt-Zeitreihen, und mathematische sowie logische Operatoren verwandeln sie in eine Zeitreihe empfohlener Marktpositionen.
- Die Ausgabe wird üblicherweise als vorzeichenbehaftete Zahl dargestellt; positive Werte bedeuten Long-Positionen, negative Werte Short-Positionen.
- Eine Regel erzeugt ein Signal, wenn sich der Wert der Ausgabezeitreihe ändert, und das Signal verlangt eine Änderung der zuvor empfohlenen Marktposition.
- Die einfachste Regel hat eine binäre Ausgabe mit nur zwei Werten, zum Beispiel +1 und −1, und kann auch Long gegen neutral oder Short gegen neutral empfehlen.
- Alle in diesem Buch betrachteten Regeln sind binäre Long/Short-Regeln mit der Ausgabe {+1, −1}.
- Eine Strategie auf einer binären Long/Short-Regel ist immer entweder long oder short; solche Regeln heißen Reversal-Regeln, weil jedes Signal von long nach short oder von short nach long umkehrt.
- Ein Schwellenwert ist das kritische Niveau, das informative Änderungen der Eingabe von irrelevanten Schwankungen trennt; die Eingabe gilt als Mischung aus Information und Rauschen, und die Schwelle wirkt als Filter.
- Regeln mit Schwelle setzen ein Signal, wenn die Zeitreihe die Schwelle nach oben oder nach unten kreuzt, erkannt über Ungleichungen wie größer-als und kleiner-als: oberhalb ist die Ausgabe +1, sonst −1.
- Eine Schwelle kann fest sein oder sich mit der analysierten Reihe ändern; variable Schwellen passen zu Reihen mit Trends, also großen und lang anhaltenden Niveauänderungen, bei denen feste Schwellen unpraktisch werden.
- Der gleitende Durchschnitt und der Alexander-Reversal-Filter, auch Zickzack-Filter genannt, sind Operatoren, mit denen variable Schwellen definiert werden.
- Feste Schwellenregeln passen zu Reihen ohne Trend, die hier locker stationär heißen: relativ stabiler Durchschnitt und Schwankungen in einer ungefähr horizontalen Spanne.
- Trendbehaftete Reihen werden durch Differenzen oder Verhältnisse detrendet; das Verhältnis zum gleitenden Durchschnitt erzeugt eine stationäre Fassung, auf der feste Schwellenregeln möglich sind.
- Eine einzige Schwelle erzeugt eine binäre Regel, weil die Zustände darüber und darunter sich ausschließen und zusammen alle Fälle abdecken.
- Zwei Schwellen erzeugen drei Zustände, über der oberen, unter der unteren oder dazwischen, und dafür genügt die einfache Ungleichung nicht.
- Bei mehreren Schwellen setzt ein Ereignis die Ausgabe, das Kreuzen einer bestimmten Schwelle in einer bestimmten Richtung, und diese Ausgabe bleibt bis zum gegenseitig ausschließenden zweiten Ereignis bestehen.
- Das Aufwärtskreuzen der oberen Schwelle setzt +1 und das Abwärtskreuzen der unteren Schwelle −1; der Operator heißt Flip-Flop und gilt für feste und für variable Schwellen.
- Hayes ergänzt Schwellen um einen Richtungsmodus auf einer stationären Reihe wie einem Diffusionsindikator: die Zone plus die Richtung über die jüngsten fünf Wochen, mit Zonenschwellen wie 40 und 60.
- Zwei Schwellen und zwei Richtungen ergeben sechs einander ausschließende Zustände; eine binäre Regel kann einem davon +1 und den anderen fünf −1 zuweisen, so Hayes bei seinem Indikator Big Mo.
- Komplexe Regeln werden abgeleitet, indem die Information aus zwei oder mehr einfachen Regeln verbunden wird, um die Vorhersagekraft zu erhöhen.
- Zwei Fragen sind dabei zentral: welche Regeln verbunden werden und in welcher mathematischen oder logischen Form ihre Ausgänge zum Ausgang der komplexen Regel werden.
- Die einfachste Verbindung ist linear und summiert die Ausgänge der einfachen Regeln; jede Regel trägt so bei, als leiste sie einen von den anderen unabhängigen Beitrag.
- Die allgemeine gewichtete lineare Form ist Y gleich a0 plus a1 mal r1 plus a2 mal r2 bis an mal rn, wobei ri der Ausgang der i-ten Regel, ai ihr Gewicht und a0 eine Konstante, der Achsenabschnitt, ist.
- Eine nichtlineare Verbindung berücksichtigt Wechselwirkungen: der Beitrag einer einzelnen Regel zum kombinierten Wert Y hängt in irgendeiner Weise von den Ausgängen der anderen Regeln ab.
- Der Vorteil der nichtlinearen Verbindung ist, dass sie komplexere Informationsmuster ausdrücken kann; der Nachteil ist, dass sie sich oft nicht als saubere, leicht verständliche Gleichung schreiben lässt.
- Weil unklar bleibt, wie die Regelausgänge zusammenwirken, werden nichtlineare Modelle manchmal Blackbox-Formeln genannt; Kombinationen aus neuronaler Netzsoftware sind ein Beispiel.
- Bei stetigen Eingaben ist die Antwortfläche einer linearen Kombination eben, ohne Hügel und Täler, und die Steigung bezüglich jeder Eingabe bleibt über den ganzen Bereich dieser Eingabe konstant.
- Die Steigung bezüglich der Eingabe X1 ist der Koeffizient a1, die bezüglich X2 der Koeffizient a2; a1 und a2 werden typischerweise per Regression aus Daten geschätzt und richten zusammen mit dem Achsenabschnitt a0 die Ebene so aus, dass sie die Datenpunkte am besten schneidet.
- In einem nichtlinearen Modell ist der Wert Y nicht einfach eine gewichtete Summe der einzelnen Eingaben, und die Steigung der Antwortfläche bezüglich einer Eingabe Xi ist nicht über ihren ganzen Bereich konstant, sodass Hügel und Täler entstehen.

## Voraussetzungen

- Benötigt werden Schätzwerte für Sigma und phi sowie der Einstiegspreis und die Prognose der Gelegenheit.

## Anwendung im Trading

- Manche Strategien nutzen makroökonomische Größen wie BIP oder Inflation, andere Fundamental- und Bilanzdaten, wieder andere suchen arbitrageähnliche Fehlpreise von Derivaten.
- Die Positionsgröße skaliert den Gewinn und lässt die Sharpe Ratio unverändert, deshalb werden die Ergebnisse je gehaltener Einheit angegeben.
- Ein Urteilspunkt ist ein bevorstehendes Großereignis, bei dem zu entscheiden ist, ob dem Modell getraut, der Hebel gesenkt oder das Modell vorübergehend abgeschaltet wird.
- Ein zweiter ist, ob Kelly auf das Eigenkapital des Gesamtportfolios oder auf jede Strategie einzeln angewendet wird.
- Die Mathematik bevorzugt die erste Lösung nur bei unveränderten erwarteten Renditen und Volatilitäten; der Autor bevorzugt praktisch die zweite, damit schwache Strategien schnell auslaufen.

## Regeln und Kriterien

- Eine Behauptung ist nur prüfbar, wenn der Zustand der Welt, falls sie wahr ist, erkennbar anders ist als der Zustand, falls sie falsch ist.
- Vertreter subjektiver Methoden stehen vor der Wahl, die Methode objektiv zu reformulieren und damit der empirischen Widerlegung auszusetzen, wie es ein Praktiker des Elliott-Wave-Prinzips getan hat, oder zuzugeben, dass sie nur im Glauben angenommen werden kann.
- Traditionell ist die Moving-Average-Cross-Regel bullisch mit Ausgabe +1 oberhalb des gleitenden Durchschnitts und bärisch mit Ausgabe −1 unterhalb.
- Inverse Regeln kehren diese Ausgabe um, −1 oberhalb und +1 unterhalb, und werden mitgetestet, weil ein traditionell als steigend gelesenes Muster fallende Kurse vorhersagen kann oder keine der beiden Lagen Prognosewert hat.
- Der Maßstab ist die Performance einer Regel ohne Prognosekraft, eines Zufallssignals, so wie ein Medikament ein Placebo schlagen muss; ein strengerer Maßstab ist zulässig, ein schwächerer nicht.
- Der Vorsprung über den Benchmark muss groß genug sein, um Glück auszuschließen, weil auch eine Regel ohne Prognosekraft den Benchmark in einer Stichprobe durch Zufall schlagen kann.
- Für den Vergleich eigenständiger Handelsregeln sind die Handelskosten anzusetzen, weil häufige Umkehrsignale höhere Kosten verursachen als seltene.
- In diesen Studien wurden keine Handelskosten angesetzt, weil das Ziel Prognosekraft war und nicht eine eigenständige Strategie; Kosten können den Wert einer häufig umkehrenden Regel verdecken.
- Eine positive Backtest-Abweichung von null führt nur dann dazu, die Regel als vorhersagend zu behandeln, wenn sie größer ist, als die um null zentrierte Stichprobenverteilung als Zufallsschwankung plausibel macht.

## Risiken und Grenzen

- Transaktionskosten können in das Verfahren aufgenommen werden, und die Abbildungen zeigen den Fall ohne sie, damit die Symmetrie der Funktionen sichtbar bleibt.
- Die üblichen Stop-Losses lassen sich bei Mean-Reversion-Strategien logisch nicht einsetzen.
- Unbekanntes Höchstkapital und nicht handelbare infinitesimale Stückzahlen machen die einfachste Regel unpraktisch.
- Subjektive technische Analyse ist nicht einmal falsch, sondern schlimmer als falsch: eine falsche Aussage hat wenigstens kognitiven Gehalt und lässt sich prüfen, die Sätze subjektiver Methoden sind leere Behauptungen und gegen empirische Prüfung abgeschirmt.
- Viel populäre technische Analyse wird mit Tradition oder Autorität gerechtfertigt statt mit formaler Logik und objektiven Belegen: Heutige Autoritäten zitieren frühere, diese noch frühere, zurück bis zu einer Quelle, deren Wissen vor allem intuitiv war, und die beiden Fehlschlüsse verstärken sich gegenseitig.
- Die wissenschaftliche Methode ist kein Kochbuch, das die Entdeckung von Wissen automatisiert, sondern eine Menge von Verfahren, um Phänomene zu beschreiben und zu deuten, mit dem Ziel, Behauptungen zu prüfen und einen Wissensbestand aufzubauen, der für Ablehnung oder Bestätigung offen ist.
- Informelle Beobachtung und intuitiver Schluss scheitern besonders, wenn die Phänomene komplex oder hoch zufällig sind, und das Verhalten der Finanzmärkte zeigt beides.
- Eine Regel, die nur Long- oder Neutral-Signale, also plus 1 oder 0, erzeugt und nur in steigenden Märkten getestet wurde, hätte auch ohne Vorhersagekraft wahrscheinlich Gewinn gemacht, und der Schluss auf fallende Märkte ist unwahrscheinlich zutreffend.
- Studien, die aus einer kleinen Zahl erfolgreicher Signale auf Vorhersagekraft schließen, sind wahrscheinlich voreilige Verallgemeinerungen, also Induktionen aus zu wenigen oder zu schlechten Belegen.
- Schlüsse aus induktiver Verallgemeinerung sind von Natur aus unsicher, weil sie über die beobachteten Fälle hinaus auf noch nicht beobachtete gleichartige Fälle springen und nur mit einer gewissen Wahrscheinlichkeit wahr sind.
- Selbst ein über die Zeit aufgebauter profitabler Track Record bedeutungsvoller subjektiver Prognosen lässt unklar, was er darstellt, weil die Ableitung unbestimmt ist und nicht erkennbar ist, ob ein konsistentes, wiederholbares Verfahren dahintersteht.
- Studien zum subjektiven Expertenurteil zeigen, dass Experten Information von einem Urteil zum nächsten nicht konsistent kombinieren.
- Intuitive Urteile leiden unter ernsthaften zufälligen Inkonsistenzen durch Ermüdung, Langeweile und alle Faktoren, die Menschen ausmachen.
- Bei exakt demselben Muster von Marktdaten zu verschiedenen Zeiten ist es gut möglich, dass ein subjektiver Analyst nicht dieselbe Prognose gibt.
- Bedeutungsvolle Track Records können auch aus konkreten Transaktionsempfehlungen entstehen, die in Echtzeit abgegeben werden.
- Die Beschränkung der Fallstudie auf einfache Regeln bildete nicht ab, was subjektive oder objektive Analysten tun, die sich selten auf eine einzige Regel stützen.
- Subjektive Analysten sind zudem stark darin beschränkt, das Informationsmuster einer Konfiguration aus mehreren Regeln richtig zu deuten.
- Eine nichtlineare Kombination einfacher Regeln kann informativer sein als die summierte Information ihrer einzelnen Bestandteile.
- Evidence-based Technical Analysis hat als wichtigste Grenze, dass kontrollierte Experimente nicht möglich sind. Technische Analyse ist zwangsläufig eine Beobachtungswissenschaft, die neues Wissen in der Historie suchen muss.

## Beispiele

- Verkaufen Finanzintermediäre Off-the-Run-Anleihen zwei Tage vor einer Auktion von US-Treasuries, verkauft die Regel diese Anleihen drei Tage vor der Auktion.
- Ein Wechsel der Ausgabe von +1 auf −1 verlangt, eine zuvor gehaltene Long-Position zu schließen und eine neue Short-Position zu eröffnen.
- Eine komplexe Regel mit Ausgabe im Bereich {+10, −10} kann die Positionsgröße variieren; +10 kann long 10 Kupferkontrakte bedeuten, und ein Wechsel von +10 auf +5 verlangt, 5 Kontrakte zu verkaufen.
- Einfache technische Regeln, einzeln und in Kombination, können statistisch und ökonomisch signifikante Gewinne erzielen, wenn sie auf Aktienindizes aus relativ jungen Unternehmen angewendet werden, den Russell 2000 und den NASDAQ Composite.
- Teil 2 bewertet ungefähr 6.400 binäre Long/Short-Regeln auf dem S&P 500.
- Hayes verbindet den Zustand über 60 bei Aufwärtsrichtung mit einer Rendite des Value Line Composite Index von 50 Prozent per annum; dieser Zustand trat zwischen 1966 und 2000 etwa 20 Prozent der Zeit auf.
- Liegt der Diffusionsindikator über 60 und ist die jüngere Änderung negativ, ist die annualisierte Marktrendite null; dieser Zustand trat etwa 16 Prozent der Zeit auf.
- Beim Renditedifferenzial zwischen BAA- und AAA-Unternehmensanleihen wurden Auf- und Abwärtstrends beide als mögliche Kaufsignale geprüft, weil die Lesart nicht offensichtlich ist.
- Ein Long-Bias entsteht, wenn die Long-Bedingung leichter erfüllt ist als die Short-Bedingung, und hebt die Backtest-Rendite in einem steigenden Markt ohne Prognosekraft an; im Beispiel ist man im S&P 500 nur short, solange der Dow Jones Transportation Average unter dem Band von −3 Prozent um seinen gleitenden Durchschnitt liegt, und sonst long.
- Gab Regel X in 20 Jahren 1.000 Kaufsignale und lag der Markt in 700 Fällen nach 10 Tagen höher, setzt der induktive Schluss die künftige Wahrscheinlichkeit eines höheren Marktes nach 10 Tagen auf 0,7.
- Die Aussage, die Indikatoren sagten einen Anstieg um unendlich viel Prozent, einen Fall um 100 Prozent oder irgendetwas dazwischen voraus, ist offensichtlich nicht falsifizierbar.
- Die Aussage, auf Basis der Indikatoren bullisch zu sein, ist ebenso bedeutungslos, weil unklar bleibt, wann der Anstieg eintreten soll oder unter welchen Umständen die Prognose falsch wäre.
- Gehaltvoll wird die Aussage, wenn der Markt um mehr als 10 Prozent vom aktuellen Niveau steigen soll, bevor er um mehr als 5 Prozent fällt; jeder Rückgang von mehr als 5 Prozent vor einem Anstieg von 10 Prozent stuft die Prognose als Fehler ein.
- Die Regel MA50 hält eine Long-Position im S&P 500, wenn der Schlusskurs größer ist als ein 50-Tage-Durchschnitt, und andernfalls eine Short-Position.
- Für MA50 behauptet die Alternativhypothese Vorhersagekraft und eine erwartete Rendite größer als null auf trendbereinigten Daten. Null ist die erwartete Rendite einer Regel ohne Vorhersagekraft. Die Nullhypothese behauptet eine erwartete Rendite von null oder weniger.
- Die Regel TT-4-91 ist ein 91-Tage-Kanalausbruch auf dem Dow-Jones-Transportation-Index und lieferte von November 1980 bis Juni 2005 Signale auf den S&P 500.
- Auf trendbereinigten S&P-500-Daten betrug die annualisierte Rendite 4,84 Prozent, und eine Regel ohne Vorhersagekraft hat auf solchen Daten die erwartete Jahresrendite null.
- Der Bootstrap-p-Wert 0,0692 gilt als möglicherweise signifikant, wenn nur diese eine Regel zum Backtest vorgeschlagen wurde; die Monte-Carlo-Permutation kommt zum fast gleichen p-Wert.
- Das Beispiel geht im S&P 500 long, wenn der Schlusskurs des Dow-Jones-Transportation-Average geteilt durch den Schlusskurs des S&P 500 über dem 50-Tage-Durchschnitt dieses Verhältnisses liegt, sonst short.
- Die Spezifikation nutzt Verhältnis und gleitenden Durchschnitt, Größer-als, Wenn-dann-sonst, die Konstante 50 und die beiden Reihen; dieser Satz schlug jede andere geprüfte Spezifikation.
- Hsu und Kuan probierten drei Methoden für komplexe Regeln: Voting-Regeln und Fractional-Position-Regeln, beide linear, sowie eine Learning Rule.
- Die Learning Rule verbindet Regeln nicht, sondern wählt aus einer Menge ähnlicher einfacher Regeln diejenige mit der besten jüngeren Leistung.
- Voting und Fractional Position sind im Wesen additive Kombinationen aller einfachen Regeln innerhalb eines Themas, etwa aller Channel-Breakout-Regeln oder aller Regeln auf einem gleitenden Durchschnitt des On-Balance Volume.
- Ashbys Gesetz der erforderlichen Varietät verlangt, dass ein Problem und seine Lösung ähnliche Grade von Komplexität haben; ein Modell, das einen Finanzmarkt vorhersagen soll, muss deshalb ebenfalls komplex sein.
- Nichtlineare Kombinationen lassen sich mit autonomen Lernsystemen erzeugen, darunter neuronale Netze, Entscheidungsbäume und ihre Ensembles, multiple Regressionssplines, Kernelregression, polynomiale Netze, genetische Programmierung und Support-Vector-Machines.
- Diese Systeme synthetisieren per induktiver Verallgemeinerung eine komplexe nichtlineare Regel, indem sie aus einer großen Menge historischer Beispiele lernen; jedes Beispiel ist ein Fall mit Indikatorwerten zu einem Datum und dem Wert der vorherzusagenden Ergebnisvariable.
- Komplexe nichtlineare Regeln ließen sich auf zwei Wegen ableiten: die Regeln in binärer Form als Kandidateneingaben vorlegen oder die von den Regeln verwendeten Indikatoren vorlegen.

## Unterschiedliche Quellenpositionen

- Die Zertifizierungsprüfung der Market Technicians Association zum Chartered Market Technician verkörpert die subjektive Tradition von Dow, Gann, Shabacker, Elliott sowie Edwards und Magee.
- Der Wechsel zu einem evidenzbasierten objektiven Ansatz würde vieles davon als bedeutungslos oder statistisch nicht hinreichend gestützt angreifen; manche Methoden überstehen die Objektivierung und die statistische Prüfung.
- Das Falsifizierbarkeitskriterium soll nicht jede Forschung an gerade entstehenden Methoden abschneiden.
- Die Sozionomik, ein Auswuchs der Elliott-Wellen-Theorie, gilt derzeit als vorwissenschaftlich und kann nach einem Gespräch mit Professor John Nofsinger noch keine prüfbaren Vorhersagen machen, weil dafür die soziale Stimmung quantifiziert werden muss, die nach der Sozionomik die entscheidende Bestimmungsgröße der Marktbewegung ist.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 1–20 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-001-p001-p020|S. 1–20]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 20–39 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-002-p020-p039|S. 20–39]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 58–77 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-004-p058-p077|S. 58–77]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 96–115 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-006-p096-p115|S. 96–115]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 115–134 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-007-p115-p134|S. 115–134]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 134–153 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-008-p134-p153|S. 134–153]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 153–172 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-009-p153-p172|S. 153–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 210–229 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-012-p210-p229|S. 210–229]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 229–248 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-013-p229-p248|S. 229–248]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 248–267 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-014-p248-p267|S. 248–267]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 267–286 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-015-p267-p286|S. 267–286]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 286–305 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-016-p286-p305|S. 286–305]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 305–324 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-017-p305-p324|S. 305–324]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 381–400 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-021-p381-p400|S. 381–400]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 457–476 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-025-p457-p476|S. 457–476]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 42–61 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-004-p042-p061|S. 42–61]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 270–289 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-019-p270-p289|S. 270–289]]

## Verwandte Themen

- Die statistische Prüfung der zweiten Teilmenge ist die Anwendung der Methoden aus den Kapiteln 4, 5 und 6; nicht die Anwendung wird als einfach bezeichnet, sondern die Entscheidung, sie vorzunehmen.
- Die Werkzeuge einer Disziplin begrenzen, was sie entdecken kann; Verbesserungen dieser Werkzeuge öffnen den Weg zu mehr Wissen, so wie das frühe Teleskop die zehnfache Auflösung des bloßen Auges hatte.
