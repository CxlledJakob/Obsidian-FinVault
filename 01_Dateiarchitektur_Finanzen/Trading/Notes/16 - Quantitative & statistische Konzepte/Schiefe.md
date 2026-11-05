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

# Schiefe


## Kurzdefinition

- Die Schiefe der Renditen ist ein Eingang der Probabilistic Sharpe Ratio.
- Die Schiefe ist das normierte dritte zentrale Moment S(x) = E[(X − µx) hoch 3 geteilt durch σx hoch 3]; das dritte zentrale Moment misst die Symmetrie von X bezüglich seines Mittelwerts.

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
- Die dritte Auflage führt schiefe Verteilungen für die Volatilitätsmodellierung in Kapitel 3 ein.
- Unter Normalität ist die Stichprobenschiefe asymptotisch normal mit Mittelwert null und Varianz 6/T.
- Die Schiefe ist nach den deskriptiven Statistiken in Tabelle 1.2 weder bei Tages- noch bei Monatsrenditen ein ernstes Problem.
- In R beträgt die Schiefe der prozentualen täglichen einfachen IBM-Renditen 0,06139878, die Teststatistik 2,487093 und der p-Wert 0,01287919.
- In S-Plus beträgt die Schiefe derselben Reihe 0,06141, die Teststatistik 2,487851 und der p-Wert 0,01285177.
- Empirische Renditeverteilungen können neben dicken Rändern auch schief sein; die Student-t wird dafür zu einer schiefen Student-t abgeändert.
- Fernández und Steel (1998) führen Schiefe in jede stetige, unimodale und um null symmetrische Verteilung ein; Lambert und Laurent (2001) wenden das auf die standardisierte Student-t der ARCH-Innovationen an.
- Xi ist der Schiefeparameter, und xi quadrat ist das Verhältnis der Wahrscheinlichkeitsmasse oberhalb zur Masse unterhalb des Modus, also ein Maß der Schiefe.
- Die Parameter rho und omega dieser Dichte hängen von den Freiheitsgraden v größer als 2 und von xi ab.
- Im Paket fGarch stehen die schiefe Student-t, die schiefe Normalverteilung und die schiefe verallgemeinerte Fehlerverteilung als sstd, snorm und sged bereit.
- Die Schiefe der standardisierten Residuen wird zusammen mit Kurtosis und QQ-Plot benutzt, um die Verteilungsannahme eines ARCH-Modells zu prüfen.
- Die Schiefe der täglichen Logpreis-Range von Apple vom 4. Januar 1999 bis 20. November 2007 beträgt 1,3, bei einer Exzess-Kurtosis von 2,13.
- Die Schiefe der täglichen IBM-Logrenditen 1998 beträgt −0,464 bei einem asymptotischen Standardfehler von 0,153.
- Die vom Sprungdiffusionsmodell von Kou implizierten Renditen sind bezüglich null asymmetrisch und zugleich leptokurtisch.
- X = ln(J) folgt einer doppelten Exponentialverteilung mit Dichte (1/(2η)) e^{−|x−κ|/η}, 0 < η < 1, auch Laplace-Verteilung genannt; E(X) = κ.
- X − κ ist mit Wahrscheinlichkeit 0,5 gleich ξ und mit Wahrscheinlichkeit 0,5 gleich −ξ, wobei ξ exponentialverteilt ist mit Mittel η und Varianz η².
- Im numerischen Beispiel ist κ = −0,02, also eine mittlere Sprunggröße von −2 Prozent; die Dichtevergleiche zeigen den linken und den rechten Rand getrennt.
- Der Text schließt aus den Hill-Plots der IBM-Tageslogrenditen, dass der Formparameter für die negativen Extreme größer wirkt und der linke Schwanz schwerer sein kann als der rechte.

## Funktionsweise

- Die Stichprobenschiefe ist 1/((T − 1) σ̂x hoch 3) mal der Summe der dritten Potenzen der Abweichungen vom Stichprobenmittel.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Getestet wird H0: S(r) = 0 gegen Ha: S(r) ≠ 0 mit t = Stichprobenschiefe / Wurzel(6/T). Verworfen wird zum Niveau α, wenn der Betrag von t das obere 100(α/2)-Quantil der Standardnormalverteilung übersteigt oder der p-Wert kleiner als α ist.

## Risiken und Grenzen


## Beispiele

- Für die täglichen einfachen IBM-Renditen liefert die Schiefe 0,0614 die Statistik t = 0,0614 / 0,0247 = 2,49 und einen p-Wert von etwa 0,013; die Reihe ist auf dem 5-Prozent-Niveau signifikant rechtsschief. Im R-Output steht die Schiefe 0,061399.
- Tabelle 1.2, Schiefe der täglichen einfachen Renditen: S&P −0,73, value-weighted −0,62, equal-weighted −0,77, IBM 0,06, Intel −0,15, 3M −0,36, Microsoft −0,13, Citigroup 1,80.
- Tägliche Logrenditen: S&P −1,17, value-weighted −0,94, equal-weighted −1,00, IBM −0,27, Intel −0,54, 3M −0,78, Microsoft −0,63, Citigroup 0,22.
- Monatliche einfache Renditen: S&P 0,32, value-weighted 0,15, equal-weighted 1,52, IBM 0,44, Intel 0,32, 3M 0,22, Microsoft 0,66, Citigroup −0,47. Monatliche Logrenditen: S&P −0,52, value-weighted −0,58, equal-weighted 0,25, IBM −0,07, Intel −0,55, 3M −0,08, Microsoft 0,10, Citigroup −1,09.
- Bei q = 190, 200 und 210 liegen die Hill-Schätzer für die positiven IBM-Renditen bei 0,300, 0,299 und 0,305 und für die negativen bei 0,290, 0,292 und 0,289.
- Die Maximum-Likelihood-Formparameter der Minima sind ab einer Blocklänge von 63 etwa 0,33; die der Maxima sind kleiner und weniger stabil, bleiben aber signifikant von null verschieden.
- Die monatlichen prozentualen Logrenditen von Januar 1926 bis Dezember 2008 haben die Schiefe minus 0,068 für IBM und minus 0,521 für den S&P 500.
- Die Schiefe der Tagesrenditen von Euro-Kurs, Yen-Kurs, IBM und Dell, Januar 1999 bis Dezember 2004, 1496 Beobachtungen, beträgt 0,0342, minus 0,1674, minus 0,0530 und minus 0,0383.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 191–210 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-011-p191-p210|S. 191–210]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 248–267 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-014-p248-p267|S. 248–267]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 20–39 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-002-p020-p039|S. 20–39]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 39–58 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-003-p039-p058|S. 39–58]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 134–153 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-008-p134-p153|S. 134–153]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 286–305 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-016-p286-p305|S. 286–305]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 305–324 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-017-p305-p324|S. 305–324]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 324–343 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-018-p324-p343|S. 324–343]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 362–381 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-020-p362-p381|S. 362–381]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 419–438 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-023-p419-p438|S. 419–438]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 552–571 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-030-p552-p571|S. 552–571]]

## Verwandte Themen
