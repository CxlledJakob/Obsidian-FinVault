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

# Beta-Exposure


## Kurzdefinition

- Alpha ist im Capital-Asset-Pricing-Modell der Achsenabschnitt, den man erhält, wenn die Renditen einer Anlagestrategie auf die Renditen eines Marktindex regressiert werden.
- Alpha ist der Teil der Rendite, der nicht der Volatilität der Strategie, also ihrem Beta, zuzurechnen ist.
- Im allgemeinen Faktormodell ist βij die Faktorladung des Assets i auf den Faktor j, und αi ist der Achsenabschnitt. Im Marktmodell von Sharpe (1970) ist rit = αi + βi rmt + εit die Überschussrendite des Assets auf die Überschussrendite des Marktes, und βi ist das Beta der Aktienrendite.

## Kernaussagen

- Verdienstliche Anlagestrategien haben Alphas, die in statistisch signifikantem Grad positiv sind.
- Das CAPM mit zeitvariablem Achsenabschnitt und zeitvariabler Steigung lautet rt gleich αt plus βt mal rM,t plus et, et normal mit Varianz σ²e. rt ist die Überschussrendite der Anlage, rM,t die Überschussrendite des Marktes.
- Alpha und Beta folgen Random Walks: αt plus 1 gleich αt plus ηt mit Varianz σ²η, und βt plus 1 gleich βt plus εt mit Varianz σ²ε. Die Innovationen et, ηt und εt sind gegenseitig unabhängig.
- Im Zustandsraum ist der Zustand (αt, βt)′, die Übergangs- und die Auswahlmatrix sind die 2-mal-2-Einheitsmatrix, die Beobachtungszeile ist (1, rM,t), die Messfehlervarianz ist σ²e und die Zustandsinnovationskovarianz ist diagonal mit σ²η und σ²ε.
- Für die monatlichen einfachen Überschussrenditen von General Motors, Januar 1990 bis Dezember 2003, ist der Markt die Überschussrendite des S&P-500-Composite. Zur Spezifikation werden (ση, σε, σe) gleich (0,02, 0,04, 0,1) angesetzt. Die Datenmatrix hat 168 Zeilen.
- Bei diffuser Initialisierung steht in der Startmatrix minus 1 auf den beiden Diagonalen der Zustände.
- Das einfache Marktmodell rt gleich β0 plus β1 mal rM,t plus et, t von 1 bis 168, wird als Zustandsraumregression geschrieben. rM,t ist zum Beispiel die Rendite des S&P-500-Composite.
- Der Zustand ist der feste Koeffizientenvektor. Die Übergangsmatrix ist die Einheitsmatrix, die Zustandsinnovationskovarianz ist null, und es wird diffus initialisiert.
- Lässt man die Koeffizienten wandern, βt plus 1 gleich βt plus Rt ηt mit ηt standardnormal und Rt gleich dem Vektor der σi, dann ist ein einzelner Beta- oder Alpha-Koeffizient zeitlich konstant, sobald sein σi gleich 0 ist.
- Das feste Marktmodell der monatlichen einfachen Überschussrenditen, in Prozent, lautet rt = α + β rM,t + et mit et ∼ N(0, σ²e), hier für t = 1 bis 168.
- Graham: Beta ist ein mehr oder weniger nützliches Maß vergangener Preisschwankungen von Stammaktien.
- Was Graham stört, ist, dass Autoritäten die Beta-Idee mit dem Begriff Risiko gleichsetzen.
- Graham trennt: Preisvariabilität ja, Risiko nein.
- Echtes Anlagerisiko misst sich nach Graham nicht an dem Prozent, um den eine Aktie in einer gegebenen Periode relativ zum Gesamtmarkt im Preis fallen kann, sondern an der Gefahr, Qualität und Ertragskraft durch wirtschaftliche Änderungen oder eine Verschlechterung des Managements zu verlieren.
- Chan et al. (2006) finden von 1989 bis 2001 ein durchschnittliches Alpha von 2,6 Prozent p.a. für US-Wachstumsmanager und 1,2 Prozent p.a. für Value-Manager.
- Houge und Loughran (2006) teilen US-Fondsmanager nach der Faktorladung auf die Value-Prämie: das Quartil mit der höchsten Ladung sind Value-Investoren, das mit der niedrigsten Growth.
- Von 1965 bis 2002 rentierte das Value-Universum mit 16 Prozent p.a. und Value-Manager nach Gebühren mit 11 Prozent; das Growth-Universum rentierte mit 10 Prozent und Growth-Manager nach Gebühren mit 9,9 Prozent.
- Eine Struktur, die long im Value-Beta ist und das Alpha eines momentum-nutzenden Growth-Managers transportiert, gilt als attraktiv, weil Growth-Manager relativ zu ihrem Universum leichter abnormale Renditen erzeugen.
- Jede Nennung von Alpha und Beta ruft das CAPM auf, weil die Trennung von Alpha und Beta aus dem Modell stammt; ohne CAPM haben Alpha und Beta keine Bedeutung.
- Das CAPM ist empirisch haltlos: Beta ist keine gute Beschreibung von Risiko, und über die lange Frist besteht im Wesentlichen kein Zusammenhang zwischen Beta und Rendite.
- Das CAPM unterschätzt die Renditen von Niedrig-Beta-Aktien massiv und überschätzt die Renditen von Hoch-Beta-Aktien.
- Fama und French (2004) schätzen jeden Dezember 1923 bis 2003 für jede Aktie an NYSE, AMEX und NASDAQ ein Beta aus zwei bis fünf Jahren früherer Monatsrenditen, bilden zehn Portfolios und verfolgen die Rendite über die nächsten zwölf Monate; die CAPM-Gerade wird klar verletzt.
- Fisher Black schlug 1993 eine strategische Neigung zu niedrigem Beta und gegen hohes Beta vor.
- Vuolteenaho (2006), Jensen-Alpha 1927 bis 2004: innerhalb von Growth, niedriges Buch-zu-Preis, liegt die Differenz aus long niedrigem Beta und short hohem Beta im Schnitt bei 5 Prozent; innerhalb von Value, hohes Buch-zu-Preis, bei 8,3 Prozent p.a. Die Beta-Arbitrage ist kein bloßer Value-Proxy.
- Grantham (2006): unter den 600 größten US-Aktien seit 1963 haben die niedrigsten Betas die höchste Rendite und die höchsten Betas die niedrigste, das Gegenteil der CAPM-Vorhersage; die Abbildung der relativen Renditen läuft 1963 bis 2006.
- In Europa hat niedriges Beta im Schnitt hohes Beta geschlagen, Abbildung 1986 bis 2006.
- Das CAPM sagt vorher, der kapitalisierungsgewichtete Index sei mittelwert-varianz-effizient, weil alle Anleger dasselbe, das wertgewichtete Marktportfolio, halten. Clarke et al. (2006) zeigen ein Minimum-Varianz-Portfolio mit höherer Rendite und niedrigerem Risiko als der Marktindex.
- Fundamentalindizes auf Gewinn und Dividenden, passiv und regelbasiert, schlugen die kapitalisierungsgewichteten MSCI-Pendants 1984 bis 2004 im Schnitt um 278 Basispunkte p.a. bei im Schnitt 53 Basispunkten niedrigerer Volatilität; die Grenze zwischen Alpha und Beta ist damit verwischt.
- Das CAPM scheitert an Annahmen, die der Realität widersprechen. Zwei kritische: jede Position, long oder short, in jeder Größe ohne Preiseinfluss, und alle Anleger benutzen die Markowitz-Optimierung. Selbst Harry Markowitz benutzt sie nicht.
- Markowitz (2005): fällt die Annahme unbegrenzter Kreditaufnahme, ändern sich die Schlüsse drastisch, der kapitalisierungsgewichtete Markt ist nicht mehr optimal und Beta ist nicht mehr linear mit der Rendite verbunden.
- Für Anleger, die auf Tracking Error starren, ist der risikofreie Bezug nicht ein Zinssatz, sondern der Marktindex. Niedriges und hohes Beta haben keine Bedeutung, wenn das Universum im Tracking Error aufgespannt ist; aktives Management ist zu Benchmark-Beta geworden.
- Die Fixierung auf Alpha und Beta lenkt von der Aufgabe ab, Renditen zu erzeugen, und eine ganze Industrie für Portable Alpha setzt ein gültiges CAPM voraus.
- Portable Alpha eines Managers mit Universum Russell 1000, auf das Beta des S&P 500 gesetzt, kann dieselben Aktien long und short halten, weil beide Large-Cap-Inlandsindizes sich stark überlappen; die Kosten des Short sind dann verschwendet.
- Portable Alpha ergibt nur Sinn, wenn das Alpha mit allen Elementen des bestehenden Portfolios unkorreliert ist. Japanisches Alpha auf ein S&P-500-Beta scheitert, wenn das Portfolio japanische Aktien schon hält.
- Alpha hängt stark vom Benchmark ab. Chan et al. (2006): die Alphas großer Growth-Fonds reichten je nach Benchmark von 0,28 bis 4,03 Prozent, bei Large-Cap-Value von minus 0,64 bis 1,09 Prozent.
- Fama und French (2004): die empirische Bilanz des CAPM ist schlecht genug, um die Art zu entwerten, wie es in Anwendungen benutzt wird. Die ICAPM lässt ihre Faktoren unbestimmt und bleibt hohl; die Ausrede, das CAPM lasse sich nicht wirklich testen, nützt Praktikern nicht.
- Ben Graham: Beta ist ein mehr oder weniger nützliches Maß vergangener Kursschwankungen. Preisvariabilität ja, Risiko nein. Echtes Risiko ist der Verlust von Qualität und Ertragskraft durch wirtschaftliche Änderung oder Verschlechterung des Managements.
- Im CAPM der frühen 1960er von Sharpe, Litner und Treynor folgt aus der Annahme, alle nutzten die Markowitz-Optimierung, ein einziger Faktor, Beta.
- Fundamentalindizes schlagen nach Rob Arnott kapitalisierungsgewichtete Indizes und sind dennoch passiv; daran zeigt sich, wie schwer Alpha und Beta zu trennen sind.
- Portable Alpha ergibt nur Sinn, wenn das Alpha mit allen Bestandteilen des bestehenden Portfolios unkorreliert ist.
- Das Alpha eines Fonds ändert sich stark mit der Benchmark. Chan et al. (2006) finden bei Large-Cap-Growth-Fonds Alphas von 0,28 Prozent bis 4,03 Prozent je nach Benchmark, bei Large-Cap-Value-Managern von minus 0,64 Prozent bis 1,09 Prozent.
- Alpha und Beta sind bequeme Kürzel für den Mehrwert von Fondsmanagern und für Marktvolatilität, können aber die eigentliche Aufgabe behindern, Gesamtrendite zu erzeugen.
- Viele Hedgefonds wirken als Beta-Wetten. Schließt man die Dedicated-Short-Fonds aus, die negativ zu Wetten auf steigende Märkte korrelieren sollten, steigt die mediane Strategiekorrelation von 0,56 auf 0,65.
- Die einzig genannte plausible Erklärung für diese Korrelation über Emerging-Market-Debt, Equity Long/Short und Global Macro ist, dass die Fonds dasselbe tun: Beta oder Momentum mitreiten oder Volatilität verkaufen.
- Jedes Mal, wenn der Aktienmarkt fällt oder die Volatilität steigt, scheinen alle Hedgefonds-Stile Geld zu verlieren.
- Für Pensionsfonds ergibt es wenig Sinn, hohe Gebühren zu zahlen, wenn Strategien wie der Verkauf von Volatilität die eigentlichen Treiber der Hedgefonds-Performance sind.
- Cremers und Petajisto (2006) regressieren die Fonds auf ein Vier-Faktoren-Modell nach Fama und French: Markt, Größe SMB, Stil HML und Momentum UMD. Fett gedruckte Ladungen sind statistisch signifikant.
- Die Faktorbetas lauten: diversifizierte Stockpicker SMB −0,18, HML 1,33, UMD 0,05; konzentrierte Stockpicker SMB 1,67, HML −0,23, UMD 0,15; Sektorwetten SMB 0,92, HML 0,14, UMD 0,12; Closet Indexer SMB 0,17, HML 0,02, UMD 0,07.
- Diversifizierte Stockpicker sind danach Large-Cap-Value. Konzentrierte Stockpicker liegen bei Small Caps mit leichtem Growth-Bias, der nicht statistisch bedeutsam ist. Closet Indexer sind im Wesentlichen Momentum-Spieler, weil kapitalisierungsgewichtete Indizes das so vorgeben.
- Diversifizierte und konzentrierte Stockpicker haben echtes Alpha, brutto und netto. Die diversifizierten führen beim Bruttoalpha und behalten den Vorsprung netto; die konzentrierten haben etwas höhere Gebühren. Sektorwetten haben negatives Bruttoalpha und netto fast −2 Prozent pro Jahr. Closet Indexer vernichten auf Nettoalpha-Ebene Wert.
- Von je 100 Dollar in aktiv verwalteten, also nicht passiven, US-Aktienfonds gehen mindestens 68 Dollar an Manager mit negativem Nettoalpha. Dieselbe Größenordnung gilt für je 100 Dollar in inländischen US-Publikumsfonds.
- Alpha zu erzeugen ist definitionsgemäß ein Nullsummenspiel: Die Gewinne des einen sind unmittelbar die Verluste eines anderen.
- Eine Benchmark bleibt für die Leistungsmessung sinnvoll, um Können von bloßem Laden auf Marktrisiko zu trennen.
- Asness et al. (2001), Hedgefonds 1994 bis 2000: Viel zu viele Fonds haben negatives Alpha und haben nur Betarisiko geladen. Sie sind effektiv Momentum-Spieler.
- Annualisiertes Alpha und die Summe aller Betas: aggregierter Hedgefondsindex −4,45 Prozent und 0,84; Convertible Arbitrage −0,98 und 0,43; Event Driven −2,12 und 0,61; Equity Market Neutral 3,36 und 0,2; Fixed Income Arbitrage −3,78 und 0,36; Long/Short Equity −2,83 und 0,99; Emerging Markets −16,2 und 1,25; Global Macro −6,64 und 0,98; Managed Futures 1,72 und −0,19; Dedicated Short Bias 11,59 und −1,27.
- Positives Alpha haben in dieser Tabelle nur Equity Market Neutral, Managed Futures und Dedicated Short Bias. Emerging Markets verbinden das schlechteste Alpha mit einem Beta über eins.
- Viele Fonds halten schwer zu bewertende OTC-Titel oder illiquide Assets. Asness et al. summieren deshalb das Beta über die laufende und die verzögerten Monatsmarktrenditen, statt nur die gleichzeitige Marktrendite zu nutzen.
- Sauber gebaute Hedgefonds sollten das Alpha erzeugen können, nach dem die Kundenfrage sucht. Vor den bestehenden Fonds ist zu warnen, weil zu viele gehebelte Long-Fonds sind.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- Zeitvariable Korrelationen lassen sich verwenden, um das zeitvariable Beta des Marktmodells für eine Renditereihe zu schätzen.
- Für gute langfristige Performance wird geraten, niedrig-Beta-Aktien zu kaufen. Die Schildkröte schlägt den Hasen am Ende; verwiesen wird auf Clarke, de Silva und Thorley 2006.

