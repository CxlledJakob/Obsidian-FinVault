---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/17 - Risikomanagement/17 - Risikomanagement|17 - Risikomanagement]]"
weitere_hauptthemen: []
unterthema: "Portfoliorisiko"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Diversifikation


## Kurzdefinition

- Diversifikation nur nach Assetklasse, Sektor und Einzeltitel genügt nicht; nötig ist zusätzlich Diversifikation nach Timeframe.
- Timeframe-Diversifikation setzt die Analyse in Long- und Short-Ideen um und nicht nur in mögliche Long-Positionen.
- Ein diversifiziertes Portfolio berücksichtigt die Korrelationen zwischen den Anlagen, statt alles in die Titel mit den höchsten erwarteten Renditen zu legen.

## Kernaussagen

- Timeframe-Diversifikation heißt, kurze, mittlere und lange Laufzeiten zugleich zu halten, wie im Fixed Income üblich. Für Aktieninvestoren und Berater gilt dasselbe.
- Gelingt sie, wirkt sie als Hedge gegen große Liquidationswellen, Short-Eindeckungsrallyes und andere kurze, nachrichtengetriebene Bewegungen, die den Markt an den Bruchpunkt bringen.
- Auch in einem langfristigen Trend können Gegenbewegungen leicht 5 bis 10 Prozent zurücknehmen.
- Sektoren, Branchen und Einzeltitel laufen häufiger gegenläufig oder rotieren, als dass sie sich gemeinsam bewegen.
- Zur Streuung gehört, Titel oder Märkte zu shorten, die voraussichtlich auseinanderlaufen.
- Nur in eine Richtung positioniert zu sein ist riskant, weil Märkte abrupt drehen können.
- Markowitz' Fluch besagt, dass mit stärkerer Korrelation der Anlagen der Bedarf an Diversifikation steigt, die Lösungen aber instabiler werden.
- Der Nutzen der Diversifikation wird oft durch Schätzfehler mehr als aufgezehrt.
- Hierarchical Risk Parity baut ein diversifiziertes Portfolio aus der Information der Kovarianzmatrix und braucht dafür keine invertierbare Matrix.
- Eine Baumstruktur verbindet N Knoten mit nur N minus 1 Kanten, sodass Gewichte nur unter Peers auf den Hierarchieebenen neu verteilt werden.
- Die Gewichte laufen von oben nach unten, analog zum Aufbau vieler Manager von der Assetklasse über Sektoren zu Einzeltiteln.
- Hierarchical Risk Parity kompromittiert zwischen Streuung über alle Anlagen und Streuung über Cluster auf mehreren Hierarchieebenen.
- Dieser Kompromiss aus beiden Streuungen schützt besser gegen gemeinsame und gegen idiosynkratische Schocks als CLA oder das Inverse-Varianz-Portfolio.
- Exakte analytische Lösungen können deutlich schlechter abschneiden als näherungsweise Machine-Learning-Lösungen.
- De Miguel und Koautoren (2009) zeigen, dass naive gleichgewichtete Portfolios Mean-Variance- und risikobasierte Optimierung außer Stichprobe schlagen.
- Die große Zahl möglicher Aktienpaare macht Diversifikation leicht, doch das Gesetz der großen Zahlen hilft nur, wenn die erwartete Out-of-Sample-Rendite eines einzelnen Paars positiv ist; der Autor hat das bei Aktienpaaren nicht gefunden.
- Die kleinen Gewinne der guten Paare wurden vollständig von den großen Verlusten der schlecht gelaufenen Paare überwogen.
- Weil die meisten Futures und Währungen Momentum zeigen, erlauben Momentum-Strategien eine echte Risikostreuung über verschiedene Assetklassen und Länder.
- Momentum-Strategien zu einem Portfolio aus Mean-Reversion-Strategien hinzuzufügen ergibt höhere Sharpe Ratios und kleinere Drawdowns als jeder Strategietyp allein.
- Theoretisch macht die große Zahl der Aktien Diversifikation leicht, wenn Paare aus einem Sektor wegen gemeinsamer ökonomischer Faktoren kointegrieren.
- Ein Portfolio vieler Aktienpaare hilft nur, wenn die erwartete Out-of-Sample-Rendite des einzelnen Paares positiv ist. Der Autor hat das bei Aktienpaaren nicht gefunden: die kleinen Gewinne der guten Paare werden von den großen Verlusten der entgleisten Paare aufgezehrt.
- Das SPY-Bestandteilportfolio ist mit etwa 98 Aktien breit gestreut. Müssen wenige Titel wegen einer Leerverkaufsbeschränkung entfallen, bleibt die Wirkung begrenzt.
- Bei querschnittlicher Mean Reversion ist nicht jede einzelne Aktie profitabel, manche dienen als Hedge. Gewinne entstehen nur über alle Aktien zusammen.
- Buy-on-Gap handelt an einem Tag nur wenige Aktien und hat deshalb keine große Kapazität. Die reine Long-Fassung erschwert zusätzlich das Risikomanagement.
- Eine Variante kauft mehr Aktien, begrenzt aber die Zahl innerhalb desselben Sektors. Eine andere ist long die Aktien und short Aktienindex-Futures.
- Weil die meisten Futures und Währungen Momentum zeigen, lassen sich Risiken wirklich über Assetklassen und Länder streuen.
- Momentum-Strategien zusätzlich zu einem Portfolio aus Mean-Reversion-Strategien erzeugen höhere Sharpe Ratios und kleinere Drawdowns als jeder Typ für sich.
- Die Kelly-Allokation über das Eigenkapital des Gesamtportfolios lässt gute Strategien schlechte kurzfristig subventionieren; Kelly auf jede Strategie einzeln enthebelt die zuletzt schlechten schnell.
- Mathematisch ist die Gesamtallokation optimal, aber nur wenn die erwarteten Renditen und Volatilitäten unverändert bleiben, was nach einem schweren Drawdown zweifelhaft ist.
- Die Erfahrung des Autors ist, dass die einzelne Anwendung praktischer ist, damit jede underperformende Strategie schnell eingeht.
- Bei zufälligen Sprüngen wird der Markt unvollständig, und die üblichen Hedge-Argumente reichen zur Optionsbewertung nicht.
- Ist die Zahl der verfügbaren Titel sehr groß, ist das Risiko plötzlicher Sprünge diversifizierbar; der Markt zahlt dann über den risikofreien Zins hinaus keine Risikoprämie für das Tragen dieses Risikos.
- Unter dieser Diversifizierbarkeit lässt sich eine Optionspreisformel ableiten, die nicht von der Risikoeinstellung abhängt.
- Alternativ kann man zu einem gegebenen Satz von Risikoprämien ein risikoneutrales Maß P* wählen und den Preis darunter berechnen.
- Der Value at Risk erfüllt die Subadditivität nicht: das Risikomaß zweier Portfolios nach dem Zusammenlegen muss nicht kleiner oder gleich der Summe der Risikomaße vor dem Zusammenlegen sein.
- Die Kovarianzstruktur eines Renditevektors ist für die Portfolioauswahl wichtig. Die Hauptkomponentenanalyse erklärt diese Struktur durch wenige Linearkombinationen und senkt damit die Dimension.
- Ein Eigenwert null der Kovarianz- oder Korrelationsmatrix bedeutet eine exakte lineare Beziehung zwischen den Komponenten. Ist der kleinste Eigenwert null, ist die zugehörige Hauptkomponente konstant, und der Zufallsvektor enthält nur k−1 zufällige Größen.
- Für fünf monatliche Aktienrenditen von IBM, Hewlett-Packard, Intel, J.P. Morgan Chase und Bank of America erklären die ersten beiden Hauptkomponenten der Korrelationsmatrix etwa 74 Prozent der Gesamtvariabilität. Die erste ist eine ungefähr gleich gewichtete Marktkomponente, die zweite der Unterschied zwischen Technologie und Finanzwerten.
- Entgegen der klassischen Finanztheorie führen diese Value-Investoren hoch konzentrierte Portfolios; Tracking Error hat für sie wenig oder keine Bedeutung.
- Über die zehn Fonds liegt die durchschnittliche Zahl der Unternehmen bei rund 35 und ohne die internationalen Fonds näher bei 20, während der durchschnittliche US-Inlands-Mutual-Fund rund 160 Aktien hält.
- Im Schnitt liegen fast 40 Prozent der Assets in den Top-Ten-Positionen, in Tabelle 23.2 sind es 38,8 Prozent; über ein weites Fondsuniversum machen die Top Ten nur rund 10 Prozent der Assets aus.
- Nicht zu investieren ist der Default dieser Manager: Sie brauchen einen Grund zum Kauf, nach Graham und Dodd eine Sicherheitsmarge.
- Der durchschnittliche Fondsmanager sorgt sich mehr um Tracking Error und Benchmark-Risiko als um die beste Anlage für die Kunden; sein Default ist Eigentum, und er braucht einen guten Grund, eine Aktie nicht zu halten.
- Keynes schrieb am 6. Februar 1942 an F. C. Scott, Safety-first als kleines Spiel in vielen Firmen, über die man kein Urteil habe, statt eines substanziellen Einsatzes dort, wo die Information ausreiche, sei eine Travestie der Anlagepolitik.
- Loeb schreibt in The Battle for Investment Survival, Diversifikation sei das Eingeständnis, nicht zu wissen, was zu tun ist, und der Versuch, einen Durchschnitt zu treffen.
- Die Konzentration dieser Fonds ist keine bewusste Wahl, sondern folgt aus der Disziplin, weil es schlicht nicht viele gute Value-Gelegenheiten gibt.
- Das Brandes Institute (2004) findet, dass konzentrierte Portfolios für sich weder bessere Renditen noch bessere volatilitätsadjustierte Renditen liefern; die Konzentration der Value-Gruppe ist das Ergebnis eines Prozesses.
- Die Untersuchung der besten Value-Investoren zeigte konzentrierte Portfolios als gemeinsamen Zug, und Keynes stimmt dem zu.
- Keynes: Ein konzentriertes Portfolio ist nicht notwendig eine unausgewogene Position; die perfekte Strategie ist eine ausgewogene Lage, also eine Vielfalt von Risiken trotz großer Einzelpositionen und wenn möglich entgegengesetzter Risiken.
- Montier vermutet, dass Keynes und Graham in der Praxis nicht uneins wären: Graham glaubte an Diversifikation, hätte aber wenig übrig für Positionen in großen Aktien, über die man nichts weiß.
- Portfolios auf absoluten statt sektorrelativen Maßen verringern die Sektordiversifikation und können ziemlich große Sektorwetten erzeugen.
- Sektorbeschränkungen, die erst nachträglich gesetzt werden, mindern das Exposure auf den jeweiligen Faktor und möglicherweise die künftigen Renditen.
- Ein sektorrelativer Ansatz kann von Anfang an ein diversifizierteres Portfolio erlauben, ohne das Exposure auf den Faktor zu mindern.
- Der Kauf eines Sektors mischt teure und billige beziehungsweise momentumstarke und momentumschwache Titel und verdünnt die Prämie; je feiner die Abstufung, desto besser.
- Absolute Bewertung führt zu großen Sektorwetten, die langfristig profitabel sein können, aber anhaltende Underperformance erzeugen, wie bei Value-Managern in der TMT-Blase.
- Ein Portfolio auf sektorrelativen statt marktweiten Maßen soll diversifizierter sein und dadurch vielleicht bessere risikobereinigte Renditen bieten.
- Das sektorrelative Maß mindert die Sektorschiefe, diversifiziert die Branchenexposure aber nicht vollständig: liegt ein Sektor eng beieinander, fehlt er in Long- und Short-Portfolio.
- Gegenüber dem Zwang, alle Sektoren abzubilden, erlaubt diese Methode ein breiteres Faktorexposure und erhofft bessere Renditen.
- Beim unadjustierten globalen Kurs-Buchwert wiegt der Materialsektor im Long-Portfolio 12 Prozent und im Short-Portfolio 5 Prozent, also fast 7 Prozentpunkte Differenz; sektorrelativ sinkt diese Differenz auf fast null.
- Einzelportfolios innerhalb jedes Sektors waren nicht optimal, weil viele Sektoren zu wenig liquide Titel hatten und Tritiles statt Dezile oder Quintile den Faktorabstand und das Alpha verkleinerten.
- Die Betas der Long-Short-Länderportfolios sind im Allgemeinen negativ und deuten auf mögliche Diversifikationsgewinne.
- Eine CAPM-Annahme lautet, Anleger steuerten Risiko durch Diversifikation.
- Portable Alpha, das dieselbe Aktie zugleich long und short hält, ist hochgradig ineffizient, weil die Kosten des Short verschenkt werden.
- Ein Minimum-Varianz-Portfolio und fundamental gewichtete Indizes erzeugen höhere Rendite bei niedrigerem Risiko als der kapitalisierungsgewichtete Index, entgegen der Behauptung, das Marktportfolio sei bereits effizient.
- LTCM hielt sich 1998 über Märkte für gut diversifiziert. Geografische Diversifikation schützte nicht; nötig war Diversifikation über Strategien. Die Vorherrschaft der Convergence-Trades ließ die Firma bei anhaltender Divergenz an allen Trades zugleich bluten.
- Sind die Positionen verschieden, lassen sich Assets kreuzen, und die Preisrückkopplung eines VaR-Kreises bleibt aus. Halten alle dieselben Positionen, fehlt dieser Ausgleich.
- Portable Alpha ist nur sinnvoll, wenn das Alpha zu allen Elementen des bestehenden Portfolios unkorreliert ist. Sonst ist der Anleger long und short derselben Sache.
- Die Wahl des Rohstoffindex verändert Rendite und Diversifikationsnutzen erheblich: der GSCI besteht zu 76 Prozent aus Energie, der CRB nur zu 18 Prozent, der DJ-AIG zu 33 Prozent.
- Erb und Harvey (2005) zeigen für Dezember 1982 bis Mai 2004 eine Überschussrendite des GSCI von 4,5 Prozent pro Jahr; ein gleichgewichteter Buy-and-Hold-Index aus denselben Rohstoffen liefert nur 0,7 Prozent pro Jahr.
- Bei einer medianen Korrelation der Hedgefonds-Strategien von 0,65 ohne Dedicated Shorts liefern Fonds von Hedgefonds keinen Diversifikationsnutzen und sind zusätzlich eine Kostenfalle.
- Über 1991–2005 betragen Rendite und Risiko: DJ-AIG 4,1 und 4,4 Prozent, GSCI 5,7 und 6,3, CRB 3,1 und 2,9. Risikoadjustiert ist der CRB in dieser Stichprobe der beste Index, allein als Funktion des Zeitraums.
- Jedes Portfolio lässt sich zerlegen in eine 100-Prozent-Position im Benchmark plus ein Long-Short-Portfolio mit Nettoanlage null. Das Long-Short-Portfolio sind alle aktiven Wetten. Die Active Share ist der Grad der Nichtüberlappung mit dem Benchmark: 100 Prozent bedeutet keinerlei Überlappung.
- Active Share gleich ein Halb mal die Summe der Beträge der Gewichtsdifferenzen von Fonds und Index über alle Assets.
- Hohe Active Share und niedriger Tracking Error kennzeichnen diversifizierte Stockpicker: viele Wetten, aber ein Portfolio, das groß genug ist, einzelne Sektorpositionen zu streuen. Niedrige Active Share und hoher Tracking Error sind konzentrierte sektorartige Wetten bei relativ passiver Aktienauswahl.
- Rund die Hälfte der Active Share wird gegen andere Publikumsfonds aufgebaut. Weichen durchschnittliche und aggregierte Active Share voneinander ab, handeln die Fonds untereinander. Ein Portfolio aus Fonds kann die gesamte Active Share deshalb senken und stellt die übliche Core-Satellite-Sicht infrage.
- Die wertgewichtete durchschnittliche Active Share fiel über die Stichprobe von 80 Prozent in den 1980ern auf 60 Prozent.
- Active Share ist hoch persistent: Hohe Active Share in diesem Jahr bleibt im nächsten Jahr und darüber hinaus wahrscheinlich hoch. Der ideale Fonds verbindet hohe Active Share mit hoher vergangener Performance.
- Fonds mit sehr hoher Active Share und guter vergangener Performance haben deutlich höheres künftiges Alpha als solche mit hoher Active Share und schlechter vergangener Performance. Diese Lücke ist in den Gruppen mit hoher Active Share viel größer als in denen mit niedriger. Es gibt danach eine Gruppe von Managern mit anhaltendem Stock-Picking-Können.
- Bei Aktien, die auf 3 Prozent real bewertet sind, soll mit dem passiven Investieren auch der Core-Satellite-Ansatz verschwinden.
- Breite Mandate erhöhen die Gelegenheiten, eine Erkenntnis anzuwenden, und gelten als voraussichtlich optimal.
- Dieselbe Strategie in vielen Märkten anzuwenden kann sehr profitabel sein und ist dennoch nicht Diversifikation.
- LTCM beruhte praktisch durchgängig auf Konvergenz, ob bei US-Treasuries oder dänischen Mortgage-Backed Securities, und wiederholte die Strategien immer wieder. Geografische Diversifikation war erreicht, strategische nicht.
- Manager, die 800 US-Aktien nach Buch zu Preis reihen, Billige kaufen und Teure verkaufen und einmal je Quartal neu gewichten, wenden nur eine Erkenntnis an. Die Breite ist nicht 800, weil die Sichten nicht unabhängig sind, aber sie ist größer als vier, die Zahl der Neugewichtungen pro Jahr.
- Core-Satellite-Strukturen und der Schub der Pensionsberater haben das Verschwinden der Balanced Funds beschleunigt, die strategische und taktische Allokation kombinierten. Diese Fonds hätten einen Teil der Rückkopplung der Blasen mildern können.
- Statt endlos vieler Spezialisten mit je einer Gebühr wäre ein Manager mit einer Gebühr und der Freiheit vorzuziehen, überall dort anzulegen, wo die Gelegenheit liegt.

