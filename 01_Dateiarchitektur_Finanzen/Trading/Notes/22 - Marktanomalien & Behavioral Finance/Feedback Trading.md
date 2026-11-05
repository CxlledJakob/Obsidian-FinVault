---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/22 - Marktanomalien & Behavioral Finance/22 - Marktanomalien & Behavioral Finance|22 - Marktanomalien & Behavioral Finance]]"
weitere_hauptthemen: []
unterthema: "Verhaltensphänomene"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Feedback Trading


## Kurzdefinition

- Feedback Trading entsteht hier, wenn ein schwer vorhersagbares Ereignis Stop-Losses auslöst und die Bewegung dadurch verstärkt.
- Feedback ist die Rückführung der Ausgabe eines Systems als Eingabe in dasselbe System.

## Kernaussagen

- Fiedor argumentiert, dass von den möglichen künftigen Ausgängen der entropiemaximierende am profitabelsten sein kann, weil frequentistische Modelle ihn am wenigsten vorhersagen.
- Dieses am wenigsten vorhersagbare Szenario löst nach Fiedor am ehesten Stop-Losses aus und erzeugt einen Feedback-Mechanismus, der die Bewegung verstärkt.
- Der Feedback-Mechanismus zeigt sich als Runs in den Vorzeichen der Renditezeitreihe.
- Arbitrage liefert negatives Feedback. Zu hohe oder zu niedrige Preise lösen Arbitragehandel aus, der die Preise zu rationalen Niveaus zurückschiebt.
- Positives Feedback entsteht, wenn Anlegerentscheidungen von Nachahmung statt von unabhängiger Wahl beherrscht werden. Anleger springen auf eine Anfangsbewegung auf, kaufen nach erster Stärke oder verkaufen nach erster Schwäche, und verstärken eine kleine Bewegung zu einem großräumigen Trend.
- Trendfolge hängt von großräumigen Preisbewegungen ab und ist deshalb am wirksamsten, wenn positives Feedback dominiert.
- Positives Feedback kann einen Teufelskreis steigender oder fallender Preise auslösen, der die Kurse weit jenseits rationaler Niveaus trägt, selbst wenn die auslösende Bewegung gerechtfertigt war.
- Erwartungen werden unvollkommen an jüngere Änderungen angepasst. Manchmal wird zu wenig angepasst, der Konservatismus-Bias, manchmal sind Menschen überempfindlich und ändern die Erwartungen stärker, als gerechtfertigt ist.
- Anleger überreagieren besonders wahrscheinlich auf neue Information, die prominent ist. Eine einzelne große Preisänderung oder eine Folge ähnlicher Änderungen kann die Erwartungen zu stark verschieben.
- Diese Preisänderungen können sich selbst nähren und Preismomentum erzeugen, das zu einer Blase oder einem Crash führen kann.
- Eine Preisblase muss nicht in einem Crash, also einer negativen Blase, enden. Computersimulationen von Systemen mit Feedbackschleifen zeigen, dass Blasen gezackt und mit vielen Pausen entstehen und sich ähnlich wieder entleeren können.
- Wenn die späten 1990er Jahre eine Preisblase waren, scheint sie mit vielen zwischenliegenden Pausen zu enden.
- Robert Shiller hält Spekulationsblasen für natürlich vorkommende Ponzi-Systeme, die spontan entstehen, ohne die Machenschaften eines betrügerischen Promoters.
- Ein Trend steigender Preise wirkt als Aufruf zum Handeln, ähnlich den Gewinnen früher Anleger in einem Ponzi-System. Die Verkäufer der Wall Street verstärken die Botschaft, indem sie das Aufwärtspotenzial betonen und die Risikoseite herunterspielen, ohne lügen zu müssen.
- Die Parallelen sind für Shiller so klar, dass die Beweislast bei denen liegt, die die Ähnlichkeit bestreiten. Zu beweisen, dass der einfache Feedback-Mechanismus aus geschärftem Fokus, Nachahmung und übertriebenem Vertrauen an den Märkten wirklich arbeitet, ist dennoch schwer.
- Im BSV-Modell entsteht eine Feedbackschleife aus dem Fehler der kleinen Zahlen: Sehen Anleger Gewinne mehrmals nacheinander in dieselbe Richtung laufen, wechseln sie vom Zweifel am Trend zur Annahme, er sei echt. Der Konservatismus-Bias bremst die Annahme des neuen Glaubens anfangs. Das Zusammenspiel bestimmt die Geschwindigkeit, mit der spekulatives Feedback entsteht.
- Aus Sicht der technischen Analyse sind durch positives Feedback entstandene Trends eine Kaskade immer unempfindlicherer Trendfolge-Signale: Eine Anfangsbewegung löst das empfindlichste Signal aus, etwa ein sehr kurzfristiges Crossover gleitender Durchschnitte, das die Preise weit genug schiebt, um ein weniger empfindliches, etwa mittelfristiges, auszulösen, und so weiter.
- Eine starke Implikation positiver Rückkopplung ist, dass eine moderate Bewegung außergewöhnlich unwahrscheinlich ist. Preise bewegen sich entweder kaum oder sehr scharf. Positives Feedback-Trading hat Kursrückgänge durch die Geschichte verschärft.
- Dynamisches Hedging und VaR tragen exotische Namen, verstärken aber in dieser Darstellung schlicht die Markttrends. In einem schon fragilen, von Überkonfidenz, Kurzsichtigkeit und Momentum zusammengehaltenen Markt ist eine weitere Quelle positiven Feedbacks besonders gefährlich.

## Funktionsweise

