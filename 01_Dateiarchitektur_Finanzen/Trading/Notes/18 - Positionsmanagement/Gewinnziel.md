---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/18 - Positionsmanagement/18 - Positionsmanagement|18 - Positionsmanagement]]"
weitere_hauptthemen: []
unterthema: "Trade Management"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Gewinnziel


## Kurzdefinition

- Das Gewinnziel ist die obere horizontale Barriere der Gewinnmitnahme in der Triple-Barrier-Methode.
- Das Gewinnziel ist die positive Schwelle, bei deren Erreichen die offene Gelegenheit geschlossen wird.
- Das Gewinnziel ist die positive Auszahlung einer Wette, die mit der Trefferwahrscheinlichkeit eintritt.

## Kernaussagen

- Nach dem Bruch werden die verlassenen Stauzonen zu einfachen Zielen für das Führen und Schließen von Positionen.
- Sie sind eine sichtbare Karte der Stellen, an denen der Markt kämpfen, drehen oder Unterstützung finden kann.
- Unterstützung und Widerstand dienen damit als Ziel für den Ausstieg, nicht nur als Einstiegssignal.
- Gewinnmitnahme und Stop-Loss sollen eine Funktion des Risikos der Wette sein.
- Liegt die feste Schwelle weit über der herrschenden Volatilität, ist das Ziel zu hoch, liegt sie weit darunter, ist es zu niedrig.
- Die Breite der oberen Barriere ist der Faktor ptSl[0] mal dem Ziel trgt.
- Ist dieser Faktor 0, gibt es keine obere Barriere.
- Wird die obere Barriere zuerst berührt, erhält die Beobachtung das Label 1.
- Dieselbe Schwelle unabhängig von der beobachteten Volatilität ist ein Grund, die Fixed-Time-Horizon-Methode in den meisten Fällen zu meiden.
- Eine Ersatzschwelle ist ein variables Sigma, geschätzt als rollierende exponentiell gewichtete Standardabweichung der Renditen.
- Volumen- oder Dollar-Bars halten die Volatilität näher an der Konstanz.
- Ohne bekannte Marktseite müssen die horizontalen Barrieren symmetrisch sein oder entfallen, weil Gewinnziel und Stop nicht unterscheidbar sind.
- Gewinnziel und Stop entsprechen den horizontalen Barrieren des Meta-Labeling.
- Bei einer Prognose von null und einer Halbwertszeit von 5 liegt das Leistungsmaximum bei kleinen Gewinnzielen und weiten Stops.
- Die optimale Regel hält das Inventar dann, bis ein kleiner Gewinn entsteht, auch wenn zwischenzeitlich das Fünf- oder Siebenfache als nicht realisierter Verlust ansteht.
- Bei Prognose null und kurzer Halbwertszeit verbindet die schlechteste Regel einen engen Stop mit einem hohen Gewinnziel.
- Auf der Diagonalen, auf der Gewinnziel und Stop symmetrisch sind, liegt die Performance am nächsten bei null.
- Bei Prognose 5 und Halbwertszeit 5 ist das optimale Gewinnziel um 6 zentriert, bei Stops zwischen 4 und 10, und das Gebiet hat eine rechteckige Form.
- Bei Prognose 5 und Halbwertszeit 10 liegt das optimale Gewinnziel um 5, und die guten Stops liegen zwischen 7 und 10.
- Bei Prognose 5 und Halbwertszeit 25 liegt das optimale Gewinnziel um 3, und die guten Stops liegen zwischen 9 und 10.
- Steigt die Halbwertszeit weiter, spreizt sich das Gebiet der besten Performance.
- Bei positiver Prognose gibt es anders als bei Prognose null kein symmetrisches Gebiet der schlechtesten Performance.
- Dasselbe qualitative Muster erscheint bei einer Prognose von 10, wenn die Halbwertszeit von 5 bis 100 steigt.
- Liefert die Strategie ein Gewinnziel, lässt sich der dazu passende Stop aus den Simulationen bestimmen.
- Gibt das Fondsmanagement einen maximalen Stop vor, lässt sich das dazu passende Gewinnziel bestimmen.
- Bei negativer Prognose ist die Heatmap das gedrehte Gegenbild der positiven Prognose, und Gewinne des einen Falls werden zu Verlusten des anderen.
- Der Fall mit negativer Prognose ist das umgekehrte Bild des Falls mit positiver Prognose, so wie der Verlust des Spielers der Gewinn des Hauses ist.
- Bei Prognose minus 5 und Halbwertszeit 5 liegt das schlechteste Gebiet um einen Stop von 6 und bei Gewinnzielen zwischen 4 und 10.
- Bei Prognose minus 5 und Halbwertszeit 10 spreizt sich das Gebiet der schlechtesten Performance, aus dem Rechteck wird ein Quadrat, und die Performance wird weniger negativ.
- Bei Prognose 5 und Halbwertszeit 50 spreizt sich das Gebiet guter Performance.
- Für einen Preis aus einem diskreten Ornstein-Uhlenbeck-Prozess gibt es nach der Vermutung genau eine Kombination aus Gewinnziel und Stop, die die Sharpe Ratio maximiert.
- Die für eine Ziel-Sharpe-Ratio nötige Trefferwahrscheinlichkeit hängt vom Gewinnziel, von der Verlustschwelle und von der Wettfrequenz ab.
- Für die Darstellung der nötigen Trefferwahrscheinlichkeit wird ein Gewinnziel von 0,1 zusammen mit einer Ziel-Sharpe-Ratio von 1,5 verwendet.

