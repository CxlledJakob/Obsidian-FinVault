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

# Korrelation


## Kurzdefinition

- Die Korrelation zum Underlying ist die Korrelation der Strategierenditen mit den Renditen des zugrunde liegenden Anlageuniversums.
- Die Konditionszahl einer Korrelationsmatrix ist der Betrag des Verhältnisses aus betragsmäßig größtem und kleinstem Eigenwert.
- Zeitreihenmomentum bedeutet, dass vergangene Renditen einer Preisreihe positiv mit künftigen Renditen korreliert sind.
- Zeitreihenmomentum bezeichnet die positive Korrelation der vergangenen und der künftigen Renditen einer Preisreihe.
- Cross-Sectional Momentum bezeichnet die positive Korrelation der vergangenen und der künftigen relativen Renditen einer Preisreihe gegenüber den anderen Preisreihen eines Portfolios.

## Kernaussagen

- Eine deutlich positive oder deutlich negative Korrelation zum Underlying bedeutet, dass die Strategie das Anlageuniversum im Wesentlichen hält oder leerverkauft und darüber hinaus wenig eigenen Wert hinzufügt.
- Eine diagonale Korrelationsmatrix hat die niedrigste Konditionszahl und ist ihre eigene Inverse.
- Kommen korrelierte, multikollineare Anlagen hinzu, steigt die Konditionszahl, der größte Eigenwert wächst und der kleinste sinkt.
- Ab einer hohen Konditionszahl machen numerische Fehler die Inverse instabil, sodass eine kleine Änderung eines Eintrags eine ganz andere Inverse ergibt.
- Eine Korrelationsmatrix misst die Kosinus der Winkel zwischen je zwei Vektoren im Raum der Renditezeitreihen.
- Korrelationsmatrizen kennen keine Hierarchie, denn jede Anlage ist ein potenzieller Ersatz für jede andere.
- Pearsons Korrelation ist nicht die einzige, die erfüllt, dass die Kovarianz gleich Korrelation mal den beiden Standardabweichungen ist.
- Die Distanz als Quadratwurzel aus der Hälfte der Differenz von eins und der Korrelation ist eine echte Metrik, weil sie ein Vielfaches des euklidischen Abstands nach Z-Standardisierung ist.
- Die Quadratwurzel aus der Differenz von eins und dem Betrag der Korrelation ist eine echte Metrik auf dem Quotienten der ganzen Zahlen modulo 2.
- Korrelationsstrukturen bleiben über lange Zeiträume nicht invariant.
- Volatilität ist mit dem Aktienindex antikorreliert: fällt der Markt, schießt die Volatilität nach oben, und in geringerem Maß gilt auch das Umgekehrte.
- Das Streudiagramm der Frontmonatskurse von ES gegen die Frontmonatskurse von VX zeigt diese inverse Beziehung.
- Im Regime von August 2008 bis 2012 ist die Volatilität bei gegebenem Indexstand deutlich niedriger als im Regime von 2004 bis Mai 2008, die Spannweite der Volatilitäten aber größer, mit extremeren Volatilitätstagen als zuvor.

## Funktionsweise

