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

# Bayesianische Inferenz


## Kurzdefinition

- Der probabilistisch korrekte Weg, die Klasse eines Ereignisses oder Objekts zu schätzen, ist das Bayes-Theorem, abgeleitet aus den Axiomen der Wahrscheinlichkeitstheorie.
- Eine Überzeugung auf probabilistisch korrekte Weise zu aktualisieren heißt, dass neue Information eine Vorüberzeugung gemäß dem Satz von Bayes verändert.
- Die Vorüberzeugung wird dabei entsprechend dem prognostischen Wert der neuen Information geändert.
- Bayesianische Inferenz verbindet eine Vorverteilung P(θ) mit den Daten zur Posteriorverteilung f(θ|X), auf der die statistische Inferenz beruht.

## Kernaussagen

- Jeder konkurrierende nichtlineare Modelltyp kann als Zustand einer Markov-Kette dargestellt werden. Diese Modellwahl verallgemeinert das in der bayesianischen Analyse übliche Odds-Ratio (Chen, McCulloch und Tsay, 1997).
- Die Schätzungen des Markov-Switching-Modells für die Wachstumsrate des realen US-GNP sind Posterior-Mittel und Posterior-Standardabweichungen eines Gibbs-Samplers mit 5000 Iterationen (McCulloch und Tsay, 1994).
- Die berichteten Schätzungen und Standardabweichungen des PCD-Modells für die IBM-Geschäfte vom 21. November 1990 sind Posterior-Mittel und Posterior-Standardabweichungen aus MCMC-Ziehungen mit 9500 Iterationen.
- McCulloch und Tsay (2000) erweitern das PCD-Modell zu einem hierarchischen Rahmen für alle 63 Handelstage vom 1. November 1990 bis 31. Januar 1991 mit mehr als 19.000 Beobachtungen; viele Parameterschätzungen werden in dieser Stichprobe signifikant.
- In der erweiterten Stichprobe liegt der Koeffizient von ln(Δti−1) im Modell für die Zeitdauer insgesamt zwischen 0,04 und 0,1, klein, aber signifikant.
- Es gibt zwei Ansätze: die klassische Schätzung durch Maximieren der Likelihood und die bayesianische Verbindung von Vorwissen und Daten.
- Nach der Definition der bedingten Wahrscheinlichkeit ist f(θ|X) = f(X|θ)P(θ) / f(X), wobei f(X) das Integral von f(X|θ)P(θ) über θ ist.
- Allgemein gilt f(θ|X) proportional zu f(X|θ)P(θ); Inferenz allein aus der Likelihood entspricht damit einem Bayes-Ansatz mit konstanter Priorverteilung.
- Eine konjugierte Priorverteilung gehört derselben Familie an wie die Posteriorverteilung und liefert für MCMC eine geschlossene bedingte Posterior.
- Die bedingten Verteilungen im Gibbs-Sampler heißen bedingte Posteriorverteilungen, weil sie die Parameter gegeben Daten, übrige Parameterwerte und das Modell beschreiben.
- Bayes-Lösungen existieren für alle zuvor behandelten Probleme; MCMC macht sie praktikabler, und in den meisten Fällen ähneln sie der klassischen Lösung.
- Result 12.1: Bei normaler Stichprobe mit unbekanntem Mittel µ und bekannter Varianz σ² und normalem Prior von µ mit Mittel µo und Varianz σ²o ist die Posterior normal mit µ* = (σ² µo + n σ²o x̄) / (σ² + n σ²o) und σ²* = σ² σ²o / (σ² + n σ²o).
- Mit der Präzision η = 1/σ² gilt η* = ηo + nη und µ* = (ηo/η*) µo + (nη/η*) x̄: die Posteriorpräzision ist die Summe der Präzisionen von Prior und Daten, der Posteriormittelwert ein präzisionsgewichtetes Mittel aus Prior- und Stichprobenmittel.
- Der Beitrag der Priorverteilung nimmt mit wachsendem Stichprobenumfang n ab; die Information über µ steckt im suffizienten Stichprobenmittel x̄ mit Präzision nη.
- Result 12.1a: Bei multivariater Normalstichprobe mit bekanntem Σ und normalem Prior (µo, Σo) ist die Posterior multivariat normal mit Σ* hoch −1 = Σo hoch −1 + n Σ hoch −1 und µ* = Σ*(Σo hoch −1 µo + n Σ hoch −1 x̄); n Σ hoch −1 ist die Präzisionsmatrix von x̄.
- Result 12.2: Normale Stichprobe mit gegebenem Mittel und unbekannter Präzision η, Gamma-Prior mit positiven α und β, ergibt eine Gamma-Posterior mit Parametern α + n/2 und β + Summe (xi − µ)²/2.
- Result 12.3: Bernoulli-Stichprobe mit Parameter θ und Beta-Prior (α, β) ergibt eine Beta-Posterior mit Parametern α + Summe xi und β + n − Summe xi.
- Result 12.4: Poisson-Stichprobe mit Parameter λ und Gamma-Prior (α, β) ergibt eine Gamma-Posterior mit Parametern α + Summe xi und β + n.
- Eine multivariate Fassung von Result 12.1 ist für MCMC bei linearen Regressionsmodellen besonders nützlich (Box und Tiao, 1973).
- Result 12.6: Stichprobe aus der negativen Binomialverteilung mit festem m und Beta-Prior (α, β) für λ ergibt eine Beta-Posterior mit Parametern α + m n und β + Summe xi.
- Result 12.7 zerlegt die zweidimensionale Prior als P(µ, η) = P(µ|η)P(η): bedingt auf η = ηo ist µ normal mit Mittel µo und Präzision τo ηo, und η ist marginal gamma mit α und β.
- Die bedingte Posterior von µ gegeben η = ηo ist normal mit µ* = (τo µo + n x̄)/(τo + n) und Präzision η* = (τo + n) ηo.
- Die marginale Posterior von η ist gamma mit α + n/2 und β* = β + (1/2) Summe (xi − x̄)² + τo n (x̄ − µo)² / (2(τo + n)).
- Result 12.8: Bei normaler Stichprobe mit Mittel null und unbekannter Varianz σ² und invertierter Chi-Quadrat-Prior mit v Freiheitsgraden, also (vλ)/σ² ∼ χ²v, ist die Posterior ebenfalls invertiert chi-quadrat mit v + n Freiheitsgraden, (vλ + Summe a²i)/σ² ∼ χ² von v+n.
- Bekannte Größen der Prior wie βo, Σo, λ, v, φo und σ²o heißen Hyperparameter; typisch setzt man βo = 0, φo = 0 und Σo diagonal mit großen Diagonalelementen, und die Priors der Teilparameter sind unabhängig.
- Für die Regression mit AR(1)-Fehlern lauten die konjugierten Priors β ∼ N(βo, Σo), φ ∼ N(φo, σ²o) und (vλ)/σ² ∼ χ²v.
- Die bedingte Posterior von β gegeben φ und σ² ist multivariat normal mit Σ* hoch −1 = (Summe xo,t xo,t′) / σ² + Σo hoch −1 und β* = Σ* mal [(Summe xo,t xo,t′ / σ²) β̂ + Σo hoch −1 βo], wobei yo,t = yt − φ yt−1 und xo,t = xt − φ xt−1.
- Die bedingte Posterior von φ ist normal; ihre Präzision ist (Summe z²t−1)/σ² + 1/σ²o, und der Mittelwert gewichtet die Kleinste-Quadrate-Schätzung φ̂ mit der Prior.
- Die bedingte Posterior von σ² ist invertiert chi-quadrat: (vλ + Summe a²t)/σ² ∼ χ² mit v + (n − 1) Freiheitsgraden, at = zt − φ zt−1.
- Im Zinsbeispiel sind die Priors β ∼ N(0, 4), φ ∼ N[0, diag(0,25, 0,16)] und (10 × 0,05)/σ² ∼ χ² mit 10 Freiheitsgraden.
- Für die Ausreißererkennung sind die Priors φ ∼ N(φo, Σo), (vλ)/σ² ∼ χ²v, ϵ ∼ Beta(γ1, γ2) und βt ∼ N(0, ξ²).
- Im AR(3)-Beispiel sind φ ∼ N(0, 0,25 I3), (5 × 0,00256)/σ² ∼ χ² mit 5 Freiheitsgraden, γ1 = 5, γ2 = 95 und ξ² = 0,1; 0,00256 liegt bei σ̂²/5 und ξ² bei 9 σ̂², die erwartete Ausreißerquote ist 5 Prozent.
- Für das stochastische Volatilitätsmodell wird die Prior als p(β, ω) = p(β)p(ω) zerlegt, also unabhängig für Mittel- und Volatilitätsgleichung.
- Beim Markov-Switching-Modell haben MCMC-Verfahren gegenüber der traditionellen Likelihood viele Vorteile, weil die Likelihood eine Mischung über alle Zustandskonfigurationen ist; Gibbs-Sampling braucht nur die bedingten Posterior-Verteilungen.
- Als konjugierte Priors werden βi ~ N(βio, σ²io) und ei ~ Beta(γi1, γi2) verwendet; der Prior von αij ist gleichverteilt über ein festgelegtes Intervall, und weil αij nichtlinear in der Likelihood ist, wird er mit Griddy Gibbs gezogen.
- Die bedingte Posterior-Verteilung von βi hängt nur von den Daten im Zustand i ab und ist normal: mit rit = rt/√ht bei st = i und sonst 0, ni Beobachtungen und Mittel r̄i gilt 1/σ²i* = ni + 1/σ²io und β*i = σ²i* (ni r̄i + βio/σ²io).
- Die Posterior-Verteilung von ei ist Beta(γi1 + ℓi, γi2 + ni − ℓi); ℓ1 zählt die Wechsel von Zustand 1 nach 2, ℓ2 die umgekehrten Wechsel, und ni ist die Zahl der Beobachtungen in Zustand i.
- Prognosen unter MCMC entstehen, indem das angepasste Modell in jeder Gibbs-Iteration Realisationen für den Prognosezeitraum erzeugt; Punktprognosen sind die Stichprobenmittel, und die Stichproben-Standardabweichungen dienen als Varianzen der Prognosefehler.
- MCMC berücksichtigt in der Prognose die Parameterunsicherheit, während das GARCH-Modell die Parameter als fest gegeben behandelt, und liefert eine prädiktive Verteilung der Volatilität, die informativer ist als eine Punktprognose und die Quantile für Value at Risk liefern kann.
- Die Recheneffizienz der Volatilitätsprognose lässt sich mit Importance Sampling erhöhen, siehe Gelman, Carlin, Stern und Rubin (2003).

