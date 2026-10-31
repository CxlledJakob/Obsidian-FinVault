---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Validierung"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Sensitivitätsanalyse


## Kurzdefinition


## Kernaussagen

- Fünf Faktoren bestimmen, wie zufällig ein Data-Mining-Vorhaben ist und damit die Größe des Data-Mining-Bias.
- Der erste Faktor ist die Zahl der auf dem Weg zur besten Regel gebacktesteten Regeln: Je mehr Regeln geprüft werden, desto größer ist der Bias.
- Der zweite ist die Zahl der Beobachtungen, aus denen die Leistungskennzahl berechnet wird: Je mehr Beobachtungen, desto kleiner der Bias.
- Der dritte ist die Korrelation der Renditehistorien der geprüften Regeln: Je weniger sie korrelieren, desto größer der Bias.
- Der vierte ist das Vorliegen sehr großer positiver Renditen in der Leistungshistorie einer Regel, zum Beispiel einer sehr großen positiven Tagesrendite: Sind sie vorhanden, tendiert der Bias dazu, größer zu sein.
- Dieser Ausreißer-Effekt wird kleiner, wenn die positiven Ausreißer im Verhältnis zur Zahl der Beobachtungen der Kennzahl wenige sind; mehr Beobachtungen verdünnen ihn.
- Der fünfte ist die Variation der wahren erwarteten Rendite unter den gebacktesteten Regeln: Je geringer diese Variation, desto größer der Bias.
- Haben die geprüften Regeln ähnliche Grade an Vorhersagekraft, ist der Data-Mining-Bias größer.
- Werden die fünf Faktoren berücksichtigt, lassen sich statistische Signifikanz oder ein Konfidenzintervall für eine durch Data Mining entdeckte Regel berechnen.

## Funktionsweise

- Eine längere Lookback-Periode ist weniger empfindlich für Preisänderungen als eine kürzere und braucht eine längere Phase jüngster Momentumänderung, bis sie beeinflusst wird.
- Der Vorteil der längeren Periode sind weniger falsche Umkehren aus kurzfristigen Momentumänderungen; der Nachteil ist ein möglicher Nachlauf von mehreren Bars zwischen Preisumkehr und Indikatorumkehr.
- Eine relativ kürzere Lookback-Periode erzeugt immer Momentumumkehren sehr nahe an den Preis-Schwunghochs und -tiefs.
- Die zeitnäheren Signale der kürzeren Periode haben den Preis vieler falscher Momentumumkehren, die der fortgesetzte Trend innerhalb kurzer Zeit wieder zurücknimmt.
- Eine zu kurze Lookback-Periode erzeugt zu viele Momentum-Whipsaws.
- Die primäre Einstellung jedes Indikators ist die Lookback-Periode, also die Zahl der Bars, die in die Momentumberechnung eingehen.

## Voraussetzungen


## Anwendung im Trading

- Die Einstellung wird gewählt, indem einige Lookback-Perioden an jüngsten Daten geprüft werden und diejenige genommen wird, die die Kriterien eines nützlichen Indikators am besten erfüllt.
- Dieselbe Prüfung weniger Lookback-Perioden wird über zwei oder drei verschiedene Zeitabschnitte gemacht, und danach werden die nützlichsten Einstellungen angenommen.
- In einem Live-Workshop lässt der Autor ein beliebiges Aktien-, ETF-, Futures-, Index- oder Forex-Symbol auf beliebiger Zeitebene aufschreiben und wählt die besten Einstellungen jedes Indikators innerhalb einer Minute.
- Der Autor erstellt die gesamte Analyse und Handelsstrategie für jeden Markt und jede Zeitebene innerhalb von drei Minuten.
- Das gezeigte Beispiel ist nur eines aus einem begrenzten Datensatz; Konzept und Ablauf sind auf jeden Markt, jede Zeitebene und jeden Indikator zu übertragen.

## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Beim täglichen SPX mit DTosc und 21 Tagen roher Lookback-Periode erreichten gewöhnlich nicht beide Linien vor einer Umkehr die Overbought- und Oversold-Zonen, und der Nachlauf betrug gewöhnlich mehrere Bars, nachdem der Preis sich deutlich vom Schwunghoch oder -tief entfernt hatte; diese Periode ist für diese Daten wahrscheinlich zu lang.
- Beim 8-Tage-Lookback derselben Daten lagen die Umkehren an Hochs und Tiefs in den Overbought- und Oversold-Zonen und auf oder innerhalb von ein oder zwei Bars zum Extrem.
- Am selben 8-Tage-Chart sind drei Bereiche markiert, in denen der Indikator unruhig wurde und Momentumumkehrsignale gab, die innerhalb von ein oder zwei Bars wieder umgekehrt wurden.
- Beim 13-Tage-Lookback erreichte der Indikator bei den meisten Momentumumkehren die Overbought- oder Oversold-Zone, die Umkehren lagen innerhalb weniger Bars zu den Preishochs und -tiefs, und zwischen den Zonen gab es keine falschen Momentumumkehren.
- Von den drei Lookback-Perioden 8, 13 und 21 Tage war für diese Daten die mit 13 Tagen die beste.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 267–286 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-015-p267-p286|S. 267–286]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 286–305 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-016-p286-p305|S. 286–305]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 42–61 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-004-p042-p061|S. 42–61]]

## Verwandte Themen
