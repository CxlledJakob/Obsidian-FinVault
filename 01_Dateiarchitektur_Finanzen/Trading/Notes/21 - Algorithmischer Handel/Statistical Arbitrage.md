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

# Statistical Arbitrage


## Kurzdefinition


## Kernaussagen

- Die Dezimalisierung am 9. April 2001 senkte die Profitabilität vieler Statistical-Arbitrage-Strategien und erhöhte zugleich die vieler Hochfrequenzstrategien.
- Ursache war, dass die Bid-Ask-Spreads sanken und die angezeigte Liquidität am besten Bid und Ask ebenfalls sank, nach Arnuk und Saluzzi 2012.
- Weil mean-reverting Muster in Aktien leicht zu finden sind, zieht der Markt viele Händler an, oft Statistical Arbitrageure genannt, und die Renditen solcher Strategien sind deshalb allgemein gesunken.
- Index-Arbitrage handelt die Wertdifferenz zwischen einem Portfolio der Indexaktien und den Futures auf diesen Index; bei gleicher Gewichtung wie im Index kointegriert der Marktwert sehr eng mit den Index-Futures, und die Differenz ist extrem klein geworden (Reverre, 2001).
- Nur die ausgefeiltesten Händler können daraus noch Gewinn ziehen, und die Strategie muss intraday, vielleicht hochfrequent, gehandelt werden; die Differenz lässt sich vergrößern, indem nur eine Teilmenge der Indexaktien das Portfolio bildet.
- Gelegenheiten für Mean-Reversion-Strategien in Währungen und Futures sind begrenzt, aber nicht inexistent, weil die meisten Paare nicht kointegrieren und die meisten Portfolios keine querschnittliche Mean Reversion zeigen.
- Die zentrale Schwierigkeit beim Backtest von Währungsarbitrage ist nicht die Komplexität der Strategien, sondern die richtige Aufbereitung der Datenreihen für Kointegrationstests und die richtige Formel zur Renditemessung.
- Die Extraktion der Rollrendite funktioniert, solange das Vorzeichen der Rollrendite nicht schnell wechselt, was gewöhnlich nicht geschieht.
- Sie hat voraussichtlich kürzere Haltedauer und geringeres Risiko als Buy-and-Hold, weil der verrauschte Spot nicht lange ausgemittelt werden muss.
- Den Basiswert zu kaufen und besonders zu shorten ist logistisch schwer, außer ein ETF hält den Basiswert.
- GLD hält physisches Gold und folgt dem Spot eng; Gold-Futures haben von Dezember 1982 bis Mai 2004 eine Rollrendite von minus 4,9 Prozent annualisiert.
- Long GLD und short GC erzielen vom 3. August 2007 bis zum 2. August 2010 1,9 Prozent annualisiert bei einem maximalen Drawdown von 0,8 Prozent; ein Hebel von 5 oder 6 wirkt attraktiv, die Finanzierungskosten von GLD liegen aber nahe bei 1,9 Prozent, die Überschussrendite ist nahe null.
- Die GC-Schlüsse liegen um 13:30 Uhr ET, die GLD-Schlüsse um 16:00 Uhr ET; weil die Signale nur aus GC kommen, schadet diese Asynchronität hier nicht.
- Es gibt keine ETFs, die andere physische Rohstoffe statt Rohstoff-Futures halten, wegen der hohen Lagerkosten.
- ETFs von Förderunternehmen kointegrieren oft mit dem Spot, weil die Rohstoffe einen großen Teil ihrer Vermögenswerte ausmachen, und können als Proxy dienen.
- Short USO und long XLE, wenn CL in Contango ist, und umgekehrt in Backwardation, erzielen vom 26. April 2006 bis zum 9. April 2012 16 Prozent annualisiert bei einer Sharpe Ratio von etwa 1.
- Einen Optionskorb zu halten, der den VIX nachbaut, ist sehr teuer, und kein ETF-Sponsor hat das getan; gesucht wird nur hohe Korrelation oder Antikorrelation zur Spotrendite, und SPY erfüllt das für VIX.
- Weil ES leichter als ein ETF zu handeln ist und nur etwa 1 Prozent annualisierte Rollrendite hat, ersetzt ES in der Arbitrage den Aktien-ETF.
- Die Regel von Simon und Campasano shortet 0,3906 VX und ein ES, wenn der VX-Frontkontrakt um 0,1 Punkte je Handelstag bis zum Settlement über dem VIX liegt, und kauft beide, wenn er um denselben Betrag darunter liegt; gehalten wird ein Tag.
- Die Hedge Ratio stammt aus der Preisregression von Gleichung 5.11, nicht aus der Renditeregression des Originalpapiers; Settlement ist der Tag nach dem Verfall der Kontrakte.
- Vom 29. Juli 2010 bis zum 7. Mai 2012, außerhalb der Bestimmung der Hedge Ratio, beträgt die annualisierte Rendite 6,9 Prozent bei einer Sharpe Ratio von 1.
- Ein dritter Weg kauft Futures in Backwardation und shortet zugleich Futures in Contango, damit sich die Spot-Renditen aufheben und die günstigen Rollrenditen bleiben.

