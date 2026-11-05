---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/11 - Indikatoren/11 - Indikatoren|11 - Indikatoren]]"
weitere_hauptthemen: []
unterthema: "Oszillatoren"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Relative Strength Index


## Kurzdefinition

- Welles Wilder definierte den RSI als RSI = 100 − 100 / (1 + RS) mit RS = CU / CD; CU ist die Summe der positiven Schlusskursdifferenzen über die Beobachtungsperiode, CD die Summe der negativen Schlusskursdifferenzen, ausgedrückt als positive Zahl.
- Nach Einsetzen und Vereinfachen ist der RSI der prozentuale Anteil der Summe der Aufwärts-Schlusskursdifferenzen an der Summe aller Schlusskursdifferenzen der Beobachtungsperiode: RSI = 100 · CU / (CU + CD).
- Wilders ursprünglicher RSI ist RSI = 100 − 100 / (1 + RS), mit RS = Durchschnitt der Closes Up über 14 Tage geteilt durch Durchschnitt der Closes Down über 14 Tage.

## Kernaussagen

- Der DTosc ist ein proprietärer Indikator der Software Dynamic Trader.
- Der DTosc ist eine Kombination aus Stochastic und Relative Strength Index.
- Der Autor bevorzugt einen Indikator wie den DTosc oder einen Stochastic oder einen anderen Indikator mit Overbought- und Oversold-Zonen.
- Im Indikatorfenster des DTosc stehen vier Zahlen: Die erste ist die rohe Lookback-Periode, die übrigen sind die Perioden, über die die Rohdaten geglättet werden.
- Bei einem Zweilinien-Indikator wie dem DTosc müssen schnelle und langsame Linie beide in der Overbought- oder Oversold-Zone liegen, damit der Indikator als overbought oder oversold gilt.
- Der MACD oder ein anderer vertrauter Indikator kann ebenso nützlich sein wie ein Indikator mit Overbought- und Oversold-Zonen.
- Der modifizierte RSI mit vorgeschaltetem Roofing Filter ist deutlich reaktionsschneller und hat weniger Lag als der Standard-RSI, weil der Hochpassteil des Roofing Filters die niederfrequenten Komponenten entfernt.
- Die übliche Interpretation von Indikatoren wie RSI oder Stochastic enthält die Frequenzverzerrungen der Spectral Dilation in ihrer Ausgabe.
- Das Einfügen des Roofing Filters verändert Nutzung und Interpretation von Standardindikatoren dramatisch und macht sie im Grunde zu neuen Indikatoren.
- In Abbildung 7.5 verwendet Ehlers für den Standard-RSI einen SuperSmoother als Glättung.

## Funktionsweise

