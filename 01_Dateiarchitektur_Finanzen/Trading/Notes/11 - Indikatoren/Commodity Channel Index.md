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
aktualisiert: 2026-11-05
---

# Commodity Channel Index


## Kurzdefinition

- Der CCI wurde von Donald Lambert (Commodities Magazine, Oktober 1980) beschrieben, um statistisch zu schätzen, wo die aktuellen Preise innerhalb der Länge eines Kanals liegen.

## Kernaussagen


## Funktionsweise

- Lambert vergleicht den aktuellen Preis relativ zu einem gleitenden Durchschnitt über die Kanallänge mit der Standardabweichung der Preise über dieselbe Länge; vereinfacht ist der CCI das Verhältnis aus momentaner Abweichung und Standardabweichung.
- Lambert teilt das Verhältnis zusätzlich durch 0,015, was einer Multiplikation mit 66,7 entspricht. Dieser Skalierungsfaktor setzt +100 und −100 als Näherungen für plus und minus eine Standardabweichung, falls die Daten gaußverteilt wären.
- Der adaptive CCI nutzt die Variable Filt, also nur die vom Roofing-Filter durchgelassenen Frequenzkomponenten, statt des Durchschnitts aus Hoch, Tief und Schluss wie bei Lambert.
- Der Durchschnittspreis muss in Langform berechnet werden statt mit dem schnellen Algorithmus (1/N des ältesten Preises abziehen und 1/N des aktuellen addieren), weil N durch die Abstimmung auf den dominanten Zyklus von Balken zu Balken variiert.
- Mit dem gleitenden Durchschnitt wird der Root Mean Square (RMS) der Preise berechnet; RMS ist gleichbedeutend mit der Standardabweichung.
- Im Code ist der Zähler Preis minus Durchschnittspreis und der Nenner 0,015 · RMS; das Verhältnis wird mit dem SuperSmoother-Filter geglättet. Referenzlinien liegen bei +100 und −100.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Ehlers verwendet beim adaptiven CCI eine volle Periode des gemessenen dominanten Zyklus als Kanallänge.
- Der CCI ist über die volle Periode des gemessenen dominanten Zyklus optimiert, damit die Standardabweichung vollständig gemessen wird.

## Risiken und Grenzen

- Die Annahme einer Gaußverteilung hinter der Skalierung auf ±100 ist nicht gut; das lässt sich heuristisch belegen, indem man die Wahrscheinlichkeitsverteilungen über viele Daten misst.
- Die Kanallänge variiert in der Literatur stark und wird in allen Fällen eher willkürlich festgelegt, um den Indikator an ein vorgefasstes Ereignis anzupassen.

## Beispiele

- Auf Dollar General (DG) über etwa ein Jahr zeigt der adaptive CCI die Lage der aktuellen Preise im Kanal, dessen Länge der gemessene dominante Zyklus bestimmt; er überschreitet plus oder minus eine Standardabweichung nur gelegentlich (Abbildung 11.3).

## Unterschiedliche Quellenpositionen

- Im Vergleich der adaptiven Indikatoren zeigen RSI, Stochastic und CCI im groben Sinn ziemlich dasselbe an; ohne Indikator-Transformationen (Kapitel 15) gibt es keinen zwingenden Grund, einen dem anderen vorzuziehen.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 140–159 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-012-p140-p159|S. 140–159]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 159–178 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-013-p159-p178|S. 159–178]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 197–216 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-015-p197-p216|S. 197–216]]

## Verwandte Themen
