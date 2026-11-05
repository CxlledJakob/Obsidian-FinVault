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

# Kovarianz


## Kurzdefinition

- Eine nicht singuläre Kovarianzmatrix der Größe N braucht mindestens halb so viele unabhängige und identisch verteilte Beobachtungen, wie das Produkt aus N und N plus 1.

## Kernaussagen

- Quadratische Programmierung verlangt die Inverse einer positiv definiten Kovarianzmatrix, also lauter positive Eigenwerte.
- Die Inversion ist fehleranfällig, wenn die Matrix numerisch schlecht konditioniert ist.
- Für eine invertierbare Matrix der Größe 50 braucht man mindestens fünf Jahre täglicher IID-Daten.
- Eine größere Matrix verschärft das Problem, weil jeder Kovarianzkoeffizient mit weniger Freiheitsgraden geschätzt wird.
- Hierarchical Risk Parity nutzt die Kovarianzmatrix, ohne Invertierbarkeit oder positive Definitheit zu verlangen, und rechnet auch auf einer singulären Matrix.
- Eine Matrix der Größe N entspricht einem vollständigen Graphen mit halb so vielen Kanten, wie das Produkt aus N und N minus 1.
- Eine Kovarianzmatrix von 50 mal 50 hat 50 Knoten und 1225 Kanten.
- Die Wurzel der Instabilität quadratischer Optimierer ist die verlangte Inversion der Kovarianzmatrix.
- Q(t) ist die Varianz des Prognosefehlers der beobachtbaren Variable, gebildet als x transponiert mal R mal x plus Ve, und ist von der Kovarianz der verborgenen Variable zu unterscheiden.
- R(t|t minus 1) ist die Kovarianz des Fehlers der verborgenen Variable, cov(β(t) minus β-Dach(t|t minus 1)), und eine 2-mal-2-Matrix, weil β aus Mittel des Spreads und Hedge Ratio besteht. R(t|t) ist die Kovarianz nach dem Update.
- Vω, die Kovarianz des Zustandsrauschens, wird als δ/(1 minus δ) mal der Einheitsmatrix gesetzt. Ve, die Varianz des Messrauschens, ist im Beispiel 0,001. Die Zustandskovarianz-Prognose addiert Vω.
- Im Modell mit einem einzelnen Mittelpreis ist R die Varianz des Fehlers dieses Mittels. Q(t) ist Var(m(t)) plus Ve, und das Varianz-Update lautet R(t|t) = (1 minus K(t)) mal R(t|t minus 1), mit K(t) = R(t|t minus 1) / (R(t|t minus 1) + Ve).
- Die Kelly-Formel für mehrere Portfolios setzt den Hebelvektor F gleich der Inversen der Kovarianzmatrix C der Portfoliorenditen mal dem Vektor M der mittleren Excess Returns.
- Bei risikofreiem Zins null ist die annualisierte zusammengesetzte Wachstumsrate bei diesen optimalen Hebeln g gleich F transponiert mal C mal F geteilt durch 2.
- Im Beispiel ist die Korrelation der beiden Strategierenditen null, und daraus folgen Kelly-Hebel von 4,4 und 4,9 bei annualisierten Überschussrenditen von 30 und 60 Prozent und Volatilitäten von 26 und 35 Prozent.

## Funktionsweise