## Funktionsweise

- Hierarchical Risk Parity arbeitet in drei Stufen: Baum-Clustering, Quasi-Diagonalisierung und rekursive Bisektion.
- Hierarchical Risk Parity konvergiert günstigstenfalls in deterministischer logarithmischer Zeit und schlechtestenfalls in deterministischer linearer Zeit.
- RiskMetrics bildet den VaR zweier Positionen als Wurzel aus VaR1 zum Quadrat plus VaR2 zum Quadrat plus 2 mal ρ12 mal VaR1 mal VaR2, wobei ρ12 der Kreuzkorrelationskoeffizient der beiden Renditen ist.
- Für m Instrumente ist der Gesamt-VaR die Wurzel aus der Summe der quadrierten Einzel-VaR plus der Summe 2 mal ρij mal VaRi mal VaRj über alle Paare i < j.

## Voraussetzungen

- Die Formel für den gemeinsamen VaR setzt voraus, dass die Logrenditen der beteiligten Anlagen gemeinsam multivariat normalverteilt sind mit Mittelwert null und Kovarianzmatrix Σ t+1.

## Anwendung im Trading

- Eine praktische Anwendung ist die Allokation über mehrere Machine-Learning-Strategien.
- Seit Bridgewater in den 1990er-Jahren Risk Parity einführte, folgen große Asset Manager dem Ansatz mit zusammen über 500 Milliarden Dollar.
- Wegen ihres hohen Hebels sollten diese Fonds von einer stabileren Risk-Parity-Allokation profitieren, mit besserer risikoadjustierter Rendite und geringeren Rebalancing-Kosten.

