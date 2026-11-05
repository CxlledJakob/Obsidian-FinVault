---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/15 - Intermarket-Analyse/15 - Intermarket-Analyse|15 - Intermarket-Analyse]]"
weitere_hauptthemen: []
unterthema: "Relative Märkte"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Lead-Lag-Beziehung


## Kurzdefinition

- Kandidaten für die Divergenzanalyse sind Paare, die gewöhnlich kohärent sind, bei denen aber ein bestimmtes Glied im Fall einer Divergenz führende Information über das andere hat; dann besteht eine ziemlich stabile Lead-Lag-Beziehung.
- Die Impulsantwort ψi ist die Wirkung der Innovation at auf die spätere Beobachtung rt plus i. Nach Orthogonalisierung ist das Element (i, j) von ψ* mit Index ℓ die Wirkung von bj,t auf ri,t plus ℓ.

## Kernaussagen

- Die bullische und die bärische Grundregel unterstellen, dass die Begleitreihe führende Information über den S&P 500 trägt: relative Stärke rechtfertigt eine Long-Position, relative Schwäche eine Short-Position.
- Die Annahme kann falsch sein: möglicherweise trägt der S&P 500 die führende Information, sodass negative Divergenzen höhere und positive Divergenzen tiefere S&P-Preise vorhersagen.
- Diese Möglichkeit war der Grund, inverse Fassungen jeder Divergenzregel mitzutesten.
- Hussman meint, Divergenzsignale seien am aufschlussreichsten, wenn zahlreiche Zeitreihen untersucht werden und eine erhebliche Zahl von ihnen zu divergieren beginnt.
- Nichtsynchroner Handel kann eine scheinbare Lead-Lag-Beziehung erzeugen: wird Aktie A häufiger gehandelt als die unabhängige Aktie B, erscheint die Rendite von A bei Nachrichten nahe dem Handelsschluss als führend für B.
- Der Effekt der Nachricht auf B tritt erst auf, möglicherweise verzögert bis zum nächsten Handelstag, sodass die Renditen eine signifikante Lag-1-Kreuzkorrelation von A nach B zeigen können, obwohl beide Aktien unabhängig sind.
- In einem Portfolio aus A und B wird aus dieser Kreuzkorrelation eine signifikante Lag-1-Autokorrelation.
- Ein Markt kann einen anderen unter manchen Umständen führen, und dieselbe Beziehung kann sich unter anderen Umständen umkehren.
- Ist ρij(ℓ) ungleich 0 und ℓ größer als 0, führt die Reihe rjt die Reihe rit mit Lag ℓ. Ist ρji(ℓ) ungleich 0 und ℓ größer als 0, führt rit die Reihe rjt mit Lag ℓ.
- Es gibt keine Lead-Lag-Beziehung und die Reihen heißen entkoppelt, wenn ρij(ℓ) und ρji(ℓ) für alle ℓ größer als 0 null sind.
- Unidirektional von rit nach rjt heißt: ρij(ℓ) ist für alle ℓ größer als 0 null, aber ρji(v) ist für mindestens ein v größer als 0 ungleich 0. Dann hängt rit von keiner Vergangenheit von rjt ab, rjt aber von vergangenen Werten von rit.
- Feedback zwischen rit und rjt liegt vor, wenn ρij(ℓ) für ein ℓ größer als 0 und ρji(v) für ein v größer als 0 ungleich 0 sind.
- Diese Bedingungen sind hinreichend. Ein passend spezifiziertes multivariates Modell ist aussagekräftiger, weil es serielle und Kreuzkorrelationen gemeinsam berücksichtigt.
- Sind für ℓ größer als 0 alle ρij(ℓ) null, hängt rit linear von keinem vergangenen Wert der Reihe rjt ab.
- Verwirft Qk(m) die Null, wird ein multivariates Modell gebaut, um die Lead-Lag-Beziehungen der Komponenten zu untersuchen.
- Im bivariaten VAR(1) ist φ12 der bedingte lineare Effekt von r2,t minus 1 auf r1t gegeben r1,t minus 1. Ist φ12 gleich 0, hängt r1t nicht von r2,t minus 1 ab. Ist φ21 gleich 0, hängt r2t gegeben r2,t minus 1 nicht von r1,t minus 1 ab.
- Sind φ12 gleich 0 und φ21 ungleich 0, ist die Beziehung unidirektional von r1t nach r2t. Sind beide Koeffizienten 0, sind die Reihen entkoppelt. Sind beide ungleich 0, besteht Feedback.
- Ist im VAR(p) das Element (i, j) von Φℓ für alle Lags ℓ gleich 0, hängt rit nicht von der Vergangenheit von rjt ab. Die Struktur der Koeffizientenmatrizen liefert damit die Lead-Lag-Information.
- Hinreichend für Entkopplung über die Kreuzkorrelationen ist, dass ρij(ℓ) und ρji(ℓ) für alle ℓ größer als 0 null sind. Unidirektional von rit nach rjt ist der Fall, in dem ρij(ℓ) für alle positiven Lags null ist, ρji(v) aber für ein v größer als 0 nicht. Feedback verlangt Nichtnullstellen in beiden Richtungen.
- Im bivariaten VMA(1) sind die Reihen entkoppelt, wenn beide Nebendiagonalelemente von Θ null sind. Unidirektional von r1t nach r2t heißt: θ12 gleich 0 und θ21 ungleich 0. Feedback heißt: beide Nebendiagonalelemente ungleich 0. Diese Einteilung überträgt sich auf ein VMA(q).
- Im VARMA messen die Elemente (i, j) von Φv und Θv für v größer als 0 die lineare Abhängigkeit von rit von rj,t minus v und von aj,t minus v. Sind alle diese Elemente null, hängt rit nicht von gelagten rjt ab. Die Umkehrung gilt nicht: Nichtnull-Koeffizienten können stehen, obwohl rit von keinem gelagten rjt abhängt.
- Notwendig und hinreichend für eine unidirektionale dynamische Beziehung von r1t nach r2t ist, dass φ22(B) θ12(B) minus φ12(B) θ22(B) gleich 0 ist, aber φ11(B) θ21(B) minus φ21(B) θ11(B) ungleich 0. Die Bedingung θ12(B) gleich φ12(B) gleich 0 ist dafür hinreichend, aber nicht notwendig.
- Die Orthogonalisierung der Impulsantwort hängt von der Komponentenreihenfolge ab, weil der erste Schock nicht transformiert wird. Die Deutung der Impulsantwort ist deshalb an die Innovationsreihe bt gebunden.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Zum Niveau 5 Prozent zeigt das vereinfachte VAR(5) eine unidirektionale dynamische Beziehung von der monatlichen S&P-500-Rendite zur IBM-Rendite. Vergangene IBM-Renditen beeinflussen den US-Markt nicht signifikant, trotz der starken gleichzeitigen Korrelation. SP5 ist der treibende Faktor der bivariaten Reihe.
- Die vereinfachten Gleichungen lauten: IBM_t gleich 1,0 plus 0,13 mal SP5 von t minus 1 minus 0,09 mal SP5 von t minus 2 plus 0,09 mal SP5 von t minus 5 plus a1t, und SP5_t gleich 0,4 plus 0,08 mal SP5 von t minus 1 minus 0,06 mal SP5 von t minus 3 plus 0,09 mal SP5 von t minus 5 plus a2t.
- IBM hängt schwach von den vorherigen S&P-Renditen ab; das stützt sich auf signifikante Kreuzkorrelationen im Element (1, 2) der Lags 1, 2 und 5.
- Im VAR(1) mit IBM als erster Komponente lauten die Gleichungen IBM_t gleich 1,06 minus 0,03 mal IBM von t minus 1 plus 0,15 mal SP5 von t minus 1 plus a1t und SP5_t gleich 0,41 minus 0,02 mal IBM von t minus 1 plus 0,10 mal SP5 von t minus 1 plus a2t. Nach den t-Statistiken ist nur SP5 von t minus 1 in beiden Gleichungen informativ.
- Bei Lag 0 der orthogonalen Impulsantwort, IBM zuerst, ist die IBM-Antwort auf den eigenen Schock 6,9973 und auf den S&P-Schock 0. Die S&P-Antwort ist 3,5432 auf den IBM-Schock und 4,2280 auf den eigenen Schock.
- Bei Lag 1 ist die IBM-Antwort 0,3088 auf den IBM-Schock, Standardfehler 0,2217, und 0,6353 auf den S&P-Schock, Standardfehler 0,2221. Die S&P-Antwort ist 0,2050 auf den IBM-Schock, Standardfehler 0,1746, und 0,4312 auf den eigenen Schock, Standardfehler 0,1750. Die Funktionen klingen schnell ab.
- Der VMA(5) liefert im Wesentlichen dieselbe dynamische Beziehung wie das VAR(5): die IBM-Monatsrendite hängt von früheren S&P-Renditen ab, die Marktrendite nicht von gelagten IBM-Renditen. Getrieben wird die Struktur von der Marktrendite; die gleichzeitige Korrelation bleibt stark.
- Beim VARMA(2,1) der logarithmierten Treasury-Sätze besteht eine unidirektionale lineare Beziehung vom 3-Jahres-Satz zum 1-Jahres-Satz: die Elemente (2, 1) aller AR- und MA-Matrizen sind null, mindestens ein Element (1, 2) ist ungleich 0.
- Die geschätzten Gleichungen lauten r3t gleich 0,025 plus 0,99 mal r3,t minus 1 plus a3t plus 0,47 mal a3,t minus 1, und r1t gleich 0,028 plus 1,82 mal r1,t minus 1 minus 0,84 mal r1,t minus 2 minus 0,97 mal r3,t minus 1 plus 0,98 mal r3,t minus 2 plus a1t minus 0,90 mal a1,t minus 1 plus 1,66 mal a3,t minus 1. Der 3-Jahres-Satz hängt nicht von der Vergangenheit des 1-Jahres-Satzes ab.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 419–438 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-023-p419-p438|S. 419–438]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 248–267 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-014-p248-p267|S. 248–267]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 400–419 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-022-p400-p419|S. 400–419]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 419–438 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-023-p419-p438|S. 419–438]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 438–457 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-024-p438-p457|S. 438–457]]

## Verwandte Themen
