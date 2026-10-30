---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/17 - Risikomanagement/17 - Risikomanagement|17 - Risikomanagement]]"
weitere_hauptthemen: []
unterthema: "Verlustrisiko"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Stop-Loss


## Kurzdefinition

- Der Stop-Loss ist die untere horizontale Barriere und eine dynamische Funktion der geschätzten Volatilität.
- Der Stop-Loss ist die negative Schwelle, bei deren Erreichen die offene Gelegenheit mit Verlust geschlossen wird.
- Der Stop-Loss ist die Bedingung, eine Position mit Verlust zu schließen.

## Kernaussagen

- Nach einem Bruch durch eine Decke kann der Stop-Loss in den unteren Bereich der Preisstauzone gelegt werden.
- Der neue Boden ist der natürliche Schutz bei einem Rücktest. Ein Weg zurück durch diese Zone bräuchte Aufwand und Volumen.
- Abwärts wird die neue Decke zum Schutz gegen einen kurzen Rücksetzer, und der Stop liegt sinngemäß jenseits dieser neuen Barriere.
- Der Stop unter dem Docht eines Hammers wird vom Markt gesetzt.
- Nach der Shooting-Star-Folge liegt der Stop der Short-Position über dem Docht der ersten Shooting-Star-Kerze.
- Die sichtbaren Stauzonen aus Volume at Price helfen beim Platzieren der Stops. Risiko- und Geldmanagement geben die Regeln vor.
- Nach dem Bruch einer langen Stauzone liegt der Stop unter dem letzten Pivot-Tief, weil darunter ein tiefes natürliches Schutzpolster steht.
- Der beste Platz ist die andere Seite der Stauzone, hinter der Barriere, die der Markt selbst gebaut hat.
- Ist im aufsteigenden Dreieck die Decke zur Unterstützung geworden, ist das die natürliche Barriere für den Stop.
- Das Risiko des Trades ist niedriger, wenn mit dem dominanten Trend der langsameren Zeitebene gehandelt wird, und höher, wenn dagegen gehandelt wird.
- Jede Anlagestrategie hat Stop-Loss-Grenzen, ob der Portfolio-Manager sie selbst setzt, die Risikoabteilung sie erzwingt oder ein Margin Call sie auslöst.
- Gewinne aus Positionen zu modellieren, die an der Börse ausgestoppt worden wären, ist unrealistisch.
- Stop-Loss und Gewinnmitnahme sollen vom Risiko der Wette abhängen.
- Wird die untere Barriere zuerst berührt, ist das Label -1.
- Die Breite der unteren Barriere ist der Faktor ptSl[1] mal dem Ziel trgt.
- Ist dieser Faktor 0, gibt es keine untere Barriere.
- Soll die Seite der Wette gelernt werden, sind die horizontalen Barrieren symmetrisch oder sie entfallen, weil Stop und Gewinnziel ohne Seite nicht unterscheidbar sind.
- Ist die Seite bekannt, wie beim Meta-Labeling, lassen sich Gewinnmitnahme und Stop-Loss unterscheiden, und die horizontalen Barrieren müssen nicht symmetrisch sein.
- Die Stop-Schwelle entspricht einer horizontalen Barriere des Meta-Labeling.
- Bei Prognose null und kurzer Halbwertszeit ist der optimale Stop weit und lässt nicht realisierte Verluste bis zum Fünf- oder Siebenfachen des kleinen Gewinnziels zu.
- Bei Prognose null und kurzer Halbwertszeit ist ein kurzer Stop zusammen mit einem hohen Gewinnziel die schlechteste Regel.
- Bei Prognose 5 und Halbwertszeit 5 liegen die guten Stops zwischen 4 und 10.
- Bei Prognose 5 und Halbwertszeit 10 liegen die guten Stops zwischen 7 und 10.
- Bei Prognose 5 und Halbwertszeit 25 liegen die guten Stops zwischen 9 und 10.
- Ist ein Gewinnziel vorgegeben, wird der passende Stop aus den simulierten Pfaden bestimmt.
- Ist ein maximaler Stop vorgegeben, wird dazu das passende Gewinnziel bestimmt.
- Bei Prognose minus 5 und Halbwertszeit 5 liegt die schlechteste Region um einen Stop von 6, mit Gewinnzielen zwischen 4 und 10.
- Bei Prognose minus 5 und Halbwertszeit 5 markiert das Rechteck die schlechteste Performance.
- Die schlechteste Region bei negativer Prognose ist das gedrehte Gegenbild der besten Region bei positiver Prognose.
- Mit steigender Halbwertszeit spreizt sich das schlechteste Gebiet, und die negativen Sharpe Ratios werden flacher.
- Eine schon bestehende Position mit erwartetem Verlust braucht einen Stop, der diesen Verlust begrenzt.
- Ein rationaler Teilnehmer eröffnet keine neue Position, wenn der erwartete Ausgang ein Verlust ist.
- Auch ohne gesetzten Stop besteht eine implizite Grenze durch einen Margin Call oder durch einen nicht mehr tragbaren Buchverlust.
- Im asymmetrischen Modell liegt die Verlustauszahlung unter der Gewinnauszahlung.
- Wird die Verlustauszahlung bei gleichem Gewinnziel negativer, steigt die Trefferwahrscheinlichkeit, die für eine Ziel-Sharpe-Ratio nötig ist.
- Wird die Verlustauszahlung negativer, steigt auch die Wettfrequenz, die bei gleicher Trefferwahrscheinlichkeit für die Ziel-Sharpe-Ratio nötig ist.
- Verlustschwelle, Gewinnschwelle und Wettfrequenz setzt der Portfoliomanager, während die Trefferwahrscheinlichkeit vom Markt kommt.

