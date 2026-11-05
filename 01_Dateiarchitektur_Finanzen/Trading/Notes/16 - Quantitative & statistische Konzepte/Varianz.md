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
aktualisiert: 2026-11-01
---

# Varianz


## Kurzdefinition

- Varianz ist der Fehler aus der Empfindlichkeit gegen kleine Änderungen der Trainingsmenge. Ist sie hoch, hat der Algorithmus überangepasst und Rauschen mit Signal verwechselt.
- Noise ist die Varianz der beobachteten Werte, etwa durch unvorhersehbare Änderungen oder Messfehler, und lässt sich durch kein Modell erklären.
- Die Inverse-Varianz-Allokation ist optimal, wenn die Kovarianzmatrix diagonal ist: Das Gewicht ist dann proportional zum Kehrwert der eigenen Varianz.
- Für den charakteristischen Vektor aus Einsen ist die Lösung des quadratischen Programms das Minimum-Varianz-Portfolio.
- Die Varianz der Logpreisänderung über die Spanne τ ist das Mittel von |z(t+τ) minus z(t)| zum Quadrat, mit z gleich log(y).

## Kernaussagen

- Der mittlere quadratische Fehler zerlegt sich in den quadrierten Bias, die Varianz des Schätzers und die Rauschvarianz. Wegen des Rauschens kann er nicht null werden.
- Der Hauptvorteil von Bagging ist, die Varianz der Prognosen zu senken und damit Overfitting zu begegnen.
- Die Varianz des Mittelwerts von N Einzelprognosen ist die mittlere Einzelvarianz mal (mittlere Korrelation plus (1 minus diese Korrelation) geteilt durch N).
- Diese Varianz sinkt nur, solange die mittlere Korrelation unter 1 liegt, und geht gegen die Einzelvarianz, wenn die Korrelation gegen 1 geht.
- Sequenzielles Bootstrap soll möglichst unabhängige Stichproben liefern, die Korrelation senken und damit die Varianz von Bagging-Klassifikatoren verringern.
- Werden richtige Prognosen als 1 gezählt, ist ihre Zahl im Mittel N mal p und ihre Varianz N mal p mal (1 minus p).
- Bei schlechten Einzellernern, deren Trefferquote weit unter 1/k liegt, bleibt das Mehrheitsvotum schlecht, die Varianz ist aber geringer.
- Bagging senkt eher die Varianz als den Bias, weil eine sehr kleine Korrelation leichter zu erreichen ist als eine Trefferquote über 1/k.
- Redundante Beobachtungen machen die Bootstrap-Ziehungen nahezu gleich und treiben die Korrelation gegen 1. Dann sinkt die Varianz nicht, unabhängig von N.
- Entscheidungsbäume erhöhen die Prognosevarianz durch Overfitting. Der Random Forest ist darauf angelegt, sie zu senken, und tut das ohne Overfitting, solange die Korrelation unter 1 bleibt.
- Frühes Stoppen schlecht skalierender Basisschätzer erhöht die Varianz der Einzelergebnisse. Zusätzliche unabhängige Schätzer im Bagging können diesen Anstieg mehr als ausgleichen.
- CLA minimiert die Varianz in der Stichprobe und hat dort die geringere Standardabweichung, 0,4486 gegen 0,4640.
- Außer Stichprobe hat CLA trotzdem die höchste Varianz der drei Verfahren.
- Die Varianzen der Portfoliorenditen außer Stichprobe betragen 0,1157 für CLA, 0,0928 für das Inverse-Varianz-Portfolio und 0,0671 für Hierarchical Risk Parity.
- CLA liegt damit 72,47 Prozent und das Inverse-Varianz-Portfolio 38,24 Prozent über der Varianz von Hierarchical Risk Parity.
- Bei mittleren Renditen nahe 0 verbessert diese Varianzreduktion die Sharpe-Ratio einer CLA-Strategie um etwa 31,3 Prozent.
- Die Annahme einer diagonalen Kovarianzmatrix stabilisiert das Inverse-Varianz-Portfolio, seine Varianz bleibt aber deutlich höher.
- Wird die ADF-Null auf Rohpreisen verworfen, haben die Preise eine endliche Varianz, und die Renditevolatilität muss mit steigenden Preisen fallen und mit fallenden steigen.
- Bei Logpreisen bedingen die Preisniveaus den Renditemittelwert, nicht die Renditevolatilität.
- Ist die Renditevarianz invariant zum Preisniveau, wird ein ADF auf Rohpreisen strukturell heteroskedastisch.
- Beim geometrischen Random Walk ist diese Varianz proportional zu τ, bei Mean Reversion oder Trend proportional zu τ hoch 2H.
- Stationarität heißt, dass die Varianz sublinear in der Zeit wächst und nicht, dass sie zeitunabhängig ist.
- Auch für 0 kleiner H kleiner 0,5 steigt die Varianz mit der Zeit, nur langsamer als bei einem geometrischen Random Walk.
- Manager, deren einziges Ziel das langfristige Nettovermögen ist, achten nicht auf Drawdowns und auf die Volatilität der Renditen.
- Varianz, mittlere absolute Abweichung und Standardabweichung sind weit verbreitete Streuungsmaße und im klassischen statistischen Ansatz wichtig.
- Streuungsmaße beschreiben, wie weit die Beobachtungen einer Stichprobe um ihre zentrale Tendenz liegen, und quantifizieren damit die Breite einer Häufigkeitsverteilung.
- Zentrale Tendenz und Variation sind unabhängige Merkmale einer Häufigkeitsverteilung. Dieselbe Streuung kann mit verschiedenen Mittelwerten einhergehen, derselbe Mittelwert mit verschiedener Streuung, und beides kann zugleich verschieden sein.
- Die Streuung der Stichprobenverteilung des Mittelwerts hängt von der Variation in den Daten der Elternpopulation ab. Je größer diese Variation, desto größer die Streuung der Stichprobenverteilung.
- Ist die Variation in der Population null, ist auch die Variation der Stichprobenmittel null, und die Stichprobenverteilung hat keinerlei Streuung.
- Ist die Variation zwischen den Individuen der Population groß, variieren die Stichprobenmittel stärker, und die Stichprobenverteilung wird breit.
- Varianz, mittlere absolute Abweichung und Standardabweichung sind weit verbreitete Streuungsmaße der klassischen Statistik. Sie quantifizieren die Breite einer Häufigkeitsverteilung.
- Die Varianz ist neben Mittelwert, Median und Standardabweichung ein gebräuchlicher Punktschätzer aus einer Stichprobe.
- Je größer die Variabilität der täglichen Regelrenditen in der Grundgesamtheit, desto breiter ist die Stichprobenverteilung der mittleren Rendite, und je mehr Beobachtungen, desto schmaler ist sie.
- Die Reduktion einer großen Stichprobe liefert zusammenfassende Statistiken, darunter den Stichprobenmittelwert, die Stichprobenvarianz und weitere Maße, die die gesamte Menge beschreiben.
- Ein Faktor für die Größe des Data-Mining-Bias ist die Variation der erwarteten Renditen unter den gebacktesteten Regeln.
- Je geringer diese Variation des wahren Verdienstes, desto größer der Bias; Regeln mit ähnlicher Vorhersagekraft erzeugen einen größeren Bias.
- Der fünfte Faktor des Data-Mining-Bias ist die Variation der erwarteten Renditen unter den getesteten Regeln: je niedriger die Variation der wahren Güte, desto größer der Bias.
- Haben die Regeln ähnliche Grade von Prognosekraft, ist der Data-Mining-Bias größer.
- Abbildung 6.25 stellt niedrige Varianz, alle Regeln gleiche Güte, der hohen Varianz gegenüber, bei der eine Regel deutlich überlegen ist.
- Bei gleicher erwarteter Rendite entstehen alle Unterschiede der beobachteten Performance nur durch Glück; unterscheiden sich die erwarteten Renditen, wird der Bias tendenziell kleiner und unter bestimmten Bedingungen sehr klein.
- Die Zahl der Beobachtungen beeinflusst sowohl die Breite als auch die Randdicke der Stichprobenverteilung der Performancestatistik, mit der die beste Regel ausgewählt wird.
- Je mehr Beobachtungen, desto schmaler die Stichprobenverteilung und desto kleiner der Data-Mining-Bias; je mehr Beobachtungen, desto leichter die Ränder und desto kleiner der Bias.
- Aus den vielen Out-of-Sample-Schätzungen eines Walk-Forward mit zahlreichen Folds lässt sich die Varianz der Performancestatistik bestimmen.
- Der Schrumpfungsgrad bei Markowitz und Xu hängt unter anderem davon ab, wie stark die Tagesrenditen jeder Regel um das große Mittel aller Regeln streuen und wie stark die mittlere Rendite jeder Regel um die mittlere Rendite aller Regeln streut.
- Je kleiner die Variabilität der wahren Qualität, also der erwarteten Rendite, unter den getesteten Regeln, desto größer der Data-Mining-Bias; die Zusammenfassung sagt, dieser Punkt sei experimentell nicht untersucht worden.
- Sind die Beobachtungen seriell korreliert, wie es in einer Zeitreihe vorkommen kann, sinkt die Varianz langsamer, als die Quadratwurzelregel nahelegt.
- Diese Aussage gilt, wenn die Teststatistik der Stichprobenmittelwert ist, aber sie gilt nicht allgemein.
- Bei normalverteilten Preisänderungen ist die Unsicherheit mit 10 Beobachtungen zehnmal so groß wie mit 1.000 Beobachtungen.
- Beim geometrischen Random Walk ist das Mittel von |z(t+τ) minus z(t)| zum Quadrat proportional zu τ. Für großes τ wird daraus eine Gleichheit mit Proportionalitätskonstante, für kleines τ kann die Beziehung von der Geraden abweichen.
- Bei Mean Reversion oder bei positiver Korrelation aufeinanderfolgender Preisbewegungen gilt stattdessen die Proportionalität zu τ hoch 2H, mit Hurst-Exponent H.
- Der Variance-Ratio-Test prüft, ob das Varianzverhältnis Var(τ) geteilt durch τ mal die Varianz des Einsschritts gleich 1 ist. Für USD.CAD wird die Null nicht verworfen, pValue 0,367281.
- Auch eine stationäre Reihe mit 0 < H < 0,5 hat eine Varianz, die mit der Zeit steigt, nur langsamer als beim geometrischen Random Walk. Deshalb wird eine gleitende Standardabweichung benutzt.
- Der Variance-Ratio-Test prüft die Null, dass der Hurst-Exponent wirklich 0,5 ist, also dass das Varianzverhältnis gleich 1 ist.
- Für TU verwirft dieser Test die Random-Walk-Hypothese nicht, obwohl der Hurst-Exponent 0,44 beträgt.
- Der Test kann nicht die einzelnen Zeitrahmen prüfen, in denen die Korrelationen der Renditen stärker als im Durchschnitt sind.
- Unter der Gauß-Annahme ist der Kelly-Hebel f gleich dem mittleren Excess Return m geteilt durch die Varianz s hoch 2 der Excess Returns.
- Eine unterschätzte Varianz überschätzt diesen Hebel und kann bei ausreichender Höhe zum Ruin führen; eine überschätzte Varianz führt nur zu einer untermaximalen Wachstumsrate.
- Im Allokationsbeispiel hat Strategie 1 eine annualisierte Volatilität von 26 Prozent bei 30 Prozent mittlerer Überschussrendite und Strategie 2 eine von 35 Prozent bei 60 Prozent; bei Korrelation null sind die Kelly-Hebel 4,4 und 4,9.
- Für mehrere Portfolios geht die Kovarianzmatrix der Renditen als C in F gleich C hoch minus 1 mal M ein.

