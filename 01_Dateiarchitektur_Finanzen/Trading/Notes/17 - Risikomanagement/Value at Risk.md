---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/17 - Risikomanagement/17 - Risikomanagement|17 - Risikomanagement]]"
weitere_hauptthemen: []
unterthema: "Risikomessung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Value at Risk


## Kurzdefinition

- Der Value at Risk einer Finanzposition über den Horizont ℓ bei oberer Schwanzwahrscheinlichkeit p erfüllt p = Wahrscheinlichkeit, dass der Verlust L(ℓ) mindestens den VaR beträgt.
- Aus Sicht des Instituts ist der VaR der maximale Verlust der Position in einem gegebenen Zeitraum bei gegebener Wahrscheinlichkeit, also der Verlust eines seltenen Ereignisses unter normalen Marktbedingungen.
- Aus Sicht einer Aufsicht ist der VaR der minimale Verlust unter außergewöhnlichen Marktverhältnissen; beide Definitionen führen zum selben VaR.
- Ist die Verteilungsfunktion des Verlusts stetig und bekannt, ist der VaR ihr (1 minus p)-Quantil, manchmal als oberes p-Quantil bezeichnet.
- Das tägliche Gesamt-VaR eines Anlegers mit zwei Aktienpositionen ist die Wurzel aus VaR1 zum Quadrat plus VaR2 zum Quadrat plus 2 ρ mal VaR1 mal VaR2. VaR1 und VaR2 sind die VaR der Einzelpositionen.

## Kernaussagen

