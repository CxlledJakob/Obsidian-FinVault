---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/12 - Momentum/12 - Momentum|12 - Momentum]]"
weitere_hauptthemen: []
unterthema: "Momentumstruktur"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-01
---

# Zeitreihenmomentum


## Kurzdefinition

- Zeitreihenmomentum bedeutet, dass vergangene Renditen einer Preisreihe positiv mit ihren künftigen Renditen korreliert sind, nach Moskowitz, Yao und Pedersen 2010.
- Zeitreihenmomentum bezeichnet die positive Korrelation der vergangenen und der künftigen Renditen einer Preisreihe.

## Kernaussagen

- Im Momentum-Lager werden zunächst einige statistische Tests für Zeitreihenmomentum erklärt.
- Strategien sollen Zeitreihenmomentum und Cross-Sectional-Momentum extrahieren.
- Untersucht werden die vier Haupttreiber von Momentum bei Aktien und Futures. Roll Returns bei Futures sind einer davon.
- Erzwungene Käufe und Verkäufe von Assets sind in vielen unterschiedlichen Umständen der Haupttreiber von Aktien- und ETF-Momentum.
- Neuere Momentum-Strategien beruhen auf Nachrichtenereignissen, News Sentiment, gehebelten ETFs, Orderflow und Hochfrequenzhandel.
- Gegen Mean-Reversion-Strategien haben sie unter verschiedenen Marktregimes der jüngeren Finanzgeschichte diametral verschiedene Risiko-Rendite-Eigenschaften.
- Die Finanzkrise 2008 leitete einen mehrjährigen Bärenmarkt der Momentum-Strategien ein, behandelt in Kapitel 6.
- Nur weil eine Momentum-Strategie vor 2008 gut abschnitt, folgt nicht, dass sie danach gut abschneidet, selbst wenn der Backtest ohne erkennbare Fallstricke ist.
- Beispiel 1.1 zeigt, dass jede zufällige Renditeverteilung mit hoher Kurtosis Momentum-Strategien begünstigen kann.
- Futures zeigen Zeitreihenmomentum hauptsächlich wegen der Persistenz des Vorzeichens der Rollrenditen.
- Momentum-Modelle gedeihen an Black-Swan-Ereignissen und an der positiven Kurtosis der Renditeverteilung.
- Das Aufwärtspotenzial ist unbegrenzt und das Abwärtspotenzial durch zeitbasierten Ausstieg oder Stop-Loss begrenzt.
- Zusammen mit Mean-Reversion-Strategien entstehen höhere Sharpe Ratios und kleinere Drawdowns als mit jedem Typ allein.
- Die meisten Aktien und Futures zeigen oft Zeitreihenmomentum, typischerweise über einen Monat oder länger.
- Dass Nachrichtenereignisse Zeitreihenmomentum erzeugen, ist lange bekannt; der Text stellt Forschung je Ereigniskategorie vor.
- Gewinnmeldungen, Änderungen von Analystenempfehlungen und Makronachrichten können es auslösen.
- Die Persistenz der Roll Return erzeugt intraday kein relevantes Zeitreihenmomentum, weil Größe und Volatilität zu klein sind.
- Eine zusätzliche kurzfristige Ursache ist das Auslösen von Stops.
- Orderflow sagt die kurzfristige Preisbewegung in derselben Richtung voraus und ist damit eine Quelle kurzfristigen Zeitreihenmomentums.
- Momentum-Trader in der Hypothese von Hong und Stein beschränken ihre Aufmerksamkeit auf vergangene Preisänderungen und leiten daraus ihre private Prognose künftiger Trends ab.
- Trendfolge unterstellt, dass neu entstehende Preistrends anzeigen, wichtige neue Fundamentalinformation beginne, sich im Markt zu verbreiten. Die Wette lautet, die Verbreitung sei unvollständig und der Preistrend setze sich nach dem anfänglichen Momentum-Signal fort.
- Damit Momentum- oder Trendfolge-Strategien funktionieren, müssen sich die Preise allmählich genug ändern, dass ein auf einer anfänglichen Preisänderung beruhendes Signal weitere Preisänderung vorhersagt.
- Die Handlungen späterer Wellen von Trendfolgern halten die Preise in Bewegung und erzeugen positives Preis-Feedback.
- Weil Momentum-Trader nicht beurteilen können, in welchem Maß die Nachricht schon diffundiert und verstanden ist, können die Preise weiter laufen, als die Fundamentaldaten rechtfertigen. Ist die Nachricht vollständig diffundiert und haben alle gehandelt, ist keine weitere Bewegung fundamental gerechtfertigt.
- Manche Trends entstehen, weil ein Preisanstieg weiteres Kaufen und Preisschwäche weiteres Verkaufen anregt. Diese Anleger suchen Signale in den jüngsten Preisänderungen statt in Nachrichten.
- Andere Fälle von Preismomentum sind das Aufholen der Preise nach einer anfänglichen Unterreaktion auf Nachrichten, wenn die Preise die Fundamentaldaten erst allmählich einholen.
- Gemessen wird Zeitreihenmomentum über den Korrelationskoeffizienten vergangener und künftiger Renditen samt p-Wert; als Lookback und Haltedauer dient das Paar mit der höchsten positiven Korrelation.
- Alternativ werden nur die Vorzeichen der Renditen korreliert, wenn die ähnliche Größe der Bewegungen egal ist.
- Ohne festes Zeitfenster dienen Hurst-Exponent und Variance-Ratio-Test als Momentum-Tests und sollen einen Random Walk ausschließen.
- Für TU sind die besten Kompromisspaare (60, 10), (60, 25), (250, 10), (250, 25), (250, 60) und (250, 120); gewählt wird 250 und 25 mit einem Koeffizienten von 0,27 und einem p-Wert von 0,02.
- Der Hurst-Exponent von TU ist 0,44, und der Variance-Ratio-Test verwirft den Random Walk nicht, weil die Reihe je nach Zeitrahmen Momentum oder Mean Reversion zeigt.
- Die einfache Regel kauft bei positiver und verkauft bei negativer 12-Monats-Rendite; statt monatlich wird täglich entschieden, und jeden Tag nur ein Fünfundzwanzigstel des Kapitals eingesetzt.
- Vom 1. Juni 2004 bis 11. Mai 2012 hat TU eine Sharpe Ratio von 1 und 1,7 Prozent annualisiert auf etwa 200.000 Dollar Nominalwert, bei etwa 400 Dollar Margin und 2,5 Prozent maximalem Drawdown.
- Tabelle 6.2: BR Lookback 100 und Haltedauer 10 mit 17,7 Prozent und Sharpe 1,09; HG 40 und 40 mit 18,0 Prozent und Sharpe 1,05; TU 250 und 25 mit 1,7 Prozent und Sharpe 1,04.
- Die serielle Korrelation entsteht, weil das Vorzeichen der Rollrendite lange gleich bleibt und die Rollrendite die Gesamtrendite dominieren kann; das gilt für BR, HG und TU, nicht aber für C.
- Die verzögerte Rollrendite ist ein saubereres Signal: long über der Schwelle, short unter der negativen Schwelle, sonst glatt; bei annualisiert 3 Prozent auf TU folgen 2,5 Prozent APR, Sharpe 2,1 und 1,1 Prozent maximaler Drawdown.
- Ein Mean-Reversion-Filter auf dieser Regel verbessert die vorhandenen Kontrakte und nimmt IBX, KT, SXF, US, CD, NG und W hinzu.
- Der S&P DTI setzt Zeitreihenmomentum über 24 Futures um, long über und short unter dem exponentiellen gleitenden Durchschnitt, monatlich rebalanciert, mit einer Sharpe Ratio von 1,3 von Januar 1988 bis Dezember 2010 und schlechter Leistung seit 2008.
- Beispiel 1.1 zeigt, dass eine Renditereihe mit der Kurtosis der TU-Futures und ohne serielle Autokorrelation in 12 Prozent der Zufallsziehungen dieselben Renditen wie die TU-Zeitreihen-Momentum-Strategie erzeugen kann.
- Die Dauer kürzerfristigen nachrichtengetriebenen Momentums wird kürzer, je mehr Händler es aufgreifen, sodass die Haltedauer womöglich ständig ohne festen Zeitplan verkürzt werden muss.
- Momentum-Strategien zusätzlich zu Mean Reversion erzeugen höhere Sharpe Ratios und kleinere Drawdowns als Zeitreihenmomentum allein.
- Der Horizont von Cross-Sectional- und Zeitreihenmomentum ist typischerweise ein Monat oder länger.
- Lange Haltedauern senken die Sharpe Ratio und die statistische Signifikanz und underperformen nach Finanzkrisen; Intraday-Zeitreihenmomentum hat diese Nachteile nicht.
- Von den vier Hauptursachen wirkt intraday alle außer der Persistenz der Rollrendite, weil deren Betrag und Volatilität intraday zu klein sind.
- Auf der kürzesten Skala erzeugen Bid-Ask-Ungleichgewicht, Änderungen im Orderflow und ungleich verteilte Stop-Orders Zeitreihenmomentum.
- Dass Ereignisse Zeitreihenmomentum erzeugen, ist lange bekannt; der Text stellt Forschung zu den einzelnen Ereigniskategorien vor, und die Dauer wird kürzer, je bekannter der Effekt ist.

