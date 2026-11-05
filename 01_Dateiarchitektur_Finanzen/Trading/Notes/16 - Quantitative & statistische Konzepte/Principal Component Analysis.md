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

# Principal Component Analysis


## Kurzdefinition

- PCA-Gewichte sind ein Allokationsvektor, dessen Risiken einer vorgegebenen Verteilung über die Hauptkomponenten der Kovarianz folgen.
- Die Hauptkomponentenanalyse erzeugt aus standardisierten Features orthogonale Merkmale und dient hier dazu, lineare Substitutionseffekte vor der Feature-Importance-Analyse abzumildern.
- Die Hauptkomponentenanalyse zerlegt hier die Kovarianzmatrix der Renditen in Eigenvektoren und Eigenwerte, V mal W gleich W mal Lambda.
- Die orthogonalen Hauptkomponenten, die einen vorgegebenen Anteil der Gesamtvarianz erklären, sind das Produkt P = Z W̃ aus der Datenmatrix Z und ausgewählten Eigenvektoren.
- Die Hauptkomponentenanalyse wird als das vermutlich gebräuchlichste statistische Verfahren der Dimensionsreduktion eingeführt. Sie ist die Grundmethode der statistischen Faktorenanalyse und kann auch die Dimension in der multivariaten Analyse senken.
- Für einen k-dimensionalen Zufallsvektor r mit Kovarianzmatrix Σr sucht die Hauptkomponentenanalyse wenige Linearkombinationen der Komponenten, die die Struktur von Σr erklären. Bei monatlichen Logrenditen von k Assets sind das die Hauptquellen der Variation. Das Stichwort ist wenige, damit die multivariate Analyse sich vereinfacht.

## Kernaussagen

