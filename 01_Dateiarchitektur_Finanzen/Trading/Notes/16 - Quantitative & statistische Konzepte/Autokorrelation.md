---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Zeitreihen"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Autokorrelation


## Kurzdefinition

- Serielle Korrelationen oder Autokorrelationen sind die Korrelationen der interessierenden Variable mit ihren eigenen Vergangenheitswerten und das grundlegende Werkzeug zur Untersuchung einer stationären Zeitreihe.
- Der Lag-ℓ-Autokorrelationskoeffizient einer schwach stationären Rendite rt ist ρℓ = Cov(rt, rt−ℓ) / Var(rt) = γℓ / γ0. Es gilt ρ0 = 1, ρℓ = ρ−ℓ und −1 ≤ ρℓ ≤ 1.
- Eine schwach stationäre Reihe ist genau dann nicht seriell korreliert, wenn ρℓ = 0 für alle ℓ > 0.
- Die Lag-l-Autokorrelation ρl einer schwach stationären Renditereihe rt ist die Korrelation zwischen rt und rt minus l und hängt nur von l ab: ρl gleich Cov(rt, rt−l) geteilt durch Var(rt), also γl durch γ0.
- Aus der Definition folgen ρ0 gleich 1, ρl gleich ρ minus l und minus 1 kleiner oder gleich ρl kleiner oder gleich 1.
- Bei der Autokorrelation wird der jüngste Datenstrom eines Tickers mit demselben Datenstrom korreliert, der um einen Parameter namens Lag verzögert ist.

## Kernaussagen

