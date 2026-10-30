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

# Market Making


## Kurzdefinition

- Market Maker, bei Ney die Specialists oder Insider, sind lizenzierte Großhändler, die beide Seiten des Marktes sehen und in den Aktien einen Markt machen.
- Ein langfristiges Gleichgewicht von null entspricht dem Geschäft von Market Makern, die Liquidität bereitstellen und erwarten, dass Abweichungen vom aktuellen Preisniveau sich im Zeitverlauf korrigieren.
- Market Maker sind in diesen Modellen die Liquiditätsanbieter, die den informierten Position Takern gegenüberstehen.

## Kernaussagen

- Jeder Markt ist auf irgendeine Weise manipuliert, Aktien verdeckt durch Market Maker, Devisen durch Zentralbanken, die regelmäßig und teils öffentlich intervenieren.
- Im Kassenmarkt wird jede Order ausgeführt, weil Market Maker Kauf und Verkauf erfüllen und ihr Inventar führen müssen.
- Ohne diese Großhändler würde der Markt nicht funktionieren.
- Ein einzelner Market Maker kann den gesamten Aktienmarkt nicht allein steuern.
- Sie nutzen jede Nachricht, ob sie relevant ist oder nicht, um Preise zu bewegen, sodass Märkte auf gute Nachrichten fallen und auf schlechte steigen können.
- Sehen die Specialists zugleich ein Überangebot und liefert eine Nachricht einen Verkaufsanlass, handeln sie weitgehend gleichzeitig, weil ihre Lager ähnlich stehen.
- An NYSE, AMEX und NASDAQ wirken Specialists als Market Maker, darunter Barclays und Getco.
- Laut Bloomberg Business 2012 versuchen US-Börsen, Market Maker zu aggressiveren Quotes zu bewegen, um Volumen anzuziehen, und mehr Firmen für diese Rolle zuzulassen.
- An der LSE gibt es für viele Titel offizielle Market Maker; die größten und meistgehandelten Aktien laufen über das elektronische System SETS.
- Das Einzige, was die Insider nicht verbergen können, ist das Volumen.
- Insidergeschäfte von Außenstehenden werden bestraft, die lizenzierte Tätigkeit der Market Maker im Markt dagegen zugelassen.
- Im Aktien- und Indexhandel sind es die Market Maker, in Futures die großen Operatoren, im Forex wieder die Market Maker und in Anleihen die großen Operatoren.
- Hochfrequentes Market Making versucht, wie traditionelles Market Making, auf beiden Seiten des Buchs Liquidität zu stellen und den Spread zu verdienen.
- Specialists unterstehen nach dem zitierten SEC-Gespräch von 1975 der Börse, nicht direkt der Kommission, und arbeiten unter Selbstregulierung.
- Je kleiner die Halbwertszeit, desto kleiner ist der autoregressive Koeffizient.
- Ein kleiner autoregressiver Koeffizient zusammen mit einem erwarteten Gewinn von null lässt die meisten Paare aus Stop und Gewinnziel bei einer Performance von null.
- Die optimale Regel hält das Inventar, bis ein kleiner Gewinn entsteht, auch auf Kosten nicht realisierter Verluste vom Fünf- oder Siebenfachen.
- Viele Market Maker handeln so, im Einklang mit dem asymmetrischen Auszahlungsdilemma bei Easley, López de Prado und O’Hara 2011.
- Die schlechteste Regel, ein enger Stop mit hohem Gewinnziel, wird in diesem Geschäft gemieden.
- Symmetrische Gewinn- und Stop-Schwellen auf der Diagonalen lassen die Performance am nächsten bei null.
- In der PIN-Theorie verkaufen Market Maker die Option, advers selektiert zu werden, und der Bid-Ask-Spread ist die dafür verlangte Prämie.
- Im Kyle-Modell können Market Maker informierte Orders nicht von Noise-Orders unterscheiden.
- Im Gleichgewicht dieses Modells ist ihre Preisanpassung linear im gesamten Orderflow.
- Kyle verlangt von ihnen ein Gleichgewicht zwischen Gewinnmaximierung und Markteffizienz.
- Sequenzielle Handelsmodelle sind unter Market Makern verbreitet, weil sie die Unsicherheitsquellen der Liquiditätsanbieter enthalten.
- Diese Quellen sind die Wahrscheinlichkeit eines Informationsereignisses, die Wahrscheinlichkeit dass die Nachricht negativ ist, sowie die Ankunftsraten von Noise Tradern und informierten Händlern.
- Mit diesen Größen müssen Market Maker ihre Quotes dynamisch nachführen und ihre Bestände steuern.
- Die Wahrscheinlichkeiten α und δ werden nach jedem eintreffenden Trade bayesianisch aktualisiert.
- Veröffentlichte Quotes geben nicht immer die Niveaus wieder, zu denen Market Maker Liquidität stellen wollen, etwa bei Corporate-, Municipal- und Agency-Bonds.
- Unter normalen Bedingungen erzeugen ihre Prognosen einen niedrigen Cross-Entropy-Verlust.
- Predatory Algorithms versuchen, Market Maker über Quotestornierungen und Ordertypen advers zu selektieren.
- Am kurzen Ende der Zeitskala stützen sich Market-Making-Strategien auf Preise, die in Sekunden zum Mittel zurückkehren.
- Eine kurze Zeitskala bedeutet mehr Trades pro Jahr, daraus höhere statistische Sicherheit und eine höhere Sharpe Ratio in Backtest und Live-Handel und schließlich eine höhere zusammengesetzte Rendite.
- Gesucht werden auch hier Mittelpreis und Standardabweichung für den Mean-Reversion-Handel, nicht die Hedge Ratio zwischen zwei kointegrierenden Reihen.
- Viele traditionelle Market Maker quoten keine großen Sizes mehr, weil High-Frequency-Strategien große Bids oder Asks frontrunnen; die NBBO-Sizes sind deshalb über viele Märkte gesunken.
- Selbst bei AAPL betragen die NBBO-Sizes oft nur ein paar hundert Aktien, bei SPY auf ARCA oft weniger als 10.000.
- High-Frequency-Händler verdienen nur an langsameren Händlern; bleiben nur sie übrig, ist der durchschnittliche Nettogewinn aller null.

