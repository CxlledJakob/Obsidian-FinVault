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

# Signaldefinition


## Kurzdefinition

- Das Signal ist der negative Z-Score des Preises des Einheitsportfolios: Nettomarktwert minus gleitender Durchschnitt, geteilt durch die gleitende Standardabweichung, mit negativem Vorzeichen.

## Kernaussagen


## Funktionsweise

- Bei Paar- und anderen Arbitragestrategien hängen die Handelssignale oft von den Differenzen der Preisquotes verschiedener Instrumente ab.
- Bei Währungspaaren ist oft das Ratio statt des Spreads ein guter Indikator.
- Eine praktische Umsetzung einer linearen Handelsstrategie sind Bollinger-Bänder mit Scaling-in.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Der Lookback von Durchschnitt und Standardabweichung wird auf die gerundete Halbwertszeit gesetzt und nicht frei optimiert.
- Der Preis des Einheitsportfolios ist sein Marktwert, analog zum Preis eines Fonds oder ETF.
- Linear bedeutet, dass die Stückzahl proportional zum Z-Score ist, nicht der Marktwert der Anlage.

## Risiken und Grenzen

- Ein Datenfehler, der einen Spread von 5 auf 6 Dollar erhöht, also um 20 Prozent, kann ein Signal auslösen, das der wahre Spread nicht ausgelöst hätte.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]

## Verwandte Themen
