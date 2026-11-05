---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Strategien und Ausführung"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-01
---

# Mean-Reversion-System


## Kurzdefinition

- Die einfache lineare Handelsstrategie ist wirklich parameterfrei: die Stückzahl ist negativ proportional zur normalisierten Abweichung des Preises vom gleitenden Durchschnitt, und der Lookback wird gleich der Halbwertszeit gesetzt.

## Kernaussagen

- Weil es keine zu optimierenden Parameter gibt und der Lookback die Halbwertszeit der Reihe ist, lässt sich Gewinn ohne Data-Snooping-Bias zeigen.
- Fortlaufendes Ein- und Aussteigen hat voraussichtlich mehr statistische Signifikanz als selektive Ein- und Ausstiegsregeln.
- Solche Strategien lassen sich aus einer großen Vielfalt kointegrierender Aktien und ETFs bauen, auch aus Instrumenten, die einzeln nicht stationär sind.
- Sie reichen von Market Making auf Sekundenskala bis zum mehrjährigen Warten auf den fairen Wert.
- Die lineare Strategie hält eine Stückzahl, die negativ proportional zur normalisierten Abweichung vom gleitenden Durchschnitt ist. Der Lookback von Durchschnitt und Standardabweichung wird gleich der Halbwertszeit gesetzt, im USD.CAD-Beispiel auf die gerundeten 115 Tage.
- Bei einer Halbwertszeit von 20 Tagen wäre ein Lookback von 5 Tagen für Durchschnitt und Standardabweichung zu kurz. Ein kleines Vielfaches der Halbwertszeit ist oft nahe optimal und vermeidet die Optimierung eines freien Parameters an der Strategieperformance.
- Der USD.CAD-Backtest ist positiv trotz langer Halbwertszeit, aber mit großem Drawdown. Transaktionskosten fehlen, der Lookback stammt aus der Stichprobe, und ohne Obergrenze des Marktwerts kann unbegrenztes Kapital nötig sein. Der Autor empfiehlt das Beispiel nicht praktisch und verweist auf Kapitel 5.
- Das Portfolio aus EWA, EWC und IGE zum ersten Johansen-Eigenvektor hat eine Halbwertszeit von 23 Tagen und soll sich deshalb besser handeln lassen als USD.CAD.
- Gleitender Durchschnitt und gleitende Standardabweichung passen sich einem langsam wandernden Mittel und einer mit der Zeit steigenden Varianz an und nehmen Gewinn schneller mit.
- In der einfachsten Form ist die lineare Strategie unpraktisch: das maximale Kapital ist vorher unbekannt, und infinitesimale Stückzahlen bei infinitesimalen Preisänderungen sind nicht handelbar.
- Die Strategie auf dem Einheitsportfolio aus EWA, EWC und IGE erreicht eine APR von 12,6 Prozent und eine Sharpe Ratio von 1,4. Die Rendite ist der P&L geteilt durch den Bruttomarktwert der verzögerten Positionen.
- Die Dollarposition je ETF ist das Vielfache des Einheitsportfolios mal Eigenvektor-Stückzahl mal Preis. Das Vielfache ist der negative Z-Score des Einheitsportfolio-Preises, mit Lookback gleich der Halbwertszeit.
- Jährlich neu aufgelegte, nur geringfügig andere ETFs vergrößern die Menge baubarer stationärer Portfolios.
- Übliche Stop-Losses lassen sich bei Mean-Reversion-Strategien logisch nicht einsetzen. Kapitel 8 behandelt, warum das so ist, und welche Risikotechniken passen.
- Praktischer als die lineare Strategie sind Bollinger-Bänder, weil jederzeit null oder eine Einheit gehalten wird und die Kapitalbindung damit nach oben begrenzt ist. Einstieg jenseits von entryZscore Standardabweichungen, Ausstieg bei einem kleineren exitZscore.
- Auf GLD-USO steigen APR und Sharpe Ratio von etwa 10,9 Prozent und 0,59 beim linearen adaptiven Preisspread auf 17,8 Prozent und 0,96 bei Bollinger mit entryZscore 1 und exitZscore 0.
- Der Logpreisspread liegt bei 9 Prozent APR und Sharpe Ratio 0,5. Die Ratio USO/GLD hat eine negative APR; Long und Short haben dort dasselbe Dollarkapital.
- Der Kalman-Handel von EWA-EWC, Einstieg bei einer Prognoseabweichung jenseits der Wurzel von Q, erreicht 26,2 Prozent APR und eine Sharpe Ratio von 2,4.
- Mehrere Bollinger-Niveaus setzen Scaling-in um. Nach Schoenberg und Corwin ist ein einzelner Ein- und Ausstieg im Backtest immer mindestens so gut; bei nicht konstanter Volatilität kann Scaling-in out of sample die realisierte Sharpe Ratio trotzdem verbessern.
- Schrittweises Aussteigen realisiert kleine Gewinne auch dann, wenn die Reihe den Mittelwert nie erreicht.
- Auf VX-Kalenderspreads ist das Signal das Verhältnis Back zu Front, mit 15 Tagen Lookback für Durchschnitt und Standardabweichung; vom 27. Oktober 2008 bis zum 23. April 2012 ergeben sich 17,7 Prozent annualisierte Rendite und eine Sharpe Ratio von 1,5.
- Vor Oktober 2008 schnitt diese VX-Strategie deutlich schlechter ab.
- Dieselbe lineare Strategie auf dem 12-Monats-Kalenderspread von CL erzielt vom 2. Januar 2008 bis zum 13. August 2012 ungehebelte 8,3 Prozent annualisiert und eine Sharpe Ratio von 1,3; die kumulierten Renditen zeigt Abbildung 5.7.
- Die Bollinger-Band-ähnliche Variante shortet das Portfolio aus 0,3906 VX und einem ES, wenn der Wert um eine Standardabweichung der Residuen aus den ersten 500 Tagen nach August 2008 abweicht.
- Auf dem Testset vom 29. Juli 2010 bis zum 8. Mai 2012 beträgt die annualisierte Rendite dieser ES-VX-Strategie 12,3 Prozent bei einer Sharpe Ratio von 1,4.
- Auf dem Crack Spread hat die lineare Strategie in der Phase des Anstiegs bis zum 3. Juli 2008 und des anschließenden Falls negative Renditen.
- Bei CL kauft die kombinierte Regel zum Schluss, wenn der Preis unter dem von vor 30 Tagen und über dem von vor 40 Tagen liegt, geht umgekehrt short und stellt glatt, wenn keine Bedingung erfüllt ist; die annualisierte Rendite ist 12 Prozent bei einer Sharpe Ratio von 1,1.
- Ein Mean-Reversion-Filter auf der Zeitreihen-Momentum-Regel von Beispiel 6.1 verbessert die Renditen und Sharpe Ratios der Kontrakte in Tabelle 6.2 und nimmt zusätzlich IBX, KT, SXF, US, CD, NG und W auf.
- Die Strategie, Aktien mit dem stärksten Verkaufsdruck der Quartale t minus 4 bis t minus 1 zu kaufen und umgekehrt zu shorten, erzielt weitere 7 Prozent annualisiert.
- Das lineare Mean-Reversion-Modell auf S&P-500-Aktien in Kapitel 4 nutzt die kurzfristige querschnittliche Mean Reversion, hält weniger als einen Tag und hat eine Sharpe Ratio von 4,7.
- Stop-Losses sind mit Mean-Reversion-Strategien nicht vereinbar, weil sie dem Einstiegssignal widersprechen.
- Die Gewinnobergrenze ist der Mean, zu dem die Preise zurückkehren; der Verlust einer einzelnen Position ist nicht ebenso gedeckelt und kann einen enormen Drawdown erzeugen.

