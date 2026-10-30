---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/11 - Indikatoren/11 - Indikatoren|11 - Indikatoren]]"
weitere_hauptthemen: []
unterthema: "Kanalindikatoren"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Donchian Channels


## Kurzdefinition

- Der n-Perioden-Kanalausbruch schließt eine Zeitreihe in einen Kanal. Die untere Grenze ist das Minimum der Reihe über die vergangenen n Perioden ohne die aktuelle Periode, die obere Grenze das Maximum über dieselben vergangenen n Perioden ohne die aktuelle Periode.

## Kernaussagen


## Funktionsweise

- Trotz extremer Einfachheit hat sich der Kanalausbruch als so wirksam erwiesen wie komplexere Trendfolge-Methoden.
- Mit jedem neuen Datenpunkt wird der Kanal neu gezeichnet. Die Rückschau auf der Zeitachse bleibt konstant, die vertikale Breite gegenüber der Wertachse passt sich dynamisch der Spanne der Reihe über die letzten n Perioden an.
- Diese dynamische Spanne kann erklären, warum die Methode wirksam ist: Sie kann die Wahrscheinlichkeit falscher Signale senken, die von einem Anstieg der Volatilität der Reihe verursacht werden und nicht von einer tatsächlichen Trendänderung.
- Der Zweck aller Trendidentifikation ist, am Rauschen vorbeizusehen, an den erratischen Bewegungen, die bedeutungslos scheinen, und die aktuelle Richtung der Reihe zu finden.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Wie üblich gedeutet, signalisiert der Operator Long, wenn die untersuchte Reihe ihr Maximum der vergangenen n Perioden überschreitet, und Short, wenn die Reihe unter ihr n-Perioden-Minimum fällt.
- Der einzige freie Parameter ist die Rückschau. Im Allgemeinen gilt: Je größer die Rückschau, desto breiter der Kanal und desto unempfindlicher der Indikator. Größere n identifizieren größere Trends.
- Die Fallstudie testete 11 verschiedene Rückschauen, deren Längen um einen Faktor von ungefähr 1,5 getrennt waren: 3, 5, 8, 12, 18, 27, 41, 61, 91, 137 und 205 Tage.

## Risiken und Grenzen


## Beispiele

- Kaufman berichtet, dass eine Studie von Dunn & Hargitt aus dem Jahr 1970 einen Channel-Breakout mit Vier-Wochen-Spanne, Donchians Vier-Wochen-Regel, als bestes von mehreren populären Systemen fand, getestet auf 16 Jahren Daten von sieben Rohstoffmärkten.
- Kaufman vergleicht Channel-Breakout-Regeln mit vier anderen Trendfolge-Methoden, exponentieller Glättung, Steigung der linearen Regression, Swing-Breakout und Point-and-Figure, an Eurodollars für die zehn Jahre 1985 bis 1994.
- Die Channel-Breakout-Methode hatte in diesem Vergleich über die zehn Jahre die höchste risikobereinigte Performance.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 381–400 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-021-p381-p400|S. 381–400]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 400–419 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-022-p400-p419|S. 400–419]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]

## Verwandte Themen