## Regeln und Kriterien

- Die Gruppengrenzen von Cremers und Petajisto: konzentrierte Stockpicker Active Share über 80 Prozent und Tracking Error über 8 Prozent; diversifizierte Stockpicker Active Share über 80 Prozent und Tracking Error unter 8 Prozent; Sektorwetten Active Share unter 80 Prozent und Tracking Error über 6 Prozent; Closet Indexer Active Share unter 60 Prozent und Tracking Error unter 6 Prozent. Indexfonds haben effektiv Active Share null und sehr niedrigen Tracking Error.

## Risiken und Grenzen

- Korrelationsmatrizen behandeln jede Anlage als Ersatz für jede andere und lassen Gewichte deshalb frei in unbeabsichtigte Richtungen laufen.
- Im Zahlenbeispiel konzentriert CLA 92,66 Prozent auf die fünf größten Positionen, Hierarchical Risk Parity nur 62,57 Prozent.
- Die Standardabweichungen liegen dabei nahe beieinander, 0,4640 gegen 0,4486, CLA streicht aber einen großen Teil des Universums für eine kleine Risikoreduktion.
- Das CLA-Portfolio ist trügerisch diversifiziert, weil Stress in den fünf größten Positionen stärker durchschlägt als bei Hierarchical Risk Parity.
- Das Inverse-Varianz-Portfolio verteilt die Gewichte gleichmäßig, ignoriert die Korrelationsstruktur und ist dadurch anfällig für systemische Schocks.
- Das Alpha eines Russell-1000-Managers auf das Beta des S&P 500 zu setzen, kann wegen der Überlappung zweier Large-Cap-Inlandindizes zugleich long und short dieselbe Aktie ergeben. Die Short-Kosten sind dann vollständig verschwendet.
- Auch ein unkorreliert wirkendes japanisches Aktien-Alpha auf einem S&P-500-Beta erzeugt dasselbe Problem, sobald das Portfolio bereits japanisches Beta hält.
- Bei einem großen diversifizierten Portfolio ist das Risiko proportional zur Wurzel der Korrelation. Steigt die maßgebliche Korrelation von der mittleren Aufwärts-Halbekorrelation 0,21 auf die Abwärtskorrelation 0,38, ist der VaR mit dem Faktor 1,35 zu multiplizieren; der Diversifikationsnutzen schrumpft im Abschwung.

