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

# Kovarianz


## Kurzdefinition

- Eine nicht singuläre Kovarianzmatrix der Größe N braucht mindestens halb so viele unabhängige und identisch verteilte Beobachtungen, wie das Produkt aus N und N plus 1.

## Kernaussagen

- Quadratische Programmierung verlangt die Inverse einer positiv definiten Kovarianzmatrix, also lauter positive Eigenwerte.
- Die Inversion ist fehleranfällig, wenn die Matrix numerisch schlecht konditioniert ist.
- Für eine invertierbare Matrix der Größe 50 braucht man mindestens fünf Jahre täglicher IID-Daten.
- Eine größere Matrix verschärft das Problem, weil jeder Kovarianzkoeffizient mit weniger Freiheitsgraden geschätzt wird.
- Hierarchical Risk Parity nutzt die Kovarianzmatrix, ohne Invertierbarkeit oder positive Definitheit zu verlangen, und rechnet auch auf einer singulären Matrix.
- Eine Matrix der Größe N entspricht einem vollständigen Graphen mit halb so vielen Kanten, wie das Produkt aus N und N minus 1.
- Eine Kovarianzmatrix von 50 mal 50 hat 50 Knoten und 1225 Kanten.
- Die Wurzel der Instabilität quadratischer Optimierer ist die verlangte Inversion der Kovarianzmatrix.

## Funktionsweise

- Die Quasi-Diagonalisierung ordnet Zeilen und Spalten so, dass die größten Werte auf der Diagonale liegen, ohne einen Basiswechsel.
- Ähnliche Anlagen stehen danach beieinander und unähnliche weit auseinander.
- Die Varianz einer Teilmenge wird als quadratische Form einer Inverse-Varianz-Gewichtung definiert.
- Ist die Kovarianzmatrix diagonal, ist das Minimum-Varianz-Gewicht proportional zum Kehrwert der eigenen Varianz.
- Bei zwei Teilmengen ist der Anteil der ersten Hälfte eins minus der Bruch aus ihrer Varianz und der Summe beider Varianzen.

## Voraussetzungen


## Anwendung im Trading

- Prognostizierte Renditen, Ledoit-Wolf-Shrinkage und Black-Litterman-Sichten lassen sich in den hierarchischen Ansatz einbauen.
- Dieselbe Idee, Matrixinversionen zu vermeiden, kann instabile Verfahren wie VAR oder VECM ersetzen.
- Weitere Einsätze bei fast singulärer Kovarianzmatrix sind die Kapitalallokation auf Manager, algorithmische Strategien, Bagging, Boosting und Random-Forest-Prognosen.

## Regeln und Kriterien


## Risiken und Grenzen

- Mit so vielen Kanten dürfen Gewichte völlig frei umschichten, und kleine Schätzfehler führen zu völlig anderen Lösungen.
- Nebenbedingungen, Black-Litterman-Priors oder eine stabilere Inverse nach Ledoit und Wolf bleiben in Geometrie, linearer Algebra und Analysis und beheben die fehlende Hierarchie nicht.
- Die Annahme einer diagonalen Kovarianzmatrix bringt dem Inverse-Varianz-Portfolio etwas Stabilität, seine Varianz liegt aber weiter über der von Hierarchical Risk Parity.

## Beispiele

- Die Konditionszahl der Kovarianzmatrix im Zahlenbeispiel beträgt 150,9324.
- Außer Stichprobe betragen die Portfoliovarianzen 0,1157 für CLA, 0,0928 für das Inverse-Varianz-Portfolio und 0,0671 für Hierarchical Risk Parity.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 248–267 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-014-p248-p267|S. 248–267]]

## Verwandte Themen