## Funktionsweise

- In der Fixed-Time-Horizon-Methode ist das Label 1, wenn die Rendite über den Horizont h größer als Tau ist, -1, wenn sie unter minus Tau liegt, und 0, wenn ihr Betrag höchstens Tau ist.
- getDailyVol liefert die Tagesvolatilität, mit der die Vorgaben für Gewinnmitnahme und Stop-Loss gesetzt werden.
- Beim Meta-Labeling ist die Seite bekannt, deshalb darf die obere Barriere eine andere Breite haben als die untere.

## Voraussetzungen


## Anwendung im Trading

- Hineinkommen ist leicht, hinausgehen ist der schwere Teil. Die historischen Zonen helfen, den Ausstieg an das eigene Preisverhalten des Marktes zu hängen.
- Ein Bruch durch eine Decke macht aus dieser Decke einen Boden, der als natürliches Schutz- und Zielniveau der laufenden Bewegung dient.
- Dieselbe Logik gilt abwärts: der alte Boden wird zur Decke und damit zum Ziel, an dem ein Short-Rücksetzer Widerstand findet.
- Das nahe bei null liegende Ergebnis symmetrischer Schwellen bei Prognose null soll bei der Beschriftung von Beobachtungen mit der Triple-Barrier-Methode beachtet werden.
- Ein positives langfristiges Gleichgewicht entspricht dem Geschäft eines Positionshalters wie eines Hedgefonds oder eines Asset Managers.

## Regeln und Kriterien

- In der Konfiguration [1,1,1] soll ein Gewinn bei begrenzter Verlusttoleranz und begrenzter Haltedauer realisiert werden.
- In der Konfiguration [1,0,0] wird die Position gehalten, bis ein Gewinn entsteht.

## Risiken und Grenzen


## Beispiele

- Bei Tau gleich 0,01 kann die realisierte Bar-Volatilität in der Nachtsitzung 0,0001 und um die Eröffnung 0,01 betragen.
- Unter einer solchen festen Schwelle wird die große Mehrheit der Labels 0, auch wenn die Rendite vorhersehbar und statistisch signifikant war.
- In der schlechtesten Region bei Prognose minus 5 und Halbwertszeit 5 liegen die Sharpe Ratios um minus 12.
- Bei Prognose minus 5 und Halbwertszeit 10 liegen die Sharpe Ratios etwa bei minus 9.
- Im Rechenbeispiel ist das Gewinnziel 0,005, die Verlustschwelle minus 0,01, die Frequenz 260 Wetten pro Jahr und die Trefferwahrscheinlichkeit 0,7.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- A Complete Guide to Volume Price Analysis.pdf, S. 96–115 → [[Trading/Pilot/blocks/a-complete-guide-to-volume-price-analysis-pdf/a-complete-guide-to-volume-price-analysis-pdf-block-006-p096-p115|S. 96–115]]
- Advances in Financial Machine Learning.pdf, S. 58–77 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-004-p058-p077|S. 58–77]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]

## Verwandte Themen