## Funktionsweise

- Hochfrequenzhändler nutzen zwei Mängel der intraday Indexberechnung: viele große Indizes, darunter Dow Jones, S&P, Nasdaq und Russell, verwenden nur Trades der Primärbörse, weniger als 30 Prozent aller gehandelten Stücke (Arnuk und Saluzzi, 2012), und der Index wird nur alle paar Sekunden aktualisiert.
- Beide Mängel erzeugen eine Abweichung zwischen dem aktuellen Marktwert des Aktienkorbs und dem Indexwert, sodass der Index-Future dem augenblicklichen Marktwert der Aktien nachläuft; liegt der Future darüber, wird er geshortet, und umgekehrt.
- Diesen augenblicklichen Marktwert liefert der direkte Datenfeed jeder US-Börse und jedes ECN, nicht der SIAC-Feed, mit Überwachung aller Indexaktien bei Latenz im Millisekundenbereich.
- Dieselbe Idee wird auf ein ETF und eine echte Teilmenge seiner Bestandteilaktien angewendet, demonstriert an SPY: Johansen einzeln mit mindestens 90 Prozent, dann ein gleichgewichtetes Long-only-Portfolio, das erneut kointegrieren muss.
- Weil die Gesamtrendite eines Futures gleich Spot-Rendite plus Rollrendite ist, wird die Rollrendite extrahiert, indem der Basiswert gekauft und der Future geshortet wird, wenn die Rollrendite negativ ist, also bei Contango, und umgekehrt bei positiver Rollrendite, also bei Backwardation.
- Das funktioniert, solange das Vorzeichen der Rollrendite nicht schnell wechselt, was es gewöhnlich nicht tut.
- Diese Arbitrage führt voraussichtlich zu einer kürzeren Haltedauer und einem niedrigeren Risiko als das Buy-and-Hold des Futures, weil dort lange gehalten werden muss, bis die laute Spot-Rendite sich herausmittelt.
- Den Basiswert zu kaufen und besonders zu shorten ist logistisch schwer, außer ein ETF hält das Asset; für viele Edelmetalle gibt es solche ETFs, und GLD besitzt physisches Gold und folgt dem Gold-Spotpreis sehr eng.
- Für andere physische Rohstoffe gibt es solche ETFs nicht, wegen der erheblichen Lagerkosten; eine ungenauere Form der Arbitrage nutzt ETFs von Rohstoffproduzenten, die oft mit dem Spotpreis kointegrieren.
- USO enthält nichts als die Frontmonatskontrakte von CL und ersetzt CL, weil XLE und CL verschiedene Schlusszeiten haben.
- Bei Contango von CL wird USO geshortet und XLE gekauft, bei Backwardation wird USO gekauft und XLE geshortet.
- Ein Kointegrationstest von Währungen ist nur sinnvoll, wenn eine Punktbewegung in beiden Reihen denselben Dollarwert hat. AUD gegen CAD wird deshalb auf AUD.USD und CAD.USD getestet.
- Eine Einheit einer Währung gegen USD ist so viele Dollar wert wie ihr Kurs, eine Einheit USD gegen eine andere Währung ist genau einen Dollar wert. Für einen Kreuzkurs wird die Log-Rendite verwendet, auch wenn die Heimatwährung EUR ist.
- Die Überschussrendite eines über Nacht gehaltenen Kreuzkurses addiert log(1 + Zins der Basis) minus log(1 + Zins der Kurswährung) zur Log-Preisänderung.
- Kalenderspreads sind die Stelle, an der Mean Reversion bei Futures die Ausnahme ist. Der 12-Monats-Spread von CL ist im ADF-Test mit 99 Prozent stationär, hat eine Halbwertszeit von etwa 36 Tagen und erzielt ungehebelt 8,3 Prozent annualisierte Rendite bei einer Sharpe Ratio von 1,3.
- Im Allgemeinen mean-reverten Kalenderspreads nicht, weil die Rollrendite das Signal vom gemeinsamen Spot abkoppelt.
- Als weitere Ausnahme nennt der Text den Spread aus Volatilitäts-Future und Aktienindex-Future.

## Voraussetzungen

