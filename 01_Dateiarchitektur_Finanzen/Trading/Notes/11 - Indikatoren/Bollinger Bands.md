---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/11 - Indikatoren/11 - Indikatoren|11 - Indikatoren]]"
weitere_hauptthemen: []
unterthema: "Kanalindikatoren"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Bollinger Bands


## Kurzdefinition

- Die Bänder liegen eine Standardabweichung über und unter dem Moving Average, der als wahrer Wert oder Mean gilt.
- Für den praktischen Handel wird eine Position erst eröffnet, wenn der Preis um mehr als entryZscore Standardabweichungen vom Mittel abweicht.
- Geschlossen wird, wenn der Preis auf exitZscore Standardabweichungen vom Mittel zurückgekehrt ist, mit exitZscore kleiner als entryZscore.

## Kernaussagen

- Die Bänder bestehen aus zwei Kanälen und einer Mittellinie, und diese Mittellinie ist ein Exponential Moving Average.
- Grundlage ist die Idee, dass der Preis zum Mean zurückkehrt.
- Oberes und unteres Band werden zu Kurszielen.
- Im Aufwärtstrend gilt die Rotation zum unteren Band als überverkauft und als Kaufgelegenheit.

## Funktionsweise

- Ein Bollinger-Band-Modell schöpft Gewinne aus einer mean-revertierenden Preisreihe, indem verkauft wird, sobald der Preis eine Schwelle überschreitet, und gekauft wird, sobald er unter eine Schwelle fällt.
- Das lineare Gegenstück kauft oder verkauft bei jedem Preisschritt, sodass der gesamte Marktwert ungefähr proportional zur negativen Abweichung vom Mittel ist. Trader nennen das Averaging-in oder Scaling-in.
- Die Preisdynamik, die das Band abschöpfen soll, ist die Ornstein-Uhlenbeck-Formel dy(t) = (λy(t−1) + μ)dt + dε. Die Preisänderung im nächsten Zeitabschnitt ist proportional zur Differenz aus Mittelpreis und aktuellem Preis.
- Long-Einstieg, wenn der Z-Score unter minus entryZscore liegt, Long-Ausstieg, wenn er mindestens minus exitZscore erreicht; Short-Einstieg oberhalb von entryZscore, Short-Ausstieg bei höchstens exitZscore.
- Die Long-Stückzahl wird am Einstieg auf 1 und am Ausstieg auf 0 gesetzt, die Short-Stückzahl auf minus 1 beziehungsweise 0, und an Tagen ohne Signal wird der Vortageswert fortgeschrieben; die Nettostückzahl ist die Summe beider Seiten.
- Die lineare Strategie skaliert die Stückzahl fortlaufend mit der Abweichung und ist damit der Grenzfall ohne festes Band; sie ist fast parameterfrei und deshalb am wenigsten anfällig für Data Snooping, aber unpraktisch, weil die maximale Kapitalbindung unbekannt ist.
- Eine Bollinger-Band-ähnliche Mean-Reversion-Strategie shortet das Portfolio aus 0,3906 VX und einem ES, sobald dessen Wert um eine Standardabweichung der im Trainingsset bestimmten Residuen abweicht.
- Beim Bollinger Band hängt die Lage der Bänder von der jüngeren Volatilität der Zeitreihe ab; Bänder können stattdessen auch ein fester Prozentsatz über und unter dem gleitenden Durchschnitt sein.
- In der Bandregel setzt das Aufwärtsdurchstoßen des oberen Bandes die Ausgabe auf +1, und dieser Wert bleibt, bis das untere Band nach unten durchstoßen wird und die Ausgabe auf −1 wechselt.

## Voraussetzungen


## Anwendung im Trading

- Auf dem Testset vom 29. Juli 2010 bis zum 8. Mai 2012 beträgt die annualisierte Rendite dieser Strategie 12,3 Prozent bei einer Sharpe Ratio von 1,4.
- Besonders profitabel war sie um die Herabstufung der US-Bonität durch Standard & Poor's.
- Die Standardabweichung der Residuen aus dem Trainingsset beträgt 2.047 Dollar; das Trainingsset sind die ersten 500 Tage nach August 2008.

## Regeln und Kriterien

- entryZscore ist ein freier Parameter und wird auf einem Trainingsset optimiert; Mittel und Standardabweichung werden über einen Lookback gerechnet, der ebenfalls optimiert oder gleich der Halbwertszeit gesetzt werden kann.
- Ist exitZscore gleich 0, wird am aktuellen Mittel geschlossen.
- Ist exitZscore gleich minus entryZscore, wird geschlossen, wenn der Preis das gegenüberliegende Band so weit durchstößt, dass ein Signal mit umgekehrtem Vorzeichen entsteht.
- Zu jedem Zeitpunkt ist entweder null oder eine Einheit long oder short investiert, deshalb sind Kapitalzuteilung und Risikosteuerung einfach.
- Ein kurzer Lookback und kleine Beträge von entryZscore und exitZscore geben eine kürzere Haltedauer, mehr Round-Trips und in der Regel höhere Gewinne.
- Scaling-in mit mehreren Bändern benutzt entryZscore gleich 1, 2, 3 bis N und exitZscore gleich 0, 1, 2 bis N minus 1; N wird auf Trainingsdaten optimiert.

## Risiken und Grenzen

- Der gleitende Durchschnitt beruht nur auf dem Preis und zeichnet die Wanderung des Means unvollständig.
- Zeit, Preis und Volumen im Marktprofil zeigen die Wanderung des Means vollständiger.
- Schoenberg und Corwin (2010) zeigen, dass Ein- oder Ausstieg an zwei oder mehr Bollinger-Bändern nie optimal ist: es gibt immer ein einzelnes Niveau, von ihnen all-in genannt, mit höherer durchschnittlicher Rendite im Backtest.
- Der Beweis nimmt an, dass die Wahrscheinlichkeit p, vor der Rückkehr zum Endpreis noch weiter abzuweichen, über die Zeit konstant ist.
- Ist die Volatilität nicht konstant, ist auch p nicht konstant, und Scaling-in liefert dann voraussichtlich eine bessere realisierte Sharpe Ratio, wenn schon nicht mehr Gewinn.
- Scaling-in ist in der Stichprobe nie optimal, kann die All-in-Methode außer Stichprobe aber übertreffen.

## Beispiele

- Auf dem Preis-Spread von GLD und USO mit entryZscore gleich 1 und exitZscore gleich 0 erreicht die Bollinger-Strategie 17,8 Prozent APR und eine Sharpe Ratio von 0,96 und verbessert damit die lineare Variante.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Markets in Profile_ Profiting from the Auction Process.pdf, S. 120–139 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-010-p120-p139|S. 120–139]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 20–39 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-002-p020-p039|S. 20–39]]

## Verwandte Themen
