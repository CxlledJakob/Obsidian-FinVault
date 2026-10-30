---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Validierung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Parameterstabilität


## Kurzdefinition

- Instabilität heißt hier, dass kleine Änderungen der prognostizierten Renditen oder einzelner Matrixeinträge ganz andere Portfolio-Lösungen erzeugen.

## Kernaussagen

- Kleine Abweichungen der prognostizierten Renditen lassen den Critical Line Algorithm sehr unterschiedliche Portfolios erzeugen, wie Michaud (1998) zeigt.
- Der Verzicht auf Renditeprognosen mildert die Instabilität, beseitigt sie aber nicht.
- Die Ursache der verbleibenden Instabilität ist die Inversion einer schlecht konditionierten Kovarianzmatrix.
- Ein vollständiger Graph verstärkt kleine Schätzfehler zu falschen Lösungen.
- Fehlende Hierarchie lässt Gewichte frei variieren und ist eine Wurzel der Instabilität des Critical Line Algorithm.
- Hierarchical Risk Parity stellt die Stabilität der Gewichte wieder her, und die Lösung ist konstruktionsbedingt intuitiv.
- Robustheit, Anschaulichkeit und Flexibilität von Hierarchical Risk Parity folgen daraus, dass keine Kovarianz-Invertierbarkeit verlangt wird.

## Funktionsweise

- Der Nutzer kann Nebenbedingungen einführen oder den Baum verändern, ohne die Suche des Algorithmus zu gefährden.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- CLA-Allokationen reagieren erratisch auf idiosynkratische und auf gemeinsame Schocks.
- Das Inverse-Varianz-Portfolio senkt nach einem Schock die betroffene Anlage und verteilt das Exposure auf alle übrigen, sodass deren Gewichte unabhängig von der Korrelation wachsen.

## Beispiele


## Unterschiedliche Quellenpositionen

- Kolanovic und Koautoren (2017) finden, dass Hierarchical Risk Parity Volatilitätsziele besser trifft als Mean-Variance-Portfolios, und bestätigen die Robustheit in Simulationsstudien.
- Raffinot (2017) bezeichnet hierarchisch geclusterte Portfolios als robust.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 248–267 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-014-p248-p267|S. 248–267]]

## Verwandte Themen
