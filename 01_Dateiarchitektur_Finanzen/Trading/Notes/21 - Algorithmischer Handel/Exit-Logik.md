---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Systementwicklung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-01
---

# Exit-Logik


## Kurzdefinition

- Die Triple-Barrier-Methode bestimmt den Ausstieg danach, welche von drei Barrieren zuerst berührt wird.
- Die Standard-Handelsregel bestimmt, wann eine bereits eröffnete Gelegenheit verlassen wird.
- Viele Strategien halten eine Position, bis ein Gewinnziel oder ein Stop-Loss erreicht ist.

## Kernaussagen

- Zwei horizontale Barrieren setzen Gewinnmitnahme und Stop-Loss als dynamische Funktion der geschätzten Volatilität.
- Die dritte Barriere ist vertikal und begrenzt die Haltedauer in der Zahl der Bars seit Positionsaufnahme.
- Wird die obere Barriere zuerst berührt, ist das Label 1.
- Wird die untere Barriere zuerst berührt, ist das Label -1.
- Wird die vertikale Barriere zuerst berührt, kann das Label das Vorzeichen der Rendite oder 0 sein.
- Der Autor bevorzugt das Vorzeichen, weil damit ein Gewinn oder Verlust innerhalb der Grenzen realisiert wird.
- Ob 0 besser passt, ist am jeweiligen Problem zu prüfen.
- Das Label ist pfadabhängig und erfordert den gesamten Kursverlauf von ti,0 bis ti,0 plus h.
- ti,1 ist der Zeitpunkt der ersten Berührung und liegt nicht nach ti,0 plus h.
- Die horizontalen Barrieren sind nicht notwendig symmetrisch.
- Jede der drei Barrieren kann abgeschaltet werden: In der Konfiguration [pt, sl, t1] bedeutet 0 inaktiv und 1 aktiv.
- Wer erkennt, dass eine schon bestehende Position einen Verlust erwartet, braucht eine Ausstiegsregel, die diesen Verlust klein hält.
- Ein rationaler Marktteilnehmer eröffnet keine Position unter der Annahme, dass ein Verlust das erwartete Ergebnis ist.
- Die abgeleitete Ausstiegsregel ist die Kombination aus Gewinnziel und Stop, die zum Preisprozess gehört.
- Die Kombination aus Gewinnziel und Stop wird aus den Eigenschaften des Preisprozesses bestimmt.
- Auch ohne ausdrücklich gesetzten Stop gibt es eine implizite Grenze, an der die Position nicht mehr finanziert werden kann oder der Buchverlust nicht mehr tragbar ist.
- Die implizite Stop-Grenze ist ein Margin Call oder die Schmerzgrenze eines steigenden Buchverlusts.
- Weil die meisten Strategien ein Gewinnziel und einen Stop-Loss haben, werden die Ergebnisse als binomialer Prozess modelliert.
- Der Portfoliomanager setzt Verlustschwelle, Gewinnschwelle und jährliche Wettfrequenz und gibt die Ausstiege mit den Aufträgen an die Händler.
- Die Trefferwahrscheinlichkeit bestimmt der Markt, und die Ziel-Sharpe-Ratio bestimmt der Investor.
- Man braucht keine echte Stationarität: kurzfristige oder saisonale Mean Reversion lässt sich mitnehmen, wenn die Position geschlossen wird, bevor der Preis das nächste Gleichgewicht erreicht.
- Saisonale Mean Reversion heißt, dass die Reihe nur in bestimmten Tagesabschnitten oder unter bestimmten Bedingungen zum Mittel zurückkehrt.
- Für Momentum-Strategien gibt es zwei übliche Ausstiegsarten, den zeitbasierten Ausstieg und den Stop-Loss.
- Alle bisher besprochenen Momentum-Strategien verwenden nur zeitbasierte Ausstiege: eine Haltedauer wird festgelegt, und bei ihrem Erreichen wird die Position geschlossen.
- Ein Stop-Loss kann die Ausstiegsbedingung oder eine zusätzliche Ausstiegsbedingung sein.
- Stop-Losses sind mit Momentum-Strategien verträglich und mit Mean-Reversion-Strategien nicht, weil sie deren Einstiegssignalen widersprechen; das wird in Kapitel 8 wieder aufgenommen.
- Durch zeitbasierten Ausstieg oder Stop-Loss ist der Verlust einer Momentum-Position immer begrenzt.
- Eine willkürlich gesetzte Gewinnobergrenze bei Momentum ist unratsam, weil das Aufwärtspotenzial sonst unbegrenzt ist.
- Die zwei üblichen Ausstiege von Momentum-Strategien sind zeitbasiert und Stop-Loss.
- Alle bisher besprochenen Momentum-Strategien nutzen nur den zeitbasierten Ausstieg: eine Haltedauer wird festgelegt, und bei ihrem Erreichen wird geschlossen.
- Ein Stop-Loss kann die Ausstiegsbedingung sein oder zusätzlich zur Haltedauer gelten.
- Stop-Losses passen zu Momentum: dreht das Momentum, wird die Gegenposition eröffnet, und weil die alte Position verloren hätte, wirkt dieser Ausstieg als Stop.
- Stop-Losses passen nicht zu Mean Reversion, weil sie den Einstiegssignalen widersprechen; das wird in Kapitel 8 wieder aufgenommen.
- Der kumulierte Verlust aufeinanderfolgender Verlustpositionen einer Momentum-Strategie kann trotzdem ruinös sein.
- Eine willkürliche Gewinnobergrenze ist unratsam, weil das Aufwärtspotenzial von Momentum sonst unbegrenzt ist.
- Die Opening-Gap-Strategie hält vom Open bis zum Close desselben Tages; die Rendite ist die Position mal (Open minus Close) geteilt durch Open.
- Die PEAD-Strategie wird am Schluss desselben Tages geschlossen. Ob eine noch kürzere Haltedauer bessere Renditen bringt, bleibt zu testen.
- Die DRN-Strategie steigt am Handelsschluss aus.
- Beim Ratio Trade wird verkauft, sobald der Bid um einen oder mehrere Ticks steigt, oder eine Verkaufsorder auf den Best Ask gelegt, wenn der Spread die Round-Trip-Kommission übersteigt; sonst Verkauf zum ursprünglichen Best Bid.
- Beim Ticking wird zum Best Ask minus einem Tick verkauft; scheitert die Füllung, Verkauf zum ursprünglichen Best Bid mit Verlust der Kommissionen plus einem Tick.
- Stop Hunting deckt die Short-Position, sobald die Sell-Stops ausgelöst sind und das Abwärtsmomentum läuft.

