---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Modelle"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Principal Component Analysis


## Kurzdefinition

- PCA-Gewichte sind ein Allokationsvektor, dessen Risiken einer vorgegebenen Verteilung über die Hauptkomponenten der Kovarianz folgen.
- Die Hauptkomponentenanalyse erzeugt aus standardisierten Features orthogonale Merkmale und dient hier dazu, lineare Substitutionseffekte vor der Feature-Importance-Analyse abzumildern.
- Die Hauptkomponentenanalyse zerlegt hier die Kovarianzmatrix der Renditen in Eigenvektoren und Eigenwerte, V mal W gleich W mal Lambda.
- Die orthogonalen Hauptkomponenten, die einen vorgegebenen Anteil der Gesamtvarianz erklären, sind das Produkt P = Z W̃ aus der Datenmatrix Z und ausgewählten Eigenvektoren.

## Kernaussagen

- Bei einer Inverse-Varianz-Allokation tragen fast alle Hauptkomponenten Risiko, auch die beiden Komponenten mit der höchsten Varianz.
- Im PCA-Portfolio trägt nur die Komponente mit der niedrigsten Varianz Risiko.
- Ein Substitutionseffekt liegt vor, wenn die geschätzte Wichtigkeit eines Features durch andere verwandte Features sinkt; das ist das ML-Analogon zur Multikollinearität.
- Ein Weg, lineare Substitutionseffekte zu behandeln, ist eine PCA auf den Rohfeatures und die anschließende Feature-Importance-Analyse auf den orthogonalen Features.
- Eine Orthogonalisierung wie die PCA verhindert nicht alle Substitutionseffekte, soll aber zumindest lineare Substitutionseffekte abmildern.
- PCA bewertet Features ohne Labelkenntnis, also ohne Overfitting im Sinne einer Klassifikation.
- Wählt MDI, MDA oder SFI dieselben Features, die PCA als prinzipiell einstuft, spricht das dagegen, dass das Muster vollständig überfittet ist.
- Die Risikoanteile summieren sich zu eins und liegen jeweils zwischen 0 und 1.
- Auf diesen Anteilen setzt Meucci (2009) die entropieinspirierte Konzentrationskennzahl auf.

## Funktionsweise

- Ausgangspunkt ist ein IID-multivariater Gauß-Prozess mit Mittelwertvektor und Kovarianzmatrix, etwa für Aktienrenditen, Änderungen von Anleiherenditen oder Änderungen von Optionsvolatilitäten.
- Die Spektralzerlegung sortiert die Eigenvektoren so, dass die Eigenwerte auf der Diagonalen absteigend geordnet sind.
- Das Portfoliorisiko ist das Quadrat von Sigma gleich Omega transponiert mal Kovarianz mal Omega und zugleich Beta transponiert mal Lambda mal Beta.
- Beta ist die Projektion der Allokation auf die orthogonale Basis.
- Der Risikoanteil der n-ten Komponente ist das Produkt aus dem Quadrat von Beta n und dem Eigenwert n, geteilt durch die Portfoliovarianz, und die Anteile summieren sich zu 1.
- In der orthogonalen Basis ist Beta n gleich Sigma mal der Quadratwurzel aus dem Quotienten von vorgegebenem Risikoanteil und Eigenwert.
- In der ursprünglichen Basis ist die Allokation das Produkt aus der Eigenvektormatrix und Beta.
- Ein Umskalieren der Allokation skaliert nur Sigma und lässt die Risikoverteilung unverändert.
- Ist keine Risikoverteilung vorgegeben, liegt das gesamte Risiko auf der Hauptkomponente mit dem kleinsten Eigenwert.
- Die Gewichte sind dann der letzte Eigenvektor, skaliert auf das Zielrisiko.
- Zuerst wird die standardisierte Matrix Z gebildet, indem jedes Feature um seinen Mittelwert zentriert und durch seine Standardabweichung geteilt wird.
- Danach werden Eigenwerte und Eigenvektoren so bestimmt, dass Z′ZW = WΛ gilt, wobei Λ eine absteigend sortierte Diagonalmatrix und W eine orthonormale Matrix ist.
- Die orthogonalen Features sind P = ZW, und ihre Orthogonalität folgt daraus, dass P′P = Λ ist.
- Die Diagonalisierung erfolgt auf Z statt auf X, weil die Zentrierung die erste Hauptkomponente in die Hauptrichtung der Beobachtungen ausrichtet, analog zu einem Intercept in der linearen Regression.
- Das Reskalieren lenkt die PCA auf Korrelationen statt auf Varianzen; ohne Reskalierung würden die ersten Hauptkomponenten von den Spalten mit der höchsten Varianz dominiert.
- Snippet 8.5 bestimmt die kleinste Zahl orthogonaler Features, die mindestens 95 % der Varianz von Z erklären.
- Die Faktorladungen eines Portfolios sind die transponierte Eigenvektormatrix mal den Allokationsvektor, dessen Gewichte sich zu eins summieren.
- Der Risikoanteil der i-ten Hauptkomponente ist das quadrierte Loading mal dem zugehörigen Eigenwert, normiert auf die Summe über alle Komponenten.
- Die Zerlegung lautet Z′Z W = W Λ, mit der Eigenvektormatrix W und der Eigenwertmatrix Λ.
- W̃ enthält die ersten M Spalten von W, mit M ≤ N, sodass der Anteil dieser Eigenwerte an der Summe aller Eigenwerte mindestens τ ist.
- τ liegt zwischen 0 und 1 einschließlich.
- Die Berechnung lässt sich in eine Summe von Teilprodukten Zb W̃b zerlegen, indem die Spalten in B Teilmengen geteilt werden.
- Zb enthält nur die b-te Spaltengruppe und ist ansonsten leer.
- Die Teilergebnisse werden fortlaufend addiert.
- getPCs lädt die Blöcke nacheinander, sodass bei hinreichend großem B der Arbeitsspeicher nicht erschöpft wird.
- Dieselbe Zerlegung wird parallel ausgeführt und verkürzt damit die Rechnung.

