---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Statistik"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Kovarianz


## Kurzdefinition

- Eine nicht singuläre Kovarianzmatrix der Größe N braucht mindestens halb so viele unabhängige und identisch verteilte Beobachtungen, wie das Produkt aus N und N plus 1.
- Die Kovarianzmatrix eines Zufallsvektors X ist Cov(X) = E[(X − µx)(X − µx)′], sofern die beteiligten Erwartungen existieren.
- Die Lag-ℓ-Autokovarianz einer Rendite ist γℓ = Cov(rt, rt−ℓ). Es gilt γ0 = Var(rt) und γ−ℓ = γℓ.
- Die Lag-l-Autokovarianz einer Renditereihe ist γl gleich Cov(rt, rt−l); für die lineare Reihe gilt γl gleich σa zum Quadrat mal der Summe von j gleich 0 bis unendlich von ψj mal ψ(j plus l).
- Eine k-dimensionale Reihe rt ist schwach stationär, wenn die ersten und zweiten Momente zeitlich unveränderlich sind; Mittelwertvektor und Kovarianzmatrix sind dann konstant.
- Der Mittelwert ist μ gleich E(rt), die gleichzeitige Kovarianzmatrix Γ0 gleich E[(rt minus μ)(rt minus μ)′]. Das i-te Diagonalelement ist die Varianz von rit, das Element (i, j) die Kovarianz zwischen rit und rjt.
- Im VAR(1) ist {at} eine Folge seriell unkorrelierter Zufallsvektoren mit Mittel 0 und Kovarianzmatrix Σ. Σ muss positiv definit sein, sonst lässt sich die Dimension von rt reduzieren. Oft wird at als multivariat normal angenommen.

## Kernaussagen