## Funktionsweise

- Die einfachsten Techniken und Strategien für mean-revertierende Portfolios sind lineare Modelle, Bollinger-Bänder und der Kalman-Filter.
- Als Eingaben für diese Tests und Strategien kommen Rohpreise, Log-Preise oder Verhältnisse infrage, und es wird gezeigt, welche Wahl am sinnvollsten ist.
- Der Kalman-Filter ist für Trader auf mehrere Arten und in mehreren Strategien nützlich.
- Der Z-Score ist Preis minus gleitender Durchschnitt, geteilt durch die gleitende Standardabweichung; die gehaltene Stückzahl ist der negative Z-Score.
- Bei einem Währungspaar USD.X ist der Marktwert einer Einheit gleich dem Kurs, deshalb setzt die lineare Mean Reversion den Portfoliomarktwert auf den negativen Z-Score von USD.CAD.
- Die tägliche P&L ist der um einen Tag verzögerte Marktwert mal der einfachen Rendite des Kurses.
- Für ein Portfolio werden Einheiten proportional zum negativen Z-Score des Preises des Einheitsportfolios aufgebaut; die Stücke des Einheitsportfolios bestimmt der Johansen-Eigenvektor.
- Die lineare Strategie hält Vielfache des Einheitsportfolios gleich dem negativen Z-Score seines Nettomarktwerts, mit Lookback gleich der gerundeten Halbwertszeit.
- Die Dollarposition je ETF ist dieses Vielfache mal den Eigenvektor-Stücken mal dem Kurs.
- Linear heißt nur, dass die Stückzahl proportional zum Z-Score ist, nicht der Marktwert der Anlage.
- Ein Einheitsportfolio aus genau einer Long- und einer Short-Position heißt Spread.
- Die lineare Fassung setzt die Stückzahl des Einheitsportfolios proportional zur Abweichung seines Marktwerts vom gleitenden Mittel und ist praktisch parameterfrei.
- Die Bollinger-Fassung hält null oder eine Einheit und schaltet bei entryZscore ein und bei exitZscore aus.
- Scaling-in staffelt mehrere Bollinger-Einstiege bei 1, 2, 3 bis N Standardabweichungen und die Ausstiege bei 0, 1, 2 bis N minus 1.
- Der Kalman-Filter ersetzt gleitende Hedge Ratio, gleitenden Durchschnitt und gleitende Standardabweichung durch Steigung, Achsenabschnitt und Prognosefehler-Standardabweichung.
- Für den Log-Preis-Spread sind die Gewichte Kapitalgewichte, und das System muss ständig rebalancieren; der Preis-Spread rechnet mit Stückzahlen.
- Der Überschussreturn eines über Nacht gehaltenen Cross enthält die Log-Preisänderung plus log(1 plus i der Basiswährung) minus log(1 plus i der Quotierungswährung).
- Die übliche lineare Mean-Reversion-Strategie auf VX benutzt das Ratio Back zu Front als Signal und einen Lookback von 15 Tagen für den gleitenden Durchschnitt und die Standardabweichungen.
- Die Bollinger-Band-ähnliche Strategie auf ES und VX shortet das Portfolio, sobald dessen Wert um eine Standardabweichung der Residuen aus dem Trainingsset abweicht.
- Das Trainingsset für diese Regression sind die ersten 500 Tage nach August 2008, und die Standardabweichung der Residuen beträgt 2.047 Dollar.