- Die meisten einfacheren Spezialplattformen können übliche Statistical-Arbitrage- oder Portfolio-Strategien mit vielen Symbolen nicht verarbeiten.
- Oft brauchen schon einfache Pairs-Trading-Strategien besondere Module.
- Open-Source-IDEs haben diese Einschränkung nicht, und eigenständige Programme ebenso wenig.
- Eine Punktbewegung in einem Währungspaar muss denselben Dollarwert haben wie eine Punktbewegung in einem anderen, sonst sind Kointegrationstest und Portfoliorendite sinnlos.

## Anwendung im Trading

- VX eignet sich zur Extraktion der Rollrendite, weil diese bis minus 50 Prozent annualisiert betragen kann und die Korrelation der Tagesrenditen mit ES minus 75 Prozent erreicht, während die Rollrendite von ES mit etwa 1 Prozent annualisiert unbedeutend ist.
- Ein Korb aus Optionen, der den VIX nachbildet, ist sehr teuer, und kein ETF-Anbieter tut das; gesucht wird nur ein Instrument mit hoher Korrelation oder Antikorrelation zur Spot-Rendite, und SPY passt, gehandelt wird aber der leichter handelbare ES.
- Nach Simon und Campasano 2012 wird bei Contango, wenn der VX-Frontkontrakt den VIX um 0,1 Punkte mal der Zahl der Handelstage bis zum Settlement übersteigt, 0,3906 Frontkontrakte VX und ein Frontkontrakt ES geshortet und einen Tag gehalten.
- Bei Backwardation um dieselbe Schwelle werden 0,3906 Frontkontrakte VX und ein Frontkontrakt ES gekauft und einen Tag gehalten.
- Liegt der Frontkontrakt über dem Spot, ist die Rollrendite negativ; die Preisdifferenz zwischen VIX und VX geteilt durch die Zeit bis zur Fälligkeit ist die Rollrendite, und VX wird gekauft, wenn die Rollrendite positiv ist.
- Die Steigung der Log-Forward-Kurve aus Gleichung 5.7 wird nicht verwendet, weil diese Gleichung für VX nicht gilt und die VX-Forward-Preise nicht auf einer Geraden liegen.
- Die Hedge Ratio folgt der Preisregression in Gleichung 5.11, nicht der Renditeregression des Originalpapiers, und das Settlement ist der Tag nach dem Verfall der Kontrakte.
- Vom 29. Juli 2010 bis zum 7. Mai 2012, nicht verwendet für die Hedge Ratio, beträgt die annualisierte Rendite 6,9 Prozent bei einer Sharpe Ratio von 1.
- Im SPY-Beispiel des Trainingsjahrs 2007 kointegrieren 98 Aktien einzeln mit mindestens 90 Prozent. Das gleichgewichtige Long-only-Portfolio wird auf Log-Preisen erneut geprüft, weil täglich auf konstantes Kapital rebalanciert wird, und kointegriert mit besser als 95 Prozent.
- Die lineare Mean Reversion auf dem Testzeitraum 2. Januar 2008 bis 9. April 2012, Lookback 5 im Rückblick, erzielt 4,5 Prozent annualisierte Rendite und eine Sharpe Ratio von 1,3. Ohne periodisches Neutraining fällt die Performance.
- Die Trace-Statistik 15,869 überschreitet den 95-Prozent-Wert 15,494, nicht den 99-Prozent-Wert 19,935. Die Eigenwert-Statistik 9,671 bleibt unter dem 90-Prozent-Wert 12,297. Genommen wird von zwei Relationen die mit dem größten Eigenwert.
- Weil Log-Preise getestet wurden, sind die Hedge Ratios Dollarkapital. Jede Aktie bekommt dasselbe Gewicht, SPY ein anderes.
- Die bekannte Johansen-Implementierung nimmt höchstens 12 Symbole. Eigenvektoren über das ganze Universum mischen zudem Long- und Short-Aktien, sodass ein Long-only-Korb nicht sauber gegen Short-SPY steht und einzelne Titel doppelt short werden können.
- Alternativ minimieren ein genetischer Algorithmus oder Simulated Annealing den durchschnittlichen absoluten Abstand zur SPY-Reihe unter der Nebenbedingung positiver Hedge Ratios.
- Die Leerverkaufsbeschränkung wiegt hier weniger schwer, weil der Korb mit etwa 98 Aktien diversifiziert ist. Fallen wenige Titel weg, bleibt die Wirkung begrenzt.
- Das parameterfreie lineare Long-Short-Modell auf relativen Tagesrenditen ist nahezu dollarneutral, setzt jeden Tag 1 Dollar Brutto ein und erzielt auf dem S&P 500 13,7 Prozent annualisierte Rendite bei einer Sharpe Ratio von 1,3, 2008 sogar 30 Prozent.
- Ab Anfang 2008 ist dieser Test echt out of sample, die Veröffentlichung war 2007. Die Intraday-Fassung erreicht 73 Prozent und eine Sharpe Ratio von 4,7, bei verdoppelten Kosten und Signalrauschen.
- Als Ranggröße neben der relativen Rendite dient das Kurs-Gewinn-Verhältnis, damit eine durch geänderte Gewinnschätzungen gedeckte Bewegung nicht als Umkehr geshortet wird.

