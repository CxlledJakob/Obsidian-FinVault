---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/07 - Orderflow & Market Microstructure/07 - Orderflow & Market Microstructure|07 - Orderflow & Market Microstructure]]"
weitere_hauptthemen: []
unterthema: "Transaktionsfluss"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Aggressive Buyers


## Kurzdefinition

- Der Aggressor eines Kaufs ist die initiierende Seite: Der Käufer matcht ein Offer, und die Tick Rule labelt diesen Trade mit 1.

## Kernaussagen

- Jeder Trade hat einen Käufer und einen Verkäufer, doch nur eine Seite initiiert ihn.
- Das Volumen der kaufinitiierten Trades, also das gegen das Ask gehandelte Volumen, heißt VB.
- Mehrere Studien, darunter Aitken und Frino (1996), finden für die Tick Rule trotz ihrer Einfachheit eine hohe Klassifikationsgenauigkeit.
- Als konkurrierende Klassifikationsverfahren nennt der Text Lee und Ready (1991) sowie Easley et al. (2016).

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- Aus der Zeichenreihe {bt} lassen sich Features bilden, darunter ein Kalman-Filter auf den erwarteten Folgezustand, Strukturbrüche, die Entropie der Folge, t-Werte aus Wald-Wolfowitz-Runs-Tests und die fraktionale Differenzierung der kumulierten Zeichen.

## Regeln und Kriterien

- Die Tick Rule setzt bt auf 1, wenn die Preisänderung positiv ist, auf −1, wenn sie negativ ist, und auf bt−1, wenn der Preis unverändert bleibt.
- Der Startwert b0 wird willkürlich auf 1 gesetzt.

## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]

## Verwandte Themen