## Voraussetzungen

- Voraussetzung für den profitablen Handel ist, dass die Reihe mean-reverting ist und die Halbwertszeit kurz genug für den eigenen Zeithorizont.
- Lookback gleich der gerundeten Halbwertszeit vermeidet die Brute-Force-Optimierung eines freien Parameters anhand der Strategieperformance.

## Anwendung im Trading

- Beispiele werden aus Interday- und Intraday-Aktienmodellen, ETF-Paaren und -Triplets, ETFs gegen ihre Komponentenaktien, Währungspaaren sowie Futures-Kalender- und Intermarket-Spreads gezogen.
- Fundamentale Überlegungen können erklären, warum ein bisher sehr profitables ETF-Paar sich vorübergehend löst, und daraus eine verbesserte Strategie bauen.
- Bei Währungen wird erklärt, warum schon die Renditeberechnung einem Aktienhändler fremd sein kann und wann Rollover-Zinsen wichtig sein können.
- Mehrere Futures-Strategien lassen sich aus einem einfachen mathematischen Modell der Futures-Preise ableiten. Backwardation und Contango werden grafisch und mathematisch gezeigt, und Spot-Renditen werden den Roll-Renditen gegenübergestellt.
- Der Volatility-Future VX kann die Grundlage einiger recht lukrativer Strategien sein.
- Auf dem CL-12-Monats-Kalenderspread ergibt die lineare Mean-Reversion-Strategie vom 2. Januar 2008 bis zum 13. August 2012 eine ungehebelte annualisierte Rendite von 8,3 Prozent bei einer Sharpe Ratio von 1,3.
- Auf dem VX-Kalenderspread ergibt sie vom 27. Oktober 2008 bis zum 23. April 2012 eine annualisierte Rendite von 17,7 Prozent bei einer Sharpe Ratio von 1,5.
- Auf dem Testset vom 29. Juli 2010 bis zum 8. Mai 2012 ergibt die ES-VX-Strategie eine annualisierte Rendite von 12,3 Prozent bei einer Sharpe Ratio von 1,4.
- Auf dem Crack Spread zeigt die lineare Mean-Reversion-Strategie negative Renditen über den beschriebenen Anstieg vom 9. März 2007 bis zum 3. Juli 2008 und den scharfen Fall danach.
- Ein Portfolio aus Mean-Reversion-Systemen erreicht zusammen mit Momentum-Strategien höhere Sharpe Ratios und kleinere Drawdowns als jedes der beiden Systeme allein.

