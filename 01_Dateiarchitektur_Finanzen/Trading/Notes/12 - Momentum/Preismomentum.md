---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/12 - Momentum/12 - Momentum|12 - Momentum]]"
weitere_hauptthemen: []
unterthema: "Momentumstruktur"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Preismomentum


## Kurzdefinition


## Kernaussagen

- Momentum-Trader werden an Excess-Hochs und Excess-Tiefs häufig gefangen, weil das Momentum dort oft am höchsten ist.
- Der Text nennt vier Hauptursachen von Momentum: bei Futures die Persistenz der Rollrenditen, besonders ihres Vorzeichens; die langsame Diffusion, Analyse und Aufnahme neuer Information; erzwungene Verkäufe oder Käufe von Fonds verschiedener Art; und Marktmanipulation durch Hochfrequenzhändler.
- Forscher teilen Preismomentum in Zeitreihenmomentum und querschnittliches Momentum, nach Moskowitz, Yao und Pedersen 2010.
- Die hier beschriebenen Strategien halten mehrere Tage; viele davon leiden unter einer neu entdeckten Schwäche, von der Intraday-Momentum weniger betroffen ist.
- Viele Futures-Renditen sind auf ziemlich langer Zeitskala seriell korreliert, weil das Vorzeichen der Rollrendite lange gleich bleibt, während die Spot-Rendite schnell das Vorzeichen und die Größe wechselt.
- Die langsame Diffusion von Nachrichten ist die Ursache des Aktienmomentums, gezeigt an profitablen querschnittlichen Sentiment-Strategien.
- Erzwungene Verkäufe und Käufe von Publikumsfonds zünden Momentum in beide Richtungen bei gemeinsam gehaltenen Aktien; Indexfonds, gehebelte ETFs und die Zwangsverkäufe von Hedgefonds können dasselbe auslösen, letztere den Quant-Fonds-Einbruch im August 2007.
- Die Wirkungsdauer von Momentum wird fortschreitend kürzer, je mehr Händler es aufgreifen, vor allem beim kürzerfristigen nachrichtengetriebenen Momentum.
- Gewinnmeldungs-Momentum dauerte früher mehrere Tage und hält nun kaum bis zum Börsenschluss, weil die Information schneller diffundiert.
- Es gibt dafür keinen vorhersagbaren Zeitplan, nach dem die Haltedauer zu verkürzen wäre.
- Momentum-Strategien sind über zeitbasierten Ausstieg oder Stop-Loss im Einzelverlust begrenzt, ihr Aufwärtspotenzial ist unbegrenzt, und eine willkürliche Gewinnobergrenze ist unratsam.
- Futures zeigen Zeitreihenmomentum hauptsächlich wegen der Persistenz des Vorzeichens der Rollrenditen.
- Die langsame Diffusion von Nachrichten ist eine Ursache des Aktienpreismomentums, gezeigt an profitablen News-Sentiment-Strategien.
- Die Ansteckung erzwungener Asset-Verkäufe und -Käufe unter Publikumsfonds trägt zum Aktienpreismomentum bei.
- Momentum-Modelle gedeihen an Black-Swan-Ereignissen und an der positiven Kurtosis der Renditeverteilung.
- Querschnitts- und Zeitreihenmomentum laufen typischerweise über einen Monat oder länger.
- Lange Haltedauern erzeugen niedrigere Sharpe Ratios, geringere Backtest-Signifikanz wegen seltener unabhängiger Signale und Underperformance nach Finanzkrisen.
- Intraday-Strategien haben diese Nachteile nicht und behalten einige zentrale Vorteile.
- Vier Hauptursachen wirken bis auf die Persistenz der Roll Return auch intraday; Roll Return ist intraday zu klein und zu wenig volatil.
- Eine zusätzliche kurzfristige Ursache ist das Auslösen von Stops, oft in Form von Breakouts.
- Auf der kürzesten Skala erzeugen Ungleichgewichte von Bid- und Ask-Size, Änderungen des Orderflows und ungleich verteilte Stop-Orders Preismomentum.
- Orderflow sagt die kurzfristige Preisbewegung in derselben Richtung voraus.

## Funktionsweise

- Excess entsteht überwiegend, weil Momentum-Trader die Auktion an diese Extreme treiben.
- Aktien, die nur wenig gefallen sind, haben eine bessere Chance auf Umkehr als solche, die stark gefallen sind, weil starke Rückgänge oft negative Nachrichten wie schlechte Gewinnmeldungen sind und dann seltener zurückkehren.
- Aus solchen Breaking-News-Bewegungen lassen sich Momentum-Strategien bauen; das wird in Kapitel 7 weiter behandelt.
- Ein Kurs über einem langfristigen gleitenden Durchschnitt zieht Verkaufsdruck größerer Akteure wie Long-only-Fonds an, deren Handelshorizont länger ist.
- Neben dem Vorzeichen der Rendite kann gekauft werden bei einem neuen N-Tage-Hoch, beim Überschreiten des N-Tage-Durchschnitts oder des exponentiellen Durchschnitts, beim Überschreiten des oberen Bollinger-Bandes oder wenn in einem gleitenden Fenster die Zahl der Aufwärtstage die der Abwärtstage übersteigt.
- Der Alexander-Filter nach Fama und Blume 1966 kauft, wenn die Tagesrendite um mindestens x Prozent steigt, und verkauft und geht short, wenn der Preis von einem folgenden Hoch um mindestens x Prozent fällt.
- Ein saubereres Signal als die verzögerte Gesamtrendite ist die verzögerte Rollrendite: long über einer Schwelle, short unter der negativen Schwelle, sonst wird jede bestehende Position geschlossen.
- Auslöser jenseits der reinen Preisaktion sind Gewinnmeldungen, Änderungen von Analystenempfehlungen und Makronachrichten.
- Das tägliche Rebalancing gehebelter ETFs erzeugt kurzfristiges Momentum in Richtung der Marktrendite seit dem vorigen Schluss.
- Änderungen der Indexzusammensetzung erzeugen Momentum in aufgenommenen oder gelöschten Aktien.
- Liegt die Ursache in langsamer Nachrichtendiffusion, liegt der Nutzen in den ersten Tagen, Stunden oder Sekunden nach dem Ereignis.
- Die Kursbewegung einer Gewinnmeldung hält danach einige Zeit in derselben Richtung an.