- Kapitel 7 nimmt den Extremal Index auf, um Abhängigkeit in Extremen zu behandeln, und erörtert seinen Einfluss auf den Value at Risk.
- Das neu gefasste Kapitel 7 enthält den Expected Shortfall, auch Conditional Value at Risk, zur Messung des finanziellen Risikos.
- Kapitel 7 gibt einen einheitlichen Zugang zum Value at Risk über eine Verlustfunktion und behandelt daneben den Expected Shortfall, gleichbedeutend mit dem Conditional Value at Risk, sowie den Extremal Index für abhängige Daten.
- Die VaR-Berechnung mit Extreme-Value-Theorie beruht in der Darstellung der ersten Auflage auf einem inhomogenen zweidimensionalen Poisson-Prozess.
- Die zweite Auflage ergänzt weitere Konzepte und Anwendungen des Value at Risk in Kapitel 7.
- Kapitel 7 behandelt Methoden zur Berechnung des Value at Risk und des Expected Shortfall einer Finanzposition.
- Das Buch ist auch als Nachschlagewerk für Praktiker gedacht, die den Value at Risk berechnen, Volatilität modellieren oder seriell korrelierte Daten analysieren.
- Die Modellierung der Volatilität liefert einen einfachen Weg, den Value at Risk einer Finanzposition im Risikomanagement zu berechnen; die Ausführung steht in Kapitel 7.
- Das spezielle IGARCH(1,1) mit alpha 0 gleich 0 ist das Volatilitätsmodell von RiskMetrics, einem Verfahren zur Berechnung des Value at Risk; die Darstellung steht in Kapitel 7.
- In diesem Fall ist die Varianzprognose auf jedem Horizont gleich der Ein-Schritt-Prognose.
- Dasselbe Modell ist ein exponentielles Glätten der Quadrate: sigma t quadrat gleich (1 minus beta 1) mal der Summe beta 1 hoch k mal a, t minus 1 minus k, quadrat, mit beta 1 als Diskontfaktor.
- Mit Wahrscheinlichkeit 1 minus p ist der mögliche Verlust über den Horizont ℓ kleiner als der VaR.
- VaR betrifft vor allem das Marktrisiko und ist auch auf Kreditrisiko und operationelles Risiko anwendbar; diese drei sind die Hauptkategorien finanziellen Risikos.
- In die Berechnung gehen p, der Zeithorizont ℓ, die Datenfrequenz, die Verteilungsfunktion oder ihre Quantile und der Marktwert der Position ein.
- Übliche Werte sind p = 0,01 im Risikomanagement und p = 0,001 im Stresstest; der Horizont ist oft 1 oder 10 Tage für Marktrisiko und 1 oder 5 Jahre für Kreditrisiko, häufig auf Tagesdaten.
- Für eine Long-Position werden negative Renditen verwendet. Der aus Logrenditen berechnete VaR ist ein Prozentsatz; der Geldbetrag ist Positionswert mal diesem VaR, näherungsweise auch Positionswert mal [exp(VaR der Logrenditen) minus 1].
- VaR ist eine Prognose und sollte aus der prädiktiven Verteilung künftiger Renditen stammen; die meisten Verfahren ignorieren die Parameterunsicherheit.
- VaR beschreibt den oberen Schwanz nicht vollständig: gleicher VaR kann verschiedene Verluste bei Überschreitung bedeuten, und VaR ist nicht subadditiv. Als Alternative dient der Expected Shortfall, auch Conditional Value at Risk.
- Das Beispiel hält je 1 Million Dollar long in Cisco und in Intel. Verwendet werden Tages-Logrenditen in Prozent vom 2. Januar 1991 bis 31. Dezember 1999, Ein-Schritt-Prognosen am Ende der Stichprobe und kritische Werte von 5 Prozent. Die Quantile werden durch 100 geteilt. Ein negatives Quantil bezeichnet den Verlust.
- Univariat, mit getrennten Volatilitätsmodellen und Stichprobenkorrelation 0,473: am Ursprung t gleich 2275 sind r̂1 gleich 0,626, σ̂²1 gleich 4,152, r̂2 gleich 0,187, σ̂²2 gleich 6,087 und ρ̂ gleich 0,473.
- Die 5-Prozent-Quantile sind q1 gleich 0,626 minus 1,65 mal der Wurzel aus 4,152 gleich minus 2,736 und q2 gleich 0,187 minus 1,65 mal der Wurzel aus 6,087 gleich minus 3,884. Daraus folgen VaR1 gleich 27.360 Dollar, VaR2 gleich 38.840 Dollar und ein Gesamt-VaR von 57.117 Dollar.
- Bivariates diagonales GARCH(1,1) mit konstanter, gemeinsam geschätzter Korrelation 0,475: die Prognosen sind r̂1 gleich 0,373, σ̂²1 gleich 4,287, r̂2 gleich 0,222, σ̂²2 gleich 5,706. VaR1 gleich 30.432 Dollar, VaR2 gleich 37.195 Dollar, Gesamt-VaR gleich 58.180 Dollar.
- Zeitvariable Korrelation über die Cholesky-Zerlegung: die Prognosen sind r̂1 gleich 0,352, r̂2 gleich 0,206, ĝ11 gleich 4,252, q̂21 gleich 0,421 und ĝ22 gleich 5,594. Daraus folgen σ̂²1 gleich 4,252, σ̂21 gleich 1,791, σ̂²2 gleich 6,348 und ρ̂ gleich 0,345. VaR1 gleich 30.504 Dollar, VaR2 gleich 39.512 Dollar, Gesamt-VaR gleich 57.648 Dollar.
- Die drei Gesamt-VaR liegen nahe beieinander. Das univariate Modell liefert den niedrigsten Wert, das Modell mit konstanter Korrelation den höchsten. Die Spanne beträgt etwa 1.100 Dollar. Das zeitvariable Modell liegt dazwischen.
- Alle Schätzungen dieser Illustration sind auf dem 5-Prozent-Niveau signifikant, und die Modelle sind nach den Ljung-Box-Statistiken der standardisierten Residuen und ihrer Quadrate angemessen. Standardfehler werden nicht berichtet.
- Eine Bayes-Lösung der Value-at-Risk-Rechnung aus Kapitel 7 kann die Parameterunsicherheit einbeziehen, verlangt aber intensive Rechnung.
- Die MCMC-Methode erzeugt eine prädiktive Verteilung der interessierenden Volatilität; sie ist informativer als eine Punktprognose und kann die für die Value-at-Risk-Rechnung benötigten Quantile liefern.
- MCMC ist für die Value-at-Risk-Rechnung nützlich, weil es einen natürlichen Weg bietet, prädiktive Verteilungen auszuwerten.
- Neben der prädiktiven Verteilung berücksichtigt MCMC bei der Prognose die Parameterunsicherheit.
- VaR-Modelle sind als Maß des eingegangenen Risikos allgegenwärtig, von Handelstischen der Investmentbanken über Hedgefonds bis zu Fondsgesellschaften. Ihre weite Nutzung droht positives Feedback-Trading auszulösen.
- Zu viele VaR-Modelle unterstellen, die jüngere Geschichte setze sich fort. Einfache Rechnungen legen nahe, dass sie das wahre Risiko allein wegen unpassender Korrelationen um 20 bis 30 Prozent unterschätzen. Eine Verdopplung oder Verdreifachung der Volatilität darüber hinaus lässt ein Desaster erwarten.
- Nach dem Basle-Abkommen gelten für interne VaR-Modelle ein Horizont von 10 Handelstagen oder zwei Kalenderwochen, 99 Prozent Konfidenz und ein Beobachtungsfenster von mindestens einem Jahr, aktualisiert mindestens einmal je Quartal. Das Fenster ist die Quelle der positiven Rückkopplung.