## Funktionsweise

- Der Markt legt mit seinem eigenen Preisverhalten die Barriere, die eine plötzliche Richtungsänderung erst überwinden muss. Deshalb ist Ausbruchshandel verbreitet.
- Das Volumen des Bruchs entscheidet, ob dieser Schutz real ist. Ein Bruch auf niedrigem Volumen ist eine Falle und liefert keinen verlässlichen Stop-Anker.
- Die alten Zonen bleiben als Karte liegen und zeigen später, wo ein Stop an historischem Kampf, an Umkehr oder an Unterstützung orientiert werden kann.
- Bei positivem Faktor liegt der Stop auf dem Negativen von ptSl[1] mal trgt.
- Gemessen wird das an der Pfadrendite, die mit der Positionsseite multipliziert wurde.
- Der Stop-Zeitpunkt ist der früheste Index, an dem diese Pfadrendite unter der Stop-Schwelle liegt.
- Die Vorgabewerte für die Grenzen stammen aus der Tagesvolatilität von getDailyVol.

## Voraussetzungen


## Anwendung im Trading

- Eine starke sichtbare Plattform hilft, das Risiko zu beurteilen. Ist sie schwach, kann der Einstieg warten.
- Eine schon bestehende Position, deren erwartetes Ergebnis ein Verlust ist, braucht einen Ausstieg, der diesen Verlust begrenzt.
- Ein rationaler Marktteilnehmer eröffnet keine Position, deren erwartetes Ergebnis ein Verlust ist.

## Regeln und Kriterien

