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

# Kointegration


## Kurzdefinition

- Kointegration ist im Engle-Granger-Sinn der Kunstgriff, der eine Regression auf nichtstationären Reihen ermöglicht und dabei das Gedächtnis erhält.
- Kointegration ist der Kunstgriff, der eine Regression auf nichtstationären Reihen ermöglicht, sodass das Gedächtnis erhalten bleibt.

## Kernaussagen

- Kointegrationsverfahren sind unter anderem deshalb wichtig, weil sie Reihen mit Gedächtnis modellieren können.
- Der Text fragt, warum gerade die Null-Differenzierung die besten Ergebnisse liefern sollte, und hält sie für ebenso willkürlich wie die Differenzierung um einen Schritt.
- Zwischen keiner Differenzierung und voller Differenzierung liegt ein weiter Bereich, der sich mit fraktionaler Differenzierung für ein prognosestarkes Modell erkunden lässt.
- Log-Preise haben in diesem Paradigma Gedächtnis und sind nicht stationär.
- Für ML-Prognosen hält der Text den Kointegrations-Kunstgriff für unnötig, weil die Fixed-Width-Fracdiff-Methode Stationarität erreicht, ohne das Gedächtnis aufzugeben.
- Im Engle-Granger-Paradigma haben Log-Preise Gedächtnis und sind nicht stationär.
- Die Fixed-Width-Fracdiff-Methode braucht diesen Kunstgriff für ML-Prognosen nicht, weil Stationarität möglich ist, ohne Gedächtnis und Prognosekraft aufzugeben.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Die Zahl kointegrierter Variablen ist begrenzt, und die kointegrierenden Vektoren sind notorisch instabil.

## Beispiele


## Unterschiedliche Quellenpositionen

- Box-Jenkins behandelt Renditen als stationär, aber gedächtnislos; Engle-Granger behandelt Log-Preise als gedächtnisbehaftet, aber nicht stationär, und nutzt Kointegration, damit die Regression trotzdem geht.
- Der Text stellt Engle-Granger, wo Log-Preise Gedächtnis behalten und nicht stationär sind, dem Box-Jenkins-Bild gegenüber, in dem Renditen stationär und gedächtnislos sind.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 96–115 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-006-p096-p115|S. 96–115]]
- Advances in Financial Machine Learning.pdf, S. 115–134 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-007-p115-p134|S. 115–134]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]

## Verwandte Themen
