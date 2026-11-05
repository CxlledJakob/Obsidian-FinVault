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

- Ehlers prägte den Begriff Spectral Dilation für den Effekt, dass längere Zyklusperioden in Marktdaten aufgrund ihrer fraktalen Natur entsprechend größere Amplitudenschwankungen haben.

## Kernaussagen

- Die Fourier-Analyse des Marktes für Erdgas-Futures zeigt starke Hinweise auf Hochfrequenzhandel.
- Die Fourier-Komponenten hoher Frequenzen werden in den jüngeren Jahren prominenter und sind viel stärker, als die Struktur des Marktes erwarten ließe.
- Die Fourier-Analyse der Handelsvolumina liefert weitere Hinweise auf algorithmischen Handel und auf eine stärkere Präsenz in jüngeren Jahren.
- Die Spektraldichte des fraktional differenzierten Prozesses ist die Fourier-Transformierte seiner Autokorrelation und verhält sich für omega gegen 0 wie omega hoch minus 2d, mit omega im Intervall von 0 bis 2 pi.
- Dieses Spektrum divergiert gegen unendlich, wenn die Frequenz gegen 0 geht.
- Die Spektraldichte eines stationären ARMA-Prozesses bleibt dagegen für alle Frequenzen von 0 bis 2 pi beschränkt.
- Der fraktionale Differenzenparameter d lässt sich per Maximum Likelihood oder per Regression des logarithmierten Periodogramms bei den niedrigen Frequenzen schätzen.
- Spectral Dilation ist inhärenter Bestandteil von Marktdaten und hat tiefgreifenden Einfluss auf alle technischen Indikatoren; sie wird meist vernachlässigt, weil Indikatoren nicht unter dem Gesichtspunkt ihres Frequenzgehalts betrachtet werden.
- Marktdaten haben eine spektrale Leistungsdichte proportional zu 1/F^α, ihre Amplitude wächst daher mit ungefähr 6 dB pro Oktave.
- Spectral Dilation wird in praktisch allen gängigen technischen Indikatoren ignoriert, was zu fehlerhaften und oft abwegigen Interpretationen des Marktgeschehens geführt hat.
- Spectral Dilation lässt sich korrigieren, indem vor der Berechnung von Indikatoren ein Roofing Filter eingesetzt wird.
- Die lineare Systemtheorie teilt jedes Problem in Eingabe-, Übertragungs- und Ausgabebox; Ehlers ging zunächst davon aus, dass die Ausgabe eines Filters nur die vom Filter definierten Frequenzkomponenten enthält.
- Das Autokorrelationsperiodogramm reagiert schnell: Die Spektralschätzungen bilden sich innerhalb einer halben Zyklusperiode nach ihrem Beginn.
- Das Autokorrelationsperiodogramm schätzt die relative zyklische Leistung als Funktion der Zeit; ohne Zyklen, etwa im Trend, kann die Autokorrelation bei allen Perioden niedrig sein, während frühere Arbeiten die maximale Zyklusamplitude jedes Bars gleich behandelten.
- Weil die Autokorrelation unabhängig von der gemessenen Periode zwischen −1 und +1 begrenzt ist, entfällt beim Autokorrelationsperiodogramm die Kompensation der Spectral Dilation der Zyklusamplitude.
- Die Auflösung der Zyklusmessung des Autokorrelationsperiodogramms ist inhärent hoch und unabhängig von einer Fensterfunktion der Preisdaten.
- Das Spektrum zeigt, dass Marktzyklen evaneszent sind: Sie kommen und gehen und ändern ihre Periodizität im Zeitverlauf.
- Das Autokorrelationsperiodogramm hat die geringste Latenz aller Spektralschätzungen für Marktdaten.
- Das Autokorrelationsperiodogramm schätzt automatisch die gesamte zyklische Leistung in den Daten als Funktion der Zeit.

## Funktionsweise