## Funktionsweise

- Die TU-Momentum-Strategie kauft den TU-Future, wenn seine 12-Monats-Rendite positiv ist, verkauft ihn, wenn sie negativ ist, und hält die Position einen Monat.
- Ein Beispielfaktor, ob die morgige Indexrendite positiv ist, ist die heutige Rendite: Eine positive heutige Rendite sagt eine positive künftige Rendite voraus.
- Ein weiterer Faktor ist die heutige Änderung des VIX. Eine negative Änderung sagt eine positive künftige Rendite voraus.
- Gemessen wird die Korrelation einer vergangenen Rendite über den Lookback mit einer künftigen Rendite über die Haltedauer, samt p-Wert, auf nicht überlappenden Paaren.
- Das Paar mit der höchsten positiven Korrelation wird Lookback und Haltedauer der Strategie.
- Alternativ wird nur die Korrelation der Vorzeichen geprüft, wenn die Beträge der Bewegungen gleichgültig sind.
- Ohne festes Fenster prüfen Hurst-Exponent und Variance-Ratio-Test langfristiges Trendverhalten gegen einen Random Walk.
- Futures zeigen Zeitreihenmomentum vor allem, weil das Vorzeichen der Rollrendite lange bestehen bleibt und die durchschnittliche Rollrendite die durchschnittliche Gesamtrendite dominieren kann.
- Das sauberere Signal ist deshalb die verzögerte Rollrendite statt der verzögerten Gesamtrendite, long über einer Schwelle, short unter der negativen Schwelle, sonst flach.
- Das Rebalancing gehebelter ETFs erzeugt kurzfristiges Momentum in Richtung der Marktrendite seit dem vorigen Schluss.
- Die TU-Momentum-Strategie kauft den TU-Future bei positiver und verkauft ihn bei negativer 12-Monats-Rendite und hält die Position einen Monat.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Kurze Haltedauern sind vorzuziehen, weil sie die besten Sharpe Ratios liefern, viele etablierte Zeitreihen-Strategien haben aber lange Fenster und damit wenige unabhängige Signale.
- Die wenigen Trades in der kurzen Testhistorie erzeugen ein Data-Snooping-Risiko; entschieden wird erst out of sample.
- Seit der Finanzkrise 2008 laufen solche Strategien schlecht, der S&P DTI hat seit dem 5. Dezember 2008 einen Drawdown von minus 25,9 Prozent.
- Die Dauer, über die das Momentum wirkt, wird kürzer, je mehr Händler es aufgreifen, und die Haltedauer muss womöglich ohne festen Zeitplan verkürzt werden.
- In Beispiel 1.1 erzeugt eine Reihe mit der Kurtosis der TU-Futures, aber ohne serielle Autokorrelation, in 12 Prozent der Zufallsziehungen dieselben Renditen wie die TU-Momentum-Strategie.
- Aufeinanderfolgende verlierende Positionen können trotzdem in die Insolvenz führen, und nach riskanten Ereignissen liefen die Strategien schlecht.
- Lange Haltedauern senken Sharpe Ratio und statistische Signifikanz und underperformen nach Finanzkrisen; die beschriebenen Intraday-Strategien haben diese Nachteile nicht.

