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

# Backtesting


## Kurzdefinition

- Die Backtesting-Station bewertet die Profitabilität einer Anlagestrategie unter verschiedenen Szenarien.
- In der engsten Definition ist ein Backtest eine historische Simulation, wie eine Strategie abgeschnitten hätte, wäre sie über einen vergangenen Zeitraum gelaufen.
- Ein Backtest ist hypothetisch und keineswegs ein Experiment.
- Ein Backtest bewertet out-of-sample die Leistung einer Anlagestrategie anhand vergangener Beobachtungen.
- Diese Beobachtungen lassen sich eng nutzen, um die historische Leistung zu simulieren, als wäre die Strategie damals gelaufen, oder weiter, um Szenarien zu simulieren, die so nicht eingetreten sind.
- Der enge Weg, auch Walk-Forward genannt, ist so verbreitet, dass der Begriff Backtest faktisch zum Synonym für historische Simulation geworden ist.
- Backtesting durch Cross-Validation prüft eine Strategie auf mehreren Trainings- und Testaufteilungen und setzt die Prognosen zu ganzen Pfaden zusammen.
- Ein anderes Backtesting erzeugt aus der Historie einen synthetischen Datensatz mit den statistischen Eigenschaften, die an den beobachteten Daten geschätzt wurden.
- Backtest-Statistiken sind Kennzahlen, mit denen Anleger Strategien beurteilen und vergleichen.

## Kernaussagen

