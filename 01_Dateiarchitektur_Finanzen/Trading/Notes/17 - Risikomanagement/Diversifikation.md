---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/17 - Risikomanagement/17 - Risikomanagement|17 - Risikomanagement]]"
weitere_hauptthemen: []
unterthema: "Portfoliorisiko"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Diversifikation


## Kurzdefinition

- Diversifikation nur nach Assetklasse, Sektor und Einzeltitel genügt nicht; nötig ist zusätzlich Diversifikation nach Timeframe.
- Timeframe-Diversifikation setzt die Analyse in Long- und Short-Ideen um und nicht nur in mögliche Long-Positionen.
- Ein diversifiziertes Portfolio berücksichtigt die Korrelationen zwischen den Anlagen, statt alles in die Titel mit den höchsten erwarteten Renditen zu legen.

## Kernaussagen

- Timeframe-Diversifikation heißt, kurze, mittlere und lange Laufzeiten zugleich zu halten, wie im Fixed Income üblich. Für Aktieninvestoren und Berater gilt dasselbe.
- Gelingt sie, wirkt sie als Hedge gegen große Liquidationswellen, Short-Eindeckungsrallyes und andere kurze, nachrichtengetriebene Bewegungen, die den Markt an den Bruchpunkt bringen.
- Auch in einem langfristigen Trend können Gegenbewegungen leicht 5 bis 10 Prozent zurücknehmen.
- Sektoren, Branchen und Einzeltitel laufen häufiger gegenläufig oder rotieren, als dass sie sich gemeinsam bewegen.
- Zur Streuung gehört, Titel oder Märkte zu shorten, die voraussichtlich auseinanderlaufen.
- Nur in eine Richtung positioniert zu sein ist riskant, weil Märkte abrupt drehen können.
- Markowitz' Fluch besagt, dass mit stärkerer Korrelation der Anlagen der Bedarf an Diversifikation steigt, die Lösungen aber instabiler werden.
- Der Nutzen der Diversifikation wird oft durch Schätzfehler mehr als aufgezehrt.
- Hierarchical Risk Parity baut ein diversifiziertes Portfolio aus der Information der Kovarianzmatrix und braucht dafür keine invertierbare Matrix.
- Eine Baumstruktur verbindet N Knoten mit nur N minus 1 Kanten, sodass Gewichte nur unter Peers auf den Hierarchieebenen neu verteilt werden.
- Die Gewichte laufen von oben nach unten, analog zum Aufbau vieler Manager von der Assetklasse über Sektoren zu Einzeltiteln.
- Hierarchical Risk Parity kompromittiert zwischen Streuung über alle Anlagen und Streuung über Cluster auf mehreren Hierarchieebenen.
- Dieser Kompromiss aus beiden Streuungen schützt besser gegen gemeinsame und gegen idiosynkratische Schocks als CLA oder das Inverse-Varianz-Portfolio.
- Exakte analytische Lösungen können deutlich schlechter abschneiden als näherungsweise Machine-Learning-Lösungen.
- De Miguel und Koautoren (2009) zeigen, dass naive gleichgewichtete Portfolios Mean-Variance- und risikobasierte Optimierung außer Stichprobe schlagen.
- Die große Zahl möglicher Aktienpaare macht Diversifikation leicht, doch das Gesetz der großen Zahlen hilft nur, wenn die erwartete Out-of-Sample-Rendite eines einzelnen Paars positiv ist; der Autor hat das bei Aktienpaaren nicht gefunden.
- Die kleinen Gewinne der guten Paare wurden vollständig von den großen Verlusten der schlecht gelaufenen Paare überwogen.
- Weil die meisten Futures und Währungen Momentum zeigen, erlauben Momentum-Strategien eine echte Risikostreuung über verschiedene Assetklassen und Länder.
- Momentum-Strategien zu einem Portfolio aus Mean-Reversion-Strategien hinzuzufügen ergibt höhere Sharpe Ratios und kleinere Drawdowns als jeder Strategietyp allein.
- Theoretisch macht die große Zahl der Aktien Diversifikation leicht, wenn Paare aus einem Sektor wegen gemeinsamer ökonomischer Faktoren kointegrieren.
- Ein Portfolio vieler Aktienpaare hilft nur, wenn die erwartete Out-of-Sample-Rendite des einzelnen Paares positiv ist. Der Autor hat das bei Aktienpaaren nicht gefunden: die kleinen Gewinne der guten Paare werden von den großen Verlusten der entgleisten Paare aufgezehrt.
- Das SPY-Bestandteilportfolio ist mit etwa 98 Aktien breit gestreut. Müssen wenige Titel wegen einer Leerverkaufsbeschränkung entfallen, bleibt die Wirkung begrenzt.
- Bei querschnittlicher Mean Reversion ist nicht jede einzelne Aktie profitabel, manche dienen als Hedge. Gewinne entstehen nur über alle Aktien zusammen.
- Buy-on-Gap handelt an einem Tag nur wenige Aktien und hat deshalb keine große Kapazität. Die reine Long-Fassung erschwert zusätzlich das Risikomanagement.
- Eine Variante kauft mehr Aktien, begrenzt aber die Zahl innerhalb desselben Sektors. Eine andere ist long die Aktien und short Aktienindex-Futures.
- Weil die meisten Futures und Währungen Momentum zeigen, lassen sich Risiken wirklich über Assetklassen und Länder streuen.
- Momentum-Strategien zusätzlich zu einem Portfolio aus Mean-Reversion-Strategien erzeugen höhere Sharpe Ratios und kleinere Drawdowns als jeder Typ für sich.
- Die Kelly-Allokation über das Eigenkapital des Gesamtportfolios lässt gute Strategien schlechte kurzfristig subventionieren; Kelly auf jede Strategie einzeln enthebelt die zuletzt schlechten schnell.
- Mathematisch ist die Gesamtallokation optimal, aber nur wenn die erwarteten Renditen und Volatilitäten unverändert bleiben, was nach einem schweren Drawdown zweifelhaft ist.
- Die Erfahrung des Autors ist, dass die einzelne Anwendung praktischer ist, damit jede underperformende Strategie schnell eingeht.
- Bei zufälligen Sprüngen wird der Markt unvollständig, und die üblichen Hedge-Argumente reichen zur Optionsbewertung nicht.
- Ist die Zahl der verfügbaren Titel sehr groß, ist das Risiko plötzlicher Sprünge diversifizierbar; der Markt zahlt dann über den risikofreien Zins hinaus keine Risikoprämie für das Tragen dieses Risikos.
- Unter dieser Diversifizierbarkeit lässt sich eine Optionspreisformel ableiten, die nicht von der Risikoeinstellung abhängt.
- Alternativ kann man zu einem gegebenen Satz von Risikoprämien ein risikoneutrales Maß P* wählen und den Preis darunter berechnen.
- Der Value at Risk erfüllt die Subadditivität nicht: das Risikomaß zweier Portfolios nach dem Zusammenlegen muss nicht kleiner oder gleich der Summe der Risikomaße vor dem Zusammenlegen sein.
- Die Kovarianzstruktur eines Renditevektors ist für die Portfolioauswahl wichtig. Die Hauptkomponentenanalyse erklärt diese Struktur durch wenige Linearkombinationen und senkt damit die Dimension.
- Ein Eigenwert null der Kovarianz- oder Korrelationsmatrix bedeutet eine exakte lineare Beziehung zwischen den Komponenten. Ist der kleinste Eigenwert null, ist die zugehörige Hauptkomponente konstant, und der Zufallsvektor enthält nur k−1 zufällige Größen.
- Für fünf monatliche Aktienrenditen von IBM, Hewlett-Packard, Intel, J.P. Morgan Chase und Bank of America erklären die ersten beiden Hauptkomponenten der Korrelationsmatrix etwa 74 Prozent der Gesamtvariabilität. Die erste ist eine ungefähr gleich gewichtete Marktkomponente, die zweite der Unterschied zwischen Technologie und Finanzwerten.

