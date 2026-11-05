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
- Sinus- und Kosinuswelle lassen sich als Vektoren in der komplexen Ebene mit reeller und imaginärer Achse darstellen. Die Wellen im Zeitbereich sind Projektionen auf die imaginäre Achse, während die Vektoren gegen den Uhrzeigersinn rotieren.
- Ein voller Zyklus im Zeitbereich ist abgeschlossen, wenn die Vektoren in der komplexen Ebene volle 360 Grad rotiert sind.
- Die Sinuswelle startet bei null und steigt zu ihrem Maximum, die Kosinuswelle startet bei ihrem Maximum und nimmt ab.
- Der Phasenwinkel wird aus dem analytischen Signal als Arkustangens des Verhältnisses von imaginärer zu reeller Komponente berechnet; die Kreisfrequenz ist die Änderungsrate der Phase.

## Funktionsweise

- Nach dem modifizierten Roofing-Filter (einpoliger Hochpass, dann SuperSmoother mit kritischer Periode 10 Balken) werden der Drei-Balken-Durchschnitt der Wellenamplitude und der Leistung berechnet; die Leistung ist proportional zum Quadrat der Amplitude.
- Der gemittelte Wellenwert wird durch die Wurzel der gemittelten Leistung geteilt, sodass der Indikator zwischen −1 und +1 schwingt.
- Einzige Eingabe ist der Duration-Parameter; eine kürzere Duration erhöht die Zahl der Trades in einer Zeitspanne und lässt geringfügig früher einsteigen, eine längere hält eine angezeigte Position länger.
- Der Code berechnet die Phase als ArcTangent(|Imag / Real|), wenn |Real| > 0, und löst die Mehrdeutigkeit nach Quadrant auf: Real < 0 und Imag > 0 ergibt 180 − Phase, Real < 0 und Imag < 0 ergibt 180 + Phase, Real > 0 und Imag < 0 ergibt 360 − Phase.
- Die Phasendifferenz ist DeltaPhase = Phase[1] − Phase. Beim Umlauf, wenn Phase[1] < 90 und Phase > 270, gilt DeltaPhase = 360 + Phase[1] − Phase.
- Der Code begrenzt DeltaPhase auf Werte von 10 bis 48, laut Kommentar innerhalb der Grenzen von 10-Bar- und 48-Bar-Zyklen.

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
