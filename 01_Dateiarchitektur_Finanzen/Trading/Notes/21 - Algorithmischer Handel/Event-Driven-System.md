---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Strategien und Ausführung"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Event-Driven-System


## Kurzdefinition

- Complex Event Processing bezeichnet ein Programm, das auf ein Ereignis sofort reagiert und die passende Aktion ausführt. Die Ereignisse sind gewöhnlich ein neuer Tick oder eine Nachricht.

## Kernaussagen

- Intraday-Momentum kann durch Ereignisse jenseits der Preisaktion entstehen, darunter Gewinnmeldungen, Änderungen von Analystenempfehlungen und makroökonomische Nachrichten.
- Dass solche Ereignisse Zeitreihenmomentum erzeugen, ist lange bekannt; der Text stellt Forschung zu den einzelnen Ereigniskategorien vor.
- Neben Gewinnmeldungen können Earnings Guidance, Analystenratings und Empfehlungsänderungen, Same-Store-Sales und Airline Load Factors einen Drift nach der Ankündigung zeigen.
- Theoretisch sollte jede Ankündigung, die den fairen Marktwert neu bewerten lässt, den Kurs zu einem neuen Gleichgewicht bewegen.
- Hafez (2011) untersucht diese Ereignisse und ihre Wirkung auf die Renditen nach dem Ereignis umfassend.

## Funktionsweise

- Für den algorithmischen Trader ist entscheidend, dass das Programm ereignisgetrieben ist und nicht bar-getrieben. Es fragt Preise oder Nachrichten nicht erst am Ende jedes Bars ab. Zwischen Ereignis und Reaktion liegt deshalb keine Wartezeit bis zum Bar-Ende.
- Industrielle Live-Ausführungsprogramme sind ereignisgetrieben: Ein Trade wird durch das Eintreffen eines neuen Ticks ausgelöst, nicht durch das Ende eines willkürlichen Zeitbars.
- Sind die historischen Eingaben ebenfalls Tick-Daten, kann dasselbe Programm theoretisch eine Hochfrequenzstrategie backtesten, die von jedem Tick oder sogar von jeder Änderung im Orderbuch abhängt, sofern die Hardware stark genug ist. In MATLAB geht das auch, ist aber umständlich.
- Genügt die Unverzüglichkeit, reichen die Callback-Funktionen, die fast jede Broker-API bietet. Ein Callback feuert bei jedem neuen Tick oder jeder Nachricht. Eine einfache Regel wie der gleitende Durchschnitt der letzten Stunde ist damit leicht umzusetzen.
- Komplexe Regeln, etwa verkaufen, wenn der Orderflow der letzten halben Stunde positiv ist, der Preis über dem gleitenden Durchschnitt liegt, die Volatilität niedrig ist und gerade eine wichtige Nachricht kam, oder Klauseln wie during, between, afterwards und in parallel auf der Ereignisfolge, lassen sich nach Ansicht der CEP-Anhänger in einer CEP-Sprache knapper ausdrücken als in einer herkömmlichen Programmiersprache.
- FXone sieht aus wie Excel, der Rechenkern ist aber in einer Hochleistungssprache wie C++ geschrieben und nicht auf VB-Makros angewiesen. Jeder Tick, im Devisenfall eine neue Quote, berechnet alle Zellen neu. Ein interner Cache verhindert doppelte Abos derselben Daten. Verschiedene Arbeitsmappen und verschiedene Zellen derselben Mappe verarbeiten Daten und Orders gleichzeitig. Eine lange Rechnung in einer Zelle hält die anderen nicht davon ab, auf einen neuen Tick zu reagieren, etwa eine Order zu senden.

## Voraussetzungen

- Die meisten Plattformen schaffen die Ausführung von Hochfrequenzhandel, wenn die Strategie 1 bis 10 Millisekunden Latenz verträgt. Der größte Teil der zu überwindenden Latenz liegt in den Live-Marktdaten oder in der Orderbestätigung des Brokers. Praktisch jedes Programm außer Excel mit einem VB-Makro sendet eine neue Order in weniger als 10 Millisekunden, nachdem die letzten Marktdaten und der Orderstatus da sind. Software- oder Hardware-Latenz ist gewöhnlich nicht der Engpass, außer ein Programm überwacht Tausende Symbole.
- Eine neue Quote oder ein neuer Trade innerhalb von 1 bis 10 Millisekunden verlangt Colocation an der Börse oder im Rechenzentrum des Brokers und einen direkten Börsenfeed, nicht einen konsolidierten Feed wie das Consolidated Tape System von SIAC. Der Datenfeed von Interactive Brokers liefert nur Schnappschüsse alle 250 Millisekunden.
- Bei manchen Retail-Brokern vergehen bis zu sechs Sekunden zwischen Ausführung und Bestätigung an das Programm. Das schließt Hochfrequenzhandel aus. Selbst bei einer Bestätigungslatenz unter 10 Millisekunden oder bei direktem Marktzugang muss das Programm beim Broker beziehungsweise an der Börse stehen.
- Multithreading heißt, auf mehrere Ereignisse, gewöhnlich neue Ticks, gleichzeitig zu reagieren. Das ist wichtig, wenn viele Symbole gehandelt werden: Die Kauforder in AAPL darf nicht warten, weil das Programm gerade über den Verkauf von BBRY entscheidet. Java und Python können das von Haus aus. MATLAB braucht die Parallel Computing Toolbox und ist auf 12 unabhängige Threads begrenzt, zu wenig für 500 Aktien gleichzeitig. Listener werden dabei nicht taub: Während A ein Tick-Ereignis verarbeitet, empfängt B weiter Ticks und arbeitet sie danach ohne verlorene Ticks ab, nach Kuznetsov 2010.
- Colocation kann ein Cloud-Server oder VPS sein, etwa Amazon EC2, slicehost.com oder gogrid.com, vor allem gegen Strom- und Netzausfälle zu Hause oder im Büro. Ein Extranet eines privaten Betreibers wie BT Radianz, Savvis oder TNS garantiert eine Mindestgeschwindigkeit. Der nächste Schritt ist das Rechenzentrum des Brokers, Beispiele Lime Brokerage und FXCM, sodass Quotes und Bestätigungen über das interne Netz laufen. Die letzte Stufe ist der Server an der Börse oder am ECN selbst.
- Der Ping zum Quote-Server von Interactive Brokers beträgt etwa 55 Millisekunden vom Heimrechner, etwa 25 Millisekunden von Amazon EC2 und etwa 16 bis 34 Millisekunden von VPS-Standorten nahe beim Broker. Ein VPS verkürzt die Laufzeit nur, wenn er physisch nah und am Backbone hängt. Das ist selbst zu prüfen.
- Die Colocation an der Börse ist teuer und nützt nur mit Prime-Broker-Beziehung und Sponsored Access, also ohne die Infrastruktur des Brokers, typischerweise bei institutionellen Kommissionen oder einem Konto in Millionenhöhe, nach Johnson 2010. Bei Forex-Prime-Brokern und ECNs sind Anforderungen und Kosten niedriger. Currenex, EBS, FXall und Hotspot sitzen in großen Zentren wie Equinix NY4.
- Ein genannter täglicher Lieferant ist der Dow-Jones-Newswire über Newsware, weil jeder Meldung ein maschinenlesbarer Code für den Ereignistyp anhängt.
- Auslöser für den Einstieg zur Eröffnung sind nur Gewinnmeldungen nach 16:00 Uhr ET des Vortags und vor 9:30 Uhr ET.

## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Monate an Tick-Daten, Trades und Quotes, oft auf vielen Symbolen und manchmal mit Level-2-Quotes, überfordern den Speicher der meisten Rechner, wenn sie nicht besonders behandelt werden, etwa mit parallelem Rechnen. Die meisten Spezial-Backtesting-Plattformen sind dafür nicht gebaut und können Bid, Ask und Last mit Größen oder Level 2 nicht backtesten. Ein Hochfrequenz-Backtest braucht deshalb gewöhnlich ein eigenes Programm und sagt wegen der möglichen Verhaltensänderung der anderen Teilnehmer durch die eigene Order oft wenig über die Live-Profitabilität.

## Beispiele

- In der Vergleichstabelle der Open-Source-IDEs sind Algo-Trader und Marketcetera CEP-fähig. ActiveQuant, OpenQuant und TradeLink sind es nicht. Tick-basiert, auch event- oder stream-basiert genannt, sind ActiveQuant, Algo-Trader, Marketcetera und TradeLink. Bei OpenQuant ist die Tick-Basis mit einem Fragezeichen markiert. Die Tabelle vergleicht nur Open-Source-IDEs; institutionelle Spezialplattformen haben diese Eigenschaften typischerweise alle.
- Auch ohne CEP haben Plattformen oft Callback-Funktionen, sodass eine tick-basierte Strategie trotzdem durch Ticks ausgelöst werden kann.
- Nachrichtengetriebenes Trading braucht einen maschinenlesbaren Newsfeed. Progress Apama bindet die maschinenlesbaren Feeds von Dow Jones und Reuters ein, Deltix den News-Sentiment-Feed von Ravenpack. Marketcetera bietet einen Feed von benzinga.com, der die Liefergeschwindigkeit von Bloomberg, Dow Jones und Reuters wahrscheinlich nicht erreicht. Die meisten anderen Spezialplattformen und Open-Source-IDEs haben keinen solchen Feed.
- Ein eigenes Programm kann die API des News-Anbieters nutzen oder eine periodisch per FTP gelieferte News-XML-Datei lesen. Hochfrequenter Nachrichtenhandel braucht die teure API. Sonst gibt es günstigere Anbieter wie Newsware. Ereignisgetriebenes Trading wird in Kapitel 7 weiter behandelt.
- Ein rein technisches Modell wie das der Gewinnmeldungen zieht bei Fusionen und Übernahmen noch etwa 3 Prozent APR.
- Eigene Tests der Zinsentscheide des Federal Open Market Committee und der Veröffentlichung des Verbraucherpreisindex fanden auf EURUSD kein signifikantes Momentum.
- Clare und Courtenay berichten, dass britische Makrodaten und Zinsankündigungen der Bank of England in GBPUSD bis mindestens zehn Minuten nach der Ankündigung Momentum erzeugten; die Daten reichen bis 1999.

## Unterschiedliche Quellenpositionen

- Der Einwand lautet, Handelsregeln sollten einfach bleiben, um Data-Snooping-Bias zu vermeiden. Die CEP-Anhänger antworten, sie schürften keine beliebigen Regeln, sondern setzten um, was erfahrene Trader bereits als profitabel kennen. Der Autor ist nicht völlig überzeugt. Progress Apama hebt sich durch seine CEP-Technik ab.
- Hafez findet entgegen verbreiteter Annahme, dass die Aktie des Übernahmeziels nach der ersten Ankündigung stärker fällt als die des Käufers.
- Für die bis 1999 beobachtete Makro-Momentumdauer in GBPUSD erwartet der Text in jüngeren Jahren eine kürzere Dauer, falls das Momentum überhaupt noch besteht.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 173–186 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-013-p173-p186|S. 173–186]]

## Verwandte Themen
