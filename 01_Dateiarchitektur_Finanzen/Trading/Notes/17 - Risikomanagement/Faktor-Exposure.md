---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/17 - Risikomanagement/17 - Risikomanagement|17 - Risikomanagement]]"
weitere_hauptthemen: []
unterthema: "Portfoliorisiko"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Faktor-Exposure


## Kurzdefinition

- Das Faktor-Exposure ist der Vektor der Faktorladungen aus der Eigenwertzerlegung der Kovarianzmatrix, multipliziert mit dem Allokationsvektor.
- Für Assetrenditen werden drei Arten von Faktormodellen unterschieden, nach Connor (1995) sowie Campbell, Lo und MacKinlay (1997). Makroökonomische Faktormodelle nutzen beobachtbare Größen wie BIP-Wachstum, Zinssätze, Inflationsrate und Arbeitslosenquote und werden mit linearer Regression geschätzt.
- Fundamentale Faktormodelle bilden gemeinsame Faktoren aus firmenspezifischen Merkmalen wie Unternehmensgröße, Buch- und Marktwerten und Branchenzugehörigkeit. Statistische Faktormodelle behandeln die gemeinsamen Faktoren als unbeobachtete latente Variablen, die aus den Renditereihen geschätzt werden.
- Das allgemeine Faktormodell lautet rit = αi + βi1 f1t + … + βim fmt + εit für k Assets und T Perioden. αi ist der Achsenabschnitt, βij die Ladung von Asset i auf Faktor j, εit der spezifische Faktor von Asset i.
- Der gemeinsame Faktor ft ist ein m-dimensionaler stationärer Prozess mit Erwartungswert μf und Kovarianzmatrix Σf. Der spezifische Faktor ist weißes Rauschen mit Erwartungswert null, unkorreliert mit allen gemeinsamen Faktoren und mit den spezifischen Faktoren der anderen Assets. Die gemeinsamen Faktoren müssen in manchen Modellen nicht untereinander unkorreliert sein.
- Die statistische Faktorenanalyse sucht wenige Faktoren, die den größten Teil der Variation in der Kovarianz- oder Korrelationsmatrix der Daten erklären.

## Kernaussagen

