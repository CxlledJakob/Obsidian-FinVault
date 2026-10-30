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

# Wahrscheinlichkeitsverteilung


## Kurzdefinition

- Stationär meint in diesem Schlusskapitel, dass die Wahrscheinlichkeitsverteilung der Preise über die Zeit unverändert bleibt.

## Kernaussagen

- Beim Suchen des optimalen Hebels kann in realistischen Situationen nicht mehr eine Gauß-Verteilung der Renditen angenommen werden.
- Unter der Nullhypothese wird die Verteilung der Tagesrenditen als bekannt unterstellt, mit Mittelwert null.
- Eine Möglichkeit ist die Gauß-Verteilung mit Mittelwert null und der Stichproben-Standardabweichung der Tagesrenditen. Die Teststatistik ist dann der Mittelwert geteilt durch die Standardabweichung mal der Wurzel der Datenpunktzahl. Eine hohe Sharpe Ratio macht die Verwerfung der Null leicht.
- Die Gauß-Verteilung erfasst Extremereignisse nicht. Jenseits davon stehen viele Alternativen zur Wahl, darunter die Student-t-Verteilung, die Schiefe und Kurtosis erfasst, und die Pareto-Verteilung, die auf ein endliches zweites Moment ganz verzichtet.
- Jede solche Wahl hat ein Element von Willkür und beruht auf endlich vielen Beobachtungen. Occams Rasiermesser gebietet die Gauß-Form, sofern nicht starke theoretische und empirische Gründe für eine nicht-gaußsche Verteilung sprechen.
- Ein zweiter Weg schätzt die Verteilung der Gewinne unter der Null empirisch, indem viele Preisreihen mit denselben ersten Momenten und derselben Länge simuliert und durch die Strategie geschickt werden.
- Ein dritter Weg verteilt dieselbe Zahl langer und kurzer Einstiege mit derselben durchschnittlichen Haltedauer zufällig über die echte historische Preisreihe.
- Die drei Verteilungen vergleichen die Strategie mit verschiedenen Zufallsmaßstäben und können deshalb verschiedene Antworten zur Signifikanz geben.
- Eine Nullhypothese ist nicht eindeutig, und verschiedene angenommene Verteilungen können verschiedene Schätzungen der statistischen Signifikanz liefern. Kritiker halten den Hypothesentest deshalb für fehlerhaft, nach Gill 1999.
- Gesucht ist P(H0|R), die Wahrscheinlichkeit, dass die Null wahr ist, gegeben die Teststatistik. Berechnet wird P(R|H0). Selten sind beide gleich.
- Jede zufällige Renditeverteilung mit hoher Kurtosis kann für Momentum-Strategien günstig sein.
- Alle drei Hebelmethoden unterstellen, dass die künftige Wahrscheinlichkeitsverteilung der Marktrenditen der vergangenen entspricht; das ist meist falsch und dennoch das Beste quantitativer Modelle.
- Restriktiver wird dasselbe für die Strategierenditen unterstellt, am restriktivsten eine Gauß-Verteilung.
- Die restriktivste Annahme erzeugt hier die einfachste Lösung, die Kelly-Formel.
- Ist die Gauß-Annahme eine gute Näherung und werden alle Gewinne reinvestiert, maximiert der Kelly-Hebel die zusammengesetzte Wachstumsrate.
- Nichtgaußische Renditen können denselben Hebel schon im Backtest ruinös machen.
- Stationär im Sinn des Schlusskapitels heißt, dass die Wahrscheinlichkeitsverteilung der Preise über die Zeit unverändert bleibt.
- Die statistischen Eigenschaften finanzieller Zeitreihen sind in diesem Sinn nicht stationär, deshalb bleibt subjektives Urteil nötig.
- Wissenschaft kann eigentlich nur mit stationären Statistiken umgehen.
- Dieser Sprachgebrauch unterscheidet sich von der Stationarität von Zeitreihen in Kapitel 2.

## Funktionsweise

- Wird die Gauß-Annahme durch eine andere analytische Form mit endlich vielen Momenten ersetzt, etwa Students t für Fat Tails, folgt ein anderer optimaler Hebel; die Pareto-Levy-Verteilung hat nicht endlich viele Momente.
- Für manche Verteilungen gibt es keine analytische Lösung; dann hilft Monte Carlo.
- g(f) mittelt log(1 plus f mal R) über Ziehungen aus einer Verteilung der ungehebelten Strategierendite pro Bar.
- Bei gaußischem R lässt sich g(f) analytisch reduzieren, und das Maximum reproduziert Kelly.
- Die wahre Verteilung von R ist unbekannt; das Pearson-System bildet aus Mittelwert, Standardabweichung, Schiefe und Kurtosis eine von sieben analytischen Verteilungen, darunter Gauß, Beta, Gamma und Students t.
- Das sind nicht die allgemeinsten Verteilungen; höhere Momente können fehlen oder unendlich sein.
- Im Beispiel war der Pearson-Typ 4, also keine benannte Standardverteilung, und 100.000 Ziehungen dienten der Schätzung von g(f).

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Bei Fat Tails soll die Wachstumsrate per Monte Carlo statt per Kelly optimiert werden.

## Risiken und Grenzen


## Beispiele

- Im TU-Beispiel wird die Gauß-Null mit der Teststatistik 2,93 verworfen, besser als 99 Prozent. Die momentgleiche Simulation ohne die Korrelationen verwirft die Null nur mit 88 Prozent, weil 1.166 von 10.000 Reihen mindestens die beobachtete durchschnittliche Strategierendite erreichen.
- Die kritischen Werte der standardisierten Gauß-Teststatistik sind 1,282 bei p 0,10, 1,645 bei 0,05, 2,326 bei 0,01 und 3,091 bei 0,001.
- Die Monte-Carlo-Deutung einer auf 1 Prozent signifikanten erwarteten APR von 10 Prozent benutzt 10.000 simulierte Preisreihen derselben Länge und mit denselben ersten drei Momenten wie die historische Reihe. Nur 100 davon erreichen eine APR von mindestens 10 Prozent.
- Die alternative Deutung randomisiert die Einstiegstage. Nur eine von 100 Permutationen erreicht eine APR von mindestens 10 Prozent.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]

## Verwandte Themen