- Bei einer Inverse-Varianz-Allokation tragen fast alle Hauptkomponenten Risiko, auch die beiden Komponenten mit der höchsten Varianz.
- Im PCA-Portfolio trägt nur die Komponente mit der niedrigsten Varianz Risiko.
- Ein Substitutionseffekt liegt vor, wenn die geschätzte Wichtigkeit eines Features durch andere verwandte Features sinkt; das ist das ML-Analogon zur Multikollinearität.
- Ein Weg, lineare Substitutionseffekte zu behandeln, ist eine PCA auf den Rohfeatures und die anschließende Feature-Importance-Analyse auf den orthogonalen Features.
- Eine Orthogonalisierung wie die PCA verhindert nicht alle Substitutionseffekte, soll aber zumindest lineare Substitutionseffekte abmildern.
- PCA bewertet Features ohne Labelkenntnis, also ohne Overfitting im Sinne einer Klassifikation.
- Wählt MDI, MDA oder SFI dieselben Features, die PCA als prinzipiell einstuft, spricht das dagegen, dass das Muster vollständig überfittet ist.
- Die Risikoanteile summieren sich zu eins und liegen jeweils zwischen 0 und 1.
- Auf diesen Anteilen setzt Meucci (2009) die entropieinspirierte Konzentrationskennzahl auf.
- Bei den monatlichen Logrenditen von IBM, Hewlett-Packard, Intel, J.P. Morgan Chase und Bank of America, Januar 1990 bis Dezember 2008, erklären die ersten zwei Hauptkomponenten der Korrelationsmatrix etwa 74 Prozent der Gesamtvariabilität. Die erste Komponente, Eigenwert 2,608 und Eigenvektor (0,428, 0,460, 0,451, 0,479, 0,416)′, ist ungefähr gleich gewichtet und steht für die Marktbewegung.
- Die zweite Komponente hat den Eigenwert 1,072 und den Eigenvektor (0,341, 0,356, 0,385, minus 0,469, minus 0,623)′ und trennt Technologie- von Finanzdienstleistungswerten. Die Kovarianzmatrix der Renditen liefert ähnliche Deutungen.
- Die Eigenwerte der Kovarianzmatrix dieses Beispiels sind 284,17, 112,93, 57,43, 46,81 und 29,87 mit kumulierten Anteilen 0,535, 0,748, 0,856, 0,944 und 1,000. Die kumulierten Anteile der Korrelationsmatrix sind 0,522, 0,736, 0,850, 0,940 und 1,000. Die Eigenvektoren stehen in den Spalten.
- Ein informelles Kriterium für die Komponentenzahl ist der Scree-Plot der absteigend geordneten Eigenwerte. Ein Knick, nach dem die restlichen Eigenwerte klein und ungefähr gleich groß sind, zeigt die passende Zahl. In beiden Scree-Plots der fünf Aktien und der fünf Anleihenindizes genügen zwei Komponenten.
- Außer wenn alle Eigenwerte nach der i-ten Komponente null sind, nähern die ersten i Hauptkomponenten die Gesamtvarianz nur an. Eine gute Näherung mit kleinem i macht die Vereinfachung wertvoll.
- Die Hauptkomponentenmethode der Faktorenanalyse bildet die Ladungsmatrix aus den mit der Wurzel des Eigenwerts multiplizierten ersten m Eigenvektoren. Die geschätzten Ladungen ändern sich nicht, wenn die Zahl der gemeinsamen Faktoren erhöht wird.
- Der quadratische Approximationsfehler dieser Faktorlösung ist durch die Summe der Quadrate der vernachlässigten Eigenwerte nach oben beschränkt.
- Die asymptotische Hauptkomponentenanalyse von Connor und Korajczyk (1986, 1988) gilt für großes k und kleines T. Sie analysiert eine T-mal-T-Matrix der abweichungsbereinigten Renditen. Für k gegen unendlich ist sie äquivalent zur statistischen Faktorenanalyse, und die Faktorschätzer sind die ersten m Eigenvektoren.
- Die Verfeinerung startet mit diesen Eigenvektoren, schätzt je Asset per OLS die Residuenvarianz auf den Faktoren, skaliert die Renditen mit der inversen Wurzel dieser Varianzen und wiederholt die Eigenanalyse.
- Bai und Ng (2002) wählen die Faktorzahl durch Minimieren von Cp1(m) oder Cp2(m) für m zwischen 0 und einem vorgegebenen Maximum. Die beiden Kriterien können verschiedene Zahlen wählen.
- Bei 40 stark gehandelten NASDAQ- und NYSE-Aktien, Januar 2001 bis Dezember 2003, ist k gleich 40 und T gleich 36. Connor-Korajczyk wählt einen Faktor, Bai-Ng sechs, und der kleinere der beiden nicht übereinstimmenden Bai-Ng-Werte wird verwendet. Sechs Faktoren erklären etwa 89,4 Prozent der Variabilität.
- Im Scree-Plot dieser asymptotischen Analyse lauten die kumulierten Varianzanteile der ersten sieben Faktoren 0,446, 0,648, 0,779, 0,829, 0,865, 0,894 und 0,909.
- Für multivariate Volatilität wird eine PCA genutzt, um die Dimension zu senken und die Volatilität dennoch genau zu nähern: ein Volatilitätsmodell für die ausgewählten Hauptkomponenten, danach die Volatilität jeder Reihe an diese Komponenten gekoppelt.
- Die PCA der Kovarianz der Innovationen at aus dem bivariaten AR(3) der monatlichen prozentualen Logrenditen von IBM und dem S&P 500 hat die Eigenwerte 63,373 und 13,489. Die erste Komponente erklärt 82,2 Prozent der verallgemeinerten Varianz. Der gemeinsame Faktor ist xt gleich 0,797 a1t plus 0,604 a2t.
- Weil die serielle Abhängigkeit der Renditen schwach ist, liefert die PCA direkt auf rt fast dieselben Eigenwerte 63,625 und 13,513. Die erste Komponente erklärt etwa 82,5 Prozent, xt gleich 0,796 r1t plus 0,605 r2t. Der Effekt der bedingten Mittelwertgleichungen auf die PCA ist vernachlässigbar.
- Der eine Faktor erklärt nur etwa 82,5 Prozent der verallgemeinerten Varianz. Das danach gebaute Volatilitätsmodell behandelt die bedingte Heteroskedastizität vor allem bei höheren Lags nicht ausreichend.

## Funktionsweise