- Die Risikoanteile summieren sich zu eins, und jeder Anteil liegt zwischen 0 und 1.
- Wird die Kovarianz auf Preisänderungen statt auf Renditen gerechnet, kann statt der Gewichte ein Bestandsvektor verwendet werden.
- Als Studien Überrenditen TA-basierter Strategien zeigten, erfanden Anhänger der Effizienzmarkthypothese neue Risikofaktoren und behaupteten, die Überrenditen seien nur Ausgleich für Risiken, die gerade dieser Strategie innewohnen.
- Die Effizienzmarkthypothese behauptet nicht, Renditen über dem Markt seien unmöglich, sondern nur, dass höhere Renditen die Übernahme zusätzlichen Risikos verlangen.
- Wären die Renditen der TA-Strategie wirklich Ausgleich für höheres Risiko, bliebe die Effizienzmarkthypothese trotz einer Rendite über dem Marktindex intakt.
- Der Fehler lag darin, den Risikofaktor erst zu konstruieren, nachdem die TA-Studien vorlagen.
- Wissenschaftlich korrekt wäre gewesen, den Risikofaktor vor der Studie zu definieren und vorherzusagen, dass ein Test der TA-Methode scheinbar marktschlagende Renditen erzeugt.
- Stattdessen nahmen sich die Verteidiger die Lizenz, jederzeit einen neuen Risikofaktor zu erfinden, um widersprechende Befunde wegzuerklären, und machten die Hypothese damit unfalsifizierbar.
- Faktormodelle sollen das gemeinsame Muster in Assetrenditen beschreiben und die Portfolioanalyse vereinfachen, weil hochdimensionale Modelle für viele Assets schwer anwendbar sind. Hauptkomponentenanalyse und Faktormodelle für Assetrenditen behandeln auch Alexander (2001) sowie Zivot und Wang (2003).
- Das statistische Faktormodell lautet rt minus µ gleich β ft plus εt, mit weniger Faktoren m als Assets k. Die gemeinsamen Faktoren und die Ladungen βij sind unbeobachtbar, deshalb ist das Modell trotz ähnlicher Form keine multivariate lineare Regression.
- Ein orthogonales Faktormodell verlangt, dass die Faktoren Erwartungswert null und Kovarianz gleich der Einheitsmatrix haben, die spezifischen Fehler Erwartungswert null und diagonale Kovarianz D haben und Faktoren und Fehler unabhängig sind.
- Unter diesen Annahmen ist die Kovarianz der Renditen ββ′ plus D, und die Kovarianz zwischen Renditen und Faktoren ist gleich β.
- Die Varianz einer Renditekomponente ist die Kommunalität plus die spezifische Varianz. Die Kommunalität ist die Summe der quadrierten Ladungen auf die m gemeinsamen Faktoren, der Rest heißt Eindeutigkeit.
- Nicht jede Kovarianzmatrix hat eine orthogonale Faktordarstellung. Hat sie eine, ist diese nicht eindeutig: Jede orthogonale Matrix P erzeugt über β mal P und P′ mal ft ein weiteres orthogonales Modell.
- Diese Nichteindeutigkeit macht die Bedeutung der Ladungen beliebig und erlaubt zugleich Rotationen zu besser interpretierbaren Faktoren. Kommunalitäten und spezifische Varianzen bleiben bei einer orthogonalen Transformation unverändert.
- Das Varimax-Kriterium von Kaiser (1958) wählt die Rotation, die die Quadrate der durch die Wurzel der Kommunalität skalierten Ladungen je Faktor möglichst weit streut, sodass in jeder Spalte Gruppen großer und vernachlässigbarer Koeffizienten entstehen.
- Die traditionelle Faktorenanalyse setzt fehlende serielle Korrelation voraus. Das ist bei Finanzdaten mit wöchentlicher oder höherer Frequenz oft verletzt, bei monatlichen Aktien- oder Indexrenditen aber häufig vertretbar. Bei Verletzung wird die lineare dynamische Abhängigkeit entfernt und die Faktorenanalyse auf die Residuen angewendet.
- Die Hauptkomponentenmethode setzt die Ladungsmatrix aus den mit der Wurzel des Eigenwerts skalierten Eigenvektoren der ersten m Komponenten. Sie braucht weder Normalität noch ein vorher festgelegtes m, gilt für Kovarianz und Korrelation und ist oft nur eine Näherung. Die so geschätzten Ladungen ändern sich nicht, wenn m erhöht wird.
- Die Summe der quadrierten Elemente der Approximationsfehler-Matrix ist höchstens die Summe der Quadrate der vernachlässigten Eigenwerte.
- Die Maximum-Likelihood-Methode setzt gemeinsame Normalität von Faktoren und spezifischen Fehlern voraus, verlangt ein vorgegebenes m und schätzt unter der Nebenbedingung, dass β′ D hoch minus 1 β diagonal ist.
- Bei fünf monatlichen Logrenditen von IBM, Hewlett-Packard, Intel, J.P. Morgan Chase und Bank of America, Januar 1990 bis Dezember 2008, erklären zwei Maximum-Likelihood-Faktoren etwa 60 Prozent der Variabilität. Nach Varimax laden die drei Technologiewerte hoch auf den ersten und die beiden Finanzwerte hoch auf den zweiten rotierten Faktor. Die Rotation vertauscht hier die Reihenfolge der Faktoren. Die spezifische Varianz von IBM ist relativ groß, die Kommunalität beträgt 0,387.
- Bei monatlichen Logrenditen von US-Anleihenindizes mit Laufzeiten 30, 20, 10, 5 und 1 Jahr erklären die ersten zwei Faktoren bei beiden Schätzmethoden mehr als 90 Prozent. Alle Reihen laden ungefähr gleich auf den ersten Faktor, die allgemeinen US-Anleihenrenditen. Die Ladungen auf den zweiten Faktor steigen mit der Restlaufzeit, summieren sich ungefähr auf null und lesen sich als Kontrast zwischen Laufzeiten von 10 Jahren oder mehr und kurzen Laufzeiten.
- Für zehn monatliche Überschussrenditen, Januar 1990 bis Dezember 2003, verwirft der Likelihood-Ratio-Test das Zweifaktorenmodell mit LR(2) gleich 72,96 und einem p-Wert nahe null bei 26 Freiheitsgraden. Das Dreifaktorenmodell hat die Chi-Quadrat-Statistik 26,48 bei 18 Freiheitsgraden und p gleich 0,0892 und gilt auf dem 5-Prozent-Niveau als vertretbar. Faktor 1 steht im Wesentlichen für Finanzdienstleister, Faktor 2 für Hightech und Alcoa, Faktor 3 für Caterpillar und Alcoa als übrigen Industriesektor. Die drei Faktoren erklären zusammen 57,9 Prozent der Varianz.
- Die asymptotische Hauptkomponentenanalyse von Connor und Korajczyk (1986, 1988) ist für kleines T und großes k gedacht. Für k gegen unendlich ist die Eigenanalyse ihrer T-mal-T-Matrix äquivalent zur statistischen Faktorenanalyse, und die Faktorschätzer sind die ersten m Eigenvektoren.
- Connor und Korajczyk (1993) wählen m so, dass die Querschnittsvarianz des spezifischen Fehlers beim Schritt von m auf m plus 1 nicht signifikant sinkt. Bai und Ng (2002) minimieren eines der Informationskriterien Cp1(m) oder Cp2(m). Die beiden Kriterien können verschiedene Faktorzahlen liefern.
- Bei 40 monatlichen einfachen Aktienrenditen, Januar 2001 bis Dezember 2003, mit k gleich 40 und T gleich 36, wählt Connor-Korajczyk einen Faktor und Bai-Ng sechs Faktoren, wobei Cp1 und Cp2 nicht übereinstimmen und der kleinere Wert genommen wird. Die sechs Faktoren erklären etwa 89,4 Prozent der Variabilität.
- Value, Size und Momentum sind gut belegte Lieferanten von Überschussrenditen, können aber zu unangenehm großen Sektorwetten führen.
- Branchenrelative Faktoren mindern diese Sektorwetten und umgehen Probleme unterschiedlicher Rechnungslegungsregime und Kapitalstrukturen.
- Ein niedriges Kurs-Buchwert-Verhältnis kann wegen unterschiedlicher Kapitalanforderungen und Bilanzierungsregeln einen Geschäftstyp definieren statt eine Value-Chance.
- Der Backtest findet, dass Value und Size sektoradjustiert am besten funktionieren, Preismomentum nicht.
- Über die letzten etwa zehn Jahre, geprägt von großen Sektorrotationsschwüngen der TMT-Blase, arbeiteten absolute Bewertung, Momentum und Size im Allgemeinen besser unadjustiert; diese Phase gilt als nicht repräsentativ.
- Über 30 Jahre und in den zehn Jahren vor der Blase hat der sektorrelative Ansatz den marktweiten im Allgemeinen übertroffen.
- Viel Quant-Arbeit wählt Titel über absolute Bewertung und justiert Sektorwetten erst danach, typischerweise über eine Optimierung, obwohl die Research-Teams nach Sektoren organisiert sind.
- Die meisten Value-Strategien profitieren vom sektorrelativen Ansatz, passend zu unterschiedlichen Rechnungslegungsregimen und Kapitalstrukturen; die Ergebnisse der Dividendenrendite sind gemischter.
- Die Höhe der Dividendenrendite hängt weniger an der Branche als an der Ausschüttungsentscheidung des Managements und könnte stärker mit Sektorrotation zusammenhängen als die anderen Value-Strategien.
- Branchenrelatives Preismomentum liefert höhere statistische Signifikanz, aber niedrigere absolute Renditen; das überrascht wenig, weil der Preis selbst nicht von Branchenzusammensetzung oder Rechnungslegung abhängt.
- Für Cashflow-Kurs, Kurs-Gewinn und Kurs-Buchwert gibt es klare Vorteile der sektorrelativen Maße gegenüber den marktweiten; beim Preismomentum liegen die Ergebnisse nur knapp auf der sektorrelativen Seite, interessanter sind meist die höheren absoluten Renditen.
- Die t-Statistiken sind beim sektorrelativen Ansatz im Allgemeinen höher, und die risikobereinigten Renditen der branchenadjustierten Maße sollten besser sein; einige risikobereinigte Renditen sind dürftig und sollen ignoriert werden.
- Weltweit über 30 Jahre, annualisiert mit t-Statistik, liegen sektorrelativ gegen marktweit beim Cashflow-Kurs 10,5 (5,9) gegen 9,7 (4,7), beim Kurs-Gewinn 9,7 (4,3) gegen 9,4 (3,9), beim Kurs-Buchwert 8,8 (4,1) gegen 8,5 (3,7), bei der Dividendenrendite 8,7 (4,0) gegen 8,5 (3,5), bei Small gegen Large 8,2 (5,3) gegen 7,8 (3,9) und beim 6-Monats-Momentum 8,0 (4,3) gegen 9,3 (4,5).
- Japan ist die Ausnahme, in der die nicht adjustierten Bewertungsmaße am besten arbeiteten.
- Asness et al. (2000) und Cohen und Polk (1998) argumentieren, dass branchenrelative Faktoren bessere Renditen liefern und Maße wie das Kurs-Buchwert-Verhältnis stark von Rechnungslegungsstandards abhängen.
- Eine Notiz vom Juni 1996 fand Faktorportfolios innerhalb der Sektoren äquivalent und hoch korreliert mit marktweiten Faktorportfolios, sodass Value- und Momentum-Überschussrenditen auch bei beschränkter Sektorposition bleiben.
- Size arbeitet sektorrelativ, hat als alleinstehende Strategie aber niedrigere Renditen und müsste getimt werden; Small Size tendiert dazu, von einer niedrigen statt hohen Bewertungsbasis zu outperformen, und kann zugunsten sektorrelativer Bewertung ignoriert werden, weil billige Small Caps ohnehin auffallen.
- Im CAPM benutzen alle Anleger die Markowitz-Optimierung, und daraus folgt ein einziger unterscheidender Faktor, Beta.
- Die Faktoren der intertemporalen ICAPM sind unbestimmt, die Theorie bleibt hohl.
- Fundamentalindizes sind passiv und schlagen trotzdem kapitalisierungsgewichtete Indizes; das zeigt, wie schwer Alpha und Beta zu trennen sind.
- Hedgefonds gelten oft als Alpha-Maschinen, die Clone-Angriffe deuten sie aber großteils als Beta-Wetten: lässt sich die Performance mit einem Sechs-Faktoren-Modell nachbilden, bleibt wenig Alpha.
- Das Alpha eines Fonds ändert sich stark mit dem Benchmark. Chan et al. (2006): Large-Cap-Growth von 0,28 bis 4,03 Prozent, Large-Cap-Value von minus 0,64 bis 1,09 Prozent.
- Die Fondsgruppen werden auf Markt, SMB (small minus big), HML (hohes Buch-zu-Preis-Verhältnis minus niedriges) und UMD (up minus down) regressiert.
- Diversifizierte Stockpicker laden mit SMB −0,18, HML 1,33 und UMD 0,05, also auf Large-Cap-Value. Konzentrierte Stockpicker laden mit SMB 1,67, HML −0,23 und UMD 0,15, also auf Small Caps mit leichtem, statistisch nicht bedeutsamem Growth-Bias.
- Sektorwetten laden mit SMB 0,92, HML 0,14 und UMD 0,12. Closet Indexer laden mit SMB 0,17, HML 0,02 und UMD 0,07 und sind damit im Wesentlichen Momentum, im Einklang mit kapitalisierungsgewichteten Indizes.