## Funktionsweise

- Es setzt drei Größen ein: den Basisanteil der gesuchten Klasse, den Basisanteil der Personen oder Fälle mit dem beobachteten Merkmalsmuster und die bedingte Wahrscheinlichkeit dieses Musters, gegeben die Zugehörigkeit zur Klasse.
- Daraus folgt die bedingte Wahrscheinlichkeit, dass der Fall zur Klasse gehört, gegeben das beobachtete Merkmalsmuster.
- Die Indikatoren It ∈ {1, …, 7} haben die Priorwahrscheinlichkeiten pi aus Tabelle 12.3; die Posterior ist pit = pi qit / Summe pj qjt, mit qit = Φ[(yt − zt − µi)/ϖi].
- Ist die Ziehung It = j, setzt man ct = µj und Ht = ϖ²j und zieht die Logvolatilität gemeinsam aus dem angenäherten linearen Gauß-Zustandsraummodell.
- Die bedingte Posterior-Dichte von αij ist keine bekannte Verteilung; für st = i ist sie proportional zu −1/2 [ln ht + (rt − βi√ht)²/ht], wobei ht den Parameter αij enthält, und wird auf einem Gitter ausgewertet, zum Beispiel 0 ≤ α11 < 1 − α12.
- Die Zustände sj werden einzeln gezogen: P(sj = 1) ist die mit der Likelihood gewichtete Übergangswahrscheinlichkeit P(sj = 1 | sj−1, sj+1) L(sj = 1), geteilt durch die Summe derselben Größen für beide Zustände, und die Ziehung nutzt eine Gleichverteilung auf [0, 1].
- Dabei ist L(sj = i) proportional zu exp(fji), und fji ist die Summe von t = j bis n von −1/2 [ln ht + a²t/ht], mit at = rt − β1√ht in Zustand 1 und at = rt − β2√ht sonst.
- Sind e1 und e2 klein, sind aufeinanderfolgende Zustände stark korreliert, und es ist effizienter, mehrere sj gemeinsam zu ziehen; der Aufwand, alle Zustandskonfigurationen aufzuzählen, wächst mit dieser Zahl schnell.
- Die Anfangsvolatilität h1 wird gleich der Stichprobenvarianz von rt gesetzt; sie als weiteren Parameter zu schätzen ist möglich, der Effekt des Festlegens wird aber in den meisten Anwendungen, besonders bei großer Stichprobe, als vernachlässigbar erwartet.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Weil Intuition nach Ähnlichkeit zum Stereotyp urteilt und nicht nach dem Bayes-Gesetz, unterläuft der Basisratenfehlschluss, also das Übergehen der Basisraten der Lage.
- Terroristen sind sehr selten und haben damit eine sehr niedrige Basisrate; unter allen Personen mit denselben auffälligen Merkmalen wie die Attentäter des 11. September 2001 ist der Anteil tatsächlicher Terroristen extrem klein, vielleicht nur eine Person von einer Million.
- Diese Basisrate ist für die Wahrscheinlichkeit entscheidend und wird vernachlässigt, weil die intuitive Beurteilung an den aufmerksamkeitsstarken Merkmalen hängt.

