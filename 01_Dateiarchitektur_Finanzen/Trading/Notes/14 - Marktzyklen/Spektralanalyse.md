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
aktualisiert: 2026-10-30
---

# Spektralanalyse


## Kurzdefinition


## Kernaussagen

- Die Fourier-Analyse des Marktes für Erdgas-Futures zeigt starke Hinweise auf Hochfrequenzhandel.
- Die Fourier-Komponenten hoher Frequenzen werden in den jüngeren Jahren prominenter und sind viel stärker, als die Struktur des Marktes erwarten ließe.
- Die Fourier-Analyse der Handelsvolumina liefert weitere Hinweise auf algorithmischen Handel und auf eine stärkere Präsenz in jüngeren Jahren.

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

## Verwandte Themen
