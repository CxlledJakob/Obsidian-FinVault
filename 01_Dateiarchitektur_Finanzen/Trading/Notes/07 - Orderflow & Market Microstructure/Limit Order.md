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

# Limit Order


## Kurzdefinition


## Kernaussagen


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

## Verwandte Themen