## Beispiele

- Die Strategie wurde wegen ihrer Einfachheit und der festen Haltedauer gewählt, damit der dritte Hypothesentest nur die Starttage der Long- und Short-Trades randomisieren muss.
- Die Gauß-Teststatistik mean(ret)/std(ret)*sqrt(length(ret)) beträgt 2,93. Die Null einer mittleren Tagesrendite von null wird mit besser als 99 Prozent Wahrscheinlichkeit verworfen.
- Erzeugt die Strategie auf Zufallsreihen mit denselben Momenten, aber ohne die eingebetteten Korrelationen, mit guter Wahrscheinlichkeit eine mindestens ebenso gute Rendite, erfasst sie kein Momentum und keine seriellen Korrelationen.
- Von 10.000 solchen Reihen war das bei 1.166 der Fall. Die Null wird nur mit 88 Prozent Wahrscheinlichkeit verworfen. Die Form der Renditeverteilung hat etwas mit dem Erfolg zu tun, der Mittelwert weniger, weil die Position zu verschiedenen Zeiten long oder short sein kann.
- Im dritten Test, der die Einstiegstage bei gleicher Zahl von Long- und Short-Trades randomisiert, erreicht keine von 100.000 Stichproben die beobachtete durchschnittliche Strategierendite. Der Text nennt diesen dritten Test für diese Strategie deutlich schwächer.
- Von 10.000 Zufallsrendite-Reihen mit denselben Momenten haben 1.166 eine mindestens ebenso hohe durchschnittliche Strategierendite. Die Null wird nur mit 88 Prozent Wahrscheinlichkeit verworfen, und die Form der Verteilung hat etwas mit dem Erfolg zu tun.
- Für TU sind die besten Kompromisse (60, 10), (60, 25), (250, 10), (250, 25), (250, 60) und (250, 120); bei den Vorzeichen (60, 10), (250, 10) und (250, 25).
- Gewählt werden 250 und 25 Tage, mit Korrelation 0,27 und p-Wert 0,02; der Hurst-Exponent ist 0,44, und der Variance-Ratio-Test verwirft den Random Walk nicht.
- Statt einer Monatsentscheidung über die 12-Monats-Rendite wird täglich entschieden und jeden Tag ein Fünfundzwanzigstel des Kapitals eingesetzt.
- Vom 1. Juni 2004 bis zum 11. Mai 2012 hat TU eine Sharpe Ratio von 1, 1,7 Prozent annualisiert auf etwa 200.000 Dollar Nominal und einen maximalen Drawdown von 2,5 Prozent bei etwa 400 Dollar Margin.
- Die Schwelle von 3 Prozent annualisierter Rollrendite hebt TU vom 2. Januar 2009 bis zum 13. August 2012 auf 2,5 Prozent annualisiert, eine Sharpe Ratio von 2,1 und einen maximalen Drawdown von 1,1 Prozent.
- Dieselbe einfache Regel gilt für andere Futures mit anderen optimalen Fenstern: BR 100 und 10, HG 40 und 40.
- Die Erklärung passt zu BR, HG und TU, weil dort die Rollrendite betragsmäßig größer ist als die Spot-Rendite, und sie passt nicht zu C, trotz dessen größtem Rollrendite-Betrag gegen die Spot-Rendite.
- Britische Makrodaten und Zinsentscheide der Bank of England erzeugten in GBPUSD bis mindestens zehn Minuten Momentum (Clare und Courtenay, 2001, Daten bis 1999).
- Eigene Tests von Zinsentscheiden des Federal Open Market Committee und des Verbraucherpreisindex fanden auf EURUSD kein signifikantes Momentum.
- Der Drift nach Gewinnmeldungen läuft in derselben Richtung wie die unmittelbare Kursreaktion, im getesteten Intraday-Setup aber nicht über Nacht.
- Die gaußsche Teststatistik mean der Tagesrenditen geteilt durch ihre Standardabweichung mal der Wurzel der Länge beträgt 2,93, die Null wird mit besser als 99 Prozent verworfen.
- Der Erfolg liegt weniger am Mittelwert der Renditeverteilung, weil die Position zu verschiedenen Zeiten long oder short sein kann; die Form der Verteilung hat mit dem Erfolg zu tun.
- Im dritten Test der TU-Strategie, der die Einstiegstage bei gleicher Zahl von Long- und Short-Trades vertauscht, erreicht unter 100.000 Ziehungen keine die beobachtete Durchschnittsrendite; der Text nennt diesen Test für die Strategie viel schwächer.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 173–186 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-013-p173-p186|S. 173–186]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 362–381 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-020-p362-p381|S. 362–381]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 1–13 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-001-p001-p013|S. 1–13]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 14–33 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-002-p014-p033|S. 14–33]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 33–51 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-003-p033-p051|S. 33–51]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 144–163 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-011-p144-p163|S. 144–163]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 163–165 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-012-p163-p165|S. 163–165]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 166–179 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-013-p166-p179|S. 166–179]]

## Verwandte Themen
