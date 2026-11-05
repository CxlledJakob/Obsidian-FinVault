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
aktualisiert: 2026-11-05
---

# Kurtosis


## Kurzdefinition

- Die Kurtosis der Renditen ist ein Eingang der Probabilistic Sharpe Ratio.
- Die Kurtosis ist das normierte vierte zentrale Moment K(x) = E[(X − µx) hoch 4 geteilt durch σx hoch 4]; das vierte zentrale Moment misst das Randverhalten von X.
- K(x) − 3 heißt Exzess-Kurtosis, weil K(x) für eine Normalverteilung gleich 3 ist; die Exzess-Kurtosis einer normalverteilten Zufallsvariablen ist damit null.

## Kernaussagen

- Für gaußsche Renditen beträgt die Kurtosis 3.
- Die Probabilistic Sharpe Ratio sinkt, wenn die Kurtosis steigt und die Ränder dicker werden.
- In der abgebildeten Fläche ist die Kurtosis auf 3 gesetzt, die beobachtete Sharpe Ratio auf 1,5 und die Benchmark auf 1,0, während Schiefe und Stichprobenlänge variieren.
- Die Gauß-Verteilung erfasst Extremereignisse im Finanzmarkt nicht. Die Student-t-Verteilung erlaubt, Schiefe und Kurtosis der Renditen zu erfassen. Die Pareto-Verteilung verzichtet vollständig auf ein endliches zweites Moment.
- Jede Wahl jenseits der Gauß-Form hat ein Element von Willkür und beruht auf endlich vielen Beobachtungen. Occams Rasiermesser gebietet eine Gauß-Form, sofern nicht starke theoretische und empirische Gründe für eine andere Verteilung sprechen.
- Im zweiten Hypothesentest haben die simulierten Tagesrenditen dieselbe Kurtosis wie die beobachteten Futures-Renditen, zusammen mit Mittelwert, Standardabweichung und Schiefe, aber nicht dieselben Korrelationen.
- Beispiel 1.1 zeigt, dass jede zufällige Renditeverteilung mit hoher Kurtosis für Momentum-Strategien günstig sein kann.
- Das Scheitern, die Nullhypothese zu verwerfen, kann diese Einsicht anregen, auch wenn die Verwerfung selbst kein sehr befriedigender Schätzer statistischer Signifikanz ist.
- Je dicker die Ränder der Renditeverteilung oder je höher ihre Kurtosis, desto besser ist dieser Markt für Momentum-Strategien.
- Je häufiger Black-Swan-Ereignisse auftreten, desto wahrscheinlicher profitiert eine Momentum-Strategie; Momentum-Modelle gedeihen an Black Swans und an der positiven Kurtosis der Renditeverteilung.
- In Beispiel 1.1 erzeugt eine Renditereihe mit derselben Kurtosis wie die TU-Futures-Reihe, aber ohne serielle Autokorrelationen, in 12 Prozent der Zufallsziehungen dieselben Renditen wie die TU-Momentum-Strategie.
- Positive Exzess-Kurtosis heißt schwere Ränder: die Verteilung legt mehr Masse auf die Ränder ihres Trägers als eine Normalverteilung, und eine Stichprobe enthält tendenziell mehr Extremwerte. Eine solche Verteilung heißt leptokurtisch.
- Negative Exzess-Kurtosis heißt kurze Ränder, zum Beispiel bei einer Gleichverteilung auf einem endlichen Intervall. Eine solche Verteilung heißt platykurtisch.
- In R bezeichnet kurtosis die Exzess-Kurtosis. Für die täglichen einfachen IBM-Renditen ist sie hoch und zeigt schwere Ränder; der ausgewiesene Wert ist 9,916359.
- Tagesrenditen von Marktindizes und Einzelaktien haben tendenziell hohe Exzess-Kurtosis. Bei Monatsreihen haben die Renditen der Marktindizes höhere Exzess-Kurtosis als die Einzelaktien.
- Die empirische Dichte der monatlichen IBM-Renditen von 1926 bis 2008 hat um den Mittelwert einen höheren Gipfel und dickere Ränder als die Normaldichte mit Stichprobenmittel und Stichprobenstandardabweichung aus Tabelle 1.2; sie ist höher und schmaler, aber mit breiterem Träger.
- Die Normalannahme für einfache Renditen wird von vielen empirischen Asset-Renditen nicht gestützt, weil diese positive Exzess-Kurtosis haben. Auch die Lognormalannahme ist mit positiver Exzess-Kurtosis historischer Aktienrenditen nicht vereinbar.
- Nichtnormale stabile Verteilungen können die Exzess-Kurtosis historischer Aktienrenditen erfassen. Mischungen von Normalverteilungen haben endliche höhere Momente und können die Exzess-Kurtosis ebenfalls erfassen.
- Die meisten Reihen in Tabelle 1.3 haben positive Exzess-Kurtosis.
- In R ist kurtosis die Exzess-Kurtosis, für die täglichen prozentualen einfachen IBM-Renditen 9,91636. In S-Plus ist kurtosis die gewöhnliche Kurtosis ohne Abzug von 3, für dieselbe Reihe 12,92.
- Unter normalverteilten Innovationen ist die unbedingte Kurtosis eines ARCH(1)-Schocks gleich 3 mal (1 minus alpha 1 quadrat) durch (1 minus 3 alpha 1 quadrat) und damit größer als 3.
- Die Excess-Kurtosis ist positiv, die Ränder sind schwerer als bei der Normalverteilung; ein bedingt gaußscher ARCH(1)-Schock erzeugt Ausreißer leichter als gaußsches weißes Rauschen.
- Damit das vierte Moment endlich ist, muss alpha 1 quadrat im Intervall von 0 bis unter 1/3 liegen; das vierte Moment selbst ist 3 alpha 0 quadrat mal (1 plus alpha 1) durch [(1 minus alpha 1) mal (1 minus 3 alpha 1 quadrat)].
- Dieselbe Restriktion begrenzt in der Praxis die Fähigkeit gaußscher ARCH-Modelle, Excess-Kurtosis zu erfassen.
- Beim Intel-ARCH(1) liegt das Quadrat des geschätzten Koeffizienten 0,356 unter 1/3, deshalb existiert das unbedingte vierte Moment der monatlichen Logrendite.
- Schiefe, Kurtosis und QQ-Plot der standardisierten Residuen prüfen die angenommene Verteilung der Innovationen.
- Eine standardisierte Student-t oder eine verallgemeinerte Fehlerverteilung mit Parameter v kleiner als 2 wird verwendet, wenn die Ränder dicker sein sollen als bei der Normalverteilung; bei der verallgemeinerten Fehlerverteilung ist v gleich 2 genau der gaußsche Fall.
- Für ein GARCH(1,1) ist die Kurtosis, sofern 1 minus 2 alpha 1 quadrat minus (alpha 1 plus beta 1) quadrat größer als 0 ist, gleich 3 mal [1 minus (alpha 1 plus beta 1) quadrat] geteilt durch [1 minus (alpha 1 plus beta 1) quadrat minus 2 alpha 1 quadrat] und größer als 3.
- Die Randverteilung eines GARCH(1,1) ist damit schwerer als die Normalverteilung.
- Empirische Studien hochfrequenter Finanzreihen zeigen, dass die Ränder von GARCH-Modellen selbst mit standardisierten Student-t-Innovationen zu kurz bleiben; weitere Angaben zur Kurtosis stehen in Abschnitt 3.16.
- Die standardisierten Residuen des gaußschen Intel-ARCH(1) und des GARCH(1,1) verwerfen die Normalität: Jarque-Bera 137,919 beziehungsweise 165,574, beide mit p-Wert 0.
- Haben die täglichen Logrenditen hohe Exzess-Kurtosis und serielle Korrelationen, können die Stichprobenschätzer der Monatsvolatilität aus Tagesrenditen, Gleichungen (3.49) und (3.50), inkonsistent sein (Bai, Russell und Tiao, 2004).
- Die Unsicherheit einer Volatilitätsschätzung verlangt die Kurtosis des Volatilitätsmodells. Abgeleitet wird die Exzess-Kurtosis eines GARCH(1,1); dieselbe Idee gilt für andere GARCH-Modelle.
- Die Innovation erfüllt E(ε_t) = 0, Var(ε_t) = 1 und E(ε⁴_t) = K_ε + 3. K_ε ist die Exzess-Kurtosis von ε_t.
- Es gilt Var(a_t) = α₀ / [1 − (α₁ + β₁)] und E(a⁴_t) = (K_ε + 3) E(σ⁴_t), sofern das vierte Moment der bedingten Varianz existiert.
- Die Exzess-Kurtosis von a_t ist K_a = (K_ε + 3)[1 − (α₁ + β₁)²] / [1 − 2α₁² − (α₁ + β₁)² − K_ε α₁²] − 3, sofern sie existiert.
- Bei normalem ε_t ist K_ε = 0 und K^{(g)}_a = 6α₁² / [1 − 2α₁² − (α₁ + β₁)²]. Die Kurtosis existiert nur bei positivem Nenner. α₁ = 0 ergibt K^{(g)}_a = 0, also keine schweren Ränder.
- Für nichtnormales ε_t gilt K_a = [K_ε + K^{(g)}_a + (5/6) K_ε K^{(g)}_a] / [1 − (1/6) K_ε K^{(g)}_a]. Das Resultat stammt von George C. Tiao und gilt für alle GARCH-Modelle, sofern die Kurtosis existiert (Bai, Russell und Tiao, 2003).
- Ist α₁ = 0, gilt K_a = K_ε, und das Randverhalten von a_t gleicht dem des standardisierten Rauschens. Ist α₁ > 0, ist K^{(g)}_a > 0, und a_t hat schwere Ränder. α₁ ist damit entscheidend für die Ränder.
- Für ARCH(1) gilt K^{(g)}_a = 6α₁² / (1 − 3α₁²), sofern 1 > 3α₁², und K_a = (K_ε + 3)(1 − α₁²) / [1 − (K_ε + 3)α₁²] − 3.
- Für eine standardisierte Student-t mit v > 4 ist die Exzess-Kurtosis K_ε = 6/(v − 4), weil E(ε⁴_t) = 6/(v − 4) + 3. Deshalb wird eine t-Verteilung mit 5 Freiheitsgraden verwendet, wenn die Freiheitsgrade vorgegeben sind.
- Die Exzess-Kurtosis von a_t ist dann K_a = [6 + (v + 1) K^{(g)}_a] / [v − 4 − K^{(g)}_a], sofern 1 − 2α₁²(v − 1)/(v − 4) − (α₁ + β₁)² > 0.
- E(σ⁴_t) = α₀²(1 + α₁ + β₁) / {[1 − (α₁ + β₁)][1 − α₁²(K_ε + 2) − (α₁ + β₁)²]}, sofern 1 > α₁ + β₁ ≥ 0 und 1 − α₁²(K_ε + 2) − (α₁ + β₁)² > 0.
- Die Exzess-Kurtosis der täglichen Logpreis-Range von Apple vom 4. Januar 1999 bis 20. November 2007 beträgt 2,13, bei einer Schiefe von 1,3.
- Die Exzess-Kurtosis der täglichen IBM-Logrenditen 1998 beträgt 2,396 bei einem asymptotischen Standardfehler von 0,306 und gibt zusammen mit der Schiefe Anlass, die Normalannahme zu bezweifeln.
- Die vom Kou-Sprungdiffusionsmodell implizierten Renditen sind leptokurtisch und bezüglich null asymmetrisch.
- Die aus Gleichung (6.31) abgeleitete Verteilung hat bei Mittel 0 und Varianz 2,0572×10^−4 einen höheren Gipfel und dickere Ränder als die Normalverteilung mit denselben beiden Momenten.
- In endlichen Stichproben ist eine doppelte Exponentialverteilung schwer von einer Student-t-Verteilung zu unterscheiden; analytisch ist sie handlicher und kann um den Mittelwert eine höhere Wahrscheinlichkeitskonzentration erzeugen.
- Histogramme beobachteter Asset-Renditen haben tendenziell einen höheren Gipfel als die Normaldichte.
- Die doppelte Exponentialverteilung und die Normalverteilung mit Mittel 0 und Varianz 0,0008 unterscheiden sich sichtbar im höheren Gipfel der doppelten Exponentialdichte.
- Wertpapierrenditen haben häufig schwere Ränder, sodass die Normalannahme von RiskMetrics den VaR oft unterschätzt.
- Die Fréchet-Familie der Extremwertverteilung, ξ > 0, umfasst stabile Verteilungen und die Student-t und entspricht einem potenzartigen rechten Schwanz; die Gumbel-Familie, ξ = 0, umfasst dünnschwänzige Verteilungen wie Normal und Lognormal.
- Der Text liest aus den Hill-Plots, dass der Formparameter für die negativen IBM-Extreme größer wirkt und der linke Schwanz der Tageslogrendite schwerer sein kann.
- Die endliche Stichprobenverteilung der Kreuzkorrelationen von Assetrenditen ist unter anderem wegen hoher Kurtosis kompliziert, neben der bedingten Heteroskedastizität.
- Empirisch können die multivariaten gaußschen Innovationen der vorigen Volatilitätsmodelle die Kurtosis der Asset-Renditen verfehlen. Eine multivariate Student-t-Verteilung kann dann für die Volatilitätsmodellierung nützlich sein.
- In der einfachen multivariaten Student-t mit v Freiheitsgraden, Mittel null und Einheitsmatrix ist die Varianz jeder Komponente v geteilt durch (v minus 2). Die standardisierte Version ist εt gleich der Wurzel aus (v minus 2) geteilt durch v, mal x.

