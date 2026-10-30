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

- Eine Long-Position bedeutet, das Wertpapier zu besitzen und darauf zu hoffen, es später zu einem höheren Preis zu verkaufen.
- Eine Short-Position bedeutet, das Wertpapier verkauft zu haben, ohne es zu besitzen, mit der Pflicht, es später zurückzukaufen. Der Inhaber gewinnt durch einen späteren Kursrückgang, weil der Rückkauf unter dem Verkaufspreis liegt.
- Neutral bezeichnet den Fall, dass der Anleger keine Position im Markt hält.
- Es gibt genau zwei Einstiegsstrategien, den Trailing-One-Bar-Entry und den Swing Entry. Beide verlangen, dass der Markt sich vor dem Einstieg in die erwartete Richtung bewegt.

## Kernaussagen


## Funktionsweise

- Die lineare Strategie steigt nicht auf einem Schwellenwert ein, sondern hält fortlaufend eine Stückzahl proportional zur Abweichung vom gleitenden Mittel.
- Im Vergleich von Schoenberg und Corwin bedeutet all-in bei L1, das gesamte Kapital zu investieren, sobald der Preis L1 erreicht, ohne darauf zu warten, ob er noch nach L2 fällt.
- All-in bei L2 wartet, bis der Preis L2 erreicht, und verdient null, wenn L2 nie kommt; average-in kauft einen Kontrakt bei L1 und einen weiteren bei L2.
- Für nicht wirklich kointegrierte Paare kann das Preisverhältnis als Einstiegssignal die dynamische Hedge Ratio ersetzen.
- Beim MACD ohne Overbought- und Oversold-Zonen gilt ein kürzerer Bar von unterhalb der Signallinie als bullische Umkehr der höheren Zeitebene. Ein längerer Bar von oberhalb der Signallinie ist die bullische Umkehr der kleineren Zeitebene.
- Die Buy-Stop-Order des Swing Entry kann nach den regulären Handelszeiten gelegt werden. Wird sie ausgeführt, setzt eine Kontingenz sofort den Sell-Stop. Wird sie nicht ausgeführt, wird am Abend geprüft, ob die Bedingungen für den nächsten Tag noch stehen.

## Voraussetzungen

- Es wird angenommen, dass alle vom Verfahren benötigten Marktinformationen bekannt und öffentlich verfügbar sind, wenn das Verfahren die Empfehlung erzeugt.

## Anwendung im Trading