- Ausgangspunkt ist ein IID-multivariater Gauß-Prozess mit Mittelwertvektor und Kovarianzmatrix, etwa für Aktienrenditen, Änderungen von Anleiherenditen oder Änderungen von Optionsvolatilitäten.
- Die Spektralzerlegung sortiert die Eigenvektoren so, dass die Eigenwerte auf der Diagonalen absteigend geordnet sind.
- Das Portfoliorisiko ist das Quadrat von Sigma gleich Omega transponiert mal Kovarianz mal Omega und zugleich Beta transponiert mal Lambda mal Beta.
- Beta ist die Projektion der Allokation auf die orthogonale Basis.
- Der Risikoanteil der n-ten Komponente ist das Produkt aus dem Quadrat von Beta n und dem Eigenwert n, geteilt durch die Portfoliovarianz, und die Anteile summieren sich zu 1.
- In der orthogonalen Basis ist Beta n gleich Sigma mal der Quadratwurzel aus dem Quotienten von vorgegebenem Risikoanteil und Eigenwert.
- In der ursprünglichen Basis ist die Allokation das Produkt aus der Eigenvektormatrix und Beta.
- Ein Umskalieren der Allokation skaliert nur Sigma und lässt die Risikoverteilung unverändert.
- Ist keine Risikoverteilung vorgegeben, liegt das gesamte Risiko auf der Hauptkomponente mit dem kleinsten Eigenwert.
- Die Gewichte sind dann der letzte Eigenvektor, skaliert auf das Zielrisiko.
- Zuerst wird die standardisierte Matrix Z gebildet, indem jedes Feature um seinen Mittelwert zentriert und durch seine Standardabweichung geteilt wird.
- Danach werden Eigenwerte und Eigenvektoren so bestimmt, dass Z′ZW = WΛ gilt, wobei Λ eine absteigend sortierte Diagonalmatrix und W eine orthonormale Matrix ist.
- Die orthogonalen Features sind P = ZW, und ihre Orthogonalität folgt daraus, dass P′P = Λ ist.
- Die Diagonalisierung erfolgt auf Z statt auf X, weil die Zentrierung die erste Hauptkomponente in die Hauptrichtung der Beobachtungen ausrichtet, analog zu einem Intercept in der linearen Regression.
- Das Reskalieren lenkt die PCA auf Korrelationen statt auf Varianzen; ohne Reskalierung würden die ersten Hauptkomponenten von den Spalten mit der höchsten Varianz dominiert.
- Snippet 8.5 bestimmt die kleinste Zahl orthogonaler Features, die mindestens 95 % der Varianz von Z erklären.
- Die Faktorladungen eines Portfolios sind die transponierte Eigenvektormatrix mal den Allokationsvektor, dessen Gewichte sich zu eins summieren.
- Der Risikoanteil der i-ten Hauptkomponente ist das quadrierte Loading mal dem zugehörigen Eigenwert, normiert auf die Summe über alle Komponenten.
- Die Zerlegung lautet Z′Z W = W Λ, mit der Eigenvektormatrix W und der Eigenwertmatrix Λ.
- W̃ enthält die ersten M Spalten von W, mit M ≤ N, sodass der Anteil dieser Eigenwerte an der Summe aller Eigenwerte mindestens τ ist.
- τ liegt zwischen 0 und 1 einschließlich.
- Die Berechnung lässt sich in eine Summe von Teilprodukten Zb W̃b zerlegen, indem die Spalten in B Teilmengen geteilt werden.
- Zb enthält nur die b-te Spaltengruppe und ist ansonsten leer.
- Die Teilergebnisse werden fortlaufend addiert.
- getPCs lädt die Blöcke nacheinander, sodass bei hinreichend großem B der Arbeitsspeicher nicht erschöpft wird.
- Dieselbe Zerlegung wird parallel ausgeführt und verkürzt damit die Rechnung.
- Die Analyse gilt für die Kovarianzmatrix oder für die Korrelationsmatrix. Die Korrelationsmatrix ist die Kovarianz des standardisierten Vektors r∗ = S hoch −1 r.
- Die Linearkombination yi = w′i r ist bei einfachen Renditen die Rendite eines Portfolios mit Gewichten wij. Die Gewichte werden auf w′i wi = 1 normiert, weil ein skalarer Faktor die Anteilsverhältnisse nicht ändert. Varianz und Kovarianz sind w′i Σr wi und w′i Σr wj.
- Die erste Hauptkomponente maximiert die Varianz unter w′1 w1 = 1. Die zweite maximiert die Varianz unter Einheitsnorm und Kovarianz null mit der ersten. Die i-te ist unkorreliert mit allen vorherigen und hat Einheitsnorm.
- Weil Σr nichtnegativ definit ist, hat sie die Spektralzerlegung mit λ1 ≥ … ≥ λk ≥ 0. Nach Resultat 9.1 ist die i-te Hauptkomponente yi = e′i r, ihre Varianz ist der Eigenwert λi, und verschiedene Hauptkomponenten sind unkorreliert. Bei gleichen Eigenwerten sind die Eigenvektoren und damit die Komponenten nicht eindeutig.
- Die Summe der Komponentenvarianzen ist die Spur von Σr und gleich der Summe der Eigenwerte und gleich der Summe der Varianzen der Hauptkomponenten. Der vom i-ten Anteil erklärte Teil der Gesamtvarianz ist λi geteilt durch die Summe aller Eigenwerte. Gewählt wird ein kleines i mit großem kumuliertem Anteil. Bei der Korrelationsmatrix ist dieser Anteil λi / k, weil die Spur gleich k ist.
- Ein Eigenwert null bedeutet eine exakte lineare Beziehung. Ist λk = 0, ist die zugehörige Linearkombination konstant, und r enthält nur k−1 zufällige Größen. Deshalb dient die Hauptkomponentenanalyse der Dimensionsreduktion.
- In der Anwendung werden Kovarianz und Korrelation unter Regularitätsbedingungen konsistent durch die Stichprobenmatrizen geschätzt, wenn die Renditen schwach stationär sind. Der Teiler ist T−1. Eigenwerte und Eigenvektoren der symmetrischen Stichprobenmatrix liefern die Komponenten. In R und S-Plus heißt der Grundbefehl princomp, in FinMetrics mfactor.
- Ein Faktor-Volatilitätsmodell beginnt mit einer Hauptkomponentenanalyse der Schocks at gleich rt minus µt. Danach wird den ersten Komponenten, die einen hohen Anteil der Variabilität erklären, ein Volatilitätsmodell angepasst, und die Volatilität jeder einzelnen Reihe wird an diese Faktorvolatilitäten gekoppelt. Die Dimension sinkt, die Näherung der multivariaten Volatilität soll erhalten bleiben.
- Die Hauptkomponentenanalyse zerlegt x Reihen in x minus 1 neue Reihen, die untereinander unkorreliert sind.
- Aus neun ähnlichen Blasen werden so acht untereinander unverbundene Hauptkomponenten.
- Benutzt wird nur die erste Hauptkomponente, das gemeinsame Kernmuster der neun Blasen; Abbildung 41.6 zeigt sie als archetypische Blase.