## Funktionsweise

- Die Kovarianzmatrix der Renditen wird als V mal W gleich W mal Lambda zerlegt, und die Ladungen sind W transponiert mal die Gewichte.
- Die Gewichte summieren sich zu eins.
- Der Risikoanteil einer Hauptkomponente ist ihr quadriertes Loading mal ihrem Eigenwert, geteilt durch die Summe dieser Terme über alle Komponenten.
- In Matrixform ist rt = α + β ft + εt mit diagonaler Kovarianz D der spezifischen Faktoren. Daraus folgt Cov(rt) = β Σf β′ + D. Sind die Faktoren beobachtet, ist das eine Querschnittsregression; die gestapelte Form R = G ξ′ + E ist dann ein multivariates lineares Regressionsmodell, dessen Störkovarianz im allgemeinen Fall nicht diagonal sein muss.
- Sind die Faktoren beobachtet, schätzt die Kleinste-Quadrate-Methode ξ̂′ = (G′G) hoch −1 G′R. Die spezifischen Varianzen stehen auf der Diagonale von Ê′Ê / (T − m − 1). Das R² des Assets i ist 1 minus dem Verhältnis der entsprechenden Diagonalelemente von Ê′Ê und R′R.
- Diese Kleinste-Quadrate-Schätzung erzwingt nicht, dass die spezifischen Faktoren untereinander unkorreliert sind, und ist deshalb im Allgemeinen nicht effizient. Die Orthogonalität verlangt aufwendige Rechnung und wird oft weggelassen. Zur Prüfung sollen die Nebendiagonalen von Ê′Ê / (T − m − 1) nahe null liegen.
- Kann die Zahl der Assets k die Zahl der Zeitpunkte T übersteigen, verweist der Text auf ein Verfahren in Abschnitt 9.6. Üblich ist außerdem die Annahme, Faktoren und damit rt seien seriell unkorreliert; serielle Abhängigkeit der beobachteten Renditen lässt sich mit den Modellen aus Kapitel 8 entfernen.
- Beim BARRA-Ansatz von Bar Rosenberg sind die beobachteten Fundamentals die zeitkonstanten Betas, und die Faktorrealisationen ft werden zu jedem Zeitpunkt per Regression geschätzt und verändern sich über die Zeit. Bei Fama und French (1992) ist die Faktorrealisation die Rendite eines Hedgeportfolios auf dem beobachteten Fundamental, und die Betas werden danach per Zeitreihenregression geschätzt.
- Im BARRA-Modell der mittelwertbereinigten Überschussrenditen ist ft bei gegebenem β mit gewichteten kleinsten Quadraten schätzbar, Gewichte sind die Standardfehler der spezifischen Faktoren, und m muss kleiner als k sein. Praktisch wird zweistufig geschätzt: erst gewöhnliche kleinste Quadrate, dann verallgemeinerte kleinste Quadrate mit der aus den gepoolten Residuen geschätzten Diagonalmatrix. Die Kovarianz der Überschussrenditen ist β Σ̂f β′ + D̂g.
- Im Einfaktor-BARRA-Fall ist die geschätzte Faktorrealisation die Rendite des Portfolios ω, das ein Halb ω′ D ω minimiert unter der Nebenbedingung ω′β = 1. Die Lösung ist ω′ = (β′ D hoch −1 β) hoch −1 β′ D hoch −1. Summieren sich die Gewichte zu eins, heißt ω Factor-Mimicking-Portfolio. Bei mehreren Faktoren wird die Idee je Faktor angewendet.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Dieselbe nachträgliche Immunisierung war schon gegen Studien eingesetzt worden, in denen öffentliche Fundamentaldaten wie das Kurs-Buchwert-Verhältnis und das KGV Überrenditen erzeugten: Niedrige Werte beider Kennzahlen seien nur Signale für Aktien mit abnormal hohem Risiko.
- Diese Risikofaktoren waren vor den Studien nicht definiert worden; nachträglich eigens erfundene Erklärungen dieser Art heißen Ad-hoc-Hypothesen.
- Das Marktmodell ist das bekannteste makroökonomische Einfaktormodell. Für 13 Aktien und den S&P 500 von Januar 1990 bis Dezember 2003 bleiben in der Residuenkorrelation große Werte, etwa 0,45 zwischen Caterpillar und Alcoa und 0,48 zwischen General Motors und Ford. Die Annahme unkorrelierter spezifischer Faktoren ist damit verletzt.
- Chen, Roll und Ross (1986) verwenden unerwartete Änderungen makroökonomischer Variablen, also Residuen nach Entfernen der dynamischen Abhängigkeit, einfach über ein VAR. Im Beispiel sind die Faktoren die Residuen eines per BIC gewählten VAR(3) auf dem CPI-Wachstum und dem Wachstum der Zivilbeschäftigung ab 16 Jahren, eingesetzt von 1990 bis 2003. Alle 13 Überschussrenditen hängen negativ an der CPI-Überraschung, die R² sind niedrig, und die Modellkorrelationsmatrix liegt nahe an der Einheitsmatrix.
- Fama und French nennen drei Fundamentals, die hohe Anteile der Variabilität der Überschussrenditen erklären: die Marktüberschussrendite, SMB als kleine minus große Aktien bei Sortierung nach Marktkapital, und HML als Value minus Growth, wobei Value ein hohes Verhältnis von Buchkapital zu Marktkapital hat.
- Der Faktorbegriff unterscheidet sich zwischen den Modellen. Weil das Modell linear ist, lassen sich Fundamentals zu einem neuen Merkmal zusammenziehen und das Ergebnis als Einfaktormodell bezeichnen; die Faktorzahl ist dann mit Vorsicht zu lesen. In statistischen Faktormodellen ist die Faktorzahl klarer bestimmt.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 286–305 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-016-p286-p305|S. 286–305]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 134–153 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-008-p134-p153|S. 134–153]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 476–495 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-026-p476-p495|S. 476–495]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 495–514 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-027-p495-p514|S. 495–514]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 514–533 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-028-p514-p533|S. 514–533]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 248–267 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-014-p248-p267|S. 248–267]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 400–419 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-022-p400-p419|S. 400–419]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 419–438 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-023-p419-p438|S. 419–438]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 438–457 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-024-p438-p457|S. 438–457]]

## Verwandte Themen
