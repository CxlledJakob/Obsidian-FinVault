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
aktualisiert: 2026-11-01
---

# Hedging


## Kurzdefinition


## Kernaussagen

- Die Gewinne trendfolgender Spekulanten lassen sich ökonomisch damit rechtfertigen, dass ihre Tätigkeit kommerziellen Hedgern eine Dienstleistung bietet: die Übertragung des Preisrisikos vom Hedger auf den Spekulanten.
- Die Profitabilität technischer Trendfolgesysteme in Rohstoff-Futures lässt sich als Kompensation, also als Risikoprämie, dafür erklären, dass sie kommerziellen Hedgern den Dienst der Risikoübertragung leisten.
- Die ökonomische Theorie sagt voraus, dass Futures-Märkte genug profitable Trends zeigen sollten, um Trendfolger zu motivieren, die Preisrisiken zu übernehmen, die Hedger abgeben wollen.
- Die ökonomische Funktion der Futures-Märkte hat nichts mit Kapitalaufnahme zu tun und alles mit Preisrisiko. Preisänderungen, besonders große, sind Risiko für Betriebe, die Rohstoffe erzeugen oder verbrauchen.
- Die Futures-Märkte geben diesen Betrieben, den Commercial Hedgern, ein Mittel, Preisrisiko auf Anleger, die Spekulanten, zu übertragen.
- Die Risikotransfer-Prämie für Rohstoff- und Währungs-Hedges entschädigt Spekulanten, die Long- und Short-Positionen in Futures übernehmen, damit kommerzielle Nutzer und Produzenten das Preisänderungsrisiko abgeben können. Die Entschädigung sind profitable Trends, die mit relativ einfachen Trendfolge-Strategien erfasst werden.
- Hedger könnten auch untereinander kontrahieren, der Weizenfarmer mit der Bäckerei. Oft ist der Hedge-Bedarf aber unausgeglichen, manchmal liegt mehr Verkaufsbedarf der Farmer vor als Kaufbedarf der Nutzer, manchmal umgekehrt.
- Diese Lücke zwischen Angebot und Nachfrage braucht eine dritte Gruppe, die zu kaufen oder zu verkaufen bereit ist.
- Die CFTC erfasst Kauf und Verkauf der Commercial Hedger. In steigenden Preistrends übersteigt der Hedge-Verkauf den Hedge-Kauf, die Hedger sind netto Verkäufer. In fallenden Trends übersteigt der Hedge-Kauf den Hedge-Verkauf, die Hedger sind netto Käufer.
- Verkaufte und gekaufte Menge müssen gleich sein. Im steigenden Trend braucht der überschießende Hedge-Verkauf zusätzliche Käufer, im fallenden Trend der überschießende Hedge-Kauf zusätzliche Verkäufer.
- Die Futures-Märkte brauchen Spekulanten, die Trendfolger sind. Die unsichtbare Hand des Marktes erzeugt die Trends, die sie dafür entschädigen, dass sie diese Lücke schließen.
- Trendfolger sind erheblichen Risiken ausgesetzt. Die meisten Trendfolge-Systeme erzeugen in 50 bis 65 Prozent der Fälle unprofitable Signale. Das geschieht in trendlosen Märkten, und das ist die Mehrheit der Zeit.
- In Drawdowns ist es für erfolgreiche Trendfolger nicht ungewöhnlich, bis zu 30 Prozent ihres Handelskapitals zu verlieren. Das Motiv, dieses Risiko zu tragen, ist die Gelegenheit, nicht die Garantie, an Trends zu verdienen, wenn sie auftreten.
- Großräumige Trends bieten eine Gewinngelegenheit für Trendfolger, die ausreichend kapitalisiert sind und den Hebel richtig steuern.
- Ist die Risikotransfer-Prämie eine gültige Erklärung der Trendfolge-Renditen, sollte Trendfolge in Aktien nicht so lohnend sein wie an den Rohstoff-Futures, weil ein Aktien-Trendfolger keine Risikotransfer-Leistung erbringt. Es gibt Daten, die nahelegen, dass Trendfolge in Aktien tatsächlich weniger lohnend ist.
- Aktien- und Anleihemärkte beschaffen Unternehmen Eigen- und Fremdkapital. Weil Aktien und Unternehmensanleihen Risiken über den risikofreien Satz der Staatspapiere hinaus tragen, werden Anleger mit der Aktienrisikoprämie und der Unternehmensanleihe-Risikoprämie entschädigt.
- Die Hedge Ratio eines Assets ist die Zahl der Einheiten, die im Portfolio long oder short gehalten werden. Bei einer Aktie ist das die Aktienzahl, und eine negative Hedge Ratio bedeutet eine Short-Position.
- Die passenden Hedge Ratios sind vor dem Test nicht bekannt, und nicht jede Linearkombination kointegrierender Reihen bildet ein stationäres Portfolio.
- Engle und Granger (1987) schätzen die Hedge Ratio zuerst per linearer Regression zweier Preisreihen und prüfen danach die Stationarität des Portfolios. Die Funktion cadf bündelt diese Schritte.
- Die CADF-Hedge-Ratio ist reihenfolgeabhängig und beim Tausch von abhängiger und unabhängiger Variable nicht der genaue Kehrwert. Oft führt nur eine der beiden Ordnungen zu einem stationären Portfolio; gewählt wird die Ordnung mit der negativsten t-Statistik.
- Die Eigenvektoren des Johansen-Tests dienen als Hedge Ratios und sind nach fallenden Eigenwerten geordnet. Der erste Eigenvektor hat die kürzeste Halbwertszeit, und der Test hängt nicht von der Reihenfolge der Preisreihen ab.
- Für EWA, EWC und IGE lautet der erste Eigenvektor minus 1,0460, 0,7600 und 0,2233. Er bestimmt die Stückzahlen des stationären Portfolios.
- Von den Johansen-Eigenvektoren bildet derjenige mit dem größten Eigenwert das stationäre Portfolio mit der kürzesten Halbwertszeit. Er bestimmt die Stückzahlen je ETF.
- Der Nettomarktwert yport ist die Summe aus Stückzahl mal Preis über alle ETFs und ersetzt in der Halbwertszeitregression die Einzelpreisreihe.
- Im Preisspread y = h1 y1 + … + hn yn sind die Hedge Ratios die Stückzahlen. Für zwei Reihen wird y = y1 minus h y2 geschrieben, damit h bei der üblichen Long-short-Kombination positiv ist.
- Für ein wirklich kointegrierendes Paar genügen OLS oder der Johansen-Eigenvektor auf möglichst langer Historie. Für reale Reihen, die das Ideal verfehlen, wird die Hedge Ratio dynamisch geschätzt.
- Ein kurzes gleitendes Fenster ändert die Hedge Ratio sprunghaft, sobald der älteste Bar heraus- und der neueste hineinfällt. Der Kalman-Filter liefert eine dynamische Hedge Ratio ohne willkürlichen Gewichts-Cutoff.
- Im GLD-USO-Beispiel wird die Hedge Ratio täglich per OLS über 20 Handelstage neu geschätzt. Der erste Johansen-Eigenvektor wäre eine Alternative. Der Spread ist minus Hedge-Ratio mal GLD plus USO.
- Bei Logpreisen sind die h Kapitalgewichte, nicht Stückzahlen. Die Ratio y1/y2 ist nur stationär, wenn die Hedge Ratios gleichen Betrag haben, nach Normierung also minus 1. Das ist nicht der Normalfall.
- Für nicht wirklich kointegrierte Paare braucht der Spread oft eine laufend neue Hedge Ratio; die Ratio als Signal erspart das. Im GLD-USO-Vergleich ist der adaptive Preisspread der Ratio dennoch deutlich überlegen.
- EUR.GBP ist selbst eine Ratio, nämlich EUR.USD geteilt durch GBP.USD. Für ein nicht fertig notiertes Kreuz wie MXN.NOK kann die Ratio wirksamer sein als der Spread, auch wenn USD.NOK und USD.MXN gehandelt werden müssen. Deren P&L fällt in NOK und in MXN an, der direkte MXN.NOK-P&L nur in NOK; die Wege sind nicht identisch.
- Im Kalman-Filter auf EWC gegen EWA ist die Steigung die dynamische Hedge Ratio und schwankt bei δ gleich 0,0001 um 1. Im anschließenden Handel ersetzt diese Steigung die Hedge Ratio des Bollinger-Codes.
- Der Crack Spread ist long drei Kontrakte CL, short zwei Kontrakte RB und short einen Kontrakt HO.
- Die 3:2:1-Ratios folgen daraus, dass drei Barrel CL ungefähr zwei Barrel Benzin und ein Barrel Heizöl ergeben; das gilt nicht für alle Raffinerien.
- Die NYMEX bietet für den Crack Spread einen fertigen Korb mit deutlich niedrigerer Margin, als wenn die Kontrakte getrennt gehandelt werden.
- Ein ADF-Test vom 20. Mai 2002 bis zum 4. Mai 2012 zeigt, dass dieser Crack Spread nicht mean-reverting ist.
- Damit die Hedge Ratio das Verhältnis der Kontraktzahlen trifft, werden die VX-Preise mit 1.000 und die ES-Preise mit 50 multipliziert, weil ein Punkt VX 1.000 Dollar und ein Punkt ES 50 Dollar entspricht.
- Aus der Regression folgt ein Portfolio, das long 0,3906 Kontrakte VX und long einen Kontrakt ES stationär sein soll.