- Quadratische Programmierung verlangt die Inverse einer positiv definiten Kovarianzmatrix, also lauter positive Eigenwerte.
- Die Inversion ist fehleranfällig, wenn die Matrix numerisch schlecht konditioniert ist.
- Für eine invertierbare Matrix der Größe 50 braucht man mindestens fünf Jahre täglicher IID-Daten.
- Eine größere Matrix verschärft das Problem, weil jeder Kovarianzkoeffizient mit weniger Freiheitsgraden geschätzt wird.
- Hierarchical Risk Parity nutzt die Kovarianzmatrix, ohne Invertierbarkeit oder positive Definitheit zu verlangen, und rechnet auch auf einer singulären Matrix.
- Eine Matrix der Größe N entspricht einem vollständigen Graphen mit halb so vielen Kanten, wie das Produkt aus N und N minus 1.
- Eine Kovarianzmatrix von 50 mal 50 hat 50 Knoten und 1225 Kanten.
- Die Wurzel der Instabilität quadratischer Optimierer ist die verlangte Inversion der Kovarianzmatrix.
- Q(t) ist die Varianz des Prognosefehlers der beobachtbaren Variable, gebildet als x transponiert mal R mal x plus Ve, und ist von der Kovarianz der verborgenen Variable zu unterscheiden.
- R(t|t minus 1) ist die Kovarianz des Fehlers der verborgenen Variable, cov(β(t) minus β-Dach(t|t minus 1)), und eine 2-mal-2-Matrix, weil β aus Mittel des Spreads und Hedge Ratio besteht. R(t|t) ist die Kovarianz nach dem Update.
- Vω, die Kovarianz des Zustandsrauschens, wird als δ/(1 minus δ) mal der Einheitsmatrix gesetzt. Ve, die Varianz des Messrauschens, ist im Beispiel 0,001. Die Zustandskovarianz-Prognose addiert Vω.
- Im Modell mit einem einzelnen Mittelpreis ist R die Varianz des Fehlers dieses Mittels. Q(t) ist Var(m(t)) plus Ve, und das Varianz-Update lautet R(t|t) = (1 minus K(t)) mal R(t|t minus 1), mit K(t) = R(t|t minus 1) / (R(t|t minus 1) + Ve).
- Die Kelly-Formel für mehrere Portfolios setzt den Hebelvektor F gleich der Inversen der Kovarianzmatrix C der Portfoliorenditen mal dem Vektor M der mittleren Excess Returns.
- Bei risikofreiem Zins null ist die annualisierte zusammengesetzte Wachstumsrate bei diesen optimalen Hebeln g gleich F transponiert mal C mal F geteilt durch 2.
- Im Beispiel ist die Korrelation der beiden Strategierenditen null, und daraus folgen Kelly-Hebel von 4,4 und 4,9 bei annualisierten Überschussrenditen von 30 und 60 Prozent und Volatilitäten von 26 und 35 Prozent.
- In der Finanzliteratur wird für den Vektor der Logrenditen rt oft die multivariate Normalverteilung verwendet.
- Wie die bedingte Kovarianzmatrix von rt sich über die Zeit entwickelt, ist zusammen mit dem bedingten Erwartungswert der Hauptgegenstand der Kapitel 8 und 10.
- Unter schwacher Stationarität ist die Varianz von rt gleich der Varianz von rt−l, deshalb ist die Lag-l-Autokorrelation die Autokovarianz geteilt durch γ0.
- Für ein schwach stationäres AR(1) gilt γ0 gleich σa zum Quadrat geteilt durch (1 minus phi1 zum Quadrat) und γl gleich phi1 mal γ(l−1) für l größer als 0, sofern phi1 zum Quadrat kleiner als 1 ist.
- Die Momentengleichung eines stationären AR(2) lautet γl gleich phi1 mal γ(l−1) plus phi2 mal γ(l−2) für l größer als 0.
- Beim AR(1) ist die Kovarianz zwischen rt−1 und dem Schock at gleich null, weil rt−1 vor t liegt und at von keiner vergangenen Information abhängt; ebenso ist der Erwartungswert von (rt minus µ) mal a(t plus 1) gleich null.
- Für ein MA(1) mit Konstante null gilt die Lag-1-Autokovarianz γ1 gleich minus θ1 mal σa zum Quadrat, und γl gleich 0 für jedes l größer als 1; at und a(t−1) sind unkorreliert.
- Für ein ARMA(1,1) mit Konstante null gilt γ1 minus phi1 mal γ0 gleich minus θ1 mal σa zum Quadrat, anders als beim reinen AR(1), wo diese Differenz null ist.
- Für jedes l größer als 1 gilt beim ARMA(1,1) γl minus phi1 mal γ(l−1) gleich 0, identisch zum AR(1).
- Multipliziert man das ARMA(1,1) mit at und bildet den Erwartungswert, ist E(rt mal at) gleich σa zum Quadrat.
- In der Varianzherleitung des ARMA(1,1) sind rt−1 und at unkorreliert.
- Für das multiplikative saisonale Modell wt gleich (1 minus θ B) mal (1 minus Θ B hoch s) mal at, mit wt als regulär und saisonal differenzierter Reihe, ist der Erwartungswert null und die Varianz (1 plus θ zum Quadrat) mal (1 plus Θ zum Quadrat) mal σa zum Quadrat.
- Die Kovarianz von wt und wt−1 ist minus θ mal (1 plus Θ zum Quadrat) mal σa zum Quadrat, die von wt und wt−(s−1) sowie von wt und wt−(s+1) ist θ mal Θ mal σa zum Quadrat, und die von wt und wt−s ist minus Θ mal (1 plus θ zum Quadrat) mal σa zum Quadrat.
- Für alle anderen positiven Lags außer 0, 1, s minus 1, s und s plus 1 ist die Kovarianz null.
- Daraus folgen ρ1 gleich minus θ geteilt durch (1 plus θ zum Quadrat), ρs gleich minus Θ geteilt durch (1 plus Θ zum Quadrat) und die Autokorrelation an s minus 1 und s plus 1 gleich dem Produkt dieser beiden Werte.
- Der Kleinste-Quadrate-Schätzer der Kovarianz von beta Dach ist sigma e quadrat mal der Inversen von Summe xt xt Strich und wird inkonsistent, sobald die Fehler seriell korreliert oder bedingt heteroskedastisch sind.
- Der White-Schätzer ist die Sandwich-Form aus der Inversen von Summe xt xt Strich, der Mitte Summe e Dach t quadrat mal xt xt Strich und noch einmal derselben Inversen.
- Der Newey-West-Schätzer ergänzt diese Mitte um gewichtete Kreuzprodukte der Lags bis zu einer Trunkierung ell; die Bartlett-Gewichte sind wj gleich 1 minus j durch (ell plus 1).
- Newey und West schlagen für ell den ganzzahligen Teil von 4 mal (T durch 100) hoch 2/9 vor; der Schätzer ist eine nichtparametrische Schätzung der Kovarianzmatrix von Summe e Dach t mal xt.
- Bei der Regression der wöchentlichen Dreijahres- auf die Einjahresänderung bleibt der Koeffizient 0,7919, sein Standardfehler steigt von 0,0073 auf 0,0163 mit White und auf 0,0198 mit Newey-West, der t-Quotient fällt von 107,91 auf 48,44 und 39,92.
- Ist die Zahl der Regressoren größer als 1, lässt sich die White-Varianz eines einzelnen Koeffizienten über eine Hilfsregression dieses Regressors auf die übrigen gewinnen: Zähler ist die Summe aus residualem Fehlerquadrat mal quadriertem Hilfsresiduum, Nenner das Quadrat der Summe der quadrierten Hilfsresiduen.
- Die Hilfsregression erzeugt Orthogonalität zwischen ihrem Residuum und den übrigen Regressoren, damit sich die White-Formel vereinfacht.
- Die bedingte Varianz der Monats-Logrendite ist, sofern die Momente existieren, die Summe der bedingten Tagesvarianzen plus das Zweifache aller bedingten Kovarianzen zwischen den Tagen des Monats.
- Im CHARMA-Modell ist Ω die symmetrische, nichtnegativ definite Kovarianzmatrix der zufälligen Koeffizienten. Für das Element gilt ω_{ij} = ω_{ji}. Die bedingte Varianz enthält die Kreuzprodukte a_{t−i}a_{t−j}.
- Für die monatlichen S&P-500-Überschussrenditen lautet die geschätzte 2×2-Matrix, Standardfehler in Klammern, ω_{11} = 0,1417 (0,0333), ω_{12} = ω_{21} = −0,0594 (0,0365) und ω_{22} = 0,3081 (0,0340).
- Im CHARMA mit drei Lags, wobei δ_{3t} mit den ersten beiden Koeffizienten unkorreliert ist, sind die Diagonalelemente 0,1212 (0,0355), 0,1913 (0,0254) und 0,2988 (0,0420), das Kreuzglied der ersten beiden Lags ist −0,0622 (0,0283).
- Sind die Tagesrenditen weißes Rauschen, fallen die Kovarianzen in der Monatsvarianz weg. Folgen sie einem MA(1), bleibt der Term 2(n−1) Cov(r_{t,1}, r_{t,2}).
- Bei nichtsynchronem Handel mit Nicht-Handels-Wahrscheinlichkeit π gilt Var(r^o_t) = σ² + 2π μ² / (1−π), also eine größere Varianz als die der wahren iid-Rendite, sobald π > 0 und μ ungleich null ist.
- Die Autokovarianz der beobachteten Rendite ist Cov(r^o_t, r^o_{t−1}) = −π μ² und Cov(r^o_t, r^o_{t−j}) = −μ² π^j für j ≥ 1.
- Im Roll-Modell ohne Änderung des fundamentalen Preises ist Var(ΔP_t) = S²/2, Cov(ΔP_t, ΔP_{t−1}) = −S²/4 und Cov(ΔP_t, ΔP_{t−j}) = 0 für j > 1.
- Folgt der fundamentale Preis einem Random Walk mit Varianz σ², wird Var(ΔP_t) = σ² + S²/2, während die Autokovarianzen dieselben bleiben.
- Der Auftragsindikator erfüllt Var(I_t) = 1 und E(I_t) = 0.
- Die VaR-Formel für mehrere Positionen folgt aus der Annahme einer gemeinsamen multivariaten Normalverteilung der Logrenditen mit Mittelwert null und Kovarianzmatrix Σ t+1.
- Unter dieser Annahme ist die Logrendite des Portfolios normalverteilt mit Mittelwert null und endlicher Varianz.
- Die Lag-ℓ-Kreuzkovarianz ist Γℓ gleich E[(rt minus μ)(rt minus ℓ minus μ)′]; das Element (i, j) ist die Kovarianz zwischen rit und rj,t minus ℓ. Bei schwacher Stationarität hängt Γℓ von ℓ ab und nicht vom Zeitpunkt t.
- Es gilt Γij(ℓ) gleich Γji(minus ℓ) und damit Γℓ gleich der Transponierten von Γ mit Index minus ℓ.
- Cov(at, rt minus ℓ) ist für alle ℓ größer als 0 gleich 0, und Cov(rt, at) gleich Σ.
- Die Kovarianzmatrix eines stationären VAR(1) ist die unendliche Summe von Φ hoch i mal Σ mal (Φ hoch i)′, mit Φ hoch 0 gleich der Einheitsmatrix.
- Die Lag-ℓ-Kreuzkovarianz eines VAR(1) erfüllt Γℓ gleich Φ mal Γ mit Index ℓ minus 1 für ℓ größer als 0, und damit Γℓ gleich Φ hoch ℓ mal Γ0.
- Für ein VAR(p) lauten die Momentengleichungen, die multivariate Yule-Walker-Gleichung: Γℓ gleich Φ1 Γ mit Index ℓ minus 1 plus bis plus Φp Γ mit Index ℓ minus p, für ℓ größer als 0. Außerdem ist Cov(rt, at) gleich Σ und Cov(rt minus ℓ, at) gleich 0 für ℓ größer als 0.
- Für einen VMA(q) ist Cov(rt, at) gleich Σ. Die gleichzeitige Kovarianz ist Σ plus Θ1 Σ Θ1′ plus bis plus Θq Σ Θq′. Für ℓ größer als q ist Γℓ gleich 0. Für 1 ≤ ℓ ≤ q ist Γℓ die Summe von j gleich ℓ bis q von Θj Σ Θ′ mit Index j minus ℓ, wobei Θ0 gleich minus I gesetzt wird.
- Ein VMA(q) ist schwach stationär, sobald die Kovarianzmatrix Σ von at existiert.
- Die Cholesky-Zerlegung schreibt Σ gleich L G L′ mit G diagonal und Einsen auf der Diagonale von L. Für bt gleich L hoch minus 1 mal at ist Cov(bt) gleich G, die Komponenten sind also unkorreliert. Die orthogonalen Innovationen lassen sich zusätzlich auf Varianz 1 normieren.
- Ein k-dimensionaler Vektor folgt einer multivariaten Normalverteilung Nk(μ, Σ), wenn Σ positiv definit ist und die Dichte den Faktor |Σ| hoch −1/2 sowie die quadratische Form (x − μ)′ Σ hoch −1 (x − μ) enthält.
- Jede von null verschiedene Linearkombination c′x ist univariat normal mit Varianz c′Σc. Die Randverteilung eines Teilvektors xi ist normal mit Kovarianzblock Σii. Der Kreuzblock Σ12 ist genau dann null, wenn die beiden Teilvektoren unabhängig sind.
- Die bedingte Kovarianz von x1 gegeben x2 = b ist Σ11 − Σ12 Σ22 hoch −1 Σ21.
- Eine symmetrische positiv definite Matrix A besitzt eine Cholesky-Zerlegung A = L G L′ mit unterer Dreiecksmatrix L, Einsen auf der Diagonale, und positiver Diagonalmatrix G. Damit gilt L hoch −1 A (L hoch −1)′ = G.
- Für eine symmetrische k×k-Matrix stapelt vech die Elemente auf und unter der Hauptdiagonalen; die Dimension von vech(A) ist k(k + 1)/2.
- Im Faktormodell ist die Kovarianz der Renditen Cov(rt) = β Σf β′ + D, mit der Faktorkovarianz Σf und der diagonalen Matrix D der spezifischen Varianzen.
- Unter dem BARRA-Ansatz ist die Kovarianz der Überschussrenditen β Σ̂f β′ + D̂g. Σ̂f ist die Stichprobenkovarianz der verallgemeinert geschätzten Faktorrealisationen mit Teiler T−1.
- Für eine Kovarianzmatrix Σ ist das globale Minimum-Varianz-Portfolio das ω, das ω′Σω unter ω′1 = 1 minimiert. Die Lösung ist ω = Σ hoch −1 1, geteilt durch 1′ Σ hoch −1 1.
- Die Stichprobenkovarianz bei schwacher Stationarität ist die Summe von (rt − Mittel)(rt − Mittel)′ über t = 1 bis T, geteilt durch T−1. Die Stichprobenkorrelation entsteht durch Standardisierung mit der Diagonale der Stichprobenstandardabweichungen. Unter Regularitätsbedingungen sind beide Schätzer konsistent.
- Weil die Kovarianzmatrix nichtnegativ definit ist, besitzt sie eine Spektralzerlegung mit Eigenwerten λ1 ≥ … ≥ λk ≥ 0. Die Varianz der i-ten Hauptkomponente ist λi, und die Summe der Komponentenvarianzen gleich der Spur gleich der Summe der Eigenwerte.
- Im orthogonalen Faktormodell ist die Kovarianzmatrix der Renditen gleich ββ′ plus der diagonalen Matrix D der spezifischen Varianzen.
- Nicht jede Kovarianzmatrix besitzt eine orthogonale Faktordarstellung.
- Der Approximationsfehler der Hauptkomponenten-Faktorlösung, gemessen als Summe der quadrierten Elemente von geschätzter Kovarianz minus (β̂β̂′ plus D̂), ist höchstens die Summe der Quadrate der weggelassenen Eigenwerte.
- Die bedingte Kovarianzmatrix einer k-dimensionalen Renditereihe enthält k mal (k plus 1) durch 2 Größen. Bei fünf Assets sind das 15 bedingte Varianzen und Kovarianzen.
- Die asymptotische Hauptkomponentenanalyse untersucht die T-mal-T-Matrix (1 durch k) mal (R minus Einsvektor mal Mittelvektor′) mal deren Transponierte, statt die übliche Asset-Kovarianzmatrix zu invertieren.
- Die verfeinerte Schätzung bildet aus den OLS-Residuenvarianzen der einzelnen Assets eine Diagonalmatrix, skaliert die Renditen mit deren inverser Wurzel und wiederholt die Eigenanalyse der daraus gebildeten T-mal-T-Kovarianz.
- Am Prognoseursprung 888 ist die Ein-Schritt-Prognose der bedingten Kovarianz von IBM und S&P 500 im konstanten Modell die Matrix mit Diagonale 71,09 und 17,79 und Nebeneintrag 21,83. Im logistischen Modell lautet sie 75,15 und 24,70 auf der Diagonale und 23,48 daneben. Im Cholesky-Modell lautet sie 73,45 und 17,87 auf der Diagonale und 7,34 daneben. Die Varianzprognosen bleiben ähnlich, die Kovarianz des Cholesky-Modells ist deutlich kleiner.
- Engle modelliert nicht die Korrelation direkt, sondern die positiv definite Matrix Qt gleich (1 minus θ1 minus θ2) mal der unbedingten Kovarianz der standardisierten Innovationen plus θ1 mal ihrem vorherigen äußeren Produkt plus θ2 mal der vorherigen Qt, und normiert danach zur Korrelationsmatrix.
- Die Hauptkomponentenanalyse der Kovarianz der Innovationen von IBM und S&P 500 liefert die Eigenwerte 63,373 und 13,489. Der erste erklärt 82,2 Prozent der verallgemeinerten Varianz. Direkt auf den Renditen sind die Eigenwerte 63,625 und 13,513, und der erste erklärt etwa 82,5 Prozent. Der Effekt der bedingten Mittelgleichungen auf diese Zerlegung ist vernachlässigbar.
- Im dreidimensionalen Cholesky-Modell hängt die bedingte Varianz des S&P 500 nicht von den vergangenen Varianzen von Cisco oder Intel ab. Die bedingten Varianzen von Cisco und Intel hängen über die inverse Cholesky-Transformation von der vergangenen Marktvarianz ab.
- Die rollierende Kovarianzschätzung der vier Tagesrenditen von Euro, Yen, IBM und Dell verwendet ein Fenster von 69 Handelstagen.
- Im lokalen Trendmodell ist die bedingte Kovarianz von Zustand μt und Ein-Schritt-Fehler vt gegeben Ft minus 1 gleich der Zustandsprognosevarianz Σt|t minus 1.
- Bedingt auf Ft minus 1 ist das Paar (μt, vt) normal mit Kovarianzmatrix, deren erste Zeile und erste Spalte jeweils Σt|t minus 1 enthalten und deren rechtes unteres Element Vt ist.
- Für die erste Differenz wt gleich (1 minus B) yt ist Cov(wt, wt minus 1) gleich minus σ²e, und Cov(wt, wt minus j) ist 0 für jedes j größer 1.
- Der Kreuzterm im Gesamt-VaR zweier Positionen ist 2 ρ mal VaR1 mal VaR2. Für Cisco und Intel beträgt die verwendete Korrelation je nach Modell 0,473, 0,475 oder prognostiziert 0,345.
- Die PCA des Faktor-Volatilitätsmodells läuft auf der Kovarianzmatrix der Innovationen beziehungsweise der Renditen. Die Eigenwerte der Innovationen sind 63,373 und 13,489, die der Renditen 63,625 und 13,513.
- Der Kalman-Filter liefert eine Cholesky-Zerlegung der Kovarianzmatrix von y: K mal Cov(y) mal K′ ist die Diagonalmatrix der Varianzen V1 bis VT.
- Für den Zustandsfehler xt gilt Cov(xt, vt) gleich Σt|t minus 1, Cov(xt, vt plus 1) gleich Σt|t minus 1 mal Lt, und Cov(xt, vT) gleich Σt|t minus 1 mal dem Produkt der Lj von j gleich t bis T minus 1.
- Im allgemeinen Modell sind Qt und Ht positiv definite Kovarianzmatrizen der Zustandsinnovation und des Messfehlers. Die Kovarianz von ut ist blockdiagonal aus Rt Qt Rt′ und Ht.
- Im zeitvariablen CAPM ist die Kovarianz der Zustandsinnovation diagonal mit den Einträgen σ²η und σ²ε, und die Kovarianz des dreidimensionalen Störvektors (ηt, εt, et) ist diagonal mit σ²η, σ²ε und σ²e.
- Die Kovarianz des Ein-Schritt-Prognosefehlers ist Vt gleich Zt mal Σt|t minus 1 mal Zt′ plus Ht. Sie wird als invertierbar vorausgesetzt, weil Ht invertierbar ist.
- Die geglättete Zustandskovarianz ist Σt|T gleich Σt|t minus 1 minus Σt|t minus 1 mal Mt minus 1 mal Σt|t minus 1.
- Die Kovarianz des j-Schritt-Prognosefehlers ist Zt plus j mal Σt plus j gegeben t mal Zt plus j′ plus Ht plus j.
- Die geglättete Messfehlerkovarianz ist Ht minus Ht mal (Vt hoch minus 1 plus Kt′ Mt Kt) mal Ht, die der geglätteten Zustandsinnovation Qt minus Qt Rt′ Mt Rt Qt.
- Die Zyklusinnovationen des strukturellen Modells sind gemeinsam normal mit Kovarianz σ²ε mal (1 minus δ²) mal der 2-mal-2-Einheitsmatrix. Die Startwerte des Zyklus und seiner Hilfskomponente sind unkorreliert.
- Die Kovarianz des Ein-Schritt-Prognosefehlers ist Var[et(1)] = Zt+1 Σt+1|t Z′t+1 + Ht+1 und gleich Vt+1 des Kalman-Filters.
- Für den j-Schritt-Fehler gilt Var[et(j)] = Zt+j Σt+j|t Z′t+j + Ht+j.
- Die vorhergesagte Zustandskovarianz erfüllt Σt+j+1|t = Tt+j Σt+j|t T′t+j + Rt+j Qt+j R′t+j.
- st+j|t und Σt+j|t sind bedingter Mittelwert und bedingte Kovarianzmatrix von st+j gegeben Ft.
- Im Komponentenmodell ist die Kovarianzmatrix von (ηt, ωt)′ gleich diag{σ²η, σ²ω}.
- Result 12.1a setzt eine bekannte Kovarianzmatrix Σ der multivariaten Normalverteilung voraus; die Posterior-Kovarianz erfüllt Σ* hoch −1 = Σo hoch −1 + n Σ hoch −1, und x̄ hat die Kovarianz Σ/n.
- Der Kleinste-Quadrate-Schätzer β̂ der transformierten Regression ist multivariat normal mit Kovarianz σ² mal der Inversen von Summe xo,t xo,t′.
- Die bedingte Posterior-Kovarianz von β erfüllt Σ* hoch −1 = (Summe xo,t xo,t′)/σ² + Σo hoch −1.
- φ̂ ist normal mit Varianz σ² (Summe z²t−1) hoch −1; die Posteriorpräzision von φ addiert dazu 1/σ²o.
- Der Kleinste-Quadrate-Schätzer der AR-Koeffizienten φ̂ ist normal mit Kovarianz σ² mal der Inversen von Summe xt−1 xt−1′.
- Für einen fehlenden Wert im AR(p) ist die Varianz des Kleinste-Quadrate-Schätzers σ² / Summe von j = 0 bis p von φj², mit φ0 = 1.
- Die bedingte Posteriorvarianz dieses fehlenden Werts ist σ²* = σ² σ²o / (σ² + σ²o Summe φj²).
- Bei einem Ausreißer ist β̂h normal mit Varianz σ² / Summe ψ², und die Posteriorvarianz ist σ² ξ² / (σ² + ξ² Summe ψ²).
- Die bedingte Kovarianzmatrix von at faktorisiert nach Cholesky als das Produkt aus der unteren Dreiecksmatrix mit q21,t, der Diagonalmatrix aus g11,t und g22,t und der oberen Dreiecksmatrix mit q21,t.
- Damit sind die interessierenden Größen g11,t, g22,t und q21,t, mit gii,t = Var(bit | Ft−1).
- Die Kovarianz von (εt, ηt)′ ist die Matrix mit 1, ρ ση, ρ ση und σ²η; umparametrisiert mit ϕ und ω = σ²η(1 − ρ²) hat sie die Determinante ω.
- Die Inverse ist (1/ω) S plus die Matrix, die nur an der (1,1)-Stelle Eins ist; R = Summe btb′t ist die 2×2-Kreuzproduktmatrix der Innovationen.
- Die bedingte Posterior von q21,t ist normal; ihre Präzision ist a1t² / g22,t + (1 + γ1²) / σ²u, und der Mittelwert mischt µt mit a2t/a1t.
- Der erste Faktor dieser Posterior ist normal mit Mittel a2t/a1t und Varianz g22,t / a1t², der zweite normal mit Mittel µt und Varianz σ² = σ²u / (1 + γ1²).

