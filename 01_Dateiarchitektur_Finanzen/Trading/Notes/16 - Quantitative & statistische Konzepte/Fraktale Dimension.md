---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Modelle"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Fraktale Dimension


## Kurzdefinition

- Zur Bestimmung der fraktalen Dimension eines Musters wird es mit einer Zahl N kleiner Objekte verschiedener Größen S überdeckt; für zwei Größen gilt N2/N1 = (S1/S2)^D, also D = log(N2/N1) / log(S1/S2).

## Kernaussagen

- Die fraktale Dimension von Preisreihen liegt zwischen D = 1 und D = 2.
- Der Hurst-Koeffizient hängt mit der fraktalen Dimension über H = 2 − D zusammen.
- Ehlers hält die Schätzung des Hurst-Koeffizienten über die fraktale Dimension für die praktikabelste Methode bei kürzerfristigen Marktdaten.
- Natürliche Fraktale wie eine Küstenlinie haben nicht die echte Regelmäßigkeit einer algorithmischen Struktur, sind aber statistisch selbstähnlich; deshalb muss man die gemessene fraktale Dimension über verschiedene Skalen mitteln.

## Funktionsweise

- Weil Preiswerte gleichmäßig verteilt sind, entspricht die Boxzahl ungefähr der mittleren Steigung der Kurve; sie wird geschätzt als (höchster Preis − tiefster Preis) im Intervall geteilt durch die Intervalllänge.
- N1 ist (Hoch − Tief) über das Intervall von 0 bis T Bars zurück geteilt durch T, N2 ist (Hoch − Tief) über das Intervall von T bis 2T Bars zurück geteilt durch T, und N3 ist (Hoch − Tief) über das ganze Intervall von 0 bis 2T geteilt durch 2T.
- Die fraktale Dimension berechnet sich als D = (Log(N1 + N2) − Log(N3)) / Log(2).
- Im Code muss Length eine gerade Zahl sein (Vorgabe 30); die Dimension wird nur berechnet, wenn N1, N2 und N3 größer als 0 sind, und als Dimen = 0,5 * ((Log(N1 + N2) − Log(N3)) / Log(2) + Dimen[1]) geglättet.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Nach Ehlers hat die fraktale Dimension wie der Hurst-Koeffizient keine direkte praktische Anwendung im Trading, weil sie eine Schätzung ist und keinen prognostischen Wert hat.

## Beispiele

- Eine 10 Meter lange Linie fasst zehn 1-Meter-Boxen (N1 = 10) und hundert 0,1-Meter-Boxen (N2 = 100); daraus folgt D = log(100/10) / log(1/0,1) = 1,0.
- Ein Quadrat mit 10 Metern Seitenlänge fasst bei denselben Boxgrößen N1 = 100 und N2 = 10.000 Boxen; daraus folgt D = log(10000/100) / log(1/0,1) = 2,0.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 71–83 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-007-p071-p083|S. 71–83]]

## Verwandte Themen
