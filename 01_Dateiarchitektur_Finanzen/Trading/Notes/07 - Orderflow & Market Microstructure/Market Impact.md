---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/07 - Orderflow & Market Microstructure/07 - Orderflow & Market Microstructure|07 - Orderflow & Market Microstructure]]"
weitere_hauptthemen: []
unterthema: "Mikrostruktur"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-01
---

# Market Impact


## Kurzdefinition

- Market Impact ist der positive Zusammenhang zwischen Preisänderung und Orderflow-Ungleichgewicht.

## Kernaussagen

- Eine einzelne Order über einen ganzen großen Block am Hoch drückt den Preis und schmälert den Verkaufsgewinn.
- Kauf in großem Volumen hebt den Preis gegen den Käufer. Verkauf in großem Volumen drückt ihn gegen den Verkäufer.
- In einem illiquiden Titel oder einer illiquiden Währung tritt diese Gegenbewegung sehr schnell ein.
- Die zweite Modellgeneration untersucht, welchen Einfluss Volumen auf Preise hat; Beispiele sind Kyle (1985) und Amihud (2002).
- Diese Modelle achten auf signiertes Volumen und auf das Orderflow-Ungleichgewicht.
- In Kyles Modell erfasst λ den Preiseinfluss und wird über Δpt = λ (bt Vt) + εt auf dem signierten Volumen geschätzt.
- Amihud (2002) misst die tägliche Preisreaktion, die mit einem Dollar Handelsvolumen einhergeht, und nutzt sie als Proxy des Preiseinflusses.
- Eine genannte Umsetzung setzt den Betrag der logarithmischen Bar-Rendite gleich λ mal der Summe des Dollarvolumens der Trades in diesem Bar, plus einem Fehlerterm.
- Hasbrouck (2009) schätzt den Preiseinflusskoeffizienten auf Trade-and-Quote-Daten mit einem Gibbs-Sampler bayesianisch.
- Die Regression erklärt die Log-Preisänderung durch die Summe der vorzeichenbehafteten Quadratwurzeln des Dollarvolumens.
- Das so geschätzte λi nähert die effektiven Handelskosten an.
- Tägliche Amihud-Lambdas weisen eine hohe Rangkorrelation zu Intraday-Schätzungen des effektiven Spreads auf.
- Der Autor hält die t-Werte dieser mikrostrukturellen Schätzungen für informativer als die Mittelwerte, weil sie mit der Standardabweichung des Schätzfehlers skalieren.
- Eine Bewegung des SPX um 1 Prozent erzwingt nach Cheng und Madhavan (2009) Käufe oder Verkäufe im Umfang von etwa 17 Prozent des Market-on-Close-Volumens und hat damit signifikanten, momentum-erzeugenden Market Impact.
- Das Rebalancing gehebelter ETFs nahe dem Schluss erzeugt Momentum im Marktwert des Portfolios und in den Basiswerten.
- Momentum Ignition legt eine große Buy-Limit-Order auf den Best Bid, um Kaufdruck vorzutäuschen und andere zum Kauf am Ask zu bewegen.
- Zum Slippage gehört neben dem Bid-Ask-Spread der Betrag, um den die Order des Anlegers den Marktpreis schiebt, nach oben beim Kauf und nach unten beim Verkauf.
- Das Platzieren oder Ausführen einer Order kann das Verhalten der anderen Marktteilnehmer ändern, sodass der Gewinn einer Hochfrequenzstrategie selbst mit dem historischen Gesamtorderbuch von diesen Reaktionen abhängt.
- Wer große Größen handelt, verringert den Market Impact von Ein- und Ausstieg, wenn die Position schrittweise auf- und abgebaut wird.
- Cheng und Madhavan schätzen, dass eine Bewegung des SPX um 1 Prozent Käufe oder Verkäufe von etwa 17 Prozent des Market-on-Close-Volumens erzwingt und damit erheblichen, momentumtreibenden Market Impact hat.
- Das Rebalancing eines dreifach gehebelten ETF wie DRN mit über hundert Millionen Dollar Eigenkapital nahe dem Schluss verkauft bei negativer Portfoliorendite die Komponenten und kauft bei positiver.
- Ende Januar 2009 lag das AUM aller gehebelten ETFs, Long und Short, bei 19 Milliarden Dollar.
- High-Frequency-Händler können nahe einer Unterstützung künstlichen Verkaufsdruck erzeugen, indem sie große Verkaufsorders legen, um den nächsten Tick nach unten zu treiben.
- Große institutionelle Orders werden nicht mehr als ein Block ausgeführt, sondern in winzige Child Orders zerlegt und über den Tag sowie verschiedene Plätze ausgeführt.
- Eine aktuellere Analyse des Intraday-Rebalancing stammt von Rodier, Haryanto, Shum und Hejazi, 2012.

## Funktionsweise

- Deshalb erledigen die Insider Kauf und Verkauf nicht in einer Session, sondern über zwei, drei oder vier Sessions.
- Dieselbe Gegenbewegung zwingt auch Distribution, Selling Climax und Buying Climax, sich über einen Zeitraum zu erstrecken.
- High-Frequency-Händler können nahe einer Unterstützung große Sell Orders legen, um den nächsten Tick nach unten zu treiben.
- Große institutionelle Orders, die früher als Block Trades liefen, werden in winzige Child Orders zerlegt, über Handelsplätze verteilt und über den Tag ausgeführt.
- Wer ein großes Bid für Flipping hält, kann an die Flipper verkaufen und den Bid-Preis nach unten drücken.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Wird die große Buy-Limit-Order beim Flipping gefüllt, kann der anschließende Verkauf mit Verlust erfolgen.
- Eine aktuellere Impact-Analyse zum Rebalancing gehebelter ETFs stammt von Rodier, Haryanto, Shum und Hejazi (2012).
- Die Regulation NMS im Juli 2007 trug zum drastischen Rückgang der durchschnittlichen Trade-Größen und zum Verschwinden des NYSE-Blocktrades bei.

## Beispiele

- Nick Leeson konnte die Positionen, die Barings zu Fall brachten, nicht auflösen, ohne den Markt gegen den eigenen Kauf und Verkauf zu bewegen.
- Die Histogramme von Kyles, Amihuds und Hasbroucks Lambdas sind auf E-mini-S&P-500-Futures geschätzt.

## Unterschiedliche Quellenpositionen

- Hasbrouck empfiehlt wie der Großteil der Literatur 5-Minuten-Time-Bars für die Tick-Stichprobe.
- Stochastische Stichproben, die mit der Marktaktivität synchronisiert sind, können nach dem Text bessere Ergebnisse liefern als die empfohlenen 5-Minuten-Time-Bars.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- A Complete Guide to Volume Price Analysis.pdf, S. 58–77 → [[Trading/Pilot/blocks/a-complete-guide-to-volume-price-analysis-pdf/a-complete-guide-to-volume-price-analysis-pdf-block-004-p058-p077|S. 58–77]]
- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 173–186 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-013-p173-p186|S. 173–186]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 20–39 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-002-p020-p039|S. 20–39]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 33–51 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-003-p033-p051|S. 33–51]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 76–95 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-006-p076-p095|S. 76–95]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 166–179 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-013-p166-p179|S. 166–179]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 438–457 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-024-p438-p457|S. 438–457]]

## Verwandte Themen
