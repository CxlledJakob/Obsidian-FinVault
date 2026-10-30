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
aktualisiert: 2026-10-30
---

# Entry-Logik


## Kurzdefinition


## Kernaussagen


## Funktionsweise

- Die lineare Strategie steigt nicht auf einem Schwellenwert ein, sondern hält fortlaufend eine Stückzahl proportional zur Abweichung vom gleitenden Mittel.
- Im Vergleich von Schoenberg und Corwin bedeutet all-in bei L1, das gesamte Kapital zu investieren, sobald der Preis L1 erreicht, ohne darauf zu warten, ob er noch nach L2 fällt.
- All-in bei L2 wartet, bis der Preis L2 erreicht, und verdient null, wenn L2 nie kommt; average-in kauft einen Kontrakt bei L1 und einen weiteren bei L2.
- Für nicht wirklich kointegrierte Paare kann das Preisverhältnis als Einstiegssignal die dynamische Hedge Ratio ersetzen.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Beim Bollinger-Band wird erst eingestiegen, wenn der Preis um mehr als entryZscore Standardabweichungen vom Mittel abweicht.
- Long, wenn der Z-Score unter minus entryZscore liegt, und short, wenn er über entryZscore liegt; im GLD-USO-Beispiel ist entryZscore gleich 1.
- Zu jedem Zeitpunkt wird null oder eine Einheit gehalten.
- Für Scaling-in liegen die Einstiegsniveaus bei 1, 2, 3 bis N Standardabweichungen.
- Beim Kalman-Filter auf dem Spread wird gekauft, wenn der Prognosefehler e kleiner als minus der Wurzel aus Q ist, und verkauft, wenn e größer als die Wurzel aus Q ist.
- Ein kurzer Lookback und kleine Z-Score-Beträge verkürzen die Haltedauer, erhöhen die Zahl der Round-Trips und steigern in der Regel den Gewinn.
- Soll ein Mean-Reversion-Portfolio während der Trade-Dauer eine feste Stückzahl je Bestandteil halten, werden die Hedge Ratios aus der Preisreihe bestimmt.
- Bei Währungspaaren ist oft das Ratio statt des Spreads ein guter Indikator.
- Können Hedge Ratio, Mittel und Standardabweichung eines Spreads künftig variieren, werden ein gleitender Look-back oder der Kalman-Filter verwendet.
- Eine praktische Umsetzung einer linearen Handelsstrategie sind Bollinger-Bänder mit Scaling-in.
- Der erwartete Preis eines Instruments lässt sich anhand des letzten Trades, also Preis und Größe, mit dem Kalman-Filter dynamisch aktualisieren.
- Buy-on-Gap wählt nahe der Eröffnung alle Aktien, deren Rendite vom Tief des Vortags zum heutigen Open kleiner als minus eine Standardabweichung ist; die Standardabweichung kommt aus den täglichen Close-to-Close-Renditen der letzten 90 Tage, und diese Aktien sind die nach unten gegappten.
- Die Liste wird darauf verengt, dass der Eröffnungskurs über dem 20-Tage-Durchschnitt der Schlusskurse liegt.
- Gekauft werden die 10 Aktien dieser Liste mit den niedrigsten Renditen seit dem Tief des Vortags; hat die Liste weniger als 10 Titel, wird die ganze Liste gekauft.
- Die Short-Variante shortet Aktien, die um eine Standardabweichung nach oben gappen und deren Kurs dennoch unter dem 20-Tage-Durchschnitt liegt.
- Einstiegssignale zum Open werden aus Preopen-Preisen bestimmt, zum Beispiel an ARCA, weil der offizielle Open nicht zugleich Signal und Füllung sein kann.
- Im linearen Long-Short werden die Gewichte nahe dem Schluss aus der Tagesrendite bestimmt; eine Intraday-Variante nutzt die Rendite vom vorigen Schluss zum heutigen Open für den Einstieg zum Open.
- Regel 2 des Buy-on-Gap ist ein Momentum-Filter auf der Mean-Reversion-Strategie und wird im Text oft wiederverwendet.
- Wechselt das Momentum die Richtung, wird die Gegenposition eröffnet; weil die ursprüngliche Position dann verloren hat, wirkt dieses neue Einstiegssignal als Stop-Loss.
- Kointegriert oder korreliert ein Instrument, etwa ein ETF oder ein anderer Future, mit Spotpreis oder Spot-Rendite eines Rohstoffs, wird die Rollrendite des Rohstoff-Futures extrahiert, indem dieses Instrument bei Backwardation geshortet und bei Contango gekauft wird.
- Opening Gap auf Futures: Long, wenn das Open über dem Vortageshoch mal (1 plus 0,1 mal der verschobenen 90-Tage-Standardabweichung der Close-to-Close-Rendite) liegt, Short spiegelbildlich unter dem Vortagestief, Ausstieg am Schluss.
- Für GBPUSD werden Close um 17:00 Uhr ET und Open um 5:00 Uhr ET verwendet; andere Öffnungs- und Schlusszeiten lassen sich je Währung ausprobieren.
- Nach Gewinnmeldungen wird zur Eröffnung gekauft, wenn die Close-to-Open-Rendite mindestens eine halbe 90-Tage-Standardabweichung beträgt, und leerverkauft, wenn sie höchstens minus eine halbe beträgt, sofern die Meldung nach dem vorigen Schluss und vor der Eröffnung lag.
- Diese Gewinnmeldungs-Regel verlangt weder die Deutung der Meldung als gut oder schlecht noch den Vergleich mit Analystenerwartungen; liquidiert wird am selben Schluss.
- DRN wird gekauft, wenn die Rendite vom Vortagesschluss bis 15 Minuten vor Schluss größer als 2 Prozent ist, und verkauft, wenn sie kleiner als minus 2 Prozent ist; der Ausstieg liegt am Marktschluss.
- Der Ratio Trade tritt dem Bid nur bei, wenn die ursprüngliche Bid-Size viel größer ist als die Ask-Size.
- Ticking kauft zum Best Bid plus einem Tick, wenn der Spread größer als zwei Ticks ist, und verkauft zum Best Ask minus einem Tick.
- Stop Hunting legt große Sell Orders, wenn der Preis nah genug an einer Unterstützung liegt, um den nächsten Tick nach unten zu treiben.
- Der kumulative oder durchschnittliche Orderflow über ein Look-back-Fenster dient als Signal, ob der Preis steigt oder fällt.

## Risiken und Grenzen

- Unter der Annahme, dass die Wahrscheinlichkeit p eines weiteren Abtauchens konstant ist und erst bei einem festen Endpreis F alles geschlossen wird, ist average-in nie die profitabelste der drei Einstiegsarten.
- Scaling-in muss im Backtest nicht optimal sein, ist im Live-Handel aber oft nützlich, weil Volatilitäten und Wahrscheinlichkeiten sich ändern.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 173–186 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-013-p173-p186|S. 173–186]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 153–172 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-009-p153-p172|S. 153–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 210–229 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-012-p210-p229|S. 210–229]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 400–419 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-022-p400-p419|S. 400–419]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 457–476 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-025-p457-p476|S. 457–476]]

## Verwandte Themen