- Teil 3 erklärt, wie eine Entdeckung gebacktestet und die Wahrscheinlichkeit bewertet wird, dass sie falsch ist.
- Ein geprüftes Szenario ist, wie die Strategie abschnitte, wenn die Historie sich wiederholt.
- Der historische Pfad ist nur ein mögliches Ergebnis eines stochastischen Prozesses und nicht zwingend der wahrscheinlichste künftige Verlauf.
- Es gibt drei Backtesting-Paradigmen, von denen die historische Simulation nur eines ist.
- Jeder Backtest ist immer in gewissem Maße überangepasst.
- Das Ausmaß dieser Überanpassung muss quantifiziert werden.
- Ein guter Backtester bezieht ein, wie die Strategie zustande kam.
- Die Wahrscheinlichkeit von Backtest-Overfitting ist anhand der Zahl der Versuche zu bewerten, die zum Herausdestillieren der Strategie nötig waren.
- Die Ergebnisse dieser Bewertung werden von anderen Stationen nicht weiterverwendet.
- Backtest-Ergebnisse werden dem Management mitgeteilt und nicht an andere weitergegeben.
- Walk-forward-Backtesting auf historischen Daten ist eine Falle, und die genannte Lösung ist combinatorial purged cross-validation in den Kapiteln 11 und 12.
- Forschung durch Backtesting ist eine Falle, und die genannte Lösung ist die Analyse der Feature Importance in Kapitel 8.
- Backtest-Overfitting wird mit Backtests auf synthetischen Daten und der deflated Sharpe Ratio begegnet, verortet in den Kapiteln 10 bis 16.
- Backtest-Overfitting ist das wichtigste offene Problem der mathematischen Finanzwelt und das Gegenstück zu P versus NP.
- Ein präzises Verfahren zur Verhinderung würde es erlauben, Backtests zur Bank zu tragen: Ein Backtest wäre fast so gut wie Bargeld und kein bloßes Verkaufsargument.
- Dann würden Hedgefonds Managern vertrauensvoll Kapital zuweisen, Anleger weniger Risiko eingehen und höhere Gebühren zahlen, und Aufsichten Lizenzen nach belastbarer Evidenz von Können vergeben.
- Ein Backtest mit annualisiertem Sharpe Ratio über 2 bei 95 Prozent Konfidenz bleibt laut Übung wahrscheinlich eine falsche Entdeckung, selbst wenn er auf demselben Datensatz unabhängig reproduziert wird.
- Falsch zeitlich zugeordnete Fundamentaldaten werden bei den Backtesting-Fehlern in Kapitel 11 wieder aufgegriffen.
- Marcos’ erstes Gesetz des Backtestings sagt, dass Backtesting kein Forschungswerkzeug ist und Feature Importance es ist.
- Eine Feature-Importance-Analyse muss erfolgen, bevor irgendein Backtest durchgeführt wird.
- Wie man korrekt backtestet, ist nicht Gegenstand von Kapitel 8 und wird in den Kapiteln 11 bis 15 behandelt.
- Bei k* verbessert sich die Performance nicht weiter, und das zeigt an, dass der Backtest nicht von Leaks profitiert.
- Backtesting gehört zu den wichtigsten und am wenigsten verstandenen Techniken im quantitativen Arsenal.
- Ein verbreitetes Missverständnis ist, den Backtest als Forschungswerkzeug zu behandeln.
- Forschen und Backtesten gleicht Trinken und Fahren; man soll nicht unter dem Einfluss eines Backtests forschen.
- Marcos’ zweites Gesetz des Backtestings sagt, dass Backtesting während der Forschung wie Trinken und Fahren ist und man nicht unter dem Einfluss eines Backtests forschen soll.
- Ein Backtest beweist nichts und garantiert nichts, nicht einmal dieselbe Sharpe Ratio, könnte man in der Zeit zurückreisen, nach Bailey und López de Prado 2012.
- Die Zufallsziehungen wären anders gewesen, und die Vergangenheit würde sich nicht wiederholen.
- Der Sinn eines Backtests ist eine Plausibilitätsprüfung unter anderem von Einsatzgröße, Turnover, Kostentragfähigkeit und Verhalten in einem gegebenen Szenario.
- Ein guter Backtest kann äußerst hilfreich sein, aber sauberes Backtesten ist äußerst schwer.
- Die meisten in Zeitschriften veröffentlichten Backtests sind fehlerhaft, als Folge von Selection Bias bei mehrfachen Tests, nach Bailey, Borwein, López de Prado und Zhu 2014 sowie Harvey et al. 2016.
- Selbst ein fehlerfreier Backtest ist wahrscheinlich falsch, weil nur eine Fachperson ihn erzeugen kann und Fachwissen bedeutet, über die Jahre Zehntausende von Backtests gefahren zu haben.
- Dann ist dies nicht der erste Backtest auf dem Datensatz, und es bleibt möglich, dass das Ergebnis eine falsche Entdeckung ist, ein statistischer Zufallstreffer nach vielen Tests.
- Je besser man im Backtesten wird, desto wahrscheinlicher tauchen falsche Entdeckungen auf.
- Anfänger tappen in die sieben Sünden von Luo et al. 2014; Profis können fehlerfreie Backtests liefern und dennoch an Multiple Testing, Selection Bias oder Backtest-Overfitting scheitern, nach Bailey und López de Prado 2014b.
- Feature Importance ist ein echtes Forschungswerkzeug, weil sie ex ante abgeleitet wird, bevor die historische Leistung simuliert wird.
- Ein Backtest liefert sehr wenig Einsicht, warum eine bestimmte Strategie Geld verdient hätte.
- Der Zweck eines Backtests ist, schlechte Modelle zu verwerfen, nicht sie zu verbessern.
- Das Modell anhand der Backtest-Ergebnisse anzupassen, ist Zeitverschwendung und gefährlich.
- Es soll nicht backgetestet werden, bevor das Modell vollständig spezifiziert ist; scheitert der Backtest, beginnt man von vorn.
- Wer so vorgeht, senkt die Chance einer falschen Entdeckung deutlich, sie wird aber nicht null.
- Wie man Backtest-Overfitting begegnet, ist wohl die grundlegendste Frage der quantitativen Finanzwelt.
- Gäbe es darauf eine leichte Antwort, würden Investmentfirmen mit Sicherheit hohe Leistung erzielen, weil sie nur in gewinnende Backtests investieren würden, und Zeitschriften könnten sicher beurteilen, ob eine Strategie ein falsch positives Ergebnis ist.
- Es gibt keinen leichten Weg, Overfitting zu verhindern; eine Reihe von Schritten kann seine Präsenz mindern.
- Bailey et al. 2017a schätzen die Probability of Backtest Overfitting über die combinatorially symmetric cross-validation.
- Aus jedem Pfad lässt sich eine Sharpe Ratio berechnen, sodass eine empirische Verteilung der Sharpe Ratio entsteht.
- Walk-Forward und gewöhnliche Cross-Validation liefern jeweils eine einzige Sharpe Ratio.
- Die synthetischen Testmengen sind ungesehen und senken die Wahrscheinlichkeit, dass die Strategie an eine bestimmte Menge von Datenpunkten angepasst wurde.
- Die optimalen Parameter einer Handelsregel werden aus dem stochastischen Prozess abgeleitet, der den beobachteten Renditestrom erzeugt.
- Die gesamte historische Stichprobe dient dazu, den Prozess zu charakterisieren, aus dem die Parameter der Handelsregel folgen.
- Die Darstellung des synthetischen Backtests beschränkt sich auf Handelsregeln.
- Drei Backtest-Paradigmen werden unterschieden: historische Simulation per Walk-Forward, Szenariosimulation per Cross-Validation und kombinatorischer purged Cross-Validation sowie Simulation auf synthetischen Daten.
- Unabhängig vom Paradigma sind die Ergebnisse mit Kennzahlen zu berichten, anhand derer Investoren die Strategie mit Wettbewerbern vergleichen.
- Die Kennzahlen sollen problematische Eigenschaften sichtbar machen, darunter stark asymmetrische Risiken und geringe Kapazität.
- Backtest-Statistiken gliedern sich in allgemeine Merkmale, Performance, Runs und Drawdowns, Implementation Shortfall, Rendite-Risiko-Effizienz, Klassifikationsmaße und Attribution.
- Ein Teil der Kennzahlen steht in den GIPS, und eine vollständige Beurteilung von Machine-Learning-Strategien braucht zusätzlich eigene Maße.
- Der Testzeitraum soll lang genug sein, um eine umfassende Zahl von Marktregimen zu enthalten.
- Das durchschnittliche verwaltete Vermögen zählt den Dollarwert von Long- und von Short-Positionen jeweils als positive Zahl.
- Die Kapazität ist das höchste verwaltete Vermögen, das noch die angestrebte risikoadjustierte Performance liefert.
- Eine maximale Dollarposition nahe dem durchschnittlichen Vermögen zeigt eine Strategie, die wenig von extremen Ereignissen abhängt.
- Bei marktneutralen Long-Short-Strategien liegt der Anteil der Long-Wetten idealerweise nahe bei 0,5.
- Die Wettfrequenz ist die Zahl der Wetten pro Jahr.
- Aufeinanderfolgende Positionen auf derselben Seite bilden eine Wette, und die Wette endet, wenn die Position glattgestellt oder auf die Gegenseite gedreht wird.
- Die Zahl der Wetten ist immer kleiner als die Zahl der Trades.
- Eine Zählung der Trades würde die Zahl der entdeckten unabhängigen Gelegenheiten überschätzen.
- Der annualisierte Umschlag ist das durchschnittlich pro Jahr gehandelte Dollarvolumen geteilt durch das durchschnittliche Jahresvermögen.
- Hoher Umschlag kann bei wenigen Wetten entstehen, wenn die Position laufend nachjustiert wird.
- Hoher Umschlag kann bei wenigen Trades entstehen, wenn jeder Trade von maximal long auf maximal short dreht.
- Der gesamte PnL ist der über den ganzen Backtest erzeugte Betrag einschließlich der Liquidationskosten der Endposition.
- Der PnL aus Long-Positionen ist der nur von Long-Positionen erzeugte Teil und dient der Beurteilung einer Verzerrung marktneutraler Strategien.
- Jedes Backtestergebnis muss zusammen mit allen Versuchen berichtet werden, die zu seiner Erstellung geführt haben.
- Ohne die Angabe aller beteiligten Versuche lässt sich die Wahrscheinlichkeit einer Fehlentdeckung nicht beurteilen.
- Die Überschrift des dritten Gesetzes des Backtesting lautet, dass die meisten Entdeckungen in der Finanzwelt falsch sind, weil die Versuche nicht mitberichtet werden.
- Zur Auswertung der Runs werden der Konzentrationsindex der negativen Renditen, der Konzentrationsindex der Wetten je Monat sowie das 95-Prozent-Perzentil von Drawdown und Time under Water berichtet.
- Strategierisiko ist das Risiko, dass die Anlagestrategie über die Zeit keinen Erfolg hat.
- Ob die Strategie über die Zeit Erfolg hat, ist die Frage der Anlageleitung.
- Das von der Risikosteuerung ausgewiesene Risiko der gehaltenen Positionen beantwortet nicht, ob die Strategie ihr Ziel über die Zeit verfehlt.
- Das Kapitel zum Strategierisiko soll zeigen, welche Kombinationen aus Wettfrequenz, Trefferchance und Auszahlung unwirtschaftlich sind.
- Fallstricke beim Backtesting können dazu führen, dass die Live-Handelsergebnisse erheblich von den Backtests abweichen.
- Dieselbe theoretische Strategie kann je nach den Details der Umsetzung spektakuläre Gewinne oder klägliche Verluste bringen.
- Selbst der korrekteste Backtest sagt die künftigen Erträge einer Strategie nicht voraus, wenn historisch ein Regimewechsel eintritt.
- Behandelt werden Data-Snooping-Bias, Survivorship Bias, primäre gegen konsolidierte Quotes, die Venue-Abhängigkeit von Devisenkursen, die Feinheiten von Leerverkaufsbeschränkungen, die Konstruktion kontinuierlicher Futures-Kontrakte und die Verwendung von Schlusskursen gegen Settlement-Preise.
- Die wichtigste Tugend solcher Plattformen, von industriellen Systemen wie Deltix bis zu Open-Source-Versionen wie TradeLink, ist der leichte Wechsel vom Backtesting in den Live-Handelsmodus.
- In den Beispiel-Backtest-Codes sind keine Transaktionskosten enthalten, obwohl diese für einen aussagekräftigen Backtest entscheidend sind.
- In den Beispielen werden In-Sample-Daten oft zugleich zur Optimierung der Parameter und zur Messung der Performance verwendet, was die Ergebnisse aufbläht.
- Diese vereinfachten Beispiele heißen Prototyp-Strategien. Sie sind nicht zum Handel unverändert gedacht, sondern als Illustration üblicher Techniken und als Anregung, sie weiter zu verfeinern.
- MATLAB ist für Backtesting und automatisierte Ausführung nicht mehr der einzige Kandidat. Der Stand der Technik wird für jedes Programmierniveau und für viele verschiedene Budgets gesichtet.
- Das Konzept des Complex Event Processing wird in diesem Zusammenhang eingeführt.
- Selbst eine veröffentlichte Strategie ist unabhängig zu backtesten, auch wenn man dem Autor die angegebene Performance glaubt, weil die Profitabilität empfindlich von der Umsetzung abhängt.
- Veröffentlichte Artikel übergehen oft Details, die eine live gehandelte Strategie erheblich beeinflussen: Orders als Market-on-Open oder als Market Orders kurz nach der Eröffnung, der E-mini S&P 500 kurz vor 16:00 Uhr Aktienschluss oder kurz vor 16:15 Uhr Futures-Schluss, und als Auslöser der Bid, der Ask oder der letzte Preis.
- Idealerweise lässt sich das Backtest-Programm per Knopfdruck in ein automatisiertes Ausführungsprogramm überführen, damit diese Details exakt umgesetzt werden.
- Ein Fallstrick bläht die Backtest-Performance gewöhnlich gegenüber der tatsächlichen vergangenen Performance auf, und das ist besonders gefährlich.
- Wer die Fallstricke übergeht, erhält ein nutzloses oder irreführendes Backtesting, das erhebliche finanzielle Verluste verursachen kann.
- Der Backtest soll der wissenschaftlichen Methode folgen. Ausgang ist eine Hypothese über eine Arbitragemöglichkeit, aus eigener Marktintuition oder veröffentlichter Forschung. Der Backtest bestätigt oder widerlegt sie. Reicht das Ergebnis nicht, wird die Hypothese geändert und der Vorgang wiederholt.
- Der Backtest einer veröffentlichten Strategie erlaubt einen echten Out-of-Sample-Test in der Zeit nach der Veröffentlichung. Echter Out-of-Sample-Test beginnt erst, wenn die Strategie veröffentlicht und festgeschrieben ist, weil Autoren bei schlechten Ergebnissen sonst Parameter ändern oder das Modell noch an die vermeintlichen Out-of-Sample-Daten anpassen können.
- Selbst ein korrekter Backtest mit hoher statistischer Signifikanz sagt künftige Renditen nicht notwendig voraus. Regimewechsel können alles verderben.
- Backtesting berechnet typischerweise eine erwartete Rendite und andere statistische Performancemaße. Deren Signifikanz wird mit Hypothesentests und Monte-Carlo-Simulationen geschätzt. Je mehr Round-Trip-Trades der Backtest enthält, desto höher ist im Allgemeinen die statistische Signifikanz.
- Backtesting ist nutzlos, wenn es die künftige Performance einer Strategie nicht vorhersagt, und Fallstricke im Backtesting senken seine Vorhersagekraft.
- Selbst ohne die üblichen Fallstricke und bei genug Trades für statistische Signifikanz ruht die Vorhersagekraft auf der Annahme, dass die statistischen Eigenschaften der Preisreihe unverändert bleiben, sodass früher profitable Regeln auch künftig profitabel sind.
- Diese Annahme wird oft ungültig: Die Wirtschaftsaussicht eines Landes ändert sich, das Management eines Unternehmens ändert sich, und die Struktur eines Finanzmarkts ändert sich.
- Strategien, die vor einem solchen Regimewechsel hervorragend abschnitten, können danach aufhören zu funktionieren, und umgekehrt. Backtests auf Daten vor dem Wechsel können ziemlich wertlos sein. Backtests auf jüngeren Daten sagen künftige Gewinne nicht besser voraus, wenn ein weiterer Regimewechsel kommt.
- Ob ein Backtest prädiktiv ist und prädiktiv bleibt, hängt auch vom Bewusstsein für fundamentale Markt- und Wirtschaftsfragen ab.
- Das Leben ist zu kurz, um jede gelesene Strategie zu backtesten. Die Kenntnis der üblichen Fallstricke hilft bei der Auswahl.
- Die vorbereitenden Stationaritätstests und die Halbwertszeit haben gewöhnlich höhere statistische Signifikanz als ein direkter Backtest der Handelsstrategie.
- ADF-Test, Variance-Ratio-Test und Halbwertszeit verwenden den Preis jeder Bar, während ein Backtest in der Regel deutlich weniger Round-Trips für die Performancestatistik liefert.
- Das Ergebnis eines Backtests hängt von der konkreten Handelsstrategie und von einem konkreten Parametersatz ab.
- Hat eine Preisreihe den Stationaritätstest bestanden oder ist ihre Halbwertszeit kurz genug, lässt sich schließlich eine profitable Strategie finden, möglicherweise eine andere als die gebacktestete.
- Der Backtest der parameterfreien linearen Strategie zeigt, dass sich Gewinne ohne Data-Snooping-Bias ziehen lassen, weil es keine zu optimierenden Parameter gibt.
- Auch der Lookback ist keine freie Strategiegröße, sondern gleich der Halbwertszeit, die von der Preisreihe selbst abhängt.
- Weil die Strategie fortlaufend ein- und aussteigt, hat sie voraussichtlich mehr statistische Signifikanz als Strategien mit komplizierten und selektiven Ein- und Ausstiegsregeln.
- Der Kelly-Hebel aus dem Backtest oder einem kurzen Walk-forward-Test ist oft so hoch, dass er den vom Broker erlaubten Höchsthebel weit übersteigt.
- Manchmal hätte derselbe Hebel schon im Backtest zum Bankrott geführt, weil die Renditen nicht gaußisch sind und der maximale Drawdown dann minus 1 ist.
- Alternativ lässt sich der Hebel direkt an den empirischen historischen Renditen optimieren.
- Leser werden aufgefordert, die Strategien des Buches out of sample zu testen.
- Weicht der Live-Handel vom Backtest ab, liegt das oft nicht an Fallstricken beim Backtesten, sondern an einem grundlegenden Wandel der Marktstruktur.
- Dieser Wandel ist ein Regime Shift durch staatliche Regulierung oder makroökonomische Änderungen.
- Der Prozess, einen fundamentalen Grund zu suchen und quantitativ zu testen, hilft besonders, wenn eine Strategie den Backtest underperformt, statt blind weitere Regeln und Indikatoren zu ergänzen.

