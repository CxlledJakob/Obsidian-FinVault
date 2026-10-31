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
- Für einen gegebenen Momentumindikator gibt es gewöhnlich verschiedene Einstellungen für verschiedene Märkte und gewöhnlich verschiedene Einstellungen für verschiedene Zeitebenen desselben Marktes.
- Die für die jüngsten Daten eines Marktes und einer Zeitebene gefundenen besten Einstellungen ändern sich.
- Momentumtrends wechseln von niedriger Volatilität mit relativ seltenen Momentumumkehren zu hoher Volatilität mit relativ häufigen Momentumumkehren.
- Gelegentlich werden die Indikatoreinstellungen angepasst, damit sie die jüngste Momentumvolatilität abbilden.
- Sind nach einer Änderung von Trendgeschwindigkeit und Volatilität die früher besten Einstellungen nach einigen Momentumzyklen nicht mehr optimal, kann die Lookback-Periode verkürzt oder vergrößert werden.
- Hat man einen Indikator und einen Einstellungssatz gewählt, bleibt man dabei, bis ein sehr zwingender Grund zur Änderung vorliegt.
- Dieselben zuvor nützlichen Einstellungen blieben über die folgenden Monate nützlich, bis der Aufwärtstrend stärker und die Korrekturen in Zeit und Preis kleiner wurden und der Indikator die Oversold-Zone nicht mehr erreichte.
- Nach einigen weiteren Oszillationen ohne Erreichen der Oversold-Zone auf den Korrekturen würde man wahrscheinlich auf eine kürzere Lookback-Periode wechseln.

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
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 42–61 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-004-p042-p061|S. 42–61]]

## Verwandte Themen
