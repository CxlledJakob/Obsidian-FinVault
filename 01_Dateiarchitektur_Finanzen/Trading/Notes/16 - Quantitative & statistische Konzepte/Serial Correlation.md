---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Zeitreihen"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Serial Correlation


## Kurzdefinition

- Serielle Korrelation und Autokorrelation bezeichnen im Buch dieselbe Größe: die Korrelation der interessierenden Variable mit ihren eigenen Vergangenheitswerten.
- Eine schwach stationäre Reihe rt ist genau dann nicht seriell korreliert, wenn ρℓ = 0 für alle ℓ > 0.

## Kernaussagen

- Serielle Bedingtheit der Labels macht die gewöhnliche k-Fold-Cross-Validation unbrauchbar, weil die Zufallsziehung redundante Beobachtungen sowohl ins Trainings- als auch ins Testset streut.
- Deshalb braucht es ein Validierungsverfahren, das das Modell an den Beobachtungen bewertet, die am wenigsten mit den Trainingsbeobachtungen korreliert oder redundant sind.
- Bei langreichweitiger serieller Abhängigkeit genügt es nicht, eine Beobachtung hinter dem Ende des Trainingssets zu testen, um Informationsleakage zu vermeiden.
- Toth et al. (2011) untersuchen den signierten Orderflow von Aktien der London Stock Exchange und finden über viele Tage positiv autokorrelierte Orderzeichen.
- Die zwei von ihnen geprüften Erklärungen sind Herding und Order Splitting.
- Auf Zeitskalen von weniger als einigen Stunden geht die Persistenz überwiegend auf Order Splitting zurück.
- Die Mikrostrukturtheorie führt die Persistenz des Orderflow-Ungleichgewichts auf die Anwesenheit informierter Händler zurück.
- Die Stärke dieser Persistenz lässt sich über die serielle Korrelation der signierten Volumina messen.
- Ein solches Feature ergänzt die Features der sequenziellen Handelsmodelle in Abschnitt 19.5.
- Das Roll-Modell nimmt serielle Unabhängigkeit der Aggressorzeichen an, E[bt bt−1] = 0.
- Die halbe Geld-Brief-Spanne ergibt sich dort aus der seriellen Kovarianz der Preisänderungen, c = √max{0, −σ[Δpt, Δpt−1]}.
- Empirisch weisen Finanzzeitreihen serielle Abhängigkeit auf.
- Den simulierten Renditen des zweiten Hypothesentests fehlen die Korrelationen, die in den beobachteten Reihen stecken.
- Lässt sich auf solchen Zufallsreihen mit guter Wahrscheinlichkeit eine mindestens ebenso gute Strategierendite erzeugen, erfasst die Momentum-Strategie kein Momentum und keine seriellen Korrelationen der Renditen und ist nur deshalb profitabel, weil die beobachtete Verteilung einen bestimmten Mittelwert und eine bestimmte Form hat.
- Von 10.000 solchen Reihen lagen 1.166 mindestens auf der beobachteten durchschnittlichen Rendite. Die Null ließ sich nur mit 88 Prozent Wahrscheinlichkeit verwerfen, und die Form der Verteilung hat etwas mit dem Erfolg zu tun.
- Die anti-serielle Korrelation der Renditen ist handelbar und ist dasselbe wie die Mean Reversion der Preise; die Mean Reversion der Renditen selbst ist nicht handelbar.
- Cross-sectional Mean Reversion impliziert, dass die kurzfristigen relativen Renditen der Instrumente seriell antikorreliert sind.
- Eine trendende Reihe hat positive Korrelationen aufeinanderfolgender Preisbewegungen und einen Hurst-Exponenten über 0,5.
- Viele Futures-Renditen weisen serielle Korrelation auf, und diese Korrelation tritt nur auf einer ziemlich langen Zeitskala auf.
- Das Vorzeichen der Rollrendite wechselt typischerweise selten, die Futures bleiben also lange in Contango oder Backwardation, während die Spot-Rendite Vorzeichen und Größe sehr schnell wechselt.
- Wird ein Future lange gehalten und dominieren die durchschnittlichen Rollrenditen die durchschnittliche Gesamtrendite, entsteht serielle Korrelation der Gesamtrenditen.
- Querschnittliches Momentum bei Währungen lässt sich der seriellen Korrelation des Weltwirtschafts- oder Zinswachstums zuschreiben.
- Eine kritische Annahme ist, dass die Beobachtungen der Stichprobe unabhängig sind. Sind sie seriell korreliert, wie es in einer Zeitreihe der Fall sein kann, sinkt die Varianz langsamer, als die Quadratwurzelregel nahelegt.
- Diese langsamere Varianzsenkung gilt, wenn die Teststatistik der Stichprobenmittelwert ist, aber nicht allgemein.
- Erreichen viele simulierte Renditepfade mit denselben ersten Momenten, aber ohne die seriellen Korrelationen, mindestens die Backtest-Rendite der Momentum-Strategie, erfasst sie kein echtes Momentum und keine serielle Korrelation, sondern profitiert von Mittelwert und Form der Verteilung.
- Bei der TU-Strategie erreichen 1.166 von 10.000 solchen Pfaden die beobachtete Durchschnittsrendite, deshalb hat die Form der Verteilung mit dem Erfolg zu tun.
- Anti-Serienkorrelation der Renditen ist handelbar und gleichbedeutend mit Mean Reversion der Preise. Die Mean Reversion der Renditen selbst lässt sich nicht handeln.
- Preisänderungen haben oft serielle Korrelation: die ADF-Null lässt sich häufig erst mit Lag k gleich 1 verwerfen, mit k gleich 0 dagegen nicht.
- Querschnitts-Mean-Reversion bedeutet, dass die kurzfristigen relativen Renditen seriell antikorreliert sind. Die relative Rendite ist die Rendite des Instruments minus die Rendite des Korbs.
- Viele Futures-Renditen sind seriell korreliert, aber nur auf einer ziemlich langen Zeitskala.
- Das passt zu BR, HG und TU, deren Rollrenditen laut Tabelle 5.1 betragsmäßig größer sind als ihre Spot-Renditen.
- Für C gilt die Erklärung nicht, obwohl C die betragsmäßig größte Rollrendite gegenüber der durchschnittlichen Spot-Rendite hat.
- Querschnittliches Momentum von Währungen lässt sich über serielle Korrelation des Weltwirtschafts- oder Zinswachstums erklären, das von Aktien über die langsame Diffusion, Analyse und Annahme neuer Information.
- Beispiel 1.1 zeigt, dass eine Renditereihe ohne serielle Autokorrelationen, aber mit derselben Kurtosis wie die TU-Futures, in 12 Prozent der Zufallsziehungen dieselben Renditen wie die TU-Momentum-Strategie erzeugen kann.
- Haben Asset-Renditen nur schwache empirische serielle Korrelationen, liegen ihre Randverteilungen nahe bei ihren bedingten Verteilungen.
- Bedingte Verteilungen sind für die Untersuchung von Asset-Renditen relevanter als Randverteilungen; Randverteilungen lassen sich aus vergangenen Renditen aber leichter schätzen.
- Eine schwach stationäre Reihe ist genau dann frei von serieller Korrelation, wenn jede Autokorrelation mit positivem Lag null ist.
- Die statistisch signifikante Lag-1-Autokorrelation der monatlichen Rendite des CRSP-Value-Weighted-Index zeigt, dass die verzögerte Rendite für die Prognose der laufenden Rendite nützlich sein kann; das zugehörige Modell ist das AR(1).
- Beim AR(1) gilt die Markov-Eigenschaft: bedingt auf rt−1 ist rt mit rt−i für i größer als 1 nicht korreliert.
- Ist ein angepasstes Modell angemessen, soll die Residuenreihe weißes Rauschen sein; Autokorrelation und Ljung-Box-Statistik der Residuen prüfen diese Nähe.
- Für die Residuen eines AR(p) folgt die Ljung-Box-Statistik Q(m) asymptotisch chi-quadrat mit m minus g Freiheitsgraden, wobei g die Zahl der AR-Koeffizienten ist.
- Die AR-Koeffizienten des angepassten AR(3) für den wertgewichteten Index sind klein; die serielle Abhängigkeit ist schwach, auch wenn sie auf dem 1-Prozent-Niveau signifikant ist.
- Ein MA(q) ist nur linear mit seinen ersten q verzögerten Werten verbunden und heißt deshalb Modell mit endlichem Gedächtnis.
- Zeigt die Autokorrelation der Residuen weitere serielle Korrelation, wird das Modell erweitert, damit es diese Korrelation aufnimmt.
- Die Null des Ljung-Box-Tests auf den Residuen lautet, dass in den geprüften Lags keine residuelle serielle Korrelation vorliegt.
- Die Stichprobenautokorrelationen einer Unit-Root-Reihe nähern sich mit wachsender Stichprobe sämtlich der 1, weil jeder vergangene Schock dauerhaft in der Reihe bleibt.
- Bei einer saisonalen Reihe ist die Autokorrelation der ersten Differenz stark an Vielfachen der Periode.
- Eine konventionelle Antwort auf sehr starke serielle Korrelation einer integrierten Reihe ist die erste Differenz.
- Ist der Regressionsfehler seriell korreliert, müssen die Kleinste-Quadrate-Schätzungen von Achsenabschnitt und Steigung nicht konsistent sein; dieses Modell wird oft falsch benutzt, weil diese Abhängigkeit übersehen wird.
- Die Residuen der Niveauregression von Drei- auf Einjahreszins sind stark seriell korreliert und fallen langsam, im Muster einer Einheitswurzel.
- In der Regression der Änderungen sind die seriellen Restkorrelationen noch signifikant, aber deutlich kleiner, und werden durch ein MA(1) ohne Konstante aufgefangen: et gleich at plus 0,1823 mal at minus 1.
- Danach ist die Lag-1-Restkorrelation nicht mehr signifikant; kleinere serielle Korrelationen bleiben auf den Lags 4, 6 und 7.
- Die beiden Wochenzinsen sind gleichzeitig und seriell korreliert: r3t gleich r3,t minus 1 plus 0,794 mal (r1t minus r1,t minus 1) plus at plus 0,182 mal at minus 1.
- Durbin-Watson erfasst nur die serielle Korrelation zum Lag 1 und ist näherungsweise 2 mal (1 minus rho Dach 1); bei Saisonalität ist die Ljung-Box-Statistik vorzuziehen.
- Für die Änderungsregression beträgt Durbin-Watson 1,6456 und Ljung-Box 230,0477 mit p-Wert 0; mit beiden ersten Lags als Regressoren beträgt Durbin-Watson 1,9865 und Ljung-Box weiter 131,6048 mit p-Wert 0.
- Die Absolutreihen der täglichen einfachen CRSP-Indexrenditen, wert- und gleichgewichtet, vom 2. Januar 1970 bis 31. Dezember 2008 bleiben in der Stichproben-Autokorrelation auch nach 300 Lags auf dem 5-Prozent-Niveau signifikant und fallen nur langsam (Ding, Granger und Engle 1993).
- Die monatlichen Intel-Logrenditen von Januar 1973 bis Dezember 2008 sind bis auf eine kleine Autokorrelation bei Lag 7 seriell unkorreliert, Q(12) gleich 18,26 mit p-Wert 0,11, aber über die Quadrate und Absolutbeträge abhängig.
- Der ARCH-Schock ist seriell unkorreliert und zugleich abhängig; große vergangene Quadrate ziehen eine große bedingte Varianz nach sich.
- Die zehnminütigen Mark-Dollar-Änderungen von 2488 Beobachtungen im Juni 1989 haben keine serielle Korrelation, ihre Quadrate aber ARCH-Effekte mit Spitzen in der partiellen Autokorrelation.
- Tagesrenditen eines Index zeigen oft kleine serielle Korrelationen, Monatsrenditen oft keine.
- Die Ljung-Box-Statistik der standardisierten Residuen prüft die Mittelgleichung auf verbliebene serielle Korrelation, die der quadrierten standardisierten Residuen die Volatilitätsgleichung.
- Die monatlichen S&P-500-Überschussrenditen von 1926 bis 1991 haben serielle Korrelationen auf den Lags 1 und 3; ein MA(3) hat die Koeffizienten 0,0944 und minus 0,1407 bei einer residualen Standardabweichung von 0,0576.
- Nach dem GARCH(1,1) bleiben in den standardisierten Residuen keine signifikanten seriellen Korrelationen und keine bedingte Heteroskedastizität: die p-Werte von Q(12) und Q(24) sind 0,45 und 0,24 für die Residuen und 0,36 und 0,33 für die Quadrate.
- Ein GARCH-M schreibt serielle Korrelationen in die Rendite, weil sie aus der seriellen Abhängigkeit der bedingten Varianz entstehen; die Existenz einer Risikoprämie ist damit ein weiterer Grund für serielle Korrelation historischer Aktienrenditen.
- Nelsons Mittelgleichung für die täglichen CRSP-Überschussrenditen enthält ein AR(1) mit geschätztem phi 1 gleich 0,205 und Standardfehler 0,012, um mögliche serielle Korrelation aufzufangen.
- Das AR(1) der monatlichen IBM-Logrenditen im EGARCH hat den Koeffizienten 0,092 bei einem Mittel von 0,0105.
- Eine Zeitreihe ist ein Long-Memory-Prozess, wenn ihre Autokorrelationsfunktion mit wachsendem Lag hyperbolisch statt exponentiell fällt.
- Die Autokorrelationsfunktion der quadrierten oder absoluten Renditen fällt oft langsam, auch wenn die Renditereihe selbst keine serielle Korrelation aufweist (Ding, Granger und Engle, 1993).
- Die Stichproben-ACF der täglichen absoluten Logrenditen von IBM und dem S&P 500, 3. Juli 1962 bis 31. Dezember 2003, ist positiv, mäßig groß und fällt langsam.
- Nelson (1991) setzt in der Mittelgleichung ein AR(1) ein, um mögliche serielle Korrelation der Überschussrenditen zu berücksichtigen.
- Im SV-Modell mit m = 1 ist corr(a²_t, a²_{t−i}) = [exp(σ²_h α₁^i) − 1] / [3 exp(σ²_h) − 1].
- Der Median der Schätzung des fraktionalen Differenzparameters d für den Logarithmus quadrierter Tagesrenditen von S&P-500-Unternehmen liegt bei etwa 0,38 (Bollerslev und Jubinski, 1999; Ray und Tsay, 2000).
- Im AR(1)–EGARCH(1,1) der IBM-Monatsrenditen 1926 bis 1997 zeigen die Ljung-Box-Statistiken der standardisierten Residuen keine serielle Korrelation: Q(10) = 6,31 (p = 0,71) und Q(20) = 21,4 (p = 0,32).
- Eine schwach stationäre, rein stochastische Zeitreihe lässt sich nach Wold als lineare Funktion unkorrelierter Schocks schreiben. Bei stationären Volatilitätsreihen sind diese Schocks unkorreliert, aber abhängig.
- Die Stichproben-ACF der standardisierten Residuen des bilinearen CRSP-Modells zeigt keine signifikante serielle Korrelation, die quadrierte Reihe dagegen schon.
- Die partielle Autokorrelation der monatlichen CRSP-Equal-Weight-Renditen ist an den Lags 1 und 3 signifikant. Die quadrierten AR(3)-Residuen hängen möglicherweise von den Lags 1, 3 und 8 ab.
- Die differenzierte Arbeitslosenquote wird mit einem saisonalen ARIMA modelliert, weil die Autokorrelation der Niveaureihe langsam fällt. Q(12) = 12,3 hat p = 0,056, Q(24) = 25,5 hat p = 0,11.
- Die standardisierten Residuen des TAR der Arbeitslosenänderung zeigen nur geringe serielle Korrelation bei Lag 12.
- Die quadrierten Residuen des AR(3)–ARCH(3) haben Q(10) = 19,78 mit p = 0,031. Ein AR(1)–GARCH(1,1) passt nach weiterer Prüfung gut.
- Unter der Null der Linearität sollen Residuen eines korrekt spezifizierten linearen Modells unabhängig sein; eine Verletzung dieser Unabhängigkeit zeigt an, dass das Modell einschließlich der Linearitätsannahme unzureichend ist.
- Bei realen Finanzzeitreihen entfernt zuerst ein AR-Modell die serielle Korrelation, und die Nichtlinearitätstests werden auf die Residuen angewandt.
- Die Ljung-Box-Statistiken in Tabelle 4.2 bestätigen, dass vor diesen Tests in den Residuen keine serielle Korrelation mehr vorliegt.
- Der TAR-F-Test prüft, dass die standardisierten Vorhersageresiduen der geordneten Autoregression unter der linearen Null nicht mit den Regressoren korrelieren.
- Der BDS-Test spricht an, sobald die k-Historien vom iid-Muster C_k(δ) = [C_1(δ)]^k abweichen, also auch bei serieller Abhängigkeit, die nicht nur ein Moment zweiter Ordnung ist.
- Nichtsynchroner Handel induziert bei μ ungleich null negative Autokorrelationen der beobachteten Rendite; die Lag-1-Autokorrelation ist ρ1 = −(1−π) π μ² / [(1−π) σ² + 2π μ²], und die Autokovarianz bei Lag j ist −μ² π^j.
- Für ein Portfolio wird aus der durch nichtsynchronen Handel erzeugten Lag-1-Kreuzkorrelation eine Lag-1-Autokorrelation der Portfoliorendite.
- Der Bid-Ask-Bounce erzeugt in den beobachteten Preisänderungen eine negative Lag-1-Korrelation und keine Korrelation darüber hinaus: ohne Änderung des fundamentalen Werts ist ρ1 = −0,5 und ρ_j = 0 für j > 1.
- Mit fundamentalem Random Walk sinkt der Betrag auf ρ1 = (−S²/4) / (S²/2 + σ²), das Vorzeichen bleibt negativ, solange der Spread positiv ist.
- Aufeinanderfolgende Preisanstiege oder -rückgänge sind bei den IBM-Intraday-Trades vom 1. November 1990 bis 31. Januar 1991 selten: 441 von 59.837 Fällen, also 0,74 Prozent, und 410 von 59.837 Fällen, also 0,69 Prozent.
- Die Richtungsreihe der IBM-Intraday-Trades hat eine einzige Autokorrelation von −0,389 bei Lag 1 und bestätigt damit die Preisumkehr von Trade zu Trade.
- Die Koeffizienten der verzögerten Preisänderungen im Ordered Probit sind negativ und hoch signifikant und zeigen dieselbe Umkehr.
- Aufeinanderfolgende gleichgerichtete Bewegungen sind selten; die Zerlegung setzt die Wahrscheinlichkeit einer Fortsetzung des Anstiegs auf 0,085 und die einer Umkehr nach einem Rückgang auf 0,904.
- Die bedingte Wahrscheinlichkeit einer Preisänderung steigt von 0,258 auf 0,476, wenn der vorherige Trade bereits eine Preisänderung hatte, sodass Änderungen in Clustern auftreten.
- Das ACD-Modell ist gerade für die serielle Abhängigkeit der bereinigten Dauern gebaut; in der Simulation mit 500 Beobachtungen ist diese Abhängigkeit in der Autokorrelationsfunktion sichtbar.
- Schwache Evidenz spricht dafür, dass auf eine große Preisänderung mit höherer Wahrscheinlichkeit wieder eine große folgt: die Wahrscheinlichkeit eines Anstiegs um genau einen Tick fällt von 0,827 über 0,709 auf 0,556, wenn die vorherige Größe 1, 2 beziehungsweise 3 Ticks war.
- Aufeinanderfolgende Preisänderungen kehren sich typischerweise um; im PCD-Modell hängt der Mittelwert der Richtung mit einem negativen Koeffizienten von Di−1 ab.
- Für IBM am 21. November 1990 gilt µi = 0,049 − 0,840 Di−1 − 0,004 ln(Δti), Standardabweichungen 0,129, 0,132 und 0,082; der negative Koeffizient von Di−1 ist hochsignifikant und zeigt die Preisumkehr.
- In dieser Eintagesstichprobe zeigt die Dauerngleichung ln(Δti) = 4,023 + 0,032 ln(Δti−1) − 0,025 Si−1 + 1,403 ϵi keine dynamische Abhängigkeit der Zeitdauer.
- Über die 63 Handelstage bis 31. Januar 1991 liegt der Koeffizient von ln(Δti−1) zwischen 0,04 und 0,1 und ist klein, aber signifikant.
- Die adjustierten IBM-Dauern sind seriell korreliert; nach dem WACD(1,1) haben die standardisierten Innovationen mit Q(10) = 4,96 und Q(20) = 10,75 und ihre Quadrate mit Q(10) = 6,20 und Q(20) = 11,16 keine signifikante serielle Abhängigkeit.
- Beim verfeinerten Schwellen-WACD gelten für êi Q(10) = 5,91 (p = 0,82) und Q(20) = 16,04 (p = 0,71) sowie für die Quadrate Q(10) = 5,35 (p = 0,87) und Q(20) = 15,20 (p = 0,76).
- Unter der geometrischen Brownschen Bewegung sind die stetig verzinsten Intervallrenditen rt nicht seriell korreliert.
- Die IBM-Logrenditen 1998 sind seriell unkorreliert, Q(10) = 4,9 ist gegenüber Chi-Quadrat mit 10 Freiheitsgraden hoch insignifikant.
- Die Cisco-Logrenditen 2007 sind seriell unkorreliert, Q(12) = 12,30 mit p-Wert 0,42.
- Serielle Korrelation der Renditen oder eine Abweichung von der geometrischen Brownschen Bewegung verlangt andere Schätzer für Drift und Volatilität als σ̂ = sr/√Δ und µ̂ = r̄/Δ + σ̂²/2.
- Die Zuwächse eines Wiener-Prozesses über nicht überlappende Intervalle sind unabhängig; bedingt auf die Gegenwart ist die Vergangenheit für die Zukunft irrelevant.
- Die Herleitung der Mehrperioden-Varianz unter RiskMetrics nutzt, dass der bedingte Erwartungswert von ε zum Quadrat von t+i minus 1 minus 1 gegeben Ft für i mindestens 2 gleich null ist.
- Weil die meisten Asset-Renditen seriell unkorreliert oder nur schwach seriell korreliert sind, setzt der Extremwert-VaR die Beziehung 1 minus p* = [Wahrscheinlichkeit, dass die Einzelrendite höchstens das Blockquantil ist] hoch n an.
- Berman (1964) erhält dieselbe Extremwert-Grenzverteilung für stationäre normale Folgen, sofern die Summe der quadrierten Autokorrelationen endlich ist.
- Die Umrechnung vom Quantil des Blockmaximums auf die Einzelrendite nutzt, dass die meisten Asset-Renditen seriell unkorreliert oder nur schwach seriell korreliert sind.
- Diese Unabhängigkeit täglicher Logrenditen wird oft statistisch verworfen, deshalb kann der klassische Extremwert-VaR unzureichend sein.
- In einem passenden zweidimensionalen Poisson-Modell sollen die Dauern zwischen Überschreitungen unabhängig standard-exponentialverteilt sein und die transformierten Exzesse keine seriellen Korrelationen haben.
- Extremereignisse treten wegen der seriellen Abhängigkeit in Clustern auf; große positive und große negative Renditen folgen oft auf ein Nachrichtenereignis.
- Klingt die serielle Abhängigkeit einer stationären Reihe schnell ab, sind xi und xi plus ℓ bei hinreichend großem ℓ im Wesentlichen unabhängig, die langreichweitige Abhängigkeit verschwindet also schnell.
- Für ξ ungleich 0 ändert der Extremalindex Lage und Skala der Grenzverteilung des Maximums, der Formparameter ξ bleibt derselbe wie bei der iid-Folge.
- Die Randverteilung der Blockmaxima hängt von der Blockgröße und von der Stärke der seriellen Abhängigkeit ab und ist nicht die Randverteilung F(x) der Einzelwerte.
- Die Innovation at eines VAR ist seriell unkorreliert, mit Mittel 0, und unkorreliert mit allen vergangenen rt minus ℓ für ℓ größer als 0.
- Die Portmanteau-Tests bestätigen serielle Abhängigkeit in den bivariaten Monatsrenditen von IBM und S&P 500 zum Niveau 5 Prozent: die p-Werte von Q2(1), Q2(5) und Q2(10) sind 0,044, 0,001 und 0,002.
- Die dynamische lineare Abhängigkeit zwischen den beiden Renditereihen ist schwach; M(2) gleich 13,41 ist zum Niveau 1 Prozent nur marginal, der kritische Wert bei 4 Freiheitsgraden ist 13,3.
- Die Schocks {at} eines VMA haben keine seriellen Korrelationen. Deshalb ist die Kreuzkovarianz eines VMA(q) ab Lag q plus 1 gleich 0.
- Die Residuen des vereinfachten VMA(5) bestehen den Portmanteau-Test zum Niveau 5 Prozent: Q2(4) gleich 16,00 mit p-Wert 0,10 und Q2(8) gleich 29,46 mit p-Wert 0,291, bei 10 und 26 Freiheitsgraden.
- In der Faktorenanalyse wird häufig angenommen, dass die Faktoren und damit der Renditevektor rt seriell unkorreliert sind.
- Sind die beobachteten Renditen seriell abhängig, können die Modelle aus Kapitel 8 diese serielle Abhängigkeit entfernen, bevor das Faktormodell geschätzt wird.
- Ist serielle Korrelation vorhanden, lässt sich die lineare dynamische Abhängigkeit mit einem parametrischen Modell entfernen und die Faktorenanalyse auf die Residuen anwenden. Zum Prüfen dienen multivariate Portmanteau-Statistiken. Bei Befund kann ein VARMA die Abhängigkeit beseitigen.
- Bei vielen Renditereihen liegt die Korrelationsmatrix der Residuen eines linearen Modells sehr nahe an der der Originaldaten, sodass die dynamische Abhängigkeit die Faktorenanalyse kaum verändert.
- Für die fünf monatlichen Logrenditen von IBM, Hewlett-Packard, Intel, J.P. Morgan Chase und Bank of America, Januar 1990 bis Dezember 2008, sind Q5(1) gleich 39,99, Q5(5) gleich 160,60 und Q5(10) gleich 293,04, mit p-Werten 0,029, 0,017 und 0,032 gegen Chi-Quadrat-Verteilungen mit 25, 125 und 250 Freiheitsgraden. Die serielle Abhängigkeit ist gering und auf dem 1-Prozent-Niveau nicht signifikant. Die Faktorenanalyse ignoriert sie der Einfachheit halber.
- Die monatlichen Logrenditen der US-Anleihenindizes mit Laufzeiten von 1 bis 30 Jahren haben serielle Abhängigkeit. Ein VARMA(2,1) ändert die gleichzeitige Korrelationsmatrix trotzdem kaum, deshalb wird die Faktorenanalyse direkt auf die Renditen angewendet.
- Die monatlichen einfachen Renditen von Pfizer und Merck, Januar 1965 bis Dezember 2008, 528 Beobachtungen, haben keine signifikante serielle Korrelation. Q(10) beträgt 10,48 mit p gleich 0,40 und 11,42 mit p gleich 0,33.
- Die standardisierten Residuen des Constant-Correlation-GARCH(1,1) für die monatlichen Logrenditen von IBM und dem S&P 500 haben auf dem 5-Prozent-Niveau keine seriellen Korrelationen. Q2(4) ist 16,77 mit p gleich 0,21 und Q2(8) ist 32,40 mit p gleich 0,30.
- Die Ljung-Box-Tests der standardisierten Residuen des univariaten GARCH(1,1) für Hang Seng und für den Nikkei 225 zeigen keine verbliebene serielle Abhängigkeit.
- Die Aktienrenditen im Beispiel von Euro, Yen, IBM und Dell haben serielle Korrelationen von geringer Größe. Die multivariate Ljung-Box-Statistik ist Q(3) gleich 59,12 mit p gleich 0,13 und Q(5) gleich 106,44 mit p gleich 0,03. Deshalb wird der Einfachheit halber nur das Stichprobenmittel als Mittelgleichung verwendet.
- Bei den Tageslogrenditen von S&P 500, Cisco und Intel, 1991 bis 1999, hängt die Indexrendite nicht von den vergangenen Renditen der beiden Unternehmen ab. Cisco und Intel hängen dagegen von vergangenen Indexrenditen ab. Renditen großer Einzeltitel werden vom vergangenen Marktverhalten beeinflusst, der Markt umgekehrt nicht signifikant von den einzelnen Unternehmen.
- Cisco hat eigene serielle Korrelation und hängt an den Lags 2 und 5 vom S&P 500 ab. Intel hängt an den Lags 1 und 5 vom S&P 500 ab. Q3(1) gleich 26,20, Q3(4) gleich 79,73 und Q3(8) gleich 123,68 sind hochsignifikant.
- Im Cholesky-Modell der monatlichen IBM- und S&P-500-Renditen zeigt der Koeffizient 0,9915 von q21,t eine starke dynamische Abhängigkeit in der Korrelationsgröße. Die standardisierten Residuen dieses Modells und die des logistischen Korrelationsmodells haben auf dem 5-Prozent-Niveau keine verbliebene serielle Korrelation.
- Im lokalen Trendmodell ist die Messfehlerfolge et nicht seriell korreliert. Die serielle Abhängigkeit von yt wird vollständig vom latenten Niveau μt getragen.
- Die erste Differenz wt gleich (1 minus B) yt hat nur eine von null verschiedene Autokovarianz, und zwar bei Lag 1, gleich minus σ²e. Ab Lag 2 ist die Autokovarianz null, also ist wt ein MA(1).
- Der Ein-Schritt-Prognosefehler vt ist mit allen früheren yt, j kleiner t, unkorreliert.
- Die standardisierten Residuen des Faktor-Volatilitätsmodells für IBM und den S&P 500 zeigen keine serielle Korrelation: Q2(4) gleich 15,37 bei einem p-Wert von 0,29 und Q2(8) gleich 34,24 bei einem p-Wert von 0,23.
- Die Alcoa-ARIMA-Residuen haben Q(12) gleich 12,4 bei einem p-Wert von 0,33 und damit keine signifikante serielle Korrelation.
- Die Ein-Schritt-Prognosefehler des Kalman-Filters sind unter Normalität gegenseitig unabhängig, auch wenn die beobachtete Reihe yt seriell abhängig ist.
- Für die standardisierten Prognosefehler der Alcoa-Log-RV ist Q(25) gleich 23,37 bei einem p-Wert von 0,56, also ohne signifikante serielle Korrelation.
- Die LM-Statistik auf verbleibende ARCH-Abhängigkeit derselben Fehler ist über 25 Lags gleich 18,48 bei einem p-Wert von 0,82.
- Im allgemeinen Zustandsraummodell sind die Ein-Schritt-Prognosefehler vt untereinander unabhängig, und vt bis vT ist unabhängig von Ft minus 1.
- Die serielle Abhängigkeit eines ARMA steckt in den Koeffizienten φ und θ. Harveys Zustandsraumform setzt keine zusätzlichen seriell korrelierten Messfehler an, Ht ist null.
- Für die Prognose werden künftige Beobachtungen wie fehlende Werte behandelt. Dabei bleibt die serielle Struktur in der Fortschreibung des Zustands erhalten: st plus j plus 1 gegeben t gleich dt plus j plus Tt plus j mal st plus j gegeben t.
- Der Posteriormittelwert α1 = 0,837 bestätigt starke serielle Abhängigkeit der Logvolatilität der monatlichen S&P-500-Renditen.
- Im bivariaten Modell ist {at} eine Folge seriell unkorrelierter gaußscher Zufallsvektoren mit Mittel null und bedingter Kovarianzmatrix Σt.
- Weil die Volatilität {zt} seriell korreliert ist, ist die gemeinsame Ziehung effizienter.
- Die Quadrate der standardisierten GARCH-Residuen haben Q(12) = 6,14 (p 0,91), die Residuen selbst Q(12) = 10,04 (p 0,61).
- Im Markov-Switching-GARCH-M (12.55) folgt aus der Abhängigkeit der Rendite von der Volatilität, dass die Rendite seriell korreliert ist und das Modell eine gewisse Vorhersagbarkeit besitzt.
- Weil die künftigen Zustände unbekannt sind, ist jede Prognose eine Mischung über Zustandskonfigurationen, und die Punktprognose künftiger Renditen hat oft hohe Unsicherheit.
- Die Ljung-Box-Statistiken der standardisierten Residuen und ihrer Quadrate des GE-GARCH-M von 1926 bis 1999 zeigen keine Modellunzulänglichkeit an.

