---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/13 - Volatilität/13 - Volatilität|13 - Volatilität]]"
weitere_hauptthemen: []
unterthema: "Volatilitätsmessung"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Yang-Zhang-Volatilität


## Kurzdefinition

- Yang und Zhang (2000) empfehlen bei über n Tage konstanter Volatilität den robusten Schätzer σ̂²_yz = σ̂²_o + k σ̂²_c + (1−k) σ̂²_rs.

## Kernaussagen


## Funktionsweise

- Die normierten Größen sind o_t = ln(O_t) − ln(C_{t−1}), u_t = ln(H_t) − ln(O_t), d_t = ln(L_t) − ln(O_t) und c_t = ln(C_t) − ln(O_t).
- σ̂²_o ist die Stichprobenvarianz der normierten Eröffnungen mit Nenner n−1, σ̂²_c die der normierten Schlüsse mit Nenner n−1. σ̂²_rs = (1/n) Σ [u_t(u_t − c_t) + d_t(d_t − c_t)] ist der Schätzer von Rogers und Satchell (1991).
- Das Gewicht k = 0,34 / [1,34 + (n+1)/(n−1)] minimiert die Varianz des Schätzers. σ̂²_yz ist eine Linearkombination dieser drei Schätzungen.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- H_t − L_t heißt die Preisspanne des t-ten Tages und hat zu spannbasierten Volatilitätsschätzern geführt (Alizadeh, Brandt und Diebold, 2002). Weil Kurse nur diskret beobachtet werden, unterschätzt die beobachtete Tagesspanne die wahre Spanne und kann die Volatilität unterschätzen. Die Verzerrung hängt von Handelsfrequenz und Tickgröße ab und ist bei intensiv gehandelten Aktien vernachlässigbar.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 191–210 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-011-p191-p210|S. 191–210]]

## Verwandte Themen