## Funktionsweise

- Der Eigenvektor des Johansen-Tests bestimmt die Stücke jedes ETF im stationären Portfolio und dient damit als Hedge Ratio.
- Der Eigenvektor zum größten Eigenwert hat die kürzeste Halbwertszeit und wird für das stationäre Portfolio gewählt.
- Der Nettomarktwert ist die Summe aus Stückzahl mal Kurs über alle ETFs.
- Der Preis des Einheitsportfolios ist y gleich h1 y1 plus h2 y2 bis hn yn, mit Hedge Ratios aus der linearen Regression oder aus den Johansen-Eigenvektoren; hi ist die Stückzahl.
- Für zwei Aktien wird der Spread als y gleich y1 minus h mal y2 geschrieben, damit h in der üblichen Long-short-Kombination positiv ist.
- Kointegrieren die Logpreise, sind die hi Kapitalgewichte und nicht Stückzahlen, und im Portfolio ist implizit Kasse enthalten, weil sich der Marktwert bei konstanten Gewichten sonst nicht ändern könnte.
- Für ein wirklich kointegrierendes Paar wird die Hedge Ratio einmal aus möglichst langer Historie mit OLS oder mit dem Johansen-Test geschätzt.
- Für reale, nicht ideal kointegrierte Reihen wird die Hedge Ratio über ein gleitendes Fenster neu geschätzt, im GLD-USO-Beispiel täglich mit OLS über 20 Handelstage, ersatzweise mit dem ersten Johansen-Eigenvektor.
- Die hier beschriebene Kalman-Filter-Anwendung auf eine einzelne mean-reverting Preisreihe sucht nicht die Hedge Ratio zwischen zwei kointegrierenden Preisreihen.
- Keynes und Hicks argumentierten, dass die Besitzer physischer Ware, die Hedger wie Farmer oder Ölproduzenten, sich durch Short-Futures absichern und auf diesen Hedges Verlust erwarten, während die Spekulanten netto long sind und für dieses Risiko entschädigt werden müssen.
- Spekulanten kaufen deshalb nur Futures mit positiver Roll-Rendite, gleichbedeutend mit Futures, die billiger sind als der erwartete künftige Spot; das ist die normale Backwardation.
- Die Merkregel lautet, Backwardation mit normal zu verbinden, und normal heißt, der Future-Preis liegt stets unter dem Spot.
- Das Argument ist nicht vollständig richtig: Rohöl, eine völlig normale Ware, ist über verschiedene Zeiträume in Contango.
- Der Crack Spread ist long drei Kontrakte CL, short zwei Kontrakte RB und short einen Kontrakt HO.
- Die Hedge-Ratios 3:2:1 entstehen, weil drei Barrel CL ungefähr zwei Barrel RB und ein Barrel Heizöl ergeben; das gilt nicht für alle Raffinerien.
- Der Name Crack Spread kommt daher, dass Benzin und Heizöl durch das Cracken der langen Kohlenwasserstoffketten von Rohöl entstehen.
- NYMEX bietet für den Crack Spread einen fertigen Korb mit deutlich niedrigerer Margin, als wenn die Kontrakte einzeln gehandelt werden.
- Ein Punkt Bewegung in VX entspricht 1.000 Dollar, ein Punkt Bewegung in ES entspricht 50 Dollar.
- Damit die Hedge Ratio das Verhältnis der Kontraktzahlen trifft, werden die VX-Preise mit 1.000 und die ES-Preise mit 50 multipliziert.
- Die lineare Beziehung lautet ES mal 50 gleich minus 0,3906 mal VX mal 1.000 plus 77.150 Dollar, wobei ES und VX die jeweiligen Futures-Settlement-Preise sind.
- Ein Portfolio, das 0,3906 Kontrakte VX long und einen Kontrakt ES long hält, soll stationär sein.

