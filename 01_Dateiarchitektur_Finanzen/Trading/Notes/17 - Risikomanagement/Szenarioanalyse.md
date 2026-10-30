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
aktualisiert: 2026-10-30
---

# Szenarioanalyse


## Kurzdefinition


## Kernaussagen

- Statt der Geschichte sollen Szenarien simuliert werden, denn ein gewöhnlicher Backtest ist eine historische Simulation und lässt sich leicht überfitten.
- Die Geschichte ist nur der realisierte Zufallspfad und hätte völlig anders sein können.
- Eine Strategie soll unter einer breiten Spanne von Szenarien profitabel sein, nicht nur auf dem anekdotischen historischen Pfad.
- Das Ergebnis von Tausenden Was-wäre-wenn-Szenarien zu überfitten ist schwerer.
- Vergangene Beobachtungen lassen sich auch dazu nutzen, Szenarien zu simulieren, die in der Vergangenheit nicht eingetreten sind; dieser weitere Gebrauch ist viel weniger bekannt als die historische Simulation.
- Das Ziel der Backtest-Cross-Validation ist nicht historisch genaue Performance, sondern künftige Leistung aus einer Reihe von Out-of-Sample-Szenarien.
- Die Cross-Validation prüft k alternative Szenarien, von denen nur eines der historischen Folge entspricht.
- Das CV-Ergebnis zeigt nicht, wie die Strategie in der Vergangenheit gelaufen wäre, sondern wie sie künftig unter verschiedenen Stressszenarien abschneiden kann.

## Funktionsweise

- Eine Antwort auf die Frage nach einem Stressszenario ist, die Beobachtungen in ein Testset mit dem gewünschten Zeitraum und ein Trainingsset mit dem Rest zu teilen.
- Für jeden Zeitraum des Backtests wird die Leistung eines Klassifikators simuliert, der alles außer diesem Zeitraum kannte.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Anleger fragen oft, wie eine Strategie in einem Stressszenario abgeschnitten hätte, das so unvorhersehbar war wie die Krise 2008, die Dotcom-Blase, der Taper Tantrum oder der China-Schrecken 2015 bis 2016.
- Ein Klassifikator, trainiert vom 1. Januar 2009 bis 1. Januar 2017 und getestet vom 1. Januar 2008 bis 31. Dezember 2008, liefert für 2008 keine historisch genaue Leistung, weil das Training Daten nutzt, die erst nach 2008 verfügbar waren.
- Das Ziel dieses Tests war, eine Strategie, die 2008 nicht kannte, einem Stressszenario wie 2008 auszusetzen.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]

## Verwandte Themen
