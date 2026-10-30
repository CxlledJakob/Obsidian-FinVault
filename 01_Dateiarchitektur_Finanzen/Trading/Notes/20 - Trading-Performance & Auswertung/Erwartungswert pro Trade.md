---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/20 - Trading-Performance & Auswertung/20 - Trading-Performance & Auswertung|20 - Trading-Performance & Auswertung]]"
weitere_hauptthemen: []
unterthema: "Renditekennzahlen"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Erwartungswert pro Trade


## Kurzdefinition

- Bei einer symmetrischen Auszahlung von plus a oder minus a ist der erwartete Gewinn einer Wette a mal (2p minus 1).

## Kernaussagen


## Funktionsweise

- Die Varianz einer symmetrischen Wette mit den Auszahlungen plus a und minus a ist 4 mal a zum Quadrat mal p mal (1 minus p).
- Bei einer asymmetrischen Auszahlung ist der Erwartungswert die Trefferwahrscheinlichkeit mal der Gewinnauszahlung plus die Gegenwahrscheinlichkeit mal der Verlustauszahlung.
- Die Varianz ist dann das Quadrat der Spanne zwischen Gewinnauszahlung und Verlustauszahlung, mal p mal (1 minus p).
- Ist die Verlustauszahlung das Negative der Gewinnauszahlung, fällt die Formel der Sharpe Ratio auf den symmetrischen Fall zurück.
- Im symmetrischen Fall kürzt sich die Auszahlungshöhe aus der Sharpe Ratio heraus.
- Bei n unabhängigen Wetten pro Jahr geht der Erwartungswert mit dem Faktor n und die Streuung mit der Wurzel aus n in die annualisierte Sharpe Ratio ein.

## Voraussetzungen

- Die Herleitung setzt unabhängig und identisch verteilte Wetten voraus.

## Anwendung im Trading

- Gewinn- und Verlustmittel können statt als einfache Mittel auch aus einer Mischung zweier Gaußverteilungen mit dem EF3M-Algorithmus geschätzt werden.

## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]

## Verwandte Themen