## Funktionsweise

- Albert Labos beschrieb die Market Maker und ihre Tricks als die Seite, deren Inventarzyklen von Akkumulation und Distribution zu lesen sind.
- Der kurzfristige Trend ist nach Richard Ney der Rahmen, in dem der Specialist seine täglichen Inventarprobleme löst, während die mittleren und langen Ziele im Blick bleiben.
- Die Feature-Matrix für die Entscheidung, Liquidität zu stellen oder passive Quotes zurückzuziehen, kann unter anderem VPIN, Kyle’s Lambda und Stornierungsraten enthalten.
- Eine Neubeurteilung kann zum Beispiel nach jeweils 10.000 gehandelten Kontrakten oder bei einer deutlichen Preisänderung erfolgen.
- Beobachtungen werden mit 1 gelabelt, wenn das Market Making einen Gewinn brachte, und mit 0 bei einem Verlust.
- Das Informationsmaß φτ ist der Wert der Verteilungsfunktion der negativen Cross-Entropy-Verluste an der aktuellen Prognose und liegt in (0, 1).
- Als Market-Making-Modell schätzt der Kalman-Filter nur eine mean-reverting Preisreihe: der verborgene Zustand ist der Mittelpreis m(t), die beobachtbare Größe ist der Preis y(t).
- Die Messgleichung ist y(t) gleich m(t) plus Rauschen, und der Zustandsübergang ist m(t) gleich m(t−1) plus Rauschen.
- Das Update lautet m plus Kalman-Gain mal (y minus m), der Gain ist R geteilt durch (R plus Ve), die Prognosevarianz ist die Varianz von m plus Ve, und die neue Zustandsvarianz ist (1 minus Gain) mal R.
- Ein favorisiertes Modell, mit dem Market Maker ihre Schätzung des mittleren Preises eines Assets aktualisieren, ist der Kalman-Filter; darauf hat Euan Sinclair 2010 hingewiesen.
- Dabei werden der mittlere Preis und die Standardabweichung einer einzelnen mean-reverting Preisreihe geschätzt, nicht die Hedge Ratio zwischen zwei kointegrierenden Reihen.
- Die Unsicherheit des beobachteten Transaktionspreises wird so angesetzt, dass eine große Trade-Größe gegenüber einer Benchmark eine kleine Unsicherheit bedeutet und umgekehrt.
- Ist die Trade-Größe gleich der Benchmark, ist der Kalman-Gain 1 und die neue Mittelpreis-Schätzung genau der beobachtete Preis.
- Die Benchmark kann ein Bruchteil des Vortagesvolumens sein und wird mit Trainingsdaten optimiert.
- Größere Trades und jüngere Preise erhalten mehr Gewicht, vergleichbar mit einem volumen- und zeitgewichteten Durchschnittspreis.
- Market Maker ziehen aus dem Orderflow wichtige fundamentale Information und setzen Bid und Ask danach.
- Große gleichgerichtete Market Orders in Sekundenbruchteilen deuten auf informierte Händler hin; der Market Maker passt Bid und Ask sofort zum eigenen Schutz an.
- Die Dringlichkeit von Market Orders zeigt, dass die Information neu und nicht weit bekannt ist.
- Nach der Füllung kleiner Quotes stellt der Market Maker dieselben Preise nach, um nicht von High-Frequency-Händlern ausgenutzt zu werden.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Specialists verkaufen zu Einzelhandelspreisen, was sie zu Großhandelspreisen gekauft haben.
- Je länger sie im Geschäft sind, desto mehr Kapital sammeln sie für Käufe zu Großhandelspreisen und den späteren Verkauf zu Einzelhandelspreisen.
- Mehr Medien bringen mehr Teilnehmer in den Markt und erhöhen die Volatilität, weil sie Angebot und Nachfrage verstärken.
- Um große Mengen zu handeln, suchen Börsenmitglieder neue Verkaufstechniken über die Massenmedien.
- Um wachsende Mittel einzusetzen, müssen Specialists immer tiefere Rückgänge erzeugen, damit genug Aktien herausgeschüttelt werden.
- Anstiege müssen auf der Oberseite dramatischer werden, um das öffentliche Interesse für den Absatz der gewachsenen Lager zu wecken.
- Die aktivsten Aktien brauchen längere Zeit für ihre Distribution.
- Die Wirtschaft wird nach Ney zunehmend dramatischen Einbrüchen ausgesetzt, mit Inflation, Arbeitslosigkeit, hohen Zinsen und Rohstoffknappheit.

