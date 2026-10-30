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

# Varianz


## Kurzdefinition

- Varianz ist der Fehler aus der Empfindlichkeit gegen kleine Änderungen der Trainingsmenge. Ist sie hoch, hat der Algorithmus überangepasst und Rauschen mit Signal verwechselt.
- Noise ist die Varianz der beobachteten Werte, etwa durch unvorhersehbare Änderungen oder Messfehler, und lässt sich durch kein Modell erklären.
- Die Inverse-Varianz-Allokation ist optimal, wenn die Kovarianzmatrix diagonal ist: Das Gewicht ist dann proportional zum Kehrwert der eigenen Varianz.
- Für den charakteristischen Vektor aus Einsen ist die Lösung des quadratischen Programms das Minimum-Varianz-Portfolio.

## Kernaussagen

- Der mittlere quadratische Fehler zerlegt sich in den quadrierten Bias, die Varianz des Schätzers und die Rauschvarianz. Wegen des Rauschens kann er nicht null werden.
- Der Hauptvorteil von Bagging ist, die Varianz der Prognosen zu senken und damit Overfitting zu begegnen.
- Die Varianz des Mittelwerts von N Einzelprognosen ist die mittlere Einzelvarianz mal (mittlere Korrelation plus (1 minus diese Korrelation) geteilt durch N).
- Diese Varianz sinkt nur, solange die mittlere Korrelation unter 1 liegt, und geht gegen die Einzelvarianz, wenn die Korrelation gegen 1 geht.
- Sequenzielles Bootstrap soll möglichst unabhängige Stichproben liefern, die Korrelation senken und damit die Varianz von Bagging-Klassifikatoren verringern.
- Werden richtige Prognosen als 1 gezählt, ist ihre Zahl im Mittel N mal p und ihre Varianz N mal p mal (1 minus p).
- Bei schlechten Einzellernern, deren Trefferquote weit unter 1/k liegt, bleibt das Mehrheitsvotum schlecht, die Varianz ist aber geringer.
- Bagging senkt eher die Varianz als den Bias, weil eine sehr kleine Korrelation leichter zu erreichen ist als eine Trefferquote über 1/k.
- Redundante Beobachtungen machen die Bootstrap-Ziehungen nahezu gleich und treiben die Korrelation gegen 1. Dann sinkt die Varianz nicht, unabhängig von N.
- Entscheidungsbäume erhöhen die Prognosevarianz durch Overfitting. Der Random Forest ist darauf angelegt, sie zu senken, und tut das ohne Overfitting, solange die Korrelation unter 1 bleibt.
- Frühes Stoppen schlecht skalierender Basisschätzer erhöht die Varianz der Einzelergebnisse. Zusätzliche unabhängige Schätzer im Bagging können diesen Anstieg mehr als ausgleichen.
- CLA minimiert die Varianz in der Stichprobe und hat dort die geringere Standardabweichung, 0,4486 gegen 0,4640.
- Außer Stichprobe hat CLA trotzdem die höchste Varianz der drei Verfahren.
- Die Varianzen der Portfoliorenditen außer Stichprobe betragen 0,1157 für CLA, 0,0928 für das Inverse-Varianz-Portfolio und 0,0671 für Hierarchical Risk Parity.
- CLA liegt damit 72,47 Prozent und das Inverse-Varianz-Portfolio 38,24 Prozent über der Varianz von Hierarchical Risk Parity.
- Bei mittleren Renditen nahe 0 verbessert diese Varianzreduktion die Sharpe-Ratio einer CLA-Strategie um etwa 31,3 Prozent.
- Die Annahme einer diagonalen Kovarianzmatrix stabilisiert das Inverse-Varianz-Portfolio, seine Varianz bleibt aber deutlich höher.
- Wird die ADF-Null auf Rohpreisen verworfen, haben die Preise eine endliche Varianz, und die Renditevolatilität muss mit steigenden Preisen fallen und mit fallenden steigen.
- Bei Logpreisen bedingen die Preisniveaus den Renditemittelwert, nicht die Renditevolatilität.
- Ist die Renditevarianz invariant zum Preisniveau, wird ein ADF auf Rohpreisen strukturell heteroskedastisch.

## Funktionsweise

- Hierarchical Risk Parity definiert die Varianz einer zusammenhängenden Teilmenge als Varianz einer Inverse-Varianz-Allokation.
- Von oben nach unten werden die Gewichte umgekehrt proportional zu den aggregierten Varianzen der benachbarten Teilmengen geteilt.
- Der Splitfaktor ist eins minus der Bruch aus der Varianz der ersten Hälfte und der Summe beider Teilvarianzen und liegt zwischen 0 und 1.
- Für zwei Anlagen ist das Minimum-Varianz-Gewicht der ersten Anlage eins minus der Bruch aus ihrer Varianz und der Summe beider Varianzen, und Stufe 3 von Hierarchical Risk Parity teilt genauso.
- Ist die Kovarianzmatrix diagonal, ist das Gewicht einer Anlage ihr inverser Varianzterm geteilt durch die Summe aller inversen Varianzen.
- Bei zwei Anlagen ist das Gewicht der ersten Anlage eins minus der Bruch aus ihrer Varianz und der Summe beider Varianzen.
- Stufe 3 von Hierarchical Risk Parity setzt den Anteil der ersten Hälfte auf eins minus den Bruch aus ihrer Varianz und der Summe beider Varianzen.
- Die Cluster-Varianz im Code ist die quadratische Form der Kovarianzscheibe mit Inverse-Varianz-Gewichten.

## Voraussetzungen


## Anwendung im Trading

- Bei Finanzbeobachtungen, die nicht unabhängig sind, nennt der Text den sequenziellen Bootstrap als Mittel, die Korrelation und damit die Varianz der gebaggten Prognose zu senken.
- Werden Labels aus der Rendite über 100 Bars gebildet, soll je Schätzer nur 1 Prozent der Beobachtungen gezogen werden, damit die Ziehungen nicht redundant werden und die Varianz nicht stehen bleibt.
- Die Varianzreduktion außer Stichprobe ist für Risk-Parity-Investoren wegen ihres hohen Hebels entscheidend.

## Regeln und Kriterien


## Risiken und Grenzen

- Liegt die mittlere Korrelation der Ensemble-Prognosen nahe 1, verändert Bagging die Varianz praktisch nicht, auch wenn sehr viele Schätzer verwendet werden.
- Bei Labels mit geringer Eindeutigkeit bleibt die Varianzreduktion aus, solange mit Zurücklegen nahezu dieselben Informationen gezogen werden.

## Beispiele

- Abbildung 6.1 zeigt die Standardabweichung der gebaggten Prognose für N zwischen 5 und 30, mittlere Korrelation zwischen 0 und 1 und mittlere Einzelstandardabweichung 1.
- Die simulierten Gauß-Renditen haben Mittelwert 0 und eine willkürlich gesetzte Standardabweichung von 10 Prozent.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 115–134 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-007-p115-p134|S. 115–134]]
- Advances in Financial Machine Learning.pdf, S. 248–267 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-014-p248-p267|S. 248–267]]
- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]

## Verwandte Themen
