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

# Market Order


## Kurzdefinition

- Kauf aus dem Orderbuch heißt Kauf zum Ask-Preis und ist gleichbedeutend mit einer Market Order zum Kauf.
- Orderflow ist bei Lyons (2001) vorzeichenbehaftetes Transaktionsvolumen: plus 100 beim Kauf von 100 Einheiten, minus 100 beim Verkauf von 100 Einheiten.

## Kernaussagen

- Empirische Forschung zeigt, dass Orderflow Preisbewegungen gut vorhersagt.
- Orderflow sagt die kurzfristige Preisbewegung in derselben Richtung voraus.
- Lernt ein großer Hedgefonds eine wichtige Nachricht, senden seine Algorithmen in Sekundenbruchteilen große Market Orders desselben Vorzeichens.
- Die Dringlichkeit dieser Market Orders zeigt, dass die Information neu und nicht weit bekannt ist.
- Market Maker schließen daraus auf informierte Händler und passen Bid und Ask sofort an.

## Funktionsweise

- Für Aktien und Futures lässt sich aus jedem Tick bestimmen, ob die Transaktion am Bid, also mit negativem Orderflow, oder am Ask, also mit positivem Orderflow, stattfand.
- Im Devisenmarkt melden die meisten Dealer keine Transaktionspreise; für diese Strategie kann auf Währungsfutures ausgewichen werden.
- Aus dem Orderflow je Transaktion werden der kumulative oder der durchschnittliche Orderflow über ein Look-back berechnet, um die Preisrichtung vorherzusagen.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Ein fehlerhafter Bid von 110 Dollar kann eine Short-Market-Sell-Order auslösen, die bei 100 Dollar gefüllt wird, weil kein Bid bei 110 Dollar vorhanden war.
- Ein wahrer Spread von 5 Dollar zwischen Ask 105 Dollar und Bid 100 Dollar kann zu klein sein, um eine Market Order zum Kauf von X und Verkauf von Y auszulösen; ein auf 6 Dollar verfälschter Spread, 20 Prozent darüber, kann sie auslösen.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 173–186 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-013-p173-p186|S. 173–186]]

## Verwandte Themen