## Regeln und Kriterien

- entryZscore und N werden auf einem Trainingsset optimiert, der Lookback kann optimiert oder gleich der Halbwertszeit gesetzt werden.
- Beim Verhältnis werden Long- und Short-Seite mit demselben Dollarkapital gefahren.
- Beim Kalman-Beispiel ist der Einstieg jenseits einer Prognose-Standardabweichung und der Ausstieg, sobald der Fehler dieses Band wieder nach innen kreuzt.
- Feste Stückzahl je Bestandteil über die Trade-Dauer: Hedge Ratios aus der Preisreihe; feste Marktwerte je Bestandteil: Hedge Ratios aus der Log-Preisreihe.
- Bei Währungspaaren wird oft das Ratio statt des Spreads als Indikator verwendet.
- Können Hedge Ratio, Mittel und Standardabweichung eines Spreads künftig variieren, werden ein gleitender Look-back oder der Kalman-Filter eingesetzt.
- Eine praktische lineare Umsetzung sind Bollinger-Bänder mit Scaling-in.
- Der erwartete Preis wird aus dem letzten Trade, Preis und Größe, mit dem Kalman-Filter aktualisiert.
- Buy-on-Gap: Aktien nahe der Eröffnung, deren Rendite vom Vortagestief zum Open kleiner als minus eine Standardabweichung der Close-to-Close-Renditen der letzten 90 Tage ist, deren Open über dem 20-Tage-Schlussdurchschnitt liegt, davon die 10 mit der niedrigsten Rendite seit dem Vortagestief, sonst die ganze kürzere Liste, und Liquidation aller Positionen zum Marktschluss.
- Die Begründung ist Panikverkauf zum Open an Tagen, an denen die Aktienindex-Futures vor der Eröffnung unten sind; danach soll die Aktie über den Tag allmählich steigen, und Regel 2 ist ein Momentum-Filter.
- Die Short-Spiegelung shortet Aktien, die um eine Standardabweichung nach oben gappen und noch unter dem 20-Tage-Durchschnitt liegen.
- Genannte Varianten handeln Long- und Short-Seite zugleich, sind long Aktien und short Index-Futures, kaufen mehr Titel bei Sektorbegrenzung, verlängern das Kaufzeitfenster über die Eröffnung hinaus oder setzen Intraday-Gewinnobergrenzen.
- Die SPY-Arbitrage nimmt im Training 2007 alle Aktien, die im Johansen-Test mit mindestens 90 Prozent mit SPY kointegrieren, bildet ein gleichgewichtetes Long-only-Portfolio, prüft dessen Kointegration auf Logpreisen erneut und handelt dann die lineare Mean-Reversion-Strategie mit Look-back 5.
- Das lineare Long-Short investiert jeden Tag das Bruttokapital von 1 Dollar nach wi gleich minus (ri minus Durchschnitt) geteilt durch die Summe der absoluten Abweichungen, nahe dem Schluss; die Intraday-Fassung bestimmt die Gewichte aus der Rendite vom vorigen Schluss zum Open und liquidiert zum Schluss.
- Neben der relativen Rendite kann das Kurs-Gewinn-Verhältnis zum Rangieren dienen, mit Gewinnen des letzten Quartals oder mit projizierten Gewinnen von Analysten oder Unternehmen.
- Das Währungssystem ist eine lineare Mean-Reversion-Strategie: Johansen auf einem rollierenden Trainingsfenster von 250 Tagen für die Hedge Ratio, Look-back 20 für Mittel und Standardabweichung, Zahl der Einheiten minus dem Z-Score des Portfolio-Marktwerts.
- Gehandelt werden AUD.USD und CAD.USD, nicht das Cross mit Hedge Ratio eins; gekauft werden soll CAD, wenn CAD.USD deutlich unter AUD.USD liegt.
- Die einfachere Fassung handelt das fertige Paar AUD.CAD, Look-back 20, und addiert die Overnight-Rollover-Zinsen; mittwochs wird der AUD-Zins verdreifacht, donnerstags der CAD-Zins.
- Der CL-Kalender-Spread nutzt das hoffentlich mean-reverting γ als Signal, mit Look-back gleich der gerundeten Halbwertszeit von etwa 36 Tagen.
- Je Tag wird ein Far- und ein Near-Kontrakt gewählt: Haltedauer 3 Monate oder 61 Handelstage, Rollen 10 Tage vor Verfall des Near-Kontrakts, Verfälle ein Jahr auseinander; zunächst long Far und short Near, und bei positivem Z-Score werden die Positionen umgekehrt.
- Die ungehebelte Tagesrendite ist der P&L geteilt durch 2, weil zwei Kontrakte im Spread sind.
- Mean-Reversion-Regeln geben das Konzept vor, dass eine Datenreihe zu ihrem Mittelwert zurückkehrt, sobald sie gegenüber den jüngeren Werten extrem hoch oder extrem tief liegt.
- Soll das Portfolio während des Trades eine feste Stückzahl halten, werden die Hedge Ratios aus den Preisreihen bestimmt. Sollen die Marktwerte der Bestandteile fest bleiben, aus den Log-Preisreihen.
- Für Währungspaare ist das Verhältnis oft ein besserer Indikator als der Spread.
- Können Hedge Ratio, Mittel und Standardabweichung eines Spreads künftig variieren, helfen ein gleitender Lookback oder der Kalman-Filter.
- Scaling-in ist im Backtest oft nicht optimal, im Live-Handel aber häufig nützlich, weil Volatilitäten und Wahrscheinlichkeiten sich ändern.
- Den erwarteten Preis aus dem letzten Trade, also aus Preis und Größe, führt der Kalman-Filter dynamisch nach.
- Buy-on-Gap wählt nahe der Eröffnung Aktien, deren Rendite vom Tief des Vortags bis zur heutigen Eröffnung unter minus einer Standardabweichung liegt. Die Standardabweichung kommt aus den Close-to-Close-Renditen der letzten 90 Tage. Das sind die nach unten gegappten Aktien.
- Zusätzlich muss der Eröffnungskurs über dem 20-Tage-Durchschnitt der Schlusskurse liegen.
- Gekauft werden die zehn Titel dieser Liste mit der niedrigsten Rendite seit dem Tief des Vortags. Sind es weniger als zehn, wird die ganze Liste gekauft. Alle Positionen werden zum Marktschluss glattgestellt.
- Vom 11. Mai 2006 bis 24. April 2012 beträgt die annualisierte Rendite 8,7 Prozent und die Sharpe Ratio 1,5.
- Die Begründung: sind die Aktienindex-Futures vor der Eröffnung unten, leiden manche Aktien überproportional unter Panikverkäufen zur Eröffnung und erholen sich im Tagesverlauf.
- Die Durchschnitts-Regel ist ein Momentum-Filter. Nur wenig gefallene Aktien kehren eher um, weil stark gefallene oft negative Nachrichten wie schlechte Gewinnmeldungen haben, und nachrichtengetriebene Einbrüche seltener umkehren.
- Ein Kurs über einem langfristigen Durchschnitt zieht Verkaufsdruck länger orientierter Long-only-Fonds an. Der Liquiditätsbedarf zur Eröffnung überzeichnet den Abwärtsdruck, und solche Bewegungen kehren eher um als fundamentale.
- Eine Fassung ohne diese Durchschnitts-Regel litt ab 2009 unter abnehmenden Renditen. Die reine Long-Ausrichtung erschwert das Risikomanagement, und die kleine Zahl gehandelter Aktien begrenzt die Kapazität.
- Das Spiegelbild shortet Aktien, die um eine Standardabweichung nach oben gappen und dennoch unter ihrem 20-Tage-Durchschnitt liegen: 46 Prozent annualisierte Rendite und Sharpe Ratio 1,27 über denselben Zeitraum, bei steilerem Drawdown und Leerverkaufsbeschränkung.
- Varianten handeln Long und Short zugleich, hedgen Long-Aktien mit Short-Index-Futures, begrenzen die Titel je Sektor, verlängern das Kaufzeitfenster über die Eröffnung hinaus oder setzen Intraday-Gewinnobergrenzen.
- Das SPY-System sucht im Trainingsjahr 2007 alle Aktien, die im Johansen-Test mit mindestens 90 Prozent mit SPY kointegrieren, bildet daraus ein gleichgewichtiges Long-only-Portfolio und prüft die Kointegration mit SPY auf Log-Preisen erneut, weil täglich auf konstantes Kapital je Aktie rebalanciert wird.
- Auf dem Testzeitraum 2. Januar 2008 bis 9. April 2012 läuft die lineare Mean Reversion mit einem im Rückblick auf 5 fixierten Lookback. Die annualisierte Rendite ist 4,5 Prozent, die Sharpe Ratio 1,3, und die Performance fällt, solange Bestandteile und Hedge Ratios nicht nachtrainiert werden.
- Das lineare Long-Short-Modell von Khandani und Lo setzt nahe dem Schluss für jede Aktie eines Index wie S&P 500, S&P 1500 oder Russell 2000 ein Kapital proportional zur negativen Abweichung ihrer Tagesrendite vom Durchschnitt, normiert auf 1 Dollar Brutto.
- Auf dem S&P 500 vom 2. Januar 2007 bis 30. Dezember 2011 sind annualisierte Rendite 13,7 Prozent und Sharpe Ratio 1,3. Die Strategie ist parameterfrei und nahezu dollarneutral. Ab Anfang 2008 ist der Test echt out of sample, weil sie 2007 veröffentlicht wurde.
- Die Intraday-Variante bestimmt die Gewichte aus der Rendite vom vorigen Schluss zur heutigen Eröffnung und stellt zum Schluss glatt: 73 Prozent annualisierte Rendite und Sharpe Ratio 4,7, bei verdoppelten, im Backtest fehlenden Transaktionskosten und Signalrauschen an der Eröffnung.
- Beispiel 5.1 handelt AUD.USD gegen CAD.USD mit einer Hedge Ratio ungleich eins, also nicht als Kreuzkurs AUD.CAD. Der Johansen-Test läuft auf den Log-Preisen der vorangehenden 250 Tage, genommen wird die erste Spalte des Eigenvektors.
- Mittel und Standardabweichung nutzen 20 Tage. Die Stückzahl des Einheitsportfolios ist der negative Z-Score, die Marktwerte in USD sind Stückzahl mal Hedge Ratio mal Preis.
- Die Tagesrendite ist der Gewinn geteilt durch den gesamten Bruttomarktwert am Ende des Vortags. Nach Ausschluss der ersten 250 Tage sind annualisierte Rendite 11 Prozent und Sharpe Ratio 1,6, vom 18. Dezember 2009 bis 26. April 2012.
- Gekauft wird CAD, wenn CAD.USD deutlich unter AUD.USD liegt. Live entspricht der Kauf einer Einheit CAD.USD dem Verkauf von 1/y Einheiten USD.CAD.
- Beispiel 5.2 handelt den fertigen Kreuzkurs AUD.CAD und hält über 17:00 Uhr ET, deshalb mit Rollover. Die Position ist das negative Vorzeichen von Schluss minus 20-Tage-Durchschnitt.
- Die Überschussrendite addiert log(1 + Zinssatz AUD) minus log(1 + Zinssatz CAD) zur Log-Preisänderung. Der AUD-Rollover wird mittwochs verdreifacht, der CAD-Rollover donnerstags.
- Diese Fassung erzielt 6,2 Prozent annualisierte Rendite bei einer Sharpe Ratio von 0,54, ohne Rollover 6,7 Prozent und 0,58, und bleibt damit deutlich schwächer als die ungleiche Hedge Ratio. Der annualisierte durchschnittliche Rollover beträgt fast 5 Prozent.
- Der Log-Marktwert eines Kalenderspreads, long der ferne und short der nahe Kontrakt, ist die Rollrendite mal (T1 − T2). Weil die Fälligkeiten fest sind, erzeugt die Rollrendite die Signale.
- Die Halbwertszeit der CL-Rollrendite ist etwa 36 Tage, aus minus log(2) geteilt durch die Steigung der Regression der Änderung auf den verzögerten Wert. Lookback von Mittel und Standardabweichung ist diese gerundete Halbwertszeit.
- Gehalten wird ein Paar 61 Handelstage, gerollt wird zehn Tage vor Verfall des nahen Kontrakts, und die Fälligkeiten liegen ein Jahr auseinander. Bei positivem Z-Score drehen die Vorzeichen von long fern und short nah.
- Die ungehebelt Tagesrendite teilt den Gewinn durch 2, weil zwei Kontrakte gehalten werden. Vom 2. Januar 2008 bis 13. August 2012 sind annualisierte Rendite 8,3 Prozent und Sharpe Ratio 1,3.
- Dieselbe lineare Regel auf VX-Kalenderspreads lässt sich mit der Gleichung für gehandelte Basiswerte nicht begründen: VIX wird nicht gehandelt, die Log-Preise gegen die Restlaufzeit liegen nicht auf einer Geraden, und die Formeln von Dupoyet, Daigler und Chen (2011) erklären die Mean Reversion nicht.

