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
aktualisiert: 2026-11-01
---

# Autokorrelation


## Kurzdefinition


## Kernaussagen

- Toth et al. (2011) finden bei Aktien der London Stock Exchange, dass Orderzeichen über viele Tage positiv autokorreliert sind.
- Als Erklärungen prüfen sie Herding und Order Splitting.
- Auf Zeitskalen von weniger als einigen Stunden führen sie die Persistenz des Orderflows überwiegend auf Order Splitting zurück.
- Im Roll-Modell ist die serielle Kovarianz der beobachteten Preisänderungen negativ und gleich −c², wobei c die halbe Geld-Brief-Spanne ist.
- Empirisch zeigen Finanzzeitreihen serielle Abhängigkeit.
- Querschnittliche Mean Reversion setzt auf die serielle Antikorrelation relativer Renditen: auf Unterperformance einer Aktie soll Überperformance folgen und umgekehrt.
- Random Walks haben kein Gedächtnis, und frühere Ergebnisse haben keine Wirkung auf die nachfolgenden Ereignisse.
- Zeitreihenmomentum heißt, dass vergangene Renditen positiv mit künftigen Renditen korreliert sind; gerechnet werden der Korrelationskoeffizient und sein p-Wert als Wahrscheinlichkeit der Nullhypothese keiner Korrelation.
- Der Koeffizient verlangt einen festen Lag; die stärkste positive Korrelation kann zwischen verschiedenen Lags liegen, etwa eine negative Korrelation der 1-Tages-Renditen neben einer sehr positiven Korrelation der vergangenen 20-Tages-Rendite mit der künftigen 40-Tages-Rendite.
- Für TU sind die besten Kompromisse aus Koeffizient und p-Wert die Paare aus Lookback und Haltedauer (60, 10), (60, 25), (250, 10), (250, 25), (250, 60) und (250, 120).
- Das Paar 250 und 25 hat für TU einen Korrelationskoeffizienten von 0,27 bei einem p-Wert von 0,02; in Tabelle 6.1 steht für 250 und 25 der Wert 0,2719 bei einem p-Wert von 0,0238.
- In Tabelle 6.1 erreicht Lookback 250 und Haltedauer 120 einen Koeffizienten von 0,5112 bei einem p-Wert von 0,0617, Lookback 250 und Haltedauer 250 einen Koeffizienten von 0,4873 bei einem p-Wert von 0,3269.
- Der Test der Vorzeichen vergangener und künftiger Renditen liefert für TU keine sehr anderen Ergebnisse; die besten Paare sind dann (60, 10), (250, 10) und (250, 25).
- Der Text verlangt nicht überlappende Paare: ist der Lookback größer als die Haltedauer, wird um die Haltedauer vorgerückt, ist die Haltedauer größer, um den Lookback.
- Der abgedruckte Code setzt die Schrittweite dagegen auf den Lookback, wenn der Lookback mindestens so groß wie die Haltedauer ist, und sonst auf die Haltedauer.
- Eine Verschiebung um einen Tag erzeugt leicht andere Renditepaare; wegen der großen Überlappung dürften die Korrelationen nicht stark abweichen, und getestet wurde nur eine von vielen möglichen Mengen.
- Serielle Korrelation der Futures-Gesamtrendite auf langer Skala entsteht, wenn das Vorzeichen der Rollrendite lange konstant bleibt und die durchschnittliche Rollrendite die durchschnittliche Gesamtrendite dominiert; die Spot-Rendite wechselt Vorzeichen und Größe sehr schnell.
- Das passt zu BR, HG und TU, deren Rollrenditen laut Tabelle 5.1 betragsmäßig größer sind als ihre Spot-Renditen.
- Für C trägt die Erklärung nicht, obwohl C die betragsmäßig größte Rollrendite im Vergleich zur durchschnittlichen Spot-Rendite hat.
- Der Korrelationskoeffizient der Tagesrenditen von VX und ES erreicht minus 75 Prozent.
- Für TU beträgt der Hurst-Exponent 0,44, und der Variance-Ratio-Test verwirft den Random Walk nicht; das widerspricht den Lag-Korrelationen nicht, weil Momentum und Mean Reversion auf verschiedenen Zeitrahmen liegen und der Variance-Ratio-Test einzelne Zeitrahmen nicht prüft.
- Beispiel 1.1 simuliert eine Renditereihe mit derselben Kurtosis wie die TU-Futures, aber ohne serielle Autokorrelationen, und erzeugt in 12 Prozent der Zufallsziehungen dieselben Renditen wie die TU-Momentum-Strategie.

## Funktionsweise

- Die aktuelle Preisänderung wird mit der vorherigen Änderung korreliert, also mit Lag 1, dann mit der Änderung davor, Lag 2, und so fort. Für jeden dieser Lags wird ein Korrelationskoeffizient berechnet.
- In einer zufälligen Datenreihe fallen die Korrelationen typischerweise sehr schnell als Funktion des Lag-Intervalls ab.
- Ist die Zeitreihe der Preisänderungen in linearer Weise nichtzufällig, unterscheiden sich einige Autokorrelationskoeffizienten signifikant vom Muster der Autokorrelationen einer Zufallsfolge.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 77–96 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-005-p077-p096|S. 77–96]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 96–115 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-006-p096-p115|S. 96–115]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 144–163 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-011-p144-p163|S. 144–163]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 163–165 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-012-p163-p165|S. 163–165]]

## Verwandte Themen