## Voraussetzungen


## Anwendung im Trading

- Ein langfristiger Hedge bleibt im Ziel langfristig, doch ein Teil davon wird gehandelt, wenn der Day-Timeframe eine Gelegenheit gibt.
- Eine gehedgte Variante des Gap-Modells ist long Aktien und short Aktienindex-Futures.
- Nach bestätigter Kointegration wird ein long-short-stationäres Portfolio aus den ausgewählten Aktien und SPY gebildet; der Johansen-Eigenvektor mit dem größten Eigenwert, die erste Spalte der Eigenmatrix, bestimmt die Gewichte.
- Weil der Johansen-Test auf Logpreisen lief, sind die Hedge Ratios eine Dollar-Kapitalallokation und keine Stückzahl; das Gewicht jeder einzelnen Aktie ist gleich, unterscheidet sich aber vom Gewicht von SPY.
- Das lineare Long-Short-Modell ist fast vollkommen dollarneutral, und einzelne Aktien dienen an manchen Tagen nur als Hedges, sodass Gewinne nur über alle Aktien aggregiert entstehen.
- Beim SPY-Beispiel bestimmt der Johansen-Eigenvektor die Gewichte von SPY gegen das Aktienportfolio. Weil der Test auf Log-Preisen lief, sind die Hedge Ratios Dollarkapital und nicht Stückzahlen.
- Das Gewicht jeder einzelnen Aktie ist wegen der gleichen Kapitalzuteilung dasselbe, es unterscheidet sich aber vom Gewicht auf SPY.
- Es gibt zwei kointegrierende Relationen. Genommen wird die mit dem größten Eigenwert, die erste Spalte der Eigenmatrix.
- Ein Test auf allen 500 Aktien plus SPY scheitert daran, dass die bekannte Johansen-Implementierung höchstens 12 Symbole nimmt und die Eigenvektoren gewöhnlich Long- und Short-Aktien mischen.
- Long- und Short-Aktien im Korb verhindern einen sauberen Hedge aus Long-only-Aktien gegen Short-SPY oder umgekehrt. Short-Aktien zusammen mit Short-SPY sind bei einzelnen Titeln doppelt short und erhöhen das spezifische Risiko.
- Als Ausweg werden die Hedge Ratios der vorausgewählten Aktien per genetischem Algorithmus oder Simulated Annealing so bestimmt, dass der durchschnittliche absolute Abstand der Aktienreihe zur SPY-Reihe minimal wird und alle Hedge Ratios positiv bleiben.
- Das lineare Long-Short-Modell ist nahezu perfekt dollarneutral und setzt jeden Tag dasselbe Bruttokapital von 1 Dollar ein.

