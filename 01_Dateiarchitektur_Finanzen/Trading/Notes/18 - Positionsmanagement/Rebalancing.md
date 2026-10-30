---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/18 - Positionsmanagement/18 - Positionsmanagement|18 - Positionsmanagement]]"
weitere_hauptthemen: []
unterthema: "Portfolioführung"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Rebalancing


## Kurzdefinition


## Kernaussagen

- Das Portfolio muss nicht jeden Tag aus derselben festen Instrumentenmenge oder denselben Gewichten bestehen; bei vielen Aktienportfolio-Strategien kommt der Vorteil gerade aus der täglichen Auswahl oder Neugewichtung.
- Das tägliche Rebalancing gehebelter ETFs erzeugt kurzfristiges Momentum.
- Nahe dem Schluss verkauft der Sponsor bei negativer Portfoliorendite die Komponenten und kauft bei positiver.
- Eine große Indexänderung erzeugt Momentum in derselben Richtung für gehebelte Long- und Short-ETFs, weil der Short-ETF bei steigendem Index Shorts abbaut und damit kauft.
- Indexänderungen erzwingen Käufe bei Aufnahme und Verkäufe bei Löschung und erzeugen unmittelbar danach Momentum.
- Das Schlusskapitel nennt das Rebalancing gehebelter ETFs zum Handelsschluss als ausnutzbare Unvollkommenheit, neben der Regression zum Mittel und den Roll Returns bei Futures.
- Kelly auf jede Strategie einzeln enthebelt schlecht laufende Strategien schnell.
- Die Allokation über das Gesamtportfolio lässt gute Strategien schlechte kurzfristig subventionieren und ist mathematisch nur bei unveränderten Erwartungen optimal.

## Funktionsweise

- Werden die Kapitalgewichte eines Log-Preis-Portfolios konstant gehalten, muss bei t rebalanciert werden: Gewinne oder Verluste werden realisiert und der Kasse zu- oder abgebucht.
- Von t minus 1 nach t ändert die Kasse ihren Marktwert durch die Marktbewegung nicht; sie ändert sich erst im Rebalancing.
- Den Marktwert dieses Portfolios stationär, aber nicht konstant zu halten, verlangt deshalb fortlaufendes Rebalancing, und das folgt aus der Verwendung der Logpreise.
- Konstanter Hebel erzwingt nach positivem Gewinn und Verlust Nachkäufe und nach negativem Verkäufe in den Verlust.
- Im Beispiel mit 100.000 Dollar Startkapital, Hebel 5 und Tagesverlust von 10.000 Dollar werden zusätzlich 40.000 Dollar liquidiert, damit der Marktwert 450.000 Dollar beträgt.
- Nach anschließendem Gewinn von 20.000 Dollar werden 80.000 Dollar Wertpapiere ergänzt, um auf 550.000 Dollar Marktwert zu kommen.
- Bei CPPI wird das Handels-Subkonto nur bei einem neuen High Water Mark wieder auf den Anteil D des Gesamtkapitals aufgefüllt; bei Verlusten fließt kein Cash zurück.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Sobald die Shorts 25 Prozent oder 35 Prozent erreichen, wird auf 70 Prozent long und 30 Prozent short umgeschichtet.
- Das SPY-Portfolio wird jeden Tag rebalanciert, sodass das Kapital je Aktie konstant bleibt; deshalb läuft der zweite Johansen-Test auf Logpreisen.
- Das lineare Long-Short investiert jeden Tag dasselbe Bruttokapital von 1 Dollar, neu gewichtet nach den relativen Tagesrenditen.
- Ein vollständigerer Backtest der SPY-Arbitrage kann die Hedge Ratios dynamisch aktualisieren und dabei neue Bestandteilaktien wählen.
- Ein RMZ-Portfolio mit konstantem Hebel 3 muss nach einem starken Fall Aktien verkaufen und nach einem Anstieg kaufen, besonders zum Marktschluss.
- Die Teststrategie kauft DRN bei mehr als 2 Prozent Rendite vom Vortagesschluss bis 15 Minuten vor Schluss und verkauft bei weniger als minus 2 Prozent; der Exit liegt am Schluss.

## Risiken und Grenzen

- Die lineare Strategie ist wegen des ständigen infinitesimalen Rebalancings und der unbegrenzten Kaufkraft unpraktisch.
- Die ausgewiesenen 9 Prozent APR und die Sharpe Ratio von 0,5 des Log-Preis-Spreads gelten vor den zusätzlichen Transaktionskosten des täglichen Rebalancings, das die Kapitalzuteilung je ETF erhält.
- Preis-Spreads sind einfacher als Log-Preis-Spreads, weil sie dieses ständige Rebalancing nicht erzwingen.
- Große Mittelzuflüsse in gehebelte Long-ETFs erzeugen positives Momentum der Basiswerte, Zuflüsse in inverse ETFs negatives Momentum.
- Verkäufe der Long-ETFs an einem starken Aufwärtstag könnten das Rebalancing-Momentum neutralisieren; die Backtests zeigen, dass das nicht oft geschah.
- Der Effekt trifft auch ungehebelte ETFs wie SPY nahe dem Schluss; der gehebelte ETF vergrößert ihn nur.
- Dieses Verkaufen in Verluste gilt als Ansteckungskanal von Krisen, unter anderem für den Quant-Einbruch im August 2007, weil ähnliche Bücher vieler Fonds eine Liquidationsspirale auslösen.

## Beispiele

- Ende Januar 2009 lag das Vermögen gehebelter ETFs bei 19 Milliarden Dollar; 1 Prozent Bewegung im SPX erzwingt Käufe oder Verkäufe von etwa 17 Prozent des Market-on-Close-Volumens.
- DRN selbst lieferte vom 12. Oktober 2011 bis 25. Oktober 2012 eine APR von 15 Prozent und eine Sharpe Ratio von 1,8.

## Unterschiedliche Quellenpositionen

- Manche Forscher sahen den Drift nach Indexänderungen über viele Tage; jüngere Tests des Autors sehen ihn nur noch intraday (Shankar und Miller, 2006).

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Markets in Profile_ Profiting from the Auction Process.pdf, S. 214–225 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-016-p214-p225|S. 214–225]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 173–186 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-013-p173-p186|S. 173–186]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]

## Verwandte Themen

- Diversifikation
- Exposure-Limit