## Regeln und Kriterien


## Risiken und Grenzen

- Wird das Alpha eines Managers mit Universum Russell 1000 auf das Beta des S&P 500 aufgepfropft, können sich zwei Large-Cap-Inlandindizes stark überlappen. Der Anleger ist potenziell gleichzeitig long und short derselben Aktie, und die Kosten des Short sind verschwendet.
- Auch ein japanisches Aktien-Alpha auf einem S&P-500-Beta scheitert, wenn das Gesamtportfolio bereits japanische Aktien und damit japanisches Beta enthält: wieder long und short dasselbe.
- Hedgefonds gelten oft als Alpha-Maschinen. Der sogenannte Angriff der Klone deutet darauf, dass sie großteils besseres Beta sind. Lässt sich die Performance wie von den Klon-Anbietern behauptet mit einem Sechs-Faktoren-Modell nachbilden, bleibt wenig Alpha.
- In einer Welt ohne CAPM gibt es keine beta-adjustierte Rendite. Als übliches Maß der Risikoadjustierung misst sie nichts und kann das Bild der Performance erheblich verzerren.

## Beispiele

- Geschätzt werden monatliche Überschussrenditen von 13 Aktien auf den S&P 500 von Januar 1990 bis Dezember 2003, also k = 13 und T = 168. Der risikolose Zins ist der 3-Monats-Treasury-Bill des Sekundärmarkts, die Renditen sind in Prozent.
- Die geschätzten Betas, dahinter die Residualstandardabweichung und das R², lauten: Alcoa 1,292, 7,694, 0,347; A.G. Edwards 1,514, 7,808, 0,415; Caterpillar 0,941, 7,725, 0,219; Ford 1,219, 8,241, 0,292; FedEx 0,805, 8,854, 0,135; General Motors 1,046, 8,130, 0,238; Hewlett-Packard 1,628, 9,469, 0,358.
- Weitere Betas derselben Schätzung: Kimberly-Clark 0,550, 6,070, 0,134; Mellon Financial 1,123, 6,120, 0,388; New York Times 0,771, 6,590, 0,205; Procter & Gamble 0,469, 6,459, 0,090; Chicago Tribune 0,718, 7,215, 0,157; Texas Instruments 1,796, 11,474, 0,316.
- Im Zwei-Faktor-Modell mit Überraschungen des CPI-Wachstums und der Beschäftigung sind alle 13 Überschussrenditen negativ mit der unerwarteten Änderung des CPI-Wachstums verbunden. Die R² bleiben niedrig.
- Im BARRA-Branchenmodell sind die Betas Indikatoren der drei Sektoren Finanzen, Hochtechnologie und Übrige. IBM hat den Betavektor (0, 1, 0)′, Alcoa (0, 0, 1)′. Bei Fama und French werden die Betas nach beobachteten Faktorrealisationen mit einer Zeitreihenregression geschätzt.
- Für General Motors von Januar 1990 bis Dezember 2003 gegen die einfachen Überschussrenditen des S&P 500 beträgt das OLS-Beta 1,0457 bei Standardfehler 0,1453, t-Wert 7,1962 und p-Wert 0,0000.
- Das angepasste Modell ist rt = 0,20 + 1,0457 rM,t + et mit σ̂e = 8,13; der Residualstandardfehler ist 8,13 bei 166 Freiheitsgraden.
- R² beträgt 0,2378 und das adjustierte R² 0,2332.
- Der Achsenabschnitt beträgt 0,1982 bei Standardfehler 0,6302, t-Wert 0,3145 und p-Wert 0,7535.
- Dieselbe Schätzung als Zustandsraummodell in SsfPack liefert die Zustände 0,1982025 und 1,045702 mit Standardabweichungen 0,6302091 und 0,1453139 sowie σ̂e = 8,130114, in voller Übereinstimmung mit OLS.
- Im zeitvariablen CAPM betragen die Schätzungen von ση und σε 4,91 × 10 hoch −5 und 1,22 × 10 hoch −2, nahe null, sodass αt und βt der GM-Renditen im Wesentlichen konstant sind.
- Die drei Innovations-Standardabweichungen des zeitvariablen CAPM sind 4,907845 × 10 hoch −5, 1,219885 × 10 hoch −2 und 8,125213.
- Abbildung 11.5 zeigt für das geglättete βt eine enge Spanne etwa von 1,02 bis 1,06 und bestätigt damit das feste Marktmodell; die geglätteten erwarteten Renditen sind rt|T mit T = 168.
- Das gleich gewichtete Long/Short-Portfolio auf das Graham-und-Dodd-Kurs-Gewinn-Verhältnis mit zehnjährigem Gewinndurchschnitt hat 1980 bis 2005 ein Beta von 0,1 gegen den Markt und von 0,1 gegen den Value-Index, bei einem Alpha von jeweils 24,3 und t-Statistiken von 4,9 und 4,7.
- Dass das Beta nahe null liegt, wird aus der gleich langen und gleich großen Long/Short-Konstruktion erwartet.
- Das Long-only-Portfolio derselben Zehnjahres-Kennzahl hat ein Beta von 1,0 gegen den Markt und von 1,1 gegen den MSCI World Value Index, bei einem Alpha von 12,6 beziehungsweise 10,8 und t-Statistiken von 2,9 und 2,5.
- Im US-Top-Dezil 1993 bis 2005 betragen die Betas 0,6 für Earnings Yield plus Kapitalrendite, 0,3 für EBIT/EV, 0,4 für die Kapitalrendite, 0,7 für Trailing-Earnings-Yield plus Rendite auf die Aktiva, 0,8 für die Trailing-Earnings-Yield und 1,2 für die Rendite auf die Aktiva, beim Markt 1,0.
- In Europa ohne Großbritannien lauten die Top-Dezil-Betas 0,9, 0,8, 0,7, 0,8, 1,1 und 1,1 für Earnings Yield plus Kapitalrendite, EBIT/EV, Kapitalrendite, Trailing-Earnings-Yield plus Rendite auf die Aktiva, Trailing-Earnings-Yield und Rendite auf die Aktiva, beim Markt 1,0.
- In Großbritannien lauten dieselben Top-Dezil-Betas 0,8, 0,5, 0,6, 0,8, 0,8 und 1,2, beim Markt 1,0.
- In Japan lauten sie 0,6, 0,6, 0,3, 0,4, 0,6 und 0,7, beim Markt 1,0.
- Bei Bali, Demirtas und Hovakimian hat Beta das falsche Vorzeichen: das Portfolio der Value-Rückkäufe hat das niedrigste Beta und die höchste Rendite, das Portfolio der Growth-Emittenten das höchste Beta und die niedrigste Rendite.
- Im Länderkorb der Dividendenrendite 1975 bis 2003 beträgt das Long-only-Alpha 1,38 bei einer t-Statistik von 5,6 und das Beta 0,11 bei t 1,9; das Long-Short-Alpha beträgt 0,69 bei t 4,0 und das Beta minus 0,1 bei t minus 1,7.
- Im Länderkorb des Kurs-Buchwerts beträgt das Long-only-Alpha 1,35 bei t 5,5 und das Beta 0,10 bei t 1,7; das Long-Short-Alpha beträgt 0,64 bei t 3,4 und das Beta minus 0,1 bei t minus 1,9.
- Die Long-Short-Betas dieser Value-Länderstrategien liegen bei minus 0,1.
- Innerhalb von Sektoren gebaute Faktorportfolios erzeugten weniger attraktives Alpha als die marktweite Umsetzung, weil aus Liquiditätsgründen Tritiles statt Dezile oder Quintile nötig waren und der Faktorabstand schrumpfte.