## Risiken und Grenzen

- Die Vor- und Nachteile des Scaling-in werden erörtert.
- Datenfehler sind bei Mean-Reversion-Strategien besonders gefährlich, wenn sie Spreads betreffen.
- Dark Pools und Hochfrequenzhandel machen manche dieser Strategien in den letzten Jahren herausfordernd.
- Die Beispielstrategien sind Prototypen. In den Backtest-Codes fehlen Transaktionskosten, und In-Sample-Daten dienen oft zugleich der Parameteroptimierung und der Leistungsmessung, was die Ergebnisse aufbläht. Sie sind nicht zum unveränderten Handel gedacht.
- Das USD.CAD-Beispiel enthält keine Transaktionskosten, Look-ahead Bias durch den In-Sample-Lookback und keine Obergrenze des Marktwerts, sodass unbegrenzt Kapital nötig sein kann.
- Der Autor empfiehlt es nicht als praktische Strategie; eine praktischere Fassung steht in Kapitel 5.
- Unbekanntes Höchstkapital und die Unmöglichkeit, infinitesimal zu handeln, machen die einfachste Fassung unpraktisch.
- Hohe Stetigkeit verführt zu Überkonfidenz und zu viel Leverage, und der Bruch beim maximalen Leverage kann katastrophal sein (Dever, 2011).
- Übliche Stop-Losses lassen sich logisch nicht einsetzen; geeignete Verfahren stehen in Kapitel 8.
- Eine kurze Zeitskala erhöht die Zahl der Trades, die statistische Sicherheit, die Sharpe Ratio und die zusammengesetzte Rendite.
- Die lineare Fassung verlangt unbegrenzt Kaufkraft und fortlaufendes infinitesimales Rebalancing und ist deshalb unpraktisch.
- Schoenberg und Corwin zeigen, dass mehrere Bollinger-Ein- oder Ausstiege im Backtest nie optimal sind, solange die Wahrscheinlichkeit eines tieferen Einbruchs konstant ist.
- Die vorgestellten Backtests enthalten keine Transaktionskosten und teilweise Look-ahead Bias durch auf denselben Daten optimierte Parameter.
- Scaling-in muss im Backtest nicht optimal sein, ist live aber oft nützlich, weil Volatilitäten und Wahrscheinlichkeiten sich ändern.
- Datenfehler können die Backtest-Ergebnisse von Mean-Reversion-Strategien aufblähen, die von Momentum-Strategien aber nicht.
- Spread-Strategien sind gegen kleine Datenfehler besonders empfindlich, im Backtest und im Live-Handel.
- Das Modell ist vollständig linear, parameterfrei und fast vollkommen dollarneutral.
- Die Open-to-Close-Fassung verdoppelt die nicht im Backtest enthaltenen Transaktionskosten und unterliegt dem Signalrauschen der Open-Preise.
- Eine positive Änderung der Gewinnschätzungen spricht für eine positive Rendite; liegt diese Rendite im Einklang mit der prozentualen Änderung der Schätzungen, ist keine Mean Reversion zu erwarten, und ein Rang nach dem Kurs-Gewinn-Verhältnis vermeidet, eine solche Aktie zu shorten.
- Ein Stop-Loss widerspricht den Einstiegssignalen eines Mean-Reversion-Systems und ist deshalb damit nicht verträglich.
- Eine einzige Position kann einen enormen Drawdown erzeugen.
- Das Aufwärtspotenzial ist auf das Mittel gedeckelt, zu dem die Preise zurückkehren, das Abwärtspotenzial kann unbegrenzt sein.
- Der Aufstieg von Dark Pools und Hochfrequenzhandel hat den Handel mancher Mean-Reversion-Strategien in den letzten Jahren erheblich erschwert.
- Datenfehler blähen die Backtests von Mean-Reversion-Strategien auf, die von Momentum-Strategien dagegen nicht.

