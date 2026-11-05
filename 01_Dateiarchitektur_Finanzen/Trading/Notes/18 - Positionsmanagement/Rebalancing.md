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
aktualisiert: 2026-11-05
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
- Mean-Reversion-Handel mit Preisspreads ist einfacher als mit Logpreisspreads, weil nur die Logversion die Kapitalgewichte konstant halten muss und deshalb fortlaufendes Rebalancing erzwingt.
- Im GLD-USO-Vergleich liegt der Logpreisspread bei 9 Prozent APR und einer Sharpe Ratio von 0,5, unter den etwa 10,9 Prozent und 0,59 des Preisspreads, und das bevor die zusätzlichen Transaktionskosten des täglichen Rebalancings abgezogen sind.
- Die lineare Strategie selbst ist unpraktisch, weil sie ständig infinitesimal rebalanciert und unbegrenzte Kaufkraft verlangt.
- Konstanter Hebel 3 auf einem Portfolio, das den MSCI US REIT Index RMZ abbildet, erzwingt nach einem starken Tagesverlust Verkäufe über das Buch und nach einem Anstieg Käufe, besonders zum Handelsschluss.
- Die Teststrategie kauft DRN, wenn die Rendite vom Vortagesschluss bis 15 Minuten vor Schluss größer als 2 Prozent ist, und verkauft unter minus 2 Prozent, mit Ausstieg am Schluss.
- Vom 12. Oktober 2011 bis 25. Oktober 2012 beträgt die APR 15 Prozent und die Sharpe Ratio 1,8.
- Das Momentum stammt aus den zugrunde liegenden Aktien und sollte auch ungehebelte ETFs wie SPY nahe dem Schluss treffen; der gehebelte ETF vergrößert nur den Effekt.
- Die Rendite sollte mit dem aggregierten Vermögen aller gehebelten ETFs steigen; Ende Januar 2009 betrug es 19 Milliarden Dollar, Long und Short, nach Cheng und Madhavan 2009.
- Eine Bewegung des SPX um 1 Prozent erzwingt Käufe oder Verkäufe von etwa 17 Prozent des Market-on-Close-Volumens.
- Ein großer Mittelzufluss in gehebelte Long-ETFs erzeugt positives Momentum der Aktien, ein Zufluss in inverse ETFs negatives.
- Ein Verkauf gehebelter Long-ETFs am Tag eines starken Indexanstiegs könnte das Momentum neutralisieren; die Backtests zeigen, dass das nicht oft geschah.
- Eine aktuellere Analyse veröffentlichten Rodier, Haryanto, Shum und Hejazi 2012.
- Konstanter Hebel 5 auf zunächst 100.000 Dollar verlangt nach einem Verlust von 10.000 Dollar die Liquidation weiterer 40.000 Dollar, damit der Marktwert 450.000 Dollar beträgt, und nach einem anschließenden Gewinn von 20.000 Dollar den Zukauf von 80.000 Dollar, damit er 550.000 Dollar beträgt.
- Dieses Verkaufen in die Verluste wird als Ansteckungskanal der Quant-Krise vom August 2007 genannt, nach Khandani und Lo 2007: Fonds mit ähnlichen Positionen liquidieren nacheinander und verstärken die Verluste.
- Unter einer Bruttohebel-Grenze, die weit unter der Summe der Kelly-Hebel liegt, ist das proportionale Herunterskalieren aller Strategien oft nicht wachstumsmaximal; dann geht die Kaufkraft in die Strategie mit der höchsten Wachstumsrate.
- CPPI setzt das Handels-Unterkonto nur bei einem neuen High Water Mark wieder auf den Anteil D auf und überträgt bei Verlusten kein Cash; die Ordergröße fällt dadurch schneller als bei einem festen Hebel f mal D auf dem Gesamtkonto.
- CPPI auf einem Mehrstrategien-Konto kann dazu führen, dass profitable Strategien unprofitable subventionieren und der Drawdown das ganze Bündel nie abschaltet.

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
- Die Kurs-Gewinn-Dezile des MSCI-World-Tests von 1980 bis 2005 werden jährlich zu Jahresbeginn neu gebildet und ein Jahr gehalten. Die Kosten dieser Rechnung werden ignoriert und wegen des jährlichen Rebalancings als niedrig eingeschätzt.

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
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 76–95 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-006-p076-p095|S. 76–95]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 166–179 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-013-p166-p179|S. 166–179]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 180–199 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-014-p180-p199|S. 180–199]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 343–362 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-019-p343-p362|S. 343–362]]

## Verwandte Themen

- Diversifikation
- Exposure-Limit
