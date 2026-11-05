---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/14 - Marktzyklen/14 - Marktzyklen|14 - Marktzyklen]]"
weitere_hauptthemen: []
unterthema: "Zyklische Analyse"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Fourier-Transformation


## Kurzdefinition


## Kernaussagen

- Die nicht-uniforme Fast-Fourier-Transformation ist nützlich, um stark unregelmäßige Zeitreihen zu analysieren.
- Die Spektraldichte f von omega eines fraktional differenzierten Prozesses ist die Fourier-Transformierte seiner Autokorrelationsfunktion.
- Für minus 0,5 kleiner d kleiner 0,5 erfüllt sie f von omega ungefähr omega hoch minus 2d, wenn omega gegen 0 geht; omega liegt im Intervall von 0 bis 2 pi.
- Das Bispektrum einer Zeitreihe ist die Fourier-Transformierte ihrer Momente dritter Ordnung.
- Für eine stationäre Reihe x_t ist das Moment dritter Ordnung c(u, v) = g Σ_{k=−∞}^{∞} ψ_k ψ_{k+u} ψ_{k+v}, mit g = E(a³_t), ψ_0 = 1 und ψ_k = 0 für k < 0.
- Die Fourier-Transformierte lautet b_3(w1, w2) = [g / (4π²)] Γ[−(w1+w2)] Γ(w1) Γ(w2), und die Spektraldichte ist p(w) = (σ²_a / 2π) |Γ(w)|².
- Daraus folgt, dass das normierte Bispektrum b(w1, w2) = |b_3(w1, w2)|² / [p(w1) p(w2) p(w1+w2)] für eine lineare Reihe über alle Frequenzen konstant ist.
- Für eine lineare gaußsche Reihe ist E(a³_t) = g = 0, sodass das Bispektrum bei allen Frequenzen (w1, w2) null ist.
- Der Bispektraltest schätzt b(w1, w2) auf einem geeignet gewählten Gitter und prüft die Konstanz mit einer Statistik ähnlich Hotellings T²; er testet damit Linearität und Gaußheit.
- Begrenzte Erfahrung zeigt, dass der Test bei großem Stichprobenumfang eine brauchbare Power hat; Details geben Priestley (1988), Subba Rao und Gabr (1984) und Hinich (1982).
- In technischen Kreisen gilt FFT (Fast Fourier Transform) fast als Synonym für Frequenzmessung, daher wird erwartet, dass Fourier-Transformationen die Methode der Wahl zur Messung von Marktzyklen sind.
- Die praktische Berechnung einer DFT für Marktdaten missachtet die theoretischen Voraussetzungen.
- Trotz aller Zugeständnisse an die reine Theorie ist die DFT-Spektralschätzung gut mit dem bevorzugten Autokorrelationsperiodogramm vergleichbar (Abbildung 9.2).
- Die DFT-Berechnung sollte eine Kompensation für Spectral Dilation enthalten.

## Funktionsweise

- Die Fourier-Analyse wird normalerweise auf gleichmäßig verteilte Daten angewandt.
- Für Finanzzeitreihen in chronologischer Zeit verwenden die Autoren eine nicht-uniforme Fast-Fourier-Transformation.
- Weil Marktaktivität in Schüben auftritt, kann eine Finanzzeitreihe nach einem Index der Handelsaktivität abgetastet werden.
- Eine Fourier-Analyse in chronologischer Zeit kann dennoch aufschlussreich sein; dafür wird die nicht-uniforme FFT eingesetzt.
- Beim Autokorrelationsperiodogramm wird die Zyklusinformation mit einer diskreten Fourier-Transformation (DFT) der Autokorrelationsergebnisse mit minimal drei Bars Mittelung gewonnen.
- Die DFT erfolgt, indem die Autokorrelation jedes Lags mit Kosinus und Sinus jeder interessierenden Periode korreliert wird; die Summe der Quadrate beider Teile ergibt die relative Leistung je Periode nach A² = A²·sin²(x) + A²·cos²(x).
- Im Code werden Kosinus- und Sinusteil für Perioden von 10 bis 48 über die Lags N von 3 bis 48 aufsummiert.
- Weil die Leistungsmessung von Bar zu Bar stark schwanken kann, wird sie je Periode mit einer EMA geglättet; im Code mit dem Gewicht 0,2 für den neuen und 0,8 für den vorigen Wert.
- Ehlers berechnet eine gleitende diskrete Fourier-Transformation (DFT): Jede Berechnung ist eine Blockrechnung über das historische Datenfenster, und die gesamte Blockrechnung wird für jeden folgenden Balken wiederholt.
- Die DFT wird für Trader in Zyklusperioden statt in Frequenzen berechnet: Ein 20-Balken-Zyklus ist greifbar, die entsprechende Frequenz von 0,05 Zyklen pro Balken hat keine besondere Bedeutung.
- Ein weiteres Schlüsselmerkmal, das die DFT brauchbar macht, ist die Darstellung der Spektralschätzung als Heatmap.
- Die DFT korreliert die Daten über das gewählte Fenster mit Kosinus und Sinus jeder interessierenden Periode. Die Summe der Quadrate beider korrelierten Werte ist die relative Leistung bei der Periode, nach A² = A²sin²(x) + A²cos²(x).
- Einzige Nutzereingabe des DFT-Codes ist, ob Spectral Dilation kompensiert wird; Standard ist die Kompensation. Die Standard-Fensterlänge ist 48 Balken, eine volle Periode der längsten berechneten Zyklusperiode.
- Vor der DFT werden die Daten in einem Hochpass mit 48-Balken-Grenzperiode vorgefiltert und dann im SuperSmoother mit 10-Balken-Grenzperiode geglättet, passend zur längsten und kürzesten interessierenden Periode.
- Bei der Kompensation wird die Wellenamplitude jeder Periode durch die Periode geteilt; ist die Kompensation ausgeschaltet, wird durch 1 geteilt, also nicht kompensiert.
- Eine automatische Verstärkungsregelung (AGC) mit schnellem Anstieg und langsamem Abklingen normiert die Spektralkomponenten auf Leistungsbasis; der Abklingfaktor ist die Wurzel aus 0,991, also 0,995. Ist die aktuelle Leistung größer als MaxPwr, wird MaxPwr sofort darauf gesetzt, sonst klingt MaxPwr auf 0,995 seines Vorwerts ab.

