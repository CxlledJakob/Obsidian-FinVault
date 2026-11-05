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

# Hilbert-Transformation


## Kurzdefinition

- Der Hilbert-Transformer ist die Technik, aus einem reellen Signal ein analytisches Signal zu erzeugen.
- Ein Hilbert-Transformer ist ein FIR-Filter, das aus dem reellen Datenstrom eine Quadraturkomponente erzeugt. Die Filterlänge ist theoretisch unendlich, kann aber als Näherung abgeschnitten werden.

## Kernaussagen


## Funktionsweise

- Ein analytisches Signal erlaubt zeitvariable Parameter und verallgemeinert das Phasor-Konzept, das auf zeitinvariante Amplitude, Phase und Frequenz beschränkt ist. Phase oder Leistung einer Welle lassen sich mit analytischen Signalen viel einfacher berechnen.
- Die Filterkoeffizienten sind Sin²(πn / 2) / n, wobei n die Position von der Filtermitte ist. Koeffizienten, die älter als die halbe Filterlänge sind, haben ein negatives Vorzeichen. Ein 23-Element-Filter hat die Koeffizienten [.091 0 .111 0 .143 0 .2 0 .33 0 1 0 −1 0 −.33 0 −.2 0 −.143 0 −.111 0 −.091] / 1,865.
- Die Sinuskomponente heißt In-Phase-Komponente, die Kosinuskomponente Quadraturkomponente. Ihre Vektoren stehen in der komplexen Ebene im rechten Winkel, sind also orthogonal; ihr Produkt ist unkorreliert, so ist die Summe von sin(x) mal cos(x) über einen vollen Zyklus null.
- sin²(x) + cos²(x) ist konstant. Ergibt die Summe der Quadrate keine Konstante, ist die Erzeugung des analytischen Signals gescheitert; dann wechselt der Markt wahrscheinlich zwischen Zyklusmodus und Trendmodus.
- Beim modifizierten Hilbert-Transformer ist Real das Ergebnis des Roofing-Filters (Zwei-Pol-Hochpass für Zyklen kürzer als 48 Bars plus SuperSmoother), per AGC auf seinen jüngsten Spitzenwert normiert.
- Die imaginäre Komponente entsteht aus der Ein-Bar-Differenz von Real, analog zur Ableitung einer Sinuswelle zur Kosinuswelle; das liefert die Phasenquadratur. Eine zweite AGC nur auf die imaginäre Komponente korrigiert die Amplitude.
- Die kritische Periode des SuperSmoothers ist beim modifizierten Hilbert-Transformer als Eingabe LPPeriod wählbar, Standardwert 20 Bars, für mehr oder weniger Glättung.
- Der Hilbert-Transformer-Indikator legt zusätzlich einen 10-Bar-SuperSmoother auf die imaginäre Komponente. Das zerstört deren Orthogonalität, weil es mehrere Bars Lag einführt, macht die Komponente aber durch Glätten des erratischen Verhaltens nutzbar.
- Im Homodyne-Code gilt Re = Real · Real[1] + Imag · Imag[1] und Im = Real[1] · Imag − Real · Imag[1]. Sind Im und Re ungleich null, ist Period = 6,28318 / |Im / Re|; die Periode wird auf 10 bis 48 begrenzt und mit einem SuperSmoother geglättet.
- Die Homodyne-Rechnung wird mit In-Phase- und Quadraturkomponente durchgeführt statt in Polarkoordinaten; die Ergebnisse sind in beiden Fällen gleich.

## Voraussetzungen


## Anwendung im Trading

- Der modifizierte Hilbert-Transformer ist ein prädiktiver Indikator, weil die Quadraturkomponente der reellen Ausgabe vorausläuft wie eine Kosinuswelle einer Sinuswelle. Der Lag von Real und Imag ist sehr klein, eine Kompensation im Plot ist nicht nötig.
- Die reelle Komponente bewegt sich mit der allgemeinen Preisrichtung, die imaginäre ist ein Vorhersageindikator für die reelle.
- Ein prognostizierter Wendepunkt nach oben liegt vor, wenn die imaginäre Komponente über die reelle kreuzt, ein Wendepunkt nach unten, wenn sie darunter kreuzt. Das gibt Zeit, den Trade vor dem Wendepunkt zu platzieren.
- Gegen falsche Wendepunktprognosen hilft, den Trade zunächst in prognostizierter Richtung einzugehen, aber schnell auszusteigen, wenn der Even Better Sinewave Indicator ihn nicht bestätigt.
- Der Hilbert-Transformer-Indikator liefert prädiktive Wendepunkte für das Swing-Trading.

## Regeln und Kriterien


## Risiken und Grenzen

- Der FIR-Lag beträgt (N − 1) / 2 bei ungerader Elementzahl. Das 23-Element-Filter hat 11 Bars Lag, was für den Handel inakzeptabel ist; sein Frequenzgang zeigt Welligkeit im Durchlassbereich und Abfall bei Frequenz null und bei der Nyquist-Frequenz, ideal wäre ein Allpass.
- Der kürzeste gekürzte Hilbert-Transformer [1 0 −1] hat nur einen Bar Lag, aber eine starke Amplitudenneigung über den Durchlassbereich von etwa 50-Bar-Periode (Frequenz 0,02) bis 10-Bar-Periode (Frequenz 0,1) und ist deshalb ebenfalls nicht handelbar.
- Ohne zusätzliche Glättung ist die imaginäre Komponente auch bei LPPeriod 20 zu erratisch, um nützlich zu sein.
- Der vorhergesagte Wendepunkt muss kein Swing-Wendepunkt sein, sondern kann der Beginn eines neuen Trends sein; dann ist die Prognose völlig falsch.
- Ehlers rät, den Code zur Berechnung des dominanten Zyklus mit dem Hilbert-Transformer nicht für den Handel zu nutzen. Er vermutet, dass das Rauschen von Sample zu Sample die Berechnung der Phasenänderungsrate überdeckt; die imaginäre Komponente darf dafür nicht geglättet werden, weil das die Orthogonalität zerstört.

## Beispiele

- Auf eine gechirpte Sinuswelle, deren Periode kontinuierlich von 10 auf 40 Bars steigt, hält der modifizierte Hilbert-Transformer über den gesamten Bereich die richtige Phasen- und Amplitudenbeziehung zwischen reeller und imaginärer Komponente; das ist dem klassischen gekürzten FIR-Transformer weit überlegen.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 178–197 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-014-p178-p197|S. 178–197]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 197–216 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-015-p197-p216|S. 197–216]]

## Verwandte Themen
