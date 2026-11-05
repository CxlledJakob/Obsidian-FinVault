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
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 115–134 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-007-p115-p134|S. 115–134]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 229–248 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-013-p229-p248|S. 229–248]]

## Verwandte Themen

- Als Beispiel für eine Abtastung nach Handelsaktivität nennt der Text VPIN, das Finanzreihen als Funktion des gehandelten Volumens abtastet.
