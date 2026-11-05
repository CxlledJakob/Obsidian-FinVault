---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Modelle"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Extreme-Value-Theorie


## Kurzdefinition

- Die Extremwerttheorie sucht Folgen βn und αn > 0, sodass die Verteilung des normierten Maximums (r(n) minus βn) / αn für wachsendes n gegen eine nicht entartete Grenzverteilung konvergiert.
- Das Minimum folgt durch Vorzeichenwechsel, r(1) = minus dem Maximum der vorzeichenverkehrten Renditen. Für eine Long-Position werden negative Logrenditen verwendet.
- Im zweidimensionalen Poisson-Prozessmodell ist die bedingte Verteilung des Überschusses xt gleich rt minus η über die Schwelle η eine verallgemeinerte Pareto-Verteilung mit Formparameter ξt und Skalenparameter ψt gleich αt plus ξt mal (η minus βt).
- Der Extremalindex θ einer streng stationären Reihe ist die nichtnegative Zahl, für die es zu jedem τ größer als 0 Schwellen un gibt mit lim n[1 minus F(un)] gleich τ und lim P(x(n) ≤ un) gleich exp(minus θτ).

## Kernaussagen

- Zusammenbrüche großer Finanzinstitute in der Krise zeigen, dass Extremereignisse in Clustern auftreten und nicht unabhängig sind.
- Zur Behandlung der Abhängigkeit in Extremen nimmt Kapitel 7 den Extremal Index auf und erörtert seinen Einfluss auf den Value at Risk.
- Kapitel 7 behandelt die Extreme-Value-Theorie, Verteilungen mit schweren Rändern und ihre Anwendung im finanziellen Risikomanagement.
- Die VaR-Berechnung mit Extreme-Value-Theorie wird in der Darstellung der ersten Auflage auf einen inhomogenen zweidimensionalen Poisson-Prozess gestützt.
- Kapitel 7 führt den Extremal Index für abhängige Daten ein.
- Bei seriell unabhängigen Renditen mit gemeinsamer Verteilungsfunktion F ist die Verteilungsfunktion des Maximums [F(x)] hoch n. Ohne Normierung entartet sie, wenn n gegen unendlich geht.
- Die verallgemeinerte Extremwertverteilung hat den Formparameter ξ, den Lageparameter βn und den Skalenparameter αn. Der Tail-Index ist α = 1/ξ. Der Fall ξ = 0 ist der Grenzwert für ξ gegen 0.
- ξ = 0 ergibt die Gumbel-Familie mit Verteilungsfunktion exp[minus exp(minus x)]. ξ > 0 ergibt die Fréchet-Familie, ξ < 0 die Weibull-Familie, jeweils mit der Potenzform (1 plus ξx) hoch minus 1/ξ im Exponenten und dem passenden Träger.
- Der rechte Schwanz fällt bei Gumbel exponentiell, bei Fréchet nach einer Potenz und ist bei Weibull endlich. Für das Risikomanagement interessiert vor allem Fréchet, das stabile Verteilungen und die Student-t enthält. Gumbel umfasst dünne Schwänze wie Normal- und Lognormalverteilung.
- Nicht die konkrete Verteilung, sondern das Schwanzverhalten von F bestimmt die Grenzverteilung des normierten Maximums. Nach Feller hängt der Tail-Index nicht vom Zeitintervall der Rendite ab und ist unter Zeitaggregation invariant.
- Für stationäre normale Folgen bleibt dieselbe Grenzform nach Berman (1964) erhalten, wenn die Autokorrelationsfunktion quadratisch summierbar ist.
- Peaks over Thresholds modelliert die Überschreitungen einer hohen Schwelle η und die Zeitpunkte dieser Überschreitungen, statt nur Blockmaxima zu verwenden. Die Blocklänge n entfällt, die Schwelle muss gewählt werden.
- Die bedingte Verteilung der Überschreitung wird durch eine verallgemeinerte Pareto-Verteilung approximiert, mit Form ξ und Skala ψ(η) = α plus ξ mal (η minus β). Für ξ = 0 wird das zur Exponentialverteilung.
- Ist der Exzess über ηo bereits eine verallgemeinerte Pareto-Verteilung, dann ist der Exzess über jede höhere Schwelle ebenfalls diese Verteilung mit demselben ξ und der Skala ψ(ηo) plus ξ mal (η minus ηo).
- Für 0 < ξ < 1 ist der mittlere Exzess ψ(ηo) / (1 minus ξ), und die Mean-Excess-Funktion ist linear im Abstand zur Schwelle. Der empirische Mean-Excess-Plot soll oberhalb einer geeigneten Schwelle linear sein; er heißt auch Mean-Residual-Life-Plot.
- Smith (1989) modelliert Zeitpunkte und Überschreitungen gemeinsam als zweidimensionalen Poisson-Prozess. Die Intensität ist proportional zur Länge des Zeitintervalls, gemessen am Basisintervall D, und wird von einer Überlebensfunktion vom Typ der Extremwertverteilung gesteuert. Tsay (1999) verwendet das für den VaR. In den USA ist D typisch 252 Handelstage.
- Ist die Intensität zeitlich konstant, ist der Poisson-Prozess homogen; hängt sie von der Zeit ab, ist er inhomogen. Erklärende Variablen machen ξt, ln(αt) und βt zu linearen Funktionen dieser Variablen.
- Ein Cluster der Überschreitungszeitpunkte zeigt eine Phase großer Marktrückgänge. Die Höhe der Überschreitung selbst ist die interessierende Größe.
- Nach Leadbetters Theorem 1 sind die möglichen nicht degenerierten Grenzverteilungen des Maximums einer streng stationären Reihe, die D(un) erfüllt, Extremwertverteilungen.
- Nach Leadbetters Theorem 2 ist die Grenzverteilung des Maximums der stationären Reihe F*(x) gleich der θ-ten Potenz der Grenzverteilung der zugehörigen iid-Reihe, mit Extremalindex θ im halboffenen Intervall (0, 1].
- Für ξ ungleich 0 bleibt der Formparameter unverändert, ξ* gleich ξ, während Skala und Lage vom Extremalindex abhängen: α* gleich α mal θ hoch ξ und β* gleich β minus α mal (1 minus θ hoch ξ) geteilt durch ξ.
- Für ξ gleich 0 gilt α* gleich α und β* gleich β plus α mal ln(θ).
- Für die iid-Vergleichsreihe ist der Grenzwert der Wahrscheinlichkeit, dass das Maximum unter un liegt, exp(minus τ); der Extremalindex θ skaliert diesen Exponenten auf minus θτ.
- Die Randverteilung der Blockmaxima ist nicht die Randverteilung F(x) der Einzelbeobachtungen; sie hängt von der Blockgröße k und von der Stärke der seriellen Abhängigkeit ab.
- Der Blockschätzer θ-Dach hoch (2) mit Index b gleich G(un) geteilt durch N(un) ist nach Hsing, Hüsler und Leadbetter (1988) der Kehrwert der mittleren Clustergröße des begrenzenden zusammengesetzten Poisson-Prozesses.

