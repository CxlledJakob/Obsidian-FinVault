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

# Embargoing


## Kurzdefinition

- Embargo heißt, Trainingsbeobachtungen zu entfernen, die unmittelbar auf ein Testset folgen, wenn Purging nicht alles Leakage verhindert.
- Ein Embargo sperrt Trainingsbeobachtungen unmittelbar nach jedem Testset, wenn Purging nicht jede Leakage verhindern kann.
- Ein Embargo wird angewendet, wenn Testbeobachtungen zeitlich vor Trainingsbeobachtungen liegen.

## Kernaussagen

- Der Anlass sind Finanzfeatures mit serieller Korrelation, wie bei ARMA-Prozessen.
- Trainingsbeobachtungen vor dem Testset müssen nicht embargoed werden, wenn ihr Label endet, bevor der Test beginnt. Diese Information war zum Testzeitpunkt bereits verfügbar.
- Betroffen sind Trainingslabels, die unmittelbar nach dem Test starten, also zwischen dem Testende und dem Testende plus einer Frist h.
- Umgesetzt wird die Frist, indem das Testlabel vor dem Purging bis zum Testende plus h verlängert wird.
- Ein kleines h von etwa 1 Prozent der Bars genügt oft, um alles Leakage zu verhindern.
- Die Kontrolle ist, dass die Leistung nicht unbegrenzt steigt, wenn die Zahl der Folds gegen die Zahl der Bars geht.
- In Walk-Forward-Backtests ist kein Embargo nötig, weil das Trainingsset dem Testset immer vorausgeht.
- Bei der Backtest-Cross-Validation können Purging und Embargo Informationsleakage verhindern, weil das Trainingsset dem Testset nicht nachläuft.

## Funktionsweise

- Vor dem Purging wird das Testlabel als Funktion des Intervalls vom Teststart bis zum Testende plus h gesetzt.
- Danach werden Trainingslabels entfernt, deren Start in diesem verlängerten Ende liegt. Abbildung 7.3 zeigt das Embargo der Trainingsbeobachtungen unmittelbar nach dem Testset.
- Das Embargo muss Trainingsbeobachtungen vor einem Testset nicht erfassen, denn endet das Training vor Testbeginn, enthalten die Labels nur Information, die zum Testzeitpunkt bereits verfügbar war.
- Relevant sind nur Trainingslabels, deren Beginn ti,0 unmittelbar nach dem Test liegt, von tj,1 bis einschließlich tj,1 plus der Embargo-Dauer h.
- Die Embargo-Periode h wird umgesetzt, indem vor dem Purging das Label des Testfensters bis tj,1 plus h verlängert wird.
- Ein kleiner Wert h von etwa 0,01T genügt oft, um jede Leakage zu verhindern.
- Dass dieses h ausreicht, lässt sich daran prüfen, dass die Performance nicht unbegrenzt steigt, wenn k gegen T geht.
- In PurgedKFold beginnt der rechte Trainingsabschnitt erst nach dem maximalen Ende der Testlabels plus Embargo.
- Im Algorithmus der kombinatorischen purged Cross-Validation setzt die Klasse PurgedKFold dieses Embargo.
- Purging und Embargoing stammen aus der Cross-Validation von Kapitel 7 und werden hier für das Backtesting durch Cross-Validation verwendet.

## Voraussetzungen

- Das Embargo ist für die Fälle gedacht, in denen das Purging überlappender Labels das Leakage nicht vollständig beseitigt.

## Anwendung im Trading


## Regeln und Kriterien

- Als Frist nennt der Text h ungefähr 0,01 mal T, wobei T die Zahl der Bars ist.
- Die Frist gilt für Trainingslabels nach dem Test, nicht für Labels, die vor Beginn des Tests enden.
- Überlappende Trainingsbeobachtungen sind zu purgen und zu embargoen, wann immer ein Trainings- und Test-Split entsteht, auch für Hyperparameter-Anpassung, Backtesting und Performance-Evaluation.

## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 115–134 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-007-p115-p134|S. 115–134]]
- Advances in Financial Machine Learning.pdf, S. 134–153 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-008-p134-p153|S. 134–153]]
- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]

## Verwandte Themen
