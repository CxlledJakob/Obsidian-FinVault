---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Statistik"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Schiefe


## Kurzdefinition

- Die Schiefe der Renditen ist ein Eingang der Probabilistic Sharpe Ratio.

## Kernaussagen

- Positive Schiefe erhöht die Probabilistic Sharpe Ratio.
- Die abgebildete Fläche zeigt die Probabilistic Sharpe Ratio in Abhängigkeit von Schiefe und Stichprobenlänge bei Kurtosis 3, beobachteter Sharpe Ratio 1,5 und Benchmark 1,0.
- Wer die Gauß-Verteilung verlässt, weil sie Extremereignisse nicht erfasst, kann mit der Student-t-Verteilung Schiefe und Kurtosis der Renditen abbilden.
- Im zweiten Hypothesentest haben die simulierten Tagesrenditen dieselbe Schiefe wie die beobachteten Futures-Renditen, neben Mittelwert, Standardabweichung und Kurtosis, aber nicht dieselben eingebetteten Korrelationen.
- Performancestatistiken, die Verhältnisse sind, können lang gezogene rechte Schwänze haben. Genannt werden die Sharpe Ratio, das Verhältnis der mittleren Rendite zum Ulcer Index und der Profit Factor.
- Für Statistiken mit solch einem langen rechten Schwanz sind die Verfahren zur Stichprobenverteilung des Mittelwerts nur begrenzt brauchbar. Der Logarithmus des Verhältnisses verkürzt den rechten Schwanz und mildert das.
- Widersprüchliche Schlüsse von Hypothesentest und Konfidenzintervall entstehen, wenn die Stichprobenverteilung nicht symmetrisch, also nach rechts oder links schief ist.
- In der nach links schiefen Abbildung liegt weniger als 5 Prozent des rechten Schwanzes über der mittleren Backtest-Rendite, der Test ist zum Niveau 0,05 signifikant, und die Untergrenze des 90-Prozent-Intervalls liegt unter einer Rendite von null.
- Der Zentrale Grenzwertsatz sichert, dass die Stichprobenverteilung des Mittelwerts bei großer Stichprobe nicht ernsthaft schief ist und mit wachsender Stichprobe zu einer symmetrischen Glocke tendiert.
- Andere Leistungskennzahlen müssen sich nicht so verhalten.
- Ist die Verteilung nicht symmetrisch, können Bootstrap-Verfahren sie schwenken, um den Widerspruch zu mildern; diese Methoden können eigene Probleme haben.
- Weil der Mittelwert sich so verhält, ist die mittlere Rendite eine attraktive Kennzahl für Regeltests.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 191–210 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-011-p191-p210|S. 191–210]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 248–267 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-014-p248-p267|S. 248–267]]

## Verwandte Themen
