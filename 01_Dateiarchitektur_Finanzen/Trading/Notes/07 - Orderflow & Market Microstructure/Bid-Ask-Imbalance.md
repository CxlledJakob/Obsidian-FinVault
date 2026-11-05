---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/07 - Orderflow & Market Microstructure/07 - Orderflow & Market Microstructure|07 - Orderflow & Market Microstructure]]"
weitere_hauptthemen: []
unterthema: "Transaktionsfluss"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-01
---

# Bid-Ask-Imbalance


## Kurzdefinition

- Das Ungleichgewicht besteht darin, dass die Bid-Size viel größer ist als die Ask-Size oder umgekehrt.

## Kernaussagen

- Ist die Bid-Size viel größer als die Ask-Size, wird ein Tick nach oben erwartet, und umgekehrt.
- Maslov und Mills (2001) finden am Nasdaq einen annähernd linearen Zusammenhang zwischen dem Ungleichgewicht von Bid- und Ask-Sizes und kurzfristigen Preisänderungen.
- Der Effekt ist bei Aktien mit geringerem Volumen stärker.
- Er beschränkt sich nicht auf die NBBO-Preise: Ein Ungleichgewicht des gesamten Orderbuchs erzeugt auch Preisänderungen, gezeigt für eine Aktie an der Stockholmer Börse von Hellström und Simonsen (2006).
- Auf der kürzesten Zeitskala können das Ungleichgewicht der Bid- und Ask-Sizes, Änderungen im Orderflow oder die ungleichmäßige Verteilung von Stop-Orders Preismomentum erzeugen.
- Viele High-Frequency-Momentum-Strategien nutzen dieses Ungleichgewicht, und High-Frequency-Händler erzeugen es manchmal selbst.
- Beim Ratio Trade auf Pro-rata-Märkten entspricht der erwartete Füllungsanteil dem Verhältnis der eigenen Ordergröße zur gesamten Ordergröße auf dem Bid.
- Steigt der Bid danach um einen oder mehrere Ticks, wird mit Gewinn verkauft oder eine Verkaufsorder auf den Best Ask gelegt, sofern der Spread größer ist als die Round-Trip-Kommission je Stück; sonst lässt sich wegen der großen Bid-Size vermutlich noch zum ursprünglichen Best Bid verkaufen, mit Verlust nur der Kommissionen.
- Ticking, auch Quote Matching, verlangt einen Spread von mehr als zwei Ticks: Kauf auf dem Best Bid plus einem Tick, danach Verkauf auf dem Best Ask minus einem Tick.
- Ticking ist nur profitabel, wenn die Round-Trip-Kommission je Stück kleiner ist als der Bid-Ask-Spread minus zwei Ticks; scheitert der Verkauf, bleibt der Verkauf zum ursprünglichen Best Bid mit Verlust der Kommissionen plus einem Tick.
- Flipping setzt Zeitpriorität statt Pro-rata voraus und startet bei ungefähr gleichen Best-Bid- und Best-Ask-Sizes; die große Kauf-Limit-Order soll Kaufdruck vortäuschen, Händler kaufen zum Ask und füllen die kleine Verkaufsorder.
- Nach sofortiger Stornierung der großen Kauforder sind die Größen wieder ungefähr gleich, viele der zuvor Kaufenden verkaufen mit Verlust zurück, und es kann zum ursprünglichen Best Bid gekauft werden.
- Füllt jemand die große Kauforder, muss unter Umständen mit Verlust verkauft werden; wer Flipping vermutet, kann an die Flipper verkaufen, den Bid drücken und die Short-Position unter dem ursprünglichen Bid decken, sobald sie ihr Inventar abgeben und auch den Ask drücken.
- High-Frequency-Händler können nur von langsameren Händlern profitieren; bleiben nur sie im Markt, ist der durchschnittliche Nettogewinn aller null.
- Weil solche Strategien große Bids oder Asks frontrunnen, quoten viele traditionelle Market Maker keine großen Größen mehr, und die NBBO-Größen sind in vielen Märkten gesunken.
- Bei AAPL betragen die NBBO-Größen oft nur wenige hundert Aktien, bei SPY an ARCA oft weniger als 10.000 Stück; nach Füllung dieser kleinen Orders wird zu denselben Preisen neu quotiert, auch damit keine großen Inventare entstehen.
- Große institutionelle Orders, die früher als Blocktrades liefen, werden in winzige Child Orders zerlegt, über verschiedene Handelsplätze gestreut und über den Tag ausgeführt.

## Funktionsweise

- Auch ohne vorhandenes Ungleichgewicht lässt sich die Illusion von Kaufdruck herstellen; das heißt Momentum Ignition.
- Der Ratio Trade tritt dem Bid nur bei, wenn die ursprüngliche Bid-Size viel größer ist als die Ask-Size.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 173–186 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-013-p173-p186|S. 173–186]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 166–179 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-013-p166-p179|S. 166–179]]

## Verwandte Themen
