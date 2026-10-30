---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Validierung"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Purged Cross-Validation


## Kurzdefinition

- Purged k-Fold-CV entfernt aus dem Trainingsset alle Beobachtungen, deren Labels zeitlich mit Labels im Testset überlappen, um Leakage zu verringern.
- Purged k-Fold-Cross-Validation entfernt aus dem Trainingsset Beobachtungen, deren Label-Intervalle mit dem Testset überlappen, damit keine Testinformation ins Training leckt.
- Die combinatorial purged cross-validation erzeugt genau so viele Kombinationen von Trainings- und Testsets, wie für eine vom Forscher gewünschte Zahl von Backtest-Pfaden nötig sind, und purgt dabei Trainingsbeobachtungen, die geleakte Information enthalten.
- Die kombinatorische purged Cross-Validation bildet aus allen Kombinationen von k Testgruppen mehrere Backtest-Pfade und entfernt aus dem Training Information, die zum Test gehört.

## Kernaussagen

- Zwei Beobachtungen überlappen informationell, wenn ihre Labels gleichzeitig sind, also beide von mindestens einer gemeinsamen Zufallsziehung abhängen.
- Eine Überlappung liegt vor, wenn mindestens eine von drei hinreichenden Bedingungen gilt: Der Trainingsstart liegt im Testintervall, das Trainingsende liegt im Testintervall, oder das Trainingsintervall umschließt das Testintervall.
- Bei der Triple-Barrier-Labelmethode ist das Label das Vorzeichen der Rendite zwischen den Preisbars am Anfang und am Ende dieses Intervalls.
- Ist das Testset zusammenhängend, sodass zwischen der ersten und der letzten Testbeobachtung keine Trainingsbeobachtung liegt, genügt für die Testzeit ein einzelner Eintrag über das ganze Testset, und das Purging wird schneller.
- Ohne diese Bereinigung steigt die Leistung allein dadurch, dass die Zahl der Folds gegen die Zahl der Bars geht, weil mehr überlappende Beobachtungen im Training bleiben.
- Oft genügt das Purging. Die Leistung steigt dann mit der Fold-Zahl, weil das Modell öfter neu kalibriert wird, aber jenseits eines bestimmten k nicht weiter.
- Bleibt die Leistung ab diesem Punkt stehen, zeigt das, dass der Backtest nicht von Leaks profitiert.
- Wo das Purging nicht alles Leakage nimmt, wird zusätzlich ein Embargo auf Trainingsbeobachtungen unmittelbar nach jedem Testset gelegt.
- Abbildung 7.2 zeigt eine Aufteilung, in der das Testset zwischen zwei Trainingsblöcken liegt und zwei Überlappungen erzeugt, die entfernt werden müssen.
- Hyperparameter werden in diesem Kapitel mit der gepurgten k-Fold-Cross-Validation getunt.
- GridSearchCV muss PurgedKFold erhalten, damit der ML-Schätzer nicht auf geleakte Information überfittet.
- Sie adressiert den Hauptnachteil von Walk-Forward und gewöhnlicher Cross-Validation, nämlich dass diese Schemata nur einen Pfad testen.
- Beim Walk-Forward garantieren nachlaufende Daten ein Out-of-Sample-Testset nur, wenn das Purging aus Kapitel 7, Abschnitt 7.4.1, korrekt umgesetzt ist.
- Ein Embargo ist im Walk-Forward nicht nötig, weil das Trainingsset dem Testset stets vorausgeht.
- Bei der Backtest-Cross-Validation ist Leakage möglich, weil das Training dem Test nicht nachläuft; Purging und Embargo können das verhindern.
- Für k gleich 1 bleibt ein Pfad, und das Verfahren fällt mit der gewöhnlichen Cross-Validation zusammen.
- Liegt die mittlere Korrelation zwischen den Pfaden unter 1, ist die Varianz des Mittelwerts kleiner als die Varianz der einzelnen Pfad-Sharpe-Ratios.
- Je schwächer die Pfade miteinander korrelieren, desto kleiner wird die Varianz des Mittelwerts ihrer Sharpe Ratios.
- Im Grenzfall sehr vieler kaum korrelierter Pfade geht die Varianz des Mittelwerts der Pfad-Sharpe-Ratios gegen null, und die ausgewählte Strategie hätte die höchste wahre Sharpe Ratio.