## Funktionsweise

- Der Lag-ℓ-Autokorrelationskoeffizient ist unter schwacher Stationarität ρℓ = Cov(rt, rt−ℓ) / Var(rt) = γℓ / γ0, mit ρ0 = 1, ρℓ = ρ−ℓ und −1 ≤ ρℓ ≤ 1.
- Das erste MCMC-Anwendungsmodell ist eine Regression mit seriell korrelierten Fehlern: zt = φ zt−1 + at, at unabhängig und identisch normal mit Mittel null und Varianz σ².
- Für die Zinsänderungen wird ein AR(2) der Fehler angesetzt: zt = φ1 zt−1 + φ2 zt−2 + at.
- Die klassische Schätzung lautet zt = 0,183 zt−1 − 0,036 zt−2 + at mit σ̂a = 0,068.

## Voraussetzungen

- Der Zentrale Grenzwertsatz gilt für eine Stichprobe, deren Beobachtungen aus derselben Elternpopulation stammen, unabhängig sind und bei der Mittelwert und Standardabweichung der Elternpopulation endlich sind.
- Die traditionelle statistische Faktorenanalyse setzt voraus, dass die Daten keine serielle Korrelation haben. Finanzdaten mit Frequenz von einer Woche oder höher verletzen das oft. Bei niedrigeren Frequenzen, etwa monatlichen Aktien- oder Indexrenditen, ist die Annahme häufig vertretbar.