## Funktionsweise

- Alternative Szenarien sind im Einklang mit den bekannten Stärken und Schwächen der vorgeschlagenen Strategie zu prüfen.
- Seriöse Datenanbieter bauen die von der Börse gelieferten Cancel-and-Correct-Codes ein, um Trades zu korrigieren, die wegen Transaktionspreisen zu weit vom Normalen storniert wurden; was ein normaler Preis ist, bestimmt allein die zuständige Börse, manchmal von Fall zu Fall.
- Thomas Falkenberry hat 2002 ausführlicher über Data Cleansing geschrieben.
- Spot- und Roll-Rendite werden per linearer Regression geschätzt: der Log des Spots gegen die Zeit, und an jedem Tag die Logpreise der fünf nächsten Kontrakte gegen die Restlaufzeit in Monaten, sofern fünf aufeinanderfolgende Kontrakte existieren.
- Trotz der Annahme konstanter Roll-Rendite hängt der Regressionskoeffizient vom gewählten Zeitpunkt und von den dann verfügbaren Kontrakten ab, sodass das geschätzte γ langsam variiert.
- Die Regressionskoeffizienten für ES gegen VX werden nur für die ersten 500 Tage der Daten nach August 2008 als Trainingsset geschätzt, weil die Statistiken daraus später das Handelsmodell speisen.

## Voraussetzungen

- Die Station braucht Data Scientists mit tiefem Verständnis empirischer und experimenteller Techniken.

## Anwendung im Trading

