---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/20 - Trading-Performance & Auswertung/20 - Trading-Performance & Auswertung|20 - Trading-Performance & Auswertung]]"
weitere_hauptthemen: []
unterthema: "Renditekennzahlen"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Trefferquote


## Kurzdefinition

- Die Trefferquote ist der Anteil der Wetten mit positivem PnL.
- Die Trefferwahrscheinlichkeit p ist die Wahrscheinlichkeit, mit der die Gewinnauszahlung einer Wette eintritt.

## Kernaussagen

- Die Trefferquote gehört zu den Performance-Kennzahlen ohne Risikoanpassung.
- Bei der Beurteilung von Runs ist eine hohe Trefferquote erwünscht, verbunden mit relativ wenigen Verlustwetten.
- Im Bild eines binären Klassifikators entspricht p der Precision: richtige Positive werden belohnt, falsche Positive werden bestraft, und Negative haben keine Auszahlung.
- Die Sharpe Ratio hängt in diesem Modell von der Precision ab.
- Viele Negative verkleinern die Zahl der Wetten und ziehen die Sharpe Ratio gegen null.
- Die beobachtete Trefferquote ist der Anteil der positiven Ergebnisse an allen Wetten.
- Die kritische Trefferwahrscheinlichkeit ist der Wert, unter dem die Strategie eine vorgegebene Ziel-Sharpe-Ratio verfehlt.
- Die Ausfallwahrscheinlichkeit der Strategie ist die Wahrscheinlichkeit, dass die Trefferquote unter diesem kritischen Wert liegt.
- Im Beispiel traf das Kaufsignal der Regel X in 700 von 1.000 Fällen zu, indem der Markt über die nächsten 10 Tage höher lag, und der induktive Schluss setzt diese Wahrscheinlichkeit für künftige Signale auf 0,7.
- Dieselbe Erfolgsquote von 70 Prozent auf nur 10 statt 1.000 Fällen machte den Schluss mindestens zehnmal unsicherer, sodass die künftige Treffgenauigkeit stark von der historischen Erfolgsquote abweichen kann.
- Je zahlreicher die angeführten Fälle und je höher ihre Qualität, desto wahrscheinlicher verallgemeinert sich die Trefferaussage zutreffend auf künftige Beobachtungen.
- Nichtuniverselle Verallgemeinerungen, auch probabilistische Verallgemeinerungen genannt, haben die Form, dass P Prozent der X die Eigenschaft Y haben oder dass X die Eigenschaft Y mit der Wahrscheinlichkeit P hat.
- Die Genauigkeit einer künstlichen Handelsregel ist der Anteil richtiger Signale und lässt sich experimentell setzen.
- Die erwartete Rendite wird gesteuert, indem die Wahrscheinlichkeit eines profitablen Monats verändert wird.
- Diese Wahrscheinlichkeit zeigt sich über eine sehr große Zahl von Monaten nach dem Gesetz der großen Zahlen; in jeder kleinen Monatsstichprobe schwankt der tatsächliche Anteil profitabler Monate zufällig um die vorgegebene Wahrscheinlichkeit.
- Eine gesetzte Wahrscheinlichkeit von 0,70 entspricht einem Roulette mit 100 Fächern, davon 70 Gewinn und 30 Verlust.
- Bei Gewinnwahrscheinlichkeit 0,50 und 24 Monaten liegt die mittlere Rendite ohne Data Mining im Schnitt bei null; wird die beste aus zwei oder mehr Regeln gewählt, zeigt sie wahrscheinlich eine Rendite über null, obwohl der Erwartungswert null ist.
- Für die Tests mit unterschiedlicher Güte wurde die Wahrscheinlichkeit eines profitablen Monats jeder Regel zufällig aus einer Verteilung gezogen, die der Vermögensverteilung ähnelt und einen langen rechten Rand hat.
- Regeln mit hoher erwarteter Rendite gelten als selten: eine erwartete Jahresrendite von 19 Prozent oder mehr trat etwa einmal unter 10.000 auf.
- Werden nur zwei Monate benutzt, ist die Wahl der Regel mit der besten beobachteten Performance nicht besser, als eine Regel zufällig aus dem Universum zu ziehen, und es ist gleichgültig, wie viele Regeln getestet werden.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- Bei einem Gewinnziel von 0,1 und einer Ziel-Sharpe-Ratio von 1,5 steigt die nötige Trefferwahrscheinlichkeit, wenn die Verlustauszahlung negativer wird oder die jährliche Wettzahl sinkt.

## Regeln und Kriterien

- Liegt die Wahrscheinlichkeit, die kritische Trefferquote zu unterschreiten, über 0,05, wird die Strategie typischerweise als zu riskant verworfen.
- Die Verwerfungsgrenze von 0,05 gilt auch für Anlagen in Instrumenten mit niedriger Volatilität.
- Soll die Strategie eingesetzt werden, muss die kritische Trefferwahrscheinlichkeit gesenkt werden.
- Gesetze unterscheiden sich in ihrer Vorhersagekraft, und die mit den konsistentesten Beziehungen sind die wertvollsten.
- Bei sonst gleichen Bedingungen ist eine Regel der technischen Analyse, die in 52 Prozent der Fälle erfolgreich ist, weniger wertvoll als eine, die in 70 Prozent der Fälle funktioniert.

## Risiken und Grenzen

- Der häufigste Induktionsfehlschluss ist die voreilige Verallgemeinerung aus zu wenigen oder qualitativ schlechten Belegen; Regelstudien mit nur wenigen erfolgreichen Signalen gehören vermutlich dazu.

## Beispiele

- Bei symmetrischer Auszahlung und einer Trefferwahrscheinlichkeit von 0,55 erfordert eine annualisierte Sharpe Ratio von 2 insgesamt 396 Wetten pro Jahr.
- Bei 52 Wetten pro Jahr ist für eine annualisierte Sharpe Ratio von 2 eine Trefferwahrscheinlichkeit von 0,6336 nötig.
- Bei 260 Wetten, Verlustauszahlung minus 0,01 und Gewinnauszahlung 0,005 liefert eine Trefferwahrscheinlichkeit von 0,7 eine annualisierte Sharpe Ratio von 1,173.
- Bei 260 Wetten, Verlustauszahlung minus 0,01 und Gewinnauszahlung 0,005 liefert eine Trefferwahrscheinlichkeit von 0,72 eine annualisierte Sharpe Ratio von 2.
- Bei Verlustauszahlung minus 0,01 und Gewinnauszahlung 0,005 liegt die kritische Trefferwahrscheinlichkeit für eine Sharpe Ratio von null bei zwei Dritteln.
- Bei Verlustauszahlung minus 0,01 und Gewinnauszahlung 0,005 zehrt ein Rückgang der Trefferwahrscheinlichkeit von 0,7 auf 0,67 den erwarteten Gewinn auf.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 96–115 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-006-p096-p115|S. 96–115]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 115–134 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-007-p115-p134|S. 115–134]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 286–305 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-016-p286-p305|S. 286–305]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 305–324 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-017-p305-p324|S. 305–324]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 153–172 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-012-p153-p172|S. 153–172]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 172–176 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-013-p172-p176|S. 172–176]]

## Verwandte Themen
