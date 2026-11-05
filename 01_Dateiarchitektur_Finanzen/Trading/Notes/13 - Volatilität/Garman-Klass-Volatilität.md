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

# Garman-Klass-Volatilität


## Kurzdefinition

- Garman und Klass (1980) schätzen die Tagesvarianz σ²_t = E[(C_t − C_{t−1})² | F_{t−1}] aus Eröffnung, Hoch, Tief und Schluss unter einem einfachen Diffusionsmodell ohne Drift.

## Kernaussagen


## Funktionsweise

- Die betrachteten Schätzer sind σ̂²_{0,t} = (C_t − C_{t−1})², σ̂²_{1,t} = (O_t − C_{t−1})²/(2f) + (C_t − O_t)²/(2(1−f)) für 0 < f < 1, und σ̂²_{2,t} = (H_t − L_t)²/(4 ln 2) ≈ 0,3607 (H_t − L_t)². Dabei ist f der Tagesanteil in [0,1], an dem nicht gehandelt wird.
- Weiter gelten σ̂²_{3,t} = 0,17 (O_t − C_{t−1})²/f + 0,83 (H_t − L_t)²/((1−f) 4 ln 2) für 0 < f < 1, σ̂²_{5,t} = 0,5 (H_t − L_t)² − [2 ln 2 − 1](C_t − O_t)² ≈ 0,5 (H_t − L_t)² − 0,386 (C_t − O_t)², und σ̂²_{6,t} = 0,12 (O_t − C_{t−1})²/f + 0,88 σ̂²_{5,t}/(1−f). Ein genauerer Schätzer σ̂²_{4,t} liegt nahe bei σ̂²_{5,t}.
- Der Effizienzfaktor ist Var(σ̂²_{0,t}) / Var(σ̂²_{i,t}). Unter dem einfachen Diffusionsmodell beträgt er näherungsweise 2, 5,2, 6,2, 7,4 und 8,4 für i = 1, 2, 3, 5 und 6. Der Schätzer σ̂²_{2,t} ist der von Parkinson (1980) mit f = 0.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Weil Kurse nur diskret beobachtet werden, liegt das beobachtete Tageshoch tendenziell unter dem wahren Hoch und das Tagestief über dem wahren Tief. Die beobachtete Spanne unterschätzt die wahre Spanne und kann die Volatilität unterschätzen. Die Verzerrung hängt von Handelsfrequenz und Tickgröße ab und sollte bei intensiv gehandelten Aktien vernachlässigbar sein.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 191–210 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-011-p191-p210|S. 191–210]]

## Verwandte Themen