- Es gibt negatives und positives Feedback. Bei negativem Feedback wird die Ausgabe mit einer negativen Zahl multipliziert und zurückgeführt, bei positivem Feedback ist der Multiplikator positiv.
- Negatives Feedback dämpft das Verhalten und treibt die Ausgabe zu einem Gleichgewicht zurück. Positives Feedback verstärkt das Verhalten und treibt die Ausgabe weiter vom Gleichgewicht weg.
- Die verbreitete Nutzung von VaR-Modellen droht positives Feedback-Trading auszulösen und Markttrends in beide Richtungen zu verstärken, weil zu viele Modelle die jüngere Geschichte in die Zukunft fortschreiben.
- Nach dem Basle-Abkommen haben interne VaR-Modelle einen Horizont von 10 Handelstagen oder zwei Kalenderwochen, ein Konfidenzintervall von 99 Prozent und ein Beobachtungsfenster von mindestens einem Jahr historischer Daten, das mindestens vierteljährlich aktualisiert wird. Das letzte Element erzeugt nach Montier die positive Rückkopplung.
- Fallen die Risikomaße, also nachlaufende Volatilität und nachlaufende Korrelationen, bleibt Risikobudget übrig, und der Druck steigt, die Positionen zu vergrößern, bis das Budget ausgeschöpft ist.
- Der VaR-Teufelskreis läuft umgekehrt: Steigen Volatilität und Korrelation und stoßen Fonds an ihre Limits, müssen sie Assets verkaufen. Der Zwangsverkauf treibt Volatilität und Korrelationen weiter, weitere Fonds stoßen an Limits und müssen ebenfalls verkaufen.
- Sobald die Nachfrage das Angebot übersteigt und die Preise steigen, folgt weitere reale und finanzielle Investition. Die positive Schleife lautet: Neue Investition erhöht das Einkommen, das weitere Investition anregt.
- Euphorie ist Momentum-Handel oder die Greater-Fool-Theorie, also Spekulation auf den nächsten Käufer, zusätzlich zur Investition für Produktion und Absatz.
- Geld- und Kreditschöpfung sind im Modell endogen und verstärken diesen Aufschwung, statt ihm nur äußerlich vorauszugehen.
- Im Bust wird die Schleife deflationär. Firmen senken Preise, um Volumen und Marktanteil zu kaufen, und verschärfen damit die Deflation. Notverkäufe von Assets drücken die Assetpreise, und die gekauften Assets erzeugen billigen Output, der die Preise im realen Markt und an den Finanzmärkten weiter untergräbt. Auch Konkurs und weitere Notverkäufe entwerten Assets.
- Was für die einzelne Firma rational ist, kann für die Wirtschaft falsch sein. Jeder Analyst mag seinen Firmen 15 Prozent langfristiges Wachstum zutrauen, in der Summe kann das nicht stimmen. Alle drei Wege des Schuldenabbaus sind extrem deflationär.
- Beim Informationserwerb besteht eine positive Rückkopplung: Je mehr Aufmerksamkeit eine Variable erhält, desto wertvoller wird neue Information über sie, und die Fokussierung verstärkt sich weiter.
- Fallen die Preise, können Anleger das als Verkauf der anderen und als Angriff auf die Blase lesen und sich anschließen, sodass ein sich selbst erfüllender Abschwung entsteht.
- Scheitert ein solcher Angriff, wird die Blase nach Abreu und Brunnermeier vorübergehend gestärkt.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Das Schema ist nach Charles Ponzi benannt, der die Idee in den 1920er Jahren erfand. Es verspricht eine hohe Rendite, setzt das Geld der Anleger aber nicht wie versprochen ein, sondern bezahlt frühere Anleger mit den Einlagen neuer. Ponzis ursprüngliches Schema beruhte auf internationalen Postcoupons.
- Eine Hausfrau aus einer Kleinstadt in Alaska sammelte über sechs Jahre schätzungsweise 10 bis 15 Millionen Dollar, indem sie 50 Prozent Rendite versprach. Angeblich beruhte das Geschäft auf ungenutzten Vielfliegermeilen großer Firmen und ähnelte Ponzis ursprünglichem Schema.
- Die Zahl der vom Betrug beeinflussten Personen folgt einer Kurve ähnlich der Ausbreitung einer Infektion. Ist der Vorrat noch unbeteiligter Spekulanten erschöpft, fehlen neue Einlagen, um die letzte Anlegerrunde zu bezahlen, und das Schema bricht zusammen.
- LTCM nutzte VaR als Risikokontrolle, und die Bond-Arbitrage-Desks der Banken mit denselben Trades ebenfalls. Als die Modelle Gefahr signalisierten, lief die beschriebene Rückkopplung und endete in einem Notverkauf epischen Ausmaßes.
- Die Abwicklung des Dollar-Yen-Carry in der Woche ab dem 5. Oktober 1998, in der der Dollar 15 Prozent gegen den Yen verlor, wird als positives Feedback eines überfüllten Trades gedeutet, nicht als allgemeine Dollar-Schwäche: Dollar/D-Mark fiel dieselbe Woche um weniger als 2 Prozent.
- Portfolio Insurance, dynamisches Hedging und informelle Stop-Losses spielten 1987 eine große Rolle im Crash, nach Shiller 1987 und 1989.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 286–305 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-016-p286-p305|S. 286–305]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 362–381 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-020-p362-p381|S. 362–381]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 172–191 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-010-p172-p191|S. 172–191]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 191–210 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-011-p191-p210|S. 191–210]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 381–400 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-021-p381-p400|S. 381–400]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 457–476 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-025-p457-p476|S. 457–476]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 476–495 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-026-p476-p495|S. 476–495]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 495–514 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-027-p495-p514|S. 495–514]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 514–533 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-028-p514-p533|S. 514–533]]

## Verwandte Themen