## Funktionsweise

- Hierarchical Risk Parity arbeitet in drei Stufen: Baum-Clustering, Quasi-Diagonalisierung und rekursive Bisektion.
- Hierarchical Risk Parity konvergiert günstigstenfalls in deterministischer logarithmischer Zeit und schlechtestenfalls in deterministischer linearer Zeit.
- RiskMetrics bildet den VaR zweier Positionen als Wurzel aus VaR1 zum Quadrat plus VaR2 zum Quadrat plus 2 mal ρ12 mal VaR1 mal VaR2, wobei ρ12 der Kreuzkorrelationskoeffizient der beiden Renditen ist.
- Für m Instrumente ist der Gesamt-VaR die Wurzel aus der Summe der quadrierten Einzel-VaR plus der Summe 2 mal ρij mal VaRi mal VaRj über alle Paare i < j.

## Voraussetzungen

- Die Formel für den gemeinsamen VaR setzt voraus, dass die Logrenditen der beteiligten Anlagen gemeinsam multivariat normalverteilt sind mit Mittelwert null und Kovarianzmatrix Σ t+1.

## Anwendung im Trading

- Eine praktische Anwendung ist die Allokation über mehrere Machine-Learning-Strategien.
- Seit Bridgewater in den 1990er-Jahren Risk Parity einführte, folgen große Asset Manager dem Ansatz mit zusammen über 500 Milliarden Dollar.
- Wegen ihres hohen Hebels sollten diese Fonds von einer stabileren Risk-Parity-Allokation profitieren, mit besserer risikoadjustierter Rendite und geringeren Rebalancing-Kosten.

