---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/22 - Marktanomalien & Behavioral Finance/22 - Marktanomalien & Behavioral Finance|22 - Marktanomalien & Behavioral Finance]]"
weitere_hauptthemen: []
unterthema: "Kalendereffekte"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Januar-Effekt


## Kurzdefinition


## Kernaussagen

- Das saisonale Muster der monatlichen einfachen Renditen des CRSP-Decile-1-Index geht hauptsächlich auf den Januar-Effekt zurück.
- Die Januar-Dummy ist 1, wenn der Monat ein Januar ist, und sonst 0; die einfache Regression der Monatsrendite auf diese Dummy entfernt die Saison, die in den Lags 12, 24 und 36 der Autokorrelation sichtbar war.
- Das saisonale Verhalten der monatlichen einfachen Rendite von Decile 1 geht hauptsächlich auf den Januar-Effekt zurück.
- Das angepasste Modell lautet Rt gleich 0,0029 plus 0,1253 mal Jant plus et; die Standardfehler der beiden Schätzungen sind 0,0033 und 0,0115.
- In der R-Ausgabe ist der Januar-Koeffizient 0,125251 mit Standardfehler 0,011546, t-Wert 10,848 und p-Wert unter 2e-16; der Achsenabschnitt 0,002864 hat den t-Wert 0,859 und den p-Wert 0,391.
- Das Bestimmtheitsmaß dieser Januar-Regression ist 0,2016, das adjustierte 0,1999, der residuale Standardfehler 0,06904 bei 466 Freiheitsgraden.
- Die Januar-Dummy besteht aus 39 Wiederholungen einer Eins gefolgt von elf Nullen.
- Nach der Dummy verschwinden in der Stichproben-Autokorrelation der Residuen die seriellen Korrelationen auf den Lags 12, 24 und 36 weitgehend, das saisonale Muster von Decile 1 ist damit entfernt.
- Die Decile-Reihen nach Marktkapitalisierung von NYSE, AMEX und NASDAQ in Übung 2.4 laufen von Januar 1970 bis Dezember 2008 und stammen von CRSP.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Der Index umfasst Januar 1970 bis Dezember 2008, 468 Beobachtungen; der Zeitplot zeigt kein klares Saisonmuster, die Stichprobenautokorrelation aber signifikante Lags bei 1, 12, 24 und 36.
- Ein saisonales Modell der Form (1 minus phi1 B) mal (1 minus phi12 B hoch 12) mal Rt gleich (1 minus θ12 B hoch 12) mal at wird identifiziert.
- Die bedingte Likelihood liefert (1 minus 0,18 B) mal (1 minus 0,87 B hoch 12) mal Rt gleich (1 minus 0,74 B hoch 12) mal at, mit Residualstandardabweichung 0,069; die saisonalen AR- und MA-Koeffizienten liegen in ähnlicher Größenordnung.
- Die exakte Likelihood liefert (1 minus 0,188 B) mal (1 minus 0,951 B hoch 12) mal Rt gleich (1 minus 0,997 B hoch 12) mal at, mit Residualstandardabweichung 0,063; die saisonalen Faktoren heben sich nahezu auf und deuten auf deterministische Saisonalität.
- Die Kleinste-Quadrate-Regression lautet Rt gleich 0,0029 plus 0,1253 mal der Januar-Dummy plus Fehler, mit Standardfehlern 0,0033 und 0,0115.
- In R sind die Schätzer 0,002864 und 0,125251 mit Standardfehlern 0,003333 und 0,011546; der t-Wert des Januarterms ist 10,848, der Residualstandardfehler 0,06904 bei 466 Freiheitsgraden, R² gleich 0,2016 und das adjustierte R² gleich 0,1999.
- Nach dieser Dummy-Regression verschwinden die seriellen Korrelationen bei den Lags 12, 24 und 36 weitgehend.
- Die R-Schätzung mit Mittelwert gibt ar1 gleich 0,1769, den saisonalen AR-Koeffizienten 0,9882, den saisonalen MA-Koeffizienten minus 0,9144 und den Intercept 0,0118, mit Standardfehlern 0,0456, 0,0093, 0,0335 und 0,0129; die Residualvarianz wird auf 0,004717 geschätzt.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 96–115 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-006-p096-p115|S. 96–115]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 115–134 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-007-p115-p134|S. 115–134]]

## Verwandte Themen
