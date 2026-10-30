---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/12 - Momentum/12 - Momentum|12 - Momentum]]"
weitere_hauptthemen: []
unterthema: "Relative Stärke"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Momentum Ranking


## Kurzdefinition


## Kernaussagen

- Portfolios aus Futures oder Aktien zeigen oft querschnittliches Momentum, und ein einfacher Rang-Algorithmus auf Basis der Renditen genügt.

## Funktionsweise

- Täglich wird die 12-Monats-Rendite, 252 Handelstage, von 52 physischen Rohstoffen rangiert; der Future mit der höchsten Rendite wird einen Monat, 25 Handelstage, long gehalten und der mit der niedrigsten short.
- Bei US-Aktien werden die Titel im obersten Dezil der um 12 Monate verzögerten Renditen einen Monat gekauft und die im untersten Dezil geshortet.
- Beispiel 6.2 sortiert die Renditen aufsteigend, schließt fehlende Werte aus, geht die obersten 50 Titel long und die untersten 50 short, bei Lookback 252 und Haltedauer 25 auf den S&P-500-Titeln.
- Statt nach verzögerten Renditen kann nach anderen Faktoren rangiert werden, fundamental nach Gewinnwachstum oder Buchwert zu Preis oder statistisch nach einer Hauptkomponentenanalyse.
- Beim PRESSURE-Faktor werden Aktien im untersten Dezil, also mit dem höchsten Verkaufsdruck, geshortet und Aktien im obersten Dezil, also mit dem höchsten Kaufdruck, gekauft.
- Buy(j, i, t) ist 1, wenn Fonds j die Haltung in Aktie i im Quartal t erhöht hat und die Zuflüsse mehr als 5 Prozent des Nettoinventarwerts betragen, sonst 0; Sell ist analog für Senkungen der Haltung definiert, und die Summe Own(j, i, t minus 1) ist die Zahl der Fonds, die die Aktie zu Beginn des Quartals halten.
- Buy ist binär und berücksichtigt die Fondsgröße nicht; der Text lässt offen, ob eine Gewichtung mit dem Nettoinventarwert bessere Ergebnisse brächte.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Das Rohstoff-Ranking erzielt vom 1. Juni 2005 bis zum 31. Dezember 2007 eine annualisierte Rendite von 18 Prozent bei einer Sharpe Ratio von 1,37 und vom 2. Januar 2008 bis zum 31. Dezember 2009 minus 33 Prozent.
- Das Aktien-Ranking in Beispiel 6.2 erzielt vom 15. Mai 2007 bis zum 31. Dezember 2007 37 Prozent annualisiert bei einer Sharpe Ratio von 4,1 und vom 2. Januar 2008 bis zum 31. Dezember 2009 minus 30 Prozent.
- Das PRESSURE-Ranking erzielt vor Kosten etwa 17 Prozent annualisiert und wird vierteljährlich neu gebildet, weil Holdings-Daten in der Regel nur vierteljährlich vorliegen.
- Saubere Holdings- und Renditedaten dafür kommen vom Center for Research in Security Prices und kosten etwa 10.000 Dollar pro Datenjahr.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]

## Verwandte Themen
