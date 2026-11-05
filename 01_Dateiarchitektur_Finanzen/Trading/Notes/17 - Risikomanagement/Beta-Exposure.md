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

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- Zeitvariable Korrelationen lassen sich verwenden, um das zeitvariable Beta des Marktmodells für eine Renditereihe zu schätzen.

## Regeln und Kriterien


## Risiken und Grenzen


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

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 457–476 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-025-p457-p476|S. 457–476]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 495–514 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-027-p495-p514|S. 495–514]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 514–533 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-028-p514-p533|S. 514–533]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 590–609 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-032-p590-p609|S. 590–609]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 609–628 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-033-p609-p628|S. 609–628]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 628–647 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-034-p628-p647|S. 628–647]]

## Verwandte Themen