- Die Alternativhypothese für MA50 behauptet Vorhersagekraft und deshalb eine erwartete Rendite größer als null auf trendbereinigten Daten. Null ist die Rendite, die von einer Regel ohne Vorhersagekraft erwartet wird. Die Nullhypothese behauptet eine erwartete Rendite von null oder weniger.

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
- Ein Leerverkaufssignal wegen Penetration der Nackenlinie ist erst zulässig, wenn die rechte Schulter, Punkt E, durch den Zigzag-Filter erkannt wurde.
- Der Kurs kann die Nackenlinie kreuzen, bevor diese Erkennung vorliegt.
- Chang und Osler setzen den Einstieg deshalb erst an, nachdem die rechte Schulter objektiv erkannt ist.
- Dieser Einstieg ist in manchen Fällen preislich ungünstiger und hält den Backtest frei von Look-ahead Bias.
- Liegt die rechte Schulter nur 4 Prozent über der Nackenlinie, die Zigzag-Schwelle aber bei 10 Prozent, darf nicht zu einem Preis nur 4 Prozent unter der Schulter eingestiegen werden; nötig ist die Bewegung von 10 Prozent unter der Schulter, die das Muster erst vollständig erkennbar macht.
- Die Regel MA50 hält eine Long-Position im S&P 500, wenn der Schlusskurs über einem 50-Tage-Durchschnitt liegt, und andernfalls eine Short-Position.
- Eine traditionelle Trendregel geht long im S&P 500, sobald der Channel-Breakout-Operator einen Aufwärtstrend anzeigt, und short, sobald er einen Abwärtstrend anzeigt.
- Inverse Trendregeln stellen dieselben Zustände mit umgekehrtem Vorzeichen: short im S&P 500, wenn die analysierte Reihe im Aufwärtstrend bestimmt wird.
- Signale der Extremwert-Regeln entstehen, wenn die geglättete und kanalnormierte Reihe eine Schwelle kreuzt.
- Es gibt vier Schwellenereignisse: Die untere Schwelle wird abwärts gekreuzt, die untere Schwelle wird aufwärts gekreuzt, die obere Schwelle wird aufwärts gekreuzt, und die obere Schwelle wird abwärts gekreuzt.
- Jede E-Regel koppelt zwei dieser Ereignisse, eines für Long-Einstieg und Short-Ausstieg und eines für Short-Einstieg und Long-Ausstieg.
- Das Schema ergibt 12 E-Regeltypen; Typ 7 ist die Umkehrung von Typ 1 und Typ 8 die Umkehrung von Typ 2, sodass eigene inverse Versionen überflüssig sind, weil alle Möglichkeiten abgedeckt sind.
- Nach Tabelle 8.3 gilt für Typ 1 Long-Einstieg und Short-Ausstieg bei Ereignis 1 und Short-Einstieg und Long-Ausstieg bei Ereignis 2; Typ 6 koppelt Ereignis 3 mit Ereignis 4 und Typ 12 Ereignis 4 mit Ereignis 3.
- Vor der Kanalnormierung wird jede Eingabe mit einem viertägigen linear gewichteten gleitenden Durchschnitt geglättet, damit die Reihe nicht um die Schwelle pendelt und zu viele Signale erzeugt.
- Alle Reihen wurden aus Gründen der Einheitlichkeit mit diesem Durchschnitt behandelt, auch bereits geglättete wie der 30-Tage-Durchschnitt des Negative Volume.
- Die Fallstudie beschränkte den Regelsatz auf einen Typ binärer Regel, die Long-Short-Umkehr, die immer eine Marktposition halten muss.
- Die Pflicht, immer eine Position zu halten, ruht auf der unwahrscheinlichen Annahme, der Markt sei dauerhaft ineffizient und biete fortlaufend Gewinngelegenheiten.
- Selektive Regeln, die nur dann Exposition suchen, wenn sie gerechtfertigt ist, passen zur vernünftigeren Annahme, Märkte seien nur gelegentlich ineffizient.
- Tristate-Regeln mit long, short und neutral oder binäre Regeln, die long und neutral oder short und neutral unterscheiden, wurden nicht geprüft und könnten überlegen sein.
- Braucht eine Regel den Schlusskurs, um das Signal zu berechnen, ist ein Ein- oder Ausstieg zu ebendiesem Schluss nicht zulässig; der erste zulässige Preis ist der nächste Preis.
- Bei Tagesdaten, wie in der Fallstudie, liegt der erste zulässige Ausführungspreis erst auf der Eröffnung des Tages nach dem Signal; Ein- und Ausstiege wurden zum Open des Folgetags eines Umkehrsignals angenommen.
- Im Beispiel mit Wilders Relative Strength Index wird aus einem Doppel-Durchschnitt-Crossover, der immer von long nach short oder von short nach long dreht, eine Regel, die ganz aus dem Markt bleiben kann.
- Liegt der Relative Strength Index beim Verkaufssignal über der Schwelle rsi_max, wird neutral statt short; liegt er beim Kaufsignal unter rsi_min, wird neutral statt long.
- Beim Voting innerhalb eines Themas wird eine Position von einer Einheit in Richtung der Mehrheit genommen; sind die meisten Regeln short, wird eine Einheit short.
- Bei der Fractional Position ist die Größe proportional zum Nettoanteil, Zahl long minus Zahl short, geteilt durch die Zahl aller Regeln.
- Bei 2.040 On-Balance-Volume-Regeln, von denen 1.158 short und 882 long signalisieren, wird eine Short-Position von 0,135 Einheiten genommen, weil (882 minus 1.158) geteilt durch 2.040 gleich −0,135 ist.
- Ein Diffusionsindikator aus den 6.402 Regeln muss die inversen Regeln weglassen, sonst nimmt er immer den Wert null an.
- Ein Diffusionsindikator der Trendregeln wird nur aus den TT-Regeln gebaut, die TI-Regeln entfallen; bei Extremen und Übergängen werden nur die Typen 1 bis 6 verwendet und die Typen 7 bis 12 ausgeschlossen, weil sie die Umkehrungen der Typen 1 bis 6 sind.
- Die komplexere Regel nimmt eine Long-Position und hat vier optimierbare Parameter: die Spanne des kurzen gleitenden Durchschnitts, die Spanne des langen gleitenden Durchschnitts, rsi_max und rsi_min.
- Eine große Zahl von Kombinationen dieser Parameterwerte wird gegen die Trainingsdaten laufen gelassen.
- Die Möglichkeit, dass die Zeitreihe genau gleich dem gleitenden Durchschnitt ist, wird beseitigt, indem der Durchschnitt mit höherer Genauigkeit berechnet wird als das Preisniveau.
- An einem Preisziel wird nicht gekauft oder verkauft. Eine Einstiegsstrategie braucht einen konkreten Kauf- oder Verkaufspreis und einen konkreten ersten Schutzstop, weil Broker keine ungefähren Orders annehmen.
- Sobald die Bedingungen für eine wahrscheinliche Korrektur- oder Trendumkehr stehen, ist der Einstieg vollständig objektiv. Bis dahin steckt Urteil in der Auswahl der Bedingungen, danach nicht mehr.
- Der Trailing-One-Bar-High- oder -Low-Einstieg legt nach der Umkehrbedingung und der Momentumumkehr der kleineren Zeitebene einen Buy-Stop oder Sell-Stop einen Tick über das Hoch oder unter das Tief des letzten abgeschlossenen Bars.
- Der erste Schutzstop liegt einen Tick jenseits des Swing-Hochs oder Swing-Tiefs, das vor dem Einstieg entstanden ist.
- Der Einstieg muss nicht am nächsten Bar erfolgen. Es kann mehrere Bars dauern, bis das nachgezogene Ein-Bar-Hoch oder Ein-Bar-Tief genommen wird.
- Nach einer bärischen Momentumumkehr läuft der Trailing-One-Bar-Low weiter, solange das Momentum bärisch bleibt und die Oversold-Zone nicht erreicht. Eine bullische Umkehr oder Oversold vor der Ausführung streicht den Einstieg, bis die nächste bärische Umkehr kommt und die höhere Zeitebene weiter bärisch und nicht oversold ist.
- Läuft der Markt nicht sofort in die erwartete Richtung, liegt der Einstieg oft zu einem besseren Preis oder mit geringerem Kapitaleinsatz als direkt nach der Umkehr.
- Wird ein Trade ausgestoppt, läuft dieselbe Strategie weiter, solange die Bedingungen gelten.
- Der Swing Entry verlangt, dass ein Swing-Hoch oder Swing-Tief in Richtung des erwarteten Trends genommen wird. Das höhere Momentum ist für einen Long bullisch oder bärisch oversold, für einen Short bärisch oder bullisch overbought, und die kleinere Zeitebene dreht in diese Richtung.
- Reines Swing-Trading kauft jedes neue Swing-Hoch oder verkauft jedes neue Swing-Tief in Trendrichtung. Das funktioniert in einem starken Trend und scheitert, wenn der Swing der letzte Abschnitt ist oder der Markt in eine seitwärts hackende Trading-Range läuft.
- Hier wird der Swing Entry nur gesetzt, wenn die Umkehrbedingungen stehen, und er erfolgt auf einem kleinen Swing der niedrigeren Zeitebene, um den Anfangseinsatz zu begrenzen.
- Ein Handel über das Swing-Hoch, der ein Wave-5-Tief bestätigen soll, hebt jedes logische Bärenmuster auf und ist ein Grund, long zu sein. Das wird Pattern-Reversal-Signal genannt.
- Für Daytrades sollen zwei höhere Zeitebenen das Momentum in Richtung der kleineren Zeitebene haben. Dieselben zwei Strategien gelten für jeden Markt, jede Zeitebene und jede Bedingung.
- Nie an einem Zielpreis kaufen oder verkaufen. Immer verlangen, dass der Markt in Richtung des erwarteten Trends läuft, bevor der Trade ausgeführt wird.

