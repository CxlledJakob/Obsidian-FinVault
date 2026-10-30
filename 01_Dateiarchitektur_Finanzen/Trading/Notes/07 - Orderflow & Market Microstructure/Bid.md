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

# Bid


## Kurzdefinition

- Das Bid ist ein Quote, zu dem ein Wertpapier auf einem Preisniveau zum Kauf gestellt wird.

## Kernaussagen

- Ein Trade entsteht, wenn ein Verkäufer ein Bid matcht.
- Niedrige Preise werden fast immer gegen das Bid gematcht.
- Das gegen das Bid gehandelte Volumen, also die verkaufsinitiierten Trades, wird VS genannt.
- Das Break-even-Bid der Market Maker ist der erwartete Preis abzüglich (μ αt δt) / (ε + μ αt δt) mal (E[St] − SB).

## Funktionsweise

- Auf Pro-rata-Märkten wie den Eurodollar-Futures an der CME wird dem Bid sofort beigetreten, damit bei einer Ausführung auf der Bid-Seite ein Teil zugeteilt wird.
- Beigetreten wird nur, wenn die ursprüngliche Bid-Size viel größer ist als die Ask-Size; das heißt Ratio Trade.
- Der erwartete Füllungsanteil entspricht dem Verhältnis der eigenen Ordergröße zur gesamten Ordergröße auf dem Bid-Preis.
- Steigt der Bid danach um einen oder mehrere Ticks, wird mit Gewinn verkauft.
- Bewegt sich der Bid nicht oder bleibt die Verkaufs-Limit-Order ungefüllt, lässt sich wegen der großen Bid-Size voraussichtlich noch zum ursprünglichen Best Bid verkaufen, mit Verlust nur in Höhe der Kommission.
- Beim Ticking liegt die Kauforder auf dem Best Bid plus einem Tick.
- Beim Flipping auf Märkten mit Zeitpriorität wird eine große Buy-Limit-Order auf den Best Bid gelegt, um Kaufdruck vorzutäuschen, und nach Füllung der kleinen Gegenseite sofort storniert.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Ein fehlerhaft angezeigter Bid von 110 Dollar um 11:02 kann eine Short-Market-Sell-Order auslösen, die bei 100 Dollar gefüllt wird, weil tatsächlich kein Bid bei 110 Dollar stand.
- Der ursprüngliche Best Bid kann storniert werden, sobald der liegende Händler erkennt, dass er frontgerannt wurde; dann bleibt zum Glattstellen nur ein niedrigerer Bid.
- Eine Falle besteht darin, dass der ursprüngliche Bid eigentlich verkaufen wollte und den Bid storniert, sobald zum Bid plus einem Tick gekauft wurde.
- Wird die große Buy-Limit-Order beim Flipping wirklich gefüllt, kann der Verkauf mit Verlust nötig werden.
- Eine Transaktion am Bid ist negativer Orderflow.

## Beispiele

- Im Paarbeispiel hat X einen wahren Bid von 100 Dollar, während Y einen wahren Ask von 105 Dollar hat.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 173–186 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-013-p173-p186|S. 173–186]]

## Verwandte Themen
