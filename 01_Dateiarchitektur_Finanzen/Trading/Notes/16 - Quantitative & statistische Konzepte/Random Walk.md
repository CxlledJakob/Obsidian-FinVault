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

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Eine Handelsregel auf einem Random Walk über historische Simulationen zu kalibrieren, führt zu Backtest-Overfitting, weil eine zufällig günstige Schwellenkombination gewählt wird.
- Backtests auf synthetischen Daten sollen verhindern, dass eine Strategie nur wegen eines statistischen Ausreißers auf einem einzelnen historischen Pfad gewählt wird.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]
- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]

## Verwandte Themen
