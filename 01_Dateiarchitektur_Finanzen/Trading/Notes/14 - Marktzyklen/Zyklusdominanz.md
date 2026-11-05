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

# Zyklusdominanz


## Kurzdefinition

- Der dominante Zyklus ist die mittlere Periode, um die sich die Spektralleistungen zentrieren.

## Kernaussagen

- Die bevorzugte Methode zur Berechnung des dominanten Zyklus ist das Autokorrelationsperiodogramm.
- Der Even Better Sinewave Indicator verzichtet vollständig auf Zyklusmessungen und stützt sich auf eine starke Normierung der Wellenform am Ausgang eines modifizierten Roofing-Filters.
- Ehlers zeigt drei Wege, die zeitvariable dominante Zyklusperiode mit analytischen Signalen zu messen: Dual Differentiator, Phase Accumulation und Homodyne. Alle messen im Kern die momentane Phase und summieren die Phasen zur Schätzung der Zyklusperiode.
- Ein weit überlegener Ansatz zur Berechnung des dominanten Zyklus ist das Autokorrelations-Periodogramm.
- Analytische Signale erlauben sehr schnelle Messungen der dominanten Zyklusperiode über die Änderungsrate des Phasenwinkels: Ändert sich der Winkel um 18 Grad pro Bar, beträgt der dominante Zyklus 20 Bars, weil das 360 Grad über 20 Bars ergibt.

## Funktionsweise

- Der Bandpassfilter kann als relativ einfache Messung des dominanten Zyklus genutzt werden.
- Ein Zyklus ist vollständig, wenn die Wellenform seit dem letzten Nulldurchgang zweimal die Null kreuzt; jeder Nulldurchgang markiert also eine halbe Zyklusperiode, und die dominante Zyklusperiode ist das Doppelte des Abstands zwischen aufeinanderfolgenden Nulldurchgängen.
- Im Code wird bei jedem Nulldurchgang DC = 2 * counter gesetzt; DC wird nach oben auf 1,25 * DC[1] und nach unten auf 0,8 * DC[1] begrenzt, und DC wird nicht kleiner als 6.
- Ehlers ermittelt den dominanten Zyklus aus der Spektralschätzung des Autokorrelationsperiodogramms mit einem Schwerpunkt-Algorithmus (Center of Gravity, CG).
- Der CG-Algorithmus summiert die Y-Werte und unabhängig davon die Produkte X·Y; der Quotient aus zweiter und erster Summe ist die mittlere Position auf der X-Achse. Beim dominanten Zyklus sind die Y-Werte die Leistungen und die X-Werte die Perioden.
- Im Code gehen nur Perioden von 10 bis 48 Bars ein, deren normierte Leistung mindestens 0,5 beträgt; der dominante Zyklus wird nur berechnet, wenn die Leistungssumme ungleich null ist.
- Der dominante Zyklus wird aus der Spektralschätzung mit einem Schwerpunkt-Algorithmus (Center of Gravity, CG) gewonnen: Die Y-Werte und unabhängig davon die Produkte X mal Y werden summiert; die zweite Summe geteilt durch die erste ergibt die mittlere Position entlang der X-Achse.
- Beim dominanten Zyklus sind die Y-Werte die Leistungen und die X-Werte die Perioden; der Algorithmus berechnet also die mittlere Periode, um die sich die Leistungen konzentrieren. Das ist der dominante Zyklus.
- Im Code gehen nur Perioden mit normierter Leistung von mindestens 0,5 in die Schwerpunktberechnung ein.
- Beim Dual Differentiator ist der Phasenwinkel der Arkustangens des Verhältnisses von imaginärer zu reeller Komponente und die Kreisfrequenz die Änderungsrate der Phase. Im Code gilt Period = 6,28318 · (Real² + Imag²) / (−Real · QDot + Imag · IDot), begrenzt auf 8 bis 48, danach mit einem SuperSmoother geglättet.
- Bei der Phase Accumulation wird je Sample die Phase als Arkustangens von Quadratur zu In-Phase gemessen, die Phasendifferenz zwischen aufeinanderfolgenden Samples gebildet und rückwärts aufsummiert; erreicht die Summe 360 Grad, ist im Mittel ein voller Zyklus durchlaufen.
- Im Phase-Accumulation-Code wird über count von 0 bis 40 summiert; die momentane Periode ist der count, bei dem die Summe erstmals 360 übersteigt. Ist sie 0, wird der Vorwert übernommen, danach wird geglättet.
- Homodyne bedeutet, dass das Signal mit sich selbst multipliziert wird, genauer das Signal des aktuellen Bars mit dem komplex konjugierten Signal des Vorbars. Weil der Zeitabstand ein Bar ist, liefert das Produkt das Amplitudenquadrat und die Kreisfrequenz 2π / Period.
- Bei der Homodyne-Methode wird der dominante Zyklus berechnet, indem 2π durch das Verhältnis von imaginärer zu reeller Komponente geteilt wird, weil bei kleinem Winkel Winkel, Tangens und Arkustangens ungefähr gleich sind.

