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
aktualisiert: 2026-10-30
---

# Kalman-Filter


## Kurzdefinition

- Der Kalman-Filter ist ein optimaler linearer Algorithmus, der den Erwartungswert einer verborgenen Variable anhand des jüngsten Werts einer beobachtbaren Variable aktualisiert (Kleeman, 2007).
- Er schätzt Hedge Ratio und mittleren Spread, ohne ein Gewichtsschema willkürlich zu wählen (Montana, Triantafyllopoulos und Tsagaris, 2009).

## Kernaussagen


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

## Voraussetzungen


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

## Verwandte Themen
