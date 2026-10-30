---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Strategien und Ausführung"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# TWAP-Algorithmus


## Kurzdefinition

- Ein TWAP-Algorithmus zerlegt eine große Order in kleine Orders, die in regelmäßigen Zeitabständen eingereicht werden, um einen vorgegebenen zeitgewichteten Durchschnittspreis zu erreichen.
- TWAP steht für Time-Weighted Average Price; gemeint sind Algorithmen, die diesen Preis anstreben.

## Kernaussagen

- Easley et al. (2012) zeigen, wie sich Execution-Algorithmen erkennen lassen, die einen bestimmten TWAP ansteuern.
- Die untersuchte Stichprobe umfasst E-mini-S&P-500-Futures vom 7. November 2010 bis zum 7. November 2011.
- Der Tag wird in 24 Stunden geteilt, und je Stunde wird das in jeder Sekunde gehandelte Volumen über die Minuten hinweg addiert.
- Die größten Volumenkonzentrationen innerhalb einer Minute liegen für fast jede Stunde in den ersten Sekunden.
- Das gilt besonders für 00:00–01:00 GMT um die Eröffnung der asiatischen Märkte, 05:00–09:00 GMT um die Eröffnung britischer und europäischer Aktien, 13:00–15:00 GMT um die Eröffnung der US-Aktien und 20:00–21:00 GMT um den US-Schluss.
- Ein erheblicher Teil der Handelsaktivität fällt in die erste Sekunde jeder Minute und gilt als typisches Zeichen von Handel, der durch TWAP-Algorithmen ausgelöst wird.
- Die bei einmal pro Minute sehr präzise liegende Aktivität werten die Autoren als starke Evidenz, dass TWAP-Algorithmen in diesem Markt eine signifikante Präsenz haben.
- Diese einmal-pro-Minute-Aktivität ist mehr als zehnmal so stark wie die benachbarten Frequenzen.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- Ein dafür genanntes Machine-Learning-Feature prüft das Order-Ungleichgewicht zu Beginn jeder Minute auf eine persistente Komponente.
- Der Text beschreibt, dass sich damit großen institutionellen Investoren zuvorkommen lässt, solange der größere Teil ihrer TWAP-Order noch aussteht.

## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Der Befund stammt aus der Fourier-Analyse der Handelspreise von Erdgas-Futures.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]
- Advances in Financial Machine Learning.pdf, S. 362–381 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-020-p362-p381|S. 362–381]]

## Verwandte Themen