## Anwendung im Trading

- Tests auf Autokorrelation null werden benutzt, um die Annahme effizienter Märkte zu prüfen, nach der eine Assetrendite nicht prognostizierbar sein soll.
- Bid-Ask-Bounce und nichtsynchrone Umsätze können besonders in Hochfrequenzdaten serielle Korrelation in die beobachtete Rendite einführen, auch wenn die ökonomische Rendite keine hat.

## Regeln und Kriterien

- Oft lässt sich die ADF-Null erst mit Lag k gleich 1 verwerfen und nicht mit k gleich 0, weil die Preisänderungen häufig serielle Korrelation haben.
- Ist {rt} iid mit endlichem zweiten Moment, ist ρ̂ℓ für jedes feste positive ℓ asymptotisch normal mit Mittelwert null und Varianz 1/T. Der Test H0: ρ1 = 0 verwendet Wurzel(T) mal ρ̂1 und lehnt ab, wenn der p-Wert klein ist, etwa unter 0,05.
- Die Bedingung D(un) begrenzt die langreichweitige Abhängigkeit: Ereignisse auf Indexmengen, die mindestens ℓn Zeitpunkte auseinanderliegen, werden mit wachsendem n asymptotisch unabhängig, sofern ℓn/n gegen 0 geht.
- Unter Unabhängigkeit dürfen die Reihen zti und wti nach Bereinigung um die erklärenden Variablen keine seriellen Korrelationen haben.
- Qk(m) prüft gemeinsam, dass die ersten m Kreuzkorrelationsmatrizen null sind, also dass weder Auto- noch Kreuzkorrelationen vorliegen.
- Für die Residuen eines VAR(p) werden mit Qk(m) die Annahmen keiner seriellen und keiner Kreuzkorrelation geprüft. Die asymptotische Chi-Quadrat-Verteilung hat k zum Quadrat mal m minus g Freiheitsgrade, g gleich der Zahl der geschätzten AR-Parameter.

