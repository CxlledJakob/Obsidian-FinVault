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

# Paper Trading


## Kurzdefinition

- Paper Trading ist die Lebenszyklus-Stufe, in der die Strategie auf einem Live-Feed in Echtzeit läuft.

## Kernaussagen

- Die Performance erfasst Latenzen beim Einlesen der Daten, bei der Berechnung und bei der Ausführung sowie weitere Zeitabstände zwischen Beobachtung und Positionierung.
- Paper Trading dauert so lange, bis genug Evidenz vorliegt, dass die Strategie wie erwartet arbeitet.
- Die Stufe folgt auf das Embargo.
- Erst die anschließende Graduation lässt die Strategie eine echte Position führen, allein oder als Teil eines Ensembles.

## Funktionsweise


## Voraussetzungen

- Die Beförderung aus dem Embargo setzt voraus, dass die Performance auf Daten nach dem Backtest-Ende mit den Backtest-Ergebnissen konsistent ist.

## Anwendung im Trading

- Ein Walk-Forward-Test kann in Form von Paper Trading durchgeführt werden.
- Besser wird das Modell mit echtem Geld bei minimalem Hebel gehandelt, damit auch die Aspekte geprüft werden, die selbst dem Paper Trading entgehen.
- Die meisten Trader wären zufrieden, wenn der Live-Handel eine Sharpe Ratio besser als die Hälfte des Backtest-Wertes erzeugt.

## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 20–39 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-002-p020-p039|S. 20–39]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]

## Verwandte Themen