- Hierarchical Risk Parity kodiert die Korrelation als Distanz und clustert darüber, statt bei der Inversion die partiellen Korrelationen des vollständigen Graphen auszuwerten.
- Das illustrierte Linkage-Kriterium ist der nearest-point-Algorithmus, also die kleinste Distanz zwischen einem Punkt und dem neuen Cluster.
- Auf einen idiosynkratischen Schock senkt Hierarchical Risk Parity die betroffene Anlage und erhöht eine korrelierte, nicht betroffene Anlage.
- Auf einen gemeinsamen Schock senkt es die betroffenen Anlagen und erhöht unkorrelierte Anlagen mit geringerer Varianz.
- Gemessen wird der Korrelationskoeffizient samt p-Wert für eine gewählte Verzögerung; die stärkste positive Korrelation kann zwischen Renditen verschiedener Lags liegen.
- Eintagesrenditen können negativ korrelieren, während die vergangene 20-Tage-Rendite mit der künftigen 40-Tage-Rendite stark positiv korreliert.
- Statt der Beträge kann die Korrelation der Vorzeichen getestet werden, wenn nur interessiert, dass eine Aufwärtsbewegung einer weiteren folgt.
- Überlappende Fenster werden ausgeschlossen: der Text rückt bei längerem Lookback um die Haltedauer und bei längerer Haltedauer um den Lookback vor.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Je korrelierter die Anlagen sind, desto nötiger ist Diversifikation und desto wahrscheinlicher werden instabile Lösungen.
- Das Inverse-Varianz-Portfolio ignoriert die Korrelationsstruktur und ist dadurch anfällig für systemische Schocks.
- Schocks auf mehrere korrelierte Anlagen bestrafen genau diese Unkenntnis der Korrelationsstruktur.
- Eine Hauptkomponentenanalyse auf einem großen Rentenuniversum leidet unter denselben Nachteilen wie CLA, weil Verfahren für kleine Datenmengen die Hierarchie nicht erkennen.
- Dieselbe Reihe kann auf verschiedenen Zeitebenen Momentum und Mean Reversion zeigen; bei TU ist der Hurst-Exponent 0,44 und der Variance-Ratio-Test verwirft den Random Walk nicht, obwohl einzelne Lag-Paare positiv korrelieren.
- Korrelationsstrukturen der Rollrendite erklären das querschnittliche Momentum von Währungen und Aktien nicht; dort kommen serielle Korrelation des Weltwirtschafts- oder Zinswachstums beziehungsweise langsame Informationsdiffusion infrage.

## Beispiele

- Aus den Korrelationen 0,7, 0,2 und minus 0,2 werden die Distanzen 0,3873, 0,6325 und 0,7746.
- Eine dargestellte Korrelationsmatrix von Rentenpapieren umfasst nach dem Clustering über 2,1 Millionen Einträge.
- Zwischen dem ersten und zweiten Rebalancing trifft eine Anlage ein idiosynkratischer Schock, zwischen dem fünften und sechsten zwei Anlagen ein gemeinsamer Schock.
- Für TU hat das Paar 250 zu 25 einen Korrelationskoeffizienten von 0,27 bei einem p-Wert von 0,02.
- Die besten Kompromisse aus Koeffizient und p-Wert sind (60, 10), (60, 25), (250, 10), (250, 25), (250, 60) und (250, 120).
- Die Korrelation der Tagesrenditen von VX und ES erreicht minus 75 Prozent.
- Die Hoffnung der querschnittlichen Rollrendite-Strategie ist, dass die Spotpreise der Rohstoffe positiv mit Wirtschaftswachstum oder anderen Makroindizes korrelieren und sich deshalb gegenseitig aufheben.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Advances in Financial Machine Learning.pdf, S. 248–267 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-014-p248-p267|S. 248–267]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 39–58 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-003-p039-p058|S. 39–58]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 58–77 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-004-p058-p077|S. 58–77]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 77–96 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-005-p077-p096|S. 77–96]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 115–134 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-007-p115-p134|S. 115–134]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 210–229 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-012-p210-p229|S. 210–229]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 248–267 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-014-p248-p267|S. 248–267]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 267–286 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-015-p267-p286|S. 267–286]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 286–305 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-016-p286-p305|S. 286–305]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 305–324 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-017-p305-p324|S. 305–324]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 324–343 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-018-p324-p343|S. 324–343]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 343–362 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-019-p343-p362|S. 343–362]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 419–438 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-023-p419-p438|S. 419–438]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 457–476 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-025-p457-p476|S. 457–476]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 476–495 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-026-p476-p495|S. 476–495]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]

## Verwandte Themen
