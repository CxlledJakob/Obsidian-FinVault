---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Modelle"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Logistische Regression


## Kurzdefinition

- Die logistische Regression setzt hier ln[p / (1−p)] = x β, also p = exp(x β) / [1 + exp(x β)], und hält damit eine Wahrscheinlichkeit im Einheitsintervall.

## Kernaussagen


## Funktionsweise

- Für die Wahrscheinlichkeit p_i einer Preisänderung genügt wegen der binären Variablen A_i der Logit auf Elementen der Informationsmenge des vorherigen Trades.
- Gegeben A_i = 1 ist auch die Richtung binär, und δ_i = P(D_i = 1 | A_i = 1) folgt einem eigenen Logit ln[δ_i / (1−δ_i)] = z_i γ.
- Die Parameter λ der geometrischen Verteilung für die Größe der Preisänderung werden ebenfalls logit-transformiert, getrennt für Anstieg und Rückgang, damit λ_{j,i} in [0, 1] liegt.
- Die Zerlegung erzwingt eine natürliche Reihenfolge: D_i ist nur bei A_i = 1 definiert, und die Größe S_i ist nur sinnvoll, wenn A_i = 1 und die Richtung gegeben sind.
- Weil sich Ni bei 0 häuft, wird die bedingte Wahrscheinlichkeit p(Ni = 0 | Δti, Fi−1) als Logit-Modell logit[α0 + α1 ln(Δti)] angesetzt, mit logit(x) = exp(x)/[1 + exp(x)].
- Für Ni > 0 gilt Ni ∼ 1 + g(λi), wobei g(λ) eine geometrische Verteilung mit Parameter λ in (0, 1) ist und λi = exp[γ0 + γ1 ln(Δti)] / (1 + exp[γ0 + γ1 ln(Δti)]).
- McCulloch und Tsay (2000) verwenden verallgemeinerte lineare Modelle für die diskreten Variablen und ein Zeitreihenmodell für die stetige Variable ln(Δti).

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Für IBM vom 1. November 1990 bis 31. Januar 1991, 63 Handelstage und nach Verwendung von Lag-1-Variablen 59.775 Beobachtungen, lautet der Logit der Preisänderung β0 + β1 A_{i−1} mit Schätzwerten −1,057 und 0,962.
- Daraus folgen P(A_i = 1 | A_{i−1} = 0) = 0,258 und P(A_i = 1 | A_{i−1} = 1) = 0,476: Preisänderungen treten gehäuft auf, und die meisten Transaktionen bleiben ohne Preisänderung.
- Der Logit der Richtung ist γ0 + γ1 D_{i−1} mit Schätzwerten −0,067 und −2,307; die Wahrscheinlichkeit eines Anstiegs beträgt 0,483 nach unveränderter Vornotiz, 0,085 nach einem Anstieg und 0,904 nach einem Rückgang.
- Die Logits der Tick-Größe lauten 2,235 − 0,670 S_{i−1} für Anstiege und 2,085 − 0,509 S_{i−1} für Rückgänge.
- In der R-Demonstration der binomischen logistischen Regression sind die Steigungen hoch signifikant, mit z = 52,62 für die vorherige Preisänderung und z = −64,17 für die vorherige Richtung.
- Für IBM am 21. November 1990 gilt Pr(Ni > 0 | Δti, Fi−1) = logit[−0,637 + 1,740 ln(Δti)], Standardabweichungen 0,238 und 0,248; die Zahl der Geschäfte ohne Preisänderung hängt positiv von der Länge des Intervalls ab.
- Ist Ni positiv, gilt λi = exp[0,178 − 0,910 ln(Δti)] / (1 + exp[0,178 − 0,910 ln(Δti)]), Standardabweichungen 0,246 und 0,138; ein großes ln(Δti) ergibt ein kleines λi und damit höhere Wahrscheinlichkeiten für große Ni.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 267–286 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-015-p267-p286|S. 267–286]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 286–305 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-016-p286-p305|S. 286–305]]

## Verwandte Themen
