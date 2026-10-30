---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Strategien und Ausführung"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Ensemble Learning


## Kurzdefinition

- Eine Ensemble-Methode verbindet mehrere schwache Lerner desselben Algorithmus zu einem stärkeren Lerner, der jeden einzelnen übertrifft.
- Ensemble-Methoden sollen Bias, Varianz oder beides senken.

## Kernaussagen

- Drei Fehlerquellen: Bias aus unrealistischen Annahmen, dann ist das Modell unterangepasst und erkennt wichtige Beziehungen nicht; Varianz aus Empfindlichkeit gegen kleine Änderungen der Trainingsmenge, dann ist es überangepasst und verwechselt Rauschen mit Signal; Noise aus der Varianz der beobachteten Werte, etwa durch unvorhersehbare Änderungen oder Messfehler.
- Noise ist der irreduzible Rest, den kein Modell erklärt. Der mittlere quadratische Fehler zerlegt sich in quadrierten Bias, Varianz des Schätzers und diese Rauschvarianz und kann wegen des Rauschens nicht null werden.
- Bagging senkt vor allem die Prognosevarianz und wirkt damit gegen Overfitting. Die Schätzer werden unabhängig und parallel auf Ziehungen mit Zurücklegen angepasst, die Prognose ist ihr einfacher Durchschnitt oder bei Klassen ein Mehrheitsvotum.
- Die Varianz des Mittels sinkt nur, wenn die mittlere Korrelation der Einzelprognosen unter 1 liegt.
- Für ein Mehrheitsvotum über k Klassen genügt als notwendige, nicht hinreichende Bedingung, dass die Zahl richtiger Stimmen über N/k liegt. Bei hinreichend großem N, etwa über p mal (p minus 1/k) hoch minus 2, liegt die Genauigkeit des Votums über der mittleren Einzelgenauigkeit, sofern diese über 1/k liegt.
- Sind die Einzellerner schlecht, deutlich unter 1/k, bleibt auch das Votum schlecht, wenn auch mit geringerer Varianz. Bagging kann die Genauigkeit schwacher Klassifikatoren nicht heben, Boosting schon.
- Weil eine sehr kleine Korrelation leichter zu erreichen ist als eine Trefferquote über 1/k, gelingt Bagging eher als Senkung der Varianz denn als Senkung des Bias.
- Boosting zieht sequenziell nach Stichprobengewichten, behält einen Schätzer nur über einer Annahmeschwelle, gewichtet Fehlklassifikationen höher und mittelt am Ende nach der Genauigkeit der einzelnen Schätzer.
- Boosting senkt Varianz und Bias. Die Korrektur des Bias erhöht aber das Risiko, zu überanpassen.
- Der Text argumentiert, dass in Finanzanwendungen Bagging dem Boosting in der Regel vorzuziehen ist, weil Overfitting wegen des niedrigen Signal-Rausch-Verhältnisses meist schwerer wiegt als Underfitting und weil sich Bagging parallelisieren lässt, Boosting im Allgemeinen aber nicht.
- Der Random Forest trainiert wie Bagging unabhängige Schätzer auf Bootstrap-Teilmengen und bewertet bei jedem Split nur eine zufällige Attributteilmenge ohne Zurücklegen, um die Schätzer weiter zu dekorrelieren.
- Er senkt die Prognosevarianz ohne Overfitting, solange die mittlere Korrelation unter 1 bleibt, bewertet die Feature-Importance und liefert eine Out-of-Bag-Genauigkeit. In Finanzanwendungen ist diese Genauigkeit leicht überschätzt, und der Bias liegt nicht notwendig unter dem einzelner Entscheidungsbäume.
- Eine Drehung des Merkmalsraums in Richtung der Achsen verringert typischerweise die nötige Baumtiefe. Der Text empfiehlt deshalb, den Random Forest auf einer PCA der Features zu rechnen, was die Rechnung beschleunigen und etwas Overfitting abbauen kann.
- Bagging kann schlecht skalierende Basisschätzer wie Support Vector Machines nutzbar machen: Viele kleine Teilaufgaben laufen parallel, und frühes Stoppen erhöht zwar die Einzelvarianz, mehr unabhängige Schätzer können das aber mehr als ausgleichen.

## Funktionsweise

- Bagging: N Mengen mit Zurücklegen, N unabhängige Schätzer, dann einfacher Durchschnitt, Mehrheitsvotum oder Mittel der vorhergesagten Wahrscheinlichkeiten.
- Boosting startet mit gleichen Gewichten, verwirft einen Schätzer unter der Schwelle, zum Beispiel 50 Prozent bei einem binären Klassifikator, wertet falsch klassifizierte Beobachtungen auf, wiederholt das bis N Schätzer entstanden sind und bildet dann den genauigkeitsgewichteten Durchschnitt. AdaBoost ist eines der verbreiteten Verfahren.
- Der Random Forest unterscheidet sich vom reinen Bagging durch die zweite Zufallsstufe bei den Attributen jedes Splits.
- Für eine große SVM nennt der Text ein max_iter von 100.000 statt des Standards minus 1, der bis unter eine Toleranz weiterläuft, oder ein höheres tol als den Standard von 10 hoch minus 3. Bei anderen Algorithmen entsprechen dem max_depth und min_weight_fraction_leaf.

## Voraussetzungen


## Anwendung im Trading

- Wegen des niedrigen Signal-Rausch-Verhältnisses hält der Text Overfitting in Finanzdaten für das vordringliche Problem und Bagging deshalb für meist geeigneter als Boosting.
- Auf sehr großen Datenmengen soll Bagging mit frühem Stoppen schnelle und robuste Schätzungen liefern, weil aus einer großen sequenziellen Aufgabe viele kleinere parallele werden.

## Regeln und Kriterien

- class_weight gleich balanced_subsample soll verhindern, dass die Bäume Minderheitsklassen falsch einordnen.
- Drei im Text gezeigte Aufbauten sind ein Random Forest mit 1.000 Bäumen, ein Bagging von Entscheidungsbäumen mit max_samples gleich der mittleren Eindeutigkeit und ein Bagging von Random Forests mit einem Baum, ohne deren eigenes Bootstrap, ebenfalls mit dieser Stichprobengrenze.

## Risiken und Grenzen

- Redundante Beobachtungen treiben die Korrelation der Ensemble-Mitglieder gegen 1. Dann sinkt die Varianz nicht, unabhängig von der Zahl der Schätzer.
- Boosting korrigiert Bias um den Preis eines höheren Overfitting-Risikos.
- Die Out-of-Bag-Genauigkeit eines Random Forest ist bei Finanzdaten leicht nach oben verzerrt.
- Selbst eine konvergierte SVM auf einer Million Beobachtungen garantiert weder ein globales Optimum noch, dass sie nicht überangepasst ist.

## Beispiele


## Unterschiedliche Quellenpositionen

- Kearns und Valiant fragten 1989, ob schwache Schätzer zu einem Schätzer mit hoher Genauigkeit verbunden werden können. Schapire zeigte 1990, dass das geht, mit dem Verfahren, das heute Boosting heißt.
- Für das Mehrheitsvotum verweist der Text auf Condorcets Jury-Theorem. Es stammt aus der politischen Abstimmung und behandelt ein dem Genauigkeitsargument ähnliches Problem.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 115–134 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-007-p115-p134|S. 115–134]]

## Verwandte Themen
