---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/18 - Positionsmanagement/18 - Positionsmanagement|18 - Positionsmanagement]]"
weitere_hauptthemen: []
unterthema: "Trade Management"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Scaling Out


## Kurzdefinition

- Scaling-in-Strategien skalieren auch schrittweise aus und warten mit der Gewinnmitnahme nicht, bis der Preis vollständig zum Mittel zurückgekehrt ist.

## Kernaussagen


## Funktionsweise

- Schon eine kleine Rückkehr lässt sich realisieren, deshalb kann die Strategie profitabel bleiben, auch wenn die Reihe nicht wirklich stationär ist und nie zum Mittel zurückkehrt.
- Bei großen Größen senkt das schrittweise Aussteigen zusammen mit dem schrittweisen Einsteigen die Marktauswirkung.
- Mit mehreren Bollinger-Bändern liegen die Ausstiege bei 0, 1, 2 bis N minus 1 Standardabweichungen, passend zu den Einstiegen 1, 2, 3 bis N.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- In der Modellrechnung von Schoenberg und Corwin werden alle Kontrakte erst bei F geschlossen, es gibt also kein average-out, selbst wenn average-in benutzt wurde.
- Auch der Ausstieg an zwei oder mehr Bollinger-Bändern ist im Backtest nie optimal, solange die Wahrscheinlichkeit eines tieferen Einbruchs konstant ist.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]

## Verwandte Themen
