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

# Walk-Forward-Analyse


## Kurzdefinition

- Walk-Forward ist eine historische Simulation, wie die Strategie in der Vergangenheit abgeschnitten hätte, und jede Strategieentscheidung beruht auf Beobachtungen, die dieser Entscheidung vorausgehen.
- Der Begriff Backtest ist faktisch zum Synonym für diese historische Simulation geworden.

## Kernaussagen

- Scikit-learn hat eine Walk-Forward-Timefolds-Methode umgesetzt: Der Test bewegt sich in der Zeit vorwärts, um Leakage zu verhindern, im Einklang damit, wie historische Backtests und der Handel ablaufen.
- Bei langreichweitiger serieller Abhängigkeit genügt es nicht, eine Beobachtung hinter dem Ende des Trainingssets zu testen, um Informationsleakage zu vermeiden.
- Ein fehlerfreier Walk-Forward ist eine gewaltige Aufgabe und verlangt extreme Kenntnis der Datenquellen, der Marktmikrostruktur, des Risikomanagements, der Performancestandards wie GIPS, der Multiple-Testing-Verfahren und der experimentellen Mathematik.
- Es gibt kein allgemeines Rezept für einen Backtest; jeder Backtest muss auf die Annahmen der jeweiligen Strategie zugeschnitten sein.
- Walk-Forward hat eine klare historische Deutung, und seine Leistung lässt sich mit Paper-Trading abgleichen.
- Geschichte ist eine Filtration, deshalb garantieren nachlaufende Daten ein Out-of-Sample-Testset ohne Leakage, sofern das Purging aus Kapitel 7, Abschnitt 7.4.1, korrekt umgesetzt ist.
- Ein Embargo ist in Walk-Forward-Backtests nicht nötig, weil das Trainingsset dem Testset immer vorausgeht.
- Die combinatorial purged cross-validation adressiert den Hauptnachteil von Walk-Forward und gewöhnlicher Cross-Validation, dass beide nur einen Pfad testen.
- Walk-Forward-Backtests haben eine hohe Varianz, weil ein großer Teil der Entscheidungen auf einem kleinen Teil der Daten beruht.
- Wenige Beobachtungen erhalten dadurch ein großes Gewicht in der Sharpe Ratio.
- Eine Aufwärmphase verkürzt den Backtest und kann die Varianz weiter erhöhen.
- Die hohe Varianz erzeugt Fehlentdeckungen, weil der Backtest mit der höchsten geschätzten Sharpe Ratio gewählt wird, auch wenn der wahre Wert null ist.
- Bei Walk-Forward muss deshalb die Zahl der Versuche kontrolliert werden.
- Ohne die Zahl der Versuche lassen sich Family-Wise Error Rate, False Discovery Rate und Probability of Backtest Overfitting nicht bestimmen.
- Cross-Validation erzeugt weniger Fehlentdeckungen als Walk-Forward und schätzt die Sharpe Ratio ebenfalls aus einem einzigen Pfad.
- Die kombinatorische purged Cross-Validation erzeugt weniger Fehlentdeckungen als Walk-Forward und als Cross-Validation.
- So sorgfältig Data-Snooping im Test auch verhindert wird, es schleicht sich ein. Deshalb ist ein Walk-Forward-Test der abschließende echte Out-of-Sample-Test.
- Dieser Walk-Forward-Test kann als Paper Trading laufen. Besser wird das Modell mit echtem Geld bei minimalem Hebel gehandelt, um zu prüfen, was selbst dem Paper Trading entgeht.
- Die meisten Trader wären zufrieden, wenn der Live-Handel eine Sharpe Ratio besser als die Hälfte des Backtest-Wertes erzeugt.
- Walk-Forward-Testing ist ein weiteres Schema zur Aufteilung der Daten, das speziell für den Handel an Finanzmärkten beschrieben wird, bei Pardo, De La Maza, Katz und McCormick sowie Kaufman.
- Es benutzt ein wanderndes Datenfenster, das selbst in einen In-Sample- und einen Out-of-Sample-Abschnitt geteilt ist.
- Wegen des dynamischen Aspekts, bei dem die Regel im Zeitverlauf mit der Marktentwicklung verändert wird, heißt der In-Sample-Abschnitt Trainingsdatensatz, weil dort die besten Parameter gelernt werden, und der Out-of-Sample-Abschnitt Testdatensatz.
- Das Fenster aus Trainings- und Testset, das vorwärts geschoben wird, wird im Regeltest manchmal Fold genannt.
- Für jeden Fold wird eine Out-of-Sample-Performanceschätzung berechnet; bei typischerweise vielen Folds lässt sich die Varianz der Performancestatistik bestimmen und ein Konfidenzintervall berechnen.
- Das wandernde Fenster gibt dem Regeltest eine dynamische Anpassung, weil in jeder neuen Realisierung des Fensters eine neue Regel formuliert werden kann.
- Das macht Walk-Forward besonders attraktiv für nichtstationäre Phänomene wie Finanzmärkte.
- Hsu und Kuan fanden adaptive Handelsregeln, von ihnen Lernstrategien genannt, in ihrem Test von über 36.000 objektiven Regeln wirksam.
- Im Walk-Forward dient der Trainingsabschnitt dem Data Mining, die dort beste Regel wird auf dem Testabschnitt geprüft und liefert eine unverzerrte Out-of-Sample-Schätzung, danach wird das ganze Fenster nach vorn geschoben und der Vorgang wiederholt.
- Das Fenster wird so weit vorgeschoben, dass sich die Testabschnitte getrennter Folds nicht überlappen; die Out-of-Sample-Schätzungen sind dadurch voneinander unabhängig.
- Michael Cooper verwendete eine Walk-forward-out-of-sample-Simulation, um Portfolios aus Long- und Short-Positionen über 1978 bis 1993 zu bilden und der Möglichkeit von Data Mining zu begegnen.
- Die aus 300 Aktien großer Kapitalisierung gebildeten Portfolios erzielten eine annualisierte Rendite von 44,95 Prozent gegen eine Buy-and-hold-Benchmark von 17,91 Prozent.
- Das so geprüfte Muster sind Aktien, die über die vorangegangenen zwei Wochen bei fallendem Volumen scharf gefallen sind und über die folgende Woche systematisch zu steigen neigen.

