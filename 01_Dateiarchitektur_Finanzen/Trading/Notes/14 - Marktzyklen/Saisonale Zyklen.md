---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/14 - Marktzyklen/14 - Marktzyklen|14 - Marktzyklen]]"
weitere_hauptthemen: []
unterthema: "Zeitzyklen"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Saisonale Zyklen


## Kurzdefinition

- Eine Finanzzeitreihe mit zyklischem oder periodischem Verhalten heißt saisonale Zeitreihe; vierteljährliche Gewinne je Aktie sind ein Beispiel, und das Muster von Johnson & Johnson wiederholt sich jedes Jahr, die Periode ist also 4.
- Bei Monatsdaten, etwa den monatlichen Umsätzen von Wal-Mart, ist die Periode 12.

## Kernaussagen

- Die meisten Aktien zeigen unter normalen Umständen, also ohne Nachricht, kurzfristig Mean Reversion, obwohl sie langfristig geometrischen Random Walks folgen. Der Text nennt das saisonale Mean Reversion.
- Diese Umkehr sitzt im Intraday-Fenster und ist mit den üblichen Stationaritäts- oder Kointegrationstests schwer zu erkennen, kann aber sehr profitabel sein.
- Preisreihen ohne Mean Reversion auf Tagesbars können in bestimmten Perioden stark mean-reverten. Das ist Saisonalität auf kurzer Zeitskala.
- Das saisonale Muster der monatlichen einfachen Rendite von Decile 1 geht hauptsächlich auf den Januar-Effekt zurück: eine Januar-Dummy beseitigt die seriellen Restkorrelationen auf den Lags 12, 24 und 36 weitgehend.
- Ein saisonales Modell der Ordnung (1,0,0) mit saisonaler Ordnung (1,0,1) und Periode 12 schätzt mit Mittel ar1 gleich 0,1769, sar1 gleich 0,9882, sma1 gleich minus 0,9144 und Intercept 0,0118; sigma quadrat ist 0,004717, die Log-Likelihood 584,07 und das AIC minus 1158,14.
- Ohne Mittel lauten dieselben Koeffizienten ar1 0,1787, sar1 0,9886 und sma1 minus 0,9127, sigma quadrat 0,00472, Log-Likelihood 583,68, AIC minus 1159,36.
- Die bedingte Maximum Likelihood in SCA liefert für diese Reihe MA der Lag 12 gleich 0,7388, AR(1) gleich 0,1765 und saisonales AR gleich 0,8698, bei 455 Beobachtungen und einem Bestimmtheitsmaß von 0,199.
- Die exakte Maximum Likelihood hebt diese Werte auf 0,9968, 0,1884 und 0,9505 und das Bestimmtheitsmaß auf 0,328, bei einem residualen Standardfehler von 0,0631807.
- Bei saisonalem Verhalten kann serielle Restabhängigkeit auf höheren Lags liegen, deshalb reicht Durbin-Watson nicht und es wird die Ljung-Box-Statistik empfohlen.
- Der Sommereffekt der Aktienvolatilität wird mit der Indikatorvariable u_t gemessen, die in Juni, Juli und August 1 und sonst 0 ist. Ob die tägliche Volatilität im Sommer niedriger ist und um wie viel, hat praktische Folgen für die Bewertung von Aktienoptionen.
- Für die monatlichen IBM-Logrenditen von Januar 1926 bis Dezember 1999 ist der Sommereffekt auf dem 1-Prozent-Niveau signifikant, p = 0,0067. Das negative Vorzeichen bestätigt eine niedrigere Volatilität im Sommer.
- Das verfeinerte Modell lautet σ²_t = 4,539 + 0,113 a²_{t−1} + 0,816 σ²_{t−1} − 5,154 u_t. Im Sommer wird die Konstante 4,539 − 5,154 = −0,615. Das ist kontraintuitiv. Die Standardfehler der Schätzungen 4,539 und 5,154 sind aber relativ groß, sodass die Differenz nicht notwendig von null verschieden ist.
- Mit der Nebenbedingung einer Sommerkonstante von null gilt σ²_t = 0,114 a²_{t−1} + 0,811 σ²_{t−1} + 4,552(1−u_t).
- Auf Basis der Mediane von a²_t und σ²_t im Jahr 1999, 29,4 und 75,1, liefert dieses Modell 64,3 im Sommer und 68,8 in den übrigen Monaten. Das Verhältnis etwa 93 Prozent entspricht 7 Prozent geringerer Volatilität der monatlichen IBM-Logrendite im Sommer.
- Die zusätzlichen Koeffizienten, die auch Steigung und GARCH-Gewicht im Sommer ändern, waren auf dem 10-Prozent-Niveau nicht signifikant. Übrig bleibt allein die Verschiebung der Konstanten.
- Obwohl die US-Arbeitslosenquote saisonbereinigt ist, sind im ARIMA der ersten Differenz die saisonalen AR- und MA-Koeffizienten hoch signifikant, Standardfehler 0,049 und 0,035. Die Güte der Saisonbereinigung verdient weitere Prüfung.
- Das Modell enthält die saisonalen Faktoren (1 − 0,51 B¹²) auf der AR-Seite und (1 − 0,82 B¹²) auf der MA-Seite.
- Im TAR der Arbeitslosenänderung erscheint in beiden Regimes ein Lag-12-Term: −0,180 y_{t−12} unterhalb der Schwelle 0,1 und −0,127 y_{t−12} oberhalb.
- Die standardisierten TAR-Residuen zeigen nur eine geringe serielle Korrelation bei Lag 12.
- Obwohl die vierteljährliche US-Arbeitslosenquote saisonbereinigt ist, bleibt das lineare Modell (1 − 0,31 B⁴)(1 − 0,65 B) Δx_t = (1 − 0,78 B⁴) a_t saisonal.
- Die Standardfehler der Koeffizienten 0,31, 0,65 und 0,78 sind 0,11, 0,06 und 0,07, und die Residualvarianz beträgt 0,090.
- Das saisonale Modell zeigt, dass das verwendete Saisonbereinigungsverfahren die Saisonalität nicht erfolgreich entfernt hat.
- Dasselbe Modell dient als Benchmark für den Prognosevergleich mit dem TAR- und dem Markov-Switching-Modell.
- Das univariate strukturelle Komponentenmodell zerlegt yt in nicht beobachteten Trend μt, Saison γt, Zyklus und irreguläre Komponente et.
- Die Saison erfüllt (1 plus B plus bis plus B hoch s minus 1) γt gleich einem normalen Schock mit Varianz σ²ω. s ist die Zahl der Saisons im Jahr, also die Periode der Saisonalität.
- Ist die Varianz dieses Saisonschocks gleich 0, ist das Saisonmuster deterministisch.
- Der Zyklus ist eine gedämpfte Drehung mit Dämpfungsfaktor δ im Intervall (0, 1] und Frequenz λc gleich 2π geteilt durch q, q die Periode. Bei δ gleich 1 wird der Zyklus eine deterministische Sinus-Cosinus-Welle.
- Die beiden Zyklusinnovationen sind gemeinsam normal mit Mittel null und Kovarianz σ²ε mal (1 minus δ²) mal der 2-mal-2-Einheitsmatrix. Die beiden Startwerte sind unabhängig normal mit Varianz σ²ε.
- GetSsfStsm lässt bis zu zehn Zykluskomponenten zu, von Cycle0 bis Cycle9, jeweils mit σε, λc und δ. Für die Saison gibt es die Varianten seasonalDummy, seasonalTrig und SeasonalHS, jeweils mit σ und s.
- Seit 1970 waren die durchschnittlichen Überschussrenditen gegenüber Cash über eine breite Palette von Aktienmärkten zwischen Mai und Oktober negativ.
- Im Update für 1970 bis 2005 wären Anleger in den USA, in Großbritannien, in Deutschland und in Japan im Schnitt besser gefahren, von Mai bis Oktober Cash zu halten und nur von November bis April in Aktien investiert zu sein.
- Jacobsen und Visaltanachoti (2006) finden mit US-Daten von 1927 bis 2005 in 12 von 17 Sektoren einen statistisch signifikanten Renditeunterschied zwischen Sommer und Winter.
- Konsum- und Lebensmittelsektoren schlagen den Markt in den Sommermonaten. Gebrauchsgüter, Chemie, Bau und Maschinen schlagen ihn in den Wintermonaten. Die Kurzfassung nennt zusätzlich Basiskonsumgüter neben Lebensmitteln als Sommergewinner.
- Eine Rotationsstrategie, die diesen Sommer-Winter-Unterschied ausnutzt, würde den Markt deutlich schlagen. Die meisten Anleger stellen solche saisonalen Befunde auf eine Stufe mit dem Lesen von Hühnerinnereien.

