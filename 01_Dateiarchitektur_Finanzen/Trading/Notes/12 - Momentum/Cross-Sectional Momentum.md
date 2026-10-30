---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/12 - Momentum/12 - Momentum|12 - Momentum]]"
weitere_hauptthemen: []
unterthema: "Relative Stärke"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Cross-Sectional Momentum


## Kurzdefinition

- Cross-Sectional Momentum bezeichnet die relative Leistung einer Preisreihe gegenüber anderen Preisreihen: eine Reihe, die andere geschlagen hat, tut das künftig wahrscheinlich weiter, und umgekehrt, nach Moskowitz, Yao und Pedersen 2010.
- Cross-Sectional Momentum ist die positive Korrelation der vergangenen und künftigen relativen Renditen einer Preisreihe, bezogen auf die anderen Preisreihen eines Portfolios.

## Kernaussagen

- Vorgeschlagen werden Strategien, die Zeitreihenmomentum und Cross-Sectional-Momentum extrahieren.
- Das Hauptthema des Momentum-Teils ist, die vier Haupttreiber von Momentum bei Aktien und Futures zu erkunden.
- Roll Returns bei Futures sind einer dieser Treiber.
- Erzwungene Käufe und Verkäufe von Assets sind in vielen unterschiedlichen Umständen der Haupttreiber von Aktien- und ETF-Momentum.
- Neuere Momentum-Strategien beruhen auf Nachrichtenereignissen, News Sentiment, gehebelten ETFs, Orderflow und Hochfrequenzhandel.
- Momentum- und Mean-Reversion-Strategien haben unter verschiedenen Marktregimes der jüngeren Finanzgeschichte diametral verschiedene Risiko-Rendite-Eigenschaften.
- Querschnittliches Momentum von Währungen und Aktien lässt sich nicht mehr mit dem Vorzeichen der Rollrendite erklären; für Währungen kommt serielle Korrelation des Weltwirtschafts- oder Zinswachstums infrage, für Aktien die langsame Diffusion, Analyse und Aufnahme neuer Information.
- Für Aktien gilt Gesamtrendite gleich Marktrendite plus Faktor-Renditen; ein querschnittliches Portfolio eliminiert die Marktrendite, und seine Rendite wird nur von den Faktoren getrieben.
- Diese Faktoren können fundamental sein, etwa Gewinnwachstum oder das Verhältnis Buchwert zu Preis oder eine Linearkombination daraus, oder statistisch, etwa aus einer Hauptkomponentenanalyse nach Chan 2009.
- Mit möglicher Ausnahme der Hauptkomponenten ändern diese Faktoren langsam, deshalb werden die Haltedauern so lang wie bei den querschnittlichen Modellen dieses Abschnitts.
- Ein Faktormodell lässt sich auch auf ein querschnittliches Futures-Portfolio anwenden, mit Makrofaktoren wie BIP-Wachstum oder Inflationsrate oder wiederum mit einer Hauptkomponentenanalyse.
- Hafez und Xie kaufen mit dem RavenPack Sentiment Index ein Portfolio mit positiver Sentimentänderung und shorten eines mit negativer Änderung und erhalten, je nach Aktienzahl, vor Kosten annualisierte Renditen von 52 bis 156 Prozent und Sharpe Ratios von 3,9 bis 5,3.
- Der Erfolg dieser Sentiment-Strategien zeigt, dass die langsame Diffusion von Nachrichten die Ursache des Aktienmomentums ist.
- Portfolios aus Futures oder Aktien zeigen oft querschnittliches Momentum, und ein einfacher Rang-Algorithmus auf den Renditen genügt.
- Die Ansteckung erzwungener Verkäufe und Käufe unter Publikumsfonds trägt zum Aktienpreismomentum bei.
- Profitable Strategien auf News-Sentiment-Momentum zeigen, dass die langsame Diffusion von Nachrichten eine Ursache des Aktienpreismomentums ist.

## Funktionsweise

- Ein dritter Weg zu den Rollrenditen ist, ein Portfolio von Futures in Backwardation zu kaufen und zugleich ein Portfolio von Futures in Contango zu shorten, in der Hoffnung, dass sich die Spot-Renditen aufheben und die günstigen Rollrenditen übrig bleiben.
- Diese Hoffnung setzt voraus, dass die Spotpreise der Rohstoffe positiv mit Wirtschaftswachstum oder anderen Makroindizes korreliert sind.
- Die vereinfachte Strategie rangiert täglich die 12-Monats-Rendite, im Programm 252 Handelstage, von 52 physischen Rohstoffen, kauft den Future mit der höchsten Rendite für einen Monat, 25 Handelstage, und shortet den Future mit der niedrigsten Rendite über dieselbe Frist.
- Die Strategie von Daniel und Moskowitz 2011 ist fast ein Spiegelbild des linearen Long-Short-Mean-Reversion-Modells von Khandani und Lo, aber mit deutlich längerem Lookback und längerer Haltedauer.
- Auf US-Aktien werden der oberste und der unterste Dezil der um 12 Monate verzögerten Renditen einen Monat gehalten.
- In Beispiel 6.2 ist der Lookback 252, die Haltedauer 25 und topN 50 auf den Schlusskursen der S&P-500-Titel; fehlende Renditen werden aus der Rangfolge ausgeschlossen, die obersten 50 werden long und die untersten 50 short.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Die Finanzkrise 2008 bis 2009 zerstört diese Momentum-Strategie bei Futures wie bei Aktien, ebenso wie den S&P DTI.
- Auf demselben S&P-500-Universum hat die lineare kurzfristige Mean Reversion aus Kapitel 4 eine Haltedauer von weniger als einem Tag und eine Sharpe Ratio von 4,7, während die gegenläufige querschnittliche Momentum-Strategie 25 Tage hält, vor 2008 ähnlich gut läuft und in den Krisenjahren zusammenbricht.

## Beispiele

- Auf den 52 Rohstoffen beträgt die annualisierte Rendite vom 1. Juni 2005 bis zum 31. Dezember 2007 18 Prozent bei einer Sharpe Ratio von 1,37 und vom 2. Januar 2008 bis zum 31. Dezember 2009 minus 33 Prozent, mit Erholung danach.
- Beispiel 6.2 erzielt vom 15. Mai 2007 bis zum 31. Dezember 2007 eine annualisierte Rendite von 37 Prozent bei einer Sharpe Ratio von 4,1; Daniel und Moskowitz finden von 1947 bis 2007 16,7 Prozent annualisiert bei einer Sharpe Ratio von 0,83.
- Dieselbe Aktienstrategie erzielt vom 2. Januar 2008 bis zum 31. Dezember 2009 eine annualisierte Rendite von minus 30 Prozent; nach 2009 stabilisiert sich die Rendite, ohne das frühere Hoch zu erreichen.
- Dieselbe Strategie funktionierte nach Daniel und Moskowitz für Welt-Aktienindizes, Währungen, internationale Aktien und US-Aktien.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 1–20 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-001-p001-p020|S. 1–20]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 343–362 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-019-p343-p362|S. 343–362]]

## Verwandte Themen
