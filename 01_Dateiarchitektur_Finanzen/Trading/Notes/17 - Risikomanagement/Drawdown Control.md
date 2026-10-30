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
aktualisiert: 2026-10-30
---

# Drawdown Control


## Kurzdefinition


## Kernaussagen

- Manchmal zwingt die Realität, den maximalen Drawdown eines Kontos zu begrenzen.
- Ein Weg ist der Stop-Loss, der oft problematisch ist; der andere ist Constant Proportion Portfolio Insurance, die neben der Begrenzung großer Drawdowns die Upside maximieren will.
- Kunden oder Arbeitgeber geben oft vor, dass der Betrag des Drawdowns vom historischen Höchststand ein Maximum nie überschreitet.
- Diese Vorgabe ist eine zusätzliche Nebenbedingung der Hebeloptimierung.
- Sie lässt sich nicht umsetzen, indem der unbeschränkte Optimalhebel einfach mit dem Verhältnis aus erlaubtem und ursprünglichem maximalem Drawdown multipliziert wird.

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

## Verwandte Themen