## Voraussetzungen

- Fourier-Transformationen haben drei Grundvoraussetzungen: Die Datenstichprobe repräsentiert eine unendlich lange Datenreihe, die Daten sind über die Stichprobe stationär (unveränderliche Eigenschaften), und nur eine ganzzahlige Anzahl von Zyklen über die Stichprobenlänge kann analysiert werden, um Endeffekte zu vermeiden.
- Bei 64 Balken ist die kleinste ganzzahlige Zyklenzahl eins (64-Balken-Zyklus); die nächsten zulässigen Perioden sind 64/2 = 32, 64/3 = 21,3 und 64/4 = 16 Balken usw. Die kürzeste zulässige Periode ist ein Zwei-Balken-Zyklus, weil kürzere Perioden das Nyquist-Kriterium von mindestens zwei Abtastwerten pro Zyklus verletzen.

## Anwendung im Trading

- Als Illustration dient die Fourier-Analyse der Handelspreise von Erdgas-Futures (Song et al. [2014]).
- Die nicht-uniforme FFT wurde zusätzlich auf die Handelsvolumina angewandt.

## Regeln und Kriterien


## Risiken und Grenzen

- Viele Verfahren zur Spektralmessung von Marktdaten, darunter Wavelets, benötigen analytische Daten, die Tradern nicht leicht zugänglich sind, und keines davon kompensiert Spectral Dilation.
- Marktzyklen sind flüchtig: Sie kommen und gehen und ändern ihre Periode. Das ist mit den Voraussetzungen der unendlich langen Datenreihe und der Stationarität nicht vereinbar.
- Es ist unrealistisch zu erwarten, dass ein relativ kurzer 12-Balken-Marktzyklus über eine relativ kurze Stichprobe von 64 Balken in Amplitude und Frequenz konstant bleibt.
- Selbst bei erfüllter Stationarität liefert die kurze Stichprobe eine sehr schlechte Messauflösung: Die nächsten Spektrallinien zwischen einem 16-Balken- und einem 21,3-Balken-Zyklus ergeben eine Auflösung von 5 Balken, 31 Prozent relativ zum 16-Balken-Zyklus.
- Die Auflösung lässt sich nur durch eine längere Stichprobe verbessern. Das verschärft die Stationaritätsprobleme, mittelt kurzfristige Ergebnisse über den längeren Zeitraum aus und erhöht die Latenz des Messergebnisses, also die Verzögerung.
- In der Beispielrechnung der DFT (Abbildung 9.1) sind deutlich Harmonische bei der Hälfte und einem Drittel der stärkeren dominanten Zyklusperiode vorhanden.

## Beispiele

- Die höchste Amplitude lag 2012 bei der Frequenz 366 statt der erwarteten 365, weil 2012 ein Schaltjahr war; das validiert, dass die nicht-uniforme FFT die erwarteten Signale erfasst.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 362–381 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-020-p362-p381|S. 362–381]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 115–134 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-007-p115-p134|S. 115–134]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 229–248 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-013-p229-p248|S. 229–248]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 97–116 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-009-p097-p116|S. 97–116]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 121–140 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-011-p121-p140|S. 121–140]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 216–235 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-016-p216-p235|S. 216–235]]

## Verwandte Themen

- Als Beispiel für eine Abtastung nach Handelsaktivität nennt der Text VPIN, das Finanzreihen als Funktion des gehandelten Volumens abtastet.