- Toth et al. (2011) finden bei Aktien der London Stock Exchange, dass Orderzeichen über viele Tage positiv autokorreliert sind.
- Als Erklärungen prüfen sie Herding und Order Splitting.
- Auf Zeitskalen von weniger als einigen Stunden führen sie die Persistenz des Orderflows überwiegend auf Order Splitting zurück.
- Im Roll-Modell ist die serielle Kovarianz der beobachteten Preisänderungen negativ und gleich −c², wobei c die halbe Geld-Brief-Spanne ist.
- Empirisch zeigen Finanzzeitreihen serielle Abhängigkeit.
- Querschnittliche Mean Reversion setzt auf die serielle Antikorrelation relativer Renditen: auf Unterperformance einer Aktie soll Überperformance folgen und umgekehrt.
- Random Walks haben kein Gedächtnis, und frühere Ergebnisse haben keine Wirkung auf die nachfolgenden Ereignisse.
- Zeitreihenmomentum heißt, dass vergangene Renditen positiv mit künftigen Renditen korreliert sind; gerechnet werden der Korrelationskoeffizient und sein p-Wert als Wahrscheinlichkeit der Nullhypothese keiner Korrelation.
- Der Koeffizient verlangt einen festen Lag; die stärkste positive Korrelation kann zwischen verschiedenen Lags liegen, etwa eine negative Korrelation der 1-Tages-Renditen neben einer sehr positiven Korrelation der vergangenen 20-Tages-Rendite mit der künftigen 40-Tages-Rendite.
- Für TU sind die besten Kompromisse aus Koeffizient und p-Wert die Paare aus Lookback und Haltedauer (60, 10), (60, 25), (250, 10), (250, 25), (250, 60) und (250, 120).
- Das Paar 250 und 25 hat für TU einen Korrelationskoeffizienten von 0,27 bei einem p-Wert von 0,02; in Tabelle 6.1 steht für 250 und 25 der Wert 0,2719 bei einem p-Wert von 0,0238.
- In Tabelle 6.1 erreicht Lookback 250 und Haltedauer 120 einen Koeffizienten von 0,5112 bei einem p-Wert von 0,0617, Lookback 250 und Haltedauer 250 einen Koeffizienten von 0,4873 bei einem p-Wert von 0,3269.
- Der Test der Vorzeichen vergangener und künftiger Renditen liefert für TU keine sehr anderen Ergebnisse; die besten Paare sind dann (60, 10), (250, 10) und (250, 25).
- Der Text verlangt nicht überlappende Paare: ist der Lookback größer als die Haltedauer, wird um die Haltedauer vorgerückt, ist die Haltedauer größer, um den Lookback.
- Der abgedruckte Code setzt die Schrittweite dagegen auf den Lookback, wenn der Lookback mindestens so groß wie die Haltedauer ist, und sonst auf die Haltedauer.
- Eine Verschiebung um einen Tag erzeugt leicht andere Renditepaare; wegen der großen Überlappung dürften die Korrelationen nicht stark abweichen, und getestet wurde nur eine von vielen möglichen Mengen.
- Serielle Korrelation der Futures-Gesamtrendite auf langer Skala entsteht, wenn das Vorzeichen der Rollrendite lange konstant bleibt und die durchschnittliche Rollrendite die durchschnittliche Gesamtrendite dominiert; die Spot-Rendite wechselt Vorzeichen und Größe sehr schnell.
- Das passt zu BR, HG und TU, deren Rollrenditen laut Tabelle 5.1 betragsmäßig größer sind als ihre Spot-Renditen.
- Für C trägt die Erklärung nicht, obwohl C die betragsmäßig größte Rollrendite im Vergleich zur durchschnittlichen Spot-Rendite hat.
- Der Korrelationskoeffizient der Tagesrenditen von VX und ES erreicht minus 75 Prozent.
- Für TU beträgt der Hurst-Exponent 0,44, und der Variance-Ratio-Test verwirft den Random Walk nicht; das widerspricht den Lag-Korrelationen nicht, weil Momentum und Mean Reversion auf verschiedenen Zeitrahmen liegen und der Variance-Ratio-Test einzelne Zeitrahmen nicht prüft.
- Beispiel 1.1 simuliert eine Renditereihe mit derselben Kurtosis wie die TU-Futures, aber ohne serielle Autokorrelationen, und erzeugt in 12 Prozent der Zufallsziehungen dieselben Renditen wie die TU-Momentum-Strategie.
- Unter einigen allgemeinen Bedingungen ist die Lag-1-Stichprobenautokorrelation ein konsistenter Schätzer von ρ1.
- Bei einem MA(1) ist nur die Lag-1-Autokorrelation ungleich null, und zwar minus θ1 geteilt durch (1 plus θ1 zum Quadrat); für alle Lags größer als 1 ist die Autokorrelation null, die ACF bricht also bei Lag 1 ab.
- Bei einem MA(2) ist ρ1 gleich (minus θ1 plus θ1 mal θ2) geteilt durch (1 plus θ1 zum Quadrat plus θ2 zum Quadrat), ρ2 gleich minus θ2 geteilt durch denselben Nenner, und ρl gleich 0 für l größer als 2.
- Bei einem MA(q) ist die Lag-q-Autokorrelation ungleich null, aber ρl gleich 0 für jedes l größer als q; die Reihe ist nur linear mit ihren ersten q Verzögerungen verbunden und heißt deshalb Finite-Memory-Modell.
- Die ACF identifiziert die MA-Ordnung: ist ρq ungleich 0 und ρl gleich 0 für alle l größer als q, folgt rt einem MA(q).
- Für MA-Modelle bestimmt die ACF die Ordnung, weil sie nach Lag q abbricht; für AR-Modelle bestimmt die partielle Autokorrelation die Ordnung, weil sie nach Lag p abbricht.
- Die Autokorrelation eines stationären ARMA(1,1) fällt wie die eines AR(1) exponentiell, der Abfall beginnt aber erst bei Lag 2, und sie bricht bei keinem endlichen Lag ab; ρ1 gleich phi1 minus θ1 mal σa zum Quadrat geteilt durch γ0, und ρl gleich phi1 mal ρ(l−1) für l größer als 1.
- Die partielle Autokorrelation eines ARMA(1,1) bricht ebenfalls bei keinem endlichen Lag ab und ähnelt der eines MA(1), wobei der exponentielle Abfall bei Lag 2 statt bei Lag 1 beginnt.
- ACF und partielle Autokorrelation legen die Ordnung eines ARMA-Modells nicht verlässlich fest; Tsay und Tiao (1984) verwenden dafür die erweiterte Autokorrelationsfunktion EACF.
- Die theoretische EACF eines ARMA(p, q) enthält ein Dreieck aus Nullen, dessen obere linke Ecke an der Stelle (p, q) liegt.
- Das starke Gedächtnis einer Unit-Root-Reihe zeigt sich in der Stichprobenautokorrelation: mit wachsendem Stichprobenumfang gehen alle Stichprobenautokorrelationen gegen 1.
- Bei einer schwach stationären Moving-Average-Darstellung fallen die ψ-Gewichte exponentiell, und die Wirkung eines vergangenen Schocks auf die laufende Rendite lässt nach; bei der Einheitswurzel bleiben die Gewichte bei 1 und die Autokorrelation klingt nicht ab.
- Bei einer saisonalen Reihe ist die Stichprobenautokorrelation der ersten Differenz stark, wenn der Lag ein Vielfaches der Periode ist.
- Für das multiplikative saisonale Modell der differenzierten Reihe gilt ρ1 gleich minus θ geteilt durch (1 plus θ zum Quadrat), ρs gleich minus Θ geteilt durch (1 plus Θ zum Quadrat), und ρ an s minus 1 sowie an s plus 1 gleich dem Produkt dieser beiden Autokorrelationen; alle anderen positiven Lags sind null.
- Bei Quartalsdaten, Periode 4, ist die Autokorrelation der airline-differenzierten Reihe nur an den Lags 1, 3, 4 und 5 von null verschieden.
- Bei einer stationären Zeitreihe fällt die Autokorrelationsfunktion mit wachsendem Lag exponentiell gegen null.
- Bei einer einheitswurzel-nichtstationären Reihe konvergiert die Stichproben-Autokorrelation für jeden festen Lag mit wachsender Stichprobe gegen 1 (Chan und Wei 1988; Tiao und Tsay 1983).
- Langzeitgedächtnis liegt vor, wenn die Autokorrelation polynomial langsam gegen null fällt; beim fraktional differenzierten Prozess (1 minus B) hoch d mal xt gleich at mit minus 0,5 kleiner d kleiner 0,5 gilt rho k ungefähr k hoch (2d minus 1).
- Für diesen Prozess ist rho 1 gleich d geteilt durch (1 minus d), und die partielle Autokorrelation phi k,k ist gleich d geteilt durch (k minus d).
- Die Absolutbeträge der täglichen einfachen Renditen der wert- und gleichgewichteten CRSP-Indizes vom 2. Januar 1970 bis 31. Dezember 2008 haben betragsmäßig kleine, aber sehr langsam abfallende Stichproben-Autokorrelationen, die auch nach 300 Lags auf dem 5-Prozent-Niveau signifikant bleiben (Ding, Granger und Engle 1993).
- Nach einer Januar-Dummy verschwinden bei den monatlichen einfachen Renditen von Decile 1 die seriellen Korrelationen der Residuen auf den Lags 12, 24 und 36 weitgehend.
- Die Residuen der Niveauregression der wöchentlichen Dreijahres- auf die Einjahresrendite haben eine hoch signifikante, langsam abfallende Stichproben-Autokorrelation.
- Die Durbin-Watson-Statistik prüft nur die Autokorrelation zum Lag 1 und ist näherungsweise 2 mal (1 minus rho Dach 1).
- Die monatlichen Logrenditen von Intel von Januar 1973 bis Dezember 2008 zeigen in der Stichproben-Autokorrelation keine signifikante serielle Korrelation außer einer kleinen bei Lag 7.
- Dieselbe Reihe hat Q(12) gleich 18,26 mit p-Wert 0,11, in der Ausgabe 18,2635 mit p-Wert 0,1079 bei 12 Freiheitsgraden und 432 Beobachtungen.
- Die Autokorrelation der absoluten und der quadrierten Logrenditen zeigt, dass die Reihe seriell abhängig ist: die Logrenditen sind seriell unkorreliert, aber nicht unabhängig.
- Die zehnminütigen prozentualen Änderungen des Kurses Deutsche Mark je US-Dollar vom 5. bis 19. Juni 1989 haben keine serielle Korrelation; die partielle Autokorrelation der Quadrate hat deutliche Spitzen.
- Tagesrenditen eines Marktindex haben oft kleine serielle Korrelationen, Monatsrenditen desselben Index oft keine signifikante.
- Im ARCH-Modell ist der Schock seriell unkorreliert, aber abhängig; die Abhängigkeit wird durch eine quadratische Funktion seiner verzögerten Werte beschrieben.
- Bei den meisten Anlagerenditen sind die seriellen Korrelationen schwach, falls sie überhaupt vorhanden sind.
- Die monatlichen Überschussrenditen des S&P 500 von 1926 bis 1991, 792 Beobachtungen, haben serielle Korrelationen auf den Lags 1 und 3.
- Ein MA(3) lautet rt gleich 0,0062 plus at plus 0,0944 mal at minus 1 minus 0,1407 mal at minus 3, mit residualer Standardabweichung 0,0576; alle Koeffizienten sind auf dem 5-Prozent-Niveau signifikant.
- Das unter Normalität angepasste AR(3) lautet rt gleich 0,088 mal rt minus 1 minus 0,023 mal rt minus 2 minus 0,123 mal rt minus 3 plus 0,0066 plus at, mit residualer Varianz 0,00333.
- Nach dem GARCH(1,1) ohne AR-Glieder zeigen die standardisierten Residuen Q(12) gleich 11,99 mit p-Wert 0,45 und Q(24) gleich 28,52 mit p-Wert 0,24, die Quadrate Q(12) gleich 13,11 mit p-Wert 0,36 und Q(24) gleich 26,45 mit p-Wert 0,33.
- Ein GARCH-M erzeugt serielle Korrelationen der Renditen, weil die bedingte Varianz selbst seriell abhängig ist; eine Risikoprämie ist damit ein weiterer Grund für serielle Korrelationen historischer Aktienrenditen.
- Der Vergleich von Volatilitätsprognosen mit dem späteren quadrierten Schock findet oft eine niedrige Korrelation und ein niedriges Bestimmtheitsmaß; ein einzelnes Quadrat ist aber kein genaues Maß der Volatilität.
- Eine Zeitreihe hat langes Gedächtnis, wenn ihre Autokorrelationsfunktion mit wachsendem Lag hyperbolisch statt exponentiell fällt.
- Die Autokorrelationsfunktion der quadrierten oder absoluten Renditen eines Assets fällt oft langsam, obwohl die Renditereihe selbst keine serielle Korrelation hat (Ding, Granger und Engle, 1993).
- Die Stichproben-ACF der täglichen absoluten Logrenditen von IBM und des S&P 500 vom 3. Juli 1962 bis 31. Dezember 2003 ist positiv, von mäßiger Größe und fällt langsam; zwei waagerechte Linien markieren die asymptotischen 5-Prozent-Grenzen.
- Im Long-Memory-SV-Modell mit (1−B)^d u_t = η_t und 0 < d < 0,5 fällt die ACF von u_t hyperbolisch statt exponentiell.
- Für das stochastische Volatilitätsmodell mit m = 1 gilt corr(a²_t, a²_{t−i}) = [exp(σ²_h α₁^i) − 1] / [3 exp(σ²_h) − 1].
- Bollerslev und Jubinski (1999) sowie Ray und Tsay (2000) finden für den Logarithmus quadrierter Tagesrenditen von Unternehmen im S&P 500 einen Median des fraktionalen Parameters d von etwa 0,38.
- Unternehmen derselben Industrie oder desselben Geschäftssektors, etwa große US-Banken und Finanzinstitute, haben tendenziell mehr gemeinsame Long-Memory-Komponenten in den täglichen Aktienvolatilitäten (Ray und Tsay, 2000).
- Nelson (1991) setzt in der Mittelgleichung ein AR(1) ein, um mögliche serielle Korrelation der täglichen Überschussrenditen zu erfassen.
- Im AR(1)–EGARCH(1,1) der monatlichen IBM-Logrenditen von Januar 1926 bis Dezember 1997, 864 Beobachtungen, liefern die standardisierten Residuen Q(10) = 6,31 (p = 0,71) und Q(20) = 21,4 (p = 0,32), die quadrierten Residuen Q(10) = 4,13 (p = 0,90) und Q(20) = 15,93 (p = 0,66); serielle Korrelation und bedingte Heteroskedastizität bleiben aus.
- Die Stichprobenautokorrelation der US-Arbeitslosenquote fällt langsam, deshalb wird die erste Differenz analysiert.
- Die partielle Stichprobenautokorrelation der monatlichen einfachen Renditen des gleichgewichteten CRSP-Index, Januar 1926 bis Dezember 2008, 996 Beobachtungen, ist an den Lags 1 und 3 signifikant, deshalb wird ein AR(3) angesetzt.
- Die quadrierten AR(3)-Residuen dieser CRSP-Reihe deuten darauf, dass die bedingte Heteroskedastizität von den Residual-Lags 1, 3 und 8 abhängen kann. Lag 8 wird der Einfachheit halber weggelassen.
- Die standardisierten Residuen des bilinearen CRSP-Modells zeigen keine signifikante serielle Korrelation, die quadrierte Residuenreihe aber schon. Die Reihe ist daher nicht unabhängig.
- Beim Vergleichsmodell AR(3)–ARCH(3) haben die quadrierten Residuen Q(10) = 19,78 mit p = 0,031.
- Die standardisierten Residuen des TAR der Arbeitslosenänderung zeigen nur eine geringe serielle Korrelation bei Lag 12.
- Für die schwach stationäre Volatilitätsreihe der Wold-Zerlegung sind die Schocks unkorreliert, aber abhängig.
- Unter der Nullhypothese der Linearität sollen die Residuen eines korrekt spezifizierten linearen Modells unabhängig sein; jede Verletzung der Unabhängigkeit zeigt Modellunzulänglichkeit an, einschließlich der Linearitätsannahme.
- Die Lag-i-Autokorrelation der quadrierten Residuen, ρ̂_i(a²_t), geht in die Ljung-Box-Statistik Q(m) = T(T+2) Σ ρ̂²_i(a²_t)/(T−i) ein; bei angemessenem ARMA(p, q) ist Q(m) asymptotisch chi-quadrat mit m−p−q Freiheitsgraden.
- Diese Statistik der quadrierten Residuen ist zum Erkennen bedingter Heteroskedastizität nützlich und asymptotisch äquivalent zum Lagrange-Multiplikator-Test von Engle (1982) für ARCH.
- Das Bispektrum ist die Fourier-Transformierte der Momente dritter Ordnung; für eine lineare Reihe ist das normierte Bispektrum b(w1, w2) über alle Frequenzen konstant, und unter Normalität ist diese Konstante null, weil E(a³_t) = 0.
- Der BDS-Test prüft die iid-Annahme über das Korrelationsintegral: bei iid gilt C_k(δ) = [C_1(δ)]^k, und √T {C_k(δ, T) − [C_1(δ, T)]^k} ist asymptotisch normal mit Mittel null.
- Die BDS-Statistik D_k(δ, T) hat eine standardnormale Grenzverteilung; vor ihrer Anwendung ist vorhandene lineare Abhängigkeit aus den Daten zu entfernen.
- Der BDS-Test kann empfindlich auf die Wahl von δ und k reagieren, besonders wenn k groß ist.
- In den Anwendungen bestätigen die Ljung-Box-Statistiken Q(5) und Q(10), dass in den Residuen vor den Nichtlinearitätstests keine serielle Korrelation mehr steht: 3,2 und 6,5 bei N(0,1), 0,9 und 1,7 bei t_6, 2,9 und 4,9 beim equal-weighted Index, 1,0 und 9,8 beim value-weighted Index und 0,6 und 7,1 bei IBM.
- Nichtsynchrone Handelszeiten können selbst dann, wenn die wahren Renditen seriell unabhängig sind, eine Lag-1-Kreuzkorrelation zwischen Aktien, eine Lag-1-Autokorrelation der Portfoliorendite und in manchen Fällen negative Autokorrelationen einer einzelnen Aktie erzeugen.
- Im vereinfachten Modell von Lo und MacKinlay (1990) sind die stetigen Renditen r_t iid mit Mittel μ und Varianz σ²; die Wahrscheinlichkeit, dass das Papier in einer Periode nicht gehandelt wird, ist π, zeitlich konstant und unabhängig von r_t.
- Die beobachtete Rendite r^o_t ist 0 mit Wahrscheinlichkeit π und sonst die seit dem letzten Handel aufgelaufene Summe der r_t; ihr Erwartungswert bleibt μ.
- Die Lag-1-Autokovarianz der beobachteten Rendite ist Cov(r^o_t, r^o_{t−1}) = −π μ², und allgemein Cov(r^o_t, r^o_{t−j}) = −μ² π^j für j ≥ 1.
- Die induzierte Lag-1-Autokorrelation ist ρ1(r^o_t) = −(1−π) π μ² / [(1−π) σ² + 2π μ²]; ist μ ungleich null, entstehen negative Autokorrelationen, und ihr Betrag kann je nach μ, π und σ erheblich sein.
- Im Roll-Modell ohne Änderung des fundamentalen Werts ist die Autokorrelation der beobachteten Preisänderungen ρ1 = −0,5 und ρ_j = 0 für jedes j > 1.
- Folgt der fundamentale Wert einem Random Walk mit Innovationen-Varianz σ², bleibt die Autokorrelation ρ1(ΔP_t) = (−S²/4) / (S²/2 + σ²) ≤ 0, solange der Spread S = P_a − P_b positiv ist; der Betrag ist kleiner als 0,5.
- Der Bid-Ask-Spread erzeugt keine serielle Korrelation jenseits von Lag 1.
- Sind die Auftragsindikatoren zweier Papiere kontemporär positiv korreliert, können die Spreads negative Lag-1-Kreuzkorrelationen erzeugen.
- Die Zahl der IBM-Transaktionen in 5-Minuten-Intervallen vom 1. November 1990 bis 31. Januar 1991 hat eine zyklische Autokorrelationsfunktion mit Periode 78, der Zahl der 5-Minuten-Intervalle eines Handelstags.
- Die Autokorrelationsfunktion der Richtungsreihe D_i der IBM-Intraday-Preisbewegungen hat nur bei Lag 1 eine Spitze, mit dem Wert −0,389; bei 59.837 Beobachtungen ist das hoch signifikant und bestätigt die Preisumkehr aufeinanderfolgender Trades.
- Im Ordered Probit für IBM 1988 sind die Koeffizienten der verzögerten Preisänderungen negativ und hoch signifikant: −1,01, −0,53 und −0,21 mit t-Werten −135,6, −85,0 und −47,2, was Preisumkehr anzeigt.
- Im ADS-Modell hängt die Wahrscheinlichkeit einer Preisänderung von der vorherigen Preisänderung ab: 0,258 nach einer unveränderten Notierung und 0,476 nach einer Preisänderung.
- Die Wahrscheinlichkeit, dass auf einen Anstieg bei erneuter Änderung wieder ein Anstieg folgt, ist nur 0,085; die Wahrscheinlichkeit eines Anstiegs nach einem Rückgang ist 0,904.
- Simulierte ACD(1,1)-Reihen mit 500 Beobachtungen zeigen in der Stichproben-Autokorrelation deutliche serielle Abhängigkeit der Dauern.
- Ist ein ACD-Modell adäquat spezifiziert, verhalten sich die standardisierten Residuen êi = xi/ψ̂i wie unabhängige, identisch verteilte Zufallsvariablen; in den simulierten WACD(1,1)- und GACD(1,1)-Reihen mit 500 Beobachtungen zeigt die Stichproben-ACF von êi keine signifikanten seriellen Korrelationen.
- Die 3534 positiven adjustierten Transaktionsdauern von IBM an den ersten fünf Handelstagen im November 1990 weisen serielle Korrelationen auf.
- Nach dem WACD(1,1) ψi = 0,169 + 0,064 xi−1 + 0,885 ψi−1 sind die Ljung-Box-Statistiken der standardisierten Innovationen Q(10) = 4,96 und Q(20) = 10,75; für die quadrierte Reihe gelten Q(10) = 6,20 und Q(20) = 11,16, also keine signifikante serielle Abhängigkeit.
- Im WACD(1,1) für diese IBM-Dauern gilt γ̂1 + ω̂1 ≈ 0,949 und zeigt damit eine gewisse Persistenz der adjustierten Dauern.
- Im GACD(1,1) ψi = 0,141 + 0,063 xi−1 + 0,897 ψi−1 liegt der Persistenzparameter γ̂1 + ω̂1 bei 0,96; für êi gelten Q(10) = 4,95 und Q(20) = 10,28, für die Quadrate Q(10) = 6,36 und Q(20) = 10,89.
- Die Stichproben-ACF der täglichen Logpreis-Range von Apple vom 4. Januar 1999 bis 20. November 2007, 2235 Beobachtungen, ist hochsignifikant und klingt langsam ab.
- Die standardisierten Residuen des GACD(1,1) für diese Apple-Range haben keine signifikanten seriellen Korrelationen, auch wenn die Lag-1-ACF knapp über der Grenze von zwei Standardfehlern liegt; nichtlineare ACD-Modelle entfernen diese Lag-1-Korrelation.
- Beim TWACD(2;1,1) für die Apple-Range liegen alle residualen ACFs innerhalb der Zwei-Standardfehler-Grenzen: Q(1) = 4,01 (p = 0,05) und Q(10) = 9,84 (p = 0,45) für die standardisierten Residuen, Q*(1) = 0,83 (p = 0,36) und Q*(10) = 9,35 (p = 0,50) für deren Quadrate.
- Im Interventionsmodell für dieselbe Apple-Range bleiben die residualen ACFs innerhalb der Zwei-Standardfehler-Grenzen, mit Q(1) = 2,37 (p = 0,12), Q(10) = 6,24 (p = 0,79), Q*(1) = 0,34 (p = 0,56) und Q*(10) = 6,79 (p = 0,75).
- Ein Wiener-Prozess hat unabhängige Zuwächse: für nicht überlappende Intervalle sind die Zuwächse unabhängig, und bedingt auf wt ist jede vergangene Information wj mit j < t für die Zukunft irrelevant.
- In der Finanzmarktliteratur hängt diese Markov-Eigenschaft mit einer schwachen Form der Markteffizienz zusammen.
- Für eine Brownsche Bewegung ist wt − ws bei s ≤ t unabhängig von wv für alle v ≤ s, und wt − ws hat dieselbe Verteilung wie wt−s − w0.
- Folgt der Aktienpreis einer geometrischen Brownschen Bewegung, sind die stetig verzinsten Renditen rt = ln(Pt) − ln(Pt−1) nicht seriell korreliert.
- Die täglichen Logrenditen von IBM 1998, 252 Beobachtungen, sind seriell unkorreliert; Q(10) = 4,9 ist gegenüber einer Chi-Quadrat-Verteilung mit 10 Freiheitsgraden hoch insignifikant.
- Die täglichen Logrenditen von Cisco Systems 2007, 251 Beobachtungen, zeigen keine serielle Korrelation; Q(12) = 12,30 mit p-Wert 0,42.
- Ist die Renditereihe seriell korreliert oder folgt der Preis nicht der geometrischen Brownschen Bewegung, müssen andere Verfahren Drift und Volatilität der Diffusionsgleichung schätzen.
- Das an die täglichen IBM-Logrenditen angepasste IGARCH(1,1) ohne Drift wird von den Q-Statistiken verworfen; Q(10) der quadrierten standardisierten Residuen beträgt 56,19 und ist hochsignifikant.
- Berman (1964) zeigt, dass dieselbe Grenzverteilung der Extremwerte für stationäre normale Folgen gilt, wenn die Autokorrelationsfunktion quadratisch summierbar ist, die Summe der quadrierten ρi also endlich bleibt.
- Die Regressionsmethode für Blockmaxima nimmt an, dass die Abweichungen ei nicht seriell korreliert sind.
- Die Diagonalelemente ρii(ℓ) der Lag-ℓ-Kreuzkorrelationsmatrix sind die Lag-ℓ-Autokorrelationen der Komponente rit.
- Die Diagonalelemente der Kreuzkorrelationsmatrizen {ρii(ℓ)} sind die Autokorrelationsfunktion der Komponente rit.
- Die monatlichen Logrenditen des S&P 500 von Januar 1926 bis Dezember 2008 haben marginale Autokorrelationen bei den Lags 1, 2, 3 und 5.
- Bei den monatlichen einfachen Renditen von US-Staatsanleihen, Januar 1942 bis Dezember 1999, sind die Stichproben-Autokorrelationen der 1-Jahres-Renditen bei Lag 1 und Lag 2 deutlich höher als die der längeren Laufzeiten; die Lag-1-Autokorrelation der 1-Jahres-Reihe ist 0,40 und die Lag-2-Autokorrelation 0,22.
- Für einen VMA(q) sind die Kreuzkorrelationsmatrizen ρℓ für alle ℓ größer als q gleich 0. Damit ist auch die Autokorrelationsfunktion jeder Komponente nach Lag q null, und die Randmodelle sind MA(q).
- Die beiden simulierten Komponenten des Modells (8.31), 200 Beobachtungen und Einheitsmatrix als Schockkovarianz, haben hohe Stichproben-Autokorrelationen und zeigen das Bild von Einheitswurzel-Nichtstationarität.
- Die Stichprobenkorrelation zwischen einer Unit-Root-nichtstationären und einer stationären Reihe konvergiert mit wachsender Stichprobe gegen null; Tsay und Tiao (1990) werden dafür angeführt.
- In der Fehlerkorrektur kann die stationäre Differenz Δxt deshalb nur über die stationäre Kombination β′xt−1 sinnvoll vom nichtstationären Niveau xt−1 abhängen.
- Die Johansen-Eigenwerte λ̂i sind die quadrierten partiellen kanonischen Korrelationen zwischen Δxt und xt−1, nachdem der deterministische Term und die verzögerten Differenzen herausgerechnet sind.
- Im dreiregimen Schwellenmodell für S&P-500-Future und Kasse hängt die Future-Logrendite in allen drei Regimen negativ von ihrem eigenen Lag 1 ab.
- Die monatlichen einfachen Renditen von Pfizer und Merck, Januar 1965 bis Dezember 2008, 528 Beobachtungen, haben keine signifikante Autokorrelation. Q(10) ist 10,48 mit p gleich 0,40 und 11,42 mit p gleich 0,33. Die Mittelgleichung enthält deshalb nur eine Konstante.
- Im DVEC(1,1) für diese beiden Reihen ist die Ljung-Box-Statistik der standardisierten Residuen für Pfizer Q(12) gleich 9,531 mit p gleich 0,657 und für Merck Q(12) gleich 12,349 mit p gleich 0,418. Für die quadrierten standardisierten Residuen ist Q(12) gleich 22,077 mit p gleich 0,03666 bei Pfizer und 6,437 mit p gleich 0,89246 bei Merck.
- Im BEKK(1,1) derselben Reihen ist Q(12) der standardisierten Residuen 9,465 mit p gleich 0,6628 für Pfizer und 11,591 mit p gleich 0,4791 für Merck. Für die Quadrate ist Q(12) gleich 21,55 mit p gleich 0,04291 bei Pfizer und 9,19 mit p gleich 0,68664 bei Merck. Die Prüfung der einzelnen Residuenreihen zeigt keine Modellunzulänglichkeit.
- Das konstante Korrelations-GARCH(1,1) für die Tageslogrenditen von Hang Seng und Nikkei 225 besteht die multivariaten Ljung-Box-Tests der standardisierten Residuen: Q2(4) gleich 17,29 mit p gleich 0,37 und Q2(12) gleich 48,21 mit p gleich 0,46, bezogen auf Chi-Quadrat-Verteilungen mit 16 und 48 Freiheitsgraden.
- Für das konstante Korrelations-GARCH(1,1) der monatlichen Logrenditen von IBM und dem S&P 500, Januar 1926 bis Dezember 1999, ist Q2(4) gleich 16,77 mit p gleich 0,21 und Q2(8) gleich 32,40 mit p gleich 0,30. Die Freiheitsgrade 13 und 29 sind angepasst, weil die Mittelgleichungen drei verzögerte Prädiktoren enthalten. Für die quadrierten Residuen gilt Q2(4) gleich 18,00 mit p gleich 0,16 und Q2(8) gleich 39,09 mit p gleich 0,10.
- Im Cholesky-GARCH für die monatlichen Logrenditen von IBM und dem S&P 500 ist q21,t gleich 0,0029 plus 0,9915 mal q21,t−1 minus 0,0041 mal a2,t−1. Der Koeffizient 0,9915 zeigt eine starke dynamische Abhängigkeit der Korrelationsgröße. Die Standardfehler sind 0,001, 0,002 und 0,0004. Alle Schätzungen sind auf dem 1-Prozent-Niveau signifikant.
- Die standardisierten Residuen dieses Cholesky-Modells haben Q2(4) gleich 19,77 mit p gleich 0,14 und Q2(8) gleich 34,22 mit p gleich 0,27. Für die Quadrate gilt Q2(4) gleich 15,34 mit p gleich 0,36 und Q2(8) gleich 31,87 mit p gleich 0,37.
- Für das zeitvariable Korrelations-GARCH(1,1) mit logistischer Korrelation gilt Q2(4) gleich 20,57 mit p gleich 0,11 und Q2(8) gleich 36,08 mit p gleich 0,21. Für die Quadrate gilt Q2(4) gleich 16,69 mit p gleich 0,27 und Q2(8) gleich 36,71 mit p gleich 0,19. Es bleibt keine signifikante serielle Korrelation.
- Bei den Tageslogrenditen von S&P 500, Cisco und Intel, 2. Januar 1991 bis 31. Dezember 1999, 2275 Beobachtungen, sind Q3(1) gleich 26,20, Q3(4) gleich 79,73 und Q3(8) gleich 123,68 hochsignifikant gegen Chi-Quadrat mit 9, 36 und 72 Freiheitsgraden, die p-Werte liegen nahe null.
- Dieselbe Kreuzkorrelationsstruktur zeigt: Die Tageslogrendite des S&P 500 hängt nicht von den vergangenen Renditen von Cisco oder Intel ab. Cisco hat eigene serielle Korrelation und hängt an den Lags 2 und 5 vom S&P 500 ab. Intel hängt an den Lags 1 und 5 vom S&P 500 ab. Der Markt wird von den vergangenen Renditen der einzelnen Unternehmen nicht signifikant beeinflusst.
- Im dreidimensionalen Modell haben die Korrelationsgrößen qij,t hohe Persistenz. Die AR(1)-Koeffizienten sind 0,824 für q21,t, 0,973 für q31,t und 0,981 für q32,t. Für diese Korrelationsgleichungen könnte ein AR(1) genügen.
- Die vier Tagesrenditen von Euro-Kurs, Yen-Kurs, IBM und Dell haben bei den Aktien kleine serielle Korrelationen. Die multivariate Ljung-Box-Statistik ist Q(3) gleich 59,12 mit p gleich 0,13 und Q(5) gleich 106,44 mit p gleich 0,03. Die univariaten Box-Ljung-Statistiken Q(12) sind 12,5, 6,4, 24,1 und 24,1.
- Im Faktor-Volatilitätsmodell der monatlichen Logrenditen von IBM und dem S&P 500 haben die standardisierten Residuen Q2(4) gleich 15,37 bei einem p-Wert von 0,29 und Q2(8) gleich 34,24 bei einem p-Wert von 0,23, also keine seriellen Korrelationen.
- Die quadrierten standardisierten Residuen desselben Modells haben Q-Stern-2(4) gleich 20,25 bei einem p-Wert von 0,09 und Q-Stern-2(8) gleich 61,95 bei einem p-Wert von 0,0004.
- Im lokalen Trendmodell sind die Messfehler et nicht seriell korreliert. Die dynamische Abhängigkeit von yt stammt allein aus dem Zustand μt.
- Für die erste Differenz wt gleich (1 minus B) yt gilt Cov(wt, wt minus 1) gleich minus σ²e und Cov(wt, wt minus j) gleich 0 für jedes j größer 1.
- Der Ein-Schritt-Prognosefehler vt hat Erwartungswert null und ist mit den früheren Beobachtungen yj für j kleiner t unkorreliert. Im linearen gaußschen Modell ist er von diesen Beobachtungen unabhängig.
- Die ARIMA(0,1,1)-Residuen der logarithmierten realisierten Alcoa-Volatilität haben Q(12) gleich 12,4 bei einem p-Wert von 0,33. Die quadrierten Residuen haben Q(12) gleich 8,2 bei einem p-Wert von 0,77.
- Unter der Normalannahme sind die Ein-Schritt-Prognosefehler vt des Kalman-Filters gegenseitig unabhängig. Die Transformation von y auf v hat eine Jacobi-Determinante von 1, und die gemeinsame Dichte zerfällt in das Produkt der Randdichten.
- Die standardisierten Prognosefehler der Alcoa-Log-RV, vt geteilt durch die Wurzel von Vt, haben Q(25) gleich 23,37 bei einem p-Wert von 0,56.
- Der Kalman-Gewinn Kt hängt nicht von μ1|0 und nicht von den Daten ab, sondern nur von Σ1|0, σ²e und σ²η. Damit ist die lineare Abbildung von den Beobachtungen auf die Prognosefehler durch diese Größen festgelegt.
- Im allgemeinen Kalman-Filter sind die Ein-Schritt-Prognosefehler vt seriell unabhängig, und die Menge vt bis vT ist unabhängig von Ft minus 1.
- Harveys Zustandsraumform eines ARMA trägt die serielle Abhängigkeit in den AR- und MA-Koeffizienten der Systemmatrizen und hat keine zusätzlichen Messfehler.
- In Akaikes Übergangsgleichung (11.37) gehen die Gewichte 1, ψ1 bis ψ m minus 1 als Koeffizienten der Innovation at plus 1 in den nächsten Zustand ein.
- Die Residuen des festen Marktmodells der monatlichen einfachen Überschussrenditen von General Motors, Januar 1990 bis Dezember 2003, haben eine Ljung-Box-Statistik von 24,2132 bei einem p-Wert von 0,3362.
- Die Durbin-Watson-Statistik dieser Residuen beträgt 2,0290.
- Nach den Residuendiagnosen erscheint das feste Marktmodell für die GM-Renditen angemessen, mit einem adjustierten R² von 23,3 Prozent.
- Im Markov-Switching-GARCH-M-Modell (12.55) folgt aus der Abhängigkeit der Rendite von der Volatilität, dass die Rendite auch seriell korreliert ist und das Modell damit eine gewisse Vorhersagbarkeit der Rendite hat.
- Die Zustände künftiger Renditen sind unbekannt, sodass eine Prognose dieses Modells eine Mischung über mögliche Zustandskonfigurationen ist und die Punktprognose oft hohe Unsicherheit hat.
- Beim GARCH-M für die monatlichen Logrenditen von General Electric von 1926 bis 1999 geben die Ljung-Box-Statistiken der standardisierten Residuen und ihrer Quadrate keinen Hinweis auf Modellunzulänglichkeit.
- Die Autokorrelationsfunktionen ökonomischer Zeitreihen wie Aktienkurse über Tage, Wochen oder Monate oder das Bruttosozialprodukt über Jahre fallen nicht exponentiell ab, wie sie es bei einem einfachen autoregressiven Prozess täten.
- Stattdessen erreichen die Autokorrelationsfunktionen vieler ökonomischer Zeitreihen eine Asymptote ungleich null und bleiben dort über die gesamte Reihe, oft auf niedrigem Niveau. Das zeigt, dass weiter zurückliegende Ereignisse die aktuellen Preise weiter beeinflussen.
- Weißes Rauschen hat keine Korrelation in der Zeit, und Random-Walk-Rauschen (Brownsche Bewegung) hat keine Korrelation zwischen den Inkrementen.
- Rauschen in ökonomischen Daten wird meist als langfristige Abhängigkeit oder Long Memory untersucht; 1/F-Rauschen ist gleichbedeutend mit langfristiger Abhängigkeit.
- Nach Ehlers lassen sich Märkte als Rauschen mit unterschiedlich starkem Langzeitgedächtnis beschreiben.
- Mit unkonventioneller Verarbeitung lässt sich über die Autokorrelation die Periodizität der Preisdaten ohne Verzerrung durch Spectral Dilation bestimmen; zudem liefert sie aufschlussreiche Wendepunktsignale.
- In einem Prozess mit langem Gedächtnis und normalverteilten Zufallszahlen folgt die Autokorrelation dem Potenzgesetz Autocorrelation(Lag) = C · Lag^−α, mit einer Konstanten C und α nominell gleich 1.
- Ein Grundprinzip der technischen Analyse ist, dass Marktdaten diesem Potenzgesetz eines effizienten Marktes nicht folgen und sich daher Information aus der partiellen Korrelation der Autokorrelationsfunktion gewinnen lässt.
- Eine Folge perfekt zufälliger Zahlen korreliert mit sich selbst perfekt, bei einem Lag von nur einem Bar sinkt die Korrelation jedoch dramatisch.
- Bei einer Sinuswelle mit 20 Bars Periode ist die über eine Periode gemittelte Autokorrelation bei Lag 0 gleich 1, sinkt mit zunehmendem Lag bis zur perfekten Antikorrelation bei Lag 10 und ist bei Lag 20 wieder perfekt; die Korrelationswerte verlaufen als Funktion des Lags exakt sinusförmig.
- Marktdaten sind deutlich unordentlicher als reine Zufallszahlen oder perfekte Sinuswellen, enthalten aber Merkmale von beiden.
- Bei zyklischen Preisumkehren wechselt die Autokorrelation bei allen Lag-Werten von Grün zu Rot oder von Rot zu Grün; dieser dramatische Wechsel kann als zuverlässiger Umkehrindikator genutzt werden.

