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

# Spektralanalyse


## Kurzdefinition


## Kernaussagen

- Die Fourier-Analyse des Marktes für Erdgas-Futures zeigt starke Hinweise auf Hochfrequenzhandel.
- Die Fourier-Komponenten hoher Frequenzen werden in den jüngeren Jahren prominenter und sind viel stärker, als die Struktur des Marktes erwarten ließe.
- Die Fourier-Analyse der Handelsvolumina liefert weitere Hinweise auf algorithmischen Handel und auf eine stärkere Präsenz in jüngeren Jahren.
- Die Spektraldichte des fraktional differenzierten Prozesses ist die Fourier-Transformierte seiner Autokorrelation und verhält sich für omega gegen 0 wie omega hoch minus 2d, mit omega im Intervall von 0 bis 2 pi.
- Dieses Spektrum divergiert gegen unendlich, wenn die Frequenz gegen 0 geht.
- Die Spektraldichte eines stationären ARMA-Prozesses bleibt dagegen für alle Frequenzen von 0 bis 2 pi beschränkt.
- Der fraktionale Differenzenparameter d lässt sich per Maximum Likelihood oder per Regression des logarithmierten Periodogramms bei den niedrigen Frequenzen schätzen.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- Aktivitäten bei der Frequenz einmal pro Minute sind erheblich höher als bei den benachbarten Frequenzen.
- Die Stärke der Aktivität bei einmal pro Minute ist mehr als zehnmal so hoch wie bei den Nachbarfrequenzen.
- Die Aktivität ist bei genau einmal pro Minute sehr präzise abgegrenzt, was auf absichtlich konstruierte automatisierte Ereignisse hinweist.

## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Abbildung 22.10 zeigt das Fourierspektrum der Handelspreise von Erdgas-Futures im Jahr 2012; die vertikale Achse ist logarithmisch.
- Die nicht-uniforme FFT weist dort starke Aktivität einmal täglich (Frequenz 366), zweimal täglich (Frequenz 732) und einmal pro Minute (Frequenz 527040 = 366*24*60) aus.
- Erwartet wurde eine große Amplitude bei Frequenz 365; das Maximum lag bei 366, weil 2012 ein Schaltjahr war.
- Die zweit- und dritthöchsten Amplituden haben die Frequenzen 732 und 52, also zweimal täglich und einmal wöchentlich.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 362–381 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-020-p362-p381|S. 362–381]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 115–134 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-007-p115-p134|S. 115–134]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 84–96 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-008-p084-p096|S. 84–96]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 97–116 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-009-p097-p116|S. 97–116]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 116–120 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-010-p116-p120|S. 116–120]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 121–140 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-011-p121-p140|S. 121–140]]

## Verwandte Themen
