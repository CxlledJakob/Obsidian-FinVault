---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Modelle"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-01
---

# Kalman-Filter


## Kurzdefinition

- Der Kalman-Filter ist ein optimaler linearer Algorithmus, der den Erwartungswert einer verborgenen Variable anhand des jüngsten Werts einer beobachtbaren Variable aktualisiert (Kleeman, 2007).
- Er schätzt Hedge Ratio und mittleren Spread, ohne ein Gewichtsschema willkürlich zu wählen (Montana, Triantafyllopoulos und Tsagaris, 2009).

## Kernaussagen

- Der Kalman-Filter gehört zu den einfachsten Techniken für den Handel mean-revertierender Portfolios, neben linearen Modellen und Bollinger-Bändern.
- Er ist für Trader auf mehrere Arten und in mehreren Strategien nützlich.
- Vω wird vereinfacht als δ/(1 minus δ) mal der 2-mal-2-Einheitsmatrix gesetzt und Ve als Skalar. δ gleich 0 hält β konstant und reduziert das Filter auf eine OLS-Regression mit festem Achsenabschnitt und fester Steigung. δ gleich 1 lässt β mit der letzten Beobachtung wild schwanken.
- Das optimale δ wird wie der optimale Lookback einer gleitenden Regression auf Trainingsdaten bestimmt. Mit Wissen im Nachhinein werden δ gleich 0,0001 und Ve gleich 0,001 gewählt. Gestartet wird mit β-Dach(1|0) gleich 0 und R(0|0) gleich 0.
- Ve und Vω lassen sich aus den Daten mit Autocovariance Least Squares nach Rajamani und Rawlings (2007, 2009) schätzen.
- Auf EWA als x und EWC als y schwankt die Kalman-Steigung bei diesem δ um 1, und der Achsenabschnitt steigt monoton. Der Prognosefehler e(t) ist die Abweichung des Spreads EWC minus EWA von seinem prognostizierten Mittel; Q(t) ändert sich bei kleinem δ nur langsam.
- Long, wenn e unter minus der Wurzel von Q liegt, Short, wenn e darüber liegt. Die übrige Positionsführung folgt dem Bollinger-Code, mit der Kalman-Steigung als Hedge Ratio. APR 26,2 Prozent, Sharpe Ratio 2,4, Abbildung 3.8.
- Für eine einzelne Reihe ist der verborgene Zustand der Mittelpreis m(t). Die Messgleichung ist y(t) = m(t) + ε(t), der Übergang m(t) = m(t minus 1) + ω(t minus 1). Das Update ist m(t|t) = m(t|t minus 1) + K(t) mal (y(t) minus m(t|t minus 1)), mit Q(t) = Var(m(t)) + Ve, K(t) = R(t|t minus 1) / (R(t|t minus 1) + Ve) und R(t|t) = (1 minus K(t)) mal R(t|t minus 1).
- Ein kurzes gleitendes Fenster verändert Hedge Ratio, Mittel und Standardabweichung sprunghaft beim Austausch des ältesten gegen den neuesten Bar. Ein EMA gewichtet neue Daten stärker, doch der exponentielle Abfall ist nicht als optimal begründet.

## Funktionsweise

