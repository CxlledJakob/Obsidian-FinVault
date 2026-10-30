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

# Ask


## Kurzdefinition

- Das Ask, im Text auch Offer, ist ein Quote, zu dem ein Wertpapier auf einem Preisniveau zum Verkauf gestellt wird.

## Kernaussagen

- Offer-Preise liegen stets über den Bid-Preisen, weil es sonst sofort zu einem Match käme.
- Ein Trade entsteht, wenn ein Käufer ein Offer matcht.
- Hohe Preise werden fast immer gegen das Offer gematcht.
- Das gegen das Ask gehandelte Volumen, also die kaufinitiierten Trades, wird VB genannt.
- Das Break-even-Ask der Market Maker liegt über dem erwarteten Preis, mit dem Aufschlag (μ αt (1 − δt)) / (ε + μ αt (1 − δt)) mal (SG − E[St]).
- Ein Kauf zum Ask-Preis ist gleichbedeutend mit einer Market Order zum Kauf und erzeugt positiven Orderflow.
- Verkauft ein Händler 100 Einheiten an Dealer, Market Maker oder Orderbuch, ist der Orderflow minus 100; der Kauf von 100 Einheiten ergibt plus 100.
- Ob eine Transaktion am Bid oder am Ask stattfand, lässt sich für Aktien und Futures aus jedem Tick bestimmen, also aus Änderungen von Best Bid, Ask sowie Transaktionspreis und -größe.
- Eine Transaktion am Ask zählt als positiver Orderflow, eine am Bid als negativer.
- Ist die Bid-Size viel größer als die Ask-Size, wird ein Tick nach oben erwartet, und umgekehrt.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Beim Ticking wird die Kauforder auf den Best Bid plus einen Tick gelegt und nach der Füllung eine Verkaufsorder auf den Best Ask minus einen Tick.
- Ticking verlangt einen ursprünglichen Spread von mehr als zwei Ticks und ist nur profitabel, wenn die Round-Trip-Kommission pro Aktie kleiner ist als der Bid-Ask-Spread minus zwei Ticks.
- Scheitert die Verkaufsorder, wird zum ursprünglichen Best Bid verkauft, mit dem Verlust der Kommission plus einem Tick.
- Nach einem Uptick kann am Best Ask verkauft werden, wenn der Bid-Ask-Spread größer ist als die Round-Trip-Kommission pro Aktie.
- Beim Flipping wird zusammen mit einer großen Buy-Limit-Order am Best Bid eine kleine Sell-Limit-Order am Best Ask gelegt.

## Risiken und Grenzen

- Zeigt ein Datenfehler den Ask von Y als 106 Dollar, wird der fehlerhafte Spread 6 Dollar, ein Anstieg von 20 Prozent über den realen Spread von 5 Dollar, und das kann eine fehlerhafte Order zum Kauf von X und Verkauf von Y auslösen.
- Market Maker passen Bid und Ask sofort an, wenn großer gleichgerichteter Orderflow auf informierte Händler hindeutet.

## Beispiele

- Im Paarbeispiel hat Y einen wahren Ask von 105 Dollar und X einen wahren Bid von 100 Dollar, sodass der Spread Y minus X 5 Dollar beträgt und zu klein sein kann, um eine Market Order zum Kauf von X und Verkauf von Y auszulösen.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 173–186 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-013-p173-p186|S. 173–186]]

## Verwandte Themen