## Risiken und Grenzen


## Beispiele

- Die Erklärung passt zu BR, HG und TU, weil ihre Rollrenditen nach Tabelle 5.1 betragsmäßig größer sind als ihre Spot-Renditen.
- Für C findet der Text den Grund nicht, obwohl C den größten Betrag der Rollrendite im Vergleich zur durchschnittlichen Spot-Rendite hat.
- Für TU ist die Korrelation der 250-Tage-Rendite mit der folgenden 25-Tage-Rendite 0,27 bei einem p-Wert von 0,02, während der Hurst-Exponent 0,44 beträgt und der Variance-Ratio-Test den Random Walk nicht verwirft.
- Beispiel 1.1 simuliert eine Renditereihe mit derselben Kurtosis wie die TU-Futures-Reihe, aber ohne serielle Autokorrelationen, und erzeugt in 12 Prozent der Zufallsziehungen dieselben Renditen wie die TU-Momentum-Strategie.
- Die monatlichen IBM-Aktienrenditen von Januar 1926 bis Dezember 2008 haben keine signifikante serielle Korrelation und liegen nahe an weißem Rauschen; die gemeinsamen Ljung-Box-Tests bestätigen das.
- Die monatlichen Renditen des wertgewichteten CRSP-Index sind seriell korreliert, mit p-Werten der Ljung-Box-Statistiken unter 0,0001, und die serielle Abhängigkeit ist stärker als bei der IBM-Einzelaktie.
- In der R-Demonstration der IBM-Reihe mit 996 Beobachtungen lautet die Ljung-Box-Statistik bei Lag 5 für die einfachen Renditen 3,3682 mit p-Wert 0,6434 und für die Logrenditen 3,5236 mit p-Wert 0,6198.
- Beim AR(3) des wertgewichteten Index wird die Null keiner residuellen seriellen Korrelation in den ersten 12 Lags auf dem 5-Prozent-Niveau knapp nicht verworfen: Q(12) gleich 16,35, p-Wert 0,060 bei 9 Freiheitsgraden.
- Nach Entfernen des auf dem 5-Prozent-Niveau nicht signifikanten Lag-2-Koeffizienten ist Q(12) gleich 16,83 mit p-Wert 0,078 bei 10 Freiheitsgraden; das verfeinerte Modell erfasst die dynamische lineare Abhängigkeit der Daten angemessen.
- Die monatlichen Logrenditen von 3M von Februar 1946 bis Dezember 2008, 755 Werte, haben auf dem 1-Prozent-Niveau keine signifikante serielle Korrelation und werden per EACF als weißes Rauschen eingeordnet.
- Das MA(9) des gleichgewichteten Index modelliert die lineare dynamische Abhängigkeit nur knapp ausreichend: Q(12) gleich 17,5 beziehungsweise 17,6, mit p-Werten 0,041 und 0,040 bei 9 Freiheitsgraden für bedingte und exakte Likelihood.
- Die Logreihe des vierteljährlichen US-BIP von 1947.I bis 2008.IV hat hohe serielle Stichprobenkorrelationen.
- Die 3M-Logrenditen von Februar 1946 bis Dezember 2008 haben keine signifikante serielle Korrelation und werden als rt gleich 0,0103 plus weißes Rauschen modelliert.
- Bei den Loggewinnen von Johnson & Johnson ist die Autokorrelation der ersten Differenz an Vielfachen von 4 stark; nach zusätzlicher saisonaler Differenz bleibt eine signifikant negative Autokorrelation bei Lag 1 und eine marginal negative bei Lag 4.
- Die Januar-Dummy entfernt bei den monatlichen Decile-1-Renditen von 1970 bis 2008 die seriellen Korrelationen an den Lags 12, 24 und 36 weitgehend.
- Das IGARCH(1,1) ohne Drift für die IBM-Tageslogrenditen wird von den Q-Statistiken verworfen; Q(10) der quadrierten standardisierten Residuen beträgt 56,19.
- Beim homogenen Modell für die negativen IBM-Renditen und Schwelle 2,5 Prozent haben die Dauergrößen zti und die Exzessgrößen wti signifikante serielle Korrelationen, und der QQ-Plot von zti zeigt eine Abweichung.
- Das homogene Poisson-Modell der IBM-Logrenditen bei Schwelle 2,5 Prozent zeigt in zti und wti signifikante serielle Korrelationen; im inhomogenen Modell liegen alle Autokorrelationen innerhalb der Grenzen von zwei Standardfehlern.
- Die täglichen IBM-Logrenditen sind nur schwach seriell abhängig; deshalb wird für den Extremalindex die Blockgröße k gleich 10 verwendet.
- Die Residuen des vereinfachten VAR(5) mit sechs AR-Parametern haben Q2(4) gleich 16,64 und Q2(8) gleich 31,55, p-Werte 0,083 und 0,208, und bestehen die Prüfung zum Niveau 5 Prozent.
- Für die fünf Anleiheindizes ist Q5(5) gleich 1065,63 hoch signifikant gegen Chi-Quadrat mit 125 Freiheitsgraden.
- Die Residuen des VARMA(2,1) für die logarithmierten US-Zinssätze zeigen kleine serielle und Kreuzkorrelationen bei den Lags 7 und 11 sowie einige Ausreißer.
- Die Residuenplots des VAR(1) für IBM und S&P 500 zeigen Cluster von Ausreißern. Die beiden horizontalen Linien sind die Grenzen von zwei Standardfehlern.
- Die Durbin-Watson-Statistik der Residuen des festen GM-Marktmodells beträgt 2,0290.
- Die Ljung-Box-Statistik dieser Residuen beträgt 24,2132 bei einem p-Wert von 0,3362.
- Nach diesen Residuendiagnosen erscheint das Modell für die monatlichen GM-Überschussrenditen von Januar 1990 bis Dezember 2003 angemessen.
- Die Gibbs-Posteriormittel sind φ1 = 0,184 und φ2 = −0,036 bei Standardfehlern 0,019 und 0,021.
- Die residuelle Autokorrelationsfunktion ist an den Lags 4 und 6 nur marginal signifikant.
- Das AR(3) der 600 Dreijahresänderungen hat die Ljung-Box-Statistik Q(12) = 11,4, insignifikant auf dem 5-Prozent-Niveau.
- Bei großem n = 2466 und einfachem Modell liegen die Posteriormittel nahe an der klassischen Schätzung.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]
- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 476–495 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-026-p476-p495|S. 476–495]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 14–33 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-002-p014-p033|S. 14–33]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 52–71 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-004-p052-p071|S. 52–71]]
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
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 685–704 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-037-p685-p704|S. 685–704]]

## Verwandte Themen
