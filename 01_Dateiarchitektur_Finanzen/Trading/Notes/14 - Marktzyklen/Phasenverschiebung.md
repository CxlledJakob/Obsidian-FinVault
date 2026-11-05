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

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- Ein zweiter Hochpassfilter, seriell an den Ausgang des Bandpassfilters geschaltet und auf dessen hochfrequente kritische Frequenz abgestimmt, erzeugt eine vorauslaufende Wellenform, die dem Bandpassausgang ähnelt und eine Phasenvorlauf-Charakteristik hat.
- Eine vorauslaufende Wellenform über die Änderungsrate des Bandpassausgangs wäre zu erratisch, um als Handelsindikator zu taugen.
- Der vorauslaufende Trigger kreuzt den Bandpassausgang genau an den Hochs und Tiefs der Wellenform, außer wenn die Daten trenden.

## Regeln und Kriterien


## Risiken und Grenzen


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
