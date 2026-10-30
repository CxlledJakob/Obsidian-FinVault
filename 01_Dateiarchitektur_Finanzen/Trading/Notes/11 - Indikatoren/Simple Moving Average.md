---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/11 - Indikatoren/11 - Indikatoren|11 - Indikatoren]]"
weitere_hauptthemen: []
unterthema: "Trendindikatoren"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Simple Moving Average


## Kurzdefinition

- Ein Simple Moving Average ist der Durchschnittspreis eines handelbaren Instruments über einen festgelegten Zeitraum.

## Kernaussagen


## Funktionsweise

- Ein Fünf-Tage-Durchschnitt addiert die Schlusskurse der letzten fünf Tage und teilt durch fünf.
- Auch bei einem Hurst-Exponenten zwischen 0 und 0,5 steigt die Varianz mit der Zeit, nur langsamer als bei einem geometrischen Random Walk; der gleitende Durchschnitt passt sich an und nimmt Gewinne schneller mit.

## Voraussetzungen


## Anwendung im Trading

- Im Buy-on-Gap muss der Eröffnungskurs über dem 20-Tage-Durchschnitt der Schlusskurse liegen; im Code ist der Look-back 20 und der Durchschnitt um einen Tag verschoben.
- Ein Kurs über einem langfristigen gleitenden Durchschnitt zieht Verkaufsdruck größerer Akteure wie Long-only-Fonds an.
- In der SPY-Komponenten-Arbitrage ist der Look-back für den gleitenden Durchschnitt und die Standardabweichung des Portfoliomarktwerts auf 5 fixiert, mit dem Vorteil des Hindsight.
- Im Währungspaar und im AUD.CAD-Beispiel werden gleitender Durchschnitt und Standardabweichung mit einem Look-back von 20 Tagen berechnet.
- Beim CL-Kalender-Spread wird der Look-back des gleitenden Durchschnitts von γ auf die gerundete Halbwertszeit gesetzt, etwa 36 Tage.
- Die lineare Mean-Reversion-Strategie auf dem VX-Kalenderspread verwendet einen Lookback von 15 Tagen für den gleitenden Durchschnitt und die Standardabweichungen.

## Regeln und Kriterien

- Der Lookback von gleitendem Durchschnitt und gleitender Standardabweichung kann gleich der Halbwertszeit der Mean Reversion gesetzt werden.
- Bei einer Halbwertszeit von 20 Tagen soll kein Lookback von 5 Tagen verwendet werden; ein kleines Vielfaches der Halbwertszeit ist oft nahe am Optimum und erspart die Optimierung des freien Parameters.
- Der Mittelwert kann sich langsam ändern, etwa durch die Wirtschaft oder das Unternehmensmanagement, deshalb wird ein gleitender statt ein fester Durchschnitt verwendet.
- Der Lookback des gleitenden Durchschnitts des Portfoliopreises wird auf die gerundete Halbwertszeit gesetzt.
- Dieser Lookback ist eine Eigenschaft der Preisreihe und kein an der Strategie optimierter Parameter.

## Risiken und Grenzen

- Alle Preise zählen gleich, ohne Unterschied zwischen Preisen auf niedrigem oder hohem Volumen.
- Auch die Auktionsrichtung des Tages bleibt unberücksichtigt, wodurch die Information stark in die Irre führen kann.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Markets in Profile_ Profiting from the Auction Process.pdf, S. 120–139 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-010-p120-p139|S. 120–139]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]

## Verwandte Themen
