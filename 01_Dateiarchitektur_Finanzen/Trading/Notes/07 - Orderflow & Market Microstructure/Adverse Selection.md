---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/07 - Orderflow & Market Microstructure/07 - Orderflow & Market Microstructure|07 - Orderflow & Market Microstructure]]"
weitere_hauptthemen: []
unterthema: "Mikrostruktur"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Adverse Selection


## Kurzdefinition

- Adverse Selection trifft Market Maker, die Liquidität an informierte Händler geben, wenn das Order-Flow-Ungleichgewicht zugleich anhaltend und für sie kaum vorhersagbar ist.
- Adverse Selection bezeichnet hier, dass Market Maker von informierten Händlern zu ihrem Nachteil ausgewählt werden.

## Kernaussagen

- Ein anhaltendes Order-Flow-Ungleichgewicht ist eine notwendige, aber nicht hinreichende Bedingung für Adverse Selection.
- Liegt die Prognose des Ungleichgewichts richtig, werden Market Maker nicht advers selektiert, auch wenn der Betrag des Ungleichgewichts deutlich über 0 liegt.
- Die Wahrscheinlichkeit der Adverse Selection hängt davon ab, wie unvorhersagbar das Order-Flow-Ungleichgewicht ist.
- Die Redundanz einer Folge bestimmt ihre verlustfreie Komprimierbarkeit, ihre Kolmogorov-Komplexität und damit ihre Vorhersagbarkeit.
- Entropie charakterisiert diese Redundanz und damit die Unvorhersagbarkeit für Market Maker.
- Die PIN-Theorie beschreibt Market Maker als Verkäufer der Option, von informierten Händlern advers selektiert zu werden.
- Der Bid-Ask-Spread ist die Prämie, die Market Maker für diese Option verlangen.
- Predatory Algorithms nutzen Quotestornierungen und verschiedene Ordertypen, um Market Maker advers zu selektieren.
- Bei asymmetrisch informierten Händlern liefern Market Maker uninformierte Prognosen, gemessen an hohem Cross-Entropy-Verlust, und werden advers selektiert.
- Mikrostrukturelle Information lässt sich nur relativ zur Prognosekraft der Market Maker definieren und messen.

## Funktionsweise

- In Volumenbars wird der Kaufanteil bestimmt, über q-Quantile in disjunkte Teilmengen quantisiert und die so entstandene Nachricht mit Kontoyiannis' Lempel-Ziv-Algorithmus auf ihre Entropie geschätzt.
- Die Zeitreihe der kumulativen Verteilungsfunktion dieser Entropie ist das Merkmal zur Prognose von Adverse Selection.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Am Flash Crash vom 6. Mai 2010 hätten Market Maker am steigenden Cross-Entropy-Verlust informierte Händler und eine gefährlich steigende Wahrscheinlichkeit adverser Selektion erkennen können.
- Der Crash entstand durch die Anhäufung tausender Prognosefehler.
- Market Maker hatten erwartet, passive Quotes auf dem Bid ausführen und auf höherem Niveau zurückverkaufen zu können.
- Sie stellten Verkäufern weiter Liquidität zu übermäßig großzügigen Kursen, bis ein Stop-out eine Liquiditätskrise auslöste.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 286–305 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-016-p286-p305|S. 286–305]]
- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]

## Verwandte Themen