## Funktionsweise

- Die Funktion getTrainTimes streicht Trainingsbeobachtungen, die im Testintervall starten, darin enden oder das Testintervall umschließen.
- Das Embargo lässt sich vor diesem Schritt einbauen, indem das Testintervall um die Frist h verlängert wird.
- In einer Partition der k-Fold-CV ist das Testset von zwei Trainingssets umgeben, und die beiden Überlappungen müssen gepurgt werden.
- Die Klasse PurgedKFold erweitert scikit-learns KFold für Labels, die Zeitintervalle überspannen.
- Das Trainingsset wird von Beobachtungen befreit, die mit den Label-Intervallen des Tests überlappen.
- Das Testset wird als zusammenhängend angenommen, mit shuffle gleich False und ohne Trainingsbeobachtungen dazwischen.
- Die Label-Through-Dates t1 müssen eine pandas-Series sein und denselben Index wie X haben.
- Der rechte Trainingsabschnitt beginnt erst nach dem maximalen Ende der Testlabels plus dem Embargo.
- Die Funktion cvScore bildet die Fold-Scores mit PurgedKFold und umgeht damit cross_val_score.
- clfHyperFit bildet die innere Cross-Validation als PurgedKFold mit der Splitzahl cv, den Label-Through-Dates t1 und dem Embargo-Anteil pctEmbargo.
- Im Snippet sind die Defaults cv = 3 und pctEmbargo = 0.
- Dieselbe gepurgte innere Cross-Validation wird an RandomizedSearchCV übergeben, sobald die randomisierte Suche statt der Grid Search läuft.
- T Beobachtungen werden ohne Mischen in N Gruppen geteilt; die Gruppen 1 bis N−1 haben die Größe des ganzzahligen Anteils T/N, und die N-te Gruppe umfasst den Rest.
- Bei einem Testset aus k Gruppen ist die Zahl der Trainings- und Test-Splits der Binomialkoeffizient N über N−k, also das Produkt von i = 0 bis k−1 von (N − i), geteilt durch k Fakultät.
- Weil jede Kombination k Gruppen testet und alle Kombinationen gebildet werden, sind die getesteten Gruppen gleichmäßig über alle N Gruppen verteilt; jede Gruppe gehört zur selben Zahl von Trainings- und Testsets.
- Die Zahl der Backtest-Pfade φ[N, k] ist k/N mal dem Binomialkoeffizienten N über N−k, gleich dem Produkt von i = 1 bis k−1 von (N − i), geteilt durch (k − 1) Fakultät.
- Für N = 6 und k = 2 gibt es 15 Splits, und jede Gruppe gehört zu φ[6, 2] = 5 Testsets, sodass sich fünf Backtest-Pfade berechnen lassen.
- Abbildung 12.1 markiert je Split die im Testset liegenden Gruppen, und Abbildung 12.2 ordnet jede getestete Gruppe einem der fünf Pfade zu.
- Pfad 1 entsteht durch Kombination der Prognosen unter anderem aus (G1, S1) und (G2, S1).
- T Beobachtungen werden ohne Umsortieren in N Gruppen geteilt.
- In jeder Aufteilung bilden N minus k Gruppen das Training und k Gruppen den Test.
- Ein Trainingslabel wird entfernt, wenn es einen Zeitraum überdeckt, der zur Bestimmung eines Testlabels gedient hat.
- Liegen Testbeobachtungen zeitlich vor Trainingsbeobachtungen, setzt die Klasse PurgedKFold zusätzlich ein Embargo.
- Auf jeder Trainingsmenge wird ein Klassifikator angepasst, und auf der zugehörigen Testmenge werden Prognosen erzeugt.
- Aus diesen Prognosen werden die Backtest-Pfade zusammengesetzt.
- Die Zahl der Pfade ist k/N mal die Zahl der Aufteilungen.
- Die Pfadzahl steigt, wenn N gegen T geht und wenn k gegen N/2 geht.
- Bei N gleich 6 und k gleich 2 gibt es 15 Aufteilungen und 5 Pfade, weil jede Gruppe in 5 Testmengen liegt.
- Pfad 1 verbindet Gruppe 1 und Gruppe 2 aus Aufteilung 1 mit Gruppe 3 aus Aufteilung 2, Gruppe 4 aus Aufteilung 3, Gruppe 5 aus Aufteilung 4 und Gruppe 6 aus Aufteilung 5.
- Für k gleich 2 entstehen N minus 1 Pfade, und trainiert wird auf dem Anteil 1 minus 2/N.
- Die Faustregel setzt N auf die angestrebte Pfadzahl plus 1 und bildet die Kombinationen mit zwei Testgruppen.
- Bei einer Gruppe je Beobachtung und k gleich 2 entstehen T minus 1 Pfade, bei einem Trainingsanteil von 1 minus 2/T.
- Die größte Pfadzahl entsteht bei N gleich T und k gleich T/2, dann wird je Kombination nur auf der Hälfte der Daten trainiert.
- In der Praxis genügt oft k gleich 2, wenn N als angestrebte Pfadzahl plus 1 gewählt wird und diese Gruppenzahl höchstens T ist.

