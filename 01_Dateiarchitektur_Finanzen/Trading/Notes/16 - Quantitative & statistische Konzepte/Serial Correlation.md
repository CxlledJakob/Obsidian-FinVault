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

# Serial Correlation


## Kurzdefinition


## Kernaussagen

- Serielle Bedingtheit der Labels macht die gewöhnliche k-Fold-Cross-Validation unbrauchbar, weil die Zufallsziehung redundante Beobachtungen sowohl ins Trainings- als auch ins Testset streut.
- Deshalb braucht es ein Validierungsverfahren, das das Modell an den Beobachtungen bewertet, die am wenigsten mit den Trainingsbeobachtungen korreliert oder redundant sind.
- Bei langreichweitiger serieller Abhängigkeit genügt es nicht, eine Beobachtung hinter dem Ende des Trainingssets zu testen, um Informationsleakage zu vermeiden.
- Toth et al. (2011) untersuchen den signierten Orderflow von Aktien der London Stock Exchange und finden über viele Tage positiv autokorrelierte Orderzeichen.
- Die zwei von ihnen geprüften Erklärungen sind Herding und Order Splitting.
- Auf Zeitskalen von weniger als einigen Stunden geht die Persistenz überwiegend auf Order Splitting zurück.
- Die Mikrostrukturtheorie führt die Persistenz des Orderflow-Ungleichgewichts auf die Anwesenheit informierter Händler zurück.
- Die Stärke dieser Persistenz lässt sich über die serielle Korrelation der signierten Volumina messen.
- Ein solches Feature ergänzt die Features der sequenziellen Handelsmodelle in Abschnitt 19.5.
- Das Roll-Modell nimmt serielle Unabhängigkeit der Aggressorzeichen an, E[bt bt−1] = 0.
- Die halbe Geld-Brief-Spanne ergibt sich dort aus der seriellen Kovarianz der Preisänderungen, c = √max{0, −σ[Δpt, Δpt−1]}.
- Empirisch weisen Finanzzeitreihen serielle Abhängigkeit auf.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]
- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]

## Verwandte Themen