## Funktionsweise

- RiskMetrics nimmt bedingt normale Tageslogrenditen mit Mittelwert null und ein IGARCH(1,1) ohne Drift an. Bei 5 Prozent ist der VaR 1,65 σt+1, bei 1 Prozent 2,326 σt+1; über k Tage wird mit der Wurzel aus k skaliert. Wegen Symmetrie und Mittelwert null stimmen Long- und Short-VaR überein. Liegen die Logrenditen in Prozent vor, wird der 1-Prozent-VaR durch zusätzliches Teilen durch 100 gebildet.
- Der ökonometrische Ansatz kombiniert eine ARMA-Mittelgleichung mit einem GARCH-Volatilitätsmodell und liest den VaR am Quantil der bedingten Verteilung der nächsten Rendite ab.
- Die Quantilschätzung ist ein nichtparametrischer VaR-Weg und setzt nur voraus, dass die Verteilung in der Prognoseperiode dieselbe bleibt wie in der Stichprobe.
- Die Ordnungsstatistik r(ℓ) mit ℓ = n p ist asymptotisch normal mit Mittel gleich dem theoretischen Quantil xp und Varianz p(1 minus p) geteilt durch n mal der quadrierten Dichte an xp, sofern diese Dichte nicht null ist.
- Ist n p nicht ganzzahlig, wird das Quantil linear zwischen den beiden benachbarten Ordnungsstatistiken interpoliert.
- Die Quantilregression schätzt das bedingte Quantil gegeben erklärenden Variablen, indem die Check-Funktion wp auf den Regressionsresiduen summiert und minimiert wird.
- Für das Blockmaximum lautet das (1 minus p*)-Quantil der verallgemeinerten Extremwertverteilung βn minus (αn / ξn) mal {1 minus [minus ln(1 minus p*)] hoch minus ξn}, falls ξn ungleich 0, und βn minus αn mal ln[minus ln(1 minus p*)], falls ξn = 0. Finanzanwendungen interessiert vor allem der Fall ξn ungleich 0.
- Bei fehlender oder schwacher serieller Korrelation gilt 1 minus p* = [Wahrscheinlichkeit, dass die Einzelrendite höchstens dieses Blockquantil ist] hoch n.
- Für eine kleine obere Schwanzwahrscheinlichkeit p ist der VaR der Logrendite aus den Blockmaxima βn minus (αn / ξn) mal {1 minus [minus n mal ln(1 minus p)] hoch minus ξn}, falls ξn ungleich 0, und βn minus αn mal ln[minus n mal ln(1 minus p)], falls ξn = 0.
- Der klassische Weg hat vier Schritte: Blocklänge wählen und Blockmaxima bilden, Skala, Lage und Form per Maximum Likelihood schätzen, die Anpassung prüfen und dann die VaR-Formel anwenden. Für Long-Positionen gehen die negativen Logrenditen ein.
- Die α-Wurzel-der-Zeit-Regel lautet VaR über ℓ Tage = ℓ hoch (1/α) mal dem Ein-Tages-VaR = ℓ hoch ξ mal dem Ein-Tages-VaR. Hier ist α = 1/ξ der Tail-Index, nicht der Skalenparameter αn. Weil ℓ hoch ξ bei ξ unter 0,5 kleiner ist als die Wurzel aus ℓ, liegt dieser Mehrperioden-VaR unter der Wurzel-der-Zeit-Regel.
- Das Return Level zu g Blöcken der Länge n ist das Niveau, das in einem von g Blöcken überschritten wird; dieser Block heißt Stressperiode. Es ist das Quantil der Blockmaxima zur Wahrscheinlichkeit 1/g und gilt für das Blockmaximum, nicht für die einzelne Rendite.
- Im zweidimensionalen Poisson-Modell mit Basisintervall D, in den USA typisch 252, ersetzt D die Blocklänge in der Quantilformel: β minus (α / ξ) mal {1 minus [minus D mal ln(1 minus p)] hoch minus ξ}, falls ξ ungleich 0.
- In der Parametrisierung mit GPD-Skala ψ(η) ist der VaR zum Quantil q = 1 minus p gleich η minus [ψ(η) / ξ] mal {1 minus [T / Nη mal (1 minus q)] hoch minus ξ}, mit Stichprobenumfang T und Nη Überschreitungen. Diese Form verwenden R und S-Plus.
- Für stationäre Logrenditen ersetzt die Extremwertformel (7.51) den VaR aus (7.28): bei ξn ungleich 0 ist VaR gleich βn minus (αn/ξn) mal {1 minus [minus nθ ln(1 minus p)] hoch (minus ξn)}, bei ξn gleich 0 gleich βn minus αn mal ln[minus nθ ln(1 minus p)]. Dabei ist n die Länge der Teilperiode und θ der Extremalindex.
- Erklärende Variablen machen die Parameter und damit den VaR anpassungsfähig an veränderte Marktbedingungen. Für den Effekt der Marktvolatilität auf den VaR werden zwei Maße verwendet: die Zahl großer Tage in den fünf vorangegangenen Handelstagen und die bedingte Standardabweichung eines gaußschen GARCH(1,1).
- Fallen nachlaufende Volatilität und Korrelationen, bleibt Risikobudget frei, und die Positionen werden ausgeweitet. Die historische Volatilität des S&P 500 ist auf allen gezeigten Maßen gefallen und erzeugt niedrige VaR-Werte.
- Der VaR-Teufelskreis: Volatilität und Korrelation steigen, Fonds stoßen an Limits und verkaufen, dadurch steigen Volatilität und Korrelationen weiter, weitere Fonds müssen verkaufen.
- Für ein großes diversifiziertes Portfolio ist das Risiko proportional zur Wurzel der Korrelation. Mit mittlerer Aufwärts-Halbekorrelation 0,21 und Abwärtskorrelation 0,38 (1970 bis 2004) ist der VaR mit 1,35 zu multiplizieren und unterschätzt das wahre Risiko um 35 Prozent. Ab 1995, Mittel 0,30 gegen 0,44, sind es 21 Prozent, wenn der VaR auf Aufwärtskorrelationen beruht.
- Ändern sich die Volatilitäten zugleich, was äußerst wahrscheinlich ist, ist diese Korrektur nur der Anfang. Die Volatilitäten könnten sich gegenüber den aktuellen Niveaus leicht verdreifachen. Die Unterschätzung des im Aktienmarkt eingegangenen Risikos ist potenziell massiv.

