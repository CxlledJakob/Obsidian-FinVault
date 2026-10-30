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

## Funktionsweise

- Alternative Szenarien sind im Einklang mit den bekannten Stärken und Schwächen der vorgeschlagenen Strategie zu prüfen.

## Voraussetzungen

- Die Station braucht Data Scientists mit tiefem Verständnis empirischer und experimenteller Techniken.

## Anwendung im Trading

- Im Embargo läuft die Strategie auf Daten, die nach dem Enddatum des Backtests beobachtet wurden.
- Diese Periode kann von den Backtestern reserviert worden sein oder aus Implementierungsverzögerungen stammen.
- Passt die Embargo-Performance zum Backtest, wird die Strategie in die nächste Stufe befördert.

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

## Beispiele


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
