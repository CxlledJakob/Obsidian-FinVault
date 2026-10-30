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
aktualisiert: 2026-10-30
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

## Funktionsweise

- Hierarchical Risk Parity arbeitet in drei Stufen: Baum-Clustering, Quasi-Diagonalisierung und rekursive Bisektion.
- Hierarchical Risk Parity konvergiert günstigstenfalls in deterministischer logarithmischer Zeit und schlechtestenfalls in deterministischer linearer Zeit.

## Voraussetzungen


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

## Verwandte Themen

- Hedging
- Rebalancing
