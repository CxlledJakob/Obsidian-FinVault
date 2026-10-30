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
aktualisiert: 2026-10-30
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

## Risiken und Grenzen

- Log-Preis-Spreads verlangen ständiges Rebalancing, um die Kapitalgewichte konstant zu halten; Preis-Spreads sind einfacher, beide sind aber theoretisch gerechtfertigt, wenn Preise und Logpreise kointegrieren.
- Eigenvektoren mit zugleich langen und kurzen Aktien verhindern ein nur longes Aktienportfolio, das mit kurzem SPY gehedgt ist: kurze Aktien und kurzes SPY wären bei einzelnen Titeln doppelt short und erhöhen das spezifische Risiko.

## Beispiele

- Für EWA, EWC und IGE wird der erste Eigenvektor verwendet; die Halbwertszeit dieses gehedgten Portfolios beträgt 23 Tage.
- Für GLD und USO arbeitet der Preis-Spread mit adaptiver Hedge Ratio deutlich besser als das Verhältnis.
- Bei δ gleich 0,0001 schwankt die Kalman-Steigung zwischen EWC und EWA um 1, und im weiteren Code tritt diese Steigung an die Stelle der Hedge Ratio.
- EUR.GBP ist selbst ein Verhältnis, weil es EUR.USD geteilt durch GBP.USD entspricht.

## Unterschiedliche Quellenpositionen


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

## Verwandte Themen

- Diversifikation