## Unterschiedliche Quellenpositionen

- Nach den Anhängern effizienter Märkte fasst ein einziges Maß das Risiko einer Aktie zusammen, ihr Beta gegen den Markt.
- Die Betas bei Bali, Demirtas und Hovakimian laufen dieser Risikothese entgegen: die Growth-Emittenten haben das höchste Beta und die niedrigste Rendite, die Value-Rückkäufe das niedrigste Beta und die höchste Rendite.
- Die klassische Finanztheorie setzt Risiko mit relativer Preisvolatilität, also Beta, gleich. Montier hält das für empirisch zweifelhaft und für ungeeignet, weil es nicht trifft, wie Menschen Risiko sehen; Beta funktioniert in dieser Darstellung nicht.
- Kein Long-only-Fondsmanager, den Montier kennt, sorgt sich um Aufwärtsrisiko; es wird der Rendite zugeschlagen und gefeiert. Sorge gilt dem Abwärtsrisiko, dem dauerhaften Kapitalverlust im Sinne Ben Grahams.
- Graham misst echtes Anlagerisiko nicht am prozentualen Kursrückgang einer Aktie relativ zum Gesamtmarkt in einer Periode, sondern an der Gefahr, Qualität und Ertragskraft durch wirtschaftliche Änderungen oder eine Verschlechterung des Managements zu verlieren.
- Frank Martins Dreifaltigkeit aus Geschäftsrisiko, Finanzrisiko und Bewertungsrisiko ist für Montier ein besserer Leitfaden als die relative Preisvolatilität der klassischen Finanztheorie.
- Mankiw führt an, Vanguards S&P-500-Fonds habe über zehn Jahre 74 Prozent der vergleichbaren Fonds vor Steuern und 86 Prozent nach Steuern geschlagen, der steuermanagte Capital-Appreciation-Fonds 90 Prozent nach Steuern, und schließt, die Effizienzmarkthypothese sei nicht streng wahr, aber wahr genug, dass die meisten Anleger besser daran täten, sie zu glauben. Montier nennt das die Verwechslung von fehlender Evidenz mit der Evidenz des Fehlens nach Taleb (2005): Underperformance kann aus institutionellen Zwängen oder Verhaltensverzerrungen stammen und beweist keine effizienten Märkte.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 457–476 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-025-p457-p476|S. 457–476]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 495–514 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-027-p495-p514|S. 495–514]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 514–533 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-028-p514-p533|S. 514–533]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 590–609 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-032-p590-p609|S. 590–609]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 609–628 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-033-p609-p628|S. 609–628]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 628–647 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-034-p628-p647|S. 628–647]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 248–267 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-014-p248-p267|S. 248–267]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 267–286 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-015-p267-p286|S. 267–286]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 305–324 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-017-p305-p324|S. 305–324]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 343–362 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-019-p343-p362|S. 343–362]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 362–381 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-020-p362-p381|S. 362–381]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 381–400 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-021-p381-p400|S. 381–400]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 400–419 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-022-p400-p419|S. 400–419]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 419–438 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-023-p419-p438|S. 419–438]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 438–457 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-024-p438-p457|S. 438–457]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 457–476 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-025-p457-p476|S. 457–476]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 609–628 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-033-p609-p628|S. 609–628]]

## Verwandte Themen
