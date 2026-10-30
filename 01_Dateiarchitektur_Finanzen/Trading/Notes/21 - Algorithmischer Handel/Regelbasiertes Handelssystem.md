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
- Trotz des Bemühens, den Handelsprozess wissenschaftlich und regelbasiert zu machen, bleiben Bereiche, in denen subjektives Urteil wichtig ist.
- Dass manchmal Urteil nötig ist, macht quantitative Regeln nicht nutzlos und algorithmische Händler nicht weniger fähig als diskretionäre.
- Kahneman schreibt, Experten seien Algorithmen in jedem Bereich mit erheblicher Unsicherheit einheitlich unterlegen, vom Sieger von Fußballspielen bis zur Lebenserwartung von Krebspatienten.
- Man kann hoffen, dass der Finanzmarkt keine Ausnahme dieser Regel ist.
- Fondsmanager behalten eine aktive Rolle: Sie urteilen, ob die Modelle nach einem Strukturwandel noch gültig sind.

## Funktionsweise

- Der numerische Weg schätzt zuerst Sigma und phi des Ornstein-Uhlenbeck-Prozesses.
- Danach wird ein Gitter aus Stop- und Gewinnschwellen gebildet, im Beispiel 20 mal 20 Knoten vom halben Sigma bis zum zehnfachen Sigma.
- Auf jedem Knoten werden die künstlichen Pfade ausgewertet und eine Sharpe Ratio berechnet.
- Gewählt wird das beste Paar, oder der beste Stop zu einem vorgegebenen Gewinnziel, oder das beste Gewinnziel zu einem vorgegebenen maximalen Stop.
- Die lineare Regel setzt die gehaltenen Einheiten proportional zum negativen Z-Score des Einheitsportfolios, mit Lookback gleich der Halbwertszeit.
- Es gibt dabei keine Strategieparameter, die anhand der Performance optimiert werden.
- Ein- und Ausstieg laufen fortlaufend mit dem Z-Score, nicht über selektive Schwellen.

## Voraussetzungen

- Benötigt werden Schätzwerte für Sigma und phi sowie der Einstiegspreis und die Prognose der Gelegenheit.

## Anwendung im Trading

- Manche Strategien nutzen makroökonomische Größen wie BIP oder Inflation, andere Fundamental- und Bilanzdaten, wieder andere suchen arbitrageähnliche Fehlpreise von Derivaten.
- Die Positionsgröße skaliert den Gewinn und lässt die Sharpe Ratio unverändert, deshalb werden die Ergebnisse je gehaltener Einheit angegeben.
- Ein Urteilspunkt ist ein bevorstehendes Großereignis, bei dem zu entscheiden ist, ob dem Modell getraut, der Hebel gesenkt oder das Modell vorübergehend abgeschaltet wird.
- Ein zweiter ist, ob Kelly auf das Eigenkapital des Gesamtportfolios oder auf jede Strategie einzeln angewendet wird.
- Die Mathematik bevorzugt die erste Lösung nur bei unveränderten erwarteten Renditen und Volatilitäten; der Autor bevorzugt praktisch die zweite, damit schwache Strategien schnell auslaufen.

## Regeln und Kriterien


## Risiken und Grenzen

- Transaktionskosten können in das Verfahren aufgenommen werden, und die Abbildungen zeigen den Fall ohne sie, damit die Symmetrie der Funktionen sichtbar bleibt.
- Die üblichen Stop-Losses lassen sich bei Mean-Reversion-Strategien logisch nicht einsetzen.
- Unbekanntes Höchstkapital und nicht handelbare infinitesimale Stückzahlen machen die einfachste Regel unpraktisch.

## Beispiele

- Verkaufen Finanzintermediäre Off-the-Run-Anleihen zwei Tage vor einer Auktion von US-Treasuries, verkauft die Regel diese Anleihen drei Tage vor der Auktion.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]

## Verwandte Themen
