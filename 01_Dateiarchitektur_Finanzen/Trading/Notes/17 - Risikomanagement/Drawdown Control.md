---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/17 - Risikomanagement/17 - Risikomanagement|17 - Risikomanagement]]"
weitere_hauptthemen: []
unterthema: "Portfoliorisiko"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-01
---

# Drawdown Control


## Kurzdefinition


## Kernaussagen

- Manchmal zwingt die Realität, den maximalen Drawdown eines Kontos zu begrenzen.
- Ein Weg ist der Stop-Loss, der oft problematisch ist; der andere ist Constant Proportion Portfolio Insurance, die neben der Begrenzung großer Drawdowns die Upside maximieren will.
- Kunden oder Arbeitgeber geben oft vor, dass der Betrag des Drawdowns vom historischen Höchststand ein Maximum nie überschreitet.
- Diese Vorgabe ist eine zusätzliche Nebenbedingung der Hebeloptimierung.
- Sie lässt sich nicht umsetzen, indem der unbeschränkte Optimalhebel einfach mit dem Verhältnis aus erlaubtem und ursprünglichem maximalem Drawdown multipliziert wird.
- Im Simulationsbeispiel ist der maximale Drawdown minus 0,999 beim unbeschränkten optimalen Hebel 19,2. Der halbe Hebel 9,6 erzeugt immer noch minus 0,963; erst eine Kürzung um den Faktor 7 auf etwa 2,7 senkt den Betrag auf etwa 0,5. Die Zahlen hängen von der simulierten Reihe ab und sind nicht genau reproduzierbar.
- Auf den historischen Strategierenditen genügt eine Kürzung des unbeschränkten optimalen Hebels um den Faktor 1,5 auf 13, um den maximalen Drawdown unter minus 0,49 zu drücken.
- Simulierte Renditen ähneln dem Value-at-Risk großer Banken und Hedgefonds und haben höhere Signifikanz. Der simulierte Drawdown kann so selten sein, dass er in einer Million Jahren kaum eintritt, und serielle Korrelationen der Historie fehlen, die den realen Drawdown senken können.
- Historische Renditen erfassen diese Korrelationen und eine realistische Lebensdauer, enthalten aber zu wenig Daten für den Worst Case; ein Kompromisshebel liegt zwischen beiden Schätzungen.
- In einer Simulation mit D gleich 0,5 bleibt der Drawdown von CPPI konstruktionsbedingt unter 0,5, während das alternative Schema ohne Stop-Loss selbst mit halbem Optimalhebel 0,9 erreicht.
- Durch den Kelly-Hebel auf dem Unterkonto senkt CPPI die Ordergröße so schnell, dass das Konto sich dem maximalen Drawdown minus D fast nicht nähern kann.
- CPPI gilt nur für ein Konto mit einer Strategie. Bei mehreren Strategien können profitable die unprofitablen subventionieren, sodass der Drawdown nie groß genug wird, um das ganze Bündel abzuschalten, außer die verlierende Strategie gesundet wieder.
- Es gibt zwei Stop-Loss-Gebräuche zur Drawdown-Begrenzung: der übliche verlässt nur die Position, wenn der unrealisierte Gewinn und Verlust unter eine Schwelle fällt, und erlaubt später einen neuen Einstieg; der seltenere verlässt die ganze Strategie einmalig, wenn der Drawdown unter eine Schwelle fällt, und CPPI ist für diesen Schutz vorzuziehen.
- Am Flash Crash des 6. Mai 2010 zogen die Liquiditätsanbieter zugleich die Liquidität ab; moderne Market Maker mussten nur ein Bid von 0,01 Dollar halten, und eine Sell-Stop-Order auf Accenture wurde zu 0,01 Dollar je Aktie ausgeführt.

## Funktionsweise

- Bei CPPI wird der Anteil D des Anfangskapitals für den Handel reserviert und mit dem Kelly-Hebel f gehebelt; 1 minus D bleibt Cash.
- Damit ist der Drawdown des Gesamtkontos auf minus D begrenzt, und bei null im Handels-Subkonto wird die Strategie aufgegeben.
- Erreicht das Gesamtkonto ein neues High Water Mark, wird das Subkonto wieder auf den Anteil D aufgefüllt; bei Verlusten fließt kein Cash zwischen Cash- und Handelskonto.
- Das ist ein geordneter Weg, eine verlierende Strategie herunterzufahren, statt über den emotionalen Zusammenbruch des Managers.
- Solange ein Drawdown besteht, senkt CPPI die Ordergröße viel schneller als der gesenkte Hebel auf dem Gesamtkonto.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Der aus der Simulation abgeleitete Höchsthebel verhindert nur, dass der simulierte Drawdown das Maximum überschreitet, nicht der künftige.
- Garantieren, dass der künftige Drawdown das Maximum nicht überschreitet, lässt sich nur mit CPPI oder mit einem Stop-Loss.
- CPPI ist nicht dasselbe wie der Hebel f mal D auf dem Gesamtkonto; selbst ein Stop bei minus D erzeugt nicht dieselbe zusammengesetzte Rendite, außer jede Periode ist positiv.
- CPPI gilt nur für ein Konto mit einer Strategie; bei mehreren können profitable Strategien unprofitable so subventionieren, dass der Drawdown das Bündel nie abschaltet.
- CPPI und Stop-Loss verhindern einen großen Drawdown über das Overnight-Gap oder bei ausgesetztem Handel nicht; Out-of-the-Money-Optionen vor einem erwarteten Schluss können einen Teil dieses Risikos beseitigen.

## Beispiele

- Im Simulationsbeispiel ist der maximale Drawdown bei unbeschränktem f von 19,2 gleich minus 0,999; der halbe Hebel 9,6 erzeugt noch minus 0,963.
- Erst eine Senkung um den Faktor 7 auf etwa 2,7 drückt den Betrag auf etwa 0,5; die Zahlen hängen von der simulierten Reihe ab und sind nicht exakt reproduzierbar.
- An historischen Strategierenditen reichte der Faktor 1,5, also Hebel 13, für einen maximalen Drawdown unter minus 0,49.
- Nach 100.000 Tagen bleibt der CPPI-Drawdown bei D gleich 0,5 betragsmäßig unter 0,5, während die Alternative ohne Stop-Loss selbst mit halbem Optimalhebel auf 0,9 kommt.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 180–199 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-014-p180-p199|S. 180–199]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 199–214 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-015-p199-p214|S. 199–214]]

## Verwandte Themen