## Funktionsweise

- Die aktuelle Preisänderung wird mit der vorherigen Änderung korreliert, also mit Lag 1, dann mit der Änderung davor, Lag 2, und so fort. Für jeden dieser Lags wird ein Korrelationskoeffizient berechnet.
- In einer zufälligen Datenreihe fallen die Korrelationen typischerweise sehr schnell als Funktion des Lag-Intervalls ab.
- Ist die Zeitreihe der Preisänderungen in linearer Weise nichtzufällig, unterscheiden sich einige Autokorrelationskoeffizienten signifikant vom Muster der Autokorrelationen einer Zufallsfolge.
- Die Lag-1-Stichprobenautokorrelation ist die Summe (rt − r̄)(rt−1 − r̄) von t = 2 bis T, geteilt durch die Summe (rt − r̄)² von t = 1 bis T, mit r̄ als Stichprobenmittel.
- Die Lag-ℓ-Stichprobenautokorrelation ist die Summe (rt − r̄)(rt−ℓ − r̄) von t = ℓ+1 bis T, geteilt durch die Summe (rt − r̄)² von t = 1 bis T, für 0 ≤ ℓ < T − 1.
- Die Lag-l-Stichprobenautokorrelation ist die Summe von t gleich l plus 1 bis T von (rt minus Stichprobenmittel) mal (rt−l minus Stichprobenmittel), geteilt durch die Summe von t gleich 1 bis T der quadrierten Abweichungen vom Stichprobenmittel, für 0 kleiner oder gleich l kleiner als T minus 1.
- Ist {rt} unabhängig und identisch verteilt mit endlichem E(rt zum Quadrat), dann ist die Stichprobenautokorrelation asymptotisch normal mit Mittel null und Varianz 1/T; die t-Ratio Wurzel aus T mal ρ-Dach 1 prüft H0: ρ1 gleich 0 gegen die zweiseitige Alternative und folgt asymptotisch der Standardnormalverteilung.
- Nach Bartletts Formel ist die Stichprobenautokorrelation für rt gleich µ plus Summe von i gleich 0 bis q von ψi mal a(t−i), mit ψ0 gleich 1 und weißem Rauschen aj, bei l größer als q asymptotisch normal mit Mittel null und Varianz (1 plus 2 mal Summe der ersten q quadrierten Autokorrelationen) geteilt durch T.
- Viele Programme setzen die asymptotische Varianz der Stichprobenautokorrelation für alle l ungleich 0 auf 1/T und unterstellen damit im Kern eine unabhängig und identisch verteilte Reihe.
- Für einen stationären AR(2) gilt ρ0 gleich 1, ρ1 gleich phi1 geteilt durch (1 minus phi2) und ρl gleich phi1 mal ρ(l minus 1) plus phi2 mal ρ(l minus 2) für l mindestens 2; reelle charakteristische Wurzeln mischen zwei exponentielle Abfälle, komplexe Wurzeln erzeugen gedämpfte Sinus- und Kosinuswellen.
- Die Portmanteau-Statistik von Box und Pierce ist Q-Stern von m gleich T mal der Summe der ersten m quadrierten Stichprobenautokorrelationen und ist unter unabhängig und identisch verteilten rt mit bestimmten Momentbedingungen asymptotisch chi-quadrat mit m Freiheitsgraden.
- Die Ljung-Box-Statistik ist Q(m) gleich T mal (T plus 2) mal der Summe von l gleich 1 bis m von ρ-Dach l zum Quadrat geteilt durch (T minus l); die Null aller Autokorrelationen bis m wird verworfen, wenn Q(m) das (1 minus α)-Quantil der Chi-Quadrat-Verteilung mit m Freiheitsgraden übersteigt oder der p-Wert höchstens α ist.
- Simulationsstudien legen für Q(m) die Wahl m ungefähr gleich dem natürlichen Logarithmus von T nahe, weil sie bessere Power liefert; bei saisonalen Reihen sind Autokorrelationen an Vielfachen der Saisonalität wichtiger.
- Die partielle Autokorrelation eines stationären gaußschen AR(p) bricht beim Lag p ab: die Stichproben-PACF konvergiert beim Lag p gegen den wahren Koeffizienten, für alle größeren Lags gegen null, und ihre asymptotische Varianz ist dort 1/T.
- Für ein gaußsches AR(l) ist AIC(l) gleich dem Logarithmus der Maximum-Likelihood-Schätzung der Innovationsvarianz plus 2l geteilt durch T, und BIC(l) gleich demselben Logarithmus plus l mal ln(T) geteilt durch T; gewählt wird die Ordnung mit dem Minimum, und BIC bestraft jeden Parameter mit ln(T) statt mit 2, sodass es bei mittlerer oder großer Stichprobe tendenziell eine niedrigere Ordnung wählt.
- Die Unabhängigkeit nach Bereinigung um erklärende Variablen wird über die Stichproben-Autokorrelationsfunktionen von zti und wti geprüft; unter Unabhängigkeit sollen beide keine seriellen Korrelationen haben.
- In der vereinfachten Notation von Tiao und Box (1981) steht ein Plus, wenn der Koeffizient mindestens 2 geteilt durch die Wurzel aus T ist, ein Minus, wenn er höchstens minus 2 geteilt durch die Wurzel aus T ist, und ein Punkt dazwischen. 1 geteilt durch die Wurzel aus T ist der asymptotische 5-Prozent-kritische Wert unter weißem Rauschen.
- Für die 996 Monate von IBM und S&P 500 beträgt der genäherte Standardfehler der geschätzten Korrelationen 1 geteilt durch die Wurzel aus 996, also 0,03169. Die gestrichelten Linien der Autokorrelations- und Kreuzkorrelationsplots sind die asymptotischen Grenzen von zwei Standardfehlern.
- Peter Swerling modellierte verrauschte Radarechos als Konstante plus Zufallszahl mit Gedächtnis, in Tradersprache als EMA von Zufallszahlen; das Swerling-Modell ist mit dem 1/F^α-Spektralmodell mit Zufallseingaben und langem Gedächtnis vereinbar.
- Synthetische Preise aus einer EMA von Zufallszahlen sind eine brauchbare Annäherung an reale Marktpreise; Preise lassen sich daher als Zufallszahlen mit Gedächtnis auffassen, deren Gedächtnisanteil die Korrelation mit der jüngeren Historie nutzen soll.
- Der einzige Input des Autokorrelationsindikators ist die Mittelungslänge; beim Standardwert 0 entspricht sie jeweils dem Lag, sodass die Mittelung die maximale Zahl an Datenpunkten ohne Überlappung von Original- und verzögertem Datenstrom enthält.
- Vor der Korrelation entfernt ein zweipoliger Hochpass auf 48 Bars die langen Wellen; 48 Bars sind mehr als zwei Monate Tagesdaten bzw. vier Stunden 5-Minuten-Bars, längere Wellen haben vermutlich keinen Nutzen für zyklisches Trading. Danach folgt ein 10-Bar-SuperSmoother.
- Für jeden Lag von 1 bis 48 wird eine Lehrbuch-Pearson-Korrelation berechnet; das Ergebnis zwischen −1 und +1 wird für die Darstellung auf 0 bis 1 skaliert.
- Die Heatmap zeigt vertikal die Lags 3 bis 48; Grün steht für perfekte Korrelation, Rot für perfekte Antikorrelation und Gelb für Zwischenwerte (Stoplight-Darstellung).
- Für die Autocorrelation Reversals werden die Bar-zu-Bar-Änderungen der Autokorrelationsfunktion über alle Lags summiert; ist die Summe groß, ist ein Wendepunkt identifiziert.
- Im Code wird für jeden Lag von 3 bis 48 gezählt, ob die auf 0 bis 1 skalierte Korrelation zwischen vorigem und aktuellem Bar die Schwelle 0,5 kreuzt; ist diese Summe größer als 24, wird Reversal = 1 gesetzt.
- Die Standardeingaben des Autocorrelation-Reversals-Indikators sind HPLength 48, LPLength 10 und AvgLength 3.