## Regeln und Kriterien


## Risiken und Grenzen

- Korrelationsmatrizen behandeln jede Anlage als Ersatz für jede andere und lassen Gewichte deshalb frei in unbeabsichtigte Richtungen laufen.
- Im Zahlenbeispiel konzentriert CLA 92,66 Prozent auf die fünf größten Positionen, Hierarchical Risk Parity nur 62,57 Prozent.
- Die Standardabweichungen liegen dabei nahe beieinander, 0,4640 gegen 0,4486, CLA streicht aber einen großen Teil des Universums für eine kleine Risikoreduktion.
- Das CLA-Portfolio ist trügerisch diversifiziert, weil Stress in den fünf größten Positionen stärker durchschlägt als bei Hierarchical Risk Parity.
- Das Inverse-Varianz-Portfolio verteilt die Gewichte gleichmäßig, ignoriert die Korrelationsstruktur und ist dadurch anfällig für systemische Schocks.

## Beispiele

- Eine angegebene Mischung ist etwa 70 Prozent long und 30 Prozent short und wird auf dieses Verhältnis zurückgeführt, sobald die Shorts 25 oder 35 Prozent erreichen.
- Aktien lassen sich nach Liquidität, Größe, Branche und Region gruppieren, und innerhalb einer Gruppe konkurrieren sie um die Allokation.
- Die Outperformance von Hierarchical Risk Parity außer Stichprobe wird bei größerem Universum, mehr Schocks, stärkerer Korrelation oder Rebalancing-Kosten noch deutlicher.
- Das mit SPY gehandelte Aktienportfolio umfasst etwa 98 Titel; müssen wenige wegen der Short-Sale-Beschränkung entfernt werden, bleibt die Wirkung begrenzt.
- Eine Variante des Buy-on-Gap kauft mehr Aktien, begrenzt aber die Zahl der Titel innerhalb desselben Sektors.

## Unterschiedliche Quellenpositionen

- Kolanovic und Koautoren (2017) finden Hierarchical-Risk-Parity-Portfolios wirklich diversifiziert, mit mehr unkorrelierten Exposures und weniger extremen Gewichten und Risikoallokationen.
- Raffinot (2017) findet Portfolios aus hierarchischem Clustering robust, wirklich diversifiziert und risikoadjustiert statistisch besser als gängige Optimierungsverfahren.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Markets in Profile_ Profiting from the Auction Process.pdf, S. 1–20 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-001-p001-p020|S. 1–20]]
- Markets in Profile_ Profiting from the Auction Process.pdf, S. 214–225 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-016-p214-p225|S. 214–225]]
- Advances in Financial Machine Learning.pdf, S. 248–267 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-014-p248-p267|S. 248–267]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 99–118 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-008-p099-p118|S. 99–118]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 163–165 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-012-p163-p165|S. 163–165]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 199–214 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-015-p199-p214|S. 199–214]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 324–343 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-018-p324-p343|S. 324–343]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 343–362 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-019-p343-p362|S. 343–362]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 495–514 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-027-p495-p514|S. 495–514]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 514–533 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-028-p514-p533|S. 514–533]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 248–267 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-014-p248-p267|S. 248–267]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 267–286 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-015-p267-p286|S. 267–286]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 286–305 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-016-p286-p305|S. 286–305]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 305–324 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-017-p305-p324|S. 305–324]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 400–419 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-022-p400-p419|S. 400–419]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 419–438 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-023-p419-p438|S. 419–438]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 438–457 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-024-p438-p457|S. 438–457]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 457–476 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-025-p457-p476|S. 457–476]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 609–628 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-033-p609-p628|S. 609–628]]

## Verwandte Themen

- Hedging
- Rebalancing
