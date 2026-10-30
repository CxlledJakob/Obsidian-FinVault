---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/11 - Indikatoren/11 - Indikatoren|11 - Indikatoren]]"
weitere_hauptthemen: []
unterthema: "Oszillatoren"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Relative Strength Index


## Kurzdefinition


## Kernaussagen

- Der DTosc ist ein proprietärer Indikator der Software Dynamic Trader.
- Der DTosc ist eine Kombination aus Stochastic und Relative Strength Index.
- Der Autor bevorzugt einen Indikator wie den DTosc oder einen Stochastic oder einen anderen Indikator mit Overbought- und Oversold-Zonen.
- Im Indikatorfenster des DTosc stehen vier Zahlen: Die erste ist die rohe Lookback-Periode, die übrigen sind die Perioden, über die die Rohdaten geglättet werden.
- Bei einem Zweilinien-Indikator wie dem DTosc müssen schnelle und langsame Linie beide in der Overbought- oder Oversold-Zone liegen, damit der Indikator als overbought oder oversold gilt.
- Der MACD oder ein anderer vertrauter Indikator kann ebenso nützlich sein wie ein Indikator mit Overbought- und Oversold-Zonen.

## Funktionsweise

- Ein Relative Strength Index mit zwei Linien macht eine Momentum-Umkehr, wenn die schnelle Linie über oder unter die langsame kreuzt.
- Die schnelle Linie ist bei den meisten Zwei-Linien-Indikatoren gewöhnlich die Rohdaten, die langsame gewöhnlich ein gleitender Durchschnitt der schnellen Linie.
- In Abbildung 2.1 werden Stochastic, RSI und der DT Oscillator verglichen, der eine Kombination aus RSI und Stoch ist; alle vier Studien einschließlich eines einfachen ROC haben eine Acht-Perioden-Rückschau.
- Die Momentumtrends von Stochastic, RSI und DTosc sind ungefähr gleich, und die Umkehren der schnellen über die langsame Linie liegen innerhalb von ein oder zwei Balken voneinander, auch ohne Justierung der Einstellungen.
- Fast jeder preisbasierte Momentum-Indikator, also auch der RSI, kann für die Multiple-Time-Frame-Momentum-Strategie genutzt werden, weil alle die Änderungsrate und dieselben Momentum-Zyklen darstellen.

## Voraussetzungen


## Anwendung im Trading

- Im Beispiel der geführten Komplexitätsoptimierung wird eine Umkehrregel aus zwei gleitenden Durchschnitten um eine Regel auf Wilders Relative Strength Index ergänzt, einem Indikator, der die Rate der Preisänderung misst.
- Der Relative Strength Index dient als Filter: liegt er beim Verkaufssignal des Doppel-Durchschnitt-Crossover über der Schwelle rsi_max, wird eine neutrale Position statt einer Short-Position genommen.
- Liegt der Relative Strength Index beim Kaufsignal unter der Schwelle rsi_min, wird eine neutrale Position statt einer Long-Position genommen.
- Diese komplexere Regel hat vier optimierbare Parameter: die Spanne des kurzen gleitenden Durchschnitts, die Spanne des langen gleitenden Durchschnitts, rsi_max und rsi_min.
- Im unterstellten Zahlenbeispiel verdient die Vier-Parameter-Regel 50 Prozent im Training gegenüber 30 Prozent der Zwei-Parameter-Regel und 20 Prozent im Test gegenüber 15 Prozent.
- Schneidet eine komplexere Regel im Testsatz besser ab, ist die vernünftige Annahme, die zusätzliche Komplexität habe weitere systematische Aspekte des Marktverhaltens ausgenutzt.

## Regeln und Kriterien

- Die komplexere Regel hat vier optimierbare Parameter, darunter rsi_max und rsi_min, neben der Spanne des kurzen und der Spanne des langen gleitenden Durchschnitts.
- Eine große Zahl von Kombinationen dieser Parameter wird gegen die Trainingsdaten laufen gelassen.

## Risiken und Grenzen

- Es gibt keinen magischen Indikator für Momentum-Handel; alle Momentum-Indikatoren stellen dieselben Zyklen dar und kehren etwa zur selben Zeit um.

## Beispiele

- Die Vier-Parameter-Regel, die die RSI-Schwellen einschließt, verdiente im Trainingsset 50 Prozent gegenüber 30 Prozent der Zwei-Parameter-Vorgängerregel.
- Im Testset verdiente diese Vier-Parameter-Regel 20 Prozent gegenüber 15 Prozent der einfachen Regel aus zwei gleitenden Durchschnitten.
- Die bessere Testset-Leistung der komplexeren Regel legt nahe, dass die zusätzliche Komplexität weitere systematische Aspekte des Marktverhaltens ausgenutzt hat.
- Am täglichen S&P 500 mit 21 Tagen roher DTosc-Lookback-Periode oszillierte der Indikator mit den Preisschwüngen, doch die meisten Momentumumkehren erreichten die Overbought- oder Oversold-Zone nicht.
- Dieselbe Serie mit 8 Tagen roher Lookback-Periode machte die Momentumumkehren an Hochs und Tiefs tendenziell in den Overbought- und Oversold-Zonen und auf oder innerhalb von ein oder zwei Bars zum Preishoch oder -tief.
- Mit 13 Tagen roher Lookback-Periode war der DTosc unter den drei geprüften Einstellungen die beste für diese Daten.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 457–476 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-025-p457-p476|S. 457–476]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 23–42 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-003-p023-p042|S. 23–42]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 42–61 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-004-p042-p061|S. 42–61]]

## Verwandte Themen