## Voraussetzungen

- Für den Extremalindex der negativen täglichen IBM-Logrenditen wurde die Blockgröße k gleich 10 gewählt, weil die täglichen Logrenditen nur schwach seriell abhängig sind.

## Anwendung im Trading

- Eine Fassung des Capital Asset Pricing Model besagt, dass die Rendite eines Assets nicht prognostizierbar ist und keine Autokorrelationen haben soll; der Test auf Autokorrelation null dient der Prüfung der Effizienzmarkthypothese.
- Preisbildung und Indexberechnung können Autokorrelationen in die beobachtete Rendite bringen, besonders bei Hochfrequenzdaten, etwa durch Bid-Ask-Bounce und nichtsynchrone Umsätze.
- Ehlers hält das Kapitel für Algo-Trader für wichtig, weil der Autokorrelationsprozess mehrere eigenständige und nützliche Indikatoren hervorbringt.
- Mit LPLength 20 eignen sich die Umkehrsignale für Handelssysteme mit Haltedauern von 10 bis 20 Bars, mit LPLength 10 für aktivere Systeme mit Haltedauern von einigen Tagen bis zu einer Woche.

## Regeln und Kriterien

- Ist {rt} eine iid-Folge mit endlichem zweiten Moment, dann ist die Lag-1-Stichprobenautokorrelation asymptotisch normal mit Mittelwert null und Varianz 1/T; Beleg ist Brockwell und Davis (1991, Theorem 7.2.2). Dieselbe asymptotische Verteilung mit Varianz 1/T gilt für jedes feste positive ℓ.
- Der Test H0: ρ1 = 0 gegen Ha: ρ1 ≠ 0 verwendet die t-Statistik Wurzel(T) mal ρ̂1, asymptotisch standardnormal. Verworfen wird, wenn die t-Statistik betragsmäßig groß ist oder gleichbedeutend der p-Wert klein ist, etwa unter 0,05.
- Die meisten Zeitreihenpakete passen die Freiheitsgrade der Ljung-Box-Statistik auf Residuen nicht an; das ist verständlich, wenn m kleiner oder gleich der Zahl der geschätzten AR-Koeffizienten ist.
- Nach Anpassung an erklärende Variablen prüft man die Unabhängigkeit eines zweidimensionalen Poisson-Modells für Überschreitungen an den Stichproben-Autokorrelationsfunktionen der Dauergrößen zti und der Exzessgrößen wti; unter Unabhängigkeit sollen beide keine seriellen Korrelationen zeigen.
- Für gaußsche Folgen mit Autokorrelation ρn ist die Bedingung D(un) erfüllt, wenn ρn mal ln(n) für n gegen unendlich gegen 0 geht (Berman 1964).
- Die Stichproben-Kreuzkorrelationsmatrizen identifizieren die Ordnung eines VMA, weil ρℓ für ℓ größer als q verschwindet.
- Die angezeigten Umkehren reagieren sehr empfindlich auf die Glättung der Preisdaten; über die Eingabe LPLength lässt sich die Zahl der angezeigten Umkehren verringern oder erhöhen, eine höhere LPLength verringert sie.
- Auch AvgLength beeinflusst die Zahl der angezeigten Umkehren; bei einer Erhöhung ist Vorsicht geboten, weil der Lag des Indikators direkt proportional zu AvgLength steigt; bei AvgLength 3 beträgt die typische Verzögerung etwa drei Bars.
- HPLength ist für volle Flexibilität als Eingabe verfügbar, eine Änderung wirkt sich aber nur relativ gering auf die angezeigten Umkehren aus.

