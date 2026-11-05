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

# Phasenverschiebung


## Kurzdefinition


## Kernaussagen

- Ist die Mittenperiode eines Bandpassfilters auf eine statische Sinuswelle mit derselben Periode abgestimmt, hat der Ausgang überhaupt keine Verzögerung.
- Die Phasenverschiebung über die Bandbreite eines Bandpassfilters ist unvermeidbar.
- Die Phasenverschiebung verdoppelt sich jedes Mal, wenn die Zahl der Pole in der Übertragungsfunktion verdoppelt wird. Deshalb soll im Trading der einfachste mögliche Filter genutzt werden, um Verzerrungen durch Phasenverschiebung zu minimieren.
- Ein Bandpassfilter, der auf eine kürzere Periode als den dominanten Zyklus abgestimmt ist, liefert einen Ausgang, der dem Swing der Eingangsdaten vorausläuft.
- Ein Bandpassfilter, der auf eine längere Periode als den dominanten Zyklus abgestimmt ist, liefert einen Ausgang, der dem Swing der Eingangsdaten hinterherläuft.
- Die Kosinuswelle kreuzt null, wenn die Sinuswelle ihr Maximum mit Steigung null erreicht. Die Kosinuswelle stellt die Änderungsrate der Sinuswelle dar.
- Die Quadraturkomponente eines modifizierten Hilbert-Transformers läuft der reellen Ausgabe voraus wie eine Kosinuswelle einer Sinuswelle; in diesem Sinn ist er prädiktiv.
- In-Phase- und Quadraturkomponente stehen als Vektoren in der komplexen Ebene im rechten Winkel zueinander.

## Funktionsweise

- Ein Bandpassfilter erhält einen voreilenden Phasengang, wenn er auf eine kürzere Periode abgestimmt wird als die Periode des gemessenen Zyklus.
- Im adaptiven Bandpass ist die Bandbreite 0,3, also 30 Prozent der abgestimmten Mittenperiode, die halbe Bandbreite damit 15 Prozent. Der Filter wird 10 Prozent zur kürzeren Periode hin vom dominanten Zyklus verstimmt, sodass die Daten noch in der Bandbreite liegen.
- Diese Verstimmung ergibt eine Phasenvoreilung gegenüber dem dominanten Zyklus in der Größenordnung von 60 Grad, also einem Sechstel eines Zyklus. Bei einem 18-Balken-Zyklus ergibt sich ein Vorlauf von 3 Balken; das ist nicht groß, aber signifikant.
- Die Triggerlinie des adaptiven Bandpasses ist 90 Prozent der Amplitude der Bandpasslinie, um einen Balken verzögert. Die Linienkreuzungen erfolgen nach dem Hoch des Bandpasses, aber die Phasenvoreilung sorgt für ein rechtzeitiges Signal.
- Kein technischer Indikator ist vorhersagend, alle Signale verzögern; weil beobachtete Zyklen oft eine kurze Zeit weiterlaufen, kann man zyklische Schwünge auf eine Sinuswelle übertragen und deren Phase künstlich vorziehen, um einen vorhersagenden Indikator zu erhalten.
- Im Code des adaptiven Bandpasses wird das Signal als BP geteilt durch einen mit 0,991 abklingenden Spitzenwert normiert; der Lead ist 1,3 · (Signal + Signal[1] − Signal[2] − Signal[3]) / 4 und wird über einen mit 0,93 abklingenden Spitzenwert auf 0,7 normiert.
- Die Konvolution wird um vier Balken nach links verschoben, um den Indikator besser mit dem tatsächlichen Wendepunkt in Deckung zu bringen, weil für die kürzeste Berechnung eine endliche Datenmenge nötig ist; das ähnelt einem zentrierten gleitenden Durchschnitt.
- Die Ein-Bar-Differenz der reellen Komponente liefert die für die imaginäre Komponente nötige Phasenquadratur, analog zur Ableitung einer Sinuswelle zu einer Kosinuswelle.
- Ein FIR-Filter mit ungerader Elementzahl N verzögert um (N − 1) / 2 Bars; beim 23-Element-Hilbert-Transformer sind das 11 Bars, beim Dreielement-Filter [1 0 −1] ein Bar.
- Die Homodyne-Methode multipliziert das Signal des aktuellen Bars mit dem komplex konjugierten Signal des Vorbars; die komplex Konjugierte ist eine komplexe Zahl mit umgekehrtem Vorzeichen der imaginären Komponente.

## Voraussetzungen


## Anwendung im Trading

- Ein zweiter Hochpassfilter, seriell an den Ausgang des Bandpassfilters geschaltet und auf dessen hochfrequente kritische Frequenz abgestimmt, erzeugt eine vorauslaufende Wellenform, die dem Bandpassausgang ähnelt und eine Phasenvorlauf-Charakteristik hat.
- Eine vorauslaufende Wellenform über die Änderungsrate des Bandpassausgangs wäre zu erratisch, um als Handelsindikator zu taugen.
- Der vorauslaufende Trigger kreuzt den Bandpassausgang genau an den Hochs und Tiefs der Wellenform, außer wenn die Daten trenden.

## Regeln und Kriterien

- Signifikante Handelssignale verlangen zusätzlich, dass die Linienkreuzung oberhalb von +0,7 oder unterhalb von −0,7 der Referenzlinien erfolgt.

## Risiken und Grenzen

- Adaptive gleitende Durchschnitte wie Kaufmans KAMA und Chandes VIDYA passen sich an Volatilitätsänderungen an; sie reagieren per Definition auf Preisänderungen und kommen damit zu spät.
- Im klassischen Hilbert-Code muss die imaginäre Kurve um 11 Bars nach links verschoben werden; für den Handel müsste Real um 11 Bars verzögert werden, um die richtige Beziehung zu Imag zu haben.
- Eine Glättung der imaginären Komponente mit einem SuperSmoother führt mehrere Bars Lag ein und zerstört ihre Orthogonalität zur reellen Komponente.

## Beispiele

- Ein 20-Bar-Bandpassfilter mit 30 Prozent Bandbreite auf 20-Bar-Daten hat keine Verzögerung.
- Wird der Bandpassfilter auf seine Halbleistungsperiode von 17 Bars abgestimmt, ist der 20-Bar-Datenzyklus länger als die abgestimmte Frequenz, und der Ausgang hat 65 Grad Verzögerung (Abstimmung 15 Prozent zu lang laut Abbildungstitel).
- Wird der Bandpassfilter auf seine andere Halbleistungsperiode von 23 Bars abgestimmt, ist der 20-Bar-Datenzyklus kürzer als die abgestimmte Frequenz, und der Ausgang hat 65 Grad Vorlauf (Abstimmung 15 Prozent zu kurz laut Abbildungstitel).

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 55–70 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-006-p055-p070|S. 55–70]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 140–159 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-012-p140-p159|S. 140–159]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 159–178 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-013-p159-p178|S. 159–178]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 178–197 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-014-p178-p197|S. 178–197]]

## Verwandte Themen
