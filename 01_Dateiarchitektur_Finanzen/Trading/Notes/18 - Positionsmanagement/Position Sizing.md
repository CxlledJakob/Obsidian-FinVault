---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/18 - Positionsmanagement/18 - Positionsmanagement|18 - Positionsmanagement]]"
weitere_hauptthemen: []
unterthema: "Positionsgröße"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Position Sizing


## Kurzdefinition

- Die Bet Size mi,t einer Strategie i zum Zeitpunkt t liegt in [−1, 1]; −1 ist eine volle Short-Position und 1 eine volle Long-Position.
- Die Zielposition zu Prognose fi ist der ganzzahlige Wert von m[ω, fi − pt] mal Q, wobei Q die maximale absolute Positionsgröße und pt der Marktpreis ist.

## Kernaussagen

- Ein ML-Algorithmus kann eine hohe Accuracy erreichen, und doch verliert die Strategie zwangsläufig Geld, wenn die Einsätze nicht richtig bemessen werden.
- Bet Sizing hat eine enge Parallele zu Texas Hold’em, und einige der besten Portfoliomanager, mit denen der Autor gearbeitet hat, sind eher starke Pokerspieler als Schachspieler.
- Positionen sollen so bemessen werden, dass Kasse bleibt für den Fall, dass das Handelssignal erst stärker wird, bevor es schwächer wird.
- Je stärker das Signal, desto kleiner die Wahrscheinlichkeit, dass es noch stärker wird, und desto größer die Bet Size.
- Sagt eine ML-Strategie einen Kauf mit hoher Wahrscheinlichkeit voraus, wird eine große Long-Position eingegangen, als Funktion der Konfidenz der Strategie.
- Im sample-gewichteten Cross-Entropy-Loss steht die vorhergesagte Wahrscheinlichkeit für die Positionsgröße.
- Die Kelly-Formel bestimmt die optimale Kapitalallokation und den optimalen Hebel und wägt Renditen gegen Risiken ab.
- Unterhebeln ist immer besser als Überhebeln, besonders wenn fremdes Geld verwaltet wird.
- Der optimale Hebel wird für Fälle gesucht, in denen die Renditen nicht mehr als gaußverteilt gelten können.
- Schwarze Schwäne, Constant Proportion Portfolio Insurance und Stop-Losses mildern die praktische Anwendung dieser Allokation.
- Risikoindikatoren werden daraufhin geprüft, ob sie ein nützlicher Teil eines umfassenden Risikomanagements sind.

## Funktionsweise

