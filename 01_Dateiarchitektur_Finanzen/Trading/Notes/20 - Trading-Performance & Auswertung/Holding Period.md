---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/20 - Trading-Performance & Auswertung/20 - Trading-Performance & Auswertung|20 - Trading-Performance & Auswertung]]"
weitere_hauptthemen: []
unterthema: "Trade-Auswertung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Holding Period


## Kurzdefinition

- Jede Wette hat eine Haltedauer vom Zeitpunkt ihrer Entstehung bis zu dem Zeitpunkt t1, an dem die erste Barriere berührt wird.
- Die durchschnittliche Haltedauer ist die mittlere Zahl der Tage, über die eine Wette gehalten wird.

## Kernaussagen

- Hochfrequente Strategien können eine Position nur Bruchteile von Sekunden halten, niederfrequente Strategien über Monate oder Jahre.
- Kurze Haltedauern können die Kapazität der Strategie begrenzen.
- Die Haltedauer hängt mit der Wettfrequenz zusammen und ist von ihr verschieden.
- Eine Strategie kann einmal im Monat wetten, etwa zur Veröffentlichung der Nonfarm Payrolls, und jede Wette nur wenige Minuten halten.

## Funktionsweise

- Eine Wette gilt zu einem Zeitpunkt loc als aktiv, wenn sie vor oder bei loc eröffnet wurde und loc vor ihrem Endzeitpunkt liegt oder das Ende noch unbekannt ist.
- Die Prognose zur Barriere i impliziert einen prognostizierten Preis zum Ende der Haltedauer, und im Intervall bis zu diesem Ende schwankt der Marktpreis, während weitere Prognosen entstehen können.
- Der Schätzer bildet die mittlere Haltedauer in Tagen über die Einstiegszeitpunkte.
- Wird eine bestehende Position vergrößert, wird die Einstiegszeit mit der Positionsgröße neu gewichtet.
- Wird die Position verkleinert, geht die seit dem Einstieg verstrichene Zeit mit dem geschlossenen Umfang in den Durchschnitt ein.
- Beim Drehen der Position wird die Haltedauer der alten Seite mit deren absolutem Umfang festgehalten, und die Einstiegszeit wird neu gesetzt.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 153–172 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-009-p153-p172|S. 153–172]]
- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]

## Verwandte Themen
