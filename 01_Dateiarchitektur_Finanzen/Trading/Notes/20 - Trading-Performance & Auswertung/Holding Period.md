---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/20 - Trading-Performance & Auswertung/20 - Trading-Performance & Auswertung|20 - Trading-Performance & Auswertung]]"
weitere_hauptthemen: []
unterthema: "Trade-Auswertung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Holding Period


## Kurzdefinition

- Jede Wette hat eine Haltedauer vom Zeitpunkt ihrer Entstehung bis zu dem Zeitpunkt t1, an dem die erste Barriere berührt wird.
- Die durchschnittliche Haltedauer ist die mittlere Zahl der Tage, über die eine Wette gehalten wird.

## Kernaussagen

- Hochfrequente Strategien können eine Position nur Bruchteile von Sekunden halten, niederfrequente Strategien über Monate oder Jahre.
- Kurze Haltedauern können die Kapazität der Strategie begrenzen.
- Die Haltedauer hängt mit der Wettfrequenz zusammen und ist von ihr verschieden.
- Eine Strategie kann einmal im Monat wetten, etwa zur Veröffentlichung der Nonfarm Payrolls, und jede Wette nur wenige Minuten halten.
- Die Strategien dieses Kapitels halten Positionen über mehrere Tage und heißen deshalb Interday-Momentum-Strategien; die Intraday-Strategien höherer Frequenz folgen im nächsten Kapitel.
- Viele Interday-Momentum-Strategien leiden unter einer neu entdeckten Schwäche, von der Intraday-Momentum-Strategien weniger betroffen sind.
- Als Lookback und Haltedauer wird das Paar aus vergangener und künftiger Periode gewählt, das die höchste positive Korrelation liefert.
- Aus Handelssicht ist eine möglichst kurze Haltedauer vorzuziehen, weil kurze Haltedauern die besten Sharpe Ratios erzeugen.
- Die Vorlage von Moskowitz, Yao und Pedersen 2012 kauft bei positiver und verkauft bei negativer 12-Monats-Rendite und hält die Position einen Monat; hier wird statt monatlich täglich entschieden, und jeden Tag wird nur ein Fünfundzwanzigstel des Kapitals eingesetzt.
- Für TU werden Lookback 250 und Haltedauer 25 gewählt, weil dieses Renditepaar einen Korrelationskoeffizienten von 0,27 bei einem p-Wert von 0,02 hat.
- Tägliches Rebalancing macht die Handelssignale einer Momentum-Strategie nicht unabhängiger, wenn Lookback und Haltedauer lang sind.
- Die Dauer, über die Momentum in Kraft bleibt, wird immer kürzer, je mehr Händler es aufgreifen; das betrifft vor allem das kürzerfristige nachrichtengetriebene Momentum des nächsten Kapitels.
- Von Gewinnmeldungen getriebenes Preismomentum dauerte früher mehrere Tage und hält inzwischen kaum bis zum Börsenschluss.
- Wird Preismomentum als langsame Diffusion von Information verstanden, enden Diffusion und Momentum früher, sobald mehr Händler die Information schneller und früher lernen.
- Der Momentum-Händler muss die Haltedauer deshalb womöglich ständig verkürzen, und es gibt dafür keinen vorhersagbaren Zeitplan.
- Der zeitbasierte Ausstieg legt eine Haltedauer fest und schließt die Position, wenn diese Haltedauer erreicht ist.
- Alle bisher besprochenen Momentum-Strategien verwenden nur solche zeitbasierten Ausstiege.
- Die Schulter-Kopf-Schulter-Signale auf den echten Aktienkursen verlieren im Schnitt etwa 0,25 Prozent über eine Haltedauer von 10 Tagen.
- Dieselbe Haltedauer von 10 Tagen ergibt bei den Mustern in den Pseudo-Aktiendaten einen durchschnittlichen Verlust von 0,03 Prozent.
- Für nicht überlappende Renditepaare verlangt der Text, bei längerem Lookback um die Haltedauer vorzurücken und bei längerer Haltedauer um den Lookback.
- Der abgedruckte Code schreitet dagegen um den Lookback vor, wenn der Lookback mindestens so groß wie die Haltedauer ist, und sonst um die Haltedauer.
- Die besten Kompromisspaare für TU sind (60, 10), (60, 25), (250, 10), (250, 25), (250, 60) und (250, 120); aus Handelssicht wird darunter die kürzestmögliche Haltedauer bevorzugt, weil sie die besten Sharpe Ratios erzeugt.
- Beim Vorzeichentest sind die besten Paare (60, 10), (250, 10) und (250, 25).
- Die Arbitrage, die die Rollrendite über den Basiswert extrahiert, hat voraussichtlich kürzere Haltedauer und geringeres Risiko als Buy-and-Hold, weil der verrauschte Spot nicht über lange Zeit ausgemittelt werden muss.
- Die VX-ES-Rollrendite-Strategie von Simon und Campasano hält die Position einen Tag.
- Tägliches Rebalancing macht die Signale eines Momentum-Portfolios nicht unabhängiger, wenn Lookback und Haltedauer lang sind; wenige unabhängige Signale senken die Sharpe Ratio.
- Die querschnittliche Momentum-Strategie auf dem S&P-500-Universum hält 25 Tage, das lineare Mean-Reversion-Modell auf demselben Universum weniger als einen Tag.
- Faktoren außer möglicherweise der Hauptkomponente ändern sich langsam, deshalb werden die Haltedauern so lang wie bei den querschnittlichen Modellen dieses Abschnitts.
- Die Dauer, über die kürzerfristiges nachrichtengetriebenes Momentum wirkt, wird immer kürzer, je mehr Händler es aufgreifen.
- Wird Momentum als langsame Diffusion von Information verstanden, endet es früher, wenn mehr Händler die Information schneller und früher lernen.
- Die Haltedauer muss deshalb womöglich ständig verkürzt werden, und es gibt dafür keinen vorhersagbaren Zeitplan.
- Die Auflösung des Pairs-Geschäfts schon bei Rückkehr des Spreads auf den Mittelwert verkürzt die Haltedauer des Portfolios und kann zugleich mehr Transaktionen und höhere Handelskosten erzeugen.
- Die durchschnittliche Haltedauer einer Aktie an der New York Stock Exchange beträgt 11 Monate.
- Über diese 11 Monate ist die Rendite nur eine Funktion von Preisänderungen und hat mit innerem Wert oder diskontiertem Cashflow nichts zu tun; Montier nennt das Spekulation.
- Weil viele Anleger Rauschen mit Nachrichten verwechseln und einander überlisten wollen, enden sie bei sehr kurzen Zeithorizonten und handeln infolgedessen zu viel.
- Analysten verwenden in der Bewertung meist nur ein oder zwei Jahre als Input, obwohl eine Aktie theoretisch ein langfristiger Anspruch auf Assets ist.
- Diese Kurzfristigkeit passt zur Schrumpfung der Haltedauern; die Analysten bedienen damit die Nachfrage ihrer Kunden.
- Wer mit Dividenden-Diskontmodell oder Total Return bewertet, nutzt eher fünf Jahre und mehr. Das beliebteste Maß, das KGV auf künftigen Gewinnen, bleibt bei ein bis zwei Jahren.
- Die durchschnittliche Aktienhaltedauer der untersuchten Value-Fonds liegt über 5 Jahren, das Maximum bei 17 Jahren und das kürzeste bei 3 Jahren.
- Nach Morningstar hält die Mutual-Fund-Branche eine Aktie im Schnitt nur ein Jahr; bei diesem Horizont wird Investieren nach Montier zur Spekulation.
- In den 1950er und 1960er Jahren lag die durchschnittliche Haltedauer an der NYSE bei 7 bis 8 Jahren; heute sind es 11 Monate.
- Die durchschnittliche Umschlagrate der zehn Fonds in Tabelle 23.2 beträgt 17,6 Prozent.
- Die niedrigste Umschlagrate in der Tabelle hat Tweedy Browne Global Value mit 6 Prozent, die höchste Mutual Beacon mit 35 Prozent.
- Munger und Buffett: Ist der Kauf einer Stammaktie richtig gemacht, ist die Zeit zum Verkauf fast nie.
- Long-only-Manager sind nach den Morningstar-Daten und den Daten von John Bogle am Schrumpfen der Haltedauer ebenso beteiligt wie Hedgefonds.
- Die untersuchten Value-Investoren hatten eine durchschnittliche Haltedauer von 5 Jahren, die durchschnittliche Haltedauer einer Aktie an der New York Stock Exchange beträgt nur 11 Monate.
- Keynes: Moderne Anleger konzentrieren sich zu sehr auf jährliche, vierteljährliche oder sogar monatliche Bewertungen dessen, was sie halten, und auf Kursgewinne und zu wenig auf die laufende Rendite und den inneren Wert.
- Keynes hielt es für ein nützliches Heilmittel, den Kauf einer Anlage dauerhaft zu machen wie eine Ehe, außer aus Tod oder einem anderen schweren Grund, damit nur die langfristigen Aussichten zählen.
- Graham: Unterbewertungen aus Vernachlässigung oder Vorurteil können unangenehm lange bestehen, und dasselbe gilt für überhöhte Preise.
- Je häufiger ein Portfolio geprüft wird, desto wahrscheinlicher wird ein Verlust gesehen.
- In einem konstruierten Universum, in dem alle Manager 3 Prozent Alpha und 6 Prozent Tracking Error haben und 50 Jahre laufen, zeigten rund 70 Prozent drei oder mehr Jahre Underperformance in Folge.
- Goyal und Wahal (2005): Eingestellte Manager hatten in den drei Jahren vor der Einstellung fast 14 Prozent Outperformance und danach insignifikante Renditen; wegen Performance Entlassene hatten davor rund 6 Prozent underperformed und in den drei Jahren danach fast 5 Prozent outperformt.
- Montier nennt das eine Lektion, die Zeithorizonte zu verlängern und die Risiken des Investierens dem Endkunden besser zu erklären.
- Die durchschnittliche Haltedauer einer Aktie an der NYSE lag in den 1950ern und 1960ern bei 7 bis 8 Jahren und liegt heute bei 9 Monaten. Die Abbildung zeigt Bogle-Daten und NYSE-Daten.
- Die durchschnittliche Haltedauer eines Publikumsfonds fiel von 16 Jahren in den 1950ern auf 4 Jahre.
- Eine Gruppe vorbildlicher Value-Investoren hielt im Schnitt 5 Jahre, der durchschnittliche US-Publikumsfonds nur 1 Jahr.
- Die billigsten 20 % des MSCI Europe haben seit 1991 im ersten Jahr rund 3 % Outperformance erzeugt; bei weiterem Halten steigt sie im Schnitt auf 32 % über fünf Jahre.
- Bei den teuersten 20 % nach dem Kurs-Gewinn-Verhältnis fällt der Anteil der Titel mit Outperformance von 38 % im ersten Jahr auf 34 % nach fünf Jahren, und die Renditen werden mit der Zeit schlechter.
- Im Value-Portfolio liefert nur etwa die Hälfte der Titel die Outperformance im ersten Jahr, nach fünf Jahren fast 60 %.
- Die Haltedauer sinkt seit Jahrzehnten. Leichtere Information und immer kürzere Performancemessung werden als Gründe genannt; der Hedgefonds-Boom ist jünger und wird als Erklärung oft überschätzt, kann am Rand aber weitere Kurzfristspieler erzeugen und Long-only-Manager in denselben Wettbewerb ziehen.
- Performancemessung innerhalb des Tages, die nicht an der normalen Varianz der gehaltenen Aktien skaliert ist, misst Rauschen.
- Die Portfolios werden jeden Monat gebildet und dann über verschiedene Zeithorizonte laufen gelassen; überlappende Stichproben ändern die Ergebnisse nicht wesentlich.
- Langfristig outperformanceende Value-Manager hielten im Schnitt fünf Jahre, Aktien an der NYSE elf Monate und der durchschnittliche US-Publikumsfonds etwas über ein Jahr.
- Die Value-Überschussrendite der billigsten 20 Prozent des MSCI Europe nach trailing PE liegt nach zwölf Monaten bei rund 3 Prozent, nach zwei Jahren kumuliert bei 5,7 Prozent und in den Jahren 3 bis 5 bei 8 bis 10 Prozent p.a.
- Die Value-Trefferquote steigt von 50 Prozent auf Einjahressicht auf 57 Prozent bei fünf Jahren, aber nicht massiv.
- Im Growth-Portfolio sinkt der Anteil der Titel mit Marktrendite über dem Index, je länger der Horizont wird, weil das Risiko eines Earnings-Torpedos zunimmt.
- Die Sektor-Tests sortieren jährlich in Tritiles und verfolgen das höchste und das niedrigste Tritile ein Jahr, dann wird der Vorgang wiederholt.
- John Bogle (2005) stellt fest, dass die durchschnittliche Haltedauer von Anlegern in US-Publikumsfonds von mehr als 10 Jahren in den 1950ern auf rund 4 Jahre gefallen ist.
- Die durchschnittliche Haltedauer einer Aktie an der NYSE lag Mitte der 1950er bei 7 bis 8 Jahren und liegt heute bei nur 11 Monaten.
- Der Rückgang ist nicht bloß die Folge des Aufstiegs der Hedgefonds. Bogles Reihe zur Haltedauer professioneller Anleger aus einer ganz anderen Quelle folgt eng dem Verlauf der NYSE-Reihe.
- So kurze Haltedauern haben nichts mit Investment zu tun. Sie sind reine Spekulation.
- Keynes hält es für ein mögliches Heilmittel der Übel moderner Anlagemärkte, den Kauf dauerhaft und unauflöslich zu machen, wie eine Ehe, außer bei Tod oder einem anderen schwerwiegenden Grund, weil der Anleger dann nur noch die langfristigen Aussichten bedenken müsste.
- Die Information Ratio hat eine Darstellung in der Zeit: Aus der Volatilität der Überschussrenditen folgt, wie lange gehalten werden muss, bis eine Strategie mit hoher Wahrscheinlichkeit die Überschussrendite zeigt.
- US-Aktien gegenüber Cash haben eine Information Ratio von 0,37. Das entspricht 14 Jahren Haltedauer, bis Kunden zu 90 Prozent sicher eine Überschussrendite über Cash sehen.
- Die Cheap-Country-Strategie braucht auf Basis der Ex-ante-Information-Ratio eine Haltedauer von sechs Jahren. Das taktische Allokationsmodell braucht sieben Jahre, um zu 90 Prozent sicher die Benchmark zu schlagen.
- Die Langfristrendite enthält die Bewertungsänderung während der Haltedauer, neben Dividendenrendite und realem Dividendenwachstum. Die bewertungsabhängigen Realrenditen sind über zehn Jahre gemessen.
- Quartalsweise Leistungsmessung bleibt bei diesen Horizonten Unsinn.
- Bei Dasgupta et al. (2006) beträgt der Renditeunterschied zwischen den am stärksten verkauften und den am stärksten gekauften institutionellen Aktien über zwei Jahre 17 Prozent und über ein Jahr rund 9 Prozent.
- Die sentimentabhängigen Überschussrenditen gegenüber Cash sind auf die nächsten zwölf Monate gerechnet: rund 13 Prozent bei sehr niedrigem Sentiment und 1,7 Prozent bei sehr hohem.
- Baker und Wurgler (2006) sortieren die Renditen der nächsten zwölf Monate nach Sentiment und nach Merkmalen wie Größe, Alter, Renditevarianz, Profitabilität und Dividende.
- Die Information Ratio übersetzt Strategie-Risiko in eine Haltedauer: US-Aktien gegenüber Cash brauchen 14 Jahre für 90 Prozent Sicherheit, billige Länder sechs Jahre und das taktische Modell sieben Jahre, jeweils auf Ex-ante-Basis für die beiden letzten.

