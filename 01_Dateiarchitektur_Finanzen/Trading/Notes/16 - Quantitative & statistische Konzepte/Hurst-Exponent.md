---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Modelle"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-01
---

# Hurst-Exponent


## Kurzdefinition

- Die Varianz der Logpreisänderung über die Spanne τ wird angenähert durch τ hoch 2H, und H ist der Hurst-Exponent.
- Für einen geometrischen Random Walk ist H gleich 0,5, für eine mean-reverting Reihe ist H kleiner als 0,5, und für eine trendende Reihe ist H größer als 0,5.
- Je weiter H gegen null sinkt, desto stärker ist die Mean Reversion, und je weiter H gegen 1 steigt, desto stärker ist der Trend; H misst also den Grad von Mean Reversion oder Trend.

## Kernaussagen

- Auf den Tageskursen von USD.CAD um 17:00 Uhr ET liefert genhurst(log(y), 2) den Hurst-Exponenten 0,49 und deutet damit nur auf schwache Mean Reversion.
- Wegen der endlichen Stichprobe ist die statistische Signifikanz eines geschätzten H nötig, bevor die Null H gleich 0,5 verworfen wird. Für USD.CAD liefert vratiotest h gleich 0 und pValue gleich 0,367281, die Random-Walk-Null wird also nicht verworfen.
- Für den Zwei-Jahres-Treasury-Future TU beträgt der Hurst-Exponent 0,44.
- Der Variance-Ratio-Test verwirft für TU die Hypothese eines Random Walk nicht.
- Der Widerspruch zu den positiven Lag-Korrelationen löst sich dadurch, dass die Reihe auf verschiedenen Zeitrahmen Momentum und Mean Reversion zeigt.
- Der Variance-Ratio-Test kann die einzelnen Zeitrahmen nicht prüfen, in denen die Korrelationen stärker als im Durchschnitt sind.
- Hurst-Exponent und Variance-Ratio-Test werden mit genhurst und vratiotest berechnet, der Korrelationskoeffizient mit corrcoef.

## Funktionsweise

- Die Varianz ist Var(τ) gleich dem Mittel von |z(t+τ) minus z(t)| zum Quadrat, wobei z der Logpreis log(y) ist und das Mittel über alle t läuft.
- Beim geometrischen Random Walk gilt dieses Mittel proportional zu τ; die Proportionalität wird für großes τ zur Gleichheit und kann für kleines τ von der Geraden abweichen.
- Bei Mean Reversion oder bei positiver Korrelation aufeinanderfolgender Preisbewegungen gilt stattdessen die Proportionalität zu τ hoch 2H.
- Die verallgemeinerte Fassung ist das Mittel von |z(t+τ) minus z(t)| hoch 2q proportional zu τ hoch 2H(q); im Beispiel wird q gleich 2 gesetzt.
- Stationarität bedeutet hier nicht, dass die Varianz zeitunabhängig und H gleich null ist, sondern nur, dass die Varianz langsamer wächst als bei normaler Diffusion.
- Wer langfristiges Trendverhalten ohne festes Zeitfenster prüfen will, berechnet den Hurst-Exponenten zusammen mit dem Variance-Ratio-Test, um die Null eines Random Walk auszuschließen.
- Dieselben Tests, in Kapitel 2 für Mean Reversion beschrieben, dienen hier als Momentum-Tests.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Der Variance-Ratio-Test prüft die Null, dass H wirklich 0,5 ist, also dass das Varianzverhältnis gleich 1 ist (Lo, 2001).
- Beim vratiotest bedeutet h gleich 1 die Ablehnung der Random-Walk-Hypothese auf dem 90-Prozent-Niveau, und h gleich 0 bedeutet, dass ein Random Walk möglich bleibt; pValue ist die Wahrscheinlichkeit, dass die Null zutrifft.

## Risiken und Grenzen


## Beispiele

- Für USD.CAD liefert genhurst den Wert H gleich 0,49 und damit eine schwach mean-reverting Reihe.
- Für dieselben Logpreise von USD.CAD liefert der Variance-Ratio-Test h gleich 0 und pValue gleich 0,367281, also etwa 37 Prozent Wahrscheinlichkeit für einen Random Walk, und die Null wird nicht verworfen.
- Für den Zwei-Jahres-Treasury-Future TU beträgt der Hurst-Exponent 0,44, und der Variance-Ratio-Test verwirft die Random-Walk-Hypothese nicht.
- Der Widerspruch zu den Korrelationstests löst sich dadurch, dass dieselbe Reihe auf verschiedenen Zeitebenen Momentum und Mean Reversion zeigt; der Variance-Ratio-Test kann die einzelnen Ebenen, auf denen die Korrelation überdurchschnittlich ist, nicht prüfen.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 1–13 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-001-p001-p013|S. 1–13]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 52–71 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-004-p052-p071|S. 52–71]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 71–75 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-005-p071-p075|S. 71–75]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 144–163 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-011-p144-p163|S. 144–163]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 115–134 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-007-p115-p134|S. 115–134]]

## Verwandte Themen

- Eine klare mathematische Darstellung von ADF- und Variance-Ratio-Test steht in den Kursnotizen von Walter Beckert (Beckert, 2011).