- Linear heißt, dass die beobachtbare Variable eine lineare Funktion der verborgenen plus Rauschen ist und die verborgene Variable zur Zeit t eine lineare Funktion ihres Werts bei t minus 1 plus Rauschen ist.
- Die Rauschterme sind gaußsch und werden bei Mittelwert null durch eine sich entwickelnde Kovarianzmatrix beschrieben.
- Optimal heißt: unter gaußschem Rauschen der beste Schätzer, und er minimiert den mittleren quadratischen Fehler.
- Anzugeben sind beobachtbare Variable, verborgene Variable, Zustandsübergangsmodell und Beobachtungsmodell; der Rest ist ein vorhandener Algorithmus.
- Für Hedge Ratio und Mittelwert des Spreads ist y beobachtbar und β die verborgene Hedge Ratio; die Messgleichung ist y(t) gleich x(t) mal β(t) plus ε(t), mit Varianz Ve des Rauschens.
- β ist ein 2-mal-1-Vektor aus Achsenabschnitt μ und Steigung, x wird um Einsen erweitert und ist das Beobachtungsmodell; nur y als beobachtbar und x als Modell zu bezeichnen, ist ein mathematischer Trick.
- Der Zustandsübergang ist β(t) gleich β(t−1) plus ω(t−1), und das Übergangsmodell ist die Einheitsmatrix.
- Die Zustandsprognose setzt den erwarteten β fort, die Zustandskovarianz wird um Vw erhöht, die Messprognose ist x mal diesem β, und die Prognosevarianz Q ist x transponiert mal R mal x plus Ve.
- Nach der Beobachtung ist das Update erwartetes β plus Kalman-Gain mal Prognosefehler e, und die Kovarianz wird um Gain mal x mal R verringert; der Gain ist R mal x geteilt durch Q.
- Der Achsenabschnitt ersetzt den gleitenden Durchschnitt des Spreads, und die Standardabweichung des Prognosefehlers ersetzt die gleitende Standardabweichung eines Bollinger-Bands.
- Der mittlere Preis m(t) ist die verborgene Variable, der Preis y(t) die beobachtbare Variable.
- Die Measurement Equation setzt den beobachteten Preis als mittleren Preis plus Messfehler an, und die State Transition setzt m(t) gleich m(t minus 1) plus einer Zustandsstörung ω(t minus 1).
- Das State Update lautet m(t gegeben t) gleich m(t gegeben t minus 1) plus K(t) mal der Differenz aus y(t) und m(t gegeben t minus 1).
- Die Varianz des Prognosefehlers ist Q(t) gleich Var(m(t)) plus Ve.
- Der Kalman-Gain ist K(t) gleich R(t gegeben t minus 1) geteilt durch R(t gegeben t minus 1) plus Ve.
- Das Update der Zustandsvarianz ist R(t gegeben t) gleich (1 minus K(t)) mal R(t gegeben t minus 1).
- Ve misst die Unsicherheit des beobachteten Transaktionspreises und wird in der praktischen Fassung zusätzlich von der Zeit abhängig gemacht: eine große Trade-Größe gegenüber der Benchmark bedeutet eine kleine Unsicherheit und umgekehrt.
- Ist die Trade-Größe T gleich der Benchmark Tmax, ist die Unsicherheit des beobachteten Preises null, der Kalman-Gain ist 1, und die neue Schätzung m(t) ist genau der beobachtete Preis.
- Tmax kann ein Bruchteil des gesamten Handelsvolumens des Vortags sein; der genaue Bruchteil wird mit Trainingsdaten optimiert.
- Größere Trades und jüngere Trade-Preise erhalten mehr Gewicht; der Ansatz ist damit einem volumen- und zeitgewichteten Durchschnittspreis vergleichbar.
- Im Market-Making-Einsatz schätzt der Kalman-Filter nur den Mittelpreis einer einzelnen mean-revertierenden Reihe. Die Hedge Ratio zweier kointegrierender Reihen wird dabei nicht gesucht.
- Der Mittelpreis m(t) ist die verborgene Variable und der Preis y(t) die beobachtbare. Die Messgleichung lautet y(t) = m(t) + ε(t).
- Die Zustandsübergangsgleichung lautet m(t) = m(t − 1) + ω(t − 1).
- Das Zustands-Update lautet m(t|t) = m(t|t − 1) + K(t) mal (y(t) − m(t|t − 1)).
- Die Varianz des Prognosefehlers ist Q(t) = Var(m(t)) + Ve.
- Der Kalman-Gain ist K(t) = R(t|t − 1) geteilt durch (R(t|t − 1) + Ve).
- Das Update der Zustandsvarianz lautet R(t|t) = (1 − K(t)) mal R(t|t − 1).
- Nach Sinclair (2010) ist das ein bevorzugtes Modell, mit dem Market Maker ihren Schätzer für den Mittelpreis eines Assets aktualisieren.
- Praktiker machen die Messunsicherheit Ve zeitabhängig. Eine große Handelsgröße gegenüber einer Benchmark bedeutet kleine Unsicherheit, und umgekehrt.
- Ist die Handelsgröße T gleich der Benchmark Tmax, ist die Unsicherheit des beobachteten Preises null, der Kalman-Gain gleich 1, und der neue Mittelwert m(t) exakt der beobachtete Preis.
- Gegenüber einem VWAP gewichtet dieser Filter nicht nur größere Trades stärker, sondern auch jüngere Preise. Das entspricht einem volumen- und zeitgewichteten Durchschnittspreis.
- Der erwartete Preis eines Instruments lässt sich so aus dem letzten Trade, also aus Preis und Größe, dynamisch nachführen.

