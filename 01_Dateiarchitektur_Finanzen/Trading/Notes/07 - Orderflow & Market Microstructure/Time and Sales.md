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

# Time and Sales


## Kurzdefinition

- Das Ticker Tape war das laufende Band aus Preis und Orderfluss; die elektronische Fassung liefert dieselben Angaben live.

## Kernaussagen

- Es entstand Mitte der 1860er aus einem Morse-Telegrafen und übertrug Aktienpreise und Orderfluss auf einen schmalen Papierstreifen.
- Die Angaben wurden an der Börse von Hand erfasst und an die Ticker in den Brokerbüros verteilt.
- Oben stand das Kürzel, darunter Preise und Volumen in einem Kurzcode.
- S trennte Stückzahl und Preis, SS meinte eine ungerade Stückzahl, meist unter 100, und Nullen fielen der Geschwindigkeit wegen oft weg.
- Wyckoff nannte das Tape eine Methode, aus dem, was jetzt auf dem Band steht, das Wahrscheinliche in der Zukunft abzuleiten.
- Tape Reading zieht aus jedem folgenden Geschäft Schlüsse und misst das momentane Angebot und die momentane Nachfrage.
- Heute kommen Preis und Volumen Sekunde für Sekunde und Tick für Tick, auch mit Level-1- und Level-2-Daten.
- Früher konnten die Daten Minuten bis Stunden hinterherhinken.
- Das Tickerband zeigt mikroskopisch, wie große Blöcke am Hoch verteilt und am Tief für das Inventar des Specialists aufgenommen werden.
- Längerfristige Trends lassen sich nicht allein am vorüberlaufenden Band ablesen. Man braucht das Gedächtnis der Charts.
- Kurze und lange Charts geben zusammen die mikroskopische und die teleskopische Sicht. Für eine vernünftige Entscheidung braucht man beide.
- Zu jeder Transaktion zum Kalenderzeitpunkt t_i, gemessen in Sekunden seit Mitternacht, gehören unter anderem Transaktionspreis, Transaktionsvolumen und die geltenden Bid- und Ask-Quotierungen; diese Sammlung heißt Transaktionsdaten.
- Die TAQ-Datenbank der NYSE enthält alle auf dem Consolidated Tape gemeldeten Aktientransaktionen von 1992 an, einschließlich NYSE, AMEX, NASDAQ und der Regionalbörsen.
- Die Berkeley Options Data Base liefert vergleichbare Optionsdaten von August 1976 bis Dezember 1996.
- Die IBM-Transaktionen vom 1. November 1990 bis 31. Januar 1991 stammen aus dem TORQ-Datensatz von Hasbrouck (1992): 63 Handelstage und 60.328 Transaktionen.
- Transaktionsdaten sind ungleichabständig, die Preise sind diskret, die Aktivität hat ein tägliches Muster, und innerhalb einer Sekunde können mehrere Transaktionen sogar zu verschiedenen Preisen liegen.
- Vor dem 29. Januar 2001 änderte sich der Preis von Trade zu Trade nur in Vielfachen der Tick-Größe; an der NYSE war das vor dem 24. Juni 1997 ein Achtel Dollar und danach bis zu diesem Datum ein Sechzehntel Dollar.
- Die Zeit in Sekunden kann in Phasen starken Handels ein zu grobes Raster sein; bei IBM traten in den normalen Stunden 6.531 Intervalle der Dauer null auf, etwa 10,91 Prozent.
- t_i ist die Kalenderzeit der i-ten Transaktion in Sekunden seit Mitternacht, y_i = P_{t_i} − P_{t_{i−1}} die Preisänderung und Δt_i = t_i − t_{i−1} die Dauer; der Index i zählt die Transaktionsfolge und nicht die Kalenderzeit.
- Die Buchführung hochfrequenter Daten ist oft schlechter als bei niedrigeren Frequenzen, sodass Datenbereinigung nötig wird; Beobachtungen können fehlen, und der genaue Transaktionszeitpunkt mancher Trades ist zweifelhaft.
- Erfasste Handelszeiten können nach 16:00 Uhr Eastern Time liegen, noch bevor der After-Hours-Handel eröffnet; der Umgang mit solchen Beobachtungen braucht eine eigene Untersuchung.
- Eine sachgerechte Bereinigung setzt voraus, dass die Funktionsweise des Marktes genau verstanden ist; die verwendeten Methoden müssen klar angegeben und bei der Inferenz berücksichtigt werden.
- Die IBM-Daten für Dezember 1999 stammen aus TAQ; neben den regulären Stunden zeigt ein Boxplot den Anteil der Trades mit Zeitstempel nach 16:00 Uhr, und am 31. Dezember endete der Handel um 13:00 Uhr.
- Bei Boeing am 1. Dezember 2008 liegen 4,59 Prozent der Transaktionen auf Preisänderungen, die keine Vielfachen von einem Cent sind; die übrigen Änderungen konzentrieren sich auf ganze Cent.
- Viele Intraday-Geschäfte einer Aktie ändern den Preis nicht; sie sind für die Handelsintensität relevant, enthalten aber keine direkte Information über die Preisbewegung.
- Die Daten eines Preisänderungsschritts bestehen aus der Kalenderzeit ti in Sekunden ab Mitternacht, der Dauer Δti = ti − ti−1, der Zahl Ni der Geschäfte ohne Preisänderung im Intervall (ti−1, ti), der Richtung Di = 1 oder Di = −1 und der Größe Si in Ticks.
- Der Preis entwickelt sich als Pti = Pti−1 + Di Si.
- Bei IBM vom 1. November 1990 bis 31. Januar 1991 gab es 60.265 Intraday-Geschäfte, von denen nur 19.022 eine Preisänderung bewirkten.
- Am 21. November 1990 gab es in den normalen Handelszeiten 726 Geschäfte, aber nur 195 mit Preisänderung; die Preisreihe aller Geschäfte und die der preisändernden Geschäfte stimmen überein.
- Die Beschränkung auf Geschäfte mit Preisänderung verkleinert die Stichprobe stark; das PCD-Modell dieses Tages verwendet 194 Preisänderungen innerhalb der normalen Handelszeiten.
- Nur wenige Preisänderungen überschreiten einen Tick: sieben Änderungen mit zwei Ticks und eine mit drei Ticks; die Richtungen sind etwa gleich auf Auf- und Abwärtsbewegungen verteilt.
- Tests der Mikrostrukturtheorie mit Transaktionsdaten verlangen eine sorgfältige Spezifikation der Variablen und ein genaues Verständnis davon, wie der Markt arbeitet und wie die Daten erhoben werden.