## Funktionsweise

- applyPtSlOnT1 prüft auf dem mit der Positionsseite multiplizierten Renditepfad, ob Stop-Loss oder Gewinnmitnahme vor der vertikalen Schranke eintreten.
- Die Funktion liefert die Zeitstempel, an denen die einzelnen Barrieren berührt wurden.
- Der Ausstiegszeitpunkt ist der früheste dieser Zeitstempel.
- getBins setzt die realisierte Rendite auf diesen ersten Kontakt und das Label auf das Vorzeichen dieser Rendite.
- Der Ausstieg erfolgt, sobald der Mark-to-Market-Gewinn die positive Gewinnschwelle erreicht oder die negative Stop-Schwelle erreicht.
- Weil die Stop-Schwelle unter der Gewinnschwelle liegt, kann nur eine der beiden Bedingungen den Ausstieg auslösen.
- Der endgültige Gewinn der Gelegenheit ist ihr Mark-to-Market-Ergebnis zum Ausstiegszeitpunkt.
- Der Mark-to-Market-Gewinn nach t Transaktionen ist die Positionsgröße mal der Differenz aus dem dann beobachteten Preis und dem Einstiegspreis.
- Scaling-in skaliert auch schrittweise aus: der Gewinn muss nicht bis zur vollen Rückkehr zum Mittel warten.
- Schon kleine Rückläufe lassen sich realisieren, sodass die Strategie auch profitabel bleiben kann, wenn die Reihe nicht wirklich stationär ist und nie zum Mittel zurückkehrt.
- In der Modellrechnung von Schoenberg und Corwin werden alle Kontrakte erst bei F geschlossen, also ohne average-out, selbst wenn mit average-in eingestiegen wurde.

## Voraussetzungen


## Anwendung im Trading

- Untersucht wird der Ausstiegskorridor einer Position, die bereits besteht, also die Lage eines Ausführungshändlers.
- Die Bestimmung der Ein- und Ausstiegsschwellen für die Anlageentscheidung selbst behandelt zum Beispiel Bertram 2009.
- Das Modell zeigt, welche Kombinationen aus Frequenz, Trefferwahrscheinlichkeit und Auszahlung unwirtschaftlich sind.

## Regeln und Kriterien

