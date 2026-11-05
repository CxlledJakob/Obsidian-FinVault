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

# Zyklusamplitude


## Kurzdefinition


## Kernaussagen

- Ein Bandpassfilter nach den Gleichungen 5-1 und 5-2 zeigt die Amplitude der zyklischen Swings in den Eingangsdaten genau an.
- Die Amplitude dieser Swings variiert zwischen Aktien, weil die Preise von Pennystocks bis über 100 Dollar je Aktie reichen; ein Pennystock kann wegen der viel kleineren Basis keinen so großen Swing haben wie ein Blue Chip.
- Die Amplitude des Marktdatenspektrums ist nicht flach (Spectral Dilation), und Trader müssen das beim Einsatz von Filtern berücksichtigen.
- Jährliche Zyklusschwankungen sind größer als monatliche, monatliche größer als tägliche und tägliche größer als stündliche (Spectral Dilation). Die Schwankungsgröße ist ungefähr linear proportional zur Zyklusperiode.
- Es ist unrealistisch zu erwarten, dass ein relativ kurzer 12-Balken-Marktzyklus über eine Stichprobe von 64 Balken in Amplitude und Frequenz konstant bleibt.

## Funktionsweise

- Die automatische Verstärkungsregelung (AGC) soll ein einheitliches Indikatorbild unabhängig von der Spanne der Preisswings liefern. Sie teilt den aktuellen Wert durch den Betrag des jüngsten maximalen Swings, sodass die normierte Wellenform ein Maximum von 1 und ein Minimum von −1 hat.
- Ehlers nutzt eine Fast-Attack-Slow-Decay-AGC: Der Normierungsfaktor darf vor dem Vergleich mit dem nächsten Wert etwas abklingen, damit nicht auf den größten Swing der gesamten Historie normiert wird.
- Ist der nächste Wert größer als der Normierungsfaktor, wird der Normierungsfaktor sofort auf diesen Wert gesetzt; ist er kleiner, klingt der Faktor um einen weiteren kleinen Betrag ab und wird mit dem dritten Wert verglichen, und so fort.
- Ohne Zurücksetzen klingt der Normierungsfaktor exponentiell ab: Bei Abklingfaktor K für den ersten Wert ist er K² für den nächsten und K³ für den dritten Wert.
- Für theoretische Sinussignale ist die effektive Verstärkung der AGC der Abklingfaktor hoch die halbe Periode: Gain = K^(Period/2).
- Im Code wird der Normierungsfaktor als Peak = 0,991 * Peak[1] fortgeschrieben, bei AbsValue(BP) > Peak auf AbsValue(BP) gesetzt, und bei Peak ungleich 0 ist Signal = BP / Peak.
- In der DFT und im Kammfilter wird die Wellenamplitude jeder Periode durch die Periode geteilt, um Spectral Dilation zu kompensieren.
- Eine automatische Verstärkungsregelung (AGC) mit schnellem Anstieg und langsamem Abklingen normiert die Spektralkomponenten und minimiert die Varianz der Spektralleistung über die Zeit; auf Leistungsbasis ist der Abklingfaktor 0,995 statt 0,991 auf Amplitudenbasis.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Über den Bereich von 10 bis 48 Bars ist das Verstärkungsverhältnis K^24 / K^5 = K^19. Ehlers wählt einen Verstärkungsabfall von 1,5 dB, also Ratio = 10^(−0,075) = 0,841, und daraus K = 0,841^(1/19) = 0,991.
- Den Abklingfaktor 0,991 verwendet Ehlers im restlichen Buch, außer wenn die AGC zur Amplitudenkompensation als Funktion der Zyklusperiode eingesetzt wird.

## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 55–70 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-006-p055-p070|S. 55–70]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 121–140 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-011-p121-p140|S. 121–140]]

## Verwandte Themen