- Ein Relative Strength Index mit zwei Linien macht eine Momentum-Umkehr, wenn die schnelle Linie über oder unter die langsame kreuzt.
- Die schnelle Linie ist bei den meisten Zwei-Linien-Indikatoren gewöhnlich die Rohdaten, die langsame gewöhnlich ein gleitender Durchschnitt der schnellen Linie.
- In Abbildung 2.1 werden Stochastic, RSI und der DT Oscillator verglichen, der eine Kombination aus RSI und Stoch ist; alle vier Studien einschließlich eines einfachen ROC haben eine Acht-Perioden-Rückschau.
- Die Momentumtrends von Stochastic, RSI und DTosc sind ungefähr gleich, und die Umkehren der schnellen über die langsame Linie liegen innerhalb von ein oder zwei Balken voneinander, auch ohne Justierung der Einstellungen.
- Fast jeder preisbasierte Momentum-Indikator, also auch der RSI, kann für die Multiple-Time-Frame-Momentum-Strategie genutzt werden, weil alle die Änderungsrate und dieselben Momentum-Zyklen darstellen.
- Der RSI ist funktional dasselbe wie ein einpoliger Hochpassfilter, weil der CU-Term im Zähler nur eine Summe von Ein-Bar-Differenzen ist.
- Der modifizierte RSI nach Ehlers beginnt mit einem Roofing Filter aus zweipoligem 48-Bar-Hochpass und 10-Bar-SuperSmoother, danach folgt die übliche RSI-Berechnung über eine Länge von standardmäßig 10 Bars.
- Im Code des modifizierten RSI wird ClosesUp durch die Summe aus ClosesUp und ClosesDn geteilt, optional mit einem SuperSmoother zu MyRSI geglättet und mit Referenzlinien bei 0,7 und 0,3 dargestellt.
- Ohne den optionalen Glättungsfilter lässt sich der Lag des modifizierten RSI etwas verringern, allerdings wird der Indikator dadurch unregelmäßiger.
- Closes Up: Liegt der heutige Schluss über dem gestrigen, wird die Differenz der Schlusskurse zum Durchschnitt addiert. Closes Down: Liegt er darunter, wird die positive Differenz addiert.
- Mit CU und CD lässt sich der RSI zu 100 · CU / (CU + CD) vereinfachen. Verallgemeinert können CU und CD die Summen über ein beliebiges Intervall sein, und der Faktor 100 ist nur eine Skalierung.
- Der RSI ist damit das Verhältnis der Summe der Closes Up zur Summe der Absolutwerte aller Schlusskursdifferenzen.
- In einer idealen Welt mit Preisen als Sinuswelle der dominanten Zyklusperiode berührt der RSI gerade 1, wenn die Aufwärtshälfte des Zyklus summiert wird, und gerade 0 bei der Abwärtshälfte; die beste adaptive Summationslänge ist daher die Hälfte des gemessenen dominanten Zyklus.
- Der adaptive RSI nutzt als Eingabe die Variable Filt statt der Schlusskurse, damit nur die vom Roofing-Filter durchgelassenen Frequenzkomponenten eingehen.
- Statt Zähler und Nenner getrennt zu mitteln, glättet Ehlers das Verhältnis mit dem SuperSmoother-Filter; dessen Koeffizienten stammen aus der Messung des dominanten Zyklus im selben Code.

## Voraussetzungen


## Anwendung im Trading

- Im Beispiel der geführten Komplexitätsoptimierung wird eine Umkehrregel aus zwei gleitenden Durchschnitten um eine Regel auf Wilders Relative Strength Index ergänzt, einem Indikator, der die Rate der Preisänderung misst.
- Der Relative Strength Index dient als Filter: liegt er beim Verkaufssignal des Doppel-Durchschnitt-Crossover über der Schwelle rsi_max, wird eine neutrale Position statt einer Short-Position genommen.
- Liegt der Relative Strength Index beim Kaufsignal unter der Schwelle rsi_min, wird eine neutrale Position statt einer Long-Position genommen.
- Diese komplexere Regel hat vier optimierbare Parameter: die Spanne des kurzen gleitenden Durchschnitts, die Spanne des langen gleitenden Durchschnitts, rsi_max und rsi_min.
- Im unterstellten Zahlenbeispiel verdient die Vier-Parameter-Regel 50 Prozent im Training gegenüber 30 Prozent der Zwei-Parameter-Regel und 20 Prozent im Test gegenüber 15 Prozent.
- Schneidet eine komplexere Regel im Testsatz besser ab, ist die vernünftige Annahme, die zusätzliche Komplexität habe weitere systematische Aspekte des Marktverhaltens ausgenutzt.
- Der aus einer Spektralschätzung gewonnene dominante Zyklus ändert sich mit der Zeit und kann genutzt werden, um Indikatoren wie den RSI automatisch abzustimmen.

## Regeln und Kriterien