- Die Quasi-Diagonalisierung ordnet Zeilen und Spalten so, dass die größten Werte auf der Diagonale liegen, ohne einen Basiswechsel.
- Ähnliche Anlagen stehen danach beieinander und unähnliche weit auseinander.
- Die Varianz einer Teilmenge wird als quadratische Form einer Inverse-Varianz-Gewichtung definiert.
- Ist die Kovarianzmatrix diagonal, ist das Minimum-Varianz-Gewicht proportional zum Kehrwert der eigenen Varianz.
- Bei zwei Teilmengen ist der Anteil der ersten Hälfte eins minus der Bruch aus ihrer Varianz und der Summe beider Varianzen.
- Die Rauschterme des Kalman-Filters werden bei Mittelwert null durch eine sich entwickelnde Kovarianzmatrix beschrieben.
- R(t gegeben t−1) ist die Kovarianz des Fehlers der verborgenen Variable, nicht eine Varianz, weil β aus Achsenabschnitt und Steigung besteht, und R ist deshalb eine 2-mal-2-Matrix.
- Die Zustandsprognose erhöht diese Kovarianz um Vw, und das Update zieht Gain mal x mal R wieder ab.
- Vw wird als (δ geteilt durch 1 minus δ) mal der Einheitsmatrix angesetzt.
- In der Mehrportfolio-Kelly-Formel ist C die Kovarianzmatrix der Portfoliorenditen, und der Hebelvektor ist C hoch minus 1 mal dem Vektor der mittleren Excess Returns.
- Bei risikofreiem Zins null und optimalen Hebeln ist die annualisierte zusammengesetzte Wachstumsrate F transponiert mal C mal F, geteilt durch 2.
- Diese Wachstumsformel gilt nur bei den optimalen Hebeln.

## Voraussetzungen


## Anwendung im Trading

- Prognostizierte Renditen, Ledoit-Wolf-Shrinkage und Black-Litterman-Sichten lassen sich in den hierarchischen Ansatz einbauen.
- Dieselbe Idee, Matrixinversionen zu vermeiden, kann instabile Verfahren wie VAR oder VECM ersetzen.
- Weitere Einsätze bei fast singulärer Kovarianzmatrix sind die Kapitalallokation auf Manager, algorithmische Strategien, Bagging, Boosting und Random-Forest-Prognosen.

## Regeln und Kriterien


## Risiken und Grenzen

- Mit so vielen Kanten dürfen Gewichte völlig frei umschichten, und kleine Schätzfehler führen zu völlig anderen Lösungen.
- Nebenbedingungen, Black-Litterman-Priors oder eine stabilere Inverse nach Ledoit und Wolf bleiben in Geometrie, linearer Algebra und Analysis und beheben die fehlende Hierarchie nicht.
- Die Annahme einer diagonalen Kovarianzmatrix bringt dem Inverse-Varianz-Portfolio etwas Stabilität, seine Varianz liegt aber weiter über der von Hierarchical Risk Parity.
- Simulierte Renditen verfehlen serielle Korrelationen, die in historischen Strategierenditen stecken können, in die Zukunft fortbestehen und den maximalen Drawdown in der realen Welt senken können.
- Historische Strategierenditen erfassen diese Korrelationen vollständig.

## Beispiele

- Die Konditionszahl der Kovarianzmatrix im Zahlenbeispiel beträgt 150,9324.
- Außer Stichprobe betragen die Portfoliovarianzen 0,1157 für CLA, 0,0928 für das Inverse-Varianz-Portfolio und 0,0671 für Hierarchical Risk Parity.
- Im Beispiel ist die Korrelation der beiden Strategien null, und die Renditen sind gaußisch.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 248–267 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-014-p248-p267|S. 248–267]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 76–95 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-006-p076-p095|S. 76–95]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 180–199 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-014-p180-p199|S. 180–199]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 39–58 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-003-p039-p058|S. 39–58]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 58–77 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-004-p058-p077|S. 58–77]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 77–96 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-005-p077-p096|S. 77–96]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 96–115 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-006-p096-p115|S. 96–115]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 115–134 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-007-p115-p134|S. 115–134]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 248–267 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-014-p248-p267|S. 248–267]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 343–362 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-019-p343-p362|S. 343–362]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 400–419 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-022-p400-p419|S. 400–419]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 419–438 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-023-p419-p438|S. 419–438]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 438–457 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-024-p438-p457|S. 438–457]]
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

## Verwandte Themen