## Beispiele

- Eine angegebene Mischung ist etwa 70 Prozent long und 30 Prozent short und wird auf dieses Verhältnis zurückgeführt, sobald die Shorts 25 oder 35 Prozent erreichen.
- Aktien lassen sich nach Liquidität, Größe, Branche und Region gruppieren, und innerhalb einer Gruppe konkurrieren sie um die Allokation.
- Die Outperformance von Hierarchical Risk Parity außer Stichprobe wird bei größerem Universum, mehr Schocks, stärkerer Korrelation oder Rebalancing-Kosten noch deutlicher.
- Das mit SPY gehandelte Aktienportfolio umfasst etwa 98 Titel; müssen wenige wegen der Short-Sale-Beschränkung entfernt werden, bleibt die Wirkung begrenzt.
- Eine Variante des Buy-on-Gap kauft mehr Aktien, begrenzt aber die Zahl der Titel innerhalb desselben Sektors.
- Der Fortune-Korb von zehn Aktien für das Jahrzehnt 2000, von dem nur eine ein KGV unter dem 50-Fachen hatte, lag zum Zeitpunkt des Textes noch rund 40 Prozent unter dem vorgeschlagenen Kauf und ist für Montier ein Beispiel dauerhaften Kapitalverlusts, nicht ein Beleg für Konzentration als Selbstzweck.
- Startet der Manager mit 100 Millionen Dollar im S&P 500, verkauft die Hälfte und legt die 50 Millionen Dollar in die Aktien, die er mag, entsteht eine Active Share von 50 Prozent. Hält er nur 50 von 500 Aktien, liegt die Active Share bei 90 Prozent, also 10 Prozent Überlappung mit dem Index.
- Der Fidelity Magellan wanderte von hoher Active Share zu einem Closet-Index-Fonds. Die Managerfolge Lynch, Smith, Vinik und Stansky zeigt, dass der Manager die Active Share trägt.
- Benchmark ist der Index mit der niedrigsten Active Share, also der höchsten Überlappung, unter S&P 500, Barra-Value- und Growth-Indizes, Russell 2000 und Wiltshire 5000. Die Datenbasis sind inländische reine US-Aktienfonds seit 1980.

