---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/14 - Marktzyklen/14 - Marktzyklen|14 - Marktzyklen]]"
weitere_hauptthemen: []
unterthema: "Zyklische Analyse"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Zyklusphase


## Kurzdefinition


## Kernaussagen

- Ehlers stellte den Sinewave Indicator erstmals 1996 vor; er beruht darauf, zyklische Datenschwünge auf eine Sinuswelle zu übertragen und deren Phase künstlich vorzuziehen, um einen vorhersagenden Indikator zu erhalten.
- Der ursprüngliche Sinewave Indicator suchte den Phasenwinkel des dominanten Zyklus mit der besten Korrelation zwischen den Preisdaten und einer theoretischen Sinuswelle des dominanten Zyklus.
- Der Even Better Sinewave Indicator ist eine Variante des Roofing-Filters mit einpoligem Hochpass; seine eindeutigen Signale entstehen durch Normierung der Wellenamplitude auf die Wurzel der Leistung.

## Funktionsweise

- Nach dem modifizierten Roofing-Filter (einpoliger Hochpass, dann SuperSmoother mit kritischer Periode 10 Balken) werden der Drei-Balken-Durchschnitt der Wellenamplitude und der Leistung berechnet; die Leistung ist proportional zum Quadrat der Amplitude.
- Der gemittelte Wellenwert wird durch die Wurzel der gemittelten Leistung geteilt, sodass der Indikator zwischen −1 und +1 schwingt.
- Einzige Eingabe ist der Duration-Parameter; eine kürzere Duration erhöht die Zahl der Trades in einer Zeitspanne und lässt geringfügig früher einsteigen, eine längere hält eine angezeigte Position länger.

## Voraussetzungen


## Anwendung im Trading

- Der Even Better Sinewave Indicator scheint auf Intraday-Futures-Daten gut zu funktionieren, was Ehlers nicht ausführlich untersucht hat: Er nimmt eine Position in der richtigen Richtung ein und bleibt ohne übermäßiges Whipsawing in guten Trades.

## Regeln und Kriterien

- Interpretation des Even Better Sinewave: Long halten, wenn der Indikator nahe +1 ist; short halten (oder flat sein, wenn nur long gehandelt wird), wenn er nahe −1 ist.
- Damit der Sinewave Indicator nützlich ist, muss der Markt im Zyklusmodus sein und die dominante Zyklusperiode mit hinreichender Genauigkeit geschätzt werden.

## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 159–178 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-013-p159-p178|S. 159–178]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 178–197 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-014-p178-p197|S. 178–197]]

## Verwandte Themen
