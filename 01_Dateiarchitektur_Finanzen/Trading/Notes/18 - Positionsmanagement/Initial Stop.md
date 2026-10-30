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

# Initial Stop


## Kurzdefinition

- Der erste Schutzstop ist der konkrete Preis, der zusammen mit dem Einstiegspreis zum Entry gehört. Er steht immer genau dort, wo der Markt das Setup ungültig macht.
- Der anfängliche Schutzstop ist der vor der Ausführung festgelegte Preis der Verlustbegrenzung, sodass das Kapitalrisiko je Handelseinheit bekannt ist, bevor der Trade ausgeführt wird.
- Die Einstiegsstrategie bestimmt die Einstiegsbedingungen sowie die konkreten Einstiegspreise und die initialen Stop-Loss-Preise.

## Kernaussagen

- Mit einer objektiven Einstiegsstrategie gibt es keine offene Entscheidung mehr über Einstiegspreis und anfänglichen Schutz-Stop-Loss, sobald die Hochwahrscheinlichkeitsbedingungen erkannt sind. Beide Preise bestimmen die Marktposition und die Einstiegsstrategie.
- Erfolgreiche Trader haben immer einen relativ engen Stop. Wird man damit mit Verlust ausgestoppt, ist der Verlust akzeptabel.
- Märkte können über Buy-Stops und unter Sell-Stops gapen, sodass die Ausführung nicht immer zum Orderpreis erfolgt. In volumenstarken, aktiven Märkten geschieht das nicht oft, und man hat keine Kontrolle darüber.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- Das Risiko je Einheit lässt sich als Differenz zwischen Einstiegspreis und initialem Schutzstoppreis definieren.

## Regeln und Kriterien

- Der Schutzstop beim Balance-Area-Bruch liegt ein paar Ticks jenseits des Bruchpunkts.
- Beim Gap-Trade liegt er an dem Preis, an dem eine Rotation die Gap vollständig auslöscht.
- Beim Trailing-One-Bar-Entry liegt er einen Tick jenseits des Swing-Hochs oder Swing-Tiefs, das vor dem Einstieg entstanden ist.
- Beim Swing Entry liegt er ebenfalls einen Tick jenseits des Swing-Extrems vor dem Einstieg.
- Nur ein Handel jenseits dieses Extrems hebt die Umkehr auf, die den Trade begründet hat. Ein näherer Stop zwischen Einstieg und Extrem ist nicht zulässig, auch wenn der Abstand groß ist.
- Wird das Extrem genommen, gibt es keinen Grund, in der Position zu bleiben.
- Dieses Kapitel behandelt nicht, wie der Stop nachgezogen wird, wenn der Markt in die erwartete Richtung läuft. Das folgt zusammen mit den Ausstiegen in Kapitel 7.
- Erfolgreiche Trader haben immer einen relativ engen Stop, und ein Verlust an diesem Stop muss akzeptabel sein.
- Der erste Schutzstop wird beim Einstieg fest gelegt und kann bewusst weit sein, wenn die Struktur das verlangt.
- Ist dieser Stop für einen Future zu weit, kann der passende ETF das anfängliche Kapitalrisiko senken.
- Future-Trader sollen für Setups mit zu großer Anfangsbelastung den entsprechenden ETF handeln können, statt die Vorarbeit wegen des Hebels zu verwerfen.
- Der erste Stop kann etwas jenseits einer Regressionsunterstützung und mehrerer kleiner Preisprojektionen liegen.
- Ein Short-Stop ein Tick über dem jüngsten Hoch wird nicht dadurch ausgelöst, dass der Kurs ein Swing-Hoch knapp darunter handelt.
- Der erste Kaufstop eines Shorts kann auf dem Pip-Spread plus einem festen Puffer über dem vorangehenden Wellenhoch liegen.
- Ist der Einstieg der Momentum-Reversal-Strategie ausgeführt, liegt der initiale Schutzstop einen Tick unter dem Swing-Tief oder über dem Swing-Hoch, das vor dem Einstieg entstanden ist.
- Beim Swing-Breakout wird der initiale Schutz-Stop-Loss einen Tick unter beziehungsweise über dem Swing-Hoch oder Swing-Tief platziert, das vor dem Einstieg entstanden ist.

