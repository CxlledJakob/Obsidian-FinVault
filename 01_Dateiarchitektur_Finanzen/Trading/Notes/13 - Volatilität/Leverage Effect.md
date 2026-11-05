---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/13 - Volatilität/13 - Volatilität|13 - Volatilität]]"
weitere_hauptthemen: []
unterthema: "Volatilitätsdynamik"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Leverage Effect


## Kurzdefinition

- Der Leverage-Effekt ist die asymmetrische Reaktion der bedingten Varianz: ein negativer vergangener Schock hebt die Volatilität stärker als ein positiver Schock derselben Größe.
- Der Leverage-Effekt wird hier darüber geprüft, ob negative und positive Schocks in einem Schwellen-Volatilitätsmodell die bedingte Varianz verschieden treffen.
- Im erweiterten DCC-Modell von Tsay (2006) ist der Hebelterm einer Komponente gleich dem vorherigen Schock, wenn dieser negativ ist, und sonst null.
- Der Parameter ρ ist die Korrelation zwischen εt und ηt und steht für den Leverage-Effekt der Rendite; typischerweise ist ρ negativ, das heißt eine negative Rendite erhöht tendenziell die Volatilität.

## Kernaussagen

- Volatilität reagiert auf einen starken Preisanstieg anders als auf einen starken Preisrückgang; das wird als Leverage-Effekt bezeichnet.
- Das ARCH-Modell unterstellt dieselbe Wirkung positiver und negativer Schocks auf die Volatilität, weil es nur vom Quadrat der vergangenen Schocks abhängt.
- In der Praxis reagiert der Preis eines Finanzwerts unterschiedlich auf positive und negative Schocks.
- Das EGARCH-Modell wurde entwickelt, um die Asymmetrie der Volatilität nach großen positiven und großen negativen Renditen zu erfassen.
- Nelson (1991) führt das exponentielle GARCH ein, damit positive und negative Anlagerenditen asymmetrisch auf die Volatilität wirken können.
- Die gewichtete Innovation ist g von epsilon t gleich theta mal epsilon t plus gamma mal (Absolutbetrag von epsilon t minus seinem Erwartungswert); beide Bestandteile haben den Mittelwert null, also auch g.
- Für nichtnegative epsilon t wirkt (theta plus gamma) mal epsilon t, für negative (theta minus gamma) mal epsilon t, jeweils abzüglich gamma mal dem Erwartungswert des Absolutbetrags.
- Bei standardnormalen Innovationen ist der Erwartungswert des Absolutbetrags die Wurzel aus 2 durch pi.
- EGARCH modelliert den Logarithmus der bedingten Varianz und lockert so die Forderung, dass die Koeffizienten positiv sein müssen.
- Im einfachen EGARCH(1,1) entwickelt sich die bedingte Varianz nichtlinear mit dem Vorzeichen von at minus 1; die Koeffizienten (gamma plus theta) und (gamma minus theta) zeigen die Asymmetrie. Das Modell ist nichtlinear, wenn theta ungleich null ist.
- Weil negative Schocks tendenziell stärker wirken, wird theta negativ erwartet.
- In der alternativen Form trägt ein positives at minus i den Beitrag alpha i mal (1 plus gamma i) mal dem Absolutbetrag der standardisierten Innovation zur Log-Volatilität bei, ein negatives den Beitrag alpha i mal (1 minus gamma i); gamma i bezeichnet dort den Leverage-Effekt und wird in Anwendungen negativ erwartet. Diese Form nutzt S-Plus.
- Nelson schätzt ein AR(1)-EGARCH an 6408 täglichen Überschussrenditen des wertgewichteten CRSP-Index von Juli 1962 bis Dezember 1987; theta wird auf minus 0,118 geschätzt, mit Standardfehler 0,009, gamma auf 0,156 mit Standardfehler 0,013.
- Dieselbe Schätzung hat alpha 0 gleich minus 10,06 (Standardfehler 0,346), w gleich 0,183 (0,028), alpha 1 gleich 1,929 (0,015), alpha 2 gleich minus 0,929 (0,015), beta gleich minus 0,978 (0,006), phi 0 gleich 0,00035 (0,000099), phi 1 gleich 0,205 (0,012), die Risikoprämie c gleich minus 3,361 (2,026) und den GED-Parameter v gleich 1,576 (0,032).
- Für 864 monatliche IBM-Logrenditen von Januar 1926 bis Dezember 1997 lautet das AR(1)-EGARCH(1,1) rt gleich 0,0105 plus 0,092 mal rt minus 1 plus at, ln der bedingten Varianz gleich minus 5,496 plus g von epsilon, t minus 1, durch (1 minus 0,856 B), und g gleich minus 0,0795 mal epsilon, t minus 1, plus 0,2647 mal (Absolutbetrag minus Wurzel aus 2 durch pi).
- Das GARCH-Modell reagiert weiterhin gleich auf positive und negative Schocks; EGARCH ist der genannte Ausweg.
- Im AR(1)–EGARCH(1,1) der monatlichen IBM-Logrenditen bis Dezember 1997 ist die Wirkung eines negativen standardisierten Schocks der Größe 2 etwa 37,4 Prozent höher als die eines positiven Schocks derselben Größe. Das Verhältnis der bedingten Varianzen ist e^{0,318} = 1,374. Je größer der Schock, desto größer der Unterschied.
- Das TGARCH- oder GJR-Modell trennt die Schocks an der Schwelle null. Ein positiver a_{t−i} trägt α_i a²_{t−i} zur bedingten Varianz bei, ein negativer (α_i + γ_i) a²_{t−i} mit γ_i > 0. Andere Schwellen sind möglich (Glosten, Jagannathan und Runkle, 1993; Zakoian, 1994).
- Im EGARCH(1,1) mit GED für die monatlichen IBM-Logrenditen bis 2003 ist der geschätzte Leverage-Koeffizient −0,264, negativ und auf dem 5-Prozent-Niveau signifikant, t-Ratio −2,094.
- Im TGARCH(1,1) für monatliche IBM-Logrenditen 1926 bis 2003 lautet die Varianzgleichung σ²_t = 3,45×10⁻⁴ + (0,0658 + 0,0843 N_{t−1}) a²_{t−1} + 0,8182 σ²_{t−1}. Der Leverage-Effekt ist auf dem 5-Prozent-Niveau signifikant.
- Bei einem Schock von zwei bedingten Standardabweichungen liegen die Varianzverhältnisse negativ zu positiv nahe beieinander: etwa 1,264 im EGARCH(1,1) und etwa 1,312 im TGARCH(1,1), Letzteres ohne den konstanten Term 0,000345.
- Aus der geschätzten IBM-Gleichung bis 1997 wird, mit √(2/π) ≈ 0,7979, ln(σ²_t) = −1,001 + 0,856 ln(σ²_{t−1}) + 0,1852 ε_{t−1}, wenn ε_{t−1} ≥ 0, und −0,3442 ε_{t−1}, wenn ε_{t−1} < 0.
- Schwellenmodelle können die asymmetrische Volatilitätsreaktion auf positive und negative Renditen abbilden. Dieselbe Idee dient der Untersuchung von Arbitrage zwischen Index-Futures und Kassapreisen.
- Im TGARCH für die täglichen IBM-Logrenditen von 1962 bis 2003 trägt ein positiver Schock den Koeffizienten 0,081 und ein negativer den Koeffizienten 0,157 vor a²_{t−1}, bei einem GARCH-Gewicht 0,863. N_{t−1} ist 1, wenn a_{t−1} < 0, und P_{t−1} = 1 − N_{t−1}.
- In diesem TGARCH sind alle Varianzparameter signifikant. Die Standardfehler der vier Varianzkoeffizienten sind 0,007, 0,008, 0,010 und 0,010.
- Das TGARCH (4.13) gibt negativen Schocks den Varianzkoeffizienten 0,157 und positiven den Koeffizienten 0,081. Es besteht die Prüfung der bedingten Heteroskedastizität nicht: Q(10) = 97,07 und Q(20) = 170,3, beide p = 0,00.
- Im AR(2)–TAR–GARCH(1,1) hängt auch der Koeffizient von σ²_{t−1} vom Vorzeichen von a_{t−1} ab. Der Zusatz lautet (0,030 a²_{t−1} + 0,062 σ²_{t−1}) N_{t−1}. Die Asymmetrie ist stärker, als ein GJR-Modell erlaubt.
- Bei negativem a_{t−1} lässt sich die Summe der Koeffizienten von a²_{t−1} und σ²_{t−1} auf eins beschränken.
- Alle Schätzungen dieses TAR-GARCH sind auf dem 1-Prozent-Niveau signifikant. Der unbedingte Mittelwert 0,033 liegt nahe am Stichprobenmittel 0,039.
- Ein ARCH(2) für die monatlichen 3M-Renditen von 1946 bis 2008 zeigt die asymmetrische Volatilitätsreaktion auf positive und negative frühere Schocks nicht.
- Das STAR-Modell stützt die Asymmetrie. Bei großem negativem a_{t−1} gilt näherungsweise σ²_t = 0,003 + 0,205 a²_{t−1} + 0,092 a²_{t−2}, bei großem positivem a_{t−1} gilt σ²_t = 0,004 − 0,034 a²_{t−1} + 0,092 a²_{t−2}.
- Der negative Koeffizient von a²_{t−1} im positiven Ast ist kontraintuitiv, aber klein. Bei einem großen positiven Schock wirken die ARCH-Effekte schwach, obwohl die Schätzungen statistisch signifikant bleiben.
- Der Skalenparameter 1000 der logistischen Übergangsfunktion wird a priori festgesetzt. Für großes negatives a_{t−1} geht der logistische Term gegen den negativen Ast, für großes positives a_{t−1} gegen den positiven Ast.
- Für die täglichen prozentualen Logrenditen von Johnson & Johnson von Januar 1998 bis Dezember 2008 soll ein GJR-Modell zeigen, ob der Leverage-Effekt auf dem 1-Prozent-Niveau signifikant ist, und mit einem allgemeinen Schwellen-Volatilitätsmodell verglichen werden.
- Für die monatlichen prozentualen GE-Logrenditen von Januar 1926 bis Dezember 2008 mit 996 Beobachtungen soll ein TGARCH mit GED-Innovationen und Schwellenvariable a_{t−1} bei Schwelle null zeigen, ob der Leverage-Effekt auf dem 5-Prozent-Niveau signifikant ist.
- Das AR(2)–TAR–GARCH(1,1) für die täglichen IBM-Logrenditen aktiviert den Zusatzterm a2 a²_{t−1} + b2 h_{t−1} nur, wenn der vorherige Schock negativ ist.
- Im geglätteten Schwellen-IGARCH für GE ändert der feste Koeffizient 10 im Term exp(−10 a_{t−1}) das Varianzgewicht, wenn der Schock von −5,06 auf +5,06 wechselt, bei σ²_996 = 50,5.
- Die Quadrattransformation in Gleichung (12.42) behält eine Korrelation zwischen ηt und εt nicht bei, sodass das genäherte Zustandsraummodell (12.43) und (12.44) den Leverage-Effekt nicht schätzen kann.
- Artigas und Tsay (2004) erhalten den Leverage-Effekt bei ρ ≠ 0 durch ηt = ρ ση εt + η*t, wobei η*t normalverteilt, unabhängig von εt und mit Varianz σ²η(1 − ρ²) ist.
- Die zugehörige Zustandsübergangsgleichung zt+1 = α zt + ρ ση εt + η*t wird nach Einsetzen von εt = (rt − x't β) exp(−zt/2) / σ0 nichtlinear: zt+1 = G(zt) + η*t mit G(zt) = α zt + ρ ση (rt − x't β) exp(−zt/2) / σ0.
- Wegen dieser nichtlinearen Übergangsgleichung gilt der Kalman-Filter aus (12.45) nicht mehr; die Näherung ist ein zeitvariabler linearer Kalman-Filter mit zt+1|t = G(zt|t) und der Varianzfortschreibung g(zt|t)² mal der geglätteten Zustandsvarianz plus σ²η(1 − ρ²), wobei g die erste Ableitung von G an zt|t ist.
- Im Vergleichsmodell ohne Leverage-Effekt sind {εt} und {ηt} zwei unabhängige gaußsche weiße Rauschreihen; mit Leverage-Effekt ist ihre Korrelation gleich ρ.