## Risiken und Grenzen


## Beispiele

- Bei den monatlichen IBM-Renditen von Januar 1926 bis Dezember 2008 liegen alle Stichprobenautokorrelationen innerhalb der zweifachen Standardfehlergrenzen und sind auf dem 5-Prozent-Niveau nicht von null verschieden; für einfache Renditen sind Q(5) gleich 3,37 und Q(10) gleich 13,99 mit p-Werten 0,64 und 0,17, für Logrenditen Q(5) gleich 3,52 und Q(10) gleich 13,39 mit p-Werten 0,62 und 0,20.
- Beim monatlichen wertgewichteten CRSP-Index sind Q(5) gleich 29,71 und Q(10) gleich 39,55 für die einfachen Renditen sowie Q(5) gleich 28,38 und Q(10) gleich 36,16 für die Logrenditen; alle vier p-Werte liegen unter 0,0001, und die serielle Abhängigkeit ist stärker als bei der Einzelaktie IBM.
- Beim wertgewichteten Index mit T gleich 996 ist der asymptotische Standardfehler der Stichproben-PACF ungefähr 0,032; auf dem 5-Prozent-Niveau wird ein AR(3) oder AR(9) identifiziert, auf dem 1-Prozent-Niveau ein AR(3).
- In Tabelle 2.1 liegt das AIC-Minimum bei minus 5,849 für p gleich 9 und das BIC-Minimum bei minus 5,833 für p gleich 1, mit minus 5,831 für p gleich 3 knapp dahinter; verschiedene Kriterien können verschiedene Ordnungen liefern, und fachliche Information sowie Einfachheit entscheiden mit.
- Die ACF eines schwach stationären AR(1) ist phi1 hoch l und fällt exponentiell mit Rate phi1 vom Startwert 1; bei positivem phi1 glatt, bei negativem phi1 in zwei alternierenden exponentiellen Ästen mit Rate phi1 zum Quadrat, gezeigt für phi1 gleich 0,8 und minus 0,8.
- Die monatlichen einfachen Renditen des gleichgewichteten CRSP-Index von Januar 1926 bis Dezember 2008 haben signifikante Stichprobenautokorrelationen bei den Lags 1, 3 und 9; identifiziert wird rt gleich c0 plus at minus θ1 a(t−1) minus θ3 a(t−3) minus θ9 a(t−9).
- Anders als die Stichproben-PACF zeigt die Stichproben-ACF, welche MA-Lags von null verschieden sind.
- Für die monatlichen Logrenditen der 3M-Aktie von Februar 1946 bis Dezember 2008, 755 Beobachtungen, zeigt die ACF auf dem 1-Prozent-Niveau keine signifikante serielle Korrelation, und die EACF legt ein ARMA(0,0) nahe, also weißes Rauschen; die Schwelle 2 geteilt durch die Wurzel aus 755 beträgt 0,073.
- Einzelne EACF-Kreuze bei den MA-Ordnungen 2, 5, 9 und 11 gehören zu Stichprobenwerten um 0,08 oder 0,09 und lägen beim 1-Prozent-Kriterium unter der Schwelle, würden also zu Nullen.
- Für die Residuen des AR(3) des wertgewichteten Index ist Q(12) gleich 16,35; mit 9 Freiheitsgraden beträgt der p-Wert 0,060, mit den von R verwendeten 12 Freiheitsgraden 0,1756 bei X-squared gleich 16,3525.
- Nach Streichen des Lag-2-Terms ist Q(12) gleich 16,83 mit p-Wert 0,078 auf der Chi-Quadrat-Verteilung mit 10 Freiheitsgraden; R meldet bei 12 Freiheitsgraden X-squared gleich 16,8276 und p-Wert 0,1562.
- Die Logrenditen von 3M von Februar 1946 bis Dezember 2008 haben nach der erweiterten Autokorrelation keine signifikante serielle Korrelation.
- Die Logreihe des vierteljährlichen US-BIP von 1947.I bis 2008.IV hat hohe serielle Stichprobenkorrelationen.
- Bei den vierteljährlichen Loggewinnen von Johnson & Johnson von 1960 bis 1980 ist die Autokorrelation der ersten Differenz an Vielfachen der Periode 4 stark; nach regulärer und saisonaler Differenz bleibt eine signifikant negative Autokorrelation bei Lag 1 und eine marginal negative bei Lag 4.
- Die monatlichen einfachen Renditen des CRSP-Decile-1-Index von Januar 1970 bis Dezember 2008, 468 Beobachtungen, zeigen im Zeitplot kein klares Saisonmuster, in der Stichprobenautokorrelation aber signifikante Lags bei 1, 12, 24 und 36.
- Nach der Regression auf eine Januar-Dummy verschwinden die seriellen Korrelationen bei den Lags 12, 24 und 36 weitgehend.
- Beim homogenen Poisson-Modell für die negativen IBM-Tageslogrenditen und Schwelle 2,5 Prozent haben sowohl zti als auch wti signifikante Autokorrelationen; die eingezeichneten Grenzen sind zwei asymptotische Standardfehler.
- Im homogenen zweidimensionalen Poisson-Modell für die mittelwertbereinigten täglichen IBM-Logrenditen vom 3. Juli 1962 bis 31. Dezember 1998, Schwelle 2,5 Prozent, haben zti und wti signifikante serielle Korrelationen jenseits der asymptotischen Grenzen von zwei Standardfehlern.
- Die Portmanteau-Statistiken der bivariaten Monatsrenditen sind Q2(1) gleich 9,81, Q2(5) gleich 47,06 und Q2(10) gleich 71,65. Gegen Chi-Quadrat mit 4, 20 und 40 Freiheitsgraden sind die p-Werte 0,044, 0,001 und 0,002; zum Niveau 5 Prozent liegt serielle Abhängigkeit vor.
- Für die Residuen des vereinfachten VAR(5) sind Q2(4) gleich 16,64 und Q2(8) gleich 31,55, mit p-Werten 0,083 und 0,208. Zum Niveau 5 Prozent ist das Modell hinsichtlich serieller und Kreuzkorrelationen der Residuen angemessen.
- Die Residuen des VARMA(2,1) für die logarithmierten US-Monatssätze haben kleine serielle und Kreuzkorrelationen bei den Lags 7 und 11. Das Modell erfasst die dynamische Struktur dennoch einigermaßen.
- Die Stichproben-Autokorrelationsfunktion der Kleinste-Quadrate-Residuen des BHP-VALE-Spreads fällt exponentiell ab und stützt damit, dass der geschätzte Spread stationär ist.
- Die partielle Autokorrelationsfunktion der wöchentlichen Änderungen des dreijährigen US-Treasury-Zinses, 18. März 1988 bis 10. September 1999, legt ein AR(3) nahe.
- Die Ljung-Box-Statistik der Residuen dieses AR(3) ist Q(12) = 11,4 und auf dem 5-Prozent-Niveau insignifikant.
- Im Regressionsmodell der Zinsänderungen mit AR(2)-Fehler ist die residuelle Autokorrelationsfunktion an den Lags 4 und 6 nur marginal signifikant; das Modell erscheint ansonsten angemessen.
- Für das Gauß-GARCH(1,1) der monatlichen S&P-500-Logrenditen, Januar 1962 bis Dezember 2009, sind die Ljung-Box-Statistiken der standardisierten Residuen und ihrer Quadrate Q(12) = 10,04 (p 0,61) und 6,14 (p 0,91) und zeigen keine Modellunzulänglichkeit.
- Der Posteriormittelwert von α1 im stochastischen Volatilitätsmodell derselben Reihe ist 0,837 bei Standardfehler 0,025 und bestätigt starke serielle Abhängigkeit der Volatilität; der Wert liegt unter dem von Jacquier, Polson und Rossi (1994) für Tagesrenditen.
- Weil {zt} seriell korreliert ist, ist gemeinsames Ziehen der Logvolatilität effizienter als einzelnes Ziehen.
- Bei Dollar General (DG) über etwa ein Jahr wird der Autokorrelationsindikator am unteren Rand bei jeder Preisumkehr rot und zwischen den Umkehren grün; nach oben wird die Darstellung wegen der stärkeren Glättung bei längeren Lags wolkenartig und liefert gemischte Signale, etwa Antikorrelation um 20 Bars und gute Korrelation bei 30 bis 40 Bars im selben Zeitraum.
- Mit der minimalen Mittelungslänge von drei Bars zeigt der Indikator bei Preisumkehren für alle Lags einen scharfen Wechsel von Rot zu Grün bzw. Grün zu Rot sowie eine zeitlich variierende Dicke und Anzahl der Balken über die Lags.
- Bei einer theoretischen 20-Bar-Sinuswelle erfolgen die scharfen Farbwechsel genau drei Bars nach Gipfeln und Tälern, und der Lag-Abstand vom unteren Rand eines roten Balkens zum nächsten roten Balken darüber beträgt genau 20 Bars, also die Periodizität der Welle.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 77–96 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-005-p077-p096|S. 77–96]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 96–115 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-006-p096-p115|S. 96–115]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 144–163 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-011-p144-p163|S. 144–163]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 163–165 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-012-p163-p165|S. 163–165]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 39–58 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-003-p039-p058|S. 39–58]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 58–77 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-004-p058-p077|S. 58–77]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 77–96 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-005-p077-p096|S. 77–96]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 96–115 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-006-p096-p115|S. 96–115]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 115–134 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-007-p115-p134|S. 115–134]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 134–153 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-008-p134-p153|S. 134–153]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 153–172 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-009-p153-p172|S. 153–172]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 191–210 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-011-p191-p210|S. 191–210]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 229–248 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-013-p229-p248|S. 229–248]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 248–267 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-014-p248-p267|S. 248–267]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 267–286 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-015-p267-p286|S. 267–286]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 286–305 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-016-p286-p305|S. 286–305]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 305–324 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-017-p305-p324|S. 305–324]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 343–362 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-019-p343-p362|S. 343–362]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 362–381 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-020-p362-p381|S. 362–381]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 381–400 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-021-p381-p400|S. 381–400]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 400–419 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-022-p400-p419|S. 400–419]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 419–438 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-023-p419-p438|S. 419–438]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 438–457 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-024-p438-p457|S. 438–457]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 457–476 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-025-p457-p476|S. 457–476]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 476–495 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-026-p476-p495|S. 476–495]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 533–552 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-029-p533-p552|S. 533–552]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 552–571 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-030-p552-p571|S. 552–571]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 571–590 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-031-p571-p590|S. 571–590]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 590–609 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-032-p590-p609|S. 590–609]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 609–628 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-033-p609-p628|S. 609–628]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 628–647 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-034-p628-p647|S. 628–647]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 647–666 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-035-p647-p666|S. 647–666]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 666–685 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-036-p666-p685|S. 666–685]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 685–704 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-037-p685-p704|S. 685–704]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 71–83 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-007-p071-p083|S. 71–83]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 97–116 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-009-p097-p116|S. 97–116]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 116–120 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-010-p116-p120|S. 116–120]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 140–159 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-012-p140-p159|S. 140–159]]

## Verwandte Themen