## Regeln und Kriterien


## Risiken und Grenzen

- Paar- und andere Arbitragestrategien, deren Signale von Quote-Differenzen abhängen, sind gegen fehlerhafte Live-Bid-Ask-Quotes besonders empfindlich, weil die Differenz meist viel kleiner ist als die Quotes und der prozentuale Fehler im Spread dadurch viel größer wird.
- Ein Johansen-Test auf alle 500 Aktien plus SPY scheitert an einer Obergrenze von 12 Symbolen und daran, dass die Eigenvektoren meist Long- und Short-Aktien mischen und damit spezifisches Doppel-Short-Risiko erzeugen.
- Dieselbe Short-Sale-Beschränkung trifft auch diese Strategie, wirkt bei etwa 98 Titeln aber begrenzt, wenn wenige Aktien entfallen.
- Nach 2008 fiel die durchschnittliche Marktvolatilität, während plötzliche Ausbrüche häufiger wurden; Mean-Reversion-Strategien, die ein hohes, aber konstantes Volatilitätsniveau brauchen, verloren dadurch allgemein an Gewinn.
- Die Regulation NMS im Juli 2007 trug zum drastischen Rückgang der durchschnittlichen Trade-Größen und zum Verschwinden des NYSE-Blocktrades bei.
- Beim Handel von Paaren oder anderen Arbitrage-Strategien sind fehlerhafte Bid- und Ask-Quotes besonders gefährlich, weil die Signale auf kleinen Quote-Differenzen beruhen und ein kleiner Fehler den Spread prozentual stark verfälscht.
- Im Beispiel steigt ein wahrer Spread von 5 Dollar durch einen um 1 Dollar falschen Ask auf 6 Dollar, also um 20 Prozent, und kann eine fehlerhafte Order zum Kauf von X und Verkauf von Y auslösen.
- Die Backtests lassen Transaktionskosten weg, weil sie von Ausführung und Universum abhängen, und sie nutzen Aktien mit Survivorship Bias sowie konsolidierte statt primärer Eröffnungen und Schlüsse, sodass MOO- und MOC-Fills schlechter ausfallen als berichtet.

## Beispiele

- Vom 1. Januar 2007 bis 31. Dezember 2007 kointegrieren 98 Aktien einzeln mit SPY; das Long-only-Portfolio kointegriert mit besser als 95 Prozent, und der Test vom 2. Januar 2008 bis 9. April 2012 liefert eine APR von 4,5 Prozent und eine Sharpe Ratio von 1,3.
- Die Rollrendite der Gold-Futures beträgt von Dezember 1982 bis Mai 2004 minus 4,9 Prozent annualisiert.
- Long GLD und short GC erzielt vom 3. August 2007 bis zum 2. August 2010 1,9 Prozent annualisiert bei einem maximalen Drawdown von 0,8 Prozent.
- Ein Hebel von 5 oder 6 wirkt darauf attraktiv, ist es aber nicht, weil die Finanzierungskosten von GLD nicht weit von diesen 1,9 Prozent entfernt liegen und die Überschussrendite nahe null ist.
- GC wird um 13:30 Uhr ET festgestellt, GLD um 16:00 Uhr ET; die Signale kommen allein aus den GC-Schlusskursen, deshalb ist die Asynchronität hier folgenlos.
- XLE gegen USO erzielt vom 26. April 2006 bis zum 9. April 2012 eine annualisierte Rendite von 16 Prozent bei einer Sharpe Ratio von etwa 1.
- AUD.USD gegen CAD.USD mit Johansen-Gewichten erzielt 11 Prozent annualisierte Rendite und eine Sharpe Ratio von 1,6. AUD.CAD mit Rollover erzielt 6,2 Prozent und 0,54.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 33–51 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-003-p033-p051|S. 33–51]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 71–75 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-005-p071-p075|S. 71–75]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 95–98 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-007-p095-p098|S. 95–98]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 99–118 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-008-p099-p118|S. 99–118]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 119–138 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-009-p119-p138|S. 119–138]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 144–163 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-011-p144-p163|S. 144–163]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 199–214 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-015-p199-p214|S. 199–214]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 457–476 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-025-p457-p476|S. 457–476]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 476–495 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-026-p476-p495|S. 476–495]]

## Verwandte Themen
