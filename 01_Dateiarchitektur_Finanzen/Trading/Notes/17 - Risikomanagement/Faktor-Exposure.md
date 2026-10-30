---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/17 - Risikomanagement/17 - Risikomanagement|17 - Risikomanagement]]"
weitere_hauptthemen: []
unterthema: "Portfoliorisiko"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Faktor-Exposure


## Kurzdefinition

- Das Faktor-Exposure ist der Vektor der Faktorladungen aus der Eigenwertzerlegung der Kovarianzmatrix, multipliziert mit dem Allokationsvektor.

## Kernaussagen

- Die Risikoanteile summieren sich zu eins, und jeder Anteil liegt zwischen 0 und 1.
- Wird die Kovarianz auf Preisänderungen statt auf Renditen gerechnet, kann statt der Gewichte ein Bestandsvektor verwendet werden.
- Als Studien Überrenditen TA-basierter Strategien zeigten, erfanden Anhänger der Effizienzmarkthypothese neue Risikofaktoren und behaupteten, die Überrenditen seien nur Ausgleich für Risiken, die gerade dieser Strategie innewohnen.
- Die Effizienzmarkthypothese behauptet nicht, Renditen über dem Markt seien unmöglich, sondern nur, dass höhere Renditen die Übernahme zusätzlichen Risikos verlangen.
- Wären die Renditen der TA-Strategie wirklich Ausgleich für höheres Risiko, bliebe die Effizienzmarkthypothese trotz einer Rendite über dem Marktindex intakt.
- Der Fehler lag darin, den Risikofaktor erst zu konstruieren, nachdem die TA-Studien vorlagen.
- Wissenschaftlich korrekt wäre gewesen, den Risikofaktor vor der Studie zu definieren und vorherzusagen, dass ein Test der TA-Methode scheinbar marktschlagende Renditen erzeugt.
- Stattdessen nahmen sich die Verteidiger die Lizenz, jederzeit einen neuen Risikofaktor zu erfinden, um widersprechende Befunde wegzuerklären, und machten die Hypothese damit unfalsifizierbar.

## Funktionsweise

- Die Kovarianzmatrix der Renditen wird als V mal W gleich W mal Lambda zerlegt, und die Ladungen sind W transponiert mal die Gewichte.
- Die Gewichte summieren sich zu eins.
- Der Risikoanteil einer Hauptkomponente ist ihr quadriertes Loading mal ihrem Eigenwert, geteilt durch die Summe dieser Terme über alle Komponenten.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Dieselbe nachträgliche Immunisierung war schon gegen Studien eingesetzt worden, in denen öffentliche Fundamentaldaten wie das Kurs-Buchwert-Verhältnis und das KGV Überrenditen erzeugten: Niedrige Werte beider Kennzahlen seien nur Signale für Aktien mit abnormal hohem Risiko.
- Diese Risikofaktoren waren vor den Studien nicht definiert worden; nachträglich eigens erfundene Erklärungen dieser Art heißen Ad-hoc-Hypothesen.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 286–305 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-016-p286-p305|S. 286–305]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 134–153 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-008-p134-p153|S. 134–153]]

## Verwandte Themen