- Die Konfiguration [1,1,1] ist der Standard: Gewinn realisieren, eine maximale Verlusttoleranz und eine maximale Haltedauer.
- Bei [0,1,1] endet die Position nach einer Anzahl Bars, sofern sie nicht vorher ausgestoppt wird.
- Bei [1,1,0] wird Gewinn mitgenommen, solange kein Stop greift, und die Position darf beliebig lange gehalten werden.
- Die Konfiguration [0,0,1] entspricht der Fixed-Time-Horizon-Methode.
- Bei [1,0,1] läuft die Position bis zu einem Gewinn oder bis zum Ende der maximalen Haltedauer, ohne Rücksicht auf zwischenzeitliche Buchverluste.
- Bei [1,0,0] wird gehalten, bis ein Gewinn entsteht, und die Position kann jahrelang im Verlust gebunden bleiben.
- Die Konfiguration [0,1,0] hält nur bis zum Stop und gilt als ziellos.
- Bei [0,0,0] gibt es keine Barrieren, die Position bleibt auf Dauer gesperrt, und es entsteht kein Label.
- Der Bollinger-Ausstieg liegt bei exitZscore Standardabweichungen vom Mittel, mit exitZscore kleiner als entryZscore.
- exitZscore gleich 0 bedeutet den Ausstieg am aktuellen Mittel.
- exitZscore gleich minus entryZscore bedeutet den Ausstieg erst jenseits des gegenüberliegenden Bands, sodass dort ein Signal mit umgekehrtem Vorzeichen entsteht.
- Im GLD-USO-Beispiel mit exitZscore gleich 0 wird die Long-Position geschlossen, sobald der Z-Score mindestens minus exitZscore ist, und die Short-Position, sobald er höchstens exitZscore ist.
- Mehrere Ausstiege zum Scaling-in liegen bei exitZscore gleich 0, 1, 2 bis N minus 1, passend zu den Einstiegen 1, 2, 3 bis N.
- Beim Kalman-Beispiel wird die Long-Position geschlossen, sobald der Prognosefehler e größer als minus der Wurzel aus Q ist, und die Short-Position, sobald e kleiner als die Wurzel aus Q ist.
- Im Buy-on-Gap werden alle Positionen zum Marktschluss liquidiert.
- In der Intraday-Variante des linearen Long-Short werden alle Positionen zum Marktschluss liquidiert.
- Eine genannte Variante setzt Intraday-Gewinnobergrenzen.
- Für GLD gegen GDX soll zumindest eine Regel den Handel beenden, sobald der Ölpreis eine bestimmte Schwelle überschreitet.
- Bei einem einzelnen Aktienpaar setzt konsistente Profitabilität voraus, dass man jedes Unternehmen fundamental versteht und die Position verlässt, bevor schlechte Nachrichten eines der beiden öffentlich werden.
- Wer bei Aktienpaaren auf Overnight-Positionen verzichtet, kann die Änderungen der fundamentalen Unternehmensbewertung vermeiden, die längere Positionen treffen.
- Beim Bollinger-Band bedeutet exitZscore gleich 0 einen Ausstieg am aktuellen Mittel. exitZscore gleich minus entryZscore bedeutet einen Ausstieg erst jenseits des gegenüberliegenden Bandes, der dort das Gegensignal auslöst.
- Schrittweises Aussteigen nimmt Gewinn bei jeder kleinen Rückkehr mit und wartet nicht auf die volle Rückkehr zum Mittel. Dadurch kann die Strategie auch profitabel bleiben, wenn die Reihe nicht stationär ist und den Mittelwert nie erreicht.
- Im Vergleich von Schoenberg und Corwin wird dagegen jeder Kontrakt erst beim Endpreis F geschlossen, auch wenn der Einstieg ein average-in war.
- Beim Kalman-Beispiel wird der Long geschlossen, sobald der Prognosefehler e über minus der Wurzel von Q steigt, und der Short, sobald e unter die Wurzel von Q fällt.
- Ein Kontraktpaar im CL-Kalenderspread wird drei Monate gehalten, gerechnet als 61 Handelstage, und zehn Tage vor Verfall des nahen Kontrakts in das nächste Paar gerollt.
- Die Fälligkeiten von nahem und fernem Kontrakt liegen ein Jahr auseinander.
- Fehlt ein Z-Score, ist die Position null. Ein positiver Z-Score dreht die Ausgangslage long fern und short nah um.
- Im Devisenhandel sind Stop-Losses brauchbar, weil von Sonntag 17:00 Uhr ET bis Freitag 17:00 Uhr ET durchgehend gehandelt wird. Ist ein Markt lange geschlossen, sind Stops nutzlos, weil er zur Wiedereröffnung gappen kann.

## Risiken und Grenzen

- Jede Anlagestrategie hat Stop-Loss-Grenzen, ob selbst gesetzt, von der Risikoabteilung erzwungen oder durch einen Margin Call ausgelöst.
- Eine Strategie auf Positionen aufzubauen, die an der Börse ausgestoppt worden wären, ist unrealistisch.
- Die übliche Kalibrierung von Ein- und Ausstiegsparametern über historische Simulationen führt zu Backtest-Overfitting.
- Schoenberg und Corwin zeigen, dass auch der Ausstieg an zwei oder mehr Bollinger-Bändern im Backtest nie optimal ist.
- Nicht jede stationäre Reihe trägt, wenn die Halbwertszeit beispielsweise zehn Jahre lang ist.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 58–77 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-004-p058-p077|S. 58–77]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 76–95 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-006-p076-p095|S. 76–95]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 119–138 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-009-p119-p138|S. 119–138]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 163–165 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-012-p163-p165|S. 163–165]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 166–179 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-013-p166-p179|S. 166–179]]

## Verwandte Themen
