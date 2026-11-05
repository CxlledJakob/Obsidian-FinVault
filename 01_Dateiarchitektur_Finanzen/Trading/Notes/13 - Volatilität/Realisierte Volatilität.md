---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/13 - Volatilität/13 - Volatilität|13 - Volatilität]]"
weitere_hauptthemen: []
unterthema: "Volatilitätsmessung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Realisierte Volatilität


## Kurzdefinition

- Die horizontalen Barrieren sind eine dynamische Funktion der geschätzten Volatilität, gleich ob realisiert oder implizit.
- Die realisierte Volatilität der Tages-Logrendite r_t ist RV_t = Σ_{i=1}^{n} r²_{t,i}, wobei n gleichabständige Intraday-Logrenditen sich zu r_t summieren (Andersen, Bollerslev, Diebold und Labys, 2001a, 2001b).

## Kernaussagen

- Dieselbe feste Schwelle trifft auf sehr unterschiedliche realisierte Bar-Volatilitäten.
- Liegt die Schwelle weit über der herrschenden Volatilität, ist das Ziel zu hoch, liegt sie weit darunter, ist es zu niedrig.
- Die Volatilitäten von Volumen- und Dollar-Bars liegen deutlich näher an einer Konstanten als die von Zeit-Bars.
- Die tägliche Volatilität ist aus Tagesrenditen nicht direkt beobachtbar, weil je Handelstag nur eine Beobachtung vorliegt.
- Mit Intraday-Daten wie Zehn-Minuten-Renditen lässt sich die tägliche Volatilität schätzen; Abschnitt 3.15 behandelt diese Schätzung, ihre Genauigkeit bleibt sorgfältig zu prüfen.
- Die Schätzung aus Hochfrequenzrenditen enthält nur sehr begrenzte Information über die Overnight-Volatilität, also die Schwankung zwischen den Handelstagen.
- Realisierte Volatilität ist die quadratische Variation von r_t und setzt voraus, dass {r_{t,i}} eine iid-Folge mit Mittelwert null und endlicher Varianz ist.
- Begrenzte Erfahrung zeigt, dass ln(RV_t) oft näherungsweise einem gaußschen ARIMA(0,1,q) folgt, das Prognosen liefern kann.
- Vorteile sind Einfachheit und die Nutzung von Intraday-Renditen. Ein großes n verwendet mehr Information, doch bei kleinem Intervall verzerren Mikrostruktureffekte wie der Bid-Ask-Bounce die Schätzung.
- Für stark gehandelte US-Assets wird oft ein Intervall von 4 bis 15 Minuten verwendet.
- Die Overnight-Rendite vom Schluss des Vortags zur Eröffnung ist bei Aktien oft beträchtlich. Sie zu ignorieren kann die Volatilität ernsthaft unterschätzen. Bei Index- und Devisenrenditen erscheinen Overnight-Renditen klein.
- French, Schwert und Stambaugh (1987) berechnen die Volatilität niederfrequenter Renditen aus hochfrequenten Daten. Wird der Tagesmittelwert null gesetzt, schätzt die Summe der quadrierten Tages-Logrenditen die Monatsvolatilität. Dieses Konzept wird auf die Tagesvolatilität aus Intraday-Logrenditen verallgemeinert.
- Unter weißem Rauschen der Tagesrenditen ist σ̂²_m = [n/(n−1)] Σ (r_{t,i} − r̄_t)². Unter einem MA(1) kommt die Summe der Produkte benachbarter zentrierter Tagesrenditen hinzu.
- Für den S&P 500 von Januar 1980 bis Dezember 1999 liegen die aus Tagesrenditen geschätzten Monatsvolatilitäten deutlich über einem GARCH(1,1) auf Monatsrenditen von Januar 1962 bis Dezember 1999. Für Oktober 1987 beträgt die Tagesschätzung etwa 680.
- Haben die Tages-Logrenditen hohe Exzess-Kurtosis und serielle Korrelationen, können diese Stichprobenschätzer inkonsistent sein (Bai, Russell und Tiao, 2004). Ein Monat hat grob 21 Handelstage, die Stichprobe ist klein.
- Manche Forscher verwenden die Summe der Quadrate der Intraday-Fünf-Minuten-Renditen als Maß der Tagesvolatilität; ein normaler Handelstag hat 77 solche Renditen.
- Für die 3M-Geschäfte im Dezember 1999 wird der Preis eines Fünf-Minuten-Intervalls als einfacher Durchschnitt aller Transaktionspreise in dem Intervall gebildet.
- Für die Boeing-Geschäfte vom 1. bis 5. Dezember 2008 ist der Preis eines Fünf-Minuten-Intervalls der letzte Transaktionspreis in dem Intervall; Übernachtrenditen werden ausgelassen.
- Im lokalen Trendmodell ist μt die latente Logvolatilität und yt der Logarithmus der realisierten Volatilität. Die wahre Logvolatilität ist nicht direkt beobachtet und folgt einem Random Walk. yt wird aus Hochfrequenzumsätzen gebaut und trägt Mikrostrukturrauschen.
- Die tägliche realisierte Volatilität von Alcoa, 2. Januar 2003 bis 7. Mai 2004, 340 Beobachtungen, ist die Summe der quadrierten Intraday-Logrenditen über 10 Minuten, in Prozent. Übernachtrenditen und die ersten 10 Minuten werden nicht verwendet. Die Daten stammen aus TAQ der NYSE. Modelliert wird der Logarithmus.
- Ein ARIMA(0,1,1) für diese Logreihe ist (1 minus B) yt gleich (1 minus 0,858 B) at mit geschätzter Residualstreuung 0,5184 und Standardfehler von θ-Dach gleich 0,028.
- Die Residuen haben Q(12) gleich 12,4 bei einem p-Wert von 0,33, die quadrierten Residuen Q(12) gleich 8,2 bei einem p-Wert von 0,77.
- Die Maximum-Likelihood-Schätzungen des lokalen Trendmodells sind ση-Dach gleich 0,0735 und σe-Dach gleich 0,4803. Aus den ARIMA-Relationen folgen σe gleich 0,480 und ση gleich 0,0736. Die Messfehler haben die größere Varianz.
- Der Kalman-Filter der Alcoa-Log-RV startet mit Σ1|0 unendlich und μ1|0 gleich 0. Die gefilterten Zustände sind glatter als die logarithmierte realisierte Volatilität. Die Ein-Schritt-Prognosefehler sind außer Stichprobe, stabil und um null zentriert.
- Die geglätteten Zustände sind noch glatter, und ihre punktweisen 95-Prozent-Intervalle sind schmaler als die der gefilterten Zustände.
- Die Maximum-Likelihood-Schätzungen sind ση gleich 0,07350827 und σe gleich 0,48026284, die Varianzen 0,0054035 und 0,2306524. In S-Plus steht für die diffuse Initialisierung P1 gleich minus 1 und a1 gleich 0.
- Die standardisierten Prognosefehler haben Q(25) gleich 23,37 bei einem p-Wert von 0,56 und eine ARCH-LM-Statistik von 18,48 bei einem p-Wert von 0,82 über 25 Lags. Das lokale Trendmodell der realisierten Volatilität ist danach angemessen.
- Die gezeichneten 95-Prozent-Bänder sind die Zustandsschätzung plus und minus 2 mal der Wurzel der Zustandsvarianz, über die 340 Tage der Alcoa-Reihe.

