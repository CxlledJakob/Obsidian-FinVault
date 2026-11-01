---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/17 - Risikomanagement/17 - Risikomanagement|17 - Risikomanagement]]"
weitere_hauptthemen: []
unterthema: "Verlustrisiko"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-01
---

# Maximum Drawdown


## Kurzdefinition

- Ein Drawdown ist der maximale Verlust zwischen zwei aufeinanderfolgenden Höchstständen.

## Kernaussagen

- Manager fremden Geldes bekommen oft vorgegeben, dass der Betrag des Drawdowns, gerechnet vom historischen Höchststand, ein Maximum nie überschreitet.
- Ein Hebel, dessen maximaler Drawdown minus 100 Prozent beträgt, kann nicht optimal sein, weil die zusammengesetzte Wachstumsrate dann ebenfalls minus 100 Prozent ist.
- Optimaler Hebel setzt voraus, dass das Eigenkapital historisch nie auf null fällt.
- Die Vorgabe ist eine zusätzliche Nebenbedingung und nicht durch einfaches Skalieren mit dem Verhältnis der Drawdowns umsetzbar.
- In Drawdowns ist es für erfolgreiche Trendfolger nicht ungewöhnlich, bis zu 30 Prozent ihres Handelskapitals zu verlieren.
- Diese Drawdowns treten auf, wenn die Märkte trendlos sind, und das ist die Mehrheit der Zeit.
- Die meisten Trendfolge-Systeme erzeugen in 50 bis 65 Prozent der Fälle unprofitable Signale. Das sind die Phasen, in denen die Trendfolger den Drawdown erleben.
- Ein Drawdown von 20 Prozent braucht einen Gewinn von 25 Prozent, nur um wieder auf Breakeven zu kommen.
- Einen erheblichen Verlust aufzuholen verlangt viel.
- Große Positionen können große Verluste erzeugen, die sich sehr schwer erholen lassen.
- Ein großer Verlust ist emotional und finanziell sehr schwer aufzuholen. Deshalb bleiben erfolgreiche Trader bei einem relativ engen Stop und einem akzeptablen Verlust.
- Einen bedeutenden Verlust aufzuholen, erfordert viel.
- Die kumulierte P&L der linearen Mean-Reversion auf USD.CAD in Abbildung 2.3 bleibt trotz einer Halbwertszeit von etwa 115 Tagen positiv, zeigt aber einen großen Drawdown. Transaktionskosten sind nicht enthalten.
- Die TU-Momentum-Strategie hat vom 1. Juni 2004 bis zum 11. Mai 2012 einen maximalen Drawdown von 2,5 Prozent.
- Die auf die verzögerte Rollrendite umgestellte TU-Strategie senkt den maximalen Drawdown auf 1,1 Prozent, gemessen vom 2. Januar 2009 bis zum 13. August 2012.
- Tabelle 6.2 weist als maximalen Drawdown für BR minus 14,8 Prozent, für HG minus 24,0 Prozent und für TU minus 2,5 Prozent aus.
- Long GLD und short GC haben vom 3. August 2007 bis zum 2. August 2010 einen maximalen Drawdown von 0,8 Prozent.
- Der S&P DTI hat von Januar 1988 bis Dezember 2010 einen maximalen Drawdown von minus 16,6 Prozent, der S&P 500 im selben Zeitraum minus 50,96 Prozent.
- Zum Schreibzeitpunkt beträgt der Drawdown des S&P DTI seit dem 5. Dezember 2008 minus 25,9 Prozent.
- Nach dem Aktiencrash 1929 brauchte eine repräsentative Momentum-Strategie mehr als 30 Jahre, um ihr altes Equity-Hoch wieder zu erreichen.
- Ursache dieses Momentum-Crashs ist vor allem der starke Rebound der Short-Positionen nach einer Marktkrise.
- Querschnittliches Aktienmomentum verschwand nach dem Crash 2008 bis 2009 und wurde durch starke Mean Reversion ersetzt; wie lange dieses Regime anhält, ist offen.
- Eine einzelne Mean-Reversion-Position kann einen enormen Drawdown erzeugen, während der Verlust einer einzelnen Momentum-Position durch Zeitausstieg oder Stop-Loss begrenzt ist.
- Der kumulierte Verlust aufeinanderfolgender Verlustpositionen einer Momentum-Strategie kann trotzdem ruinös sein.
- Momentum zusätzlich zu Mean Reversion erzeugt kleinere Drawdowns als jeder Typ allein.
- Momentum-Strategien können in riskanten Ereignissen gedeihen, schnitten aber in deren Folge schlecht ab.
- Im Simulationsbeispiel beträgt der maximale Drawdown minus 0,999 beim unbeschränkten optimalen Hebel 19,2. Der halbe Hebel 9,6 lässt ihn bei minus 0,963; erst der Faktor 7, also etwa 2,7, senkt den Betrag auf etwa 0,5. Die Zahlen sind an die Zufallsreihe gebunden.
- Auf historischen Strategierenditen genügt der Faktor 1,5, also der Hebel 13, um den maximalen Drawdown unter minus 0,49 zu drücken.
- Die Schätzung auf simulierten Strategierenditen ähnelt dem Value-at-Risk und hat höhere Signifikanz, kann aber einen Drawdown enthalten, der in einer Million Jahren kaum eintritt, und lässt serielle Korrelationen aus, die den realen maximalen Drawdown senken können.
- Die historischen Strategierenditen erfassen diese Korrelationen und eine realistische Lebensdauer statt einer Million Jahre, enthalten aber zu wenig Daten für den Worst Case; ein Kompromisshebel liegt dazwischen.
- Bei CPPI ist der Drawdown des Gesamtkontos konstruktionsbedingt auf minus D begrenzt. In einer Simulation mit D gleich 0,5 bleibt er unter 0,5, während der Hebel f mal D ohne Stop-Loss einen Drawdown von 0,9 erreicht.
- Der aus der Simulation gesetzte Höchsthebel verhindert nur, dass der simulierte Drawdown das erlaubte Maximum überschreitet, nicht der künftige.

