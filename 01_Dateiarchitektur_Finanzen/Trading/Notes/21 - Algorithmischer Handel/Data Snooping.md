---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Validierung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Data Snooping


## Kurzdefinition

- Data Mining und Data Snooping werden in den sieben Sünden von Luo et al. 2014 als das Trainieren des Modells auf dem Testset gefasst.
- Über viele Versuche hinweg liegt der erwartete Höchstwert der geschätzten Sharpe Ratio selbst dann über null, wenn die wahre Sharpe Ratio null ist.
- Data-Snooping-Bias entsteht, wenn zu viele freie Parameter an zufällige, flüchtige Marktmuster der Vergangenheit angepasst werden, damit die historische Performance gut aussieht.

## Kernaussagen

- Unter der Nullhypothese einer wahren Sharpe Ratio von null ist der erwartete Höchstwert der geschätzten Sharpe Ratios die Vergleichsschwelle der Deflated Sharpe Ratio.
- Die Schwelle steigt schnell mit der Zahl unabhängiger Versuche und mit der Varianz der in diesen Versuchen geschätzten Sharpe Ratios.
- Jedes Backtestergebnis muss zusammen mit allen Versuchen berichtet werden, die zu seiner Erstellung geführt haben.
- Fehlt die Angabe aller Versuche, lässt sich die Wahrscheinlichkeit einer Fehlentdeckung nicht beurteilen.
- Die Überschrift des dritten Gesetzes des Backtesting lautet, dass die meisten Entdeckungen in der Finanzwelt falsch sind, weil die Versuche nicht mitberichtet werden.
- Die Deflated Sharpe Ratio korrigiert die Sharpe Ratio um nichtnormale Renditen, um die Länge der Historie und um Mehrfachtests sowie Selection Bias.
- Der durchgehende Schwerpunkt liegt auf einfachen und linearen Strategien als Gegenmittel gegen die Overfitting- und Data-Snooping-Verzerrungen, die komplexe Strategien oft plagen.
- Möglichst viele technische Handelsindikatoren oder Regeln auf eine Preisreihe zu werfen, um zu sehen, welcher Indikator oder welche Regel profitabel ist, lädt Data-Snooping-Bias ein.
- Stattdessen wird die grundlegende Eigenschaft der Preisreihe mit einem einfachen mathematischen Modell herausgearbeitet und dieses Modell dann finanziell ausgenutzt.
- Diese zufälligen Muster kehren in der Zukunft wahrscheinlich nicht wieder, sodass ein daran angepasstes Modell wenig Vorhersagekraft hat.
- Der bekannte Nachweis ist ein Test auf Out-of-Sample-Daten und die Verwerfung eines Modells, das ihn nicht besteht.
- Wer das Modell nachjustiert, bis In-Sample- und Out-of-Sample-Ergebnis beide annehmbar aussehen, hat die Out-of-Sample-Daten in In-Sample-Daten verwandelt.
- Zur Eingrenzung wird das Modell so einfach wie möglich und mit so wenigen Parametern wie möglich gebaut.
- Am Ende schleicht sich der Bias dennoch ein. Deshalb ist ein Walk-Forward-Test der abschließende echte Out-of-Sample-Test.
- Dieser Walk-Forward kann als Paper Trading laufen. Besser wird das Modell mit echtem Geld bei minimalem Hebel gehandelt, um Aspekte zu prüfen, die selbst dem Paper Trading entgehen.
- Die meisten Trader wären zufrieden, wenn der Live-Handel eine Sharpe Ratio besser als die Hälfte des Backtest-Wertes erzeugt.
- Die lineare Mean-Reversion-Strategie hat keinen Data-Snooping-Bias, weil sie keine Parameter besitzt, die optimiert werden.
- Selbst der Lookback wird nicht an der Strategie optimiert, sondern gleich der Halbwertszeit gesetzt, einer Eigenschaft der Preisreihe und nicht der konkreten Handelsregel.
- Die lineare Strategie wird gewählt, weil sie praktisch parameterfrei ist und deshalb am wenigsten unter Data-Snooping-Bias leidet.
- Sie eignet sich, um zu zeigen, ob Mean-Reversion-Handel für ein Portfolio profitabel sein kann, ist aber unpraktisch, weil die Abweichung vom Mittel und damit das gebundene Kapital nicht begrenzt ist.
- Alle höheren Momente zu erfassen lädt wegen der meist geringen empirischen Datenmenge zu Data-Snooping-Bias ein.
- Praktisch werden deshalb für die Monte-Carlo-Verteilung nur die ersten vier Momente über das Pearson-System verwendet.
- Die Hebeloptimierung an der einen historischen Backtest-Renditereihe leidet unter dem üblichen Data-Snooping-Bias der Parameteroptimierung.
- Der so gefundene Hebel ist für eine andere künftige Realisierung im Allgemeinen nicht optimal.
- Weil Finanzpaniken und Krisen selten sind, ist es leicht, beim Test eines führenden Risikoindikators dem Data-Snooping-Bias zu erliegen.

## Funktionsweise