## Funktionsweise

- Hierarchical Risk Parity definiert die Varianz einer zusammenhängenden Teilmenge als Varianz einer Inverse-Varianz-Allokation.
- Von oben nach unten werden die Gewichte umgekehrt proportional zu den aggregierten Varianzen der benachbarten Teilmengen geteilt.
- Der Splitfaktor ist eins minus der Bruch aus der Varianz der ersten Hälfte und der Summe beider Teilvarianzen und liegt zwischen 0 und 1.
- Für zwei Anlagen ist das Minimum-Varianz-Gewicht der ersten Anlage eins minus der Bruch aus ihrer Varianz und der Summe beider Varianzen, und Stufe 3 von Hierarchical Risk Parity teilt genauso.
- Ist die Kovarianzmatrix diagonal, ist das Gewicht einer Anlage ihr inverser Varianzterm geteilt durch die Summe aller inversen Varianzen.
- Bei zwei Anlagen ist das Gewicht der ersten Anlage eins minus der Bruch aus ihrer Varianz und der Summe beider Varianzen.
- Stufe 3 von Hierarchical Risk Parity setzt den Anteil der ersten Hälfte auf eins minus den Bruch aus ihrer Varianz und der Summe beider Varianzen.
- Die Cluster-Varianz im Code ist die quadratische Form der Kovarianzscheibe mit Inverse-Varianz-Gewichten.
- Der Variance-Ratio-Test prüft, ob das Verhältnis der Varianz über die Spanne τ zur τ-fachen Ein-Schritt-Varianz gleich 1 ist (Lo, 2001).
- Die Proportionalität zur Zeitspanne wird für großes τ zur Gleichheit und kann für kleines τ von der Geraden abweichen.
- Der Kalman-Filter minimiert den mittleren quadratischen Fehler der geschätzten Variablen und ist unter gaußschem Rauschen der beste Schätzer.
- Q(t) ist die Varianz des Prognosefehlers e(t) und wird als x transponiert mal R mal x plus Ve prognostiziert.
- R ist die Kovarianz des Fehlers der verborgenen Variable; die Varianz des Prognosefehlers ist davon zu unterscheiden.
- Im Market-Making-Modell ist die Prognosevarianz die Varianz des Mittelpreisschätzers plus Ve, und das Zustandsvarianz-Update multipliziert die alte Varianz mit 1 minus dem Kalman-Gain.
- In der Kelly-Formel ist s hoch 2 die Varianz der Excess Returns, und der optimale Hebel ist der mittlere Excess Return geteilt durch diese Varianz.
- Das Pearson-System nimmt neben dem Mittelwert die Standardabweichung sowie Schiefe und Kurtosis als Input der Monte-Carlo-Verteilung.
- Die Varianz des Prognosefehlers im Market-Making-Kalman-Filter ist Q(t) = Var(m(t)) + Ve.
- Der Kalman-Gain ist K(t) = R(t|t − 1) geteilt durch (R(t|t − 1) + Ve), und die aktualisierte Zustandsvarianz ist R(t|t) = (1 − K(t)) mal R(t|t − 1).
- Die Messfehlervarianz Ve wird klein, wenn die Handelsgröße gegenüber einer Benchmark groß ist. Bei T gleich Tmax ist Ve null und der neue Mittelwert gleich dem beobachteten Preis.