- Ein strategieunabhängiger Weg bildet ct als Zahl der gleichzeitigen Long-Wetten minus Zahl der gleichzeitigen Short-Wetten.
- Diese Bet-Concurrency wird je Seite analog zur Label-Concurrency aus Kapitel 4 über überlappende Zeitspannen bestimmt.
- Auf die Reihe {ct} wird eine Mischung zweier Normalverteilungen angepasst, etwa nach dem Verfahren von López de Prado und Foreman 2014.
- Die Bet Size ist (F[ct] − F[0]) / (1 − F[0]), wenn ct mindestens 0 ist, und (F[ct] − F[0]) / F[0], wenn ct negativ ist; F ist die Verteilungsfunktion der angepassten Mischung.
- Ein zweiter Weg folgt einem Budget: Die Bet Size ist die Zahl gleichzeitiger Long-Wetten geteilt durch ihr Maximum minus die Zahl gleichzeitiger Short-Wetten geteilt durch ihr Maximum.
- Das Ziel dieses Budgets ist, dass die Maximalposition nicht erreicht wird, bevor das letzte gleichzeitige Signal ausgelöst wurde.
- Ein dritter Weg ist Meta-Labeling: Ein Klassifikator wie SVC oder Random Forest bestimmt die Wahrscheinlichkeit einer Fehlklassifikation, und daraus wird die Bet Size abgeleitet.
- Der Algorithmus, der die Bet Size entscheidet, ist vom Primärmodell unabhängig und kann Merkmale aufnehmen, die Fehlalarme vorhersagen.
- Die vorhergesagte Wahrscheinlichkeit lässt sich bei diesem Weg unmittelbar in eine Bet Size übersetzen.
- Für zwei Ausgänge x in {−1, 1} wird die Nullhypothese p[x = 1] = 1/2 geprüft; die Prüfgröße z = (p[x = 1] − 1/2) / √(p[x = 1](1 − p[x = 1])) ist standardnormal, und die Bet Size ist m = 2Z[z] − 1 in [−1, 1].
- Dieselbe Prüfgröße lässt sich als (2p[x = 1] − 1) / (2 √(p[x = 1](1 − p[x = 1]))) schreiben.
- Bei mehr als zwei Ausgängen wird One-versus-Rest verwendet; die Labels sind die zugehörigen Bet Sizes, und für jedes Label wird eine Wahrscheinlichkeit geschätzt, die sich zu 1 summieren.
- Mit p̃ als größter dieser Wahrscheinlichkeiten wird die Nullhypothese p̃ = 1/‖X‖ geprüft; z = (p̃ − 1/‖X‖) / √(p̃(1 − p̃)) liegt in [0, +∞), und die Bet Size ist m = x (2Z[z] − 1) in [−1, 1].
- Z[z] regelt dabei die Größe der Prognose x, und die Seite steckt in x.
- Die Unsicherheit ist absolut, wenn alle Ausgänge gleich wahrscheinlich sind.
- Snippet 10.1 übersetzt Wahrscheinlichkeiten in ein Signal, mittelt gleichzeitig offene Wetten und diskretisiert den Wert; stammt die Prognose aus einem Meta-Labeling, wird zusätzlich mit der Seite multipliziert.
- Eine alte Wette durch eine neu eintreffende zu ersetzen, führt leicht zu übermäßigem Turnover.
- Sinnvoller ist, zu jedem Zeitpunkt die Größen aller noch aktiven Wetten zu mitteln.
- Aktiv ist eine Wette, wenn sie vor oder bei dem Zeitpunkt eröffnet wurde und der Zeitpunkt vor ihrem Ende liegt oder das Ende noch unbekannt ist; gibt es keine aktive Wette, ist das Signal 0.
- Auch nach der Mittelung würden kleine Prognoseänderungen unnötige Mini-Trades auslösen, deshalb wird die Bet Size diskretisiert als m* = round(m/d) · d mit d in (0, 1].
- Nach der Diskretisierung werden Werte über 1 auf 1 gedeckelt und Werte unter −1 auf −1 gesetzt.
- Die Triple-Barrier-Prognose zum Bar i impliziert einen prognostizierten Preis, der zu den Barrieren passt, und bis zum Ausgang können weitere Prognosen für denselben Endpreis entstehen.
- Die Sigmoid-Bet-Size ist m[ω, x] = x / √(ω + x²), wobei x = fi − pt die Abweichung zwischen Prognose und Marktpreis ist und ω die Breite der Sigmoidfunktion steuert.
- Für eine reelle Preisabweichung x gilt −1 < m[ω, x] < 1, und die ganzzahlige Zielposition ist durch −Q < Zielposition < Q begrenzt.
- Die Zielposition lässt sich dynamisch anpassen, während sich pt ändert; geht pt gegen fi, geht die Zielposition gegen 0, weil der Algorithmus die Gewinne realisieren will.
- Daraus folgt ein Break-even-Limitpreis für die Ordergröße Zielposition minus aktueller Position, damit keine Verluste realisiert werden.
- Dieser Limitpreis ist der Durchschnitt der inversen Preise über die ganzzahligen Positionsstufen zwischen aktueller Position und Zielposition.
- Die Inverse von m bezüglich des Preises ist L[fi, ω, m] = fi − m · √(ω / (1 − m²)).
- Der Text sagt, der Fall m² = 1 müsse nicht behandelt werden, weil der Betrag der Zielposition kleiner als 1 sei.
- Weil diese Funktion monoton ist, kann der Algorithmus keine Verluste realisieren, während pt gegen fi läuft.
- Zu einem vorgegebenen Paar aus Preisabweichung x und gewünschter Bet Size m* kalibriert man ω als x² mal (m* hoch −2 minus 1).
- Als Alternative zur Sigmoidfunktion kann die Potenzfunktion Vorzeichen von x mal Betrag von x hoch ω dienen, mit ω mindestens 0 und x in [−1, 1], sodass das Ergebnis in [−1, 1] liegt.
- Diese Alternative erreicht an den Rändern −1 und 1 die Bet Sizes −1 und 1, die Krümmung lässt sich direkt über ω steuern, und für ω > 1 wechselt sie von konkav zu konvex und ist um den Wendepunkt nahezu flach.
- Die Herleitung der Gleichungen für die Potenzfunktion bleibt eine Übung.
- Um Overtrading zu vermeiden, wird die Bet Size als round(m/d) · d diskretisiert, wobei d in (0, 1] den Grad der Diskretisierung bestimmt.
- Nach der Rundung werden Werte über 1 auf 1 und Werte unter −1 auf −1 gesetzt.
- Die lineare Strategie hält eine Stückzahl, die negativ proportional zum Z-Score ist, also zu Preis minus gleitendem Durchschnitt, geteilt durch die gleitende Standardabweichung.
- Bei USD.X ist der Marktwert einer Einheit der Kurs selbst, deshalb ist der Portfoliomarktwert gleich dem negativen Z-Score.
- Beim Portfolio werden Vielfache des Einheitsportfolios proportional zum negativen Z-Score seines Preises gehalten; die Stücke des Einheitsportfolios setzt der Johansen-Eigenvektor.
- Die Zahl der Einheiten des Einheitsportfolios ist der negative Z-Score seines Preises; linear bezieht sich auf diese Stückzahl, nicht auf eine Proportionalität des Anlage-Marktwerts.
- Die Dollarposition jedes ETF ist das Produkt aus diesem Vielfachen, den Eigenvektor-Stücken und dem Kurs.
- Die ausgewiesene Rendite teilt die P&L durch den Bruttomarktwert, die Summe der absoluten Positionsmarktwerte.
- Die lineare Strategie setzt die Stückzahl proportional zur Abweichung vom Mittel und hat deshalb keine bekannte Obergrenze der Kapitalbindung.
- Die Bollinger-Strategie hält zu jedem Zeitpunkt null oder eine Einheit und macht die Kapitalzuteilung dadurch einfach.
- Scaling-in erhöht das investierte Kapital, je weiter der Preis vom Mittel abweicht, weil der mögliche Gewinn aus der Rückkehr mitwächst.
- Beim Verhältnis erhalten Long- und Short-Seite dasselbe Dollarkapital.
- Beim Log-Preis-Portfolio werden die Kapitalgewichte konstant gehalten, und die Differenz zur Marktwertänderung sitzt in der Kasse.
- Bei der Fractional-Position-Regel ist die Positionsgröße proportional zum Nettoanteil der einfachen Regeln, die long oder short sind: Zahl long minus Zahl short, geteilt durch die Gesamtzahl der Regeln.
- Im On-Balance-Volume-Beispiel von Hsu und Kuan mit 2.040 Regeln, davon 1.158 short und 882 long, wird eine Short-Position von 0,135 Einheiten gehalten, weil (882 minus 1.158) geteilt durch 2.040 gleich −0,135 ist.
- Beim Voting wird unabhängig davon, wie groß die Mehrheit ist, nur eine Position von einer Einheit in Richtung dieser Mehrheit genommen.
- Ein Diffusionsindikator auf Basis der Fractional Position hält eine anteilige Long- oder Short-Position und passt sie an, wenn sich der Nettoanteil von long zu short ändert.
- Eine gewichtete lineare Kombination weist jeder einfachen Regel einen Koeffizienten ai zu, der von ihrer Vorhersagekraft abhängt.
- Der Satz der Gewichte, der nach einem Gütemaß wie minimalem Prognosefehler oder maximaler finanzieller Leistung am besten ist, wird durch Optimierung gesucht.
- Die einfachste lineare Kombination gibt jedem Bestandteil dasselbe Gewicht; zwei binäre Umkehrregeln ergeben dann −2, wenn beide short sind, 0, wenn eine short und eine long ist, und +2, wenn beide long sind.