## Funktionsweise

- Eine Wette gilt zu einem Zeitpunkt loc als aktiv, wenn sie vor oder bei loc eröffnet wurde und loc vor ihrem Endzeitpunkt liegt oder das Ende noch unbekannt ist.
- Die Prognose zur Barriere i impliziert einen prognostizierten Preis zum Ende der Haltedauer, und im Intervall bis zu diesem Ende schwankt der Marktpreis, während weitere Prognosen entstehen können.
- Der Schätzer bildet die mittlere Haltedauer in Tagen über die Einstiegszeitpunkte.
- Wird eine bestehende Position vergrößert, wird die Einstiegszeit mit der Positionsgröße neu gewichtet.
- Wird die Position verkleinert, geht die seit dem Einstieg verstrichene Zeit mit dem geschlossenen Umfang in den Durchschnitt ein.
- Beim Drehen der Position wird die Haltedauer der alten Seite mit deren absolutem Umfang festgehalten, und die Einstiegszeit wird neu gesetzt.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Die Halbwertszeit der Mean Reversion sagt, welche Haltedauer zu erwarten ist und welcher Lookback zu verwenden ist.
- Bei einer Halbwertszeit von 20 Tagen soll für eine Mean-Reversion-Strategie kein Lookback von 5 Tagen für gleitenden Durchschnitt oder Standardabweichung verwendet werden.
- Den Lookback auf ein kleines Vielfaches der Halbwertszeit zu setzen, liegt oft nahe am Optimum.
- Im Devisenhandel bedeutet Overnight, eine Position bis oder über 17:00 Uhr ET zu halten.
- Ist man ein Paar B.Q über Nacht long, beträgt die Zinsdifferenz iB minus iQ; ist der Zins der Quotierungswährung höher als der der Basiswährung, ist dieser Rollover-Zins ein Sollzins.
- Wegen der Abwicklung an T plus 2 wird der Rollover mit eins plus der Zahl der geschlossenen Tage multipliziert, wenn die Position den 17:00-Uhr-ET-Schluss an Tag T übersteht und Tag T plus 3 für eine der beiden Währungen ein Wochenende oder Feiertag ist; wer am Mittwoch über 17:00 Uhr ET hält, hat den dreifachen Tagessatz, weil Samstag und Sonntag geschlossen sind.
- Bei USD.CAD und USD.MXN liegt die Abwicklung an T plus 1, sodass der Rollover nur dann mit den geschlossenen Tagen multipliziert wird, wenn Tag T plus 2 ein Wochenende oder Feiertag ist; den dreifachen Tagessatz gibt es damit, wenn die Position den Donnerstag über 17:00 Uhr ET hinaus gehalten wird.
- Beim CL-Kalender-Spread beträgt die Haltedauer eines Kontraktpaars 3 Monate, also 61 Handelstage.
- 10 Tage vor Verfall des aktuellen Near-Kontrakts wird auf das nächste Kontraktpaar gerollt, und die Verfälle von Near und Far liegen 1 Jahr auseinander.
- Bei reinen Intraday-Positionen sind die Finanzierungskosten null.
- Die Strategie niedriger gegen hoher Trailing-Kurs-Gewinn-Verhältnisse am MSCI World von 1980 bis 2005 wird mit einjähriger Haltedauer und jährlichem Rebalancing gemessen: die Dezile entstehen zu Jahresbeginn, die Performance über die folgenden zwölf Monate.

