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
aktualisiert: 2026-11-01
---

# Limit Order


## Kurzdefinition


## Kernaussagen

- Der Ratio Trade tritt dem Bid sofort bei, damit bei jeder Füllung auf der Bid-Seite ein Teil zugeteilt wird, und nur wenn die ursprüngliche Bid-Size viel größer ist als die Ask-Size.
- Der erwartete Füllungsanteil gleicht dem Verhältnis der eigenen Größe zur gesamten Größe auf dem Bid; steigt der Bid um einen oder mehrere Ticks, wird mit Gewinn verkauft oder eine Verkaufsorder auf den Best Ask gelegt, wenn der Spread die Round-Trip-Kommission übersteigt.
- Bewegt sich der Bid nicht, lässt sich vermutlich noch zum ursprünglichen Best Bid verkaufen, mit Verlust nur der Kommissionen.
- Ticking ist nur profitabel, wenn die Round-Trip-Kommission je Stück kleiner ist als der Spread minus zwei Ticks; scheitert der Verkauf einen Tick unter dem Best Ask, folgt der Verkauf zum ursprünglichen Best Bid mit Verlust der Kommissionen plus einem Tick.
- Flipping startet bei ungefähr gleichen Größen, lockt mit der großen Kauforder Käufe zum Ask an und kauft nach der Stornierung zum ursprünglichen Best Bid zurück, wenn die zuvor Kaufenden mit Verlust verkaufen.
- Wer die große Kauforder für Flipping hält, kann an die Flipper verkaufen und die Short-Position unter dem ursprünglichen Bid decken, sobald Bid und Ask nachgeben.
- Nach Füllung der kleinen NBBO-Orders quoten Market Maker wieder zu denselben Preisen; große Quotes werden auch vermieden, weil ihre Füllung große Inventare erzeugt.
- Große institutionelle Orders werden in winzige Child Orders zerlegt, über Handelsplätze gestreut und über den Tag ausgeführt.

## Funktionsweise

- Auf Pro-rata-Märkten wie den Eurodollar-Futures an der CME wird dem Bid mit einer Order beigetreten, deren erwarteter Füllungsanteil dem Verhältnis der eigenen Größe zur gesamten Größe auf dem Bid entspricht.
- Beim Ticking liegt die Kauf-Limit-Order auf dem Best Bid plus einem Tick und die anschließende Verkaufsorder auf dem Best Ask minus einem Tick.
- Beim Flipping, auf Märkten mit Zeitpriorität statt Pro-rata-Zuteilung, wird eine große Buy-Limit-Order auf den Best Bid und gleichzeitig eine kleine Sell-Limit-Order auf den Best Ask gelegt.
- Sobald die kleine Verkaufsorder gefüllt ist, wird die große Kauforder sofort storniert.

## Voraussetzungen

- Private Feeds wie ITCH von Nasdaq, der EDGX Book Feed von Direct Edge und PITCH von BATS liefern die Lebensgeschichte einer Order einschließlich Änderungen und Teilausführungen.
- Wie oft ein großes Bid storniert statt gefüllt wird, hilft dabei, Flipping zu erkennen.

## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Wird die große Kauforder tatsächlich gefüllt, kann mit Verlust verkauft werden müssen.
- Der ursprüngliche Best Bid kann storniert werden, wenn erkannt wird, dass er frontgerannt wurde.
- Wer den ursprünglichen Best Bid gelegt hat, kann die Aktien teurer als zum eigenen Bid verkaufen wollen und den Bid stornieren, sobald zum Bid plus einem Tick gekauft wurde.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 173–186 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-013-p173-p186|S. 173–186]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 166–179 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-013-p166-p179|S. 166–179]]

## Verwandte Themen