## Voraussetzungen

- Die Kovarianzmatrix muss hermitesch sein.
- Die beschriebene PCA geht von einer Matrix stationärer Features aus, mit Beobachtungen t von 1 bis T und Variablen n von 1 bis N.

## Anwendung im Trading

- Der so bestimmte Allokationsvektor ist eine Möglichkeit, die Gewichte für den ETF-Trick zu bilden.
- Neben der Behandlung von Substitutionseffekten kann die Orthogonalisierung die Dimension von X senken, indem Merkmale zu kleinen Eigenwerten entfallen, was die Konvergenz von ML-Algorithmen meist beschleunigt.
- Die Analyse läuft dann auf Features, die dazu bestimmt sind, die Struktur der Daten zu erklären.

## Regeln und Kriterien

- Das gewichtete Kendall-Tau zwischen den Feature Importances und den zugehörigen Eigenwerten, gleichbedeutend mit dem inversen PCA-Rang, liegt näher bei 1, wenn beide Rangfolgen stärker übereinstimmen.
- Ein gewichtetes Kendall-Tau wird dem gewöhnlichen vorgezogen, weil die Rangübereinstimmung bei den wichtigsten Features Vorrang hat und die Übereinstimmung bei irrelevanten, vermutlich verrauschten Features weniger zählt.
- Weil weightedtau höhere Werte stärker gewichtet, wird die Korrelation auf dem inversen PCA-Rang berechnet.

## Risiken und Grenzen

- In realen Machine-Learning-Anwendungen enthält Z oft Milliarden Datenpunkte.
- Manche dieser Probleme lassen sich wegen des Speicherbedarfs ohne Parallelisierung nicht lösen, auch wenn man länger auf das Ergebnis warten würde.

## Beispiele

- Im Streudiagramm der Eigenwerte gegen die MDI-Werte beträgt die Pearson-Korrelation 0,8491 bei einem p-Wert unter 1E-150.
- Das hyperbolisch gewichtete Kendall-Tau zwischen Feature Importance und Eigenwerten beträgt in der Stichprobe von Abbildung 8.1 0,8206.
- Im Scipy-Beispiel mit den Importances 0,55, 0,33, 0,07 und 0,05 sowie den PCA-Rängen 1, 2, 4 und 3 ergibt das gewichtete Kendall-Tau auf dem inversen PCA-Rang 0,8133.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 58–77 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-004-p058-p077|S. 58–77]]
- Advances in Financial Machine Learning.pdf, S. 134–153 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-008-p134-p153|S. 134–153]]
- Advances in Financial Machine Learning.pdf, S. 286–305 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-016-p286-p305|S. 286–305]]
- Advances in Financial Machine Learning.pdf, S. 324–343 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-018-p324-p343|S. 324–343]]

## Verwandte Themen
