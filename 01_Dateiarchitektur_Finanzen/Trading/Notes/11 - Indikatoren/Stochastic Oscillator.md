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
aktualisiert: 2026-10-30
---

# Stochastic Oscillator


## Kurzdefinition

- Die Fallstudie bezeichnet Stochastics als Kanalnormierung. George Lane beschrieb Anfang der 1970er Jahre einen praktisch identischen Operator und nannte ihn Stochastic. Der Name ist ein Fehlgriff, denn Stochastic bezeichnet mathematisch die Entwicklung einer Zufallsvariablen über die Zeit, während an der Kanalnormierung nichts Zufälliges ist; sie ist eine vollständig deterministische Datentransformation.
- Der Stochastic ist ein sehr verbreiteter Indikator und in jeder Handelssoftware enthalten.
- Er hat Overbought- und Oversold-Zonen sowie eine schnelle und eine langsame Linie; beide Eigenschaften sind für diese Momentumstrategien hilfreich.
- Die langsame Linie ist gewöhnlich nur ein gleitender Durchschnitt der schnellen Linie und reagiert langsamer auf Momentumänderungen.

## Kernaussagen


## Funktionsweise

- Der Kanalnormierungs-Operator entfernt den Trend einer Zeitreihe und macht dadurch kurzfristige Schwankungen um den Trend deutlich. Er misst die aktuelle Position der Reihe innerhalb eines gleitenden Kanals.
- Der Kanal ist durch das Maximum und das Minimum der Zeitreihe über eine festgelegte Rückschau definiert und darin dem Kanalausbruch ähnlich.
- Die kanalnormierte Fassung ist auf den Bereich 0 bis 100 skaliert. Liegt die rohe Reihe an ihrem Maximum innerhalb der Rückschau, nimmt der Operator den Wert 100 an. Liegt sie am Minimum, ist der Wert null. Ein Wert von 50 zeigt, dass die Reihe gerade in der Mitte zwischen Maximum und Minimum liegt.
- Die Formel teilt die Differenz aus dem Wert der Reihe zur Zeit t und dem Minimum der letzten n Tage durch die Differenz aus Maximum und Minimum der letzten n Tage und multipliziert mit 100.
- Im Rechenbeispiel der Abbildung beträgt das Kanalmaximum 83, das Kanalminimum 60 und der aktuelle Wert 75. Die kanalnormierte Größe wird als (75 minus 60) geteilt durch (83 minus 60) gleich 0,65 angegeben.
- In seinen Filtereigenschaften wirkt der Operator als Hochpass. Im Gegensatz zum gleitenden Durchschnitt, einem Tiefpass, drückt er die kurzperiodischen, hochfrequenten Schwingungen in der Ausgabe aus und filtert die langperiodischen Schwankungen, den Trend, heraus.
- Die Eingabereihe kann einen deutlichen Aufwärtstrend haben, während die Ausgabereihe keinen Trend hat.
- Ein Stochastic mit zwei Linien macht eine Momentum-Umkehr, wenn die schnelle Linie über oder unter die langsame kreuzt.
- Die schnelle Linie ist gewöhnlich die Rohdaten, die langsame gewöhnlich ein gleitender Durchschnitt der schnellen Linie.
- In Abbildung 2.1 hat der Stochastic zusammen mit RSI, DT Oscillator und einem einfachen ROC eine Lookback-Periode von acht Perioden.
- Der DT Oscillator ist eine Kombination aus RSI und Stochastic.
- Die Momentum-Umkehren des Stochastic, bei denen die schnelle die langsame Linie kreuzt, liegen innerhalb von ein oder zwei Balken der Umkehren der anderen Indikatoren in dieser Abbildung.
- In Abbildung 2.2 lagen die Umkehren von Stochastic und DTosc plus oder minus einen Balken voneinander; beide wären gleich hilfreich gewesen, die Momentum-Umkehren dieser Daten zu erkennen.
- Auch ohne Justierung der Einstellungen stellte der Stochastic die Momentum-Zyklen etwa gleich gut dar wie die anderen Indikatoren.
- Fast jeder preisbasierte Indikator, einschließlich des Stochastic, eignet sich für die Multiple-Time-Frame-Momentum-Strategie, weil alle die Änderungsrate und dieselben Zyklen darstellen.
- Overbought und Oversold beschreiben schlecht, dass der Indikator lediglich extreme Werte erreicht.
- Das Erreichen der Overbought-Zone am oberen Extrem heißt nicht zwangsläufig, dass der Markt zur Abwärtswende bereit ist, sondern nur, dass der Indikator nahe dem Extrem steht.
- Erst nach Historie und dem Betrachten vieler Momentumzyklen lässt sich sagen, ob der Preis gewöhnlich an oder nahe einer Umkehr steht, wenn der Indikator Overbought oder Oversold erreicht.
- Kreuzt die schnelle Linie über die langsame, ist das eine bullische Momentumumkehr; kreuzt sie darunter, eine bärische.
- Diese Umkehr warnt, dass sich die Momentumrate ändert, und oft geht eine richtungsgebende Preisänderung um ein paar Bars voraus oder folgt.
- Die Momentumumkehren sind keine Handelssignale, sondern Bedingungen, die erfüllt sein müssen, um einen Trade zu erwägen.
- Bei einem Zweilinien-Indikator wie dem Stochastic müssen schnelle und langsame Linie beide in der Zone liegen, damit er als overbought oder oversold gilt.
- Ein Stochastic hängt in der Overbought-Zone, wenn der Trend bullisch ist, macht relativ flache Momentumkorrekturen und erreicht auf Preiskorrekturen oft nicht die Oversold-Zone.
- Die Trendneigung größeren Grades beeinflusst, wie der Stochastic zykliert.

