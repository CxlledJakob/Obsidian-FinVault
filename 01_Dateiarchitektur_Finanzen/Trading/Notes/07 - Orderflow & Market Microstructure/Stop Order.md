---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/07 - Orderflow & Market Microstructure/07 - Orderflow & Market Microstructure|07 - Orderflow & Market Microstructure]]"
weitere_hauptthemen: []
unterthema: "Orderbuch"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Stop Order


## Kurzdefinition


## Kernaussagen

- Broker nehmen keine ungefähren Orders an, sondern konkrete Preisorders. Deshalb haben Einstieg und erster Schutzstop einen exakten Preis.
- Der Einstieg erfolgt über einen Buy-Stop einen Tick über dem Hoch oder einen Sell-Stop einen Tick unter dem Tief, entweder des letzten abgeschlossenen Bars oder des Swing-Extrems.
- Der erste Schutz ist ein Sell-Stop einen Tick unter dem Swing-Tief oder ein Buy-Stop einen Tick über dem Swing-Hoch.

## Funktionsweise

- Die meisten Plattformen haben eine Kontingenz: Wird der Buy-Stop ausgeführt, wird sofort der Sell-Stop eingestellt.
- Wird der Buy-Stop am Folgetag nicht ausgeführt, kann am Abend der passende Buy-Stop für den nächsten Tag neu gesetzt werden, wenn die Bedingungen noch gelten.
- Ein Alert auf die Momentumumkehr ersetzt das dauernde Beobachten. Danach werden die Stop-Orders gelegt, und der Markt führt den Buy-Stop aus oder nicht.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Die Swing-Einstiegsstrategie kauft oder verkauft nie zu einem Zielpreis. Ausgeführt wird erst, wenn der Markt sich in die erwartete Trendrichtung bewegt.
- Ob die Stop-Order ausgeführt wird, ist offen. Einstiegspreis und Schutzstop stehen fest, falls sie ausgeführt wird.

## Risiken und Grenzen

- Märkte können über Buy-Stops und unter Sell-Stops gapen, die Ausführung liegt dann nicht am Orderpreis. In volumenstarken, aktiven Märkten geschieht das nicht oft, und Kontrolle darüber gibt es nicht.

## Beispiele

- Im ES stand der Buy-Stop des Swing Entry bei 1449,50 und der kontingente Schutz-Sell-Stop bei 1411,25. Die Order konnte nach den regulären Handelszeiten gelegt werden.
- Im 60-Minuten-Trailing-Long lag der Buy-Stop bei 1431,25, ein Tick über dem Ein-Bar-Hoch, und der Sell-Stop bei 1406,50, ein Tick unter dem Swing-Tief.
- Im 5-Minuten-Beispiel wurde der Short am nächsten Bar unter 1356,25 ausgeführt, mit Buy-Stop einen Tick über 1362,75.
- Nach der bullischen 15-Minuten-Umkehr im ES liegt der Buy-Stop für den Long bei 1441,75, einen Tick über dem Hoch des letzten abgeschlossenen Bars, und der Schutz-Sell-Stop bei 1435,25, einen Tick unter dem Tief.
- Ein Buy-Stop für mehr als zwei Kontrakte ist bei diesem 20.000-Dollar-Konto nicht zulässig.
- Beim Google-Swing-Einstieg liegt der anfängliche Schutz-Sell-Stop einen Tick unter dem kleineren Swing-Tief bei 505,79.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 153–172 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-012-p153-p172|S. 153–172]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 172–176 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-013-p172-p176|S. 172–176]]

## Verwandte Themen