## Voraussetzungen


## Anwendung im Trading

- Die Rechnung gilt einer Long-Position von 10 Millionen Dollar in IBM. Eine Überschreitung bei Schwelle 2,5 Prozent liegt vor, wenn der Tageskurs um mehr als 2,5 Prozent fällt. Die Daten sind tägliche Logrenditen in Prozent vom 3. Juli 1962 bis 31. Dezember 1998.
- Multivariate Volatilitäten lassen sich verwenden, um den Value at Risk einer Finanzposition aus mehreren Assets zu berechnen. Dieselbe bedingte Kovarianzmatrix ist auch für die Portfolioauswahl und die Asset-Allokation wichtig.

## Regeln und Kriterien


## Risiken und Grenzen

- Die Normalannahme unterschätzt den VaR oft, weil Renditen schwere Ränder haben. Die Wurzel-der-Zeit-Regel gilt nur für das IGARCH(1,1) ohne Drift bei Mittelwert null; bei Mittelwert μ ungleich null ist das 95-Prozent-Quantil über k Perioden kμ plus 1,65 mal der Wurzel aus k mal σt+1.
- Die empirische Quantilmethode ist einfach und setzt keine bestimmte Verteilung voraus. Sie nimmt aber an, der prognostizierte Verlust könne den historischen nicht übersteigen, ist bei kleinem p ineffizient und berücksichtigt keine erklärenden Variablen. Der so erhaltene VaR kann als Untergrenze des tatsächlichen VaR dienen.
- Der klassische Extremwert-VaR für IBM liegt bei 5 und 1 Prozent unter dem empirischen Quantil und unter den GARCH-Werten. Bei 0,1 Prozent dreht sich das Verhältnis zur Normalannahme um. Bei 9190 Tagen können die empirischen 5- und 1-Prozent-Quantile als Untergrenzen gelten, bei 0,1 Prozent nicht mehr.
- Für die betrachtete IBM-Reihe reagiert der VaR des neueren Ansatzes wenig auf die Schwelle. Der Text empfiehlt, das Stichprobenmittel zuerst zu entfernen. Gegenüber der klassischen Blockmethode ist das Ergebnis über die drei Schwellen stabiler.
- Wird der Extremalindex übersehen, droht eine Unterschätzung des VaR. Das homogene Poisson-Modell aus Beispiel 7.8 scheint den VaR gegenüber dem inhomogenen Modell zu unterschätzen.
- Viele Modelle behandeln Risiko als exogen. In Turbulenz ist es endogen. Ob der Teufelskreis entsteht, hängt von Hebel und Gleichförmigkeit der Positionen ab. Unterschiedliche Positionen lassen sich kreuzen, identische nicht.
- Während alle denselben Trade aufbauen, sind die gemessenen Volatilitäten und Korrelationen fast sicher zu niedrig.
- LTCM nutzte VaR als Risikokontrolle, ebenso die Bond-Arbitrage-Desks mit denselben Trades. Als die Modelle Gefahr zeigten, folgte die Rückkopplung und ein Notverkauf epischen Ausmaßes.
- Investmentbanken sahen ihre VaR steigen, während sie schwindenden Marktrenditen nachjagten. Das ist beunruhigend, weil die VaR bei fallender Volatilität hätten sinken sollen.
- Dynamisches Hedging und VaR verstärken Markttrends. Fehlt ein fundamentaler Auslöser und scheitert der gemeinsame Reflation-Trade nur, weil alle ihn halten, laufen die Systeme just am Ausgang hoch.