## Funktionsweise

- Die Quasi-Diagonalisierung ordnet Zeilen und Spalten so, dass die größten Werte auf der Diagonale liegen, ohne einen Basiswechsel.
- Ähnliche Anlagen stehen danach beieinander und unähnliche weit auseinander.
- Die Varianz einer Teilmenge wird als quadratische Form einer Inverse-Varianz-Gewichtung definiert.
- Ist die Kovarianzmatrix diagonal, ist das Minimum-Varianz-Gewicht proportional zum Kehrwert der eigenen Varianz.
- Bei zwei Teilmengen ist der Anteil der ersten Hälfte eins minus der Bruch aus ihrer Varianz und der Summe beider Varianzen.
- Die Rauschterme des Kalman-Filters werden bei Mittelwert null durch eine sich entwickelnde Kovarianzmatrix beschrieben.
- R(t gegeben t−1) ist die Kovarianz des Fehlers der verborgenen Variable, nicht eine Varianz, weil β aus Achsenabschnitt und Steigung besteht, und R ist deshalb eine 2-mal-2-Matrix.
- Die Zustandsprognose erhöht diese Kovarianz um Vw, und das Update zieht Gain mal x mal R wieder ab.
- Vw wird als (δ geteilt durch 1 minus δ) mal der Einheitsmatrix angesetzt.
- In der Mehrportfolio-Kelly-Formel ist C die Kovarianzmatrix der Portfoliorenditen, und der Hebelvektor ist C hoch minus 1 mal dem Vektor der mittleren Excess Returns.
- Bei risikofreiem Zins null und optimalen Hebeln ist die annualisierte zusammengesetzte Wachstumsrate F transponiert mal C mal F, geteilt durch 2.
- Diese Wachstumsformel gilt nur bei den optimalen Hebeln.
- Die Stichprobenkovarianzmatrix ist 1/(T − 1) mal der Summe (xt − µ̂x)(xt − µ̂x)′. Stichprobenmittel und Stichprobenkovarianz sind konsistent für ihre theoretischen Gegenstücke, sofern die Kovarianzmatrix von X existiert.
- Der Stichprobenschätzer für ℓ ≥ 0 ist Γ-Dach mit Index ℓ gleich (1/T) mal der Summe von t gleich ℓ plus 1 bis T von (rt minus r-quer)(rt minus ℓ minus r-quer)′, wobei r-quer der Vektor der Stichprobenmittel ist.
- Weil Σ positiv definit ist, gibt es eine Cholesky-Zerlegung Σ gleich L G L′ mit L unterer Dreiecksmatrix und Einsen auf der Diagonale sowie G diagonal. Für bt gleich L hoch minus 1 mal at sind die Komponenten unkorreliert und Cov(bt) gleich G.
- Die Kovarianzmatrix des 1-Schritt-Prognosefehlers eines VAR(p) ist Σ. Die des 2-Schritt-Fehlers ah plus 2 plus Φ1 mal ah plus 1 ist Σ plus Φ1 Σ Φ1′. Bei schwacher Stationarität konvergiert die Kovarianz des ℓ-Schritt-Fehlers gegen die Kovarianzmatrix von rt.
- Der Maximum-Likelihood-Schätzer von Σ im VAR(i) ist (1/T) mal der Summe der äußeren Produkte der Residuen. Der OLS-Residualschätzer teilt dieselbe Summe durch T minus 2i minus 1. Die Punktschätzer von φ0 und Φj stimmen bei AR-Modellen überein, die Schätzer von Σ nicht.
- Ist eine Startschätzung von Σ vorhanden, werden die Gleichungen für a0 in der exakten VMA-Likelihood mit Σ hoch minus 1/2 vormultipliziert. Das Ergebnis ist eine multiple lineare Regression, aus der a0 per Kleinste Quadrate geschätzt wird.
- Die EWMA-Kovarianz ist das gewichtete Mittel der äußeren Produkte vergangener Innovationen. Die Gewichte sind (1 minus lambda) mal lambda hoch (j minus 1), geteilt durch (1 minus lambda hoch t minus 1), und summieren sich zu eins. Für großes t gilt die Rekursion: neue Kovarianz gleich (1 minus lambda) mal jüngstem äußeren Produkt plus lambda mal vorheriger Kovarianz.
- Im bivariaten DVEC(1,1) hängt jede bedingte Varianz und die bedingte Kovarianz nur vom eigenen Vergangenheitswert und vom passenden Produkt der vorherigen Schocks ab. Eine positiv definite Matrix ist nicht gesichert.
- BEKK sichert die positive Definitheit fast sicher, wenn das Produkt der unteren Dreiecksmatrix A mit ihrer Transponierten positiv definit ist. Die Parameterzahl ist k zum Quadrat mal (m plus s) plus k mal (k plus 1) durch 2.
- In der bivariaten Cholesky-Zerlegung ist σ11,t gleich g11,t, σ21,t gleich q21,t mal g11,t und σ22,t gleich g22,t plus q21,t zum Quadrat mal g11,t. Allgemein ist die bedingte Varianz der i-ten Komponente die Summe von qiv,t zum Quadrat mal gvv,t über v gleich 1 bis i, und die Kovarianz der Komponenten i und j, j kleiner als i, ist die Summe von qiv,t mal qjv,t mal gvv,t über v gleich 1 bis j. Die Diagonaleinträge qvv,t sind eins.
- Die Kovarianz der Cholesky-transformierten Schocks bt ist die Diagonalmatrix Gt. Die Determinante der bedingten Kovarianz ist das Produkt der positiven Diagonaleinträge gii,t.
- Im schwach stationären Constant-Correlation-Modell, alle Eigenwerte von alpha1 plus beta1 positiv und kleiner als 1, sind die unbedingten Varianzen (I minus alpha1 minus beta1) hoch minus 1 mal phi0, und die unbedingte Kovarianz ist die konstante Korrelation mal dem Produkt der unbedingten Standardabweichungen.
- Die ℓ-Schritt-Prognose der Kovarianz zweier Schocks im Constant-Correlation-Modell ist die geschätzte Korrelation mal der Wurzel aus dem Produkt der beiden prognostizierten bedingten Varianzen.