## Funktionsweise

- Saisonales Differenzieren einer Reihe mit Periode s bildet yt minus y(t−s), also (1 minus B hoch s) yt; die gewöhnliche Differenz yt minus yt−1 heißt reguläres Differenzieren.
- Das Airline-Modell lautet (1 minus B hoch s) mal (1 minus B) mal xt gleich (1 minus θ B) mal (1 minus Θ B hoch s) mal at, mit Betrag von θ und Betrag von Θ jeweils kleiner als 1; der autoregressive Teil besteht nur aus regulärer und saisonaler Differenz, der Moving-Average-Teil hat zwei Parameter.
- Die Autokorrelation der so differenzierten Reihe ist an Lag 1 gleich minus θ geteilt durch (1 plus θ zum Quadrat), an Lag s gleich minus Θ geteilt durch (1 plus Θ zum Quadrat), und an s minus 1 sowie s plus 1 gleich dem Produkt dieser beiden Werte; alle anderen positiven Lags sind null.
- Bei Quartalsdaten ist diese Autokorrelation nur an den Lags 1, 3, 4 und 5 von null verschieden.
- Die Autokorrelation an s minus 1 und s plus 1 ist die Wechselwirkung von Lag-1- und Lag-s-Abhängigkeit; die Dynamik der regulären und der saisonalen Komponente ist näherungsweise orthogonal, deshalb heißt das Modell multiplikatives saisonales MA-Modell.
- Das nichtmultiplikative Modell wt gleich (1 minus θ B minus Θ B hoch s) mal at hat die Autokorrelation an s plus 1 gleich null; das multiplikative Modell ist sparsamer, weil es bei gleicher Parameterzahl mehr von null verschiedene Autokorrelationen hat.
- Ist Θ gleich 1, enthält das Airline-Modell eine deterministische Saisonkomponente; Dummy-Variablen liefern dann dieselben Prognosen, bei nicht deterministischem Muster aber schlechtere.
- Bei kleiner Stichprobe oder möglicher deterministischer Saison soll ein multiplikatives saisonales Modell mit der exakten Likelihood geschätzt werden.
- Im Komponentenmodell der logarithmierten Quartalsgewinne je Aktie von Johnson & Johnson, 1960 bis 1980, ist yt = µt + γt + et, wobei γt die Saisonkomponente ist.
- Die Saison erfüllt (1 + B + B² + B³)γt = ωt, also γt = −Summe der drei vorangegangenen Saisonwerte plus ωt, mit ωt ∼ N(0, σ²ω).
- Das Modell hat die drei Parameter σe, ση und σω und ist ein einfaches Modell unbeobachteter Komponenten in Zustandsraumform.

