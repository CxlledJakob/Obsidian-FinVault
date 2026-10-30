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

## Funktionsweise


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