- Ein Rücklauf über das Bracket-Extrem hinaus soll den Ausstieg auslösen.
- Den Trade aus eigenem Entschluss beenden, statt zu warten, bis Stops einen herausnehmen.
- Beginnt die anfängliche Zuversicht eines Open-Drive nachzulassen, ist das der Anlass zum Ausstieg.
- Beim Balance-Area-Bruch liegt der Ausstiegsstop ein paar Ticks jenseits des Bruchpunkts, weil die Rückkehr in die Area die Ablehnung anzeigt.
- Beim Gap-Trade liegt der Stop dort, wo eine Preisrotation die Gap vollständig durchhandelt und damit löscht.
- Fehlt die Folge, wird mit kleinem Verlust ausgestiegen, sobald der Preis zurück in die Balance-Area handelt.
- Stops werden an zuvor bekannte Referenzpunkte gelegt.
- Ausgestiegen wird, sobald Bedingungen entstehen, die der angenommenen Marktstimmung widersprechen.
- In der Konfiguration [1,1,1] gibt es neben Gewinnziel und Haltedauer eine maximale Verlusttoleranz.
- In der Konfiguration [0,1,1] endet die Position nach einer Anzahl Bars, sofern sie nicht vorher ausgestoppt wird.
- Die Konfiguration [0,1,0] hält ausschließlich bis zum Stop und gilt als ziellos.
- Die Konfigurationen [1,0,1] und [1,0,0] führen die Position ohne Rücksicht auf zwischenzeitliche nicht realisierte Verluste.

## Risiken und Grenzen

- Eine solche Strategie trägt eigenes Risiko, auch wenn die gehaltenen Instrumente eine niedrige Volatilität haben.

## Beispiele

- Im SLV lag ein Stop unter dem Docht des Hammers.
- Im AUD/USD auf 15 Minuten lag der Short-Stop über dem Docht der ersten Shooting Star.
- Bei Procter & Gamble lieferten die Volumenunterschiede der beiden Stauzonen einen Anhalt für die Stop-Orders.
- Im GBP/USD auf 15 Minuten saß der Stop unter dem letzten Pivot-Tief der etwa 70 Kerzen langen Stauung.
- Auf der Stunde lag der Schutz über dem Markt, nachdem der alte Boden zur Decke geworden war.
- Im Beispiel beträgt die Verlustschwelle minus 0,01 und das Gewinnziel 0,005.
- Bei Verlustauszahlung minus 0,01 und Gewinnauszahlung 0,005 zehrt ein Rückgang der Trefferwahrscheinlichkeit von 0,7 auf 0,67 den erwarteten Gewinn auf, weil die Schwelle für eine Sharpe Ratio von null bei zwei Dritteln liegt.

## Unterschiedliche Quellenpositionen

- Praktisch keine Veröffentlichung berücksichtigt den Stop-Loss, wenn sie Beobachtungen labelt, und das kennzeichnet für den Autor den Zustand der Anlage-Literatur.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Markets in Profile_ Profiting from the Auction Process.pdf, S. 181–200 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-014-p181-p200|S. 181–200]]
- Mind Over Markets_ Power Trading with Market Generated Information, Updated Edition.pdf, S. 269–288 → [[Trading/Pilot/blocks/mind-over-markets/mind-over-markets-block-017-p269-p288|S. 269–288]]
- Mind Over Markets_ Power Trading with Market Generated Information, Updated Edition.pdf, S. 288–296 → [[Trading/Pilot/blocks/mind-over-markets/mind-over-markets-block-018-p288-p296|S. 288–296]]
- A Complete Guide to Volume Price Analysis.pdf, S. 96–115 → [[Trading/Pilot/blocks/a-complete-guide-to-volume-price-analysis-pdf/a-complete-guide-to-volume-price-analysis-pdf-block-006-p096-p115|S. 96–115]]
- A Complete Guide to Volume Price Analysis.pdf, S. 115–134 → [[Trading/Pilot/blocks/a-complete-guide-to-volume-price-analysis-pdf/a-complete-guide-to-volume-price-analysis-pdf-block-007-p115-p134|S. 115–134]]
- A Complete Guide to Volume Price Analysis.pdf, S. 134–153 → [[Trading/Pilot/blocks/a-complete-guide-to-volume-price-analysis-pdf/a-complete-guide-to-volume-price-analysis-pdf-block-008-p134-p153|S. 134–153]]
- Advances in Financial Machine Learning.pdf, S. 58–77 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-004-p058-p077|S. 58–77]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]

## Verwandte Themen
