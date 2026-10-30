---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/06 - Volumenanalyse/06 - Volumenanalyse|06 - Volumenanalyse]]"
weitere_hauptthemen: []
unterthema: "Volumenindikatoren"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# On-Balance Volume


## Kurzdefinition

- Der kumulative On-Balance-Volume-Indikator gilt als vielleicht die erste Preis-Volumen-Funktion und wird Joseph Granville sowie Woods und Vignolia zugeschrieben.
- Er ist die kumulative Summe des mit Vorzeichen versehenen gesamten Marktvolumens; das Vorzeichen folgt dem Vorzeichen der Änderung eines Marktindex im gewählten Zeitintervall.

## Kernaussagen


## Funktionsweise

- Die Fallstudie nahm die tägliche Änderung des S&P 500: stieg der Index, wurde das gesamte NYSE-Volumen positiv zum bisherigen Stand addiert, fiel er, wurde es negativ addiert, also abgezogen.
- Bei unverändertem Schluss ist der Faktor ft gleich 0; bei höherem Schluss ist ft gleich 1 und bei tieferem Schluss gleich −1.
- Das Tages-On-Balance-Volume ist der Faktor ft mal dem NYSE-Volumen, und der kumulative Stand ist der Vortagesstand plus dieses Produkt.
- Zusätzlich wurden gleitende Durchschnitte über 10 und 30 Tage gebildet: OBV10 gleich MA(OBV, 10) und OBV30 gleich MA(OBV, 30).
- Tabelle 8.2 führt Cumulative On-Balance Volume sowie OBV10 und OBV30 als Eingabereihen 9 bis 11.

## Voraussetzungen


## Anwendung im Trading

- Hsu und Kuan bilden komplexe Regeln auch über alle einfachen Regeln eines Themas, zum Beispiel alle Regeln, die auf einem gleitenden Durchschnitt des On-Balance Volume beruhen.
- Sie betrachteten 2.040 On-Balance-Volume-Regeln.
- Signalisierten davon 1.158 eine Short-Position und 882 eine Long-Position, wurde eine Short-Position von 0,135 Einheiten genommen, weil (882 minus 1.158) geteilt durch 2.040 gleich −0,135 ist.
- Das Voting innerhalb desselben Themas nimmt eine Position von einer Einheit in Richtung der Mehrheit der einfachen Regeln.
- Die Fractional Position desselben Themas skaliert die Positionsgröße mit dem Nettoanteil der Regeln, die long sind, minus der Regeln, die short sind, geteilt durch die Gesamtzahl.

## Regeln und Kriterien


## Risiken und Grenzen

- Als Schwäche gilt, dass schon eine winzige positive oder negative Kursänderung das gesamte Tagesvolumen positiv oder negativ setzt.
- Chaikens Accumulation Distribution sowie Bostians Intra-day Intensity und Williams’ Variable Accumulation Distribution sollten dieses Alles-oder-nichts mildern, indem kleine Kursänderungen nicht wie große behandelt werden.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 400–419 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-022-p400-p419|S. 400–419]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]

## Verwandte Themen

- Granville stellt On-Balance Volume in Granville's New Strategy of Daily Stock Market Timing for Maximum Profit (1976) dar.
- Die Zuschreibung an Woods und Vignolia findet sich im Abschnitt Body of Knowledge auf der Website der Market Technicians Association.
- Die im Text verwendete Formulierung des On-Balance Volume ist die aus dem Technical Indicators Reference Manual für AIQ Trading Export Pro von AIQ Systems.