## Funktionsweise

- Die Varianzgleichung lautet: Quadrat der Volatilitätsdiagonalen gleich Λ0 plus Λ1 mal der vorherigen Volatilität zum Quadrat plus Λ2 mal den quadrierten Schocks plus Λ3 mal den quadrierten Hebeltermen. Alle Λi sind diagonal.
- Die Parameter erfüllen, dass die Summe der drei Steigungskoeffizienten je Komponente größer oder gleich null und kleiner als 1 ist, die Konstante positiv ist und alle Steigungen nichtnegativ sind. Die obere Schranke sichert, dass die Volatilitäten existieren. Ist die Hebelmatrix null, gibt es keinen Hebeleffekt.
- In der Parametrisierung rt = x′t β + σ0 exp(zt/2) εt und zt+1 = α zt + ηt ist ηt die Innovation von zt+1 und unabhängig von zt; diese Zeitverschiebung erlaubt den Leverage-Effekt.
- Würde man zt = α zt−1 + ηt setzen, könnten ηt und εt nicht korreliert sein, weil eine Korrelation ungleich null zt und εt in der Renditegleichung verbinden und Identifikationsprobleme erzeugen würde.
- Eine äquivalente Form setzt die Rendite auf exp(zt−1/2) und zt = α zt−1 + ηt; eine weitere schreibt z*t = α0 + α z*t−1 + ηt mit E(z*t) = α0/(1 − α) ungleich null.
- Es gilt zt = ln(ht) − ln(σ²0) und σ²0 = exp{E[ln(ht)]}, also eine mittelwertbereinigte Logvolatilität; die Volatilität σ0 exp(zt/2) bleibt positiv.
- Die Umparametrisierung der Kovarianz benutzt ω = σ²η(1 − ρ²) und ϕ, mit σ²η = ω + ϕ² und ρ = ϕ/ση.
- Die Quadrattransformation yt = ln[(rt − x′t β)² / σ²0] behält eine vorhandene Korrelation zwischen ηt und εt nicht, sodass das angenäherte Zustandsraummodell den Leverage-Effekt nicht schätzen kann.
- Artigas und Tsay (2004) setzen ηt = ρ ση εt + η*t mit η*t unabhängig von εt und Var(η*t) = σ²η(1 − ρ²) und erhalten die nichtlineare Übergangsgleichung zt+1 = G(zt) + η*t.
- G(zt) = α zt + ρ ση (rt − x′t β) exp(−zt/2) / σ0; angenähert wird mit einem zeitvariablen linearen Kalman-Filter, zt+1|t = G(zt|t) und Σt+1|t = g(zt|t)² Σt|t + σ²η(1 − ρ²).

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Bei den Tagesrenditen von Euro, Yen, IBM und Dell, Januar 1999 bis Dezember 2004, sind die Hebeleffekte nur für die beiden Aktien statistisch signifikant und haben die Form eines IGARCH-Modells. Die Hebelmatrix ist diagonal mit den Einträgen 0, 0, 0,0159 und 0,0114. Die Beträge sind klein, aber signifikant.
- Der Likelihood-Ratio-Test gegen das restringierte Modell ohne Hebel ergibt 15,16. Bei Chi-Quadrat mit 2 Freiheitsgraden ist der p-Wert 0,0005. Die maximierte Likelihood ist minus 9169,04 mit Hebel und minus 9176,62 ohne Hebel. Die Wechselkursreihen haben in der Hebelmatrix den Eintrag null.
- Beispiel 12.5 betrachtet die monatlichen S&P-500-Logrenditen von Januar 1962 bis November 2004, 515 Beobachtungen, eine Teilreihe von Beispiel 12.3.
- Modell 1 setzt {εt} und {ηt} als unabhängige gaußsche White-Noise-Folgen, also ohne Leverage; Modell 2 setzt corr(εt, ηt) = ρ als Leverage-Effekt.
- Beide Modelle haben die Form rt = µ + σo exp(zt/2) εt und zt+1 = α zt + ηt mit εt ∼ iid N(0, 1) und ηt ∼ iid N(0, σ²η).
- Die Schätzung mit FFBS und Gibbs-Sampling über 2000 plus 8000 Iterationen, die ersten 2000 als Burn-in, liefert mit Leverage die Posterior-Mittel μ = 0,0081, σo = 0,0764, α = −0,0616, ση = 2,5639 und ρ = −0,3892 bei Standardfehlern 0,0274, 0,0255, 0,1186, 0,3924 und 0,0292.
- Ohne Leverage lauten die Posterior-Mittel μ = 0,0080, σo = 0,0775, α = −0,0613 und ση = 2,5827 bei Standardfehlern 0,0279, 0,0266, 0,1164 und 0,3783.
- Der Text hebt ρ̂ = −0,39 hervor und nennt diesen Wert nahe an dem in der Literatur üblichen; die posterioren Mittel der geschätzten Volatilität mit und ohne Leverage-Effekt liegen sehr nah beieinander.
- Gegenüber der kürzeren Reihe in Beispiel 12.3 haben die geschätzten Volatilitäten ähnliche Muster und dieselbe Größenordnung.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 134–153 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-008-p134-p153|S. 134–153]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 153–172 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-009-p153-p172|S. 153–172]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 191–210 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-011-p191-p210|S. 191–210]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 210–229 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-012-p210-p229|S. 210–229]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 248–267 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-014-p248-p267|S. 248–267]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 552–571 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-030-p552-p571|S. 552–571]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 666–685 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-036-p666-p685|S. 666–685]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 685–704 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-037-p685-p704|S. 685–704]]

## Verwandte Themen