## Beispiele

- Für 10 Millionen Dollar long im D-Mark/Dollar-Kontrakt und eine Tages-Standardabweichung von etwa 0,53 Prozent im Juni 1997 beträgt der 5-Prozent-VaR 87.450 Dollar auf einen Tag und etwa 276.541 Dollar auf zehn Tage.
- Für 10 Millionen Dollar long in IBM am 31. Dezember 1998 liefert RiskMetrics 302.500 Dollar bei 5 Prozent und 426.500 Dollar bei 1 Prozent; das gaußsche AR(2)–GARCH(1,1) liefert 287.700 und 409.738 Dollar, die Student-t mit 5 Freiheitsgraden 283.520 und 475.943 Dollar.
- Dieselbe RiskMetrics-Rechnung in S-Plus mit α = 0,964 und Volatilitätsprognose 0,01888 ergibt 311.520 Dollar bei 5 Prozent und 439.187 Dollar bei 1 Prozent, etwas höher als die Schätzung mit RATS.
- Für die negativen täglichen Intel-Logrenditen vom 15. Dezember 1972 bis 31. Dezember 2008, 9096 Beobachtungen, ist das empirische 95-Prozent-Quantil 4,2952 Prozent.
- Für die negativen IBM-Logrenditen, 9190 Beobachtungen, ist das empirische 95-Prozent-Quantil 0,021603, der 5-Prozent-VaR von 10 Millionen Dollar also 216.030 Dollar. Das empirische 99-Prozent-Quantil liegt bei etwa 3,630 Prozent, der 1-Prozent-VaR bei 363.000 Dollar. Beide Beträge liegen unter den zuvor berechneten ökonometrischen VaR.
- Für das gaußsche AR(2)–GARCH(1,1) ist der 5-Prozent-VaR über 15 Tage ab dem 31. Dezember 1998 für 10 Millionen Dollar 1.039.191 Dollar, kleiner als 287.700 mal der Wurzel aus 15 = 1.114.257 Dollar. Die Wurzel-der-Zeit-Regel gilt damit nur für das spezielle IGARCH(1,1) ohne Drift.
- Mit Blocklänge 63 und den Schätzungen Skala 0,945, Lage 2,583 und Form 0,335 ist der 1-Prozent-VaR der negativen IBM-Tageslogrendite 3,04969 Prozent, also 304.969 Dollar auf 10 Millionen, und der 5-Prozent-VaR 166.641 Dollar. Mit Blocklänge 21, Skala 0,823, Lage 1,902 und Form 0,197 steigen die Werte auf 340.013 und 184.127 Dollar.
- Für den nächsten Handelstag und 10 Millionen Dollar long nennt der Vergleich bei 5 Prozent: RiskMetrics 302.500, gaußsches AR(2)–GARCH 287.200, Student-t mit 5 Freiheitsgraden 283.520, empirisches Quantil 216.030 und klassische Extremwerttheorie mit Blocklänge 21 gleich 184.127 Dollar.
- Bei 1 Prozent lauten dieselben fünf VaR 426.500, 409.738, 475.943, 365.709 und 340.013 Dollar. Bei 0,1 Prozent lauten sie 566.443, 546.641, 836.341, 780.712 und 666.590 Dollar.
- Mit p = 0,01 und Blocklänge 63 ist der 30-Tage-VaR 30 hoch 0,335 mal 304.969 Dollar = 3,125 mal 304.969 = 952.997 Dollar.
- Für negative IBM-Renditen und Blöcke von 21 Tagen ist das Return Level für 12 solche Blöcke 4,4835 Prozent. Die R-Ausgabe von rlevel.gev nennt 4,177923, 4,481976 und 4,858102.
- Im Poisson-Modell ohne Mittelwertkorrektur ergeben die Schwellen 3,0, 2,5 und 2,0 Prozent bei 5 Prozent die VaR 228.239, 219.106 und 212.981 Dollar und bei 1 Prozent 359.303, 361.119 und 368.552 Dollar.
- Nach Abzug des Stichprobenmittels steigen diese VaR auf 232.094, 225.782 und 217.740 Dollar bei 5 Prozent sowie 363.697, 364.254 und 372.372 Dollar bei 1 Prozent.
- Die GPD-Rechnung bei Schwelle 2,5 Prozent liefert für 10 Millionen Dollar die VaR 220.889 und 361.661 Dollar bei 5 und 1 Prozent.
- Am 31. Dezember 1998, x3 gleich 0, x4 gleich 0,9737, x5 gleich 1,9766, ergeben ξ gleich 0,01195, ln(α) gleich 0,19331 und β gleich 6,105. Bei Tail-Wahrscheinlichkeit 0,05 ist das Quantil 3,03756 Prozent und der VaR 303.756 Dollar; bei 0,01 ist der VaR 497.425 Dollar.
- Am 30. Dezember 1998, x3 gleich 1, x4 gleich 0,9737, x5 gleich 1,8757, ergeben ξ gleich 0,2500, ln(α) gleich 0,52385 und β gleich 5,8834. Das 95-Prozent-Quantil ist 2,69139 Prozent, der VaR 269.139 Dollar; bei Tail-Wahrscheinlichkeit 0,01 ist der VaR 448.323 Dollar.
- Das 5-Prozent-VaR des inhomogenen Modells liegt leicht über dem gaußschen AR(2)–GARCH(1,1) aus Beispiel 7.3, das 1-Prozent-VaR über Fall 1 von Beispiel 7.3. Der Einfluss schwerer Ränder ist bei der kleineren Tail-Wahrscheinlichkeit größer.
- Mit Blockschätzer θ gleich 0,823 und n gleich 63 Tagen beträgt das 1-Prozent-VaR der Long-Position für den nächsten Handelstag 3,2714, höher als 3,0497 in Beispiel 7.6 ohne Extremalindex. Die Rechnung 2,583 minus (0,945/0,335) mal {1 minus [minus 63 mal 0,823 mal ln(0,99)] hoch minus 0,335} ergibt 3,271388.
- Bei Schwelle 2,5 Prozent gibt es 334 Überschreitungen, bei Schwelle 3,0 Prozent 184. Der Stichprobenmittelwert der Logrenditen wird vor der Schätzung entfernt; die Summe läuft über 9190 Tage.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 1–20 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-001-p001-p020|S. 1–20]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 20–39 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-002-p020-p039|S. 20–39]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 134–153 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-008-p134-p153|S. 134–153]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 153–172 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-009-p153-p172|S. 153–172]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 343–362 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-019-p343-p362|S. 343–362]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 362–381 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-020-p362-p381|S. 362–381]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 381–400 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-021-p381-p400|S. 381–400]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 400–419 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-022-p400-p419|S. 400–419]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 514–533 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-028-p514-p533|S. 514–533]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 571–590 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-031-p571-p590|S. 571–590]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 628–647 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-034-p628-p647|S. 628–647]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 685–704 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-037-p685-p704|S. 685–704]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 457–476 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-025-p457-p476|S. 457–476]]

## Verwandte Themen
