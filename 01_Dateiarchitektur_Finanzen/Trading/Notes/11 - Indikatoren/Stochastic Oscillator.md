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

## Kernaussagen


## Funktionsweise

- Der Kanalnormierungs-Operator entfernt den Trend einer Zeitreihe und macht dadurch kurzfristige Schwankungen um den Trend deutlich. Er misst die aktuelle Position der Reihe innerhalb eines gleitenden Kanals.
- Der Kanal ist durch das Maximum und das Minimum der Zeitreihe über eine festgelegte Rückschau definiert und darin dem Kanalausbruch ähnlich.
- Die kanalnormierte Fassung ist auf den Bereich 0 bis 100 skaliert. Liegt die rohe Reihe an ihrem Maximum innerhalb der Rückschau, nimmt der Operator den Wert 100 an. Liegt sie am Minimum, ist der Wert null. Ein Wert von 50 zeigt, dass die Reihe gerade in der Mitte zwischen Maximum und Minimum liegt.
- Die Formel teilt die Differenz aus dem Wert der Reihe zur Zeit t und dem Minimum der letzten n Tage durch die Differenz aus Maximum und Minimum der letzten n Tage und multipliziert mit 100.
- Im Rechenbeispiel der Abbildung beträgt das Kanalmaximum 83, das Kanalminimum 60 und der aktuelle Wert 75. Die kanalnormierte Größe wird als (75 minus 60) geteilt durch (83 minus 60) gleich 0,65 angegeben.
- In seinen Filtereigenschaften wirkt der Operator als Hochpass. Im Gegensatz zum gleitenden Durchschnitt, einem Tiefpass, drückt er die kurzperiodischen, hochfrequenten Schwingungen in der Ausgabe aus und filtert die langperiodischen Schwankungen, den Trend, heraus.
- Die Eingabereihe kann einen deutlichen Aufwärtstrend haben, während die Ausgabereihe keinen Trend hat.

## Voraussetzungen


## Anwendung im Trading

- Spätestens 1965 nutzte Heiby den Operator, um Divergenzregeln zu formulieren. Er verglich den kanalnormierten Wert des S&P 500 mit dem kanalnormierten Wert eines Marktbreite-Indikators.
- Nach Heiby lag eine Divergenz vor, wenn eine Reihe im oberen Quartil ihrer 50-Tage-Spanne lag, Wert größer als 74, und die andere Reihe im unteren Quartil ihrer Spanne, Wert kleiner als 26.
- Die Fallstudie nutzt den Operator für zwei Arten von Regeln: Extreme und Übergänge sowie Divergenzen.
- Dieser Text verwendet den Ausdruck Kanalnormierung statt Lanes Ausdruck, weil er beschreibt, was der Operator tut. Die meisten Schriften der technischen Analyse verwenden weiter den Ausdruck Stochastics.

## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 381–400 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-021-p381-p400|S. 381–400]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 400–419 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-022-p400-p419|S. 400–419]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 419–438 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-023-p419-p438|S. 419–438]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]

## Verwandte Themen
