---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/18 - Positionsmanagement/18 - Positionsmanagement|18 - Positionsmanagement]]"
weitere_hauptthemen: []
unterthema: "Positionsgröße"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Leverage


## Kurzdefinition

- Leverage misst die Verschuldung, die nötig ist, um die berichtete Performance zu erreichen.

## Kernaussagen

- Die Kelly-Formel bestimmt den optimalen Hebel und die Kapitalallokation bei der Abwägung von Renditen und Risiken.
- Unterhebeln ist immer besser als Überhebeln, besonders bei der Verwaltung fremden Geldes.
- Der optimale Hebel wird für realistische Situationen gesucht, in denen keine Gauß-Verteilung der Renditen mehr angenommen werden kann.
- Praktische Erfahrung mit schwarzen Schwänen, Constant Proportion Portfolio Insurance und Stop-Losses mildert die Anwendung der Kelly-Formel.
- Der einsetzbare Hebel bei Währungen ist viel höher als beim Handel der entsprechenden Aktienindex-ETF-Paare; das ist zweischneidig.
- Die lineare Mean-Reversion auf dem CL-Kalender-Spread hat eine ungehebelte APR von 8,3 Prozent und eine Sharpe Ratio von 1,3 vom 2. Januar 2008 bis 13. August 2012.
- Die Tagesrendite dieses Spreads ist der Tages-P&L geteilt durch 2, weil zwei Kontrakte gehalten werden.
- Umsichtiger Hebeleinsatz ist das Schlüsselkonzept dieses Risikomanagements und wird über Kelly oder numerische Maximierung der zusammengesetzten Wachstumsrate bestimmt.
- Hebel null vermeidet jedes Risiko und erzeugt keine Rendite.
- Alle drei Methoden unterstellen, dass die künftige Renditeverteilung des Marktes der vergangenen entspricht; das ist meist falsch und dennoch das Beste quantitativer Modelle.
- Restriktiver wird dasselbe für die Strategie selbst unterstellt, am restriktivsten eine Gauß-Verteilung der Strategierenditen.
- Ein Hebel mit maximalem Drawdown von minus 100 Prozent ist nicht optimal, weil die Wachstumsrate dann ebenfalls minus 100 Prozent ist.
- Optimaler Hebel heißt, dass das Eigenkapital historisch nie null erreicht; ein kleinerer erlaubter Maximal-Drawdown ist eine zusätzliche Nebenbedingung.
- Der Hebel soll konstant bleiben, mit oder ohne diese Drawdown-Nebenbedingung.
- Falscher Hebeleinsatz kann beeinträchtigen, dass Arbitrage die Märkte zur Effizienz treibt. Selbst wer über- und unterbewertete Papiere zutreffend erkennt, kann durch zu viel Hebel ausgelöscht werden.
- Für günstige Wetten, also Spekulationen mit positiver Erwartung, gibt es einen optimalen Hebel. Wird er überschritten, steigt die Ruinwahrscheinlichkeit trotz der positiven Erwartung.
- Im Münzbeispiel ist der optimale Einsatzanteil 0,25. Ein Arbitrageur mit guter Information und zu viel Hebel entspricht einem höheren Anteil; bei 0,58 ist der Verlust des gesamten Kapitals wahrscheinlich, trotz günstiger Erwartung.
- Long Term Capital Management hatte die erkannten Fehlbewertungen im Herbst 1998 letztlich auf der richtigen Seite, doch der Überhebel nahm dem Fonds die Ausdauer, die Positionen durch eine kurze Phase noch größerer Fehlbewertung zu halten.
- Der Kollaps des Fonds hätte beinahe den gesamten Finanzmarkt mitgerissen.

## Funktionsweise

- Ein Portfolio, das den MSCI US REIT Index RMZ mit konstantem Hebel 3 besonders zum Marktschluss abbilden soll, muss nach einem starken Tagesverlust Aktien über das Portfolio hinweg verkaufen.
- Steigt der RMZ an diesem Tag, müssen die Positionen durch Käufe erhöht werden.
- Der Sponsor eines dreifach gehebelten ETF wie DRN, dessen Eigenkapital über 100 Millionen Dollar liegt, verkauft die Komponenten bei negativer Portfoliorendite und kauft bei positiver, nahe dem Schluss.
- Eine große Indexbewegung erzeugt Momentum in derselben Richtung für gehebelte Long- und für Short-ETFs.
- Fällt das Eigenkapital eines Short-ETF bei positivem Index, muss der Sponsor Shorts reduzieren und damit Aktien kaufen, ebenso wie der Long-ETF.
- Konstanter Hebel zwingt nach positivem Gewinn und Verlust zum Nachkaufen und nach negativem zum Verkauf in den Verlust.
- Start bei 100.000 Dollar Eigenkapital und Hebel 5 bedeutet 500.000 Dollar Portfoliomarktwert.
- Nach einem Tagesverlust von 10.000 Dollar auf 90.000 Dollar Eigenkapital und 490.000 Dollar Marktwert müssen weitere 40.000 Dollar liquidiert werden, damit der Marktwert 5 mal 90.000 gleich 450.000 Dollar beträgt.
- Nach einem Gewinn von 20.000 Dollar am nächsten Tag soll der Marktwert 5 mal 110.000 gleich 550.000 Dollar sein; vom dann aktuellen 470.000 Dollar müssen 80.000 Dollar Wertpapiere ergänzt werden.

## Voraussetzungen


## Anwendung im Trading