## Voraussetzungen


## Anwendung im Trading

- Ein Backtest ist unter anderem eine Plausibilitätsprüfung der Einsatzgröße.

## Regeln und Kriterien

- In der Modellrechnung reicht die Kaufkraft für genau zwei Kontrakte, egal ob sie bei L1, bei L2 oder erst bei F eingesetzt werden.
- All-in setzt beide Kontrakte auf einem einzigen Niveau, average-in einen Kontrakt bei L1 und den zweiten nur, wenn L2 erreicht wird.
- Buy-on-Gap kauft höchstens 10 Aktien, im Code topN gleich 10; ist die gefilterte Liste kürzer, wird sie ganz gekauft, und die Rendite des Backtests wird durch topN geteilt.
- Im SPY-Beispiel erhält jede kointegrierende Aktie gleiches Kapital; der Johansen-Eigenvektor auf Logpreisen setzt die Dollar-Allokation zwischen diesem Portfolio und SPY, nicht die Stückzahl.
- Die lineare Mean-Reversion-Strategie setzt die Zahl der Einheiten auf den negativen Abstand des Log-Marktwerts von seinem gleitenden Mittel, geteilt durch die gleitende Standardabweichung, bei Look-back 5.
- Im querschnittlichen Modell ist wi gleich minus (ri minus der Durchschnittsrendite) geteilt durch die Summe der absoluten Abweichungen, sodass jeden Tag dasselbe Bruttokapital von 1 Dollar investiert wird.