## Beispiele

- Auf USD.CAD ist die kumulierte P&L trotz etwa 115 Tagen Halbwertszeit positiv, mit großem Drawdown.
- Das Einheitsportfolio aus dem stärksten Eigenvektor von EWA, EWC und IGE hat 23 Tage Halbwertszeit, kürzer als die 115 Tage von USD.CAD.
- Auf EWA, EWC und IGE beträgt die Halbwertszeit 23 Tage, die APR 12,6 Prozent und die Sharpe Ratio 1,4.
- EWA mit EWC folgt aus zwei rohstoffdominierten Volkswirtschaften, GDX mit GLD aus der Abhängigkeit der Goldbergbauer vom Goldpreis.
- GLD gegen USO: Preis-Spread etwa 10,9 Prozent APR und Sharpe Ratio etwa 0,59, Log-Spread 9 Prozent und 0,5, Verhältnis negative APR, Bollinger-Band 17,8 Prozent und 0,96.
- EWA gegen EWC mit Kalman-Filter: 26,2 Prozent APR und Sharpe Ratio 2,4, bei δ gleich 0,0001 und Ve gleich 0,001.
- Buy-on-Gap auf dem S&P 500 mit Survivorship Bias: APR 8,7 Prozent und Sharpe Ratio 1,5 vom 11. Mai 2006 bis 24. April 2012; die Autorenfassung ohne Regel 2 war profitabel, litt aber ab 2009 unter nachlassenden Renditen und hat geringe Kapazität.
- Short-on-Gap: APR 46 Prozent und Sharpe Ratio 1,27 über denselben Zeitraum, mit steilerem Drawdown.
- SPY gegen die 98 Komponenten: APR 4,5 Prozent und Sharpe Ratio 1,3 vom 2. Januar 2008 bis 9. April 2012.
- Lineares Long-Short auf dem SPX: APR 13,7 Prozent und Sharpe Ratio 1,3 vom 2. Januar 2007 bis 30. Dezember 2011, davon APR 30 Prozent 2008 und 11 Prozent 2011; die Open-to-Close-Variante hat APR 73 Prozent und Sharpe Ratio 4,7.
- AUD.USD gegen CAD.USD: APR 11 Prozent und Sharpe Ratio 1,6 vom 18. Dezember 2009 bis 26. April 2012, ohne die ersten 250 Trainingstage.
- AUD.CAD mit Rollover: APR 6,2 Prozent und Sharpe Ratio 0,54, deutlich schwächer als die Fassung mit Hedge Ratio ungleich eins; ohne Rollover wären es 6,7 Prozent und 0,58.
- CL-12-Monats-Spread: ungehebelte APR 8,3 Prozent und Sharpe Ratio 1,3 vom 2. Januar 2008 bis 13. August 2012.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 476–495 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-026-p476-p495|S. 476–495]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 1–13 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-001-p001-p013|S. 1–13]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 52–71 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-004-p052-p071|S. 52–71]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 71–75 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-005-p071-p075|S. 71–75]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 76–95 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-006-p076-p095|S. 76–95]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 95–98 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-007-p095-p098|S. 95–98]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 99–118 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-008-p099-p118|S. 99–118]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 119–138 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-009-p119-p138|S. 119–138]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 138–143 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-010-p138-p143|S. 138–143]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 144–163 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-011-p144-p163|S. 144–163]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 163–165 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-012-p163-p165|S. 163–165]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 457–476 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-025-p457-p476|S. 457–476]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 476–495 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-026-p476-p495|S. 476–495]]

## Verwandte Themen