## Voraussetzungen


## Anwendung im Trading

- Bei Auktionen, die das längere Timeframe treibt, wechseln anpassungsfähige Day-Trader vom rotationalen Handel zum Momentum-Handel.
- Regel 2 des Buy-on-Gap ist ein Momentum-Filter auf einer Mean-Reversion-Strategie: der Open muss über dem 20-Tage-Durchschnitt der Schlusskurse liegen, und dieses Muster wird im Text oft wiederholt.
- Ein Momentum-Filter auf Mean-Reversal-Strategien verbessert typischerweise deren Konsistenz.

## Regeln und Kriterien

- Erkannt wird dieses Excess erst danach, wenn der Innovator die nachlaufenden Momentum-Trader fadet.

## Risiken und Grenzen

- Datenfehler, die Mean-Reversion-Backtests aufblähen, unterdrücken die Backtest-Performance von Momentum-Strategien und sind deshalb für Momentum weniger gefährlich.
- Im Beispiel mit der falschen Historie 100, 110, 100 Dollar kauft die Momentum-Strategie im Backtest um 11:01 bei 110 Dollar und kann um 11:02 bei 100 Dollar mit Verlust gestoppt werden.
- Schlechte Ticks in Live-Daten veranlassen auch Momentum-Strategien zu falschen Orders und sind für deren Ausführung ebenso verlustbringend.
- Profitable Momentum-Strategien sind nach der Handelserfahrung des Textes schwerer zu bauen und haben tendenziell niedrigere Sharpe Ratios als Mean-Reversal-Strategien.
- Nach einer Finanzkrise laufen sie mehrere Jahre miserable, weil Shorts stark zurückfedern; nach 1929 dauerte es mehr als 30 Jahre bis zum alten Höchststand einer repräsentativen Momentum-Strategie.
- Stop-Losses passen zu Momentum, weil der Richtungswechsel die Gegenposition eröffnet und damit die verlierende Position schließt.
- Der aufsummierte Verlust aufeinanderfolgender verlierender Momentum-Positionen kann in die Insolvenz führen.
- Nach riskanten Ereignissen liefen Momentum-Strategien schlecht, obwohl sie in Risiken gedeihen können.

## Beispiele

- Hafez und Xie erzielen mit positiver gegen negative Sentimentänderung vor Kosten annualisierte Renditen von 52 bis 156 Prozent und Sharpe Ratios von 3,9 bis 5,3.
- Weitere Sentiment-Anbieter sind Recorded Future, thestocksonar.com und Thomson Reuters News Analytics; sie unterscheiden sich in der Nachrichtenabdeckung und im Algorithmus des Sentiment-Scores.
- Elementarisierte Feeds liefert günstig Newsware; geringere Latenz und bessere Abdeckung bieten Bloomberg Event-Driven Trading, Dow Jones Elementized News Feeds und Thomson Reuters Machine Readable News.
- Bollen, Mao und Zeng 2010 halten die in Twitter-Feeds sichtbare gesellschaftliche Stimmung für prädiktiv für den Marktindex; dazu wurde ein Hedgefonds über mehrere Millionen Dollar aufgelegt, nach Bryant 2010, die Geltung der Forschung wurde aber angegriffen, nach Buy the Hype 2012.

## Unterschiedliche Quellenpositionen

- Viele Momentum-Strategien haben als einzige Rechtfertigung, dass andere Anleger langsamer auf Nachrichten reagieren; zugespitzt muss man an größere Narren glauben.
- Diese Narren holen irgendwann auf, und die Momentum-Strategie kann eines Tages ohne Erklärung aufhören zu funktionieren.
- Mean-Reversion-Paare haben demgegenüber oft eine fundamentale Geschichte, und selbst ihr Auseinanderfallen, wie GDX und GLD Anfang 2008 wegen hoher Energiepreise, bleibt häufig erklärbar.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Mind Over Markets_ Power Trading with Market Generated Information, Updated Edition.pdf, S. 336–355 → [[Trading/Pilot/blocks/mind-over-markets/mind-over-markets-block-022-p336-p355|S. 336–355]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 173–186 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-013-p173-p186|S. 173–186]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 1–20 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-001-p001-p020|S. 1–20]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 96–115 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-006-p096-p115|S. 96–115]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 343–362 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-019-p343-p362|S. 343–362]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 362–381 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-020-p362-p381|S. 362–381]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 381–400 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-021-p381-p400|S. 381–400]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 419–438 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-023-p419-p438|S. 419–438]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]

## Verwandte Themen