## Risiken und Grenzen

- Weil kein Maximum des Portfoliomarktwerts gesetzt wird, kann für die ausgewiesene P&L unbegrenzt Kapital nötig sein.
- Der Autor empfiehlt die unbegrenzte lineare Positionsgröße nicht als praktische Handelsstrategie.
- Das Höchstkapital ist im Voraus unbekannt, und infinitesimale Stückzahlen bei infinitesimalen Preisbewegungen sind nicht handelbar.
- Nach einer ungebrochenen Erfolgsserie wird die Strategie oft mit maximalem Leverage gehandelt, und der dann seltene Verlust kann katastrophal sein.
- Unter konstantem p ist keine Staffelung die erwartungsgemäß profitabelste Größe; entweder beide Kontrakte bei L1 oder beide bei L2 sind besser.
- Bei großen Größen senken Scaling-in und Scaling-out die Marktauswirkung von Ein- und Ausstieg.
- Ist die Volatilität nicht konstant, kann die Staffelung außer Stichprobe eine bessere realisierte Sharpe Ratio liefern.
- Buy-on-Gap handelt je Tag recht wenige Aktien und hat deshalb keine große Kapazität.
- Ein Backtest auf Trade- oder Quote-Preisen ist nur realistisch, wenn nur 100 Stück gehandelt werden oder erhebliche Transaktionskosten angesetzt sind; die NBBO-Größe von AAPL ist oft nur 100 Stück, die von EWC an einem typischen Tag etwa 5.000.
- Werden nach dem Signal nicht beide Seiten als Market Order geschickt, bleiben bei Teilausführung kleiner Orderbruchteile zeitweise kleine ungehedgte Positionen.

## Beispiele

- Zwei Strategien auf demselben Instrument prognostizierten beide richtig, der Preis stieg von 1 über 0,5 auf 1,25 und damit um 25 %; die Einsatzfolge 0,5, 1, 0 verdiente 0,5, die Folge 1, 0,5, 0 verlor 0,125, weil sie die volle Anfangsposition verkleinern musste, als der Markt dagegen lief.
- Die Bet Size kann zum Beispiel 0,9 betragen, wenn die Wahrscheinlichkeit, ein noch stärkeres Signal zu beobachten, nur 0,1 ist.
- Abbildung 10.2 zeigt die Diskretisierung der Bet Size für d = 0,2.
- Abbildung 10.2 zeigt die Diskretisierung für d = 0,2.
- Im Beispiel wird die Sigmoidfunktion so kalibriert, dass sie bei einer Preisabweichung von 10 die Bet Size 0,95 liefert.
- Bei einer Maximalposition von 100, einem Prognosepreis von 115 und einem Marktpreis von 100 hat die Order die Größe 97, und ihr Limitpreis 112,3657 liegt zwischen Marktpreis und Prognosepreis.
- Setzt man den Prognosepreis auf 110, beträgt die Zielposition 95, im Einklang mit der Kalibrierung von ω.
- Abbildung 10.3 zeigt die Potenzfunktion Vorzeichen von x mal Betrag von x zum Quadrat, die von konkav zu konvex wechselt, und die Sigmoidfunktion x / √(0,1 + x²), die von konvex zu konkav wechselt.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 153–172 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-009-p153-p172|S. 153–172]]
- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]

## Verwandte Themen