## Voraussetzungen

- Die Kovarianzmatrix muss hermitesch sein.
- Die beschriebene PCA geht von einer Matrix stationärer Features aus, mit Beobachtungen t von 1 bis T und Variablen n von 1 bis N.

## Anwendung im Trading

- Der so bestimmte Allokationsvektor ist eine Möglichkeit, die Gewichte für den ETF-Trick zu bilden.
- Neben der Behandlung von Substitutionseffekten kann die Orthogonalisierung die Dimension von X senken, indem Merkmale zu kleinen Eigenwerten entfallen, was die Konvergenz von ML-Algorithmen meist beschleunigt.
- Die Analyse läuft dann auf Features, die dazu bestimmt sind, die Struktur der Daten zu erklären.

## Regeln und Kriterien

- Das gewichtete Kendall-Tau zwischen den Feature Importances und den zugehörigen Eigenwerten, gleichbedeutend mit dem inversen PCA-Rang, liegt näher bei 1, wenn beide Rangfolgen stärker übereinstimmen.
- Ein gewichtetes Kendall-Tau wird dem gewöhnlichen vorgezogen, weil die Rangübereinstimmung bei den wichtigsten Features Vorrang hat und die Übereinstimmung bei irrelevanten, vermutlich verrauschten Features weniger zählt.
- Weil weightedtau höhere Werte stärker gewichtet, wird die Korrelation auf dem inversen PCA-Rang berechnet.

## Risiken und Grenzen

- In realen Machine-Learning-Anwendungen enthält Z oft Milliarden Datenpunkte.
- Manche dieser Probleme lassen sich wegen des Speicherbedarfs ohne Parallelisierung nicht lösen, auch wenn man länger auf das Ergebnis warten würde.

## Beispiele

