---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/13 - Volatilität/13 - Volatilität|13 - Volatilität]]"
weitere_hauptthemen: []
unterthema: "Volatilitätsmessung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Realisierte Volatilität


## Kurzdefinition

- Die horizontalen Barrieren sind eine dynamische Funktion der geschätzten Volatilität, gleich ob realisiert oder implizit.

## Kernaussagen

- Dieselbe feste Schwelle trifft auf sehr unterschiedliche realisierte Bar-Volatilitäten.
- Liegt die Schwelle weit über der herrschenden Volatilität, ist das Ziel zu hoch, liegt sie weit darunter, ist es zu niedrig.
- Die Volatilitäten von Volumen- und Dollar-Bars liegen deutlich näher an einer Konstanten als die von Zeit-Bars.

## Funktionsweise

- getDailyVol schätzt an Intraday-Zeitpunkten die Tagesvolatilität als exponentiell gewichtete gleitende Standardabweichung der Tagesrenditen.
- Die Tagesrendite ist der Schlusskurs geteilt durch den Schlusskurs einen Tag zuvor, minus 1.
- Der voreingestellte Span dieser Schätzung beträgt 100 Tage.
- Die Ausgabe setzt die Vorgabe für die Grenzen von Gewinnmitnahme und Stop-Loss.

## Voraussetzungen


## Anwendung im Trading

- Beim Labeln kann eine variable Schwelle aus der rollierenden exponentiell gewichteten Standardabweichung der Renditen an die Stelle eines festen Tau treten.

## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Die realisierte Bar-Volatilität beträgt im Beispiel 0,0001 in der Nachtsitzung und 0,01 um die Eröffnung.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 58–77 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-004-p058-p077|S. 58–77]]

## Verwandte Themen
