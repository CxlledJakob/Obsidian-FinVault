---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/17 - Risikomanagement/17 - Risikomanagement|17 - Risikomanagement]]"
weitere_hauptthemen: []
unterthema: "Portfoliorisiko"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Konzentrationsrisiko


## Kurzdefinition

- Konzentrationsrisiko entsteht, wenn ein Optimierer das Gewicht auf wenige Anlagen bündelt und das Portfolio dadurch idiosynkratischen Schocks aussetzt.
- Die entropieinspirierte Portfoliokonzentration nach Meucci (2009) ist eins minus das Produkt aus dem Kehrwert von N und der Exponentialfunktion der negativen Summe der Produkte aus Risikoanteil und Logarithmus des Risikoanteils.

## Kernaussagen

- Quadratische Optimierer und insbesondere Markowitz' Critical Line Algorithm leiden unter Instabilität, Konzentration und Underperformance.
- Die extreme Konzentration des Critical Line Algorithm wird durch das Ziel getrieben, das Portfoliorisiko zu minimieren.
- Im Zahlenbeispiel liegen 92,66 Prozent des CLA-Gewichts auf den fünf größten Positionen, bei Hierarchical Risk Parity nur 62,57 Prozent.
- CLA setzt drei Anlagen auf Gewicht null und verwirft damit einen großen Teil des Universums zugunsten einer geringen Risikoreduktion.
- Ohne die Schranke, dass Gewichte nicht negativ werden, wären diese drei Allokationen negativ gewesen.
- Die Konditionszahl der Beispiel-Kovarianzmatrix beträgt nur 150,9324 und ist damit für CLA nicht besonders ungünstig.
- Kolanovic und Koautoren (2017) berichten für Hierarchical Risk Parity weniger extreme Gewichte und Risikoallokationen.
- Der Risikoanteil jeder Hauptkomponente liegt zwischen 0 und 1, und die Anteile summieren sich zu eins.
- Der Risikoanteil ist keine Wahrscheinlichkeit, die Verbindung zur Entropie läuft über den verallgemeinerten Mittelwert.
- Die Risikoanteile stammen aus der Zerlegung von Bailey und López de Prado (2012).
- Einer der sechs Züge der bewährten Value-Investoren sind konzentrierte Portfolios.
- Keynes hält Safety-first als kleines Spiel in vielen Firmen, über die man kein gutes Urteil hat, für eine Travestie gegenüber einem substanziellen Einsatz dort, wo die Information ausreicht.
- Keynes: Eine ausgewogene Position ist eine Vielfalt von Risiken, obwohl die einzelnen Positionen groß sind, und wenn möglich mit entgegengesetzten Risiken.
- Graham: Eine Anlage kann in einer Gruppe von Papieren gerechtfertigt sein, die einzeln nicht sicher genug wäre; Diversifikation kann nötig sein, um das Risiko der einzelnen Papiere auf das Minimum zu senken, das die Anforderungen der Anlage noch erfüllen.
- Graham hält Diversifikation für einen integralen Teil aller Standardoperationen der Stammaktienanlage.
- Keynes: Wer kurzfristige Marktschwankungen ignorieren will, braucht größere Sicherheitsmittel und darf nicht in so großem Maßstab mit geliehenem Geld arbeiten.
- Value, Size und Momentum können zu unangenehm großen Sektorwetten führen.
- Absolute statt sektorrelative Maße verringern die Sektordiversifikation und können ziemlich große Sektorwetten erzeugen.
- Nachträglich aufgelegte Sektorbeschränkungen mindern das Exposure auf den Faktor und möglicherweise die künftigen Renditen.
- Branchenrelative Faktoren mindern das Problem der großen Sektorwetten.
- Portfolios auf absoluten Bewertungsniveaus führen zu großen Sektorwetten und können lange Underperformance erzeugen, sichtbar an den Verlusten der Value-Manager in der TMT-Blase.
- Beim absoluten globalen Kurs-Buchwert beträgt die Gewichtsdifferenz des Materialsektors zwischen Long und Short fast 7 Prozentpunkte, 12 Prozent gegen 5 Prozent; sektorrelativ fällt sie auf fast null.
- Das sektorrelative Maß senkt die Sektorschiefe, beseitigt sie aber nicht: ein Sektor, dessen Kennzahlen eng beieinander liegen, kann in beiden Portfolios fehlen.
- Nach dem Platzen der Blase stammte viel von der Value-Outperformance daraus, in billigen, also nicht TMT-, Sektoren zu liegen.
- Die Indexwahl ist eine strategische Entscheidung, weil die Rendite eng am Benchmark hängt. Der GSCI besteht zu 76 Prozent aus Energie, der DJ-AIG zu 33 Prozent, der CRB zu 18 Prozent.
- Der GSCI ist damit weitgehend eine Wette auf Energie und hat 1991–2005 mit 6,3 Prozent eine höhere Volatilität als DJ-AIG mit 4,4 und CRB mit 2,9 Prozent.
- Weitere Gewichte GSCI, DJ-AIG und CRB in Prozent: Industriemetalle 7, 18 und 12; Edelmetalle 2, 8 und 16; Landwirtschaft 10, 18 und 18; Vieh 5, 11 und 12; Softs 0, 12 und 24.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Ein Schock auf eine einzelne Anlage bestraft die Konzentration von CLA.
- Stress bei den fünf größten CLA-Positionen trifft das Portfolio stärker als dasselbe Ereignis bei Hierarchical Risk Parity.
- CLA-Allokationen reagieren erratisch auf idiosynkratische und gemeinsame Schocks.
- Werden Rebalancing-Kosten berücksichtigt, wäre die CLA-Performance sehr negativ gewesen.

## Beispiele

- Die Standardabweichungen im Zahlenbeispiel sind ähnlich, 0,4486 für CLA und 0,4640 für Hierarchical Risk Parity, obwohl CLA die Hälfte des Anlageuniversums verwirft.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 248–267 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-014-p248-p267|S. 248–267]]
- Advances in Financial Machine Learning.pdf, S. 286–305 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-016-p286-p305|S. 286–305]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 305–324 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-017-p305-p324|S. 305–324]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 400–419 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-022-p400-p419|S. 400–419]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 419–438 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-023-p419-p438|S. 419–438]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 609–628 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-033-p609-p628|S. 609–628]]

## Verwandte Themen
