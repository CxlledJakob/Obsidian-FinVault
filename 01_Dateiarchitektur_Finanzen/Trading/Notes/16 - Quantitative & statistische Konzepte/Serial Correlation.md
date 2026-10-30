---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Zeitreihen"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Serial Correlation


## Kurzdefinition


## Kernaussagen

- Serielle Bedingtheit der Labels macht die gewöhnliche k-Fold-Cross-Validation unbrauchbar, weil die Zufallsziehung redundante Beobachtungen sowohl ins Trainings- als auch ins Testset streut.
- Deshalb braucht es ein Validierungsverfahren, das das Modell an den Beobachtungen bewertet, die am wenigsten mit den Trainingsbeobachtungen korreliert oder redundant sind.
- Bei langreichweitiger serieller Abhängigkeit genügt es nicht, eine Beobachtung hinter dem Ende des Trainingssets zu testen, um Informationsleakage zu vermeiden.
- Toth et al. (2011) untersuchen den signierten Orderflow von Aktien der London Stock Exchange und finden über viele Tage positiv autokorrelierte Orderzeichen.
- Die zwei von ihnen geprüften Erklärungen sind Herding und Order Splitting.
- Auf Zeitskalen von weniger als einigen Stunden geht die Persistenz überwiegend auf Order Splitting zurück.
- Die Mikrostrukturtheorie führt die Persistenz des Orderflow-Ungleichgewichts auf die Anwesenheit informierter Händler zurück.
- Die Stärke dieser Persistenz lässt sich über die serielle Korrelation der signierten Volumina messen.
- Ein solches Feature ergänzt die Features der sequenziellen Handelsmodelle in Abschnitt 19.5.
- Das Roll-Modell nimmt serielle Unabhängigkeit der Aggressorzeichen an, E[bt bt−1] = 0.
- Die halbe Geld-Brief-Spanne ergibt sich dort aus der seriellen Kovarianz der Preisänderungen, c = √max{0, −σ[Δpt, Δpt−1]}.
- Empirisch weisen Finanzzeitreihen serielle Abhängigkeit auf.
- Den simulierten Renditen des zweiten Hypothesentests fehlen die Korrelationen, die in den beobachteten Reihen stecken.
- Lässt sich auf solchen Zufallsreihen mit guter Wahrscheinlichkeit eine mindestens ebenso gute Strategierendite erzeugen, erfasst die Momentum-Strategie kein Momentum und keine seriellen Korrelationen der Renditen und ist nur deshalb profitabel, weil die beobachtete Verteilung einen bestimmten Mittelwert und eine bestimmte Form hat.
- Von 10.000 solchen Reihen lagen 1.166 mindestens auf der beobachteten durchschnittlichen Rendite. Die Null ließ sich nur mit 88 Prozent Wahrscheinlichkeit verwerfen, und die Form der Verteilung hat etwas mit dem Erfolg zu tun.
- Die anti-serielle Korrelation der Renditen ist handelbar und ist dasselbe wie die Mean Reversion der Preise; die Mean Reversion der Renditen selbst ist nicht handelbar.
- Cross-sectional Mean Reversion impliziert, dass die kurzfristigen relativen Renditen der Instrumente seriell antikorreliert sind.
- Eine trendende Reihe hat positive Korrelationen aufeinanderfolgender Preisbewegungen und einen Hurst-Exponenten über 0,5.
- Viele Futures-Renditen weisen serielle Korrelation auf, und diese Korrelation tritt nur auf einer ziemlich langen Zeitskala auf.
- Das Vorzeichen der Rollrendite wechselt typischerweise selten, die Futures bleiben also lange in Contango oder Backwardation, während die Spot-Rendite Vorzeichen und Größe sehr schnell wechselt.
- Wird ein Future lange gehalten und dominieren die durchschnittlichen Rollrenditen die durchschnittliche Gesamtrendite, entsteht serielle Korrelation der Gesamtrenditen.
- Querschnittliches Momentum bei Währungen lässt sich der seriellen Korrelation des Weltwirtschafts- oder Zinswachstums zuschreiben.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Oft lässt sich die ADF-Null erst mit Lag k gleich 1 verwerfen und nicht mit k gleich 0, weil die Preisänderungen häufig serielle Korrelation haben.

## Risiken und Grenzen


## Beispiele

- Die Erklärung passt zu BR, HG und TU, weil ihre Rollrenditen nach Tabelle 5.1 betragsmäßig größer sind als ihre Spot-Renditen.
- Für C findet der Text den Grund nicht, obwohl C den größten Betrag der Rollrendite im Vergleich zur durchschnittlichen Spot-Rendite hat.
- Für TU ist die Korrelation der 250-Tage-Rendite mit der folgenden 25-Tage-Rendite 0,27 bei einem p-Wert von 0,02, während der Hurst-Exponent 0,44 beträgt und der Variance-Ratio-Test den Random Walk nicht verwirft.
- Beispiel 1.1 simuliert eine Renditereihe mit derselben Kurtosis wie die TU-Futures-Reihe, aber ohne serielle Autokorrelationen, und erzeugt in 12 Prozent der Zufallsziehungen dieselben Renditen wie die TU-Momentum-Strategie.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]
- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 476–495 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-026-p476-p495|S. 476–495]]

## Verwandte Themen
