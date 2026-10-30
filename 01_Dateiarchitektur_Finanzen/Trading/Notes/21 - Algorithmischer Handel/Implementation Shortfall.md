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

# Implementation Shortfall


## Kurzdefinition

- Implementation Shortfall erfasst, wie Ausführungskosten das Ergebnis einer Strategie belasten.
- Die Rendite auf die Ausführungskosten ist die Dollar-Performance einschließlich Brokergebühren und Slippage, geteilt durch die gesamten Ausführungskosten.

## Kernaussagen

- Strategien scheitern oft an falschen Annahmen über die Ausführungskosten.
- Die Brokergebühren je Umschlag sind die an den Broker gezahlten Gebühren einschließlich der Börsengebühren.
- Der durchschnittliche Slippage je Umschlag sind die Ausführungskosten eines Portfolioumschlags ohne die Brokergebühren.
- Die Dollar-Performance je Umschlag setzt die Dollar-Performance einschließlich Gebühren und Slippage ins Verhältnis zu den gesamten Portfolioumschlägen.
- Die Dollar-Performance je Umschlag zeigt, wie viel teurer die Ausführung werden dürfte, bevor der Überschuss der Strategie aufgezehrt ist.
- Die Brokergebühren je Umschlag schließen die Börsengebühren ein.
- Der durchschnittliche Slippage je Umschlag sind die Ausführungskosten ohne die Brokergebühren.
- Dazu gehört der Kauf zu einem Fill-Preis über dem Mittelpreis in dem Moment, in dem die Order an den Broker geht.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Die Rendite auf die Ausführungskosten soll ein großes Vielfaches sein, sodass die Strategie eine schlechtere Ausführung überlebt.

## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]

## Verwandte Themen
