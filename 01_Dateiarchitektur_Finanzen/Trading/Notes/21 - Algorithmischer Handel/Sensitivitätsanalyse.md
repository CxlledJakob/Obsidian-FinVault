---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Validierung"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Sensitivitätsanalyse


## Kurzdefinition


## Kernaussagen

- Fünf Faktoren bestimmen, wie zufällig ein Data-Mining-Vorhaben ist und damit die Größe des Data-Mining-Bias.
- Der erste Faktor ist die Zahl der auf dem Weg zur besten Regel gebacktesteten Regeln: Je mehr Regeln geprüft werden, desto größer ist der Bias.
- Der zweite ist die Zahl der Beobachtungen, aus denen die Leistungskennzahl berechnet wird: Je mehr Beobachtungen, desto kleiner der Bias.
- Der dritte ist die Korrelation der Renditehistorien der geprüften Regeln: Je weniger sie korrelieren, desto größer der Bias.
- Der vierte ist das Vorliegen sehr großer positiver Renditen in der Leistungshistorie einer Regel, zum Beispiel einer sehr großen positiven Tagesrendite: Sind sie vorhanden, tendiert der Bias dazu, größer zu sein.
- Dieser Ausreißer-Effekt wird kleiner, wenn die positiven Ausreißer im Verhältnis zur Zahl der Beobachtungen der Kennzahl wenige sind; mehr Beobachtungen verdünnen ihn.
- Der fünfte ist die Variation der wahren erwarteten Rendite unter den gebacktesteten Regeln: Je geringer diese Variation, desto größer der Bias.
- Haben die geprüften Regeln ähnliche Grade an Vorhersagekraft, ist der Data-Mining-Bias größer.
- Werden die fünf Faktoren berücksichtigt, lassen sich statistische Signifikanz oder ein Konfidenzintervall für eine durch Data Mining entdeckte Regel berechnen.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 267–286 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-015-p267-p286|S. 267–286]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 286–305 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-016-p286-p305|S. 286–305]]

## Verwandte Themen