## Funktionsweise

- Das Schema aus drei Segmenten, Training, Test und Validierung, lässt sich auf Walk-forward-Basis führen: nachdem die beste Regel in der ersten Datenfalte gefunden wurde, rückt das dreigeteilte Datenfenster vor und der ganze Prozess wiederholt sich in der nächsten Falte.
- Figur 9.7 zeigt aufeinanderfolgende Falten, jede mit Trainings-, Test- und Validierungssatz, die in der Zeit voranschreiten.
- In der inneren Schleife werden bei einer gegebenen Komplexität verschiedene Parameterwerte auf dem Trainingssatz probiert, und die beste Regel dieser Stufe wird auf dem Testsatz gemessen.
- Die äußere Schleife sucht die optimale Komplexität, indem nacheinander Regeln höherer Komplexität, also mit einer größeren Zahl von Parametern, im Training gesucht und im Test bewertet werden.
- Der Validierungssatz bleibt aus der Suche nach Parametern und Komplexität heraus und dient erst danach der Bewertung der Leistung der besten Regel.
- Weil der Testsatz bei der Komplexitätssuche mehrfach benutzt wird, ist die dort erreichte Bestleistung positiv verzerrt; der Validierungssatz liefert die unverzerrte Schätzung der künftigen Leistung.
- Bei fest vorgegebener Komplexität und reiner Suche nach optimalen Parametern genügen zwei Segmente, Training und Test; das dritte Segment wird erst nötig, wenn die Komplexität selbst optimiert wird.
- Im menschlichen Beispiel beginnt die Suche mit 100 Tests einer Regel aus zwei gleitenden Durchschnitten, wenn jeder Durchschnitt 10 Parameterwerte hat.
- Solange der Testsatz nur einmal benutzt wird, sind 15 Prozent annualisierte Rendite dort eine unverzerrte Schätzung; sobald weitere Komplexitätsstufen denselben Testsatz erneut besuchen, entsteht der Data-Mining-Bias, den erst der Validierungssatz korrigiert.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Ein häufiger Fehler ist Leakage in Walk-Forward-Backtests, bei dem t1.index im Trainingsset liegt, t1.values aber im Testset.
- Walk-Forward prüft nur ein Szenario, den historischen Pfad, und dieser lässt sich leicht überfitten, nach Bailey et al. 2014.
- Walk-Forward ist nicht notwendig repräsentativ für die künftige Leistung, weil die Ergebnisse durch die besondere Folge der Datenpunkte verzerrt sein können.
- Befürworter des Walk-Forward argumentieren typischerweise, die Vergangenheit vorherzusagen führe zu übermäßig optimistischen Leistungsschätzungen.
- Ein Walk-Forward-Backtest lässt sich ebenso leicht überfitten wie ein Walk-Backward-Backtest, und widersprüchliche Ergebnisse bei geänderter Beobachtungsfolge sind ein Beleg für dieses Overfitting.
- Würde das Hauptargument für Walk-Forward stimmen, müssten Walk-Backward-Backtests ihre Walk-Forward-Gegenstücke systematisch übertreffen; das ist nicht der Fall, deshalb ist das Hauptargument eher schwach.
- Ohne Zufallsziehung gibt es nur einen Testpfad, der immer wieder wiederholt werden kann, bis ein falsch positives Ergebnis erscheint.
- Die ersten Entscheidungen beruhen auf einem kleineren Teil der Gesamtstichprobe; selbst mit Aufwärmphase wird der Großteil der Information nur von einem kleinen Teil der Entscheidungen verwendet.
- Nutzt die Aufwärmphase t0 von T Beobachtungen, trifft die Strategie die Hälfte ihrer Entscheidungen auf durchschnittlich nur einem Anteil von drei Vierteln t0/T plus einem Viertel der Beobachtungen.
- Eine längere Aufwärmphase mildert dieses Problem, verkürzt aber auch den Backtest.

## Beispiele

- Eine Aktienstrategie, die ab dem 1. Januar 2007 per Walk-Forward auf S&P-500-Daten getestet wird, wird bis zum 15. März 2009 durch die Mischung aus Rallyes und Verkäufen auf markneutral und niedrige Konfidenz trainiert; danach dominiert die lange Rallye, und am 1. Januar 2017 überwiegen die Kaufprognosen.
- Dieselbe Information rückwärts, vom 1. Januar 2017 zum 1. Januar 2007, ergäbe eine ganz andere Leistung, weil dann eine lange Rallye von einem scharfen Ausverkauf gefolgt wäre.
- Wer eine bestimmte Folge ausnutzt, kann mit einer per Walk-Forward ausgewählten Strategie auf eine Niederlage zusteuern.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 305–324 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-017-p305-p324|S. 305–324]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 381–400 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-021-p381-p400|S. 381–400]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]

## Verwandte Themen

- Gleitende Durchschnitte, wandernde Max-Min-Preiskanäle und Rate-of-Change-Indikatoren benutzen ebenfalls ein Datenfenster, das entlang der Zeitachse gleitet, und die Rechenoperationen bleiben auf die Daten im Fenster beschränkt.
