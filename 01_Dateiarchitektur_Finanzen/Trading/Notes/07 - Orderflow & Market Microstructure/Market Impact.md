---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/07 - Orderflow & Market Microstructure/07 - Orderflow & Market Microstructure|07 - Orderflow & Market Microstructure]]"
weitere_hauptthemen: []
unterthema: "Mikrostruktur"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Market Impact


## Kurzdefinition

- Market Impact ist der positive Zusammenhang zwischen Preisänderung und Orderflow-Ungleichgewicht.

## Kernaussagen

- Eine einzelne Order über einen ganzen großen Block am Hoch drückt den Preis und schmälert den Verkaufsgewinn.
- Kauf in großem Volumen hebt den Preis gegen den Käufer. Verkauf in großem Volumen drückt ihn gegen den Verkäufer.
- In einem illiquiden Titel oder einer illiquiden Währung tritt diese Gegenbewegung sehr schnell ein.
- Die zweite Modellgeneration untersucht, welchen Einfluss Volumen auf Preise hat; Beispiele sind Kyle (1985) und Amihud (2002).
- Diese Modelle achten auf signiertes Volumen und auf das Orderflow-Ungleichgewicht.
- In Kyles Modell erfasst λ den Preiseinfluss und wird über Δpt = λ (bt Vt) + εt auf dem signierten Volumen geschätzt.
- Amihud (2002) misst die tägliche Preisreaktion, die mit einem Dollar Handelsvolumen einhergeht, und nutzt sie als Proxy des Preiseinflusses.
- Eine genannte Umsetzung setzt den Betrag der logarithmischen Bar-Rendite gleich λ mal der Summe des Dollarvolumens der Trades in diesem Bar, plus einem Fehlerterm.
- Hasbrouck (2009) schätzt den Preiseinflusskoeffizienten auf Trade-and-Quote-Daten mit einem Gibbs-Sampler bayesianisch.
- Die Regression erklärt die Log-Preisänderung durch die Summe der vorzeichenbehafteten Quadratwurzeln des Dollarvolumens.
- Das so geschätzte λi nähert die effektiven Handelskosten an.
- Tägliche Amihud-Lambdas weisen eine hohe Rangkorrelation zu Intraday-Schätzungen des effektiven Spreads auf.
- Der Autor hält die t-Werte dieser mikrostrukturellen Schätzungen für informativer als die Mittelwerte, weil sie mit der Standardabweichung des Schätzfehlers skalieren.

## Funktionsweise

- Deshalb erledigen die Insider Kauf und Verkauf nicht in einer Session, sondern über zwei, drei oder vier Sessions.
- Dieselbe Gegenbewegung zwingt auch Distribution, Selling Climax und Buying Climax, sich über einen Zeitraum zu erstrecken.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Nick Leeson konnte die Positionen, die Barings zu Fall brachten, nicht auflösen, ohne den Markt gegen den eigenen Kauf und Verkauf zu bewegen.
- Die Histogramme von Kyles, Amihuds und Hasbroucks Lambdas sind auf E-mini-S&P-500-Futures geschätzt.

## Unterschiedliche Quellenpositionen

- Hasbrouck empfiehlt wie der Großteil der Literatur 5-Minuten-Time-Bars für die Tick-Stichprobe.
- Stochastische Stichproben, die mit der Marktaktivität synchronisiert sind, können nach dem Text bessere Ergebnisse liefern als die empfohlenen 5-Minuten-Time-Bars.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- A Complete Guide to Volume Price Analysis.pdf, S. 58–77 → [[Trading/Pilot/blocks/a-complete-guide-to-volume-price-analysis-pdf/a-complete-guide-to-volume-price-analysis-pdf-block-004-p058-p077|S. 58–77]]
- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]

## Verwandte Themen
