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

# Aggressive Buyers


## Kurzdefinition

- Der Aggressor eines Kaufs ist die initiierende Seite: Der Käufer matcht ein Offer, und die Tick Rule labelt diesen Trade mit 1.

## Kernaussagen

- Jeder Trade hat einen Käufer und einen Verkäufer, doch nur eine Seite initiiert ihn.
- Das Volumen der kaufinitiierten Trades, also das gegen das Ask gehandelte Volumen, heißt VB.
- Mehrere Studien, darunter Aitken und Frino (1996), finden für die Tick Rule trotz ihrer Einfachheit eine hohe Klassifikationsgenauigkeit.
- Als konkurrierende Klassifikationsverfahren nennt der Text Lee und Ready (1991) sowie Easley et al. (2016).
- Im Modell von Roll (1984) ist I_t ein Indikator des Auftragstyps: I_t = 1 mit Wahrscheinlichkeit 0,5 bei einer käuferinitiierten Transaktion und I_t = −1 mit Wahrscheinlichkeit 0,5 bei einer verkäuferinitiierten Transaktion.
- Der beobachtete Marktpreis erfüllt P_t = P*_t + I_t S/2, wobei S = P_a − P_b der Bid-Ask-Spread und P*_t der fundamentale Wert in einem friktionslosen Markt ist.
- Ändert sich P*_t nicht, ist die beobachtete Preisänderung ΔP_t = (I_t − I_{t−1}) S/2.
- Liegt der vorherige beobachtete Preis auf dem höheren Ask, ist die nächste beobachtete Preisänderung entweder 0 oder −S.
- Der Indikator IBS_{i−v} ist 1, wenn der Transaktionspreis über dem Mittel aus Ask und Bid liegt, 0, wenn er genau auf diesem Mittel liegt, und −1, wenn er darunter liegt.
- Ein Preis über (P^a + P^b)/2 wird damit als käuferinitiierte Seite der Quote klassifiziert und geht mit drei Lags in den bedingten Mittelwert des Ordered-Probit-Modells ein.
- Im Zerlegungsmodell ist D_i = 1 die Richtung eines Preisanstiegs, gegeben dass überhaupt eine Preisänderung eintritt.

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
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 248–267 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-014-p248-p267|S. 248–267]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 267–286 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-015-p267-p286|S. 267–286]]

## Verwandte Themen