## Funktionsweise

- Weil ein einzelnes Maximum die drei Parameter nicht schätzt, wird die Stichprobe in g nicht überlappende Blöcke der Länge n geteilt, mit T = n g. Die Blockmaxima werden als Stichprobe aus der Extremwertverteilung behandelt.
- Für Tagesrenditen entspricht n = 21 etwa einem Monat und n = 63 einem Quartal. Ist T kein Vielfaches von n, kann der letzte Block kürzer sein oder man lässt die ersten Beobachtungen weg.
- Die Maximum-Likelihood-Schätzer von ξn, βn und αn sind unter geeigneten Annahmen unverzerrt, asymptotisch normal und von minimaler Varianz.
- Die Kleinste-Quadrate-Schätzer der Regressionsmethode auf den Ordnungsstatistiken der Blockmaxima sind konsistent, aber weniger effizient; das Kapitel verwendet die Likelihood-Schätzer.
- Der Hill-Schätzer mittelt die Abstände der Logarithmen der q größten Ordnungsstatistiken zum Logarithmus der q-ten. Er gilt nur für Fréchet und ist dort effizienter als Pickands. Wurzel aus q mal (Hill-Schätzer minus ξ) ist asymptotisch normal mit Mittel null und Varianz ξ zum Quadrat.
- Der Pickands-Schätzer ist 1 geteilt durch ln(2) mal dem Logarithmus eines Verhältnisses dreier Ordnungsstatistiken und verlangt q höchstens T/4. Er ist konsistent, wenn q passend mit T wächst; seine asymptotische Varianz ist ξ zum Quadrat mal (2 hoch (2ξ plus 1) plus 1) geteilt durch [2 mal (2ξ minus 1) mal ln(2)] zum Quadrat.
- Praktisch trägt man den Hill-Schätzer gegen q ab und wählt ein q, bei dem die Schätzung stabil wirkt. Der geschätzte Tail-Index 1/ξ dient dann extremen Quantilen.
- Der Blockschätzer θ-Dach hoch (1) mit Index b ist (1/k) mal ln(1 minus G(un)/g) geteilt durch ln(1 minus N(un)/n); dabei ist N(un) die Zahl der Überschreitungen und G(un) die Zahl der Blöcke mit mindestens einer Überschreitung.
- Ist das Modell passend, sind die aus der Pareto-Verteilung abgeleiteten wti unabhängig und exponentialverteilt mit Mittel 1; die GPD-Annahme für die Überschüsse wird mit einem QQ-Plot geprüft.
- Für eine stationäre Logrendite-Reihe wird der VaR der Extremwerttheorie um den Extremalindex korrigiert: für ξn ungleich 0 ist VaR gleich βn minus (αn/ξn) mal {1 minus [minus nθ ln(1 minus p)] hoch (minus ξn)}, und für ξn gleich 0 gleich βn minus αn mal ln[minus nθ ln(1 minus p)], wobei n die Länge der Teilperiode ist.

