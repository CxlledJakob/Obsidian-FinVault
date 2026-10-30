---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Systementwicklung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Transaktionskostenmodell


## Kurzdefinition

- Im ETF-Trick bestehen die Transaktionskosten aus einem Kostensatz je Dollar Umsatz, den daraus berechneten Rebalancing- und Spread-Kosten sowie ansetzbaren Margin- und Finanzierungskosten.
- Die Transaktionskosten eines Assets sind die mit einem horizonspezifischen Faktor skalierte Quadratwurzel aus der absoluten Änderung seiner Kapitalallokation.

## Kernaussagen

- Tau i ist der Kostensatz für einen Dollar Umsatz in Instrument i.
- Im Beispiel beträgt dieser Satz einen Basispunkt.
- Die Rebalancing-Kosten werden nicht in den Investitionswert K eingebettet.
- Im Code lassen sich diese Kosten als negative Dividende behandeln.
- Kauf oder Verkauf einer Einheit des virtuellen ETF wird mit den Kosten belastet, die dem Kreuzen seines Bid-Ask-Spreads entsprechen.
- Transaktionskostenfunktionen sind nicht notwendig linear.
- Nichtlineare Kosten kann die Strategie anhand der angegebenen Größen simulieren.
- Die Carry-Variable kann neben Dividende oder Kupon auch Marginkosten oder Finanzierungskosten belasten.
- Die Serie eines investierten Dollars berücksichtigt den Implementation Shortfall.
- Die Kostenfunktion τ[ω] darf jede funktionale Form annehmen.
- Die als Beispiel verwendete Form ist ohne Beschränkung der Allgemeinheit die Summe der mit cn,h skalierten Quadratwurzeln der absoluten Allokationsänderungen.
- Im ersten Horizont ist τ1 die Summe von cn,1 mal der Quadratwurzel aus dem absoluten Abstand zwischen ωn,1 und der Anfangsallokation ω*n.
- Ab dem zweiten Horizont ist τh die Summe von cn,h mal der Quadratwurzel aus dem absoluten Abstand zwischen ωn,h und ωn,h−1.
- τ[ω] ist ein Vektor der Länge H.
- Der Vektor Ch = {cn,h} bestimmt die relativen Transaktionskosten der Assets und ändert sich mit dem Horizont h.
- Die erwarteten Investmentrenditen sind r = diag[μ′ω] − τ[ω].
- Die Kosten sind unstetig, ändern sich mit h und sind in r eingebettet.
- Eine Lösung wird auch bei unstetigen Kostenfunktionen gefunden, ohne analytische Eigenschaften der Zielfunktion zu verwenden.
- In den Beispiel-Backtest-Codes sind keine Transaktionskosten enthalten, obwohl sie für einen aussagekräftigen Backtest entscheidend sind.
- Die Transaktionskosten von Forex sind stark venue-abhängig, weil die Bid-Ask-Spreads desselben Währungspaars zwischen den Plätzen erheblich variieren, und sie müssen im Backtest berücksichtigt werden.
- Hard to borrow kann beim Leerverkauf heißen, dass der Leerverkäufer dem Aktienverleiher Zinsen zahlt, statt wie im Normalfall Zinsen zu erhalten.
- Die Dezimalisierung der US-Aktienpreise verengte die Bid-Ask-Spreads drastisch, sodass Pair-Trader, die wie Market Maker agieren, auch geringere Market-Making-Gewinne erzielen (Serge, 2008).

## Funktionsweise

- Zu einem Roll- oder Anpassungstermin werden je Instrument der alte Absolutbestand mal Schlusskurs und der neue Absolutbestand mal den nächsten Eröffnungskurs addiert, mit Punktwert und Kostensatz multipliziert und über die Instrumente summiert.
- Die Kosten für Kauf oder Verkauf einer Einheit des virtuellen ETF sind die Summe über den absoluten vorherigen Bestand mal Schlusskurs mal Punktwert mal Kostensatz.
- Der Punktwert ist der Dollarwert eines Punktes und schließt den Wechselkurs ein.
- Die Zahl handelbarer Korbeinheiten ist das Minimum der Quotienten aus Volumen und absolutem vorherigem Bestand und wird damit vom am wenigsten aktiven Glied bestimmt.
- Die Kosten gehen in den Zähler der Sharpe Ratio ein, weil sie von den erwarteten Überschussrenditen abgezogen werden.
- Für jede diskrete Trajektorie werden die Transaktionskosten über die Horizonte hinweg bewertet, bevor die Sharpe Ratio verglichen wird.

## Voraussetzungen

- Die Renditen sind je Horizont multivariat normal und über die Zeit unabhängig, aber nicht identisch verteilt.

## Anwendung im Trading

- Das Problem betrifft besonders große Asset Manager, weil übermäßiger Turnover und Implementation Shortfall die Profitabilität ihrer Strategien entscheidend schmälern können.
- Anders als bei Garleanu und Pedersen (2012) wird nicht vorausgesetzt, dass die Renditen aus einer identisch und unabhängig verteilten Normalverteilung stammen.

## Regeln und Kriterien


## Risiken und Grenzen

- Werden die Rebalancing-Kosten in den Investitionswert eingebettet, erzeugt das Shorten des Spreads beim Anpassen der Gewichte fiktive Gewinne.
- Die Handelszeiten der Bestandteile stimmen nicht exakt überein, deshalb ist der Spread nicht immer zum letzten veröffentlichten Kurs und ohne Latenzrisiko handelbar.
- Zusammen mit den unstetigen, horizonspezifischen Kosten ist die Aufgabe kein konvexes quadratisches Programm.
- Der Preis dieser allgemeinen Kostenfunktionen ist ein extrem hoher Rechenaufwand, vergleichbar mit der Bewertung aller Wege im Problem des Handlungsreisenden.
- Die Backtests dieses Buchs enthalten keine Transaktionskosten, weil diese empfindlich von der genauen Ausführungsmethode und vom genauen Aktienuniversum abhängen.
- Ein Backtest einer Aktienpaar-Strategie auf Trade- oder Quote-Preisen ist unrealistisch, wenn nicht nur 100 Stück gehandelt werden oder erhebliche Transaktionskosten angesetzt werden.
- Market Orders auf beiden Seiten, nachdem das Signal von den NBBO-Preisen kam, können erheblichen Slippage erzeugen.
- In der Open-to-Close-Variante des linearen Long-Short verdoppeln sich die Transaktionskosten gegenüber einmal täglichem Handel, weil zweimal am Tag gehandelt wird; auch diese Kosten fehlen im Backtest.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 58–77 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-004-p058-p077|S. 58–77]]
- Advances in Financial Machine Learning.pdf, S. 343–362 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-019-p343-p362|S. 343–362]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]

## Verwandte Themen