## Risiken und Grenzen

- Ist die Halbwertszeit sehr lang, lassen sich in einem gegebenen Zeitraum nur wenige Round-Trips abschließen, und die Strategie ist wenig profitabel.
- Bei kurzfristigen Strategien wie dem AUD-CAD-Beispiel mit ungleichem Hedge ist die Wirkung der Rollover-Zinsen meist nicht groß; Overnight-Strategien müssen sie in den Backtest nehmen.
- Lange Lookbacks und Haltedauern ergeben wenige unabhängige Signale und damit eine niedrigere Sharpe Ratio.

## Beispiele

- Für USD.CAD ergibt die Regression eine Halbwertszeit von etwa 115 Tagen.
- In Tabelle 6.2 betragen die Haltedauern 10 Tage für BR, 40 Tage für HG und 25 Tage für TU.
- Die VX-ES-Rollrendite-Strategie hält die Position einen Tag.
- Die vereinfachte querschnittliche Rohstoffstrategie hält den besten und den schlechtesten Future 25 Handelstage, entsprechend einem Monat.
- Die Arbitrage gegen den Basiswert oder einen Proxy hat voraussichtlich eine kürzere Haltedauer als das Buy-and-Hold des Futures, weil dort lange gehalten werden muss, bis die laute Spot-Rendite sich herausmittelt.
- Faktoren außer möglicherweise der Hauptkomponentenanalyse ändern langsam, deshalb sind die Haltedauern beim Rang nach Faktoren so lang wie bei den querschnittlichen Modellen dieses Abschnitts.
- Das PRESSURE-Portfolio wird vierteljährlich angepasst, weil Holdings-Daten in der Regel nur vierteljährlich vorliegen.
- Das lineare Mean-Reversion-Modell für S&P-500-Aktien hält weniger als einen Tag, die gegenläufige querschnittliche Momentum-Strategie 25 Tage.
- Die übrigen Umschlagraten in Tabelle 23.2 sind Clipper 13 Prozent, FPA Capital 26 Prozent, First Eagle Global 12 Prozent, Oak Value 29 Prozent, Oakmark Select 16 Prozent, Longleaf Partners 17 Prozent, Legg Mason Value 13 Prozent und Tweedy Browne American Value 9 Prozent.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 153–172 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-009-p153-p172|S. 153–172]]
- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 153–172 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-009-p153-p172|S. 153–172]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 144–163 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-011-p144-p163|S. 144–163]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 163–165 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-012-p163-p165|S. 163–165]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 457–476 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-025-p457-p476|S. 457–476]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 476–495 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-026-p476-p495|S. 476–495]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 115–134 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-007-p115-p134|S. 115–134]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 134–153 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-008-p134-p153|S. 134–153]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 191–210 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-011-p191-p210|S. 191–210]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 210–229 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-012-p210-p229|S. 210–229]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 248–267 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-014-p248-p267|S. 248–267]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 267–286 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-015-p267-p286|S. 267–286]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 286–305 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-016-p286-p305|S. 286–305]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 305–324 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-017-p305-p324|S. 305–324]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 343–362 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-019-p343-p362|S. 343–362]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 381–400 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-021-p381-p400|S. 381–400]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 400–419 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-022-p400-p419|S. 400–419]]

## Verwandte Themen
