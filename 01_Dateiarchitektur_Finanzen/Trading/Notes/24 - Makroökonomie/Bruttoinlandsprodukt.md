---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/24 - Makroökonomie/24 - Makroökonomie|24 - Makroökonomie]]"
weitere_hauptthemen: []
unterthema: "Wachstum und Inflation"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Bruttoinlandsprodukt


## Kurzdefinition


## Kernaussagen

- Untersucht wird die Wachstumsrate des realen vierteljährlichen US-Bruttosozialprodukts, saisonbereinigt und in Prozent, vom zweiten Quartal 1947 bis zum ersten Quartal 1991. Die Mehrheit der Wachstumsraten ist positiv.
- Ein Markov-Switching-AR(4) trennt einen Expansionszustand mit mittlerer Wachstumsrate 0,965 von einem Kontraktionszustand mit −1,288.
- Die Mittel entstehen als 0,909 / (1 − 0,265 − 0,029 + 0,126 + 0,11) = 0,965 und −0,42 / (1 − 0,216 − 0,628 + 0,073 + 0,097) = −1,288.
- Die erwartete Dauer beträgt etwa 11,31 Quartale in der Expansion und 3,69 Quartale in der Kontraktion, also rund drei Jahre beziehungsweise etwa ein Jahr.
- Die Übergangswahrscheinlichkeit aus der Kontraktion ist 0,286, die in die Kontraktion 0,118. Ein Verlassen der Kontraktion ist damit wahrscheinlicher als der Eintritt.
- Die relativ großen Posterior-Standardabweichungen in Zustand 2 spiegeln die wenigen Quartale mit negativem Wachstum.
- Die AR-Koeffizienten von x_{t−2} unterscheiden sich deutlich, 0,029 gegen 0,628. Die Dynamik von Expansion und Kontraktion ist verschieden.
- Dieselbe Reihe untersuchen Tiao und Tsay (1994) sowie Potter (1995) mit TAR-Modellen, Hamilton (1989) und McCulloch und Tsay (1994) mit Markov-Switching.
- Zustand 1, Posterior-Mittel und Standardfehler: Konstante 0,909 (0,202), AR-Koeffizienten 0,265 (0,113), 0,029 (0,126), −0,126 (0,103), −0,110 (0,109), Innovationsstandardabweichung 0,816 (0,125), Übergangswahrscheinlichkeit 0,118 (0,053).
- Zustand 2: Konstante −0,420 (0,324), AR-Koeffizienten 0,216 (0,347), 0,628 (0,377), −0,073 (0,364), −0,097 (0,404), Innovationsstandardabweichung 1,017 (0,293), Übergangswahrscheinlichkeit 0,286 (0,064).

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Die Logreihe des vierteljährlichen US-Bruttoinlandsprodukts von 1947.I bis 2008.IV zeigt einen Aufwärtstrend des Wirtschaftswachstums und hohe serielle Stichprobenkorrelationen.
- Die erste Differenz dieser Logreihe ist die Wachstumsrate des US-BIP und schwankt um ein festes Mittelniveau, wobei die Schwankung in den jüngeren Jahren kleiner wirkt.
- Der erweiterte Dickey-Fuller-Test mit Lagordnung 10, gewählt nach der Stichproben-PACF der Differenz, liefert die Statistik minus 1,701 mit p-Wert 0,4297; die Einheitswurzel-Hypothese wird nicht verworfen, und β-Dach gleich 1 minus 0,0008 gleich 0,9992.
- Andere Lagordnungen ändern die Schlussfolgerung dieses Tests nicht.
- In R liefert adfTest mit 10 Lags und Typ c die Dickey-Fuller-Statistik minus 1,6109 mit p-Wert 0,4569; die per Maximum Likelihood bestimmte Ordnung der Differenz ist 10.
- Im S-Plus-Output beträgt die Konstante 0,0134 mit Standardfehler 0,0045, t-Wert 2,9636 und p-Wert 0,0034; R² ist 0,2877, das adjustierte R² 0,2564, Durbin-Watson 1,9940, und der Residualstandardfehler 0,009318 bei 234 Freiheitsgraden.
- Derselbe Output gibt Lag 1 als minus 0,0008 mit t-Wert minus 1,7006 und p-Wert 0,0904, Lag 2 als 0,3799, Lag 3 als 0,1883 und Lag 10 als 0,1784, die letzten drei mit p-Werten unter 0,01.
- Die saisonbereinigte Reihe des impliziten Preisdeflators des vierteljährlichen US-BIP könnte doppelte Einheitswurzeln haben; der Mittelwert der zweiten Differenz unterscheidet sich nicht signifikant von null.
- Die von der US-Regierung veröffentlichten Reihen der BIP-Wachstumsrate und der Arbeitslosenquote sind in der Regel saisonbereinigt.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 96–115 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-006-p096-p115|S. 96–115]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 210–229 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-012-p210-p229|S. 210–229]]

## Verwandte Themen