## Risiken und Grenzen

- Am Flash Crash vom 6. Mai 2010 erwarteten Market Maker, passive Bids ausführen und teurer zurückverkaufen zu können.
- Der Crash entstand durch die Anhäufung tausender Prognosefehler.
- Sie stellten weiter Liquidität zu übermäßig großzügigen Kursen, bis der Stop-out eine Liquiditätskrise auslöste.
- Ein weiterer Bid-Ask-Spread hätte den verkaufsseitigen Orderflow stoppen können, weil die Verkäufer diese Abschläge nicht mehr akzeptiert hätten.
- Ein weiterer Grund, große Quotes zu vermeiden, ist, dass aus ihrer Füllung große Inventare entstehen, die Market Maker nicht halten wollen.

## Beispiele

- In der Parabel von Onkel Joe streut der einzige Widget-Händler Knappheit, hebt die Preise, leert das Lager und kauft in der Panik über das Gerücht eines größeren Konkurrenten zu fallenden Preisen zurück.
- Die SEC-Konzeptveröffentlichung von Ende 2012 nennt neben Market Making noch Arbitrage aus Fehlbewertungen, strukturelle Strategien wie Latency Arbitrage und Quote Stuffing sowie direktionale Strategien wie Order Anticipation und Momentum Ignition.
- Für Prognose 0, Halbwertszeit 5 und Sigma 1 erreichen die Sharpe Ratios etwa 3,2.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- A Complete Guide to Volume Price Analysis.pdf, S. 1–20 → [[Trading/Pilot/blocks/a-complete-guide-to-volume-price-analysis-pdf/a-complete-guide-to-volume-price-analysis-pdf-block-001-p001-p020|S. 1–20]]
- A Complete Guide to Volume Price Analysis.pdf, S. 58–77 → [[Trading/Pilot/blocks/a-complete-guide-to-volume-price-analysis-pdf/a-complete-guide-to-volume-price-analysis-pdf-block-004-p058-p077|S. 58–77]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 173–186 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-013-p173-p186|S. 173–186]]

## Verwandte Themen