## Voraussetzungen

- Die Quadratwurzel-Senkung der Varianz des Mittelwerts setzt unabhängige Beobachtungen voraus.
- Der Zentrale Grenzwertsatz verlangt, dass die Varianz der Elternpopulation endlich ist, neben einem endlichen Mittelwert und unabhängigen Beobachtungen aus derselben Population.
- Der Grundsatz, dass größere Stichproben besser sind, gilt für stationäre Prozesse. Bei höchstwahrscheinlich nichtstationären Finanzzeitreihen können größere Stichproben nicht besser sein.

## Anwendung im Trading

- Bei Finanzbeobachtungen, die nicht unabhängig sind, nennt der Text den sequenziellen Bootstrap als Mittel, die Korrelation und damit die Varianz der gebaggten Prognose zu senken.
- Werden Labels aus der Rendite über 100 Bars gebildet, soll je Schätzer nur 1 Prozent der Beobachtungen gezogen werden, damit die Ziehungen nicht redundant werden und die Varianz nicht stehen bleibt.
- Die Varianzreduktion außer Stichprobe ist für Risk-Parity-Investoren wegen ihres hohen Hebels entscheidend.

## Regeln und Kriterien


## Risiken und Grenzen

- Liegt die mittlere Korrelation der Ensemble-Prognosen nahe 1, verändert Bagging die Varianz praktisch nicht, auch wenn sehr viele Schätzer verwendet werden.
- Bei Labels mit geringer Eindeutigkeit bleibt die Varianzreduktion aus, solange mit Zurücklegen nahezu dieselben Informationen gezogen werden.
- Eine unterschätzte Varianz führt zu einem überschätzten optimalen Hebel und kann zum Ruin führen.
- Schätzfehler der Varianz sind unvermeidlich, und die künftige Varianz muss nicht der historischen entsprechen.
- Kelly über mehrere Strategien ist nur optimal, wenn auch die Volatilitäten unverändert bleiben.