## Voraussetzungen


## Anwendung im Trading

- Saisonale Zeitreihenmodelle sind für die Bewertung wetterabhängiger Derivate und von Energiefutures nützlich, weil die meisten umweltbezogenen Reihen stark saisonal sind.
- Wo Saisonalität zweitrangig ist, wird sie entfernt, und die saisonbereinigte Reihe dient der Inferenz; die meisten von der US-Regierung veröffentlichten Wirtschaftsdaten, etwa BIP-Wachstum und Arbeitslosenquote, sind saisonbereinigt.
- Für Prognosen ist die Saisonalität so wichtig wie die übrigen Merkmale und bleibt im Modell.

## Regeln und Kriterien


## Risiken und Grenzen

- Zustandsraummodelle sind eine Alternative für saisonale Reihen, doch die geschätzten Komponenten sind nicht eindeutig und hängen von Spezifikation und Nebenbedingungen ab.
- seasonalTrig in SsfPack liefert eine andere Zerlegung derselben Reihe; für die Prognose ist die Wahl unerheblich, sofern die Zerlegung gültig ist.

## Beispiele

- Buy-on-Gap kauft Aktien, die vom Tief des Vortags zur Eröffnung um mehr als eine Standardabweichung fallen und deren Open über dem 20-Tage-Durchschnitt liegt, und verkauft sie zum Schluss. Vom 11. Mai 2006 bis 24. April 2012 sind die annualisierte Rendite 8,7 Prozent und die Sharpe Ratio 1,5.
- Die Begründung ist der Tagesablauf: Panikverkäufe zur Eröffnung, wenn die Index-Futures vorher unten sind, ebbt ab, und die Aktie erholt sich über den Tag.
- Das Short-Spiegelbild, ein Gap nach oben um eine Standardabweichung bei einem Kurs unter dem 20-Tage-Durchschnitt, erzielt 46 Prozent annualisierte Rendite und eine Sharpe Ratio von 1,27, bei steilerem Drawdown.
- Die Quartalsgewinne von Johnson & Johnson von 1960.I bis 1980.IV wuchsen exponentiell, und ihre Schwankung nahm zu; der Logarithmus macht das Wachstum linear und stabilisiert die Varianz. Weil alle Gewinne positiv sind, ist vor dem Logarithmus keine Verschiebung nötig; sonst kann eine positive Konstante zu jedem Punkt addiert werden.
- Das mit exakter Likelihood angepasste Airline-Modell der Loggewinne lautet (1 minus B) mal (1 minus B hoch 4) mal xt gleich (1 minus 0,678 B) mal (1 minus 0,314 B hoch 4) mal at, mit Residualstandardabweichung 0,089; die Standardfehler der beiden MA-Parameter sind 0,080 und 0,101.
- Die Ljung-Box-Statistik der Residuen ist Q(12) gleich 10,0 mit p-Wert 0,44; das Modell wirkt angemessen.
- Neu geschätzt auf den ersten 76 Beobachtungen und bewertet an den letzten 8, zeigen die Ein- bis Acht-Schritt-Prognosen ab dem vierten Quartal 1978 ein starkes Saisonmuster und liegen nahe an den beobachteten Gewinnen; die Gewinnprognosen nutzen die Antilog-Transformation.
- Beim CRSP-Decile-1-Index von Januar 1970 bis Dezember 2008 geht das saisonale Verhalten der monatlichen einfachen Rendite hauptsächlich auf den Januar-Effekt zurück: nach einer Januar-Dummy verschwinden die Autokorrelationen bei den Lags 12, 24 und 36 weitgehend.
- Die Maximum-Likelihood-Schätzungen sind (σ̂e, σ̂η, σ̂ω) = (2,044516 × 10 hoch −6, 7,269655 × 10 hoch −2, 2,931691 × 10 hoch −2).
- Die geglättete Saison γt|T mit T = 84 verändert ihr Muster über die Zeit; Abbildung 11.6 zeigt Trend und Saison mit punktweisen 95-Prozent-Bereichen.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 99–118 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-008-p099-p118|S. 99–118]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 96–115 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-006-p096-p115|S. 96–115]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 115–134 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-007-p115-p134|S. 115–134]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 191–210 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-011-p191-p210|S. 191–210]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 229–248 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-013-p229-p248|S. 229–248]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 609–628 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-033-p609-p628|S. 609–628]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 628–647 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-034-p628-p647|S. 628–647]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 77–96 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-005-p077-p096|S. 77–96]]

## Verwandte Themen
