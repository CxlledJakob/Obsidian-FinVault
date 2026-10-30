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

## Kernaussagen

- Unter der Nullhypothese einer wahren Sharpe Ratio von null ist der erwartete Höchstwert der geschätzten Sharpe Ratios die Vergleichsschwelle der Deflated Sharpe Ratio.
- Die Schwelle steigt schnell mit der Zahl unabhängiger Versuche und mit der Varianz der in diesen Versuchen geschätzten Sharpe Ratios.
- Jedes Backtestergebnis muss zusammen mit allen Versuchen berichtet werden, die zu seiner Erstellung geführt haben.
- Fehlt die Angabe aller Versuche, lässt sich die Wahrscheinlichkeit einer Fehlentdeckung nicht beurteilen.
- Die Überschrift des dritten Gesetzes des Backtesting lautet, dass die meisten Entdeckungen in der Finanzwelt falsch sind, weil die Versuche nicht mitberichtet werden.
- Die Deflated Sharpe Ratio korrigiert die Sharpe Ratio um nichtnormale Renditen, um die Länge der Historie und um Mehrfachtests sowie Selection Bias.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Data Snooping gehört zu den Grundfehlern, die die meisten in Zeitschriften veröffentlichten Arbeiten routinemäßig begehen.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 134–153 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-008-p134-p153|S. 134–153]]
- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]
- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]

## Verwandte Themen