## Beispiele

- Abbildung 6.1 zeigt die Standardabweichung der gebaggten Prognose für N zwischen 5 und 30, mittlere Korrelation zwischen 0 und 1 und mittlere Einzelstandardabweichung 1.
- Die simulierten Gauß-Renditen haben Mittelwert 0 und eine willkürlich gesetzte Standardabweichung von 10 Prozent.
- Für die Logpreise von USD.CAD ist h gleich 0 und pValue gleich 0,367281, das Varianzverhältnis ist also mit dem Random Walk vereinbar.
- Im EWA-EWC-Beispiel wird Ve gleich 0,001 gesetzt, und bei δ gleich 0,0001 ändert sich Q nur langsam.
- Gehandelt wird, wenn der Prognosefehler betragsmäßig größer ist als die Wurzel dieser Prognosevarianz.
- Strategie 1 im Kapitalbeispiel hat 26 Prozent annualisierte Volatilität bei 30 Prozent mittlerem Excess Return, Strategie 2 hat 35 Prozent Volatilität bei 60 Prozent.
- Wägen alle Personen 150 Pfund, hat jede Stichprobe den Durchschnitt 150 Pfund, und die Stichprobenverteilung des Mittelwerts hat keine Streuung.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 115–134 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-007-p115-p134|S. 115–134]]
- Advances in Financial Machine Learning.pdf, S. 248–267 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-014-p248-p267|S. 248–267]]
- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 172–191 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-010-p172-p191|S. 172–191]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 191–210 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-011-p191-p210|S. 191–210]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 229–248 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-013-p229-p248|S. 229–248]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 267–286 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-015-p267-p286|S. 267–286]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 286–305 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-016-p286-p305|S. 286–305]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 305–324 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-017-p305-p324|S. 305–324]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 476–495 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-026-p476-p495|S. 476–495]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 1–13 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-001-p001-p013|S. 1–13]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 52–71 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-004-p052-p071|S. 52–71]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 95–98 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-007-p095-p098|S. 95–98]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 144–163 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-011-p144-p163|S. 144–163]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 180–199 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-014-p180-p199|S. 180–199]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 20–39 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-002-p020-p039|S. 20–39]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 39–58 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-003-p039-p058|S. 39–58]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 58–77 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-004-p058-p077|S. 58–77]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 77–96 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-005-p077-p096|S. 77–96]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 96–115 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-006-p096-p115|S. 96–115]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 115–134 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-007-p115-p134|S. 115–134]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 134–153 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-008-p134-p153|S. 134–153]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 153–172 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-009-p153-p172|S. 153–172]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 191–210 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-011-p191-p210|S. 191–210]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 210–229 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-012-p210-p229|S. 210–229]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 229–248 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-013-p229-p248|S. 229–248]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 248–267 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-014-p248-p267|S. 248–267]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 267–286 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-015-p267-p286|S. 267–286]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 286–305 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-016-p286-p305|S. 286–305]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 305–324 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-017-p305-p324|S. 305–324]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 324–343 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-018-p324-p343|S. 324–343]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 343–362 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-019-p343-p362|S. 343–362]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 362–381 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-020-p362-p381|S. 362–381]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 381–400 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-021-p381-p400|S. 381–400]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 400–419 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-022-p400-p419|S. 400–419]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 419–438 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-023-p419-p438|S. 419–438]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 438–457 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-024-p438-p457|S. 438–457]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 457–476 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-025-p457-p476|S. 457–476]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 476–495 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-026-p476-p495|S. 476–495]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 495–514 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-027-p495-p514|S. 495–514]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 514–533 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-028-p514-p533|S. 514–533]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 533–552 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-029-p533-p552|S. 533–552]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 552–571 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-030-p552-p571|S. 552–571]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 571–590 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-031-p571-p590|S. 571–590]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 590–609 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-032-p590-p609|S. 590–609]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 609–628 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-033-p609-p628|S. 609–628]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 628–647 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-034-p628-p647|S. 628–647]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 647–666 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-035-p647-p666|S. 647–666]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 666–685 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-036-p666-p685|S. 666–685]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 685–704 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-037-p685-p704|S. 685–704]]

## Verwandte Themen
