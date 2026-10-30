---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/07 - Orderflow & Market Microstructure/07 - Orderflow & Market Microstructure|07 - Orderflow & Market Microstructure]]"
weitere_hauptthemen: []
unterthema: "Mikrostruktur"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Quote Stuffing


## Kurzdefinition

- Quote Stuffers überfluten eine Börse mit Nachrichten, allein um konkurrierende Algorithmen zu verlangsamen, und betreiben damit Latency Arbitrage.

## Kernaussagen

- Die Konkurrenten müssen Nachrichten parsen, von denen nur die Urheber wissen, dass sie ignoriert werden können.
- Easley et al. (2012) nennen daneben Quote Danglers, Liquidity Squeezers und Pack Hunters als weitere predatäre Algorithmen.
- Diese Algorithmen nutzen Quotestornierungen und verschiedene Ordertypen, um Market Maker advers zu selektieren.
- Sie hinterlassen unterschiedliche Signaturen im Handelsprotokoll.
- Hohe Quotestornierungsraten können auf geringe Liquidität hindeuten, weil Quotes veröffentlicht werden, die nicht ausgeführt werden sollen.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- Die Raten von Quotestornierung, Limit Orders und Market Orders können die Grundlage für Features sein, die auf die Absichten dieser Algorithmen hinweisen.

## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]

## Verwandte Themen
