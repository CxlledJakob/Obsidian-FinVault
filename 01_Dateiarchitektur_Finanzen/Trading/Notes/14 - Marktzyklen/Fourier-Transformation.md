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

# Fourier-Transformation


## Kurzdefinition


## Kernaussagen

- Die nicht-uniforme Fast-Fourier-Transformation ist nützlich, um stark unregelmäßige Zeitreihen zu analysieren.

## Funktionsweise

- Die Fourier-Analyse wird normalerweise auf gleichmäßig verteilte Daten angewandt.
- Für Finanzzeitreihen in chronologischer Zeit verwenden die Autoren eine nicht-uniforme Fast-Fourier-Transformation.
- Weil Marktaktivität in Schüben auftritt, kann eine Finanzzeitreihe nach einem Index der Handelsaktivität abgetastet werden.
- Eine Fourier-Analyse in chronologischer Zeit kann dennoch aufschlussreich sein; dafür wird die nicht-uniforme FFT eingesetzt.

## Voraussetzungen


## Anwendung im Trading

- Als Illustration dient die Fourier-Analyse der Handelspreise von Erdgas-Futures (Song et al. [2014]).
- Die nicht-uniforme FFT wurde zusätzlich auf die Handelsvolumina angewandt.

## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Die höchste Amplitude lag 2012 bei der Frequenz 366 statt der erwarteten 365, weil 2012 ein Schaltjahr war; das validiert, dass die nicht-uniforme FFT die erwarteten Signale erfasst.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 362–381 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-020-p362-p381|S. 362–381]]

## Verwandte Themen

- Als Beispiel für eine Abtastung nach Handelsaktivität nennt der Text VPIN, das Finanzreihen als Funktion des gehandelten Volumens abtastet.
