---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/17 - Risikomanagement/17 - Risikomanagement|17 - Risikomanagement]]"
weitere_hauptthemen: []
unterthema: "Portfoliorisiko"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Konzentrationsrisiko


## Kurzdefinition

- Konzentrationsrisiko entsteht, wenn ein Optimierer das Gewicht auf wenige Anlagen bündelt und das Portfolio dadurch idiosynkratischen Schocks aussetzt.
- Die entropieinspirierte Portfoliokonzentration nach Meucci (2009) ist eins minus das Produkt aus dem Kehrwert von N und der Exponentialfunktion der negativen Summe der Produkte aus Risikoanteil und Logarithmus des Risikoanteils.

## Kernaussagen

- Quadratische Optimierer und insbesondere Markowitz' Critical Line Algorithm leiden unter Instabilität, Konzentration und Underperformance.
- Die extreme Konzentration des Critical Line Algorithm wird durch das Ziel getrieben, das Portfoliorisiko zu minimieren.
- Im Zahlenbeispiel liegen 92,66 Prozent des CLA-Gewichts auf den fünf größten Positionen, bei Hierarchical Risk Parity nur 62,57 Prozent.
- CLA setzt drei Anlagen auf Gewicht null und verwirft damit einen großen Teil des Universums zugunsten einer geringen Risikoreduktion.
- Ohne die Schranke, dass Gewichte nicht negativ werden, wären diese drei Allokationen negativ gewesen.
- Die Konditionszahl der Beispiel-Kovarianzmatrix beträgt nur 150,9324 und ist damit für CLA nicht besonders ungünstig.
- Kolanovic und Koautoren (2017) berichten für Hierarchical Risk Parity weniger extreme Gewichte und Risikoallokationen.
- Der Risikoanteil jeder Hauptkomponente liegt zwischen 0 und 1, und die Anteile summieren sich zu eins.
- Der Risikoanteil ist keine Wahrscheinlichkeit, die Verbindung zur Entropie läuft über den verallgemeinerten Mittelwert.
- Die Risikoanteile stammen aus der Zerlegung von Bailey und López de Prado (2012).

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Ein Schock auf eine einzelne Anlage bestraft die Konzentration von CLA.
- Stress bei den fünf größten CLA-Positionen trifft das Portfolio stärker als dasselbe Ereignis bei Hierarchical Risk Parity.
- CLA-Allokationen reagieren erratisch auf idiosynkratische und gemeinsame Schocks.
- Werden Rebalancing-Kosten berücksichtigt, wäre die CLA-Performance sehr negativ gewesen.

## Beispiele

- Die Standardabweichungen im Zahlenbeispiel sind ähnlich, 0,4486 für CLA und 0,4640 für Hierarchical Risk Parity, obwohl CLA die Hälfte des Anlageuniversums verwirft.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 248–267 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-014-p248-p267|S. 248–267]]
- Advances in Financial Machine Learning.pdf, S. 286–305 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-016-p286-p305|S. 286–305]]

## Verwandte Themen