## Unterschiedliche Quellenpositionen

- Kolanovic und Koautoren (2017) finden Hierarchical-Risk-Parity-Portfolios wirklich diversifiziert, mit mehr unkorrelierten Exposures und weniger extremen Gewichten und Risikoallokationen.
- Raffinot (2017) findet Portfolios aus hierarchischem Clustering robust, wirklich diversifiziert und risikoadjustiert statistisch besser als gängige Optimierungsverfahren.
- Keynes schreibt, Safety-first als kleines Spiel in vielen Firmen, über die man kein gutes Urteil habe, statt eines substanziellen Einsatzes dort, wo die Information ausreiche, sei eine Travestie der Anlagepolitik.
- Graham argumentiert, eine Anlage könne in einer Gruppe von Papieren gerechtfertigt sein, die einzeln nicht sicher genug wäre, sodass Diversifikation nötig sein kann, um das Risiko der einzelnen Papiere auf das mit den Anforderungen der Anlage noch vereinbare Minimum zu senken.
- Graham hält Diversifikation für einen integralen Teil aller Standardoperationen der Stammaktienanlage.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Markets in Profile_ Profiting from the Auction Process.pdf, S. 1–20 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-001-p001-p020|S. 1–20]]
- Markets in Profile_ Profiting from the Auction Process.pdf, S. 214–225 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-016-p214-p225|S. 214–225]]
- Advances in Financial Machine Learning.pdf, S. 248–267 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-014-p248-p267|S. 248–267]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 99–118 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-008-p099-p118|S. 99–118]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 163–165 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-012-p163-p165|S. 163–165]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 199–214 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-015-p199-p214|S. 199–214]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 324–343 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-018-p324-p343|S. 324–343]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 343–362 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-019-p343-p362|S. 343–362]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 495–514 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-027-p495-p514|S. 495–514]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 514–533 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-028-p514-p533|S. 514–533]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 248–267 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-014-p248-p267|S. 248–267]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 267–286 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-015-p267-p286|S. 267–286]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 286–305 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-016-p286-p305|S. 286–305]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 305–324 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-017-p305-p324|S. 305–324]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 400–419 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-022-p400-p419|S. 400–419]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 419–438 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-023-p419-p438|S. 419–438]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 438–457 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-024-p438-p457|S. 438–457]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 457–476 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-025-p457-p476|S. 457–476]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 609–628 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-033-p609-p628|S. 609–628]]

## Verwandte Themen

- Hedging
- Rebalancing