## Voraussetzungen

- Schwache Stationarität verlangt, dass Cov(rt, rt−ℓ) = γℓ nur von ℓ abhängt, und setzt damit endliche erste und zweite Momente voraus.
- Sofern nicht ausdrücklich etwas anderes gesagt wird, werden die Renditereihen finanzieller Assets als schwach stationär angenommen.

## Anwendung im Trading

- Prognostizierte Renditen, Ledoit-Wolf-Shrinkage und Black-Litterman-Sichten lassen sich in den hierarchischen Ansatz einbauen.
- Dieselbe Idee, Matrixinversionen zu vermeiden, kann instabile Verfahren wie VAR oder VECM ersetzen.
- Weitere Einsätze bei fast singulärer Kovarianzmatrix sind die Kapitalallokation auf Manager, algorithmische Strategien, Bagging, Boosting und Random-Forest-Prognosen.

## Regeln und Kriterien


## Risiken und Grenzen

- Mit so vielen Kanten dürfen Gewichte völlig frei umschichten, und kleine Schätzfehler führen zu völlig anderen Lösungen.
- Nebenbedingungen, Black-Litterman-Priors oder eine stabilere Inverse nach Ledoit und Wolf bleiben in Geometrie, linearer Algebra und Analysis und beheben die fehlende Hierarchie nicht.
- Die Annahme einer diagonalen Kovarianzmatrix bringt dem Inverse-Varianz-Portfolio etwas Stabilität, seine Varianz liegt aber weiter über der von Hierarchical Risk Parity.
- Simulierte Renditen verfehlen serielle Korrelationen, die in historischen Strategierenditen stecken können, in die Zukunft fortbestehen und den maximalen Drawdown in der realen Welt senken können.
- Historische Strategierenditen erfassen diese Korrelationen vollständig.

