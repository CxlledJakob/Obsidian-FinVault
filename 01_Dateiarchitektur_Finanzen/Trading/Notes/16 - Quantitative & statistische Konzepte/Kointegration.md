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

## Verwandte Themen