- Im Streudiagramm der Eigenwerte gegen die MDI-Werte beträgt die Pearson-Korrelation 0,8491 bei einem p-Wert unter 1E-150.
- Das hyperbolisch gewichtete Kendall-Tau zwischen Feature Importance und Eigenwerten beträgt in der Stichprobe von Abbildung 8.1 0,8206.
- Im Scipy-Beispiel mit den Importances 0,55, 0,33, 0,07 und 0,05 sowie den PCA-Rängen 1, 2, 4 und 3 ergibt das gewichtete Kendall-Tau auf dem inversen PCA-Rang 0,8133.
- Beispiel 9.1 verwendet die monatlichen Logrenditen einschließlich Dividenden von IBM, Hewlett-Packard, Intel, J.P. Morgan Chase und Bank of America von Januar 1990 bis Dezember 2008, 228 Beobachtungen, in Prozent. Renditen derselben Branche zeigen ähnliche Muster. Der Stichprobenmittelvektor ist (0,70, 0,99, 1,20, 0,82, 0,41)′.
- Auf der Stichprobenkovarianz sind die Eigenwerte 284,17, 112,93, 57,43, 46,81 und 29,87, die Varianzanteile 0,535, 0,213, 0,108, 0,088 und 0,056 und die kumulierten Anteile 0,535, 0,748, 0,856, 0,944 und 1.
- Auf der Stichprobenkorrelation sind die Eigenwerte 2,607, 1,072, 0,569, 0,451 und 0,301, die Anteile 0,522, 0,214, 0,114, 0,090 und 0,060 und die kumulierten Anteile 0,522, 0,736, 0,850, 0,940 und 1. Der Text nennt für die ersten beiden Eigenwerte 2,608 und 1,072 und einen erklärten Anteil von etwa 74 Prozent.
- Der erste Eigenvektor der Korrelationsmatrix, etwa (0,428, 0,460, 0,451, 0,479, 0,416)′, ist eine ungefähr gleich gewichtete Linearkombination und kann die allgemeine Marktbewegung darstellen. Der zweite, etwa (0,341, 0,356, 0,385, −0,469, −0,623)′, ist der Unterschied zwischen Technologie und Finanzdienstleistern und kann eine Branchenkomponente sein. Ähnliche Deutungen ergeben sich aus der Kovarianzmatrix.
- Ein informelles Verfahren zur Wahl der Komponentenzahl ist der Scree-Plot, der die Eigenwerte vom größten zum kleinsten gegen ihren Index abträgt. Gesucht wird ein Knick. Abbildung 9.5(a) zeigt diesen Plot für die fünf Aktienrenditen.
- Für die monatlichen Logrenditen von IBM und dem S&P 500 hat die Kovarianz der Innovationen die Eigenwerte 63,373 und 13,489. Der erste erklärt 82,2 Prozent der verallgemeinerten Varianz. Der zugehörige Faktor ist xt gleich 0,797 mal a1t plus 0,604 mal a2t.
- Dieselbe Zerlegung direkt auf den Renditen liefert die Eigenwerte 63,625 und 13,513, im Wesentlichen dieselben Werte. Der erste Faktor erklärt etwa 82,5 Prozent und lautet xt gleich 0,796 mal r1t plus 0,605 mal r2t. Weil die serielle Abhängigkeit der Renditen schwach ist, ist der Effekt der bedingten Mittelgleichungen auf die Hauptkomponentenanalyse vernachlässigbar. Für die weitere Modellierung wird der renditebasierte Faktor verwendet.
- Die neun Blasen mit Gipfeljahr sind South Sea 1720, UK 1840er mini 1837, UK 1840er maxi 1845, US 1929, Silber 1980, Gold 1980, Japan 1990, Thailand 1996 und Chinese Red Chips 1997.
- Die Regression des S&P 500 auf diese erste Hauptkomponente und die daraus erzeugten Prognosen stützen das frühere Blasenmodell.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 58–77 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-004-p058-p077|S. 58–77]]
- Advances in Financial Machine Learning.pdf, S. 134–153 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-008-p134-p153|S. 134–153]]
- Advances in Financial Machine Learning.pdf, S. 286–305 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-016-p286-p305|S. 286–305]]
- Advances in Financial Machine Learning.pdf, S. 324–343 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-018-p324-p343|S. 324–343]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 476–495 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-026-p476-p495|S. 476–495]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 495–514 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-027-p495-p514|S. 495–514]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 514–533 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-028-p514-p533|S. 514–533]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 552–571 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-030-p552-p571|S. 552–571]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 571–590 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-031-p571-p590|S. 571–590]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 533–552 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-029-p533-p552|S. 533–552]]

## Verwandte Themen