## Voraussetzungen

- Als Eingaben für diese Tests und Strategien kommen Rohpreise, Log-Preise oder Verhältnisse infrage, und es wird gezeigt, welche Wahl am sinnvollsten ist.

## Anwendung im Trading

- Der Kalman-Filter ist ein von Market Makern favorisiertes Modell, um die Schätzung des mittleren Preises eines Assets zu aktualisieren, worauf Euan Sinclair 2010 hingewiesen hat.
- In dieser Anwendung geht es nur um eine mean-reverting Preisreihe; gesucht werden deren mittlerer Preis und deren Standardabweichung für den Mean-Reversion-Handel, nicht die Hedge Ratio zweier kointegrierender Reihen.
- Können Hedge Ratio, Mittel und Standardabweichung eines Spreads künftig variieren, sind ein gleitender Look-back oder der Kalman-Filter das genannte Mittel.
- Der erwartete Preis eines Instruments lässt sich aus dem letzten Trade, also Preis und Größe, mit dem Kalman-Filter dynamisch fortschreiben.

## Regeln und Kriterien

- Gestartet wird mit erwartetem β bei 0 und R gleich 0.
- Vw wird als (δ geteilt durch 1 minus δ) mal der 2-mal-2-Einheitsmatrix angesetzt, mit δ zwischen 0 und 1.
- δ gleich 0 hält β konstant und reduziert den Filter auf OLS mit festem Offset und fester Steigung; δ gleich 1 lässt β wild mit der letzten Beobachtung schwanken.
- Das optimale δ kommt aus Trainingsdaten; mit Wissen im Nachhinein werden δ gleich 0,0001 und Ve gleich 0,001 gesetzt.

## Risiken und Grenzen


## Beispiele

- Bei δ gleich 0,0001 schwankt die Steigung zwischen EWC und EWA um 1, und der Achsenabschnitt steigt monoton.
- Der Spread wird gekauft, wenn der Prognosefehler unter minus der Wurzel aus Q liegt, und verkauft, wenn er darüber liegt.
- Diese Kalman-Strategie auf EWA und EWC erreicht 26,2 Prozent APR und eine Sharpe Ratio von 2,4.
- Als Market-Making-Modell einer einzelnen Reihe ist der Mittelpreis verborgen und der Preis beobachtbar: y(t) gleich m(t) plus Rauschen, und m(t) gleich m(t−1) plus Rauschen.
- Statt den Filter selbst zu kodieren, verweist der Text auf freie MATLAB-Codes unter www.cs.ubc.ca/~murphyk/Software/Kalman/kalman.html und auf MATLABs Control System Toolbox.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 1–13 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-001-p001-p013|S. 1–13]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 76–95 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-006-p076-p095|S. 76–95]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 95–98 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-007-p095-p098|S. 95–98]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 571–590 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-031-p571-p590|S. 571–590]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 590–609 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-032-p590-p609|S. 590–609]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 609–628 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-033-p609-p628|S. 609–628]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 628–647 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-034-p628-p647|S. 628–647]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 647–666 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-035-p647-p666|S. 647–666]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 666–685 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-036-p666-p685|S. 666–685]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 685–704 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-037-p685-p704|S. 685–704]]

## Verwandte Themen
