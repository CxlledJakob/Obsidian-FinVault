---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/18 - Positionsmanagement/18 - Positionsmanagement|18 - Positionsmanagement]]"
weitere_hauptthemen: []
unterthema: "Trade Management"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Scaling Out


## Kurzdefinition

- Scaling-in-Strategien skalieren auch schrittweise aus und warten mit der Gewinnmitnahme nicht, bis der Preis vollständig zum Mittel zurückgekehrt ist.
- Multiple-Unit-Trading heißt, jede Position in mindestens zwei Units zu teilen. Eine Unit kann ein Future-Kontrakt oder zehn Kontrakte sein, 100 oder 1.000 Aktien. Der Betrag ist beliebig, jeder Trade braucht aber mindestens zwei Units.

## Kernaussagen

- Immer zwei Units handeln und die erste an einem Ziel der kleineren Korrektur herausnehmen. Über die Zeit sollen die Nettoergebnisse mit dieser Strategie für alle Trades viel größer sein.
- Im Einzelfall wäre der Gewinn größer, wenn beide Units wie die zweite geführt würden. Vorher ist nicht bekannt, ob nur eine kleinere Korrektur entsteht, obwohl alle Faktoren auf den größeren Trend zeigen.
- Die erste Unit wird sehr schnell an einem kleineren Retracement mit kleinem Gewinn geschlossen. Der Stop der zweiten geht auf Breakeven und sichert damit mindestens diesen kleinen Gewinn, falls der Ausblick falsch ist.

## Funktionsweise

- Schon eine kleine Rückkehr lässt sich realisieren, deshalb kann die Strategie profitabel bleiben, auch wenn die Reihe nicht wirklich stationär ist und nie zum Mittel zurückkehrt.
- Bei großen Größen senkt das schrittweise Aussteigen zusammen mit dem schrittweisen Einsteigen die Marktauswirkung.
- Mit mehreren Bollinger-Bändern liegen die Ausstiege bei 0, 1, 2 bis N minus 1 Standardabweichungen, passend zu den Einstiegen 1, 2, 3 bis N.
- Läuft der Markt nach dem Einstieg in die erwartete Richtung, wird eine Unit gewöhnlich relativ schnell mit relativ kleinem Gewinn geschlossen. Die zweite bleibt, um den längeren Trend zu erfassen.
- Die erste Unit nimmt an, man liege beim Trend der größeren Zeitebene falsch und der Markt mache nur eine kleinere Korrektur. Sie wird geschlossen, sobald die Bedingungen für den Abschluss dieser kleineren Korrektur vorliegen.
- Entwickelt sich der Trend wie erwartet, bleibt die zweite Unit, um die Rendite der größeren Zeitebene zu maximieren.
- In den Beispielen heißen die beiden Units kurzfristige und langfristige Unit. Der Autor erwartet bessere Ergebnisse, wenn jeder Trade so geteilt wird. Erfolgreiche Trader nutzen das, solange es Handel gibt, und für den Autor machte es einen großen Unterschied, als er es in seinen Plan aufnahm.
- Die kurzfristige Unit wird nicht schon nach der ersten Momentum-Umkehr der kleineren Zeitebene geschlossen. Der Markt machte danach gewöhnlich noch eine zweite Umkehr, selbst wenn kein längerer Trend entstand.
- Der Plan handelt zwei Einheiten: die erste wird am kurzfristigen Ziel geschlossen, die zweite für einen möglichen längeren Trend gehalten.
- Die erste Einheit wird nach Erreichen des 50-Prozent-Retracements mit dem nachgezogenen 60-Minuten-Ein-Bar-Tief geführt.
- Ein relativ kleiner Gewinn auf einer Einheit wird schnell mitgenommen; die zweite behält einen weiter vom Markt entfernten Stop.
- Selbst wenn die zweite Einheit an einem neuen Tief ausgestoppt wird, kann der Zwei-Einheiten-Trade netto ein paar Pips im Plus bleiben.
- Die Hälfte wird an einem kleineren Retracement geschlossen, falls der Rückgang nur eine kleine Korrektur und nicht der Beginn eines Abwärtstrends ist.
- Die zweite Einheit wird verlassen, sobald eine bestätigte dreiteilige Bewegung die Korrektur und die folgende Fortsetzung anzeigt, statt sie für den ursprünglich erwarteten längeren Lauf zu halten.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- In der Modellrechnung von Schoenberg und Corwin werden alle Kontrakte erst bei F geschlossen, es gibt also kein average-out, selbst wenn average-in benutzt wurde.
- Auch der Ausstieg an zwei oder mehr Bollinger-Bändern ist im Backtest nie optimal, solange die Wahrscheinlichkeit eines tieferen Einbruchs konstant ist.

## Beispiele

- Jaime Johnson, leitender technischer Analyst der DT Daily Reports für Futures, Aktien und ETF sowie Forex, hat in Tutorials gezeigt, wie man bei der Marktlage völlig falsch liegen und mit zwei Units trotzdem einen Gewinn erzielen kann.
- Beim XAU wurde die halbe Position mit 18,02 Punkten geschlossen, in der Rechnung 150,37 minus 132,34, ausgestoppt bei 150,36. Die zweite Unit lief weiter.
- Beim S&P brachte die kurzfristige Unit 35 Punkte, 1466,25 minus 1431,25. Die langfristige Unit blieb offen.
- Die kurzfristige EUR/USD-Unit brachte 156 Pips auf 18 Pips Risiko und wurde relativ schnell geschlossen, für den Fall, dass nur eine korrektive Rally vorlag. Die langfristige Unit lief fast sechs Wochen bis 561 Pips.
- Im ungehebelteten SPY brachte die erste Unit ungefähr 2 Prozent in zwei Tagen, die zweite ungefähr 5,3 Prozent in weniger als zwei Wochen.
- Nach dem Ausstieg der kurzfristigen EUR/USD-Unit werden die 60-Minuten-Daten nicht mehr gebraucht. Die langfristige Unit läuft auf Wochen- und Tagesdaten weiter.
- OIH wurde auf beiden Units gleichzeitig mit 4,93 Verlust ausgestoppt, weil der gemeinsame anfängliche Stop nicht angepasst wurde. Ein gestuftes Herausnehmen fand nicht statt.
- Im EUR/USD ging die erste Einheit bei 1,4387 mit 46 Pips heraus, die zweite blieb für den längeren Trend und brachte 246 Pips.
- Beim GBP wurden 37 Pips auf der ersten und 82 Pips auf der zweiten Einheit realisiert, zusammen 119 Pips.
- Beim ES sollte eine Einheit bei 1360 und die zweite bei 1390 geschlossen werden; eine Einheit ging bei 1360 mit 38,75 Punkten heraus.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 177–196 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-014-p177-p196|S. 177–196]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 196–214 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-015-p196-p214|S. 196–214]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 215–234 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-016-p215-p234|S. 215–234]]

## Verwandte Themen
