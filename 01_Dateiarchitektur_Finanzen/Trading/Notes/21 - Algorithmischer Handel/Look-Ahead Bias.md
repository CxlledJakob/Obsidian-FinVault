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

# Look-Ahead Bias


## Kurzdefinition

- Look-ahead Bias heißt, Information zu nutzen, die im Zeitpunkt der simulierten Entscheidung nicht öffentlich war.
- In diesem Kapitel heißt Look-ahead Bias, dass das Backtest-Programm die Preise von morgen benutzt, um die Handelssignale von heute zu bestimmen.

## Kernaussagen

- Fundamentaldaten werden mit Zeitverzug berichtet.
- Die Analyse darf einen Datenpunkt erst verwenden, nachdem er öffentlich verfügbar war.
- Die Annahme, diese Daten seien am Ende der Berichtsperiode veröffentlicht worden, ist ein Anfängerfehler und trifft nie zu.
- Bloomberg indiziert Fundamentaldaten mit dem letzten Datum im Bericht und weist die Werte damit einem Zeitpunkt zu, an dem sie noch nicht bekannt waren.
- Backfilling weist fehlenden Daten einen Wert zu, auch wenn dieser damals unbekannt war.
- Ein nachträglich berichtigter Wert war am Tag der ersten Veröffentlichung nicht bekannt.
- Häufig wird der endgültige Wert auf den Zeitpunkt der ersten Veröffentlichung oder sogar auf den letzten Tag der Berichtsperiode gelegt.
- Nach korrekter zeitlicher Zuordnung lässt sich ein erheblicher Teil der Befunde in der Faktorliteratur nicht mehr reproduzieren.
- Informationsleckage in der Kreuzvalidierung ist eine Falle, und die genannte Lösung sind Purging und Embargoing in den Kapiteln 7 und 9.
- Dieser Zuordnungsfehler und seine Folgen werden bei den Backtesting-Fehlern in Kapitel 11 wieder behandelt.
- Dieselben Daten für die Parameteroptimierung, etwa die beste Hedge Ratio, und für den Backtest zu verwenden, führt Look-ahead Bias ein.
- Kapitel 1 hat vor diesem Fehler und vor dem Weglassen der Transaktionskosten gewarnt; die Prototypen lassen ihn nur der einfacheren Darstellung wegen stehen, und eigene Umsetzungen sollen ihn entfernen.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Für jeden Datenpunkt ist der Zeitstempel sicher zu bestimmen, und Veröffentlichungsdaten, Verteilungsverzögerungen sowie Backfill-Korrekturen sind zu berücksichtigen.
- Sind Backtest- und Live-Programm dasselbe und unterscheiden sich nur die zugeführten Daten, historische Daten gegen Live-Marktdaten, kann im Programm kein Look-ahead Bias entstehen.
- Welche Plattformen denselben Quellcode für Backtest und Live-Ausführung erlauben, wird später im Kapitel gezeigt.
- Eine Plattform, die dasselbe Programm für Backtest und Live-Ausführung nutzt, kann Look-ahead Bias beseitigen.
- Spezialplattformen speisen historische Marktdaten Tick für Tick oder Bar für Bar in die Trade-Engine, genau wie Live-Marktdaten. Zukunftsinformation kann dadurch nicht als Eingabe verwendet werden.
- Das ist ein Hauptvorteil einer Spezial-Handelsplattform.

## Risiken und Grenzen

- Look-ahead Bias ist die zweite der sieben Sünden des quantitativen Investierens bei Luo et al. 2014, und die meisten in Zeitschriften veröffentlichten Arbeiten begehen solche Grundfehler routinemäßig.
- Look-ahead Bias ist im Wesentlichen ein Programmierfehler. Er kann nur ein Backtest-Programm befallen, kein Live-Handelsprogramm, weil ein Live-Programm keine Zukunftsinformation beschaffen kann.
- Look-ahead Bias meint hier, künftige, zum damaligen Zeitpunkt unwissbare Information fälschlich als Teil der historischen Dateneingabe in die Backtest-Engine aufzunehmen.
- Der leichte Wechsel zwischen Backtest und Live-Ausführung beseitigt auch Abweichungen beim Übertragen einer Backtest-Strategie in eine Live-Strategie, wie sie Programme in allgemeinen Sprachen von C++ bis MATLAB oft plagen.
- Wegen dieses Look-ahead Bias, fehlender Transaktionskosten und unbegrenzten Kapitals empfiehlt der Autor das Beispiel nicht als praktische Handelsstrategie.

## Beispiele

- Bei Bloomberg liegt das letzte im Bericht enthaltene Datum oft etwa 1,5 Monate vor dem Veröffentlichungstag.
- Für eine vierteljährliche BIP-Meldung liegen typischerweise drei Werte vor: der ursprünglich veröffentlichte Wert und zwei monatliche Revisionen.
- Ein häufiges Beispiel ist, das Tageshoch oder Tagestief zu benutzen, um das Einstiegssignal noch am selben Tag im Backtest zu setzen. Vor Handelsschluss sind Hoch und Tief des Tages nicht bekannt.
- In der linearen Mean-Reversion-Strategie auf USD.CAD entsteht Look-ahead Bias, weil die Halbwertszeit und damit der Lookback an denselben Daten bestimmt werden, auf denen die Strategie ausgewertet wird.
- Der Lookback von 20 Handelstagen für die Hedge Ratio von GLD und USO ist mit dem Wissen im Nachhinein nahe am Optimum gesetzt.
- δ gleich 0,0001 und Ve gleich 0,001 des Kalman-Filters sind mit demselben Wissen im Nachhinein gewählt, obwohl das optimale δ aus Trainingsdaten kommen soll.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 39–58 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-003-p039-p058|S. 39–58]]
- Advances in Financial Machine Learning.pdf, S. 115–134 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-007-p115-p134|S. 115–134]]
- Advances in Financial Machine Learning.pdf, S. 134–153 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-008-p134-p153|S. 134–153]]
- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 20–39 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-002-p020-p039|S. 20–39]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 153–172 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-009-p153-p172|S. 153–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]

## Verwandte Themen
