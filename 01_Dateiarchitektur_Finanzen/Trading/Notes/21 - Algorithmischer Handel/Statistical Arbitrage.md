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
aktualisiert: 2026-10-30
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

## Regeln und Kriterien


## Risiken und Grenzen

- Paar- und andere Arbitragestrategien, deren Signale von Quote-Differenzen abhängen, sind gegen fehlerhafte Live-Bid-Ask-Quotes besonders empfindlich, weil die Differenz meist viel kleiner ist als die Quotes und der prozentuale Fehler im Spread dadurch viel größer wird.
- Ein Johansen-Test auf alle 500 Aktien plus SPY scheitert an einer Obergrenze von 12 Symbolen und daran, dass die Eigenvektoren meist Long- und Short-Aktien mischen und damit spezifisches Doppel-Short-Risiko erzeugen.
- Dieselbe Short-Sale-Beschränkung trifft auch diese Strategie, wirkt bei etwa 98 Titeln aber begrenzt, wenn wenige Aktien entfallen.

## Beispiele

- Vom 1. Januar 2007 bis 31. Dezember 2007 kointegrieren 98 Aktien einzeln mit SPY; das Long-only-Portfolio kointegriert mit besser als 95 Prozent, und der Test vom 2. Januar 2008 bis 9. April 2012 liefert eine APR von 4,5 Prozent und eine Sharpe Ratio von 1,3.
- Die Rollrendite der Gold-Futures beträgt von Dezember 1982 bis Mai 2004 minus 4,9 Prozent annualisiert.
- Long GLD und short GC erzielt vom 3. August 2007 bis zum 2. August 2010 1,9 Prozent annualisiert bei einem maximalen Drawdown von 0,8 Prozent.
- Ein Hebel von 5 oder 6 wirkt darauf attraktiv, ist es aber nicht, weil die Finanzierungskosten von GLD nicht weit von diesen 1,9 Prozent entfernt liegen und die Überschussrendite nahe null ist.
- GC wird um 13:30 Uhr ET festgestellt, GLD um 16:00 Uhr ET; die Signale kommen allein aus den GC-Schlusskursen, deshalb ist die Asynchronität hier folgenlos.
- XLE gegen USO erzielt vom 26. April 2006 bis zum 9. April 2012 eine annualisierte Rendite von 16 Prozent bei einer Sharpe Ratio von etwa 1.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]

## Verwandte Themen