## Funktionsweise

- Das Tickerband von 1974 wird auf der kurzen elektronischen Zeitskala durch das Chart ersetzt. Konzept und Prinzip bleiben dieselben.
- Die schnelle Zeitebene ist der mikroskopische Blick, die längere der breitere Blick auf das Verhältnis von Volumen und Preis.
- Die gemeinsame bedingte Dichte von (Δti, Ni, Di, Si) zerlegt sich in f(Si | Di, Ni, Δti, Fi−1) mal f(Di | Ni, Δti, Fi−1) mal f(Ni | Δti, Fi−1) mal f(Δti | Fi−1).

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Am 29. Oktober 1929 zeigte das Band unter anderem Goodyear (GT), US Steel (X), Radio Corporation (R) und Westinghouse (WX); PR kennzeichnete Vorzugsaktien.
- Bei US Steel standen zuerst 10.000 Stück zu 185 3/4, am Bandende 200 Stück als 2.5 1/2, ohne sichere Aussage, ob der Preis noch 185 oder schon 175 oder 165 war.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- A Complete Guide to Volume Price Analysis.pdf, S. 1–20 → [[Trading/Pilot/blocks/a-complete-guide-to-volume-price-analysis-pdf/a-complete-guide-to-volume-price-analysis-pdf-block-001-p001-p020|S. 1–20]]
- A Complete Guide to Volume Price Analysis.pdf, S. 58–77 → [[Trading/Pilot/blocks/a-complete-guide-to-volume-price-analysis-pdf/a-complete-guide-to-volume-price-analysis-pdf-block-004-p058-p077|S. 58–77]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 248–267 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-014-p248-p267|S. 248–267]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 267–286 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-015-p267-p286|S. 267–286]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 286–305 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-016-p286-p305|S. 286–305]]

## Verwandte Themen