## Regeln und Kriterien

- Hedges werden gesetzt, wenn ein Titel zu hoch steht.
- Bei Übernahmen, Fusionen und Abspaltungen, nachdem der Preis zu tief getrieben wurde, werden diese Hedges abgebaut.
- Genannte Formen sind mehr Cash, defensive Titel, der Verkauf von Optionen auf Indizes oder Einzeltitel und der Kauf von Index-Puts auf den Gesamtmarkt, auf Branchen oder Sektoren.
- Steigt der Preis, wird der Hedge gegen das Inventar schrittweise durch den Verkauf von Futures aufgebaut.
- Öffnet der Markt weit über der Value des Vortags und zeigt die frühe Struktur Schwäche, wird der Hedge an diesem höheren Open vergrößert.
- Auktioniert der Preis im Tagesverlauf tiefer, kann ein Teil der Shorts geschlossen und später zu höheren Preisen wieder aufgesetzt werden.
- Das Verhältnis y1/y2 ist nur im Sonderfall h1 gleich minus h2 stationär; normalerweise sind die Hedge Ratios nicht betragsgleich und nach Normierung nicht gleich minus 1.
- Ist das Paar nicht wirklich kointegriert, erspart das Verhältnis als Signal die fortlaufend angepasste Hedge Ratio.
- Ein gleitendes Fenster ändert die Hedge Ratio abrupt, wenn der älteste Bar herausfällt und der neueste hinzukommt; der Kalman-Filter aktualisiert die Hedge Ratio ohne willkürlichen Gewichtsschnitt.
- Im Kalman-Filter ist β ein Vektor aus Achsenabschnitt und Steigung, und die beobachtende Reihe wird um eine Spalte aus Einsen erweitert, damit der Spread einen von null verschiedenen Mittelwert haben darf.
- Für ein Mean-Reversion-Portfolio mit fester Stückzahl während der Trade-Dauer werden die Hedge Ratios aus der Preisreihe bestimmt.
- Für ein Mean-Reversion-Portfolio mit festen Marktwerten je Bestandteil während der Trade-Dauer werden die Hedge Ratios aus der Log-Preisreihe bestimmt.
- Können Hedge Ratio, Mittel und Standardabweichung eines Spreads künftig variieren, werden ein gleitender Look-back oder der Kalman-Filter verwendet.
- Eine Alternative minimiert nach dem Einzeltest gegen SPY per genetischem Algorithmus oder Simulated Annealing die mittlere absolute Differenz zwischen Aktienportfolio und SPY-Preisreihe; alle Hedge Ratios müssen positiv sein, und MATLABs Global Optimization Toolbox stellt beide Verfahren bereit.
- Der Johansen-Test liefert die Hedge Ratio des Kapitals zwischen AUD.USD und CAD.USD; ist diese Ratio nicht eins, kann das Paar nicht als ein Cross AUD.CAD gehandelt werden.
- Damit der Eigenvektor Kapitalgewichte ist, müssen beide Preisreihen dieselbe Quotierungswährung haben, sonst haben Punktbewegungen nicht denselben Wert und der Johansen-Test ist bedeutungslos.
- Soll ein mean-revertierendes Portfolio während des Trades eine feste Stückzahl halten, werden die Hedge Ratios aus den Preisreihen bestimmt.
- Sollen die Marktwerte der Bestandteile während des Trades fest bleiben, werden die Hedge Ratios aus den Log-Preisreihen bestimmt.
- Können Hedge Ratio, Mittel und Standardabweichung eines Spreads künftig variieren, helfen ein gleitender Lookback oder der Kalman-Filter.
- Der Johansen-Eigenvektor ist nur als Kapitalgewichte lesbar, wenn beide Reihen dieselbe Kurswährung haben. Sonst hat eine Punktbewegung nicht denselben Wert, und der Test ist bedeutungslos. Deshalb werden AUD.USD und CAD.USD verwendet.
- Die Hedge Ratio ist hier nicht eins, das Paar ist also kein fertiger Kreuzkurs AUD.CAD. Live wird der Kauf einer Einheit CAD.USD zum Verkauf von 1/y Einheiten USD.CAD.
- Ein Kalenderspread ist long einen Future und short einen anderen auf denselben Basiswert mit anderer Fälligkeit. Bei gleichen Marktwerten ist der Spread die Differenz der Log-Preise, und sein Log-Marktwert ist γ mal (T1 − T2).