## Voraussetzungen

- Die klassische Herleitung setzt serielle Unabhängigkeit und eine gemeinsame stetige Verteilung mit Träger von der Untergrenze l bis zur Obergrenze u voraus; für Logrenditen sind beide Grenzen unendlich. Schwache Abhängigkeit lässt dieselbe Grenzform zu.

## Anwendung im Trading


## Regeln und Kriterien

- Die Anpassung prüft drei Punkte: exponentialverteilte Dauern zwischen Überschreitungen, die Transformation der Exzesse auf eine Standardexponentialverteilung mit Mittel 1, und fehlende Autokorrelation dieser beiden Reihen.
- Für eine ruhige Renditereihe kann eine Schwelle von 2,5 Prozent für eine Long-Position genügen, für eine sehr volatile Reihe, etwa eine Dotcom-Aktie, bis 10 Prozent. Eine begrenzte Erfahrung wählt die Schwelle so, dass etwa 5 Prozent der Stichprobe überschreiten. Die Wahl ist statistisch und finanziell, weil Institute verschiedene Risikotoleranzen haben.

## Risiken und Grenzen

- Die Schätzungen können von der Blocklänge n abhängen. Lage- und Skalenparameter wachsen dem Betrag nach mit n, weil Blockminimum und Blockmaximum in n nicht fallen. Für n = 252 ist die Streuung höher, weil die Zahl der Blöcke g klein ist.
- Blockmaxima übersehen das Volatility Clustering der täglichen Logrenditen, und die Unabhängigkeitsannahme wird oft verworfen. Der neuere Ansatz soll diese Schwächen vermeiden. Die klassische Rechnung hängt zudem von der Blocklänge n ab: großes n stützt die Grenzverteilung, verkleinert aber die Zahl der Blöcke.
- Wird der Extremalindex übersehen, besteht die Gefahr, den VaR zu unterschätzen.
- Das homogene zweidimensionale Poisson-Modell besteht die Prüfung nicht: zti und wti zeigen signifikante serielle Korrelationen, und der QQ-Plot von zti weicht von der theoretischen Exponentialgeraden ab. Das inhomogene Modell liegt innerhalb der Zwei-Standardfehler-Grenzen und zeigt keine Modellunzulänglichkeit.

## Beispiele