## Voraussetzungen


## Anwendung im Trading

- Der dominante Zyklus ändert sich mit der Zeit und kann zum automatischen Abstimmen anderer Indikatoren wie Bandpassfilter, CCI, RSI oder Stochastic genutzt werden.
- Im Periodogramm für Dollar General verläuft der berechnete dominante Zyklus als blaue Linie ungefähr durch die Mitte der stärksten Spektralkomponenten.
- Der dominante Zyklus ändert sich mit der Zeit und kann genutzt werden, um andere Indikatoren wie Bandpassfilter, Commodity Channel Index (CCI), Relative Strength Index (RSI) und Stochastic automatisch abzustimmen.
- Ehlers verwendet im weiteren Buch das Autokorrelationsperiodogramm zur Berechnung des dominanten Zyklus.
- Schlüsselparameter von Stochastic, RSI, CCI und Bandpassfilter ist die Rückschauperiode, die üblicherweise fest ist. Weil sich die gemessene Zyklusperiode ändert, ist es sinnvoll, diese Indikatoren an die gemessene Zyklusperiode anzupassen.
- Beobachtete handelbare Marktzyklen halten meist eine kurze Zeit an; auf die gemessene Zyklusperiode abgestimmte Indikatoren sind deshalb für die aktuellen Bedingungen optimiert und können sogar vorhersagende Eigenschaften haben.
- Der mit dem Autokorrelationsperiodogramm gemessene dominante Zyklus setzt die Rückschauperiode der Indikatoren dynamisch; die Indikatorcodes sind zudem so verändert, dass die Effekte der Spectral Dilation entfernt werden.
- Abstimmung auf den dominanten Zyklus: RSI über die halbe Periode, Stochastic und CCI über die volle Periode, Bandpassfilter auf 90 Prozent der Periode.

## Regeln und Kriterien

- Für die Messung soll der Durchlassbereich des Bandpassfilters verbreitert werden, damit die Selektivität des Filters die Messung nicht verzerrt. Eine Eingangsbandbreite von 0,7 ergibt einen etwa oktavbreiten Durchlassbereich.
- Bei Mittenperiode 20 und relativer Bandbreite 0,7 beträgt die Bandbreite 14, und der Durchlassbereich reicht von 13- bis 27-Bar-Perioden.
- Ein Hochpassfilter, eine Oktave unter der Halbbandbreitenkante des Bandpassfilters abgestimmt, ist zwingend, damit der gefilterte Ausgang nominell mittelwertfrei ist; ohne Mittelwert null können die Nulldurchgänge erheblich fehlerhaft sein.
- Weil die Messung von Nulldurchgang zu Nulldurchgang stark schwanken kann, begrenzt der Code die Änderung zwischen Messungen auf höchstens 25 Prozent.
- Wird der dominante Zyklus über einen relativ kleinen Periodenbereich gesucht, kann Spectral Dilation ignoriert werden; wird er aus Daten mit mehreren Oktaven von Zyklusperioden extrahiert, muss sie kompensiert werden.
- Ist die Länge ein Eingabeparameter eines Indikators, lässt sich der Indikator oft optimieren, indem die Länge auf die dominante Zyklusperiode oder einen Bruchteil davon abgestimmt wird.
- Der Bandpassfilter wird optimiert, indem er auf 90 Prozent der gemessenen dominanten Zyklusperiode abgestimmt wird; das liefert etwa 60 Grad Phasenvoreilung.
- Damit der Sinewave Indicator nützlich ist, muss der Markt im Zyklusmodus sein und die Periode des dominanten Zyklus mit hinreichender Genauigkeit geschätzt werden.

## Risiken und Grenzen

- Die Messung der dominanten Zyklusperiode über Nulldurchgänge der Bandpasswelle ist einfach, aber nicht unbedingt die genaueste Methode; genauere Verfahren untersuchen den gesamten Spektralgehalt der Daten.
- Weil die Glättungslänge meist kürzer als ein voller Zyklus ist, sind die Ergebnisse der Hilbert-Methoden recht verrauscht und nur marginal handelstauglich; Ehlers nimmt den Code nur der Vollständigkeit halber auf.
- Die Algorithmen funktionieren auf rauschfreien theoretischen Wellenformen recht gut. Ehlers vermutet, dass das Rauschen von Sample zu Sample die Berechnung der Phasenänderungsrate überdeckt und die Ergebnisse im Grunde wertlos macht.
- Bei der Homodyne-Methode kann der Winkel idealerweise nicht negativ sein, weil die Zeit nicht rückwärts läuft; der Glättungsfilter dient vor allem dazu, die durch Rauschen erratischen Berechnungen zu überdecken.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 55–70 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-006-p055-p070|S. 55–70]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 97–116 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-009-p097-p116|S. 97–116]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 121–140 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-011-p121-p140|S. 121–140]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 140–159 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-012-p140-p159|S. 140–159]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 159–178 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-013-p159-p178|S. 159–178]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 178–197 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-014-p178-p197|S. 178–197]]

## Verwandte Themen
