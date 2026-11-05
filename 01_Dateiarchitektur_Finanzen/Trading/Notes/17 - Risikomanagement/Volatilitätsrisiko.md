---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/17 - Risikomanagement/17 - Risikomanagement|17 - Risikomanagement]]"
weitere_hauptthemen: []
unterthema: "Risikomessung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Volatilitätsrisiko


## Kurzdefinition


## Kernaussagen

- Wären die Preise so eng an die Fundamentalwerte gebunden, wie die Effizienzmarkthypothese behauptet, müsste das Ausmaß der Preisänderungen dem Ausmaß der Änderungen der Fundamentaldaten ähneln. Studien zeigen, dass die Preise weit volatiler sind als die Fundamentaldaten.
- Wird der Fundamentalwert als Barwert künftiger Dividenden definiert, können Änderungen dieses Fundamentalwerts die hohe Volatilität der Preise nicht erklären.
- Die Technologieaktienblase, die im Frühjahr 2000 platzte, und die Blase der japanischen Aktienkurse in den späten 1980er Jahren sind Beispiele für Preisbewegungen, die sich nicht durch Änderungen des Fundamentalwerts erklären lassen.
- Die Effizienzmarkthypothese sagt große Preisänderungen nur voraus, wenn wesentliche neue Information in den Markt kommt. Die Evidenz stimmt dem nicht zu.
- Der Börsenkrach vom Oktober 1987 war nicht von Nachrichten begleitet, die einen Kursrückgang von mehr als 20 Prozent gerechtfertigt hätten.
- Eine Studie von Cutler von 1991, die Shleifer zitiert, untersuchte die 50 größten Ein-Tages-Preisbewegungen seit dem Ende des Zweiten Weltkriegs. Viele dieser Ereignisse waren nicht mit wesentlichen Nachrichten verbunden.
- Roll zeigte, dass Schwankungen im Preis von Frozen-Orange-Juice-Futures oft ohne Entwicklungen beim Wetter auftraten, dem wichtigsten fundamentalen Einfluss dieses Markts.
- Roll zeigte außerdem, dass Bewegungen einzelner Aktien oft nicht mit Unternehmensnachrichten verbunden sind.
- Behavioral Finance bietet knappe Erklärungen der überschüssigen Marktvolatilität wie auch der Überschussrenditen von Strategien auf veralteter Information.
- Das Capital Asset Pricing Model verwendet nur einen Risikofaktor, die Volatilität einer Aktie relativ zum Marktindex. Fama und French ersetzen es durch ein Modell mit drei Risikofaktoren.
- Die Rendite eines Wertpapiers kann von seiner Volatilität abhängen; das GARCH-M-Modell setzt dafür eine Risikoprämie in die Mittelgleichung, M steht für GARCH in the mean.
- Ein einfaches GARCH(1,1)-M lautet rt gleich mü plus c mal sigma t quadrat plus at, mit derselben Varianzgleichung wie ein GARCH(1,1); c heißt Risikoprämienparameter.
- Ein positives c bedeutet, dass die Rendite positiv mit ihrer Volatilität zusammenhängt. Andere Formen sind c mal sigma t und c mal dem Logarithmus der bedingten Varianz.
- Für die monatlichen S&P-500-Überschussrenditen von Januar 1926 bis Dezember 1991 lautet die Schätzung rt gleich 0,0055 plus 1,09 mal sigma t quadrat plus at und sigma t quadrat gleich 0,0000876 plus 0,123 mal a, t minus 1, quadrat plus 0,849 mal sigma, t minus 1, quadrat.
- Die Standardfehler der beiden Mittelparameter sind 0,0023 und 0,818, die der Varianzparameter 0,0000251, 0,0205 und 0,0196; die Risikoprämie ist positiv, aber auf dem 5-Prozent-Niveau nicht signifikant.
- In S-Plus heißen die drei Prämienspezifikationen var.in.mean, sd.in.mean und logvar.in.mean.
- In Nelsons EGARCH für die täglichen CRSP-Überschussrenditen steht die bedingte Varianz ebenfalls als Regressor in der Mittelgleichung; die geschätzte Risikoprämie c ist minus 3,361 mit Standardfehler 2,026, negativ und statistisch insignifikant.
- Die serielle Abhängigkeit der bedingten Varianz schreibt über die Risikoprämie serielle Korrelationen in die Renditereihe.
- Diese Value-Manager meinen mit Risiko die Aussichten für Gewinnmargen und Bilanz, nicht die Preisvolatilität des Marktes.
- Sie richten sich auf das Geschäftsrisiko und behandeln die Aktienvolatilität mit der Geringschätzung, die sie nach Montier verdient.
- Keynes und Graham teilten den Glauben an wertbasiertes Investieren und erkannten zugleich die Gefahren übermäßiger Volatilität.
- Sie kennzeichnen den Markt insgesamt als bipolar, also als manisch-depressiv.
- Risikomanager arbeiten mit nachlaufender Korrelation und Volatilität und raten bei fallenden Märkten als Erste zum Verkauf der Positionen.
- Keynes und Graham waren sich der exzessiven Volatilität bewusst, die die Märkte plagt und den Anlegern Schmerz bereitet, und zugleich dessen, dass diese Preisvolatilität die Quelle der Outperformance ist.
- Keynes: Die Tagesschwankungen der Gewinne bestehender Anlagen, offensichtlich flüchtig und unbedeutend, haben einen völlig übertriebenen und sogar absurden Einfluss auf den Markt.
- Keynes: Eine konventionelle Bewertung aus der Massenpsychologie kann sich heftig ändern durch eine plötzliche Meinungsschwankung aus Faktoren, die den voraussichtlichen Ertrag kaum verändern.
- Keynes: Weitgehend sind es die Schwankungen, die die Schnäppchen hervorbringen, und die Unsicherheit aus den Schwankungen, die andere daran hindert, sie zu nutzen.
- Graham: Je weiter die Schwankungen und je länger sie in eine Richtung anhalten, desto schwerer ist es, den Anlagegesichtspunkt zu bewahren.
- Die Fußnote hält fest, dass das Thema exzessiver Volatilität später in früher Behavioral-Finance-Arbeit von Robert Shiller aufgenommen wurde, Shiller (1992).
- Graham setzt Beta nicht mit Risiko gleich: Preisvariabilität ja, Risiko nein; echtes Risiko ist der Verlust von Qualität und Ertragskraft durch wirtschaftliche Änderungen oder schlechteres Management, nicht der prozentuale Kursrückgang relativ zum Markt in einer Periode.
- Die bewährten Value-Manager sorgen sich um Geschäftsrisiko, nicht um Preisvolatilität.
- Der Anleger mit soliden Aktien soll nach Graham sizable Rückgänge und sizable Anstiege erwarten und die Notierungen nutzen oder ignorieren.
- Das US-Value-Portfolio hat seit 1988 eine Standardabweichung von 17,7 Prozent, das Portfolio mit hohem prognostiziertem Wachstum eine von 25,1 Prozent.
- Die CAGRs sind mit 13,7 Prozent und 14,0 Prozent fast gleich, sodass Value auf risikobereinigter Basis deutlich geschlagen hätte.
- Montier wendet das gegen die Behauptung, Value-Aktien seien riskanter.
- Keines der Value-Portfolios erzeugt eine negative absolute Rendite, global wie in den USA, in Europa und in Japan, was Montier als Schutz und nicht als höheres Risiko liest.
- Beta ist keine gute Beschreibung von Risiko: das CAPM unterschätzt Niedrig-Beta-Renditen, überschätzt Hoch-Beta-Renditen, und langfristig besteht im Wesentlichen kein Zusammenhang zwischen Beta und Rendite.
- Graham: Beta misst vergangene Kursschwankungen. Preisvariabilität ist nicht Risiko; echtes Anlagerisiko ist der Verlust von Qualität und Ertragskraft durch die Wirtschaft oder das Management.
- Unter den 600 größten US-Aktien seit 1963 und in Europa 1986 bis 2006 lieferte niedriges Beta höhere Renditen als hohes Beta.
- Ein Minimum-Varianz-Portfolio schlug den Marktindex mit höherer Rendite und niedrigerem Risiko.
- Die Fundamentalindizes hatten im Schnitt 53 Basispunkte weniger Volatilität und trotzdem 278 Basispunkte p.a. mehr Rendite als die kapitalisierungsgewichteten MSCI-Indizes.
- Die Branche ersetzt die Varianz der Renditen durch den Tracking Error; niedriges und hohes Beta verlieren darin ihre Bedeutung, und der Marktindex wird zum risikofreien Bezug.
- In Markturbulenz ist die historische Volatilität voraussichtlich ein schlechter Führer, weil die Modelle die jüngeren Bedingungen fortschreiben.
- Die Volatilitäten könnten sich gegenüber den aktuellen Niveaus leicht verdoppeln oder verdreifachen. Zusammen mit einer Unterschätzung aus unpassenden Korrelationen um 20 bis 30 Prozent droht ein Desaster.
- Die historische Volatilität des S&P 500 ist auf allen gezeigten Maßen gefallen. Die Unterschätzung des im Aktienmarkt gerade eingegangenen Risikos ist potenziell massiv.
- Alle Hedgefonds-Stile scheinen Geld zu verlieren, wenn die Volatilität steigt oder der Aktienmarkt fällt; ein gemeinsamer Treiber ist der Verkauf von Volatilität.
- Hohe Gebühren sind für Pensionsfonds schwer zu rechtfertigen, wenn der Verkauf von Volatilität der eigentliche Performancetreiber ist.
- Der Ausstieg aus diesen gleichgerichteten Positionen verheißt nichts Gutes, und Fonds von Hedgefonds liefern bei medianen Korrelationen von 0,65 keinen Diversifikationsnutzen.
- Unter den Rohstoffindizes 1991–2005 hat der GSCI mit 6,3 Prozent eine höhere Volatilität als der DJ-AIG mit 4,4 und der CRB mit 2,9 Prozent.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Steigen Volatilität und Korrelation, stoßen Fonds an ihre Limits und müssen verkaufen. Der Verkauf treibt die Volatilität weiter, ein VaR-Teufelskreis.
- Volatilität, die gemessen wird, während ein gemeinsamer Trade aufgebaut wird, ist fast sicher zu niedrig.
- Ändert sich die Volatilität zugleich mit der Korrelation, was äußerst wahrscheinlich scheint, ist die aus den Korrelationen berechnete VaR-Unterschätzung nur der Anfang.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 343–362 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-019-p343-p362|S. 343–362]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 153–172 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-009-p153-p172|S. 153–172]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 286–305 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-016-p286-p305|S. 286–305]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 305–324 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-017-p305-p324|S. 305–324]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 324–343 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-018-p324-p343|S. 324–343]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 438–457 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-024-p438-p457|S. 438–457]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 457–476 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-025-p457-p476|S. 457–476]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 609–628 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-033-p609-p628|S. 609–628]]

## Verwandte Themen