- Für die IBM-Tageslogrenditen vom 3. Juli 1962 bis 31. Dezember 1998, T = 9190, in Prozent, liegt der Hill-Schätzer bei q = 190, 200 und 210 für die Renditen bei 0,300, 0,299 und 0,305 und für die negativen Renditen bei 0,290, 0,292 und 0,289, mit Standardfehlern um 0,02. Die Formparameter von etwa 0,30 sind auf dem asymptotischen 5-Prozent-Niveau von null verschieden; die Verteilung gehört zur Fréchet-Familie, die Normalannahme wird verworfen, im Einklang mit Longin (1996).
- Die Maximum-Likelihood-Schätzung für die Minima liefert bei n = 21 und g = 437 die Werte Skala 0,823, Lage 1,902 und Form 0,197; bei n = 63 und g = 145 die Werte 0,945, 2,583 und 0,335; bei n = 126 die Werte 1,147, 3,141 und 0,330; bei n = 252 die Werte 1,542, 3,761 und 0,322. Ab n = 63 liegt der Formparameter der negativen Extreme etwa bei 0,33 und ist stabiler als bei den positiven Extremen.
- Die GEV-Residuen wi = [1 plus ξn mal (Blockmaximum minus βn) / αn] hoch minus 1/ξn sollen bei korrektem Modell unabhängig exponentialverteilt sein. Für die negativen IBM-Renditen und n = 21 ist die Anpassung nach Residuen- und QQ-Plot vertretbar.
- Für die negativen IBM-Tageslogrenditen von 1962 bis 1998 ist ein QQ-Plot der Exzesse über 2,5 Prozent gekrümmt, der linke Schwanz also schwerer als normal und ξ ungleich 0. Der Mean-Excess-Plot spricht unter anderem für eine Schwelle von etwa 3 Prozent.
- Im homogenen Poisson-Modell gibt es bei den Schwellen 3,0, 2,5 und 2,0 Prozent 175, 310 und 554 Überschreitungen; die Formparameter sind 0,30697, 0,26418 und 0,18751. Ein Tagesverlust von mindestens 2,5 Prozent tritt mit Wahrscheinlichkeit 310/9190, etwa 3,4 Prozent, auf. Das Entfernen des Stichprobenmittels ändert die Schätzungen wenig.
- Die GPD-Schätzung bei Schwelle 2,5 Prozent lautet ξ = 0,26418 und Skala 0,007786 in Logrenditen, passend zu ψ(η) = 0,007787 aus der anderen Parametrisierung. Diagnostische QQ- und Tail-Plots zeigen kleine Abweichungen von der Geraden.
- Das homogene Modell bei Schwelle 2,5 Prozent besteht die Prüfung nicht: die Dauergrößen und die transformierten Exzesse haben signifikante serielle Korrelationen, und der QQ-Plot der Dauern weicht von der theoretischen Exponentialgeraden ab.
- Beim inhomogenen Poisson-Modell der täglichen prozentualen IBM-Logrenditen, 3. Juli 1962 bis 31. Dezember 1998, Schwelle 2,5 Prozent und 334 Überschreitungen, hängen alle drei Intensitätsparameter signifikant vom Jahrestrend ab: der Formparameter hat einen negativen Trend, Lage- und Skalenparameter steigen über die Zeit.
- Die Indikatoren für das vierte Quartal und für Panikverkäufe sind in diesem IBM-Modell für Lage, Skala und Form der Intensität nicht signifikant.
- Skala und Form hängen signifikant vom qualitativen Volatilitätsmaß ab, also von der Zahl der Tage unter t minus 1 bis t minus 5, an denen der Betrag der mittelwertbereinigten Logrendite mindestens 2,5 Prozent war.
- Am 31. Dezember 1998, mit x3 gleich 0, x4 gleich 0,9737 und x5 gleich 1,9766, liefert das Modell ξ gleich 0,01195, ln(α) gleich 0,19331 und β gleich 6,105; bei Tail-Wahrscheinlichkeit 0,05 ist das VaR-Quantil 3,03756 Prozent.
- Für die negativen täglichen IBM-Logrenditen, Blockgröße k gleich 10 und Schwelle 0,025, ist der Blockschätzer θ-Dach hoch (1) mit Index b gleich 0,823, gerechnet auf 919 Blöcken.
- Mit θ gleich 0,823, Teilperiodenlänge n gleich 63, βn gleich 2,583, αn gleich 0,945 und ξn gleich 0,335 beträgt das 1-Prozent-VaR 3,2714, höher als 3,0497 in Beispiel 7.6 ohne Extremalindex.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 1–20 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-001-p001-p020|S. 1–20]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 20–39 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-002-p020-p039|S. 20–39]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 362–381 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-020-p362-p381|S. 362–381]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 381–400 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-021-p381-p400|S. 381–400]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 400–419 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-022-p400-p419|S. 400–419]]

## Verwandte Themen
