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
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 1–20 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-001-p001-p020|S. 1–20]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 20–39 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-002-p020-p039|S. 20–39]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 134–153 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-008-p134-p153|S. 134–153]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 210–229 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-012-p210-p229|S. 210–229]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 362–381 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-020-p362-p381|S. 362–381]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 381–400 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-021-p381-p400|S. 381–400]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 400–419 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-022-p400-p419|S. 400–419]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 457–476 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-025-p457-p476|S. 457–476]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]

## Verwandte Themen