## Funktionsweise

- In Geldeinheiten ist er der Höchststand minus dem folgenden Tief.
- In Renditen ist er eins minus dem Verhältnis von Tief zu Höchststand.
- Verwendet werden nur Höchststände, auf die ein tieferer Stand folgt.
- Die Reihe kann aus Renditen oder aus einer Dollar-Performance berechnet werden.
- Diese Schätzung des maximalen Drawdowns beruht hier auf simulierten Strategierenditen, nicht auf den historischen Renditen des Backtests.
- Simulierte Reihen ähneln dem Value-at-Risk großer Banken und Hedgefonds und haben höhere statistische Signifikanz.
- Der Hebel an der simulierten Obergrenze verhindert nur den simulierten, nicht den künftigen Drawdown jenseits des Maximums.
- Nur CPPI oder ein Stop-Loss können garantieren, dass der künftige Drawdown das vorgegebene Maximum nicht überschreitet.
- Geht bei CPPI das Handels-Subkonto auf null, ist der erlaubte Drawdown minus D erreicht und die Strategie wird aufgegeben.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Als Kennzahl wird das 95-Prozent-Perzentil der Drawdown-Reihe berichtet.

## Risiken und Grenzen

- Mit einer einzigen Position einer Mean-Reversion-Strategie kann ein enormer Drawdown entstehen.
- Der aufsummierte Verlust aufeinanderfolgender verlierender Momentum-Positionen kann trotzdem in die Insolvenz führen.
- Momentum-Strategien zusätzlich zu einem Mean-Reversion-Portfolio erzeugen kleinere Drawdowns als jeder Strategietyp allein.
- Der simulierte Maximal-Drawdown kann so selten sein, dass er in einer Million Jahren kaum einmal eintritt; das ist eine genannte Ausrede von Fondsmanagern nach dem Scheitern.
- Simulierte Reihen verfehlen serielle Korrelationen, die den realen maximalen Drawdown senken können.
- Historische Drawdowns decken eine realistische Strategielebensdauer ab, enthalten aber zu wenig Daten für den Worst Case.
- CPPI und Stop-Loss verhindern einen Drawdown über das Overnight-Gap oder bei ausgesetztem Handel nicht.
- Für Mean Reversion soll der Stop-Loss größer sein als der maximale Intraday-Drawdown des Backtests.
- Bei endlicher Stichprobe unterliegen der maximale Drawdown und die Durchschnittsrendite dem Zufall; die Strategie kann in einer kleinen Stichprobe nur Glück gehabt haben.

## Beispiele

- Die lineare Mean-Reversion-Strategie auf USD.CAD hat trotz positiver Gesamt-P&L einen großen Drawdown.
- Die TU-Momentum-Strategie auf dem Nominalwert hat vom 1. Juni 2004 bis zum 11. Mai 2012 einen maximalen Drawdown von 2,5 Prozent; Hebel ist möglich, weil die Margin nur etwa 400 Dollar bei etwa 200.000 Dollar Nominalwert beträgt, der Drawdown bleibt aber zu tragen.
- In Tabelle 6.2 beträgt der maximale Drawdown minus 14,8 Prozent für BR, minus 24,0 Prozent für HG und minus 2,5 Prozent für TU.
- Das TU-Signal auf der annualisierten Rollrendite mit Schwelle 3 Prozent senkt den maximalen Drawdown vom 2. Januar 2009 bis zum 13. August 2012 auf 1,1 Prozent.
- Der S&P DTI hat nach Dever 2011 von Januar 1988 bis Dezember 2010 einen maximalen Drawdown von minus 16,6 Prozent, der S&P 500 im selben Zeitraum einen von minus 50,96 Prozent.
- Zum Zeitpunkt des Textes hat der S&P DTI seit dem 5. Dezember 2008 einen Drawdown von minus 25,9 Prozent.
- Long GLD und short GC hat vom 3. August 2007 bis zum 2. August 2010 einen maximalen Drawdown von 0,8 Prozent.
- Bei unbeschränktem f gleich 19,2 auf der simulierten Reihe ist der maximale Drawdown minus 0,999; bei f gleich 9,6 noch minus 0,963.
- Erst die Senkung um den Faktor 7 auf etwa 2,7 bringt den Betrag auf etwa 0,5; die Zahlen sind an die genaue simulierte Reihe gebunden und nicht exakt reproduzierbar.
- An den historischen Strategierenditen senkt der Faktor 1,5, also der Hebel 13, den maximalen Drawdown unter minus 0,49.
- Bei CPPI mit erlaubtem Drawdown minus 0,5 bleibt der Betrag unter 0,5; die Alternative ohne Stop-Loss erreicht 0,9 selbst mit halbem Optimalhebel.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 362–381 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-020-p362-p381|S. 362–381]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 153–172 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-012-p153-p172|S. 153–172]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 172–176 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-013-p172-p176|S. 172–176]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 14–33 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-002-p014-p033|S. 14–33]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 52–71 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-004-p052-p071|S. 52–71]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 144–163 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-011-p144-p163|S. 144–163]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 163–165 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-012-p163-p165|S. 163–165]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 180–199 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-014-p180-p199|S. 180–199]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 199–214 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-015-p199-p214|S. 199–214]]

## Verwandte Themen
