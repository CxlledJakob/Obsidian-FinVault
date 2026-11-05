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
aktualisiert: 2026-11-05
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
- Ein stochastisches Volatilitätsmodell wird per Quasi-Likelihood über Kalman-Filterung oder per Monte-Carlo-Methode geschätzt.
- Jacquier, Polson und Rossi (1994) vergleichen die Schätzergebnisse von Quasi-Likelihood und Markov-Chain-Monte-Carlo für stochastische Volatilitätsmodelle.
- Das Zustandsraummodell vereinfacht die Maximum-Likelihood-Schätzung und den Umgang mit fehlenden Werten. Es hängt mit dem ARIMA-Modell zusammen. Anwendungen in diesem Kapitel sind realisierte Volatilität, Marktmodelle mit zeitvariablen Koeffizienten und vierteljährliche Gewinne je Aktie.
- Das lokale Trendmodell ist yt gleich μt plus et, et normal mit Mittel null und Varianz σ²e, und μt plus 1 gleich μt plus ηt, ηt normal mit Mittel null und Varianz σ²η. Die beiden weißen Rauschen sind unabhängig, der Start μ1 ist vorgegeben oder hat eine bekannte Verteilung und ist für t größer 0 von beiden unabhängig.
- μt ist der nicht direkt beobachtete Zustand, Gleichung (11.1) die Beobachtungsgleichung mit Messfehler et, Gleichung (11.2) die Zustandsgleichung mit Innovation ηt. Durbin und Koopman (2001) nennen es Local-Level-Modell, einen einfachen Fall des strukturellen Zeitreihenmodells von Harvey (1993).
- Filtern heißt, μt aus Ft zu rekonstruieren und die Messfehler zu entfernen. Prognose heißt, μt plus h oder yt plus h für h größer 0 aus Ft vorherzusagen. Glätten heißt, μt aus FT zu schätzen, wobei T größer t ist.
- Der Kalman-Gewinn Kt gleich Σt|t minus 1 geteilt durch Vt ist der Regressionskoeffizient von μt auf den neuen Schock vt und steuert, wie stark vt den Zustand verändert.
- Das Update ist μt|t gleich μt|t minus 1 plus Kt mal vt, und Σt|t gleich Σt|t minus 1 mal (1 minus Kt). Die Prognose ist μt plus 1 gegeben t gleich μt|t, und Σt plus 1 gegeben t gleich Σt|t plus σ²η.
- Die Rekursion für t von 1 bis T lautet: vt gleich yt minus μt|t minus 1, Vt gleich Σt|t minus 1 plus σ²e, Kt gleich Σt|t minus 1 geteilt durch Vt, μt plus 1 gegeben t gleich μt|t minus 1 plus Kt mal vt, Σt plus 1 gegeben t gleich Σt|t minus 1 mal (1 minus Kt) plus σ²η. Der Start ist μ1 verteilt als normal mit Mittel μ1|0 und Varianz Σ1|0. Der Algorithmus stammt von Kalman (1960).
- Für das lokale Trendmodell werden σe und ση per Maximum Likelihood geschätzt. Der Filter wertet dabei die Likelihood der Daten aus. Die Wahl der Startwerte Σ1|0 und μ1|0 braucht eigene Aufmerksamkeit.
- Für die logarithmierte realisierte Tagesvolatilität von Alcoa sind die Maximum-Likelihood-Schätzungen ση-Dach gleich 0,0735 und σe-Dach gleich 0,4803. Die Messfehler haben die größere Varianz.
- Satz 11.1 setzt gemeinsame multivariate Normalität und nichtsinguläre Blockkovarianzen voraus. Dann ist E(x|y) gleich μx plus Σxy Σyy hoch minus 1 mal (y minus μy), und Var(x|y) gleich Σxx minus Σxy Σyy hoch minus 1 mal Σyx.
- Ist Σyz gleich 0, dann ist E(x|y, z) gleich E(x|y) plus Σxz Σzz hoch minus 1 mal (z minus μz), und Var(x|y, z) gleich Var(x|y) minus Σxz Σzz hoch minus 1 mal Σzx.
- Der Ein-Schritt-Fehler vt gleich yt minus μt|t minus 1 hat Varianz Σt|t minus 1 plus σ²e, Erwartungswert null und Kovarianz null mit yj für j kleiner t. Die Information Ft lässt sich als Ft minus 1 zusammen mit vt schreiben.
- Bedingt auf Ft minus 1 sind μt und vt gemeinsam normal, mit Mittel (μt|t minus 1, 0) und mit Σt|t minus 1 auf den drei Positionen der ersten Zeile und Spalte der Kovarianz sowie Vt rechts unten. Die bedingte Kovarianz von μt und vt ist Σt|t minus 1.
- Auf die logarithmierte realisierte Tagesvolatilität von Alcoa wird der Filter mit Σ1|0 unendlich und μ1|0 gleich 0 angewendet. Die gefilterten Zustände sind glatter als die Reihe. Die Ein-Schritt-Fehler sind außer Stichprobe, stabil und um null zentriert.
- Unter Normalität sind die Ein-Schritt-Fehler vt gegenseitig unabhängig. Der Filter liefert die Cholesky-Zerlegung der Kovarianz von y: K mal Cov(y) mal K′ gleich der Diagonalmatrix aus V1 bis VT.
- Der Kalman-Gewinn hängt nicht von μ1|0 und nicht von den Daten ab, sondern von Σ1|0, σ²e und σ²η.
- Der Zustandsprognosefehler xt gleich μt minus μt|t minus 1 erfüllt vt gleich xt plus et und xt plus 1 gleich Lt xt plus ηt minus Kt et, mit Lt gleich 1 minus Kt gleich σ²e geteilt durch Vt.
- Die Glättung läuft rückwärts: qt minus 1 gleich vt geteilt durch Vt plus Lt mal qt, und μt|T gleich μt|t minus 1 plus Σt|t minus 1 mal qt minus 1, mit Start qT gleich 0.
- Die geglättete Varianz folgt aus Mt minus 1 gleich 1 geteilt durch Vt plus Lt zum Quadrat mal Mt und Σt|T gleich Σt|t minus 1 minus (Σt|t minus 1) zum Quadrat mal Mt minus 1, mit MT gleich 0. Es gilt Var(qt minus 1) gleich Mt minus 1.
- Die geglätteten Zustände der Alcoa-Reihe sind glatter als die gefilterten, und ihre 95-Prozent-Intervalle sind schmaler. Die Breite des 95-Prozent-Intervalls von μ1|1 hängt von Σ1|0 ab.
- Fehlen die Beobachtungen von ℓ plus 1 bis ℓ plus h, läuft der Filter mit vt gleich 0 und Kt gleich 0 weiter. Es gibt dann keine neue Innovation und keinen neuen Gewinn. Die Zustandsprognosevarianz wächst je fehlendem Schritt um σ²η.
- Diffuse Initialisierung: geht Σ1|0 gegen unendlich, werden μ2|1 gleich y1 und Σ2|1 gleich σ²e plus σ²η. Das entspricht einem festen y1 und μ1 normal mit Mittel y1 und Varianz σ²e. Ein sehr großes Σ1|0 bedeutet Unsicherheit über den Start.
- Die diffuse Initialisierung lässt die Glättung für t von T bis 2 unberührt. Für t gleich 1 gilt im Grenzwert μ1|T gleich y1 plus σ²e mal q1 und Σ1|T gleich σ²e minus σ⁴e mal M1.
- Ist über μ1 wenig bekannt, wird die diffuse Initialisierung empfohlen. Eine unendliche Varianz ist in Anwendungen schwer zu rechtfertigen. Alternativ wird μ1 als zusätzlicher Parameter gemeinsam geschätzt, verwandt mit der exakten Maximum Likelihood der Kapitel 2 und 8.
- Die Log-Likelihood unter Normalität ist minus T/2 mal ln(2π) minus 1/2 mal der Summe von ln(Vt) plus v²t geteilt durch Vt. Sie wird rekursiv über den Filter ausgewertet, auch bei fehlenden Werten.
- Für Alcoa liefert die Maximum Likelihood ση gleich 0,07350827 und σe gleich 0,48026284. Die zugehörigen Varianzen sind 0,0054035 und 0,2306524. In S-Plus bedeutet P1 gleich minus 1 die diffuse Initialisierung, a1 gleich 0.
- Die standardisierten Fehler vt geteilt durch die Wurzel von Vt haben Q(25) gleich 23,37 bei einem p-Wert von 0,56 und eine ARCH-LM-Statistik von 18,48 bei einem p-Wert von 0,82 über 25 Lags. Das lokale Trendmodell ist danach angemessen.
- Das allgemeine lineare gaußsche Zustandsraummodell ist st plus 1 gleich dt plus Tt st plus Rt ηt und yt gleich ct plus Zt st plus et, mit ηt normal mit Kovarianz Qt und et normal mit Kovarianz Ht. Qt und Ht sind positiv definit, et und ηt sind unabhängig. Die Zustandsgleichung ist eine Markov-Kette erster Ordnung.
- Die Systemmatrizen Tt, Rt, Qt, Zt und Ht sind bekannt, oft dünn besetzt und können von einem per Maximum Likelihood geschätzten Parameter θ abhängen. Sie dürfen zeitlich variieren.
- Die diffuse Initialisierung im allgemeinen Modell setzt Σ1|0 gleich Σ-Stern plus λ mal Σ-unendlich, mit großem λ, das gegen unendlich gehen kann. Der Startzustand ist für t größer 0 unabhängig von et und ηt.
- Für das allgemeine Modell liefert der Filter rekursiv die bedingte Verteilung von st plus 1 gegeben Ft. Weil diese Verteilung normal ist, genügen bedingter Mittelwert und Kovarianz.
- Die Zustandsprognose ist st plus 1 gegeben t gleich dt plus Tt mal st|t, und ihre Kovarianz ist Tt mal Σt|t mal Tt′ plus Rt Qt Rt′.
- Der Ein-Schritt-Fehler ist vt gleich yt minus ct minus Zt mal st|t minus 1. Er hat bedingt auf Ft minus 1 den Erwartungswert null, ist von Ft minus 1 unabhängig, und die Folge vt besteht aus unabhängigen normalen Vektoren.
- Vt gleich Zt mal Σt|t minus 1 mal Zt′ plus Ht. Das Update ist st|t gleich st|t minus 1 plus Ct mal Vt hoch minus 1 mal vt, mit Ct gleich Σt|t minus 1 mal Zt′. Der Kalman-Gewinn ist Kt gleich Tt mal Σt|t minus 1 mal Zt′ mal Vt hoch minus 1.
- Die gefilterte Kovarianz ist Σt|t gleich Σt|t minus 1 minus Ct Vt hoch minus 1 Ct′. Mit Lt gleich Tt minus Kt Zt gilt Σt plus 1 gegeben t gleich Tt mal Σt|t minus 1 mal Lt′ plus Rt Qt Rt′.
- Sind alle Systemmatrizen zeitlich konstant, konvergiert Σt|t minus 1 gegen eine Steady-State-Matrix Σ-Stern, die Σ-Stern gleich T Σ-Stern T′ minus T Σ-Stern Z V hoch minus 1 Z Σ-Stern T′ plus R Q R′ erfüllt, mit V gleich Z Σ-Stern Z′ plus H. Danach sind Vt, Kt und die Zustandsprognosekovarianz konstant.
- Der Zustandsprognosefehler xt gleich st minus st|t minus 1 hat Kovarianz Σt|t minus 1. Es gilt vt gleich Zt xt plus et und xt plus 1 gleich Lt xt plus Rt ηt minus Kt et.
- Der Fixed-Interval-Smoother nach de Jong (1989) ist qt minus 1 gleich Zt′ Vt hoch minus 1 vt plus Lt′ qt und st|T gleich st|t minus 1 plus Σt|t minus 1 mal qt minus 1, mit Start qT gleich 0.
- Die geglättete Kovarianz ist Σt|T gleich Σt|t minus 1 minus Σt|t minus 1 mal Mt minus 1 mal Σt|t minus 1, mit Mt minus 1 gleich Zt′ Vt hoch minus 1 Zt plus Lt′ Mt Lt und MT gleich 0. Mt ist die Varianz von qt.
- Praktisch wird erst für t von 1 bis T gefiltert und vt, Vt, Kt, st|t minus 1 und Σt|t minus 1 werden gespeichert. Danach läuft die Glättung für t von T bis 1.
- Die geglätteten Störungen sind et|T gleich Ht mal (Vt hoch minus 1 vt minus Kt′ qt) und ηt|T gleich Qt Rt′ qt. Die Größe ot gleich Vt hoch minus 1 vt minus Kt′ qt heißt Glättungs-Messfehler.
- Die Kovarianz der geglätteten Messstörung ist Ht minus Ht mal (Vt hoch minus 1 plus Kt′ Mt Kt) mal Ht. Die der geglätteten Zustandsinnovation ist Qt minus Qt Rt′ Mt Rt Qt.
- Koopman (1993) rekonstruiert den geglätteten Zustand vorwärts: st plus 1 gegeben T gleich dt plus Tt mal st|T plus Rt Qt Rt′ qt, Start s1|T gleich s1|0 plus Σ1|0 q0.
- Fehlt die ganze Beobachtung, setzt man vt gleich 0 und Kt gleich 0. Dann ist st plus 1 gegeben t gleich dt plus Tt mal st|t minus 1, und die Kovarianz ist Tt mal Σt|t minus 1 mal Tt′ plus Rt Qt Rt′. In der Glättung wird qt minus 1 gleich Tt′ qt und Mt minus 1 gleich Tt′ Mt Tt.
- Fehlen nur Komponenten, ist y-Stern t gleich J yt mit einer Auswahlmatrix J aus Zeilen der Einheitsmatrix. Die Beobachtungsgleichung verwendet dann c-Stern gleich J ct, Z-Stern gleich J Zt und H-Stern gleich J Ht J′.
- Die Prognose minimalen mittleren quadratischen Fehlers ist yt(j) gleich E(yt plus j | Ft) gleich ct plus j plus Zt plus j mal st plus j gegeben t. Man erhält sie, indem die künftigen Werte yt plus 1 bis yt plus h wie fehlende Beobachtungen behandelt werden.
- Die Kovarianz des j-Schritt-Prognosefehlers ist Zt plus j mal Σt plus j gegeben t mal Zt plus j′ plus Ht plus j. Für j gleich 1 ist das genau Vt plus 1. Der Zustand wird fortgeschrieben als st plus j plus 1 gegeben t gleich dt plus j plus Tt plus j mal st plus j gegeben t.
- Fehlende Werte einer Zeitreihe lassen sich mit dem Kalman-Filter oder mit MCMC behandeln; genannt werden Jones (1980), Kapitel 11 sowie McCulloch und Tsay (1994a).
- Der Kleinste-Quadrate-Schätzer eines als fehlend behandelten ln ht in der AR(1)-Volatilitätsgleichung stimmt mit dem bedingten Mittel aus Gleichung (12.23) überein und ist normal mit Varianz σ²v / (1 + α1²).
- Startwerte von ht lassen sich durch Anpassen eines Volatilitätsmodells aus Kapitel 3 gewinnen.
- Die Quadrattransformation in Gleichung (12.42) behält eine vorhandene Korrelation zwischen ηt und εt nicht; das genäherte Zustandsraummodell (12.43) und (12.44) kann den Leverage-Effekt deshalb nicht schätzen.
- Nach dem Einsetzen des Leverage-Effekts ist die Übergangsgleichung für zt nichtlinear, und der Kalman-Filter aus Gleichung (12.45) ist nicht mehr anwendbar.

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
- Prognosen und die Kovarianzmatrizen der Prognosefehler lassen sich mit dem Kalman-Filter aus Gleichung (11.64) gewinnen, indem {yt+1, …, yt+h} als fehlende Werte behandelt werden.
- Der Ein-Schritt-Prognosefehler ist et(1) = yt+1 − yt(1) = Zt+1(st+1 − st+1|t) + et+1, und seine Kovarianz Var[et(1)] = Zt+1 Σt+1|t Z′t+1 + Ht+1 ist genau die Matrix Vt+1 des Kalman-Filters.
- Für j Schritte gilt yt(j) = ct+j + Zt+j st+j|t und Var[et(j)] = Zt+j Σt+j|t Z′t+j + Ht+j.
- Die Zustandsprognose ist st+j+1|t = dt+j + Tt+j st+j|t, und der Fehler erfüllt st+j+1 − st+j+1|t = Tt+j(st+j − st+j|t) + Rt+j ηt+j.
- Die Kovarianzrekursion lautet Σt+j+1|t = Tt+j Σt+j|t T′t+j + Rt+j Qt+j R′t+j.
- Bei fehlenden Werten läuft die Rekursion mit vt+j = 0 und Kt+j = 0; Var[et(j)] ist dann gleich Vt+j.
- Die Prognosefehlerreihe {vt} dient der Likelihood, die standardisierten Fehler Dt hoch −1/2 mal vt der Modellprüfung, mit Dt = diag{Vt(1,1), …, Vt(k,k)}.
- Forward Filtering and Backward Sampling im Kalman-Filter zieht den Volatilitätsprozess gemeinsam und kann die Rechenzeit stark senken; genannt werden Carter und Kohn (1994) sowie Frühwirth-Schnatter (1994).
- Für das Gauß-Zustandsraummodell ohne Leverage gilt vt = yt − ct − zt|t−1, Vt = Σt|t−1 + Ht, zt|t = zt|t−1 + Σt|t−1 Vt hoch −1 vt, Σt|t = Σt|t−1 − Σt|t−1 Vt hoch −1 Σt|t−1, zt+1|t = α zt|t und Σt+1|t = α² Σt|t + σ²η.
- Wegen der Markov-Eigenschaft faktorisiert die gemeinsame Posterior von z in p(zn|Fn) mal die aufeinanderfolgenden bedingten Verteilungen p(zt | zt+1, Ft).
- p(zn|Fn) ist normal mit Mittel zn|n und Varianz Σn|n; p(zt | zt+1, Ft) ist normal mit Mittel zt|t + α Σt|t Σt+1|t hoch −1 (zt+1 − zt+1|t) und Varianz Σt|t − α² Σt|t² Σt+1|t hoch −1.
- Die gemeinsame Verteilung von (zt, zt+1) gegeben Ft ist bivariat normal mit den aus dem Filter bekannten Mitteln und der Kovarianzmatrix, deren Nebendiagonale α Σt|t ist.
- Mit Startwerten z1|0 und Σ1|0 läuft der Filter vorwärts durch die Daten, danach die rekursive Rückwärtsziehung; das Verfahren gilt für allgemeine lineare Gauß-Zustandsraummodelle.
- Weil ε*t = ln(ε²t) nicht normal ist, nähern Kim, Shephard und Chib (1998) die Verteilung durch eine Mischung aus sieben Normalverteilungen an, damit ein Gauß-Zustandsraummodell entsteht.
- Bei ρ ungleich 0 schlagen Artigas und Tsay (2004) ein zeitvariables Zustandsraummodell vor; der gewöhnliche Filter gilt nicht mehr, und die letzten beiden Filtergleichungen werden zu zt+1|t = G(zt|t) und Σt+1|t = g(zt|t)² Σt|t + σ²η(1 − ρ²), mit g als Ableitung von G an zt|t.
- Artigas und Tsay (2004) setzen bei ρ ≠ 0 ηt = ρ ση εt + η*t, wobei η*t normal, unabhängig von εt und mit Varianz σ²η(1 − ρ²) ist; mit εt = (rt − x't β) exp(−zt/2) / σ0 wird zt+1 = G(zt) + η*t und G(zt) = α zt + ρ ση (rt − x't β) exp(−zt/2) / σ0.
- Als Näherung dient ein zeitvariabler linearer Kalman-Filter: zt+1|t = G(zt|t), und die fortgeschriebene Zustandsvarianz ist g(zt|t)² mal der Varianz zum geglätteten Zustand plus σ²η(1 − ρ²); g ist die erste Ableitung von G, ausgewertet am geglätteten Zustand zt|t.

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