## Risiken und Grenzen

- Log-Preis-Spreads verlangen ständiges Rebalancing, um die Kapitalgewichte konstant zu halten; Preis-Spreads sind einfacher, beide sind aber theoretisch gerechtfertigt, wenn Preise und Logpreise kointegrieren.
- Eigenvektoren mit zugleich langen und kurzen Aktien verhindern ein nur longes Aktienportfolio, das mit kurzem SPY gehedgt ist: kurze Aktien und kurzes SPY wären bei einzelnen Titeln doppelt short und erhöhen das spezifische Risiko.

## Beispiele

- Für EWA, EWC und IGE wird der erste Eigenvektor verwendet; die Halbwertszeit dieses gehedgten Portfolios beträgt 23 Tage.
- Für GLD und USO arbeitet der Preis-Spread mit adaptiver Hedge Ratio deutlich besser als das Verhältnis.
- Bei δ gleich 0,0001 schwankt die Kalman-Steigung zwischen EWC und EWA um 1, und im weiteren Code tritt diese Steigung an die Stelle der Hedge Ratio.
- EUR.GBP ist selbst ein Verhältnis, weil es EUR.USD geteilt durch GBP.USD entspricht.

## Unterschiedliche Quellenpositionen

- Nach Keynes und Hicks shorten die Besitzer der physischen Ware, die Hedger, Futures und erwarten, auf dem Hedge zu verlieren. Die Spekulanten sind netto long und kaufen nur Futures mit positiver Rollrendite, also mit einem Preis unter dem erwarteten künftigen Spot. Das ist die normale Backwardation.
- Die Eselsbrücke lautet, Backwardation gehöre zu normal, und normal heiße, der Future liege immer unter dem Spot. Das ist nicht vollständig richtig: Rohöl, eine normale Ware, liegt über verschiedene Zeiträume in Contango.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Markets in Profile_ Profiting from the Auction Process.pdf, S. 214–225 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-016-p214-p225|S. 214–225]]
- Mind Over Markets_ Power Trading with Market Generated Information, Updated Edition.pdf, S. 53–72 → [[Trading/Pilot/blocks/mind-over-markets/mind-over-markets-block-005-p053-p072|S. 53–72]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 1–20 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-001-p001-p020|S. 1–20]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 324–343 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-018-p324-p343|S. 324–343]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 362–381 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-020-p362-p381|S. 362–381]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 52–71 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-004-p052-p071|S. 52–71]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 71–75 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-005-p071-p075|S. 71–75]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 76–95 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-006-p076-p095|S. 76–95]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 95–98 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-007-p095-p098|S. 95–98]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 99–118 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-008-p099-p118|S. 99–118]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 119–138 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-009-p119-p138|S. 119–138]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 138–143 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-010-p138-p143|S. 138–143]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 324–343 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-018-p324-p343|S. 324–343]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 495–514 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-027-p495-p514|S. 495–514]]

## Verwandte Themen

- Diversifikation
