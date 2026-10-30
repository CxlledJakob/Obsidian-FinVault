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


## Funktionsweise


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


## Beispiele

- Die Vier-Parameter-Regel, die die RSI-Schwellen einschließt, verdiente im Trainingsset 50 Prozent gegenüber 30 Prozent der Zwei-Parameter-Vorgängerregel.
- Im Testset verdiente diese Vier-Parameter-Regel 20 Prozent gegenüber 15 Prozent der einfachen Regel aus zwei gleitenden Durchschnitten.
- Die bessere Testset-Leistung der komplexeren Regel legt nahe, dass die zusätzliche Komplexität weitere systematische Aspekte des Marktverhaltens ausgenutzt hat.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 457–476 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-025-p457-p476|S. 457–476]]

## Verwandte Themen
