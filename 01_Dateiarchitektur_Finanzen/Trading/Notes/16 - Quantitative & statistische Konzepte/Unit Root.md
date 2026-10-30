---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Zeitreihen"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Unit Root


## Kurzdefinition

- Right-Tail-Unit-Root-Tests prüfen exponentielles Wachstum oder Kollaps unter einer autoregressiven Spezifikation.

## Kernaussagen

- Enthält die Reihe eine Unit Root, dann ist der kleinste Fixed-Width-Fracdiff-Koeffizient d*, der sie stationär macht, kleiner als 1.
- Ist die Reihe bereits stationär, gilt d* gleich 0. Zeigt sie explosives Verhalten wie in einer Blase, gilt d* größer als 1.
- Der besonders interessierende Fall ist d* wenig über 0 und weit unter 1. Die Originalreihe ist dann nur mild nichtstationär: Differenzierung ist nötig, eine volle ganzzahlige Differenzierung entfernt aber zu viel Gedächtnis und Prognosekraft.
- Die Null des Chow-Typ-Dickey-Fuller-Tests ist ein Unit Root mit Rho gleich 1, die Alternative ein explosiver Prozess mit Rho größer als 1 nach dem Bruch.
- Standard-Unit-Root- und Kointegrationstests erkennen Blasen schlecht, weil periodisch zusammenbrechende Blasen eher wie ein Unit-Root- oder stationärer autoregressiver Prozess aussehen.
- Im Null-Lag-Modell auf Logpreisen ist Beta gleich 0 der Unit-Root-Zustand: das System ist nichtstationär und verhält sich als Martingal.
- Der gewöhnliche ADF-Test ist der Spezialfall von SADF, bei dem die minimale Fensterlänge gleich Endpunkt minus 1 ist.
- SADF testet auf der ADF-Regression mit Konstante und Lag-Differenzen die Null Beta kleiner oder gleich 0 gegen die Alternative Beta größer als 0.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Phillips, Wu und Yu (2011) sagen, Standard-Unit-Root-Tests können einen stationären Prozess und ein periodisch zusammenbrechendes Blasenmodell nicht wirksam unterscheiden.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 96–115 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-006-p096-p115|S. 96–115]]
- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]

## Verwandte Themen
