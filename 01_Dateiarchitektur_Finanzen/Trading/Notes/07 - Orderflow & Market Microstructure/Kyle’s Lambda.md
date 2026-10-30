---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/07 - Orderflow & Market Microstructure/07 - Orderflow & Market Microstructure|07 - Orderflow & Market Microstructure]]"
weitere_hauptthemen: []
unterthema: "Mikrostruktur"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Kyle’s Lambda


## Kurzdefinition

- Kyle’s Lambda λ ist im strategischen Handelsmodell von Kyle (1985) das inverse Liquiditätsmaß der linearen Preisanpassung und erfasst den Preiseinfluss.

## Kernaussagen

- Der Market Maker beobachtet nur den gesamten Orderflow y = x + u und kann Orders von Noise Tradern und informierten Händlern nicht unterscheiden.
- Er passt den Preis als Funktion des Orderflow-Ungleichgewichts an, weil dieses auf einen informierten Händler hindeuten kann.
- Der positive Zusammenhang zwischen Preisänderung und Orderflow-Ungleichgewicht heißt Market Impact.
- Der informierte Händler unterstellt die lineare Anpassung p = λ y + μ und maximiert den Gewinn (v − p) x bei x = (v − μ) / (2λ).
- Geringere Liquidität bedeutet ein höheres λ und damit eine geringere Nachfrage des informierten Händlers.
- Im Gleichgewicht gilt μ = p0 und λ = (1/2) √(Σ0 / σ²u).
- Die Illiquidität steigt mit der Unsicherheit über v und sinkt mit dem Umfang des Noise.
- Der erwartete Gewinn des informierten Händlers lässt sich als (1 / (4λ)) (v − p0)² schreiben.
- Drei Gewinnquellen sind die Fehlbewertung des Titels, die Varianz des Netto-Orderflows der Noise Trader und der Kehrwert der Varianz des Terminalwerts.
- Je höher der Noise, desto leichter kann der informierte Händler seine Absichten verbergen, und je niedriger die Volatilität, desto leichter lässt sich die Fehlbewertung monetarisieren.
- Als Feature wird λ über die Regression Δpt = λ (bt Vt) + εt geschätzt, wobei bt Vt das signierte Volumen ist.

## Funktionsweise

- Die vom Market Maker unterstellte Nachfrage ist linear in v, x = α + β v, mit α = −μ / (2λ) und β = 1 / (2λ).
- Kyle verlangt ein Gleichgewicht zwischen Gewinnmaximierung des Market Makers und Markteffizienz, und unter den linearen Funktionen ist die Lösung eindeutig.
- Auf Dollar Bars der E-mini-S&P-500-Futures ist bt der volumengewichtete Durchschnitt der Trade-Vorzeichen.
- Vt ist in dieser Berechnung die Summe der Volumina im Bar.
- Δpt ist die Preisänderung zwischen zwei aufeinanderfolgenden Bars.
- Für Dollar Bars der E-mini-S&P-500-Futures werden die Trade-Vorzeichen und Volumina je Bar aggregiert.
- Auf den Dollar Bars ist bt der volumengewichtete Durchschnitt der Trade-Vorzeichen.
- Vt ist dort die Summe der Volumina in dem Bar.

## Voraussetzungen

- Der Terminalwert v ist normalverteilt mit Erwartungswert p0 und Varianz Σ0.
- Ein Noise Trader handelt eine von v unabhängige Menge u, die normalverteilt mit Varianz σ²u ist.
- Ein informierter Händler kennt v und fragt die Menge x über eine Market Order nach.

## Anwendung im Trading

- Kyle’s Lambda gehört zu den Features, mit denen ein Market Maker entscheiden kann, ob er auf einem Niveau Liquidität stellt oder passive Quotes zurückzieht.

## Regeln und Kriterien

- Die Bedingung zweiter Ordnung für das Maximum des informierten Händlers lautet λ > 0.

## Risiken und Grenzen


## Beispiele

- Abbildung 19.1 zeigt das Histogramm von Kyle’s Lambda, geschätzt auf E-mini-S&P-500-Futures.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]
- Advances in Financial Machine Learning.pdf, S. 324–343 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-018-p324-p343|S. 324–343]]

## Verwandte Themen
