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
aktualisiert: 2026-10-30
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

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 173–186 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-013-p173-p186|S. 173–186]]

## Verwandte Themen
