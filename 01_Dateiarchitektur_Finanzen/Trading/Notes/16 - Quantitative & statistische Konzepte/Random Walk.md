---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Zeitreihen"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Random Walk


## Kurzdefinition

- Im Chow-Typ-Dickey-Fuller-Test ist die Nullhypothese, dass die Reihe einem Random Walk folgt, also Rho gleich 1 ist.
- Im Roll-Modell folgt der Mid-Price einem Random Walk ohne Drift, mt = mt−1 + ut.

## Kernaussagen

- Mit steigender Halbwertszeit steigt phi, definiert als zwei potenziert mit minus eins durch die Halbwertszeit, und der Prozess rückt an einen Random Walk heran.
- Geht phi gegen 1, bleiben keine erkennbaren Bereiche, in denen eine Handelsregel die Performance zuverlässig maximiert.
- Bei Prognose 0 spreizen sich die Gebiete hoher und niedriger Performance mit wachsender Halbwertszeit, und die Sharpe Ratios sinken.
- Bei Prognose 5 und Halbwertszeit 100 ist der Prozess so nah an einem Random Walk, dass die höchste Sharpe Ratio nur noch 0,32 beträgt.
- Bei Prognose 5 und Halbwertszeit 100 ist der Prozess so nah an einem Random Walk, dass die höchste Sharpe Ratio nur 0,32 beträgt.
- Bei negativer Prognose wirkt die Annäherung an den Random Walk mildernd, weil das schlechteste Gebiet sich spreizt und die Sharpe Ratio weniger negativ wird.
- Bei Prognose minus 5 und Halbwertszeit 10 wird aus dem Rechteck ein Quadrat, und die Sharpe Ratios liegen etwa bei minus 9.
- Steigen die Halbwertszeiten weiter auf 25, 50 und 100, verflacht die Performance.
- Sobald die Performance bei langer Halbwertszeit verflacht, wird das Optimieren der Handelsregel eine Übung in Backtest-Overfitting.
- Bei Prognose minus 10 wiederholt sich das gedrehte Gegenbild des Falls mit positivem langfristigem Gleichgewicht.
- Die Alternative ist, dass die Reihe als Random Walk beginnt und zum Bruchzeitpunkt in einen explosiven Prozess mit Rho größer als 1 wechselt.
- Der Bruchzeitpunkt ist ein Anteil Tau zwischen 0 und 1 der Stichprobenlänge.
- Exponentielles Wachstum oder Kollaps ist mit einem Random Walk unvereinbar und auf Dauer unhaltbar.
- Chows Ansatz unterstellt genau ein Bruchdatum, und die Blase läuft bis zum Stichprobenende, ohne Rückwechsel zum Random Walk.
- Für die Folge Random Walk, Blase, Random Walk ist der Supremum-Augmented-Dickey-Fuller-Test vorgesehen.
- Im Null-Lag-Modell auf Logpreisen verhält sich das System bei Beta gleich 0 als nichtstationäres Martingal.
- Die Änderungen des Mid-Price sind unabhängig und identisch normalverteilt mit Varianz σ²u.
- Die beobachteten Preise weichen vom Mid-Price um die halbe Spanne ab, pt = mt + bt c.
- Empirisch haben Finanzzeitreihen einen Drift, sind heteroskedastisch, zeigen serielle Abhängigkeit, und ihre Renditeverteilung ist nicht normal.
- Mit einem geeigneten Sampling, wie in Kapitel 2 beschrieben, müssen die Random-Walk-Annahmen nicht allzu unrealistisch sein.
- Das Rauschen des unbeobachteten Preises ohne Mikrostrukturrauschen ist σ²u = σ²[Δpt] + 2 σ[Δpt, Δpt−1].
- Die meisten Preisreihen sind geometrische Random Walks; die Renditen verteilen sich gewöhnlich zufällig um einen Mittelwert von null.
- Beim geometrischen Random Walk wächst die Varianz der Logpreisänderung linear mit der Zeitspanne τ, und der Hurst-Exponent ist 0,5.
- Kann die ADF-Null λ gleich 0 nicht verworfen werden, hängt der nächste Schritt nicht vom aktuellen Niveau ab, und ein Random Walk bleibt möglich.
- Stationarität bedeutet, dass Preise langsamer diffundieren als ein geometrischer Random Walk.
- Hurst-Exponent und Variance-Ratio-Test sind dafür gebaut, diese Stationarität gegen den geometrischen Random Walk zu prüfen.
- Aktienkurse folgen langfristig geometrischen Random Walks, auch wenn sie kurzfristig unter normalen Umständen mean-reverting sind.
- Der geometrische Random Walk beschreibt tägliche Einzelaktien gut: einmal weggegangen, kehren sie selten zu ihrem Startpunkt zurück; Intraday- und saisonale Mean Reversion sind Sonderfälle.
- Dass Aktienkurse geometrischen Random Walks folgen, wie es viele Forscher und Malkiel 2008 betonen, gilt nur, wenn die Reihe streng in regelmäßigen Abständen auf Mean Reversion getestet wird, etwa an den täglichen Schlüssen.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Der Variance-Ratio-Test prüft die Null, dass der Hurst-Exponent wirklich 0,5 ist; h gleich 1 verwirft den Random Walk auf 90 Prozent, h gleich 0 lässt ihn zu.

## Risiken und Grenzen

- Eine Handelsregel auf einem Random Walk über historische Simulationen zu kalibrieren, führt zu Backtest-Overfitting, weil eine zufällig günstige Schwellenkombination gewählt wird.
- Backtests auf synthetischen Daten sollen verhindern, dass eine Strategie nur wegen eines statistischen Ausreißers auf einem einzelnen historischen Pfad gewählt wird.

## Beispiele

- USD.CAD sieht in der Abbildung nicht stationär aus; die ADF-Statistik von etwa minus 1,84 verwirft die Null auf 90 Prozent nicht, der kritische Wert ist minus 2,594, und die AR(1)-Schätzung liegt bei 0,994120.
- Der Variance-Ratio-Test auf den Logpreisen von USD.CAD ergibt h gleich 0 und pValue gleich 0,367281, also rund 37 Prozent Wahrscheinlichkeit, dass die Reihe ein Random Walk ist.
- λ ist bei USD.CAD dennoch negativ, die Reihe trendet also zumindest nicht, und der Hurst-Exponent von 0,49 deutet auf schwache Mean Reversion.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]
- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 1–20 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-001-p001-p020|S. 1–20]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 20–39 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-002-p020-p039|S. 20–39]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 39–58 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-003-p039-p058|S. 39–58]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 58–77 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-004-p058-p077|S. 58–77]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 77–96 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-005-p077-p096|S. 77–96]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 96–115 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-006-p096-p115|S. 96–115]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 153–172 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-009-p153-p172|S. 153–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 324–343 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-018-p324-p343|S. 324–343]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 343–362 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-019-p343-p362|S. 343–362]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 362–381 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-020-p362-p381|S. 362–381]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 476–495 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-026-p476-p495|S. 476–495]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]

## Verwandte Themen