- Im Embargo läuft die Strategie auf Daten, die nach dem Enddatum des Backtests beobachtet wurden.
- Diese Periode kann von den Backtestern reserviert worden sein oder aus Implementierungsverzögerungen stammen.
- Passt die Embargo-Performance zum Backtest, wird die Strategie in die nächste Stufe befördert.
- Es gibt zwei Grundentscheidungen: eine Spezialplattform für Backtest und Ausführung kaufen und die Strategie in deren Oberfläche oder Sprache bauen, oder das eigene Programm in einer allgemeinen Sprache wie C++ schreiben, allein oder in einer integrierten Entwicklungsumgebung mit Bibliothek für den algorithmischen Handel.
- Eine Plattform, die dasselbe Programm für Backtest und Live-Ausführung nutzt, beseitigt Übertragungsfehler zwischen beiden und Look-ahead Bias, weil historische Daten Tick für Tick oder Bar für Bar eingespeist werden, so wie Live-Daten. Dieselbe Identität ermöglicht theoretisch tickbasierte Hochfrequenz-Backtests, sofern die Hardware stark genug ist.
- Die meisten Plattformen können die Ausführung von Hochfrequenzhandel verkraften, wenn die Strategie Latenzen von 1 bis 10 Millisekunden verträgt. Der Engpass ist meist die Latenz der Live-Daten oder der Orderbestätigung, nicht die Software, außer bei Excel mit VB-Makro oder wenn ein Programm Tausende Symbole überwacht.
- Das Backtesting von Hochfrequenzhandel ist etwas anderes. Viele Monate Tick-Daten, manchmal Level-2-Quotes, überfordern den Speicher, wenn sie nicht besonders behandelt werden. Die meisten Spezialplattformen können Bid, Ask und Last mit Größen oder Level 2 nicht backtesten. Gewöhnlich ist ein eigenes Programm nötig, und wegen der Heisenbergschen Unschärfe sagt der Backtest über die Live-Profitabilität oft wenig.

## Regeln und Kriterien

- Überlappende Trainingsbeobachtungen müssen gepurgt und mit einem Embargo versehen werden, sobald ein Trainings- und Test-Split entsteht, sei es für Hyperparameter-Anpassung, Backtesting oder Performance-Evaluation.
- Modelle sollen für ganze Anlageklassen oder Anlageuniversen entwickelt werden, nicht für einzelne Titel, denn Anleger diversifizieren und begehen einen Fehler nicht nur bei einem einzelnen Wert.
- Findet man einen Fehler nur bei einem einzelnen Titel, ist das wahrscheinlich eine falsche Entdeckung, wie profitabel er auch scheinen mag.
- Bagging soll Overfitting vorbeugen und die Varianz des Prognosefehlers senken; verschlechtert Bagging die Leistung einer Strategie, war sie wahrscheinlich auf wenige Beobachtungen oder Ausreißer überfittet.
- Es soll nicht backgetestet werden, bevor die gesamte Forschung der Kapitel 1 bis 10 abgeschlossen ist.
- Jeder auf einem Datensatz durchgeführte Backtest ist festzuhalten, damit die Probability of Backtest Overfitting des schließlich gewählten Ergebnisses geschätzt und die Sharpe Ratio um die Zahl der Versuche deflationiert werden kann.
- Es sollen Szenarien statt der Geschichte simuliert werden, denn ein gewöhnlicher Backtest ist eine historische Simulation und leicht zu überfitten.
- Die Geschichte ist nur der realisierte Zufallspfad und hätte völlig anders verlaufen können; die Strategie soll unter vielen Szenarien tragfähig sein, nicht nur auf dem anekdotischen historischen Pfad.
- Tausende Was-wäre-wenn-Szenarien zu überfitten ist schwerer als einen historischen Pfad zu überfitten.
- Findet der Backtest keine profitable Strategie, wird von vorn begonnen, und die Versuchung, diese Ergebnisse wiederzuverwenden, ist zu unterlassen.
- Eine Strategie, deren Wahrscheinlichkeit das Sharpe-Ziel zu verfehlen über 0,05 liegt, gilt typischerweise als zu riskant.
- Das gilt auch für Strategien in Instrumenten mit niedriger Volatilität und auch dann, wenn der Geldverlust klein bleibt.
- Für einen Einsatz muss der Entwickler die kritische Trefferwahrscheinlichkeit senken.
- Bei einem N-zu-1-Split wird der Kurs durch N geteilt, der Gesamtwert bleibt gleich, weil der Bestand auf das N-fache steigt. Ohne Teilung der historischen Preise vor dem Ex-Tag durch N entsteht ein scheinbarer Kurseinbruch und Fehlersignale, im Backtest wie live unmittelbar vor der Eröffnung am Ex-Tag. Bei einem Reverse-Split 1-zu-N werden die historischen Preise vor dem Ex-Tag mit N multipliziert.
- Eine Barausschüttung von d Dollar je Aktie, in bar oder in Aktien, senkt den Kurs um d, wenn keine anderen Marktbewegungen dazukommen, weil der Gesamtwert gleich bleibt. Ohne Rückanpassung der Historie vor dem Ex-Tag kann der Sprung ein Fehlersignal auslösen. Dieselbe Anpassung gilt live vor der Eröffnung am Ex-Tag, für Aktien und für ETFs. Bei Optionen ist sie etwas komplizierter.
- Der Front Month hängt vom Rollover ab. Manche rollen zehn Tage vor Verfall des aktuellen Frontkontrakts, andere beim Open-Interest-Crossover, wenn das Open Interest des nächsten Kontrakts das des aktuellen übersteigt. Kauf und Verkauf des Rollovers sind von der Strategie unabhängig und sollen nur minimal zusätzlichen Gewinn oder Verlust bringen. Der Roll-Return wirkt dagegen jeden Tag auf jeden Kontrakt und ist nicht die Folge des Herüberrollens.
- Der von Datenanbietern gelieferte Futures-Tagesschluss ist gewöhnlich der Settlement-Preis, nicht der letzte Handelspreis. Ein Settlement wird börsentäglich festgesetzt, auch ohne jeden Handel, und weicht im Allgemeinen vom letzten Trade ab. Meist soll der Settlement-Preis verwendet werden, weil er bei einem Live-Geschäft nahe am Close dem Ausführungskurs am nächsten kommt. Der letzte Trade kann Stunden früher liegen.
- entryZscore ist ein freier Parameter, der auf einem Trainingsset optimiert wird; der Lookback kann ebenfalls optimiert oder gleich der Halbwertszeit gesetzt werden.
- Das optimale δ des Kalman-Filters wird wie der optimale Lookback einer gleitenden Regression aus Trainingsdaten bestimmt.
- Beim Test eines Preisspreads müssen die fortlaufenden Kontrakte mit Preisen und nicht mit Renditen rückadjustiert werden, sonst springt der Preisspread an den Rolls.
- Wer Intermarket-Spreads selbst testet, muss synchrone Preise sicherstellen.
- Ein Backtest des BZ-CL-Spreads mit Schlusskursen vor dem 5. September 2001 wäre falsch, weil BZ vorher an der Intercontinental Petroleum Exchange in London gehandelt wurde und NYMEX, wo CL durchgängig gehandelt wurde, eine andere Schlusszeit hat.
- Futures-Preise müssen oft mit einem Faktor multipliziert werden, der Punkte in US-Dollar umrechnet.
- Bei einem Portfolio aus zwei Währungs-Cross-Rates ist zu beachten, ob sie dieselbe Notierungswährung, dieselbe Basiswährung oder keine von beiden teilen, denn die Formeln für die Renditen sind nicht in allen Fällen dieselben.
- Eine lineare Regression oder ein Johansen-Test auf einer Mischung der beiden ES-VX-Regime wäre ein Fehler.
- Korrelationen zwischen Lookback- und Haltedauer-Renditen dürfen nur auf nicht überlappenden Paaren gerechnet werden.
- Ist der Lookback länger als die Haltedauer, wird im Text um die Haltedauer vorgerückt; ist die Haltedauer länger als der Lookback, wird um den Lookback vorgerückt.
- Im abgedruckten Code wird bei einem Lookback größer oder gleich der Haltedauer in Schritten des Lookbacks vorgerückt und sonst in Schritten der Haltedauer.
- Ein Vorrollen der Daten um einen Tag ergibt ein etwas anderes Renditeset; wegen der großen Überlappung dürften die Korrelationen nicht stark abweichen, und getestet wurde nur eines von vielen möglichen Sets.
- Für den Backtest der Drift nach Gewinnmeldungen werden nur Meldungen verwendet, die nach 16:00 Uhr ET des vorigen Handelstags und vor 9:30 Uhr ET der aktuellen Eröffnung liegen.
- Meldungen zu anderen Zeiten dürfen den Einstieg zur heutigen Eröffnung nicht auslösen.
- Ob die Meldung überraschend genug ist, wird an der 90-Tage-Standardabweichung der Rendite vom vorigen Schluss zum nächsten Open gemessen.
- Long gilt bei einer Close-to-Open-Rendite von mindestens einer halben dieser Standardabweichung und passender Meldung, Short bei höchstens minus einer halben.
- Ein Stop-Loss größer als der maximale Intraday-Drawdown des Backtests wäre im Backtest nie ausgelöst worden, lässt die Backtest-Performance unverändert und kann ein künftiges Black-Swan-Ereignis vor dem Ruin bewahren.
- Ein Kompromiss kann ein Hebel zwischen der simulierten und der historischen Drawdown-Schätzung sein.
- Hat das Modell frühere Stressperioden im Backtest überstanden, sieht der Autor keinen Grund, den Hebel vor einer kommenden Krise zu senken.
- Hat das Modell frühere Stressperioden im Backtest überstanden, gibt es nach der Erfahrung des Autors keinen Grund, den Hebel vor einer kommenden Krise zu senken.
- Besser ist, in guten Zeiten mit konservativerem Hebel zu starten, als ihn in schlechten senken zu müssen.