## Voraussetzungen


## Anwendung im Trading

- Spätestens 1965 nutzte Heiby den Operator, um Divergenzregeln zu formulieren. Er verglich den kanalnormierten Wert des S&P 500 mit dem kanalnormierten Wert eines Marktbreite-Indikators.
- Nach Heiby lag eine Divergenz vor, wenn eine Reihe im oberen Quartil ihrer 50-Tage-Spanne lag, Wert größer als 74, und die andere Reihe im unteren Quartil ihrer Spanne, Wert kleiner als 26.
- Die Fallstudie nutzt den Operator für zwei Arten von Regeln: Extreme und Übergänge sowie Divergenzen.
- Dieser Text verwendet den Ausdruck Kanalnormierung statt Lanes Ausdruck, weil er beschreibt, was der Operator tut. Die meisten Schriften der technischen Analyse verwenden weiter den Ausdruck Stochastics.
- Die bärische Stochastic-Umkehr der höheren Zeitebene eröffnet das Setup. Ausgeführt wird erst, wenn die kleinere Zeitebene ebenfalls bärisch dreht und der Preis das verlangte Bar- oder Swing-Tief nimmt.

## Regeln und Kriterien

- Für den Stochastic gelten dieselben vier Dual-Time-Frame-Regeln wie für den DTosc, weil auch er Overbought- und Oversold-Zonen hat.
- Im Chartbeispiel liegen die Zonen bei 75 Prozent Overbought und 25 Prozent Oversold.

## Risiken und Grenzen

- Es gibt keinen magischen oder mystischen Stochastic für Momentum-Handel; ein angeblich geheimer narrensicherer Indikator ist wahrscheinlich schon einer aus dem Chartprogramm.

## Beispiele

- Am S&P über etwa vier Monate mit einer Serie klarer Schwünge und bullischer Neigung machte der Stochastic Momentumumkehren innerhalb von ein oder zwei Bars zu jeder Preisumkehr.
- In diesem Abschnitt erreichten beide Linien vor einer bärischen Momentumumkehr weit die Overbought-Zone, vor den bullischen Umkehren aber typischerweise nicht die Oversold-Zone.
- In einem anderen viermonatigen starken Aufwärtstrend mit nur kleinen Korrekturen und denselben Einstellungen hing der Stochastic lange in der Overbought-Zone und fiel nur bei größeren, mehrere Bars dauernden Korrekturen unter die Overbought-Linie.
- Am 15-Minuten-EUR/USD drehte das Stochastic-Momentum einige 15-Minuten-Bars vor dem DTosc bärisch, doch die erste bärische 15-Minuten-Stochastic-Umkehr lag ebenfalls nach dem starken Aufwärtsstoß.
- Obwohl der Stochastic an den Momentumhochs dieses bärischen Momentumtrends die Overbought-Zone nicht erreichte, folgte auf jede bärische 15-Minuten-Umkehr ein Rückgang.
- Alle diese Stochastic-Setups waren gute Daytrade-Setups, und die meisten waren gute Swingtrade-Setups.
- Abbildung 2.24 zeigt bärische Stochastic-Umkehren der kleineren Zeitebene während eines Bärentrends der größeren Zeitebene.
- Mitte Dezember machte das tägliche Stochastic-Momentum eine bärische Umkehr, der Preis lag am 50-Prozent-Retracement. Zwei Tage später nahm IBM das Trailing-One-Bar-Low und führte den Short aus. Einige Tage später folgte ein kleiner Verlust am Stop.
- Für diesen Tages-Short musste das Wochenmomentum bärisch oder bullisch overbought sein.
- Am letzten Wochenbar hatte der wöchentliche Stochastic eine bärische Umkehr gemacht und damit das Swing-Entry-Short-Setup auf den Tagesdaten eröffnet, in der Woche zum 19. Oktober.
- Erst am 31. Oktober machte IBM eine bärische Stochastic-Umkehr auf Tagesbasis. Der Kurs hatte das 50-Prozent-Retracement am 100-Prozent-Zeitretracement berührt, sieben Handelstage abwärts und sieben aufwärts.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 381–400 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-021-p381-p400|S. 381–400]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 400–419 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-022-p400-p419|S. 400–419]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 419–438 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-023-p419-p438|S. 419–438]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 23–42 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-003-p023-p042|S. 23–42]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 42–61 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-004-p042-p061|S. 42–61]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 61–62 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-005-p061-p062|S. 61–62]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 153–172 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-012-p153-p172|S. 153–172]]

## Verwandte Themen