## Risiken und Grenzen


## Beispiele

- Im 60-Minuten-Long lag der Schutz-Sell-Stop bei 1406,50, ein Tick unter dem Swing-Tief, der Einstieg bei 1431,25, ein Tick über dem Ein-Bar-Hoch, mit 24,75 Punkten Abstand je Kontrakt.
- Im Trailing-One-Bar-Low-Short lag der Buy-Stop einen Tick über dem Hoch von Bar 3, dem höchsten Bar seit der bärischen Momentumumkehr und dem jüngsten Swing-Hoch.
- Im IBM-Tages-Short lag der Buy-Stop einen Tick über dem Swing-Hoch vor dem Einstieg. Einige Tage später wurde der Trade mit kleinem Verlust ausgestoppt.
- Im EUR/GBP lag der Buy-Stop einen Pip über dem korrektiven Hoch. Im EUR/USD-Long lag er einen Tick unter dem Swing-Tief vor der bullischen Umkehr.
- Beim Swing Entry im ES stand der Buy-Stop bei 1449,50. Wurde er ausgeführt, kam der Schutz-Sell-Stop automatisch bei 1411,25.
- Im 5-Minuten-Short lag der Buy-Stop einen Tick über dem Swing-Hoch bei 1362,75, der Einstieg unter dem Swing-Tief bei 1356,25.
- Im 15-Minuten-ES nach bullischer Umkehr mit der Tr-1BH-Strategie liegt der Buy-Stop bei 1441,75, einen Tick über dem Hoch des letzten abgeschlossenen Bars, und der anfängliche Schutz-Sell-Stop bei 1435,25, einen Tick unter dem Tief.
- Ob dieser Trade ausgeführt wird, ist vorher offen. Wird er ausgeführt, stehen Einstiegspreis und Stoppreis fest.
- Beim Google-Swing-Einstieg über dem potenziellen Swing-Hoch der Welle B liegt der anfängliche Schutz-Sell-Stop einen Tick unter dem kleineren Swing-Tief bei 505,79. Die Differenzrechnung verwendet 505,78 Dollar: 526,83 minus 505,78 gleich 21,05 Dollar je Aktie.
- Der ES-Long ging bei 1311,25 ein, der erste Verkaufsstop lag bei 1269; für dasselbe Setup wurde der SPY-ETF als risikoärmere Variante genannt.
- Bei den Sojabohnen lag der Einstieg am 20. April bei 767'25 und der erste Verkaufsstop bei 743'75.
- Der ES-Short hatte den Stop bei 1294,50, ein Tick über dem jüngsten Hoch; das spätere Swing-Hoch 1294,25 erreichte ihn nicht.
- Im USD/CAD lag der Kaufstop bei 1,0328, Pip-Spread plus fünf Pips über dem Hoch von Welle 2 oder B vom 23. Januar; der Einstieg war am 24. Januar bei 1,0233.
- Trotz großer anfänglicher Kapitalbindung wurde der ES-Stop noch am Einstiegstag so nachgezogen, dass ein Ausstoppen mindestens einen kleinen Gewinn ließ.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Mind Over Markets_ Power Trading with Market Generated Information, Updated Edition.pdf, S. 269–288 → [[Trading/Pilot/blocks/mind-over-markets/mind-over-markets-block-017-p269-p288|S. 269–288]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 153–172 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-012-p153-p172|S. 153–172]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 172–176 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-013-p172-p176|S. 172–176]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 234–250 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-017-p234-p250|S. 234–250]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 270–289 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-019-p270-p289|S. 270–289]]

## Verwandte Themen
