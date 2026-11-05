---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/07 - Orderflow & Market Microstructure/07 - Orderflow & Market Microstructure|07 - Orderflow & Market Microstructure]]"
weitere_hauptthemen: []
unterthema: "Mikrostruktur"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-01
---

# Slippage


## Kurzdefinition

- Der durchschnittliche Slippage je Umschlag sind die Ausführungskosten eines Portfolioumschlags ohne Brokergebühren.
- Der Slippage je Umschlag sind die Ausführungskosten ohne Brokergebühren.
- Slippage entsteht durch den Bid-Ask-Spread und durch den Betrag, um den die Order des Anlegers den Preis schiebt, nach oben beim Kauf und nach unten beim Verkauf.

## Kernaussagen

- Slippage geht zusammen mit den Brokergebühren in die Dollar-Performance je Umschlag ein.
- Strategien scheitern oft an falschen Annahmen über Ausführungskosten.
- Slippage geht zusammen mit den Brokergebühren in die Dollar-Performance und in die Rendite auf die Ausführungskosten ein.
- Die Rendite auf die Ausführungskosten soll ein großes Vielfaches sein, sodass die Strategie eine schlechtere Ausführung übersteht.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Zu den Handelskosten im Regeltest gehören Brokerprovisionen und Slippage.
- Regeln mit häufigen Umkehrsignalen verursachen höhere Handelskosten als Regeln mit seltenen Signalen; das ist zu berücksichtigen, wenn sie als eigenständige Handelsregeln verglichen werden.
- Geht es nur darum, Signale mit Prognoseinformation zu finden, können Handelskosten den Wert einer häufig umkehrenden Regel verdecken.
- Die Regelstudien dieses Buches setzten keine Handelskosten an, weil sie Prognosekraft suchten und nicht eigenständige Handelsstrategien.

## Risiken und Grenzen

- Market Orders auf beiden Seiten, nachdem das Signal von den NBBO-Preisen kam, können erheblichen Slippage erzeugen. Stattdessen gehen Limit Orders auf eine oder beide Seiten, mit kleinen Teilmengen, vorübergehend ungedeckten Positionen und aktiver Storno- und Neueinreichung.
- Bei einer NBBO-Größe von oft nur 100 Aktien, wie bei AAPL, ist ein Backtest auf Trade- oder Quote-Preisen unrealistisch, außer die Strategie handelt nur 100 Stück oder setzt erhebliche Transaktionskosten an.
- Die Backtests enthalten keine Transaktionskosten. In der Intraday-Long-Short-Variante verdoppeln sie sich gegenüber der Fassung mit einem Handel pro Tag.

## Beispiele

- Dazu gehört der Verlust, der entsteht, wenn ein Wertpapier zu einem Fill-Preis über dem Mittelpreis im Zeitpunkt der Weitergabe an den ausführenden Broker gekauft wird.
- Ein Beispiel ist der Verlust aus einem Kauf zu einem Fill-Preis, der über dem Mittelpreis im Zeitpunkt der Order an den Broker liegt.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 20–39 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-002-p020-p039|S. 20–39]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 95–98 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-007-p095-p098|S. 95–98]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 99–118 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-008-p099-p118|S. 99–118]]

## Verwandte Themen
