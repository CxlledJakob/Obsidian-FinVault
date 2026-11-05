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
aktualisiert: 2026-11-05
---

# Aggressive Sellers


## Kurzdefinition

- Der Aggressor eines Verkaufs ist die initiierende Seite: Der Verkäufer matcht ein Bid, und die Tick Rule labelt diesen Trade mit −1.

## Kernaussagen

- Jeder Trade hat einen Käufer und einen Verkäufer, doch nur eine Seite initiiert ihn.
- VS ist das Volumen der verkaufsinitiierten Trades, also das Volumen, das gegen das Bid gehandelt wird.
- Im Roll-Modell ist die Aggressorseite bt ein Element von {−1, 1}.
- Mehrere Studien, darunter Aitken und Frino (1996), finden für die Tick Rule eine hohe Klassifikationsgenauigkeit.
- Im Modell von Roll (1984) bedeutet I_t = −1 eine verkäuferinitiierte Transaktion und tritt mit Wahrscheinlichkeit 0,5 ein; I_t = 1 ist die käuferinitiierte Gegenseite, ebenfalls mit Wahrscheinlichkeit 0,5.
- Mit diesem Indikator gilt P_t = P*_t − S/2 bei einer verkäuferinitiierten Transaktion.
- Ändert sich der fundamentale Wert nicht und lag der vorherige Preis auf dem niedrigeren Bid, ist die nächste beobachtete Preisänderung entweder 0 oder +S.
- E(I_t) = 0 und Var(I_t) = 1, und die Folge {I_t} ist unabhängig.
- IBS_{i−v} = −1 markiert eine Transaktion unterhalb des Mittels aus Ask und Bid, also die verkäuferinitiierte Seite der geltenden Quote.
- Im Zerlegungsmodell ist D_i = −1 die Richtung eines Preisrückgangs, sofern A_i = 1 eine Preisänderung anzeigt.
- Die Wahrscheinlichkeit eines Preisanstiegs bei eingetretener Änderung fällt auf 0,085, wenn die vorherige Änderung ebenfalls ein Anstieg war, und steigt auf 0,904, wenn die vorherige Änderung ein Rückgang war.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Die Tick Rule setzt bt auf −1, wenn die Preisänderung negativ ist, und übernimmt bei unverändertem Preis das Zeichen des vorherigen Trades.

## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 248–267 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-014-p248-p267|S. 248–267]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 267–286 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-015-p267-p286|S. 267–286]]

## Verwandte Themen
