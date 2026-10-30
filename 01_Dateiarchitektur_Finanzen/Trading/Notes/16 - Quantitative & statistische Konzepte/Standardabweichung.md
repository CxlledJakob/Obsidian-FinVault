---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Statistik"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Standardabweichung


## Kurzdefinition

- Die Value Area entspricht etwa einer Standardabweichung.

## Kernaussagen

- Diese Spanne trennt Preis und Value: Innerhalb gelten sie als dasselbe, außerhalb liegt der Preis von der Value entfernt.
- Die Value Area ist die Spanne, in der etwa 70 Prozent des Volumens lagen, und entspricht einer Standardabweichung der Glockenkurve.
- Die Bänder entsprechen einer Standardabweichung über und unter dem Moving Average, der als Mean gilt.
- Oberes und unteres Band werden daraus als Kursziele abgeleitet.
- Selbst eine stationäre Reihe mit Hurst-Exponent zwischen 0 und 0,5 hat eine Varianz, die mit der Zeit steigt, nur langsamer als beim geometrischen Random Walk; die gleitende Standardabweichung passt sich daran an.
- Die Standardabweichung der Residuen der ES-VX-Regression beträgt 2.047 Dollar.
- Die Bollinger-Band-ähnliche Strategie shortet das Portfolio, sobald dessen Wert um eine Standardabweichung dieser im Trainingsset bestimmten Residuen abweicht.
- Für die lineare Mean-Reversion-Strategie auf VX beträgt der Lookback der Standardabweichungen 15 Tage.

## Funktionsweise

- Unter der Gauß-Nullhypothese ist der Mittelwert null, und die Standardabweichung ist die Stichproben-Standardabweichung der Tagesrenditen.
- Die Teststatistik teilt den Mittelwert durch diese Standardabweichung und multipliziert mit der Wurzel der Zahl der Datenpunkte.
- Die simulierten Tagesrenditen des zweiten Tests haben dieselbe Standardabweichung wie die beobachteten Futures-Renditen.
- Der Z-Score eines Faktors ist der Faktor minus seinem historischen Mittelwert, geteilt durch seine historische Standardabweichung, und diese Momente werden mit In-Sample-Daten berechnet.
- Die Prognose der Ein-Tages-Rendite skaliert die gemittelten vorzeichenbehafteten Z-Scores mit der historischen Standardabweichung der Ein-Tages-Renditen und addiert deren historischen Mittelwert.
- Die normalisierte Abweichung der linearen Strategie ist der Preis minus gleitender Durchschnitt, geteilt durch die gleitende Standardabweichung.
- Der Lookback dieser gleitenden Standardabweichung kann gleich der Halbwertszeit gesetzt werden.
- Der Z-Score des Einheitsportfolios teilt die Abweichung vom gleitenden Durchschnitt durch die gleitende Standardabweichung über denselben Lookback, die gerundete Halbwertszeit.
- Der Bollinger-Einstieg liegt mehr als entryZscore Standardabweichungen vom Mittel entfernt, der Ausstieg bei exitZscore Standardabweichungen, und beide Größen werden über den Lookback geschätzt.
- Der Z-Score ist Portfoliopreis minus gleitender Durchschnitt, geteilt durch die gleitende Standardabweichung.
- Beim Kalman-Filter ersetzt die Standardabweichung des Prognosefehlers, die Wurzel aus Q, die gleitende Standardabweichung des Bollinger-Bands.
- Im Market-Making-Modell ist Q die Varianz des Mittelpreis-Fehlers plus Ve.
- Die Varianz des Prognosefehlers im Kalman-Filter ist Q(t) gleich Var(m(t)) plus Ve.
- Der Kalman-Gain ist K(t) gleich R(t gegeben t minus 1) geteilt durch diese Varianz plus Ve, und die Zustandsvarianz wird mit (1 minus K(t)) fortgeschrieben.

## Voraussetzungen


## Anwendung im Trading

- Für den Mean-Reversion-Handel einer einzelnen Preisreihe werden neben dem mittleren Preis die Standardabweichung dieser Reihe gesucht.
- Können Hedge Ratio, Mittel und Standardabweichung eines Spreads künftig variieren, werden ein gleitender Look-back oder der Kalman-Filter verwendet.
- Die Sharpe Ratio teilt die durchschnittliche Überschussrendite durch die Standardabweichung der Überschussrenditen, geeignet annualisiert.
- Im Währungspaar ist der Z-Score der Abstand des Portfolio-Marktwerts von seinem Mittel, geteilt durch die Standardabweichung über den Look-back von 20 Tagen, und die Positionsgröße ist das Negative dieses Z-Scores.
- Beim Kalender-Spread werden Mittel und Standardabweichung von γ über einen Look-back gleich der gerundeten Halbwertszeit berechnet, und der Z-Score ist die Abweichung geteilt durch diese gleitende Standardabweichung.

## Regeln und Kriterien

- Kleine Beträge von entryZscore und exitZscore, zusammen mit einem kurzen Lookback, verkürzen die Haltedauer und erhöhen in der Regel den Gewinn.
- Im Kalman-Beispiel mit kleinem δ ändert sich die Wurzel aus Q nur langsam, und die Schwellen liegen bei plus und minus dieser Wurzel.
- Buy-on-Gap wählt Aktien, deren Rendite vom Tief des Vortags zum heutigen Open kleiner als minus eine Standardabweichung liegt; diese Standardabweichung wird aus den täglichen Close-to-Close-Renditen der letzten 90 Tage berechnet, der Entry-Z-Score im Code ist 1, und die Kaufschwelle ist das Vortagestief mal (1 minus dieser Z-Score mal der Standardabweichung).
- Die Short-Variante verlangt ein Gap nach oben um eine Standardabweichung, bei einem Open, der noch unter dem 20-Tage-Durchschnitt liegt.
- In der SPY-Arbitrage ist die Zahl der Einheiten der negative Abstand des Log-Marktwerts vom gleitenden Mittel, geteilt durch die gleitende Standardabweichung, mit Look-back 5.

## Risiken und Grenzen


## Beispiele

- Auf GLD und USO werden entryZscore gleich 1 und exitZscore gleich 0 verwendet und erreichen 17,8 Prozent APR sowie eine Sharpe Ratio von 0,96.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Markets in Profile_ Profiting from the Auction Process.pdf, S. 36–49 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-004-p036-p049|S. 36–49]]
- Markets in Profile_ Profiting from the Auction Process.pdf, S. 62–79 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-006-p062-p079|S. 62–79]]
- Markets in Profile_ Profiting from the Auction Process.pdf, S. 120–139 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-010-p120-p139|S. 120–139]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]

## Verwandte Themen

- Value Area High
- Value Area Low
- Bollinger Bands
- Standardabweichungsbänder
