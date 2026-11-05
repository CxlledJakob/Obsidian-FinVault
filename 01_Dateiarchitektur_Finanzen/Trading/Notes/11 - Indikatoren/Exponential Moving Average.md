---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/11 - Indikatoren/11 - Indikatoren|11 - Indikatoren]]"
weitere_hauptthemen: []
unterthema: "Trendindikatoren"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Exponential Moving Average


## Kurzdefinition

- Ein EMA ist ein rekursiver Filter: Sein Output hängt nicht nur von den Inputdaten ab, sondern auch von früheren Werten des Outputs.

## Kernaussagen

- Die Mittellinie der Bollinger Bands ist ein Exponential Moving Average.
- Dieser Durchschnitt gilt als wahrer Wert oder Mean.
- Ein exponentieller gleitender Durchschnitt gewichtet neue Daten stärker und braucht keinen harten Cutoff. Es ist aber nicht klar, warum gerade der exponentielle Abfall der Gewichte optimal sein soll.
- Dieselbe Unschärfe gilt, wenn Mittel, Standardabweichung oder Hedge Ratio mit einem exponentiell gewichteten Schema statt mit einem harten Lookback geschätzt werden. Der Kalman-Filter vermeidet die willkürliche Wahl dieses Schemas.
- Andere Bezeichnungen für rekursive Filter sind Exponential-Moving-Average-Filter, Infinite-Impulse-Response-Filter (IIR), Ladder-Filter und autoregressive Filter.
- Rekursive Filter sind in manchen für das Trading genutzten Programmiersprachen schwer umzusetzen.
- In der Tabelle der Filterkoeffizienten nach Ehlers hat der EMA b0 = α, b1 = 0, b2 = 0, a0 = 1, a1 = −(1 − α) und a2 = 0.

## Funktionsweise

- Mit den Koeffizienten b0 = α, a0 = 1 und a1 = −(1 − α) wird die allgemeine Transferfunktion zu Output = α * Input + (1 − α) * Output[1]; das ist genau die Gleichung des EMA.
- Die Koeffizienten auf der rechten Seite der EMA-Gleichung summieren sich zu 1, sodass der Filter keinen Noise Gain hat.
- Der EMA ist ein Tiefpassfilter: Er lässt die niederfrequenten Anteile der Inputdaten durch und dämpft die höherfrequenten Anteile.
- Wird Alpha kleiner gewählt, kommen weniger der niederfrequenten Anteile durch und die hochfrequenten Anteile werden stärker gedämpft.
- Wird Alpha größer gewählt, glättet der EMA weniger, und mehr höherfrequente Anteile des Inputs gelangen in den Output.
- Die Transferfunktion des EMA hat keine Nullstellen und keine Polstellen.
- Ein EMA wird berechnet als ein Bruchteil des aktuellen Preises plus der komplementäre Bruchteil des EMA von vor einem Bar: EMA = α * Price + (1 − α) * EMA[1].
- Alpha kann einen Wert zwischen null und eins haben; die zweite Fraktion muss eins minus Alpha betragen, weil beide zusammen eins ergeben müssen.
- Auf einen Impuls antwortet der EMA mit der Folge 1, (1 − α), (1 − α)², (1 − α)³ bis (1 − α)^N; die Amplitude fällt exponentiell ab, daher der Name.
- Ein Teil jedes Inputs bleibt grundsätzlich in allen folgenden Berechnungen enthalten, auch wenn sein Beitrag verschwindend klein wird; deshalb gehört der EMA zu den Infinite-Impulse-Response-Filtern (IIR).
- Springt der Preis nach langer Zeit bei null auf 1 und bleibt dort, hat der EMA am ersten Bar den Wert α, am zweiten α + α * (1 − α), am dritten α + α * (1 − α) + α * (1 − α)² und nähert sich allmählich 1.

## Voraussetzungen


## Anwendung im Trading

- Ein Einstiegssignal für Zeitreihenmomentum ist, zu kaufen, wenn der Preis den N-Tage-Durchschnitt oder den exponentiellen gleitenden Durchschnitt überschreitet.
- Der S&P Diversified Trends Indicator geht einen Future long, wenn er über seinem exponentiellen gleitenden Durchschnitt liegt, und short, wenn er darunter liegt, mit monatlichem Rebalancing.
- Der Index umfasst 24 Futures; der Fonds RYMFX und der ETF WDTI bilden ihn ab.
- Nach Dever 2011 beträgt die Sharpe Ratio dieses Index von Januar 1988 bis Dezember 2010 1,3 bei einem maximalen Drawdown von minus 16,6 Prozent, gegenüber einer Sharpe Ratio von 0,61 und einem maximalen Drawdown von minus 50,96 Prozent des S&P 500 im selben Zeitraum.
- Seit der Finanzkrise 2008 ist die Leistung schlecht, und zum Zeitpunkt des Textes beträgt der Drawdown seit dem 5. Dezember 2008 minus 25,9 Prozent.
- Filter lassen sich hintereinanderschalten: Der Output eines Bandpassfilters kann zum Beispiel Input eines EMA mit einer anderen kritischen Periode sein, um die Daten weiter zu glätten.

## Regeln und Kriterien

- Aus einem akzeptablen Lag L lässt sich Alpha berechnen: α = 1 / (L + 1); bei drei Bars Lag ist α = 0,25.
- Über gleiche statische Lags entspricht ein EMA einem N-Bar-SMA mit α = 2 / (N + 1); diese Beziehung wird in den meisten Technische-Analyse-Büchern genannt.
- Ein EMA soll immer als EMA = α * Input + (1 − α) * EMA[1] geschrieben werden, um Rechenfehler bei der Auswertung des Bruchkoeffizienten zu vermeiden.
- Ehlers legt α als globale Variable an und schreibt die EMA-Gleichung vollständig in α aus, damit sich beide Terme sicher zu eins summieren.

## Risiken und Grenzen

- Der Durchschnitt beruht nur auf dem Preis und zeigt die Wanderung des Means unvollständig.
- Ein häufiger Programmierfehler ist, für α zum Beispiel 0,2 und für (1 − α) eine andere Zahl wie 0,9 einzusetzen; summieren sich die Terme nicht zu eins, liefert der rekursive Algorithmus sprunghafte Ergebnisse oder kann den Computer sogar abstürzen lassen.
- Die Lags eines SMA und seines EMA-Äquivalents sind nur bei der Frequenz null gleich.
- Obwohl die statischen Lags übereinstimmen, liegt die kritische Periode des EMA nicht an derselben Stelle wie die des SMA; ein besserer Wert für α ergibt sich aus der Transferfunktion des EMA.
- Ein Weighted Moving Average hat im Durchlassbereich mehr Lag als der entsprechende EMA.

## Beispiele


## Unterschiedliche Quellenpositionen

- In den Key Points des Kapitels steht für den EMA-Koeffizienten, der einem N-Bar-SMA entspricht, α = 2 / (N − 1), während die Herleitung im Text α = 2 / (N + 1) ergibt.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Markets in Profile_ Profiting from the Auction Process.pdf, S. 120–139 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-010-p120-p139|S. 120–139]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 76–95 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-006-p076-p095|S. 76–95]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 144–163 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-011-p144-p163|S. 144–163]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 12–25 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-002-p012-p025|S. 12–25]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 26–34 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-003-p026-p034|S. 26–34]]

## Verwandte Themen