## Beispiele

- Für das univariate SV-Modell der monatlichen S&P-500-Logrenditen sind die Priors µ ∼ N(0, 4), α ∼ N[(0, 0,6)′, diag(0,25, 0,04)] und (10 × 0,1)/σ²v ∼ χ² mit 10 Freiheitsgraden.
- Die Priors sind relativ nichtinformativ; die Posterioren in Abbildung 12.5, gestrichelt die Prior und durchgezogen die Posterior aus 2000 Gibbs-Iterationen, sind besonders für µ und σ²v konzentriert.
- Die Posteriormittel und Standardfehler sind µ 0,409 (0,157), α0 0,454 (0,068), α1 0,837 (0,025) und σ²v 0,086 (0,007).
- Andere Startwerte, Priors und Iterationszahlen lassen die Ergebnisse stabil; Effizienz und Ergebnis des Griddy Gibbs hängen von der Spanne für ht ab.
- Im bivariaten Modell sind die Priors βi0 ∼ N(0, 4), αi ∼ N[(0, 0,7)′, diag(0,25, 0,04)], γ0 ∼ N(0, 1), (10 × 0,1)/σ²iv ∼ χ²10 und (5 × 0,2)/σ²u ∼ χ²5, ebenfalls relativ nichtinformativ.
- Für die Kovarianz von (εt, ηt) wird ω = σ²η(1 − ρ²) als inverse Gamma mit Hyperparametern (γ0/2, γ1/2) und ϕ|ω ∼ N(0, ω/2) angesetzt; die gemeinsame Posterior zerfällt in eine Normalverteilung für ϕ und eine inverse Gamma für ω.
- Es gilt ϕ ∼ N(ϕ̃, ω / (2 + e′e)) mit ϕ̃ = e′η / (2 + e′e), und ω ∼ IG von (n + 1 + γ0)/2 und (1/2)[γ1 + η′η − (e′η)² / (2 + e′e)].
- Daraus folgen σ²η = ω + ϕ² und ρ = ϕ/ση; die Dichte einer IG(α, β) ist β^α / Γ(α) mal ω hoch −(α+1) mal exp(−β/ω) für ω > 0, mit α > 2 und β > 0.
- Für die monatlichen S&P-500-Logrenditen von Januar 1962 bis November 2004, 515 Beobachtungen, läuft Gibbs-Sampling mit FFBS über 2000 plus 8000 Iterationen, davon die ersten 2000 als Burn-in; mit Leverage ist das Posterior-Mittel von ρ gleich −0,3892 bei Standardfehler 0,0292, etwa −0,39 und nahe dem in der Literatur üblichen Wert.
- Dieselbe Schätzung mit Leverage liefert die Posterior-Mittel μ = 0,0081, σo = 0,0764, α = −0,0616 und ση = 2,5639 mit Standardfehlern 0,0274, 0,0255, 0,1186 und 0,3924; ohne Leverage μ = 0,0080, σo = 0,0775, α = −0,0613 und ση = 2,5827 mit Standardfehlern 0,0279, 0,0266, 0,1164 und 0,3783.
- Für General Electric von Januar 1926 bis Dezember 1999 sind die Priors β1 ~ N(0,3, 0,09), β2 ~ N(1,3, 0,09) und ei ~ Beta(5, 95); Griddy Gibbs nutzt 400 gleichabständige Punkte auf αi0 in [0, 6,0], αi1 in [0, 1] und αi2 in [0, 0,5] mit der Nebenbedingung αi1 + αi2 < 1.
- Der GE-Sampler läuft 5000 plus 2000 Iterationen, und nur die letzten 2000 gehen in die Inferenz ein; die Startwerte sind ei = 0,1, s1 als Bernoulli-Ziehung mit gleichen Wahrscheinlichkeiten sowie α1 = (1,0, 0,6, 0,2)' und α2 = (2, 0,7, 0,1)'.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 77–96 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-005-p077-p096|S. 77–96]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 210–229 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-012-p210-p229|S. 210–229]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 286–305 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-016-p286-p305|S. 286–305]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 628–647 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-034-p628-p647|S. 628–647]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 647–666 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-035-p647-p666|S. 647–666]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 666–685 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-036-p666-p685|S. 666–685]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 685–704 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-037-p685-p704|S. 685–704]]

## Verwandte Themen
