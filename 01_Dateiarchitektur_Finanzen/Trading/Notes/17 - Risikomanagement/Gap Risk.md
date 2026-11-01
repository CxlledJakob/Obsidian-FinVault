---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/17 - Risikomanagement/17 - Risikomanagement|17 - Risikomanagement]]"
weitere_hauptthemen: []
unterthema: "Risikomessung"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-01
---

# Gap Risk


## Kurzdefinition


## Kernaussagen

- CPPI und der Stop-Loss können einen großen Drawdown über das Overnight-Gap oder bei ausgesetztem Handel nicht verhindern.
- Käufe von Out-of-the-Money-Optionen vor einem erwarteten Marktschluss können einen Teil dieses Risikos beseitigen.
- Ein Stop-Loss hält den unrealisierten Gewinn und Verlust nur dann im selbst gesetzten Limit, wenn der Markt offen ist, solange die Position gehalten wird.
- Das Aneinanderhängen der Front-Month-Preise erzeugt vom letzten Tag vor dem Rollover zum Rollover-Tag oft eine erhebliche Preislücke und damit im Backtest eine falsche Rendite oder einen falschen P&L.

## Funktionsweise

- Die Preis-Rückanpassung addiert q(T+1) minus p(T+1) zu jedem Preis am oder vor T, sodass die Änderung von T nach T+1 gleich p(T+1) minus p(T) ist; die Rendite auf der angepassten Reihe ist dann (p(T+1) minus p(T)) geteilt durch (p(T) plus q(T+1) minus p(T+1)) und nicht durch p(T).
- Die Rendite-Rückanpassung multipliziert jeden Preis am oder vor T mit q(T+1)/p(T+1) und macht damit die Rendite richtig und den P&L falsch.

## Voraussetzungen

- Wirksam ist er ohne Overnight-Positionen oder in Währungen und manchen Futures, deren elektronischer Markt außer an Wochenenden und Feiertagen immer offen ist.

## Anwendung im Trading

- Devisen werden zumindest fünf Tage die Woche von Sonntag 17:00 Uhr ET bis Freitag 17:00 Uhr ET gehandelt, ET als EDT oder EST, also GMT minus 4 oder GMT minus 5; deshalb lassen sich Stops dort sinnvoll einsetzen.

## Regeln und Kriterien


## Risiken und Grenzen

- Ist ein Markt lange geschlossen, sind Stop-Losses nutzlos, weil der Markt bei der Wiedereröffnung nach oben oder unten gappen kann.
- Gapt der Preis bei der Wiedereröffnung, kann der Stop zu einem viel schlechteren Preis ausgeführt werden, als der maximal erlaubte Verlust vorschreibt.
- Optionskäufe, die dieses Risiko beseitigen, können teuer sein und lohnen nur für erwartete Marktschließungen.
- Preis-Rückanpassung kann in der fernen Vergangenheit negative Preise erzeugen; ein additives Konstanten-Offset auf alle Preise verhindert das, erschwert aber die Renditerechnung.
- In extremen Umständen ist ein Stop-Loss auch bei geöffnetem Markt nutzlos, wenn alle Liquiditätsanbieter ihre Liquidität gleichzeitig zurückziehen.
- Beim Flash Crash am 6. Mai 2010 mussten Market Maker in Zeiten von Marktstress nur ein Gebot von 0,01 US-Dollar halten, die sogenannte Stub Quote (Arnuk und Saluzzi, 2012).
- Eine Verkaufs-Stop-Order auf Accenture, ein Unternehmen mit einem Umsatz von mehreren Milliarden US-Dollar, wurde an diesem Tag zu 0,01 US-Dollar je Aktie ausgeführt.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 14–33 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-002-p014-p033|S. 14–33]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 180–199 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-014-p180-p199|S. 180–199]]

## Verwandte Themen
