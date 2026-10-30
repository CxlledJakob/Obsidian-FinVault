---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/07 - Orderflow & Market Microstructure/07 - Orderflow & Market Microstructure|07 - Orderflow & Market Microstructure]]"
weitere_hauptthemen: []
unterthema: "Mikrostruktur"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# VPIN


## Kurzdefinition

- VPIN ist unter einer Volumen-Uhr die Wahrscheinlichkeit informierten Handels, näherungsweise der Erwartungswert des Betrags von zwei mal Kaufanteil minus eins.
- VPIN ist der von Easley, López de Prado und O'Hara (2011) vorgeschlagene volumensynchronisierte Hochfrequenzschätzer der Probability of Informed Trading.
- VPIN ist die Volume Synchronized Probability of Informed Trading (Easley, Lopez de Prado und O'Hara [2011]).

## Kernaussagen

- Wenn gute und schlechte Nachrichten gleich wahrscheinlich sind, ist PIN der Bruch mit Alpha mal Mu im Zähler und mit Alpha mal Mu plus 2 Epsilon im Nenner.
- Mu ist die Ankunftsrate informierter Händler, Epsilon die uninformierter Händler und Alpha die Wahrscheinlichkeit eines Informationsereignisses.
- PIN ist der Anteil der Orders informierter Händler am gesamten Order Flow.
- In einem Volumenbar der Größe V ist der erwartete Betrag der Differenz aus Kauf- und Verkaufsvolumen ungefähr Alpha mal Mu, und das erwartete Gesamtvolumen ist Alpha mal Mu plus 2 Epsilon.
- Die Volumen-Uhr setzt dieses erwartete Gesamtvolumen exogen gleich V, dadurch wird PIN zu VPIN gleich Alpha mal Mu geteilt durch V.
- Der Kaufanteil ist das Kaufvolumen geteilt durch V, und zwei mal Kaufanteil minus eins ist das Order-Flow-Ungleichgewicht im Intervall von minus 1 bis 1.
- Die VPIN-Theorie verknüpft PIN mit der Persistenz von Order-Flow-Ungleichgewichten unter einer Volumen-Uhr.
- Easley et al. (2012a, 2012b) erklären die Schätzung von VPIN als Hochfrequenzschätzung von PIN unter volumenbasiertem Sampling.
- Die Volume Clock synchronisiert die Stichprobe mit der Marktaktivität, gemessen am Volumen.
- Informierte Händler treffen mit Rate μ ein und uninformierte mit Rate ε, jeweils gemäß einer Poisson-Verteilung.
- Im Standardfall δt = 1/2 ist PINt = αt μ / (αt μ + 2ε), wobei αt die Wahrscheinlichkeit neuer Information im Untersuchungsfenster ist.
- Die klassische PIN-Schätzung bestimmt die vier nicht beobachtbaren Parameter {α, δ, μ, ε} per Maximum Likelihood als Mischung dreier Poisson-Verteilungen.
- Easley et al. (2008) zeigen E[VB − VS] = α μ (1 − 2δ).
- Für ein hinreichend großes μ gilt näherungsweise E[|VB − VS|] ≈ α μ.
- VB ist die Summe der kaufinitiierten Volumina in einem Volume Bar und VS die Summe der verkaufsinitiierten Volumina.
- Weil alle Volume Bars die Größe V haben, gilt der Mittelwert von VB + VS gleich V = α μ + 2ε.
- VPINτ ist die Summe der absoluten Volumenungleichgewichte über n Bars, geteilt durch das Produkt nV.
- Weitere Details und Fallstudien stehen bei Easley et al. (2013).
- VPIN und eine Variante des Herfindahl-Hirschman-Index der Marktfragmentierung wurden als Indikatoren mit Frühwarneigenschaften vor dem Flash Crash von 2010 umgesetzt.
- Die von VPIN erkannten Ereignisse gelten als intrinsisch, weil eine Änderung der Schwelle der VPIN-CDF die Zahl der Ereignisse nur geringfügig verändert.
- Wären die Ereignisse zufällig, hätte eine Änderung dieser Schwelle von 0,9 auf 0,99 die Zahl der Ereignisse um den Faktor 10 verringert.
- Ein schnelleres VPIN-Programm erlaubt es, die Echtzeit-Wirksamkeit von VPIN zu bestätigen.
- Die Arbeit war einer der ersten Schritte, um zu zeigen, dass sich solche Frühwarnsignale schnell genug berechnen lassen.

## Funktionsweise

- VPIN tastet Finanzreihen als Funktion des gehandelten Volumens ab.
- Für die Berechnung von VPIN werden Bars und Buckets gespeichert.

## Voraussetzungen

- Ticks werden innerhalb des Volumenbars als Kauf oder Verkauf klassifiziert, etwa mit der Tick Rule oder dem Lee-Ready-Algorithmus.
- Die Herleitung von PIN in dieser Form setzt ausgeglichene Chancen auf gute und schlechte Nachrichten voraus.

## Anwendung im Trading

- Weitere Einzelheiten dieser mikrostrukturellen Theorie stehen in Kapitel 19.
- VPIN ist eines der Features, mit denen ein Market Maker prüfen kann, ob er Liquidität stellen oder passive Quotes zurückziehen soll.
- Die Hochleistungsfassung soll die Warnsignale so früh wie möglich liefern, damit Zeit für korrigierende Maßnahmen bleibt.
- Anlass war die lange Aufarbeitung des Flash Crash durch SEC und CFTC; die Ermittler mussten Dutzende Terabyte durchsuchen, und die CFTC führte die Verzögerung öffentlich auf das Datenvolumen zurück.
- Beide Algorithmen wurden in C++ implementiert und nutzen MPI für die Kommunikation zwischen Prozessoren.
- Eine Programmfassung liest HDF5-Dateien, die andere die üblichen ASCII-Textdateien.
- Die Berechnung von VPIN und HHI für alle S&P-500-Aktien über zehn Jahre dauerte auf einem CPU-Kern etwa 3,5 Stunden mit ASCII-Daten und 603,98 Sekunden mit HDF5.
- Mit 512 CPU-Kernen sinkt diese HDF5-Laufzeit auf 2,58 Sekunden, eine Beschleunigung um das 234-Fache.
- Mit der zehnfachen Datenmenge dauerte die Berechnung dieser Indizes nur etwa 2,3-mal so lange, die Latenz stieg also unterlinear.
- Auf dem großen Datensatz senkte die HDF5-Indexierung bei 512 CPU-Kernen die Laufzeit von 16,95 auf 4,59 Sekunden, eine Beschleunigung um 3,7.
- Die Testdaten der VPIN-Kalibrierung umfassen 67 Monate Trades der hundert am häufigsten gehandelten Futures-Kontrakte.
- Im Mittel dauert die Verarbeitung eines Kontrakts über 67 Monate rund 1,5 Sekunden; zuvor etwa 18 Minuten, eine Beschleunigung um das 720-Fache allein durch die algorithmische Verbesserung ohne Parallelisierung.
- Der HPC-Code kann auf Parallelrechnern mit MPI laufen und die Rechenzeit weiter senken.
- Zur Beschleunigung dienen schnellerer I/O-Zugriff über HDF5 und eine schlankere Datenstruktur für die Bars und Buckets (Wu et al. [2013]).

## Regeln und Kriterien

- Mit der berichteten Parameterwahl sinkt die Falsch-positiv-Rate von VPIN über hundert Kontrakte von 20 % auf 7 %.
- Die Volume-Bar wird mit den Medianpreisen der Trades bepreist, nicht mit dem in Analysen üblichen Schlusskurs.
- Verwendet werden 200 Buckets pro Tag und 30 Bars pro Bucket.
- Das Stützfenster für die VPIN-Berechnung beträgt einen Tag, die Ereignisdauer 0,1 Tag.
- Die Bulk-Volume-Classification nutzt eine Student-t-Verteilung mit ν = 0,1.
- Die Schwelle für die CDF von VPIN liegt bei 0,99.
- Diese Parameter liefern eine niedrige Falsch-positiv-Rate über die Gesamtheit der Futures-Kontrakte und sind nicht das Ergebnis einzelner Anpassungen.
- Für verschiedene Kontraktklassen lassen sich andere Parameter wählen, sodass die Falsch-positiv-Rate in manchen Fällen deutlich unter 1 % fällt.

## Risiken und Grenzen

- Zins- und Index-Futures haben typischerweise niedrigere Falsch-positiv-Raten, Rohstoff-Futures wie Energie und Metall allgemein höhere.

## Beispiele

- Am 6. Mai 2010 fiel der Dow Jones Industrial Average gegen 14:45 Uhr U.S. Eastern Daylight Time um fast 10 %.
- Viele Aktien wurden zu einem Cent je Aktie gehandelt, dem Mindestpreis, und Apple-Aktien (AAPL) zu 100.000 US-Dollar, dem vom Börsenplatz erlaubten Höchstpreis.
- Abbildung 22.7 zeigt den Apple-Kurs dieses Tages zusammen mit HHI- und VPIN-Werten, berechnet alle 5 Minuten während der Marktzeiten.
- Abbildung 22.9 zeigt die mittleren Falsch-positiv-Raten (α) verschiedener Klassen von Futures-Kontrakten, geordnet nach ihrem Mittelwert.

## Unterschiedliche Quellenpositionen

- Andersen und Bondarenko (2013) schließen aus linearen Regressionen, dass VPIN kein guter Prädiktor der Volatilität ist.
- Vorhersagekraft von VPIN finden dagegen unter anderem Abad und Yague (2012), Bethel et al. (2012), Cheung et al. (2015), Kim et al. (2014), Song et al. (2014), Van Ness et al. (2017) und Wei et al. (2013).
- Der Text wendet ein, dass lineare Regression komplexe nichtlineare Muster in Finanzmärkten verfehlen kann.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 286–305 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-016-p286-p305|S. 286–305]]
- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]
- Advances in Financial Machine Learning.pdf, S. 362–381 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-020-p362-p381|S. 362–381]]

## Verwandte Themen

- Zusammen mit VPIN wurde eine Variante des Herfindahl-Hirschman-Index (HHI) der Marktfragmentierung implementiert (Hirschman [1980]).
