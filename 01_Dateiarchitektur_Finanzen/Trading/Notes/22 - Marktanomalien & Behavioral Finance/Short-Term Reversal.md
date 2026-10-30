---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/22 - Marktanomalien & Behavioral Finance/22 - Marktanomalien & Behavioral Finance|22 - Marktanomalien & Behavioral Finance]]"
weitere_hauptthemen: []
unterthema: "Renditeanomalien"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Short-Term Reversal


## Kurzdefinition

- Kurzfristige oder saisonale Mean Reversion ist die Umkehr, die bei den meisten Aktien unter normalen Umständen, also ohne Nachricht, intraday auftritt, obwohl die Preise langfristig geometrischen Random Walks folgen.

## Kernaussagen

- Cross-sectional Mean Reversion impliziert, dass die kurzfristigen relativen Renditen der Instrumente eines Korbs seriell antikorreliert sind.
- Die relative Rendite eines Instruments ist seine Rendite minus der Rendite des Korbs.
- Dieses Phänomen tritt am häufigsten bei Aktienkörben auf und wird in Kapitel 4 bei mean-reverting Strategien für Aktien und ETFs behandelt.
- Käufer überverkaufter Aktien können überdurchschnittliche kurzfristige Renditen erzielen. Michael Cooper zeigt das an Aktien, die negatives Preismomentum bei fallendem Handelsvolumen aufweisen.
- Aktien, die über die vorangegangenen zwei Wochen bei fallendem Volumen scharf gefallen sind, zeigen eine systematische Neigung, über die folgende Woche zu steigen.
- Das fallende Volumen ist plausibel, weil es bedeutet, dass nicht genügend Käufer vorhanden sind, um den akuten Bedarf der Verkäufer zu decken. Die Überschussrenditen erscheinen als Liquiditätsprämie.
- Die Long- und Short-Portfolios wurden in einer Walk-forward-out-of-sample-Simulation über 1978 bis 1993 gebildet, um Data Mining zu begegnen, aus 300 Aktien großer Kapitalisierung.
- Diese Long-Short-Portfolios erzielten eine annualisierte Rendite von 44,95 Prozent gegen eine Buy-and-hold-Benchmark von 17,91 Prozent.
- Gegentrend-Strategien, die Aktien kaufen, welche über die jüngere Vergangenheit sehr schwach waren, identifizieren Papiere mit einer systematischen Neigung, über die nahe Frist zu steigen. In einem effizienten Markt ist das die Bezahlung für das Stellen von Liquidität und kein kostenloses Muster.
- Jacobs und Levy isolierten mit multipler Regression den reinen Return-Reversal-Effekt und fanden ihn als einen der stärksten und beständigsten Prädiktoren der relativen Aktienperformance.
- Aktien, die über den vergangenen Monat schwach waren, neigen über den folgenden Monat zu positiver relativer Performance.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Buy-on-Gap kauft Aktien, die vom Vortagestief zum Open um mehr als eine Standardabweichung der 90-Tage-Close-to-Close-Renditen gefallen sind, deren Open über dem 20-Tage-Schlussdurchschnitt liegt, nimmt davon die 10 schwächsten und liquidiert zum Schluss.
- Die Begründung ist unverhältnismäßiger Panikverkauf zum Open, wenn die Index-Futures vorbörslich unten sind, und eine allmähliche Erholung über den Tag.
- Querschnittlich folgt auf relative Unterperformance relative Überperformance und umgekehrt, gemessen als Rendite minus Durchschnitt des Universums.

## Risiken und Grenzen

- Starke Rückgänge kehren seltener um als kleine, weil sie oft an negativen Nachrichten liegen; die Strategie kann deshalb in einem nachrichtenreichen Umfeld bestehen, in dem traditioneller mehrtägiger Aktienpaarhandel wahrscheinlich scheitert.
- Die Autorenfassung ohne den Momentum-Filter litt ab 2009 unter nachlassenden Renditen, die long-only-Seite stellt Risikomanagement-Probleme, und die geringe Titelzahl je Tag begrenzt die Kapazität.

## Beispiele

- Buy-on-Gap: APR 8,7 Prozent und Sharpe Ratio 1,5 vom 11. Mai 2006 bis 24. April 2012; die Short-Spiegelung: APR 46 Prozent und Sharpe Ratio 1,27.
- Das lineare Long-Short, das relative Gewinner shortet und relative Verlierer kauft, hat auf dem SPX eine APR von 13,7 Prozent und eine Sharpe Ratio von 1,3; die Intraday-Fassung hat eine APR von 73 Prozent und eine Sharpe Ratio von 4,7.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 381–400 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-021-p381-p400|S. 381–400]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 457–476 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-025-p457-p476|S. 457–476]]

## Verwandte Themen
