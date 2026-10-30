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
aktualisiert: 2026-10-30
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

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 153–172 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-009-p153-p172|S. 153–172]]
- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]

## Verwandte Themen
