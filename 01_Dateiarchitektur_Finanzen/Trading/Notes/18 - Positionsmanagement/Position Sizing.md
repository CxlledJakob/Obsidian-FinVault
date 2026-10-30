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

## Voraussetzungen


## Anwendung im Trading

- Ein Backtest ist unter anderem eine Plausibilitätsprüfung der Einsatzgröße.

## Regeln und Kriterien


## Risiken und Grenzen


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

## Verwandte Themen
