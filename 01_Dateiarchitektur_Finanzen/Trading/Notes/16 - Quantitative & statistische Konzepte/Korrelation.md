---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Statistik"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Korrelation


## Kurzdefinition

- Die Korrelation zum Underlying ist die Korrelation der Strategierenditen mit den Renditen des zugrunde liegenden Anlageuniversums.
- Die Konditionszahl einer Korrelationsmatrix ist der Betrag des Verhältnisses aus betragsmäßig größtem und kleinstem Eigenwert.

## Kernaussagen

- Eine deutlich positive oder deutlich negative Korrelation zum Underlying bedeutet, dass die Strategie das Anlageuniversum im Wesentlichen hält oder leerverkauft und darüber hinaus wenig eigenen Wert hinzufügt.
- Eine diagonale Korrelationsmatrix hat die niedrigste Konditionszahl und ist ihre eigene Inverse.
- Kommen korrelierte, multikollineare Anlagen hinzu, steigt die Konditionszahl, der größte Eigenwert wächst und der kleinste sinkt.
- Ab einer hohen Konditionszahl machen numerische Fehler die Inverse instabil, sodass eine kleine Änderung eines Eintrags eine ganz andere Inverse ergibt.
- Eine Korrelationsmatrix misst die Kosinus der Winkel zwischen je zwei Vektoren im Raum der Renditezeitreihen.
- Korrelationsmatrizen kennen keine Hierarchie, denn jede Anlage ist ein potenzieller Ersatz für jede andere.
- Pearsons Korrelation ist nicht die einzige, die erfüllt, dass die Kovarianz gleich Korrelation mal den beiden Standardabweichungen ist.
- Die Distanz als Quadratwurzel aus der Hälfte der Differenz von eins und der Korrelation ist eine echte Metrik, weil sie ein Vielfaches des euklidischen Abstands nach Z-Standardisierung ist.
- Die Quadratwurzel aus der Differenz von eins und dem Betrag der Korrelation ist eine echte Metrik auf dem Quotienten der ganzen Zahlen modulo 2.
- Korrelationsstrukturen bleiben über lange Zeiträume nicht invariant.

## Funktionsweise

- Hierarchical Risk Parity kodiert die Korrelation als Distanz und clustert darüber, statt bei der Inversion die partiellen Korrelationen des vollständigen Graphen auszuwerten.
- Das illustrierte Linkage-Kriterium ist der nearest-point-Algorithmus, also die kleinste Distanz zwischen einem Punkt und dem neuen Cluster.
- Auf einen idiosynkratischen Schock senkt Hierarchical Risk Parity die betroffene Anlage und erhöht eine korrelierte, nicht betroffene Anlage.
- Auf einen gemeinsamen Schock senkt es die betroffenen Anlagen und erhöht unkorrelierte Anlagen mit geringerer Varianz.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Je korrelierter die Anlagen sind, desto nötiger ist Diversifikation und desto wahrscheinlicher werden instabile Lösungen.
- Das Inverse-Varianz-Portfolio ignoriert die Korrelationsstruktur und ist dadurch anfällig für systemische Schocks.
- Schocks auf mehrere korrelierte Anlagen bestrafen genau diese Unkenntnis der Korrelationsstruktur.
- Eine Hauptkomponentenanalyse auf einem großen Rentenuniversum leidet unter denselben Nachteilen wie CLA, weil Verfahren für kleine Datenmengen die Hierarchie nicht erkennen.

## Beispiele

- Aus den Korrelationen 0,7, 0,2 und minus 0,2 werden die Distanzen 0,3873, 0,6325 und 0,7746.
- Eine dargestellte Korrelationsmatrix von Rentenpapieren umfasst nach dem Clustering über 2,1 Millionen Einträge.
- Zwischen dem ersten und zweiten Rebalancing trifft eine Anlage ein idiosynkratischer Schock, zwischen dem fünften und sechsten zwei Anlagen ein gemeinsamer Schock.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Advances in Financial Machine Learning.pdf, S. 248–267 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-014-p248-p267|S. 248–267]]

## Verwandte Themen