## Risiken und Grenzen

- Im Sisyphus-Paradigma bleibt die Suche oft bei einem falsch positiven Befund, der in einem überangepassten Backtest gut aussieht.
- Ist Backtest-Overfitting schon in der ökonometrischen Analyse ein Problem, macht die Flexibilität von ML es zu einer ständigen Bedrohung.
- In der Finanzwelt gilt das besonders, weil die Datensätze kürzer sind, das Signal-Rausch-Verhältnis niedriger ist und Labore fehlen, in denen alle Umgebungsvariablen kontrolliert werden.
- Die empirischen Stützen von CAPM, APT, Asset-Allocation-Verfahren und Risikomanagement wurden ausgewählt, ohne die Wahrscheinlichkeiten falscher Entdeckungen zu bestimmen.
- Ein verbreiteter Fehler ist, Daten durch einen ML-Algorithmus zu schicken, die Vorhersagen zu backtesten und die Abfolge zu wiederholen, bis ein gut aussehendes Backtest erscheint; Fachzeitschriften sind voll von solchen Scheinentdeckungen, und auch große Hedgefonds tappen in diese Falle.
- Es spielt keine Rolle, ob der Backtest ein Walk-Forward-Out-of-Sample ist: Wiederholtes Testen derselben Daten führt wahrscheinlich zu einer falschen Entdeckung.
- Statistiker betrachten diesen methodischen Fehler als wissenschaftlichen Betrug, und die American Statistical Association warnt in ihren Ethical Guidelines von 2016, Discussion #4, davor.
- Beim üblichen Signifikanzniveau von 5 % False-Positive-Rate genügen typischerweise etwa 20 solcher Iterationen, um eine falsche Investmentstrategie zu entdecken.
- Viele erfahrene Portfoliomanager, auch mit quantitativem Hintergrund, erkennen nicht, wie leicht sich ein Backtest überfitten lässt.
- Luo, Alvarez, Wang, Jussa, Wang und Rohal 2014 nennen in „Seven Sins of Quantitative Investing“ die üblichen Verdächtigen, und die meisten in Zeitschriften veröffentlichten Arbeiten begehen solche Grundfehler routinemäßig.
- Survivorship Bias heißt, das heutige Anlageuniversum zu verwenden und damit zu ignorieren, dass Unternehmen pleitegingen und Titel auf dem Weg delisted wurden.
- Look-ahead Bias heißt, Information zu nutzen, die im Zeitpunkt der simulierten Entscheidung nicht öffentlich war; Zeitstempel, Veröffentlichungsdaten, Verteilungsverzögerungen und Backfill-Korrekturen sind zu beachten.
- Storytelling heißt, im Nachhinein eine Geschichte zu erfinden, die ein Zufallsmuster rechtfertigt.
- Data Mining und Data Snooping heißen in dieser Liste, das Modell auf dem Testset zu trainieren.
- Transaktionskosten sind schwer zu simulieren, weil sich diese Kosten nur sicher feststellen ließen, wenn man mit dem Orderbuch interagiert und den Handel tatsächlich ausgeführt hätte.
- Ein weiterer Fehler ist, eine Strategie auf wenige extreme Ausgänge zu stützen, die sich so, wie in der Vergangenheit beobachtet, nie wieder ereignen müssen.
- Eine Short-Position in Kassaprodukten verlangt einen Verleiher; Leihekosten und verfügbare Menge sind in der Regel unbekannt und hängen von Beziehungen, Bestand und relativer Nachfrage ab.
- Weitere häufige Fehler sind eine nicht standardisierte Performancerechnung, das Ignorieren versteckter Risiken, der Blick nur auf Returns, die Verwechslung von Korrelation und Kausalität, ein unrepräsentativer Zeitraum, das Versäumnis, das Unerwartete zu erwarten, das Ignorieren von Stop-out-Limits oder Margin Calls, das Ignorieren von Funding-Kosten und das Vergessen praktischer Aspekte, nach Sarfati 2015.
- Es gibt stets eine Ex-post-Geschichte, Luos dritte Sünde, so wie sich ein Lottogewinner einreden kann, er habe seinen Glücksfall verdient.
- Autoren, die Hunderte von Alphas und Faktoren gefunden haben, haben die Lotterielose gefunden, die das letzte Spiel gewonnen haben; die Nummern sind für die nächste Runde nutzlos, und sie berichten nicht die Millionen Simulationen, die dafür nötig waren.
- Die aus dem Prozess abgeleitete Handelsregel fällt als zusätzliche Quelle von Overfitting weg, während die übrige Strategie weiterhin aus einem überangepassten Backtest stammen kann.
- Unterhalb eines Mindestvermögens fehlen passende Einsatzgröße und Risikostreuung, und darüber fällt die Performance durch höhere Transaktionskosten und geringeren Umschlag.
- Ein Long-Anteil marktneutraler Strategien fern von 0,5 kann eine Positionsverzerrung anzeigen oder einen kurzen Testzeitraum, der künftige Marktverhältnisse schlecht trifft.
- Strategien mit Market-on-Open- oder Market-on-Close-Orders brauchen die Kurse der Primärbörse. Der konsolidierte Tagesschluss ist der letzte Ausführungskurs auf irgendeinem Platz während der regulären Handelszeit, die Eröffnung der erste. Die Order geht nur an die Primärbörse: IBM an die NYSE, SPY an NYSE Arca, MSFT an die Nasdaq. Konsolidierte Preise blähen besonders den Backtest eines mean-revertierenden Modells auf, weil wenige Stücke abseits der Primärbörse zu einem Preis fern vom Auktionspreis ausgeführt werden können und die Transaktionspreise des Folgetags von diesem schwer erreichbaren Ausreißer gewöhnlich zurücklaufen. Schluss und Eröffnung an den US-Primärbörsen entstehen immer durch eine Auktion, ein Geschäft am Schluss einer Zweitbörse nicht.
- Historische Hoch- und Tiefkurse sind meist die konsolidierten, oft übertriebene Werte aus kleinen Geschäften an Zweitbörsen. Werden sie verwendet, bläht sich der Backtest ebenfalls auf. Primärbörsenkurse haben Bloomberg-Nutzer im Abo. Direkte Live-Feeds lassen sich selbst speichern. Unabhängig sind sie teuer, über einen institutionellen Broker wie Lime Brokerage bei Colocation im eigenen Rechenzentrum oft günstiger. Die meisten Retail-Broker geben direkte Börsenfeeds nicht weiter. Ohne solche Daten bleibt eine gesunde Skepsis gegenüber den Backtest-Ergebnissen.
- Ein Devisen-Backtest ist nur realistisch, wenn die historischen Daten von denselben Venues stammen, an denen gehandelt werden soll. Keine Regel verlangt, dass ein Geschäft an einem Platz zum besten Bid oder Ask über alle Plätze erfolgt. Aggregatoren wie Streambase führen Feeds in einem Orderbuch zusammen. Die konsolidierte Historie ist dann brauchbar, sofern an einem der beteiligten Plätze ausgeführt werden kann. Handelspreise und Größen sind bei Devisen im Gegensatz zu Bid- und Ask-Quotes im Allgemeinen nicht verfügbar, zumindest nicht ohne kleine Verzögerung, weil kein Händler oder ECN sie allen Teilnehmern melden muss. Viele Händler behandeln sie als proprietär.
- Leerverkaufsbeschränkungen blähen den Backtest auf, wenn das Modell Aktien leerverkauft, die schwer oder gar nicht zu leihen waren, weil niemand sonst den Kurs durch Leerverkäufe drücken konnte. Der Broker muss Stücke bei anderen Kunden oder Instituten lokalisieren, typischerweise Fonds mit großen Long-Beständen, und ein Aktienleihegeschäft schließen. Hard to borrow kann heißen, dass der Leerverkäufer dem Verleiher Zinsen zahlt, statt wie im Normalfall umgekehrt, oder dass die Aktie in der gewünschten Menge oder überhaupt nicht geliehen werden kann. Nach dem Zusammenbruch von Lehman verbot die SEC für mehrere Monate Leerverkäufe aller Finanzaktien. Small Caps sind viel stärker betroffen als Large Caps, auch ETFs können hard to borrow sein, und der Autor konnte SPY in den Monaten nach Lehman nicht leihen.
- Die ursprüngliche Uptick-Regel galt von 1938 bis 2007. Der Leerverkauf musste über dem letzten Handelspreis erfolgen oder zum letzten Preis, wenn dieser höher war als der Preis des Geschäfts davor. Bei Nasdaq musste der Leerverkaufspreis über dem letzten Bid liegen, nicht über dem letzten Trade. Die Alternative Uptick Rule von 2010 verlangt einen Trade-Preis über dem nationalen Best Bid, aber nur nach einem Circuit Breaker, also wenn die Aktie 10 Prozent unter ihrem vorigen Schluss gehandelt wurde. Der Breaker gilt auch am folgenden Tag und verhindert faktisch, dass Short-Market-Orders ausgeführt werden. Ignoriert der Backtest, ob diese Regeln zum historischen Zeitpunkt galten, ist die Performance aufgebläht.
- Eine unangepasste kontinuierliche Futures-Serie setzt am Rollover-Tag T+1 den Schluss q(T+1) des nächsten Kontrakts neben den Schluss p(T) des alten und liefert den falschen Punkte-P&L q(T+1)−p(T) statt p(T+1)−p(T) und die falsche Rendite (q(T+1)−p(T))/p(T) statt (p(T+1)−p(T))/p(T). Die Preisrückanpassung addiert q(T+1)−p(T+1) zu jedem Preis an jedem Tag bis einschließlich T, und das mehrfach für jeden weiter zurückliegenden Rollover, sodass die Preisänderung von T auf T+1 gleich p(T+1)−p(T) wird. Die Rendite wird dann (p(T+1)−p(T))/(p(T)+q(T+1)−p(T+1)). Die Renditerückanpassung multipliziert jeden Preis bis T mit q(T+1)/p(T+1) und macht dann den P&L falsch. Beides zugleich stimmt nur, wenn die einzelnen Kontrakte samt Rollover selbst gebacktestet werden.
- Die Preisrückanpassung kann weit in der Vergangenheit negative Preise erzeugen. Das kann die Strategie stören und macht die Renditerechnung jedenfalls problematisch. Ein übliches Gegenmittel ist, zu allen Preisen eine Konstante zu addieren, sodass keiner negativ ist. Signale aus der Preisdifferenz zweier Kontrakte verlangen die Preisrückanpassung, Signale aus dem Preisverhältnis die Renditerückanpassung. csidata.com nutzt nur die Preisrückanpassung, optional mit einer additiven Konstante gegen negative Preise. tickdata.com erlaubt die Wahl zwischen Preis- und Renditerückanpassung, aber keine Konstante gegen negative Preise.
- Die Dezimalisierung der US-Aktiennotierungen am 9. April 2001, zuvor Notierung in Achteln oder Sechzehnteln eines Penny, senkte die Bid-Ask-Spreads und die angezeigte Liquidität am besten Bid und Ask, nach Arnuk und Saluzzi 2012. Die Profitabilität vieler Statistical-Arbitrage-Strategien sank, die vieler Hochfrequenzstrategien stieg.
- Die Finanzkrise 2008 löste danach einen Einbruch der durchschnittlichen Tagesumsätze um 50 Prozent aus, nach Durden 2012. Retail-Handel und Besitz von Stammaktien gingen besonders zurück. Die durchschnittliche Volatilität sank, plötzliche Ausbrüche wurden häufiger, darunter der Flash Crash im Mai 2010 und die Herabstufung der US-Bonität im August 2011. Die Gewinne von Mean-Reversion-Strategien, die von einem hohen, aber konstanten Volatilitätsniveau leben, sanken allgemein.
- Dieselbe Krise 2008 leitete einen mehrjährigen Bärenmarkt der Momentum-Strategien ein.
- Die Regulation NMS der SEC, im Juli 2007 umgesetzt, trug zum drastischen Rückgang der durchschnittlichen Trade-Größen und zum Verschwinden des NYSE-Blocktrades bei, nach Arnuk und Saluzzi 2012.
- Die alte Uptick-Regel für Leerverkäufe fiel im Juni 2007, die neue Alternative Uptick Rule kam 2010 zurück.
- Eine Strategie mit 30 Prozent annualisierter Rendite, Sharpe Ratio 0,3 und zwei Jahren maximaler Drawdown-Dauer lohnt den Backtest nicht. Wenige Trader, im Unterschied zu Investoren, ertragen zwei Jahre unter Wasser. Die niedrige Sharpe Ratio zusammen mit der langen Drawdown-Dauer zeigt, dass die Strategie nicht konsistent ist. Die hohe Rendite ist wahrscheinlich Data-Snooping, und die lange Drawdown-Dauer besteht eine Cross-Validation kaum.
- Nicht backtesten sollte man Strategien mit hoher Rendite bei niedriger Sharpe Ratio und solche, deren maximale Drawdown-Dauer länger ist, als man selbst oder die Investoren aushalten.
- Eine Long-only-Strategie ist an der Rendite einer Buy-and-hold-Position zu messen, also an der Information Ratio und nicht an der Sharpe Ratio. Die Rohöl-Strategie von 2007 mit 20 Prozent und Sharpe Ratio 1,5 war dem Front-Month-Buy-and-hold mit 47 Prozent und Sharpe Ratio 1,7 nicht überlegen.
- Ein neuronales Handelsnetz mit etwa 100 Knoten und einer Backtest-Sharpe-Ratio von 6 hat eine Parameterzahl, die proportional zur Knotenzahl ist. Mit mindestens 100 Parametern lässt sich jede Zeitreihe anpassen. Vorwärts hat das Modell wegen Data-Snooping wenig oder keine Vorhersagekraft.
- Ein sogenannter Backtest einer Hochfrequenzstrategie ist sehr skeptisch zu sehen. Die Performance hängt von den Ordertypen, der Ausführungsmethode und der Marktmikrostruktur ab, und selbst mit dem historischen Orderbuch noch von den Reaktionen der anderen Teilnehmer. Das Platzieren oder Ausführen einer Order kann ihr Verhalten ändern, eine Art Heisenbergsche Unschärfe.
- Im Beispiel der linearen Mean-Reversion-Strategie werden wie bei den meisten Beispielstrategien dieses Buchs keine Transaktionskosten einbezogen.
- In diesem Beispiel steckt Look-ahead Bias, weil Halbwertszeit und damit der Lookback an denselben In-Sample-Daten bestimmt werden.
- Weil der Marktwert des Portfolios nicht nach oben begrenzt ist, kann für die ausgewiesene P&L unbegrenzt Kapital nötig sein.
- Der Autor empfiehlt diese lineare Strategie nicht als praktische Handelsstrategie; eine praktischere Fassung steht in Kapitel 5.
- Die einfachste lineare Strategie ist unpraktisch, weil das nötige Höchstkapital im Voraus unbekannt ist und man nicht bei jeder infinitesimalen Preisbewegung infinitesimal viele Stücke handeln kann.
- Die Halbwertszeit des Tripels von 23 Tagen ist deutlich kürzer als die 115 Tage von USD.CAD, deshalb wird erwartet, dass die Mean-Reversion-Strategie hier besser funktioniert.
- In allen Strategie-Backtests dieses Buchs sind keine Transaktionskosten enthalten.
- Mitunter wird Look-ahead Bias eingebaut, indem dieselben Daten für die Parameteroptimierung, etwa die beste Hedge Ratio, und für den Backtest verwendet werden.
- Das sind Fallstricke, vor denen Kapitel 1 warnt; die Rechtfertigung ist nur die einfachere Darstellung und der einfachere Quellcode, und Leser sollen sie in eigenen Backtests dieser Prototypen beseitigen.
- Datenfehler oder Ausreißer in den historischen Daten blähen in der Regel die Backtest-Performance von Mean-Reversion-Strategien auf.
- Dieselbe Art Datenfehler drückt die Backtest-Performance von Momentum-Strategien, sodass der Fehler für diese Strategien weniger gefährlich ist.
- Datenqualität ist bei Intraday-Daten besonders wichtig, weil sie viel mehr Gelegenheiten für solche Fehler bieten.
- Scaling-in muss im Backtest nicht optimal sein, ist im Live-Handel aber oft nützlich, weil Volatilitäten und Wahrscheinlichkeiten sich ändern.
- Die Backtests in diesem Buch enthalten keine Transaktionskosten, weil diese empfindlich von der genauen Ausführungsmethode und vom gewählten Aktienuniversum abhängen.
- Eine weitere Falle der Aktienmodelle ist Survivorship Bias, weil Daten ohne diesen Bias umständlicher und teurer zu beschaffen sind; die Hoffnung ist, dass die Ergebnisse zumindest für das letzte Jahr oder die letzten zwei nicht zu unrealistisch sind.
- Der gewählte Index, typischerweise der S&P 500, ändert seine Zusammensetzung über die Historie; ein korrekter Neu-Backtest braucht eine Datenbank der historischen täglichen Indexzusammensetzungen.
- Die verwendeten historischen Preise sind sämtlich konsolidierte Eröffnungs- und Schlusskurse; wer mit Market-on-Open, Limit-on-Open, Market-on-Close oder Limit-on-Close handelt, wird zum Open oder Close der Primärbörse gefüllt, und die tatsächlichen Renditen liegen dann gewöhnlich unter den berichteten.
- Open-Preise können nicht zugleich das Einstiegssignal bestimmen und die Füllung zum offiziellen Open sein; Preopen-Preise, etwa an ARCA, erzeugen Signalrauschen, und der Backtest konsolidierter gegen Primärbörsenpreise ist eine eigene Falle.
- Ein Backtest einer Aktienpaar-Strategie auf Trade- oder Quote-Preisen ist unrealistisch, außer man handelt nur 100 Stück oder setzt erhebliche Transaktionskosten an; bei AAPL ist eine NBBO-Größe von nur 100 Stück nicht ungewöhnlich.
- Die alternative Uptick-Regel der US-Aktienmärkte seit 2010 erzeugt Unsicherheit in Backtest und Live-Ausführung: ist der Circuit Breaker ausgelöst, sind Short-Market-Orders im Wesentlichen verboten.
- Auch close-to-close lassen sich die Gewichte nicht zum exakten Schlusskurs bestimmen und genau zu diesen Preisen ausführen; Preise wenige Sekunden vor dem Close liegen typischerweise viel näher am offiziellen Primärbörsen-Schluss, weil der Primärmarkt dann offen und liquide ist.
- Beim Test auf Kointegration von Währungen und bei der Rendite eines Währungsportfolios muss eine Punktbewegung in einem Paar denselben Dollarwert haben wie in einem anderen, sonst ergeben die Resultate keinen Sinn.
- Die zentrale Schwierigkeit beim Backtest von Währungsarbitrage ist nicht die Komplexität der Strategien, sondern die richtige Aufbereitung der Reihen für Kointegrationstests und die richtige Renditeformel.
- Die Renditeformeln ohne Rollover-Zinsen sind nicht streng korrekt; bei kurzfristigen Strategien wie dem Beispiel mit 250-Tage-Training ist ihre Wirkung meist nicht groß, bei Strategien mit Overnight-Positionen hängen die Rollover-Regeln aber an der Genauigkeit des Backtests.
- Wird ein angesammelter Gewinn in Basis- und Quotierungswährung nicht regelmäßig in die Heimatwährung gewechselt, kann er den Backtest deutlich verfehlen.
- Roll-Renditen können Strategien verderben, die sich auf den Spot stützen: fehlendes Verständnis, dass ein Produzenten-ETF mit dem Spot kointegrieren kann und mit dem Future trotzdem nicht, kostete den Autor mehr als 100.000 Dollar und ruinierte sein erstes Jahr 2006 als unabhängiger Händler.
- Der VIX ist mean-reverting, die back-adjustierten Front-Month-Preise von VX laut ADF aber definitiv nicht; der Unterschied ist vollständig die Roll-Rendite.
- Wegen der langen Haltedauern enthält die begrenzte Testhistorie wenige Trades, sodass in diesen Momentum-Ergebnissen ein Data-Snooping-Bias droht; der eigentliche Test ist echtes Out-of-Sample-Testing.
- Die Schlusskurse von GC werden um 13:30 Uhr ET erfasst, die von GLD um 16:00 Uhr ET; in diesem Backtest ist die Asynchronität folgenlos, weil die Signale allein aus den GC-Schlusskursen kommen.
- XLE und CL haben verschiedene Schlusszeiten, deshalb wird die Arbitrage leichter zwischen XLE und USO untersucht.
- Die Kennzahlen von Hafez und Xie sowie die 17, 17 und 7 Prozent der Fonds-Pressure-Strategien gelten vor Transaktionskosten.
- Beim PRESSURE-Portfolio ist die Slippage wahrscheinlich erheblich, weil die Holdings der Fonds zum Quartalsende verzögert eintreffen.
- Die Portfoliorendite wird durch 30 geteilt, weil im Testzeitraum höchstens 30 Positionen an einem Tag vorkamen.
- In dieser 30 steckt Look-ahead-Bias, weil das künftige Maximum unbekannt ist; der Text hält den Bias für nicht schwerwiegend, weil die Höchstzahl der Meldungen pro Tag recht vorhersehbar ist.
- Die Optimierung der historischen Wachstumsrate nutzt nur die eine realisierte Renditereihe und leidet unter Data-Snooping-Bias.
- Der für diese historische Realisierung optimale Hebel ist für eine künftige Realisierung im Allgemeinen nicht optimal.
- Anders als Monte Carlo bieten die historischen Renditen zu wenig Daten für einen Hebel, der über viele Realisierungen gut funktioniert.
- Selbst von den Fallstricken aus Kapitel 1 befreite Strategien können durch Regimewechsel Opfer werden; die Strategien illustrieren Technik und sind keine Garantie.
- Backtests führender Risikoindikatoren sind anfällig für Data-Snooping, weil Finanzpaniken selten sind, und kein Finanzindikator sagt natürliche oder andere nichtfinanzielle Katastrophen voraus.
- Simulierte Renditen verfehlen serielle Korrelationen, die in der Historie stecken, fortbestehen und den realen maximalen Drawdown senken können.