## Funktionsweise

- getDailyVol schätzt an Intraday-Zeitpunkten die Tagesvolatilität als exponentiell gewichtete gleitende Standardabweichung der Tagesrenditen.
- Die Tagesrendite ist der Schlusskurs geteilt durch den Schlusskurs einen Tag zuvor, minus 1.
- Der voreingestellte Span dieser Schätzung beträgt 100 Tage.
- Die Ausgabe setzt die Vorgabe für die Grenzen von Gewinnmitnahme und Stop-Loss.

## Voraussetzungen


## Anwendung im Trading

- Beim Labeln kann eine variable Schwelle aus der rollierenden exponentiell gewichteten Standardabweichung der Renditen an die Stelle eines festen Tau treten.

## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Die realisierte Bar-Volatilität beträgt im Beispiel 0,0001 in der Nachtsitzung und 0,01 um die Eröffnung.
- Die Datei aa-rv-20m.txt enthält die realisierte Tagesvolatilität der Alcoa-Aktienrenditen vom 2. Januar 2003 bis 7. Mai 2004, konstruiert aus 20-Minuten-Intraday-Logrenditen.
- Aufgabe 11.2 verlangt ein ARIMA(0,1,1) für die Log-Volatilität sowie die Schätzung des lokalen Trendmodells mit Zeitplots der gefilterten und geglätteten Zustände und punktweisen 95-Prozent-Intervallen.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 58–77 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-004-p058-p077|S. 58–77]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 134–153 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-008-p134-p153|S. 134–153]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 305–324 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-017-p305-p324|S. 305–324]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 571–590 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-031-p571-p590|S. 571–590]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 590–609 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-032-p590-p609|S. 590–609]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 628–647 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-034-p628-p647|S. 628–647]]

## Verwandte Themen