## Funktionsweise

- Die Stichprobenkurtosis ist 1/((T − 1) σ̂x hoch 4) mal der Summe der vierten Potenzen der Abweichungen vom Stichprobenmittel.
- Unter Normalität ist die Stichproben-Exzess-Kurtosis asymptotisch normal mit Mittelwert null und Varianz 24/T.
- Bei einer Skalenmischung ist die Logrendite bedingt normal mit Mittel µ und Varianz σ², wobei σ² selbst zufällig ist und einer positiven Verteilung folgt, zum Beispiel σ hoch −2 einer Gammaverteilung.
- Ein Beispiel einer endlichen Mischung ist rt = (1 − X) N(µ, σ1²) + X N(µ, σ2²), wobei X Bernoulli mit P(X = 1) = α und 0 < α < 1 ist, σ1² klein und σ2² vergleichsweise groß.
- Mit α = 0,05 folgen 95 Prozent der Renditen N(µ, σ1²) und 5 Prozent N(µ, σ2²). Das große σ2² legt mehr Masse auf die Ränder, der kleine Anteil aus der zweiten Komponente lässt die Mehrheit der Renditen einer einfachen Normalverteilung folgen.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Der Test H0: K(r) − 3 = 0 gegen Ha: K(r) − 3 ≠ 0 verwendet t = (Stichprobenkurtosis − 3) / Wurzel(24/T) und verwirft H0 genau dann, wenn der p-Wert kleiner als das Signifikanzniveau α ist.
- Jarque und Bera (1987) kombinieren Schiefe und Exzess-Kurtosis zu JB = Schiefequadrat / (6/T) + (Kurtosis − 3) zum Quadrat / (24/T), asymptotisch chi-quadrat mit 2 Freiheitsgraden.

