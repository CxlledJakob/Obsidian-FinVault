---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/06 - Volumenanalyse/06 - Volumenanalyse|06 - Volumenanalyse]]"
weitere_hauptthemen: []
unterthema: "Volumenindikatoren"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Accumulation Distribution Line


## Kurzdefinition

- Die Accumulation-Distribution-Volumenfunktion wird Marc Chaiken zugeschrieben; ähnliche Funktionen sind die Intra-day Intensity von David Bostian und die Variable Accumulation Distribution von Larry Williams.
- Sie soll die als Schwäche des On-Balance Volume gesehene Alles-oder-nichts-Zuordnung mildern, die das gesamte Tagesvolumen schon bei winziger Kursänderung positiv oder negativ zählt.

## Kernaussagen


## Funktionsweise

- Chaiken kennzeichnet den Tag über die Lage des Schlusses in der Hoch-Tief-Spanne: die Differenz zwischen Schluss und Mitte der Tagesspanne, geteilt durch die Spannengröße.
- Der Range Factor ist Rft gleich ((Pct minus Plt) minus (Pht minus Pct)) geteilt durch (Pht minus Plt), mit Schluss, Tief und Hoch.
- Das Tagesvolumen der Funktion ist ADVt gleich Vt mal Rft, und die kumulative Reihe ist der Stand vom Vortag plus Vt mal Rft.
- Nur ein Schluss am Tageshoch oder am Tagestief weist das gesamte Volumen positiv als Akkumulation oder negativ als Distribution zu; typischerweise wird nur ein Bruchteil des Volumens zugeordnet.
- Ein Schluss über der Mitte der Tagesspanne gilt als von bullischer Akkumulation beherrscht und soll höhere Preise vorhersagen; ein Schluss darunter gilt als bärische Distribution und soll tiefere Preise vorhersagen.
- Ein als kumulative Summe definierter Preis-Volumen-Indikator zeigt langfristige Trends wie Vermögenspreise und Zinsen und ist nichtstationär; ein gleitender Durchschnitt derselben Funktion ist stationär, trendfrei und bleibt wegen positiver wie negativer Tageswerte nahe bei null.
- Bei Williams vergleicht der Zähler des Range-Faktors den Eröffnungspreis mit dem Schluss.
- Chaiken vergleicht den Schlusskurs mit dem Mittelpreis der Tagesspanne.

## Voraussetzungen


## Anwendung im Trading

- Die Fallstudie rechnete die Funktion mit den Dow-Jones-Industrials statt mit dem S&P 500, weil für den S&P 500 keine täglichen Hochs und Tiefs vorlagen, und nahm an, die Schlusslage des Dow in seiner Spanne ähnele der des S&P 500.
- Gleitende Durchschnitte der täglichen Accumulation-Distribution-Werte wurden für 10 und 30 Tage gebaut: ADV10 gleich MA(ADV, 10) und ADV30 gleich MA(ADV, 30).
- Tabelle 8.2 führt Cumulative Accum. Distr. Volume als CADV sowie ADV10 und ADV30 als Eingabereihen 12 bis 14.

## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 400–419 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-022-p400-p419|S. 400–419]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]

## Verwandte Themen

- Der Accumulation-Distribution-Indikator wird von der Body of Knowledge der Market Technicians Association und von Colby, The Encyclopedia of Technical Market Indicators, 2. Auflage (2003), Marc Chaiken zugeschrieben. Eine bestimmte Veröffentlichung wird nicht genannt.
- Chaikens Indikator ähnelt einem Indikator von Larry Williams aus The Secret of Selecting Stocks for Immediate and Substantial Gains (1971), 1986 bei Windsor Books neu aufgelegt.