- Die geschätzten Komponenten sind nicht eindeutig und hängen vom Modell und von den Nebenbedingungen ab; es gibt unendlich viele Zerlegungen einer Reihe in unbeobachtete Komponenten.
- Eine andere Saisonspezifikation, etwa seasonalTrig in SsfPack, liefert eine andere Zerlegung derselben Johnson-&-Johnson-Reihe.
- Für die Prognose ist die Wahl der Zerlegung unerheblich, sofern die gewählte Zerlegung gültig ist; bei der Interpretation der Komponenten ist Vorsicht nötig.

## Beispiele

- Bei δ gleich 0,0001 schwankt die Steigung zwischen EWC und EWA um 1, und der Achsenabschnitt steigt monoton.
- Der Spread wird gekauft, wenn der Prognosefehler unter minus der Wurzel aus Q liegt, und verkauft, wenn er darüber liegt.
- Diese Kalman-Strategie auf EWA und EWC erreicht 26,2 Prozent APR und eine Sharpe Ratio von 2,4.
- Als Market-Making-Modell einer einzelnen Reihe ist der Mittelpreis verborgen und der Preis beobachtbar: y(t) gleich m(t) plus Rauschen, und m(t) gleich m(t−1) plus Rauschen.
- Statt den Filter selbst zu kodieren, verweist der Text auf freie MATLAB-Codes unter www.cs.ubc.ca/~murphyk/Software/Kalman/kalman.html und auf MATLABs Control System Toolbox.
- Das feste Marktmodell ist ein Spezialfall des Zustandsraummodells; SsfPack und OLS stimmen für die GM-Überschussrenditen überein, mit Zuständen 0,1982025 und 1,045702.
- Im zeitvariablen CAPM liegen ση und σε bei 4,91 × 10 hoch −5 und 1,22 × 10 hoch −2, also nahe null, und αt sowie βt sind für GM im Wesentlichen konstant.
- Für die logarithmierten Quartalsgewinne je Aktie von Johnson & Johnson, 1960 bis 1980, lautet das Komponentenmodell yt = µt + γt + et mit et ∼ N(0, σ²e), lokalem Trend µt+1 = µt + ηt und Saison (1 + B + B² + B³)γt = ωt.
- Die Maximum-Likelihood-Schätzungen sind (σ̂e, σ̂η, σ̂ω) = (2,044516 × 10 hoch −6, 7,269655 × 10 hoch −2, 2,931691 × 10 hoch −2).
- Die geglätteten Komponenten sind µt|T und γt|T mit T = 84; das saisonale Muster verändert sich über die Zeit, und die Abbildungen zeigen punktweise 95-Prozent-Bereiche.
- KalmanFil liefert die Ein-Schritt-Prognosefehler, KalmanSmo die geglätteten Residuen der Beobachtungsgleichung.

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