## Risiken und Grenzen

- Unter der Annahme, dass die Wahrscheinlichkeit p eines weiteren Abtauchens konstant ist und erst bei einem festen Endpreis F alles geschlossen wird, ist average-in nie die profitabelste der drei Einstiegsarten.
- Scaling-in muss im Backtest nicht optimal sein, ist im Live-Handel aber oft nützlich, weil Volatilitäten und Wahrscheinlichkeiten sich ändern.

## Beispiele

- Im Short-Beispiel nahm Bar 4 das nachgezogene Ein-Bar-Tief. Weder Bar 2 noch Bar 3 hatten das Tief des vorigen Bars genommen. Der Schutz-Buy-Stop lag einen Tick über dem Hoch von Bar 3, dem höchsten Bar seit der bärischen Momentumumkehr.
- Beim EUR/USD entstand die bullische Wochen-MACD-Umkehr in der Woche zum 20. Oktober. Drei Tagesbars später drehte der Tages-MACD bullisch. Am Folgetag wurde einen Tick über dem Hoch des Vortags gekauft, mit Stop einen Tick unter dem Swing-Tief vor der bullischen Umkehr.
- Im 5-Minuten-Daytrade lag der Swing-Entry-Short unter 1356,25 und wurde am nächsten Bar ausgeführt, mit Buy-Stop einen Tick über dem Swing-Hoch bei 1362,75.

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
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 153–172 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-012-p153-p172|S. 153–172]]

## Verwandte Themen
