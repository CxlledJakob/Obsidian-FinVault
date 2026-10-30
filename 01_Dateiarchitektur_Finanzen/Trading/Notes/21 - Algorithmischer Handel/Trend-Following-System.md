---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Strategien und Ausführung"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Trend-Following-System


## Kurzdefinition


## Kernaussagen

- Zeitreihenmomentum ist die positive Korrelation vergangener und künftiger Renditen einer Preisreihe, und Futures zeigen es hauptsächlich wegen der Persistenz des Vorzeichens der Rollrenditen.
- Querschnittliches Momentum ist die positive Korrelation vergangener und künftiger relativer Renditen gegenüber den anderen Reihen eines Portfolios, und ein einfacher Rang auf den Renditen genügt oft.
- Die zwei üblichen Ausstiege sind zeitbasiert und Stop-Loss; alle bisher besprochenen Momentum-Strategien nutzen nur die Haltedauer, ein Stop kann dazukommen.
- Der Einzelverlust ist dadurch begrenzt, das Aufwärtspotenzial ist unbegrenzt, und eine willkürliche Gewinnobergrenze ist unratsam.
- Die Modelle gedeihen an Black Swans und an hoher Kurtosis, und die meisten Futures und Währungen erlauben damit Streuung über Assetklassen und Länder.
- Zusammen mit Mean-Reversion-Strategien entstehen höhere Sharpe Ratios und kleinere Drawdowns als mit jedem Typ allein.
- Profitable News-Sentiment-Strategien zeigen die langsame Nachrichtendiffusion als Ursache des Aktienmomentums, und die Ansteckung erzwungener Fondsverkäufe und -käufe trägt ebenfalls dazu bei.

## Funktionsweise

- Die einfache Zeitreihen-Momentum-Regel nach Moskowitz, Yao und Pedersen kauft den Future bei positiver und verkauft ihn bei negativer 12-Monats-Rendite und hält einen Monat; hier wird täglich entschieden und jeden Tag nur ein Fünfundzwanzigstel des Kapitals eingesetzt.
- Für TU sind Lookback und Haltedauer 250 und 25 Tage, gewählt wegen einer Korrelation von 0,27 bei einem p-Wert von 0,02.
- Ein saubereres Signal ist die verzögerte Rollrendite: long, wenn sie über einer Schwelle liegt, short, wenn sie unter der negativen Schwelle liegt, sonst wird jede Position geschlossen.
- Weitere Einstiege sind ein neues N-Tage-Hoch, das Überschreiten des N-Tage-Durchschnitts oder des exponentiellen Durchschnitts, das Überschreiten des oberen Bollinger-Bandes und ein Übergewicht der Aufwärtstage in einem gleitenden Fenster.
- Der Alexander-Filter kauft, wenn die Tagesrendite um mindestens x Prozent steigt, und verkauft und geht short, wenn der Preis von einem folgenden Hoch um mindestens x Prozent fällt.
- Der S&P DTI ist long, wenn ein Future über seinem exponentiellen Durchschnitt liegt, und short, wenn er darunter liegt, mit monatlichem Rebalancing über 24 Futures.

## Voraussetzungen


## Anwendung im Trading

- Kointegriert oder korreliert ein ETF oder ein anderer Future mit Spotpreis oder Spot-Rendite eines Rohstoffs, wird dieses Instrument bei Backwardation geshortet und bei Contango gekauft, um die Rollrendite des Rohstoff-Futures zu extrahieren.

## Regeln und Kriterien


## Risiken und Grenzen

- Wenige Trades wegen langer Haltedauern erzeugen ein Data-Snooping-Risiko; der eigentliche Test ist echtes Out-of-Sample-Testing.
- Für C trägt die Rollrendite-Erklärung nicht, obwohl ihre Rollrendite betragsmäßig am stärksten gegen die durchschnittliche Spot-Rendite ist.
- Die Wirkungsdauer wird kürzer, je mehr Händler das Momentum aufgreifen, ohne vorhersagbaren Zeitplan für die kürzere Haltedauer; Gewinnmeldungs-Momentum hält kaum noch bis zum Schluss.
- Stop-Losses widersprechen Mean-Reversion-Einstiegen.
- Eine einzelne Mean-Reversion-Position kann einen enormen Drawdown erzeugen, und aufeinanderfolgende Momentum-Verluste können trotzdem ruinös werden.
- In Beispiel 1.1 erreicht eine Reihe mit der Kurtosis der TU-Futures, aber ohne serielle Autokorrelation, in 12 Prozent der Ziehungen dieselben Renditen wie die TU-Momentum-Strategie.

## Beispiele

- TU erzielt vom 1. Juni 2004 bis zum 11. Mai 2012 eine Sharpe Ratio von 1 und 1,7 Prozent annualisiert auf etwa 200.000 Dollar Nominalwert bei etwa 400 Dollar Margin und 2,5 Prozent maximalem Drawdown.
- Tabelle 6.2: BR Lookback 100 und Haltedauer 10 mit 17,7 Prozent, Sharpe Ratio 1,09 und maximalem Drawdown minus 14,8 Prozent; HG 40 und 40 mit 18,0 Prozent, 1,05 und minus 24,0 Prozent; TU 250 und 25 mit 1,7 Prozent, 1,04 und minus 2,5 Prozent.
- Auf TU ergibt die Schwelle von 3 Prozent annualisierter Rollrendite vom 2. Januar 2009 bis zum 13. August 2012 2,5 Prozent annualisiert, eine Sharpe Ratio von 2,1 und einen maximalen Drawdown von 1,1 Prozent.
- Auf CL wird zum Schluss gekauft, wenn der Preis unter dem Stand von vor 30 Tagen und über dem von vor 40 Tagen liegt, umgekehrt für Shorts, sonst wird glattgestellt, mit 12 Prozent annualisiert und einer Sharpe Ratio von 1,1.
- Ein Mean-Reversion-Filter ergänzt IBX, KT, SXF, US, CD, NG und W und verbessert die schon enthaltenen Kontrakte.
- Der DTI hat nach Dever von Januar 1988 bis Dezember 2010 eine Sharpe Ratio von 1,3 und einen maximalen Drawdown von minus 16,6 Prozent, gegen 0,61 und minus 50,96 Prozent beim S&P 500, läuft seit 2008 schlecht und steht seit dem 5. Dezember 2008 mit minus 25,9 Prozent im Drawdown.
- RYMFX und WDTI bilden den DTI ab.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 210–229 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-012-p210-p229|S. 210–229]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 248–267 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-014-p248-p267|S. 248–267]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 324–343 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-018-p324-p343|S. 324–343]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 362–381 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-020-p362-p381|S. 362–381]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 381–400 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-021-p381-p400|S. 381–400]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]

## Verwandte Themen