- Ein Roofing Filter begrenzt den Frequenzgehalt der Eingabe vor dem Indikatoraufbau: Ein Hochpass lässt nur Perioden kürzer als zum Beispiel 48 Bars durch, ein SuperSmoother nur Perioden länger als 10 Bars, zusammen ein breitbandiger Bandpass für 10 bis 48 Bars.
- Ein einpoliger Hochpass dämpft mit 6 dB pro Oktave und gleicht damit nur das fraktale Amplitudenwachstum der längeren Perioden aus; seine Ausgabe enthält diese Frequenzkomponenten weiterhin.
- Der Roofing Filter mit nur einem einpoligen Hochpass hat keinen Nullmittelwert und liegt in Aufwärtstrends über längere Zeit oberhalb von null.
- Ein zweiter Hochpass mit weiteren 6 dB pro Oktave Dämpfung stellt einen nominellen Nullmittelwert her und entfernt zusätzlich Lag aus der Ausgabe des Roofing Filters.
- Die bessere Formulierung des Roofing Filters ist die Reihenschaltung eines zweipoligen Hochpasses mit dem SuperSmoother.
- Ein Roofing Filter stellt einen nahezu nullzentrierten Mittelwert der trendbereinigten Daten her, indem er nur zyklische Komponenten innerhalb seines Durchlassbereichs zur weiteren Analyse weitergibt.
- Das Autokorrelationsperiodogramm nutzt eine Vorfilterung aus 48-Bar-Hochpass und 10-Bar-SuperSmoother, berechnet für jeden Lag eine Pearson-Korrelation und transformiert die Ergebnisse per DFT.
- Eine automatische Verstärkungsregelung (AGC) mit schnellem Anstieg und langsamem Abklingen normiert die Spektralkomponenten: Ist die aktuelle Leistung größer als MaxPwr, wird MaxPwr sofort darauf gesetzt, sonst klingt MaxPwr laut Text auf 0,991 des Vorwerts ab; im Code steht der Faktor 0,995.
- Die normierten Spektralwerte zwischen 0 und 1 werden in Farben umgesetzt: Über 0,5 mischen sich Rot und Grün, bei 1 ergibt sich Gelb, bei 0,5 Rot; unter 0,5 nimmt die Rotsättigung ab bis Schwarz bei 0.
- Ein optionaler, auskommentierter Codeblock erhöht die visuelle Auflösung, indem die Spektralkomponenten potenziert werden; die Wahl des Exponenten ist willkürlich.

## Voraussetzungen


## Anwendung im Trading

- Aktivitäten bei der Frequenz einmal pro Minute sind erheblich höher als bei den benachbarten Frequenzen.
- Die Stärke der Aktivität bei einmal pro Minute ist mehr als zehnmal so hoch wie bei den Nachbarfrequenzen.
- Die Aktivität ist bei genau einmal pro Minute sehr präzise abgegrenzt, was auf absichtlich konstruierte automatisierte Ereignisse hinweist.
- Der Roofing Filter kann selbst ein erfolgreicher technischer Indikator sein; die Grenzperioden für Hoch- und Tiefpass lassen sich als Eingaben je Aktie, ETF oder Future einstellen.
- Kaufsignale am Zyklustief und Verkaufs- bzw. Ausstiegssignale am Zyklushoch werden beim Roofing-Filter-Indikator durch das Kreuzen des Filters mit sich selbst um zwei Bars verzögert markiert.
- Im Beispiel der Abbildung 7.3 sind die LP-Periode willkürlich auf 40 und die HP-Periode auf 80 Bars gesetzt; die Signale sind nicht durch Rechenverzögerung beeinträchtigt.
- Der Roofing-Filter-Indikator gibt sehr gute Orientierung für diskretionäres Trading, für ein gutes mechanisches Handelssystem wären zusätzliche Regeln nötig.
- Für eine normierte Amplitude kann nach der Filt-Berechnung der AGC-Codebaustein aus Kapitel 5 ergänzt werden.
- Das Periodogramm ist eine Zeit-Frequenz-Darstellung (TFR), die Trader leicht nutzen können, indem sie die Farben als Stärke der Spektralkomponenten lesen; die Wissenschaft nutzt dafür Konturplots und Wasserfalldiagramme.

## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Abbildung 22.10 zeigt das Fourierspektrum der Handelspreise von Erdgas-Futures im Jahr 2012; die vertikale Achse ist logarithmisch.
- Die nicht-uniforme FFT weist dort starke Aktivität einmal täglich (Frequenz 366), zweimal täglich (Frequenz 732) und einmal pro Minute (Frequenz 527040 = 366*24*60) aus.
- Erwartet wurde eine große Amplitude bei Frequenz 365; das Maximum lag bei 366, weil 2012 ein Schaltjahr war.
- Die zweit- und dritthöchsten Amplituden haben die Frequenzen 732 und 52, also zweimal täglich und einmal wöchentlich.
- Im Autokorrelationsperiodogramm für Dollar General (DG) über etwa ein Jahr ist die vertikale Skala die Zykluslänge in Bars, sodass die Darstellung für Intraday-, Tages- und Wochendaten gleichermaßen gilt; die Zyklusstärke ist von Gelb bis Schwarz gefärbt, wie von weißglühend über rotglühend bis kalt.

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