## Beispiele

- Trotz der langen Halbwertszeit ist die kumulierte P&L der linearen Strategie auf USD.CAD positiv, allerdings mit großem Drawdown.
- Der Backtest der linearen Strategie auf EWA, EWC und IGE zeigt in Abbildung 2.7 die kumulierten Renditen und liefert APR gleich 12,6 Prozent sowie eine Sharpe Ratio von 1,4.
- Die tägliche P&L ist die Summe aus verzögerten Dollarpositionen mal den einfachen Renditen der drei ETFs, und die Rendite teilt diese P&L durch den Bruttomarktwert.
- Der Preis-Spread von GLD und USO mit täglich neu geschätzter Hedge Ratio und einem im Nachhinein fast optimalen Lookback von 20 Handelstagen erreicht etwa 10,9 Prozent APR und eine Sharpe Ratio von etwa 0,59, obwohl die beiden ETFs nicht kointegriert sind.
- Der Log-Preis-Spread derselben beiden ETFs erreicht 9 Prozent APR und eine Sharpe Ratio von 0,5, noch vor den zusätzlichen Kosten des täglichen Rebalancings.
- Dieselbe lineare Strategie auf dem Verhältnis USO zu GLD hat eine negative APR.
- Die Bollinger-Variante mit entryZscore gleich 1 und exitZscore gleich 0 erreicht auf GLD und USO 17,8 Prozent APR und eine Sharpe Ratio von 0,96.
- Die Kalman-Strategie auf EWA und EWC, mit δ gleich 0,0001 und Ve gleich 0,001 im Nachhinein gewählt, erreicht 26,2 Prozent APR und eine Sharpe Ratio von 2,4.
- Waren die tatsächlichen Preise um 11:00, 11:01 und 11:02 jeweils 100 Dollar, die Historie aber fälschlich 100, 110 und 100 Dollar, shortet eine Mean-Reversion-Strategie im Backtest um 11:01 bei 110 Dollar und deckt um 11:02 bei 100 Dollar ein, mit einem fiktiven Gewinn von 10 Dollar.
- Im selben Beispiel kauft eine Momentum-Strategie im Backtest um 11:01 bei 110 Dollar und kann um 11:02 bei 100 Dollar mit Verlust gestoppt werden.
- Buy-on-Gap auf SPX-Aktien mit Survivorship Bias hat vom 11. Mai 2006 bis 24. April 2012 eine APR von 8,7 Prozent und eine Sharpe Ratio von 1,5; die vom Autor gehandelte Fassung ohne Regel 2 litt ab 2009 unter nachlassenden Renditen, ist long-only risikotechnisch anspruchsvoll und hat wegen weniger Titel je Tag keine große Kapazität.
- Die gespiegelte Short-on-Gap-Fassung hat über denselben Zeitraum eine APR von 46 Prozent und eine Sharpe Ratio von 1,27, aber einen steileren Drawdown und dasselbe Short-Sale-Problem.
- Die Arbitrage zwischen einem gleichgewichteten Portfolio aus 98 mit SPY kointegrierenden Aktien und SPY hat im Test vom 2. Januar 2008 bis 9. April 2012 eine APR von 4,5 Prozent und eine Sharpe Ratio von 1,3; der Look-back von 5 für Mittel und Standardabweichung ist mit Hindsight fixiert, und die Performance fällt auch, weil das Modell nicht periodisch neu trainiert wird.
- Das lineare Long-Short-Modell auf dem SPX hat vom 2. Januar 2007 bis 30. Dezember 2011 eine APR von 13,7 Prozent und eine Sharpe Ratio von 1,3, darunter 30 Prozent APR 2008 und 11 Prozent APR 2011; ab Anfang 2008 ist das ein echter Out-of-Sample-Test, weil die Strategie 2007 veröffentlicht wurde, und kleinere Caps liefern gewöhnlich höhere Renditen.
- Die Open-to-Close-Variante desselben Modells hat über denselben Zeitraum eine APR von 73 Prozent und eine Sharpe Ratio von 4,7; die nicht enthaltenen Transaktionskosten verdoppeln sich, weil zweimal täglich gehandelt wird, und es besteht dasselbe Signalrauschen wie beim Buy-on-Gap.
- Die dem Autor bekannte Johansen-Implementierung von LeSage 1998 akzeptiert höchstens 12 Symbole, sodass ein Test auf alle 500 SPX-Titel plus SPY daran scheitert.
- Beispiel AUD gegen CAD nutzt ein festes Trainingsfenster von 250 Tagen, weil es im Nachhinein bessere Ergebnisse liefert, und einen Look-back von 20 Tagen für Mittel und Standardabweichung; nach Ausschluss der ersten 250 Tage sind APR 11 Prozent und Sharpe Ratio 1,6 vom 18. Dezember 2009 bis 26. April 2012.
- Der Johansen-Test muss auf AUD.USD und CAD.USD laufen, nicht auf USD.AUD gegen USD.CAD, damit der Dollarwert einer Punktbewegung gleich ist; eine Order Kauf 1 CAD.USD wird live zu Verkauf 1/y USD.CAD, wobei y die aktuelle USD.CAD-Quote ist.
- AUD.CAD mit Rollover hat APR 6,2 Prozent und Sharpe Ratio 0,54; ohne Rollover wären es 6,7 Prozent und 0,58, bei einem annualisierten durchschnittlichen Rollover von fast 5 Prozent.
- Der 12-Monats-Log-Kalender-Spread von CL ist im ADF mit 99 Prozent stationär, Halbwertszeit 36 Tage; die lineare Strategie hat vom 2. Januar 2008 bis 13. August 2012 eine ungehebelte APR von 8,3 Prozent und eine Sharpe Ratio von 1,3.
- Die historischen Zinsen im Rollover-Backtest kommen vom Geldmarktsatz der Reserve Bank of Australia und von den Overnight-Finanzierungssätzen der Bank of Canada.
- Trotz der Vorbehalte liefert die direkte Optimierung über die Backtest-Renditen im Beispiel derselben Strategie wieder den Hebel 18,4, wie Kelly.
- An den historischen Strategierenditen senkte eine Kürzung des unbeschränkten Optimalhebels um den Faktor 1,5 auf 13 den maximalen Drawdown unter minus 0,49.
- Der Autor hat nie eine Mean-Reversion-Strategie gebacktestet, deren APR oder Sharpe Ratio durch einen Stop-Loss stieg.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 20–39 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-002-p020-p039|S. 20–39]]
- Advances in Financial Machine Learning.pdf, S. 39–58 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-003-p039-p058|S. 39–58]]
- Advances in Financial Machine Learning.pdf, S. 134–153 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-008-p134-p153|S. 134–153]]
- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 173–186 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-013-p173-p186|S. 173–186]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]

## Verwandte Themen
