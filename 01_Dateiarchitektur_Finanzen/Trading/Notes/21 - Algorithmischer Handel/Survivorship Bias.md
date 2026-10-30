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

# Survivorship Bias


## Kurzdefinition

- Survivorship Bias heißt, das heutige Anlageuniversum zu verwenden und damit zu ignorieren, dass Unternehmen auf dem Weg pleitegingen und Titel delisted wurden.

## Kernaussagen

- Survivorship Bias wirkte in der Behauptung, ein Stop-Loss senke immer die Performance von Mean-Reversion-Strategien.
- Reihen, die von Mean Reversion zu Momentum wechseln, erscheinen nicht im Katalog, weil gescheiterte Backtests nicht aufgenommen wurden.
- Jede erfolgreich gebacktestete Mean-Reversion-Strategie trägt diesen Bias und zeigt bei aufgezwungenem Stop-Loss niedrigere Performance.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- Überlebensbereinigte historische Daten zu vernünftigen Preisen gibt es bei csidata.com, das eine Liste delisteter Aktien liefert. Weitere Anbieter sind kibot.com, tickdata.com und crsp.com.
- Eigene bereinigte Daten entstehen, indem jeden Tag die historischen Preise aller Aktien eines Index gespeichert werden.
- Fehlen solche Daten, lässt sich der Schaden begrenzen, indem nur etwa die jüngsten drei Jahre Historie gebacktestet werden.

## Regeln und Kriterien

- Die erste Frage an eine solche Strategie ist, ob die Aktiendatenbank frei von Survivorship Bias ist, also Aktien enthält, die seither delisted wurden.
- Erwähnt der Autor nicht ausdrücklich, dass die Daten delistete Aktien enthalten, ist von Survivorship Bias auszugehen, und die Rendite ist wahrscheinlich aufgebläht.
- Bei einem reinen Long-Modell ist zu prüfen, ob die Daten frei von Survivorship Bias sind.
- Deshalb wird der Stop-Loss größer gewählt als der maximale Intraday-Drawdown des Backtests.

## Risiken und Grenzen

- Survivorship Bias ist die erste der sieben Sünden des quantitativen Investierens bei Luo et al. 2014, und die meisten in Zeitschriften veröffentlichten Arbeiten begehen solche Grundfehler routinemäßig.
- Der Bias ist für mean-revertierende Long-only-Aktienstrategien gefährlicher als für mean-revertierende Long-Short- oder Short-only-Strategien.
- Er bläht den Backtest einer Long-only-Strategie auf, die erst tief kauft und dann hoch verkauft, und er drückt den Backtest einer Short-only-Strategie, die erst hoch verkauft und dann tief kauft. Aktien, die auf null fielen, hätten short sehr gut abgeschnitten, fehlen in den verzerrten Daten aber.
- Bei mean-revertierenden Long-Short-Strategien haben die beiden Effekte entgegengesetzte Vorzeichen. Die Aufblähung der Long-Seite überwiegt meist die Abwertung der Short-Seite, sodass die Gefahr kleiner, aber nicht beseitigt ist.
- Für Momentum-Modelle ist der Bias weniger gefährlich. Der profitable Short-Momentum-Trade fehlt in den verzerrten Daten tendenziell, und die Backtest-Rendite wird dadurch gedrückt.
- Die Aktienmodelle in diesem Buch nutzen Daten mit Survivorship Bias, weil Daten ohne diesen Bias umständlicher und teurer zusammenzustellen sind.
- Die Hoffnung ist, dass die Ergebnisse zumindest für das letzte Jahr oder die letzten zwei nicht zu unrealistisch sind.
- Ein Neu-Backtest auf biasfreien Daten muss beachten, dass der gewählte Index, typischerweise der S&P 500, seine Zusammensetzung über die Historie ändert; nötig ist eine Datenbank der historischen täglichen Indexzusammensetzungen.
- Das im Buy-on-Gap-Backtest verwendete Universum ist der S&P 500, aber eines mit Survivorship Bias.

## Beispiele

- Im Extremfall kauft das Modell die eine Aktie, die am Vortag am stärksten gefallen ist, und hält sie für immer. Live läuft das meist schlecht, weil das Unternehmen oft in die Insolvenz geht und die Position zu 100 Prozent verloren ist.
- Enthält die Historie nur Aktien, die bis heute überlebt haben, kann der Backtest ausgezeichnet aussehen: Gekauft wurde eine stark geschlagene Aktie, die danach überlebte, obwohl dieses Überleben im Live-Handel nicht vorhersehbar war.
- Eine einfache Buy-low-sell-high-Strategie kauft zu Jahresbeginn die zehn am niedrigsten bepreisten Aktien und hält sie ein Jahr. Der Backtest für 2001 zeigt 388 Prozent Rendite.
- Enthält die Datenbank nur Aktien, die bis heute überlebt haben, wählt die Strategie wahrscheinlich genau die glücklichen Überlebenden, die Anfang 2001 sehr billig waren. Mit diesem Rückblick sind 388 Prozent erreichbar.
- Enthält die Datenbank delistete Aktien, wählt die Strategie wahrscheinlich diese Titel, mit einem Verlust von fast 100 Prozent. Dieser Verlust wäre die realisierte Rendite gewesen, hätte man die Strategie 2001 gehandelt. Die 388 Prozent sind eine aufgeblähte Backtest-Rendite, die sich nie realisieren lässt.

## Unterschiedliche Quellenpositionen

- Genauer senkt der Stop-Loss die Performance nur, solange die Preise mean-reverting bleiben, und verbessert sie, wenn ein Regimewechsel zum Trend einsetzt.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]

## Verwandte Themen