- Die extremste lineare Prognose gibt allen Koeffizienten denselben Betrag, nicht notwendig dasselbe Vorzeichen. Faktoren werden zuerst mit In-Sample-Daten in Z-Scores verwandelt, z(i) = (f(i) − Mittelwert von f) / Standardabweichung von f.
- Die Prognose der morgigen Rendite ist der historische Mittelwert der Ein-Tages-Renditen plus ihre historische Standardabweichung mal dem Mittel der mit dem Vorzeichen der historischen Korrelation gewichteten Z-Scores. Das ist Gleichung 1.2, eine vereinfachte Fassung des üblichen Faktormodells.
- Kahneman schreibt 2011 in Thinking, Fast and Slow, Formeln mit gleichem Gewicht für alle Prädiktoren seien oft überlegen, weil Zufälle der Stichprobe sie nicht treffen.
- Die Prognose der absoluten Renditen kann ungenau sein. Die der relativen Renditen zwischen Aktien ist oft gut genug: Long die oberste Dezile, Short die unterste, und die durchschnittliche Portfoliorendite ist oft positiv.
- Geht es nur um die Rangfolge, werden je Faktor die Ränge einer Aktie mit dem Vorzeichen der Korrelation zwischen Faktor und erwarteter Aktienrendite multipliziert und über die Faktoren summiert. Die Gleichungen 1.1 und 1.2 entfallen dann.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Out-of-Sample-Tests, Cross-Validation und hohe Sharpe Ratios mindern Data-Snooping-Bias. Keine dieser Praktiken ist maßgeblicher als der Walk-Forward-Test.
- Einfache Modelle sind ein einfaches Heilmittel gegen Data-Snooping-Bias.
- Strategien mit hoher Rendite und niedriger Sharpe Ratio lohnen den Backtest nicht, weil die hohe Rendite wahrscheinlich auf Data-Snooping beruht.
- Die Key Points mahnen, den Data-Snooping-Bias im Blick zu behalten, wenn der Hebel direkt an der zusammengesetzten Wachstumsrate der Backtest-Renditen optimiert wird.
- Dieselbe Mahnung gilt für den Test, ob führende Risikoindikatoren wirken.

## Risiken und Grenzen

- Data Snooping gehört zu den Grundfehlern, die die meisten in Zeitschriften veröffentlichten Arbeiten routinemäßig begehen.
- Der Lookback von 20 Handelstagen für die gleitende Hedge Ratio von GLD und USO ist mit dem Wissen im Nachhinein nahe am Optimum gesetzt.
- δ gleich 0,0001 und Ve gleich 0,001 für den Kalman-Filter sind ebenfalls mit dem Wissen im Nachhinein gewählt; das optimale δ lässt sich aus Trainingsdaten bestimmen.
- Dieselben Daten für die Parameteroptimierung und für den Backtest zu verwenden, ist ein Look-ahead Bias, vor dem Kapitel 1 warnt.
- Im Währungspaar-Beispiel wird ein festes Trainingsfenster von 250 Tagen verwendet, weil es im Nachhinein bessere Ergebnisse liefert, während der Look-back für Mittel und Standardabweichung 20 Tage bleibt.
- Weil die langen Haltedauern in der begrenzten Testhistorie nur wenige Trades erzeugen, besteht in diesen Momentum-Ergebnissen das Risiko eines Data-Snooping-Bias.
- Der eigentliche Test der Strategie ist echtes Out-of-Sample-Testing.

## Beispiele

- Ein Beispielfaktor für ein positives morgiges Indexvorzeichen ist die heutige Rendite: eine positive heutige Rendite sagt eine positive künftige Rendite voraus. Ein weiterer ist die heutige Änderung des VIX: eine negative Änderung sagt eine positive künftige Rendite voraus.
- Greenblatts Zwei-Faktor-Modell von 2006, die Magic Formula, setzt f(1) auf die Kapitalrendite und f(2) auf die Earnings Yield, kauft die 30 bestplatzierten Aktien und hält sie ein Jahr. Die jährliche Prozentrendite war von 1988 bis 2004 30,8 Prozent, gegenüber 12,4 Prozent für den S&P 500.
- Die hohe Durchschnittsrendite einer Strategie mit Sharpe Ratio 0,3 und zwei Jahren Drawdown-Dauer ist wahrscheinlich das Ergebnis von Data-Snooping-Bias. Die lange Drawdown-Dauer macht es außerdem unwahrscheinlich, dass sie eine Cross-Validation besteht.
- Bei einem neuronalen Netz ist die Zahl der mit In-Sample-Daten anzupassenden Parameter proportional zur Zahl der Knoten. Mit etwa 100 Knoten und damit mindestens 100 Parametern lässt sich jede Zeitreihe anpassen und eine Sharpe Ratio von 6 im Backtest erzielen, vorwärts aber mit wenig oder keiner Vorhersagekraft wegen Data-Snooping-Bias.

## Unterschiedliche Quellenpositionen

- Gegen den Einwand, Handelsregeln müssten einfach bleiben, um Data-Snooping-Bias zu vermeiden, sagen Anhänger des Complex Event Processing, sie schürften nicht nach beliebigen Regeln, sondern setzten Regeln um, von denen erfahrene Trader bereits wissen, dass sie profitabel sind. Der Autor ist davon nicht völlig überzeugt.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 134–153 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-008-p134-p153|S. 134–153]]
- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]
- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]

## Verwandte Themen