## Beispiele

- Die Konditionszahl der Kovarianzmatrix im Zahlenbeispiel beträgt 150,9324.
- Außer Stichprobe betragen die Portfoliovarianzen 0,1157 für CLA, 0,0928 für das Inverse-Varianz-Portfolio und 0,0671 für Hierarchical Risk Parity.
- Im Beispiel ist die Korrelation der beiden Strategien null, und die Renditen sind gaußisch.
- Im Beispiel 8.3 ist Σ gleich [[2, 1], [1, 1]]. Die Cholesky-Matrix L hoch minus 1 ist [[1, 0], [minus 0,5, 1]], und die Kovarianz der transformierten Schocks ist diag(2; 0,5). Nach Umsortierung der Komponenten wird L hoch minus 1 zu [[1, 0], [minus 1, 1]] und G zur Einheitsmatrix.
- Die Innovations-Kovarianz des VAR(5) für IBM und S&P 500 hat die Diagonale 48 und 30 und die Nebendiagonale 24, im vollen wie im vereinfachten Modell.
- Die Stichproben-Standardabweichungen der fünf Anleiherenditen, als Maß der zweiten Momente, sind 10 hoch minus 2 mal (2,53; 2,43; 1,97; 1,39; 0,53) für 30, 20, 10, 5 und 1 Jahr.
- Die bedingte Likelihood des vereinfachten VAR(5) liefert die Fehler-Kovarianzmatrix mit 48,328570, 24,361464 und 30,027406.
- Im VARMA(2,1) der Zinssätze ist die Schock-Kovarianz, angegeben als Σ mal 10 hoch 3, gleich [[3,58, 2,50], [2,50, 2,19]].
- Im Simulationsbeispiel (8.31) ist die Kovarianzmatrix der Schocks die Einheitsmatrix und positiv definit.
- Für das Marktmodell und die Stichprobenkovarianz der 13 Überschussrenditen unterscheiden sich die globalen Minimum-Varianz-Gewichte von Chicago Tribune deutlich: 0,1400 im Modell gegen 0,0168 in den Daten. Beide Portfolios geben Kimberly-Clark, New York Times und Procter & Gamble die größeren Gewichte. Die Modellgewichte lauten außerdem Alcoa 0,0117, A.G. Edwards −0,0306, Caterpillar 0,0792, Ford 0,0225, FedEx 0,0802, General Motors 0,0533, Hewlett-Packard −0,0354, Kimberly-Clark 0,2503, Mellon 0,0703, New York Times 0,1539, Procter & Gamble 0,2434 und Texas Instruments −0,0388.
- Die Datengewichte des globalen Minimum-Varianz-Portfolios lauten Alcoa −0,0073, A.G. Edwards −0,0085, Caterpillar 0,0866, Ford −0,0232, FedEx 0,0943, General Motors 0,0916, Hewlett-Packard 0,0345, Kimberly-Clark 0,2296, Mellon 0,0495, New York Times 0,1790, Procter & Gamble 0,2651, Chicago Tribune 0,0168 und Texas Instruments −0,0080.
- Die Hauptkomponentenanalyse der Stichprobenkovarianz der fünf Monats-Logrenditen von IBM, Hewlett-Packard, Intel, J.P. Morgan Chase und Bank of America hat die Eigenwerte 284,17, 112,93, 57,43, 46,81 und 29,87, die Anteile 0,535, 0,213, 0,108, 0,088 und 0,056 sowie die kumulierten Anteile 0,535, 0,748, 0,856, 0,944 und 1.
- Für Hang Seng und Nikkei 225 beträgt der EWMA-Parameter lambda etwa 0,9305.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 248–267 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-014-p248-p267|S. 248–267]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 76–95 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-006-p076-p095|S. 76–95]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 180–199 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-014-p180-p199|S. 180–199]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 39–58 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-003-p039-p058|S. 39–58]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 58–77 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-004-p058-p077|S. 58–77]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 77–96 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-005-p077-p096|S. 77–96]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 96–115 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-006-p096-p115|S. 96–115]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 115–134 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-007-p115-p134|S. 115–134]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 248–267 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-014-p248-p267|S. 248–267]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 343–362 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-019-p343-p362|S. 343–362]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 400–419 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-022-p400-p419|S. 400–419]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 419–438 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-023-p419-p438|S. 419–438]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 438–457 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-024-p438-p457|S. 438–457]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 476–495 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-026-p476-p495|S. 476–495]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 495–514 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-027-p495-p514|S. 495–514]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 514–533 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-028-p514-p533|S. 514–533]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 533–552 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-029-p533-p552|S. 533–552]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 552–571 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-030-p552-p571|S. 552–571]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 571–590 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-031-p571-p590|S. 571–590]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 590–609 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-032-p590-p609|S. 590–609]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 609–628 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-033-p609-p628|S. 609–628]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 628–647 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-034-p628-p647|S. 628–647]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 647–666 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-035-p647-p666|S. 647–666]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 666–685 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-036-p666-p685|S. 666–685]]

## Verwandte Themen
