---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Systementwicklung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Regelbasiertes Handelssystem


## Kurzdefinition

- Eine Investmentstrategie ist ein Algorithmus, der eine Marktunvollkommenheit behauptet, und die Handelsregel ist die Taktik für Ein- und Ausstieg.

## Kernaussagen

- Strategien können sehr unterschiedlich sein, während die Taktiken vergleichsweise einheitlich sind.
- Es gibt Dutzende Hedgefonds-Stile, und jeder Stil betreibt Dutzende eigener Strategien.
- Eine Position wird eröffnet, wenn das Signal der Strategie einen festgelegten Wert erreicht.
- Der Ausstieg wird oft durch ein Gewinnziel und einen Stop-Loss festgelegt.
- Die Handelsregel ist das Paar aus Stop-Schwelle und Gewinnschwelle.
- Die rohe Kalibrierung definiert alternative Paare, testet jedes historisch und wählt das Paar mit der höchsten Sharpe Ratio.
- Die bei der Auswahl maximierte Sharpe Ratio ist der mittlere Gewinn der Regel geteilt durch die Standardabweichung des Gewinns.

## Funktionsweise

- Der numerische Weg schätzt zuerst Sigma und phi des Ornstein-Uhlenbeck-Prozesses.
- Danach wird ein Gitter aus Stop- und Gewinnschwellen gebildet, im Beispiel 20 mal 20 Knoten vom halben Sigma bis zum zehnfachen Sigma.
- Auf jedem Knoten werden die künstlichen Pfade ausgewertet und eine Sharpe Ratio berechnet.
- Gewählt wird das beste Paar, oder der beste Stop zu einem vorgegebenen Gewinnziel, oder das beste Gewinnziel zu einem vorgegebenen maximalen Stop.

## Voraussetzungen

- Benötigt werden Schätzwerte für Sigma und phi sowie der Einstiegspreis und die Prognose der Gelegenheit.

## Anwendung im Trading

- Manche Strategien nutzen makroökonomische Größen wie BIP oder Inflation, andere Fundamental- und Bilanzdaten, wieder andere suchen arbitrageähnliche Fehlpreise von Derivaten.
- Die Positionsgröße skaliert den Gewinn und lässt die Sharpe Ratio unverändert, deshalb werden die Ergebnisse je gehaltener Einheit angegeben.

## Regeln und Kriterien


## Risiken und Grenzen

- Transaktionskosten können in das Verfahren aufgenommen werden, und die Abbildungen zeigen den Fall ohne sie, damit die Symmetrie der Funktionen sichtbar bleibt.

## Beispiele

- Verkaufen Finanzintermediäre Off-the-Run-Anleihen zwei Tage vor einer Auktion von US-Treasuries, verkauft die Regel diese Anleihen drei Tage vor der Auktion.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]

## Verwandte Themen