- Gehebelte ETFs dienen als Handelsinstrument, um den Effekt zu vergrößern; das Momentum betrifft auch die Renditen ungehebelter ETFs wie SPY nahe dem Schluss.
- Gekauft wird DRN, wenn die Rendite vom Vortagesschluss bis 15 Minuten vor Schluss über 2 Prozent liegt, verkauft wird bei unter minus 2 Prozent, der Ausstieg liegt am Schluss.
- Die Rendite dieser Strategie sollte steigen, wenn das aggregierte Vermögen aller gehebelten ETFs steigt.
- Die Intraday-Strategie nach Gewinnmeldungen lässt sich mindestens vierfach hebeln und kommt dann auf eine annualisierte Durchschnittsrendite nahe 27 Prozent.
- Bei einem großen bevorstehenden Ereignis ist zu entscheiden, ob dem Modell wie im Backtest getraut, der Hebel gesenkt oder das Modell vorübergehend abgeschaltet wird.
- Hat das Modell frühere Stressperioden im Backtest überstanden, senkt der Autor den Hebel vor einer kommenden Krise nicht.
- Besser ist, in guten Zeiten mit einem konservativeren Hebel zu starten, als ihn in schlechten senken zu müssen.

## Regeln und Kriterien

- Kommt Leverage vor, sind ihm Kosten zuzuordnen.
- Eine Messgröße ist das Verhältnis der durchschnittlichen Dollarpositionsgröße zum durchschnittlichen verwalteten Vermögen.
- Bei mehreren Strategien und einem Fmax weit unter der Kelly-Summe ist oft die Konzentration auf die Strategie mit dem höchsten mittleren Excess Return besser als proportionales Skalieren.
- Die Key Points nennen Half-Kelly für langfristiges Vermögenswachstum, Monte Carlo statt Kelly bei Fat Tails und CPPI, wenn ein Maximal-Drawdown eingehalten und die Wachstumsrate möglichst hoch sein soll.

## Risiken und Grenzen

- Die scheinbar hohe Stetigkeit von Mean-Reversion-Strategien verleitet Trader zu Überkonfidenz und in der Folge zu zu viel Leverage (Dever, 2011); das Beispiel ist Long Term Capital Management.
- Bricht die Strategie plötzlich auseinander, oft aus einem erst im Nachhinein erkennbaren fundamentalen Grund, geschieht das häufig beim maximalen Leverage nach einer ungebrochenen Serie von Erfolgen.
- Der seltene Verlust ist dann oft sehr schmerzhaft und manchmal katastrophal.
- Dieser erzwungene Umsatz hat signifikanten Market Impact und erzeugt Momentum; eine aktuellere Analyse stammt von Rodier, Haryanto, Shum und Hejazi (2012).
- Große Zuflüsse in gehebelte Long-ETFs erzeugen positives Momentum der Basiswerte, große Zuflüsse in inverse ETFs negatives Momentum.
- Theoretisch könnten Verkäufe der Long-ETFs an einem starken Aufwärtstag das Momentum neutralisieren; die Backtests zeigen, dass das nicht oft geschah.
- Viele Analysten sehen in diesem Verkauf in Verluste eine Ansteckungsursache von Finanzkrisen, genannt für den Quant-Fonds-Einbruch im August 2007 (Khandani und Lo, 2007).
- Halten viele Fonds ähnliche Positionen, kann die Liquidation eines Fonds wegen einer unabhängigen Strategie Verluste bei den anderen auslösen, die ebenfalls liquidieren: eine Tragödie der Allmende.
- Half-Kelly und die Lesart von Kelly als Obergrenze begrenzen die Ruin-Folge eines überschätzten Hebels.
- Die 3-fach-ETFs BGU und TNA liegen über dem Kelly-Hebel von etwa 1,8 der Russell-Indizes; ihr Nettoinventarwert kann auf null gehen.
- Unknown Unknowns schaden, nicht die Known Unknowns; die Modelle lassen sich nicht abschalten, bevor die Unknown Unknowns eintreten.

## Beispiele

- Der Handel in DRN liefert vom 12. Oktober 2011 bis 25. Oktober 2012 eine APR von 15 Prozent und eine Sharpe Ratio von 1,8.
- Ende Januar 2009 betrug das gesamte verwaltete Vermögen gehebelter ETFs einschließlich Long- und Short-Fonds 19 Milliarden Dollar (Cheng und Madhavan, 2009).
- Dieselben Autoren schätzen, dass eine Bewegung des SPX um 1 Prozent Käufe oder Verkäufe von Aktien im Umfang von etwa 17 Prozent des Market-on-Close-Volumens erzwingt.
- Im Monte-Carlo-Beispiel liegt das optimale f bei 19, nahe dem Kelly-Wert 18,4; ab 1 geteilt durch 0,0331 gleich 30,2 droht wegen der schlechtesten Rendite von minus 0,0331 der Ruin, und bei f gleich 31 ist die Wachstumsrate minus 1.
- Für einen Drawdown von etwa 0,5 musste der Simulationshebel von 19,2 um den Faktor 7 auf etwa 2,7 sinken.
- CPPI hebelt nur das Subkonto mit dem Anteil D mit dem Kelly-Hebel und lässt 1 minus D in Cash.

## Unterschiedliche Quellenpositionen

- Kelly je Strategie enthebelt Underperformer schnell und ist nach seiner Erfahrung praktischer als die Allokation über alle Strategien.
- Die Mathematik weist die Allokation über alle Strategien als optimal aus, solange erwartete Renditen und Volatilitäten unverändert bleiben.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 173–186 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-013-p173-p186|S. 173–186]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 343–362 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-019-p343-p362|S. 343–362]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 153–172 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-012-p153-p172|S. 153–172]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 251–270 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-018-p251-p270|S. 251–270]]

## Verwandte Themen