## Voraussetzungen


## Anwendung im Trading

- Das Verfahren ist die im Text vorgeschlagene Form der k-Fold-CV für Finanzlabels, die aus überlappenden Zeiträumen gebildet werden.

## Regeln und Kriterien

- Die drei hinreichenden Bedingungen sind: Teststart kleiner oder gleich Trainingsstart kleiner oder gleich Testende; Teststart kleiner oder gleich Trainingsende kleiner oder gleich Testende; Trainingsstart kleiner oder gleich Teststart kleiner oder gleich Testende kleiner oder gleich Trainingsende.
- Als Embargo-Frist nennt der Text etwa 0,01 mal die Zahl der Bars. Sie ist ausreichend, wenn die Leistung bei immer größerem k nicht unbegrenzt steigt.
- Purging und Embargo sind bei jedem Trainings- und Test-Split nötig, auch für Hyperparameter-Anpassung, Backtesting und Performance-Evaluation.
- Die Mean-Decrease-Accuracy muss mit gepurgter und embargoed Cross-Validation berechnet werden.
- Bis zur Behebung der sklearn-Fehler 6231 und 9144 soll cvScore statt cross_val_score verwendet werden.

## Risiken und Grenzen

- Ein häufiger Fehler in Walk-Forward-Backtests ist Leakage, bei dem t1.index im Trainingsset liegt, t1.values aber im Testset.
- Eine Varianz von null ist unerreichbar, weil die Pfadzahl begrenzt ist.
- Bei einer großen Pfadzahl kann die Varianz so klein werden, dass die Wahrscheinlichkeit einer Fehlentdeckung vernachlässigbar wird.

## Beispiele

- Im synthetischen MDA-Beispiel sind die Standardabweichungen der Mittelwerte etwas höher; das ließe sich mindern, indem die Zahl der Partitionen der gepurgten k-Fold-CV von 10 auf 100 steigt, bei zehnfacher Rechenzeit ohne Parallelisierung.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 115–134 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-007-p115-p134|S. 115–134]]
- Advances in Financial Machine Learning.pdf, S. 134–153 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-008-p134-p153|S. 134–153]]
- Advances in Financial Machine Learning.pdf, S. 153–172 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-009-p153-p172|S. 153–172]]
- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]

## Verwandte Themen