- Die komplexere Regel hat vier optimierbare Parameter, darunter rsi_max und rsi_min, neben der Spanne des kurzen und der Spanne des langen gleitenden Durchschnitts.
- Eine große Zahl von Kombinationen dieser Parameter wird gegen die Trainingsdaten laufen gelassen.
- Die einzige Variable des RSI ist die Beobachtungsperiode; für maximale Wirksamkeit soll sie die Hälfte der gemessenen Zyklusperiode betragen.
- Ist die Beobachtungsperiode der halbe dominante Zyklus, entspricht bei einer reinen Sinuswelle die Summe der Aufwärtsschlüsse vom Tal bis zum Gipfel genau der Gesamtsumme, sodass der RSI 100 beträgt; in der folgenden Halbperiode gibt es keine Aufwärtsschlüsse und der RSI ist null.
- Der adaptive RSI hat Referenzlinien bei 30 und 70 Prozent; sie lassen sich leicht auf 20/80 Prozent oder andere passende Werte ändern.
- Der RSI ist über die halbe Periode des gemessenen dominanten Zyklus optimiert, um volle Ausschläge ohne Übersättigung zu erreichen.

## Risiken und Grenzen

- Es gibt keinen magischen Indikator für Momentum-Handel; alle Momentum-Indikatoren stellen dieselben Zyklen dar und kehren etwa zur selben Zeit um.
- Bei sehr langer Summationslänge sind die Closes Up etwa die Hälfte der absoluten Kursdifferenzen; der RSI pendelt dann um 0,5 und ist praktisch wertlos.
- Bei sehr kurzer Summationslänge bleibt der RSI in Aufwärtstrends lange bei 1 und in Abwärtstrends lange bei 0 stecken.
- Die übliche Länge von 14 Tagen wurde laut Ehlers' Broker verwendet, weil Wilder es so sagte; diese unbefriedigende Antwort war für Ehlers der Anlass, jahrzehntelang nach optimalen Indikatoreinstellungen zu suchen.

## Beispiele

- Die Vier-Parameter-Regel, die die RSI-Schwellen einschließt, verdiente im Trainingsset 50 Prozent gegenüber 30 Prozent der Zwei-Parameter-Vorgängerregel.
- Im Testset verdiente diese Vier-Parameter-Regel 20 Prozent gegenüber 15 Prozent der einfachen Regel aus zwei gleitenden Durchschnitten.
- Die bessere Testset-Leistung der komplexeren Regel legt nahe, dass die zusätzliche Komplexität weitere systematische Aspekte des Marktverhaltens ausgenutzt hat.
- Am täglichen S&P 500 mit 21 Tagen roher DTosc-Lookback-Periode oszillierte der Indikator mit den Preisschwüngen, doch die meisten Momentumumkehren erreichten die Overbought- oder Oversold-Zone nicht.
- Dieselbe Serie mit 8 Tagen roher Lookback-Periode machte die Momentumumkehren an Hochs und Tiefs tendenziell in den Overbought- und Oversold-Zonen und auf oder innerhalb von ein oder zwei Bars zum Preishoch oder -tief.
- Mit 13 Tagen roher Lookback-Periode war der DTosc unter den drei geprüften Einstellungen die beste für diese Daten.
- Auf Dollar General (DG) über etwa ein Jahr erreicht der adaptive RSI 0 oder 1 nur, wenn die Preise einen zyklischen Schwung über die halbe dominante Zyklusperiode hatten. Das geschieht relativ selten und zeigt, dass der Indikator richtig abgestimmt ist (Abbildung 11.1).

## Unterschiedliche Quellenpositionen

- Im direkten Vergleich der adaptiven Indikatoren zeigen RSI, Stochastic und CCI im groben Sinn ziemlich dasselbe; ohne Indikator-Transformationen gibt es keinen zwingenden Grund, einen dem anderen vorzuziehen.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 457–476 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-025-p457-p476|S. 457–476]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 23–42 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-003-p023-p042|S. 23–42]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 42–61 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-004-p042-p061|S. 42–61]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 84–96 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-008-p084-p096|S. 84–96]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 121–140 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-011-p121-p140|S. 121–140]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 140–159 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-012-p140-p159|S. 140–159]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 159–178 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-013-p159-p178|S. 159–178]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 197–216 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-015-p197-p216|S. 197–216]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 216–235 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-016-p216-p235|S. 216–235]]

## Verwandte Themen
