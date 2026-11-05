---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/17 - Risikomanagement/17 - Risikomanagement|17 - Risikomanagement]]"
weitere_hauptthemen: []
unterthema: "Portfoliorisiko"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Positionskorrelation


## Kurzdefinition

- Die Korrelation der Positionen geht in das gemeinsame VaR ein: das Gesamt-VaR zweier Long-Positionen ist die Wurzel aus VaR1 zum Quadrat plus VaR2 zum Quadrat plus 2 ρ mal VaR1 mal VaR2.

## Kernaussagen

- Das Beispiel hält je 1 Million Dollar long in Cisco Systems und in Intel. Gerechnet wird das tägliche 5-Prozent-VaR aus Tages-Logrenditen vom 2. Januar 1991 bis 31. Dezember 1999.
- Drei Korrelationen werden verwendet: die Stichprobenkorrelation 0,473, die gemeinsam geschätzte konstante Korrelation 0,475 und die prognostizierte zeitvariable Korrelation 0,345 am Ursprung t gleich 2275.
- Die zugehörigen Gesamt-VaR betragen 57.117 Dollar, 58.180 Dollar und 57.648 Dollar. Die Spanne ist etwa 1.100 Dollar.
- Die Einzel-VaR betragen univariat 27.360 Dollar für Cisco und 38.840 Dollar für Intel, bei konstanter Korrelation 30.432 und 37.195 Dollar, bei zeitvariabler Korrelation 30.504 und 39.512 Dollar.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Nach dem Einfaktor-Marktmodell bleiben zwischen den 13 Aktien große residuale Kreuzkorrelationen, darunter 0,45 zwischen Caterpillar und Alcoa und 0,48 zwischen General Motors und Ford.
- Im BARRA-Modell mit drei Branchenfaktoren ist die modellierte Korrelation innerhalb der Branche höher als die Stichprobenkorrelation. Caterpillar und Procter & Gamble korrelieren in der Stichprobe mit 0,1 und im angepassten Modell mit 0,6.
- Die zweite Hauptkomponente der fünf Monatsrenditen von IBM, Hewlett-Packard, Intel, J.P. Morgan Chase und Bank of America trennt die Technologiewerte von den Finanzwerten und wird als Branchenkomponente gelesen. Die erste ist eine ungefähr gleich gewichtete Marktkomponente.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 495–514 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-027-p495-p514|S. 495–514]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 514–533 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-028-p514-p533|S. 514–533]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 571–590 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-031-p571-p590|S. 571–590]]

## Verwandte Themen