## Risiken und Grenzen

- Die Parameter der Mischung, etwa α im endlichen Fall, sind schwer zu schätzen.
- Nichtnormale stabile Verteilungen haben keine endliche Varianz, im Konflikt mit den meisten Finanztheorien, und ihre statistische Modellierung ist schwierig.

## Beispiele

- Tabelle 1.2, Exzess-Kurtosis der täglichen einfachen Renditen in Prozent, Stichprobe endet am 31. Dezember 2008: S&P 22,81, value-weighted 18,02, equal-weighted 17,08, IBM 9,92, Intel 6,13, 3M 13,34, Microsoft 9,92, Citigroup 55,25.
- Dieselbe Tabelle, tägliche Logrenditen: S&P 30,20, value-weighted 21,56, equal-weighted 17,76, IBM 12,17, Intel 7,81, 3M 20,57, Microsoft 14,23, Citigroup 33,19.
- Monatliche einfache Renditen: S&P 9,47, value-weighted 7,69, equal-weighted 14,94, IBM 3,43, Intel 2,70, 3M 0,98, Microsoft 1,96, Citigroup 1,77. Monatliche Logrenditen: S&P 7,93, value-weighted 6,85, equal-weighted 8,55, IBM 2,62, Intel 3,06, 3M 1,25, Microsoft 1,59, Citigroup 3,76.
- Abbildung 1.1 vergleicht die Dichten einer endlichen Mischung (1 − X) N(0, 1) + X N(0, 16) mit P(X = 1) = 0,05, der Cauchy-Verteilung mit Dichte 1/(π(1 + x²)) und der Standardnormalverteilung. Die Cauchy-Verteilung hat dickere Ränder als die Mischung, und diese hat dickere Ränder als die Standardnormalverteilung.
- Der Jarque-Bera-Test verwirft die Normalität der prozentualen IBM-Logrenditen: in R X-squared = 60921,9343, asymptotischer p-Wert kleiner als 2,2e-16; in S-Plus Teststatistik 60921,93 und p-Wert 0,00.
- Eine standardisierte Student-t mit 5 Freiheitsgraden im AR(2)–GARCH(1,1) hebt gegenüber der Normalannahme den 1-Prozent-VaR einer IBM-Long-Position von 10 Millionen Dollar von 409.738 auf 475.943 Dollar, während der 5-Prozent-VaR mit 283.520 gegen 287.700 Dollar nahezu gleich bleibt.
- In Tabelle 8.1 beträgt die Überschusskurtosis der monatlichen prozentualen Logrenditen von Januar 1926 bis Dezember 2008 für IBM 2,622 und für den S&P 500 7,927.
- Die vier Tagesrenditen von Euro-Kurs, Yen-Kurs, IBM und Dell, Januar 1999 bis Dezember 2004, 1496 Beobachtungen, haben schwere Ränder mit positiver Exzess-Kurtosis. Die Werte sind 2,7090 für den Euro-Kurs, 2,0332 für den Yen-Kurs, 6,2164 für IBM und 3,3054 für Dell.
- Die standardisierten Innovationen des zugehörigen DCC-Modells werden als multivariate Student-t-Verteilung modelliert. Die geschätzten Freiheitsgrade liegen je nach Spezifikation bei 7,8729, 7,8772, 7,9180 und im Hebelmodell bei 8,4527.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 267–286 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-015-p267-p286|S. 267–286]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 286–305 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-016-p286-p305|S. 286–305]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 14–33 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-002-p014-p033|S. 14–33]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 33–51 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-003-p033-p051|S. 33–51]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 163–165 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-012-p163-p165|S. 163–165]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 20–39 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-002-p020-p039|S. 20–39]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 39–58 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-003-p039-p058|S. 39–58]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 134–153 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-008-p134-p153|S. 134–153]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 153–172 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-009-p153-p172|S. 153–172]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 191–210 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-011-p191-p210|S. 191–210]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 286–305 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-016-p286-p305|S. 286–305]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 305–324 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-017-p305-p324|S. 305–324]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 324–343 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-018-p324-p343|S. 324–343]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 343–362 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-019-p343-p362|S. 343–362]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 362–381 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-020-p362-p381|S. 362–381]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 419–438 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-023-p419-p438|S. 419–438]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 552–571 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-030-p552-p571|S. 552–571]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 571–590 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-031-p571-p590|S. 571–590]]

## Verwandte Themen
