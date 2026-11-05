---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/14 - Marktzyklen/14 - Marktzyklen|14 - Marktzyklen]]"
weitere_hauptthemen: []
unterthema: "Zeitzyklen"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Intraday-Zyklus


## Kurzdefinition

- Unter normalen Handelsbedingungen zeigt die Transaktionsaktivität ein tägliches periodisches Muster; an der NYSE ist sie zu Beginn und am Schluss der Handelszeit schwerer und in der Mittagszeit dünner, also U-förmig, und die Dauern zwischen den Transaktionen folgen demselben Tageszyklus.

## Kernaussagen

- Hochfrequente Daten sind Beobachtungen in feinen Zeitabständen, in der Finanzanwendung oft täglich oder feiner; die höchste Frequenz sind die Transaktionen selbst, mit der Zeit in Sekunden.
- Transaktionen liegen nicht in gleichen Zeitabständen, sodass die beobachteten Transaktionspreise keine gleichabständige Zeitreihe bilden; die Dauer zwischen Trades kann Information über die Handelsintensität enthalten.
- Für IBM vom 1. November 1990 bis 31. Januar 1991 umfasst der TORQ-Datensatz 63 Handelstage und 60.328 Transaktionen; betrachtet werden nur die normalen Stunden von 9:30 bis 16:00 Uhr Eastern Time, Preisänderungen zwischen Handelstagen bleiben außen vor.
- Die Zahl der Transaktionen in 5-Minuten-Intervallen hat eine Autokorrelation mit Periode 78, und 78 ist die Zahl der 5-Minuten-Intervalle eines Handelstags.
- Der über 63 Tage gemittelte Verlauf dieser 78 Intervalle zeigt eine U-Form: mehr Handel zur Eröffnung und zum Schluss, dünnerer Handel über die Mittagsstunden.
- In den normalen Stunden gibt es 59.838 Zeitintervalle zwischen Trades; 6.531 davon haben die Dauer null, also mehrere Transaktionen in derselben Sekunde, das sind etwa 10,91 Prozent.
- Unter diesen Mehrfachtransaktionen hatten 1.002 unterschiedliche Preise, etwa 1,67 Prozent aller Intraday-Transaktionen; Dauern von null können die statistische Modellierung der Zeit zwischen Trades damit stören.
- Über Nacht unterscheiden sich Aktienrenditen erheblich von Intraday-Renditen.
- Längere Dauern zwischen Trades zeigen fehlende Handelsaktivität und damit eine Phase ohne neue Information; die Dynamik der Dauern enthält deshalb Information über die Intraday-Aktivität.
- Weil die Intraday-Transaktionen ein Tagesmuster haben, wird die bereinigte Dauer Δt*_i = Δt_i / f(t_i) modelliert, wobei f(t_i) die deterministische zyklische Komponente ist.
- Für die IBM-Daten wird f(t_i) = exp[d(t_i)] mit quadratischen Funktionen und Indikatoren angesetzt; kein einzelnes Schätzverfahren für f dominiert die anderen in den statistischen Eigenschaften.
- f5 ist der Indikator der ersten fünf Minuten nach 9:30 Uhr Eastern Time, f6 der Indikator der zweiten fünf Minuten, und f7 der Indikator der letzten 30 Minuten von 15:30 bis 16:00 Uhr.
- Die per Kleinste-Quadrate angepasste Gleichung lautet ln(Δt_i) = 2,555 + 0,159 f1(t_i) + 0,270 f2(t_i) + 0,384 f3(t_i) + 0,061 f4(t_i) − 0,611 f5(t_i) − 0,157 f6(t_i) + 0,073 f7(t_i).
- f3(43200) = f4(43200), und 43.200 Sekunden seit Mitternacht entsprechen 12:00 Uhr mittags.
- Nach dieser Bereinigung ist das Tagesmuster der über 5-Minuten-Intervalle gemittelten Dauern weitgehend entfernt.
- Die Hazard-Funktion eines EACD ist über die Zeit konstant, die eines WACD monoton; beides ist einschränkend, weil die Intensität von Aktientransaktionen weder konstant noch monoton sein muss.
- Ein GACD mit verallgemeinerter Gamma-Verteilung lässt auch U-förmige und umgekehrt U-förmige Hazard-Funktionen zu.
- Am 31. Dezember 1999 schloss der Markt bereits um 13:00 Uhr statt um 16:00 Uhr; sonst gelten 9:30 bis 16:00 Uhr Eastern Time.
- Die IBM-Transaktionsdauern der ersten fünf Handelstage im November 1990 werden vor der WACD-Schätzung um die deterministische Komponente bereinigt; verwendet werden 3534 positive adjustierte Dauern.
- Auch nach Bereinigung des Tagesmusters unterscheiden sich die Handelsdynamiken, gemessen an den Intraday-Transaktionsdauern, zwischen Phasen starken und schwachen Handels.
- In den Zeitdauern zwischen Preisänderungen gibt es kein Tagesmuster.
- Marktaktivitäten werden oft durch das Eintreffen von Nachrichten und anderer Information getrieben.

## Funktionsweise

- Ein Tagesmuster der Handelsdauer lässt sich über einen lokalen Durchschnitt bereinigen: ein Handelstag wird in 39 Zehn-Minuten-Intervalle geteilt, di ist der Durchschnitt aller Log-Dauern des i-ten Intervalls über alle Handelstage, und die adjustierte Dauer ist tj/exp(di) für j in diesem Intervall.
- Zur Bereinigung des Tagesmusters der Handelsdauer gibt es ausgefeiltere Verfahren; die einfache Anpassung verwendet nur diesen lokalen Durchschnitt.
- Das Tagesmuster des Handels lässt sich an der Zahl der Geschäfte je Fünf-Minuten-Intervall und an der Stichproben-Autokorrelationsfunktion dieser Reihe prüfen.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Die Intraday-Preisänderungen von IBM in dieser Stichprobe, gemessen in Ticks von 0,125 Dollar, haben die Häufigkeiten 0,66, 1,33, 14,53, 67,06, 14,53, 1,27 und 0,63 Prozent für ≤ −3 bis ≥ 3 Ticks.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 248–267 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-014-p248-p267|S. 248–267]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 267–286 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-015-p267-p286|S. 267–286]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 286–305 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-016-p286-p305|S. 286–305]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 305–324 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-017-p305-p324|S. 305–324]]

## Verwandte Themen
