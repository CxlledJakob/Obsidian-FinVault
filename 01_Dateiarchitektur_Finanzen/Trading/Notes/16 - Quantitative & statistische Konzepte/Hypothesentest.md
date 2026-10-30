---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Statistik"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Hypothesentest


## Kurzdefinition


## Kernaussagen

- Ein ADF-Test auf dem Verhältnis Back zu Front von VX zeigt, dass dieses Verhältnis mit 99 Prozent Wahrscheinlichkeit stationär ist.
- Ein ADF-Test auf dem Crack Spread vom 20. Mai 2002 bis zum 4. Mai 2012 zeigt, dass dieser Spread nicht mean-reverting ist.
- Ein ADF-Test auf CL und BZ im Verhältnis 1:1 zeigt, dass der Spread weit von stationär entfernt ist.
- Eine lineare Regression oder ein Johansen-Test auf einer Mischung der Regime 2004 bis Mai 2008 und August 2008 bis 2012 wäre ein Fehler.
- Dass manchmal Urteil nötig ist, macht quantitative Regeln nicht nutzlos.
- Kahneman schreibt, Experten seien Algorithmen in jedem Bereich mit erheblicher Unsicherheit oder Unvorhersagbarkeit einheitlich unterlegen, von den Siegern von Fußballspielen bis zur Lebenserwartung von Krebspatienten.
- Der Text hofft, dass der Finanzmarkt keine Ausnahme von dieser Regel ist.

## Funktionsweise

- Auf einem endlichen Backtest wird eine Teststatistik berechnet. Im Beispiel ist das die durchschnittliche Tagesrendite der Strategie in dieser Periode.
- Die Nullhypothese unterstellt, die wahre durchschnittliche Tagesrendite auf einem unendlichen Datensatz sei null.
- Die Wahrscheinlichkeitsverteilung der Tagesrenditen wird als bekannt unterstellt und hat unter der Null den Mittelwert null.
- Der p-Wert ist die Wahrscheinlichkeit, dass die durchschnittlichen Tagesrenditen mindestens so groß sind wie der beobachtete Backtest-Wert. Bei einer allgemeinen Teststatistik ist es die Wahrscheinlichkeit eines mindestens so extremen Wertes, einschließlich eines negativen.
- Ist der p-Wert sehr klein, zum Beispiel kleiner als 0,01, wird die Nullhypothese verworfen, und die gebacktestete durchschnittliche Tagesrendite gilt als statistisch signifikant.
- Der gedankenintensivste Schritt ist die Bestimmung der Verteilung unter der Null.
- Erster Weg: Die Tagesrenditen folgen einer Gauß-Verteilung mit Mittelwert null und der Stichproben-Standardabweichung der Tagesrenditen. Die Standard-Teststatistik ist der Mittelwert geteilt durch die Standardabweichung, multipliziert mit der Wurzel der Zahl der Datenpunkte, nach Berntson 2002.
- Zweiter Weg: Monte Carlo erzeugt viele simulierte Preisreihen mit denselben ersten Momenten und derselben Länge wie die echten Daten. Der Anteil p, in dem die durchschnittliche Strategierendite mindestens die Backtest-Rendite erreicht, soll klein sein. Sonst kann die Rendite allein an den Marktrenditen liegen. Die Annahme ist, dass die Strategie subtile Muster oder Korrelationen nutzt und nicht nur die ersten Momente der Preisverteilung.
- Dritter Weg nach Lo, Mamaysky und Wang 2000: Es werden Mengen simulierter Trades erzeugt, mit derselben Zahl langer und kurzer Einstiege und derselben durchschnittlichen Haltedauer wie im Backtest, zufällig über die tatsächliche historische Preisreihe verteilt. Gemessen wird der Anteil der Mengen, deren durchschnittliche Rendite mindestens die Backtest-Rendite erreicht.
- Die drei Wege können verschiedene Antworten geben, weil die Verteilung jeweils anders ist und jede angenommene Verteilung die Strategie gegen einen anderen Zufallsmaßstab stellt.
- Der ADF-Test prüft, ob die Null λ gleich 0 verworfen werden kann; wird sie verworfen, hängt die nächste Änderung Δy(t) vom aktuellen Niveau y(t−1) ab, und die Reihe ist kein Random Walk.
- Die Teststatistik ist der Regressionskoeffizient λ, mit y(t−1) als unabhängiger und Δy(t) als abhängiger Variable, geteilt durch den Standardfehler des Fits, also λ/SE(λ).
- Dickey und Fuller haben die Verteilung dieser Statistik tabelliert, sodass sich für einen Wert von λ/SE(λ) ablesen lässt, ob die Null etwa auf dem 95-Prozent-Niveau verworfen wird.
- Weil Mean Reversion erwartet wird, muss λ/SE(λ) negativ und negativer als der kritische Wert sein.
- Die kritischen Werte hängen vom Stichprobenumfang ab und davon, ob ein von null verschiedener Mittelwert minus μ/λ oder ein stetiger Drift minus βt/λ angenommen wird.
- Zeitreihenmomentum lässt sich über den Korrelationskoeffizienten der Renditen und seinen p-Wert prüfen; der p-Wert ist die Wahrscheinlichkeit der Nullhypothese keiner Korrelation.
- Dafür muss eine konkrete Zeitverzögerung gewählt werden.
- Alternativ wird die Korrelation der Vorzeichen vergangener und künftiger Renditen getestet, wenn nur die Richtung und nicht die ähnliche Größe der Bewegungen interessiert.
- Der Hurst-Exponent und der Variance-Ratio-Test prüfen langfristiges Trendverhalten gegen die Null eines Random Walk, ohne ein festes Fenster vorzugeben.
- Die Renditepaare für verschiedene Lookbacks und Haltedauern müssen nicht überlappen.
- Der algorithmische Handel kann wissenschaftlich vorgehen: Eine Hypothese wird als quantitatives Modell formuliert und an neuen, ungesehenen Daten auf Vorhersagekraft getestet.
- Scheitert das Modell an bestimmten Daten, werden die Gründe gesucht, vielleicht Variablen ergänzt, und der Test wird wiederholt.
- Statt blind Regeln und Indikatoren zu ergänzen, soll ein fundamentaler Grund gesucht und quantitativ geprüft werden, besonders wenn die Strategie den Backtest underperformt.

## Voraussetzungen


## Anwendung im Trading

- Der Johansen-Test bestimmt im Währungspaar die Kapital-Hedge-Ratio; er wird auf AUD.USD und CAD.USD angewendet, damit eine Punktbewegung in beiden Instrumenten denselben Dollarwert hat.
- Die Halbwertszeit von γ wird aus der Regression der Änderung von γ auf den verzögerten Wert geschätzt, als minus log(2) geteilt durch den Steigungskoeffizienten, und liegt bei etwa 36 Tagen.

## Regeln und Kriterien

- Für die tägliche Sharpe Ratio mal der Wurzel der Zahl der Tage n gelten nach Berntson 2002 die kritischen Werte 1,282 bei p-Wert 0,10, 1,645 bei 0,05, 2,326 bei 0,01 und 3,091 bei 0,001.
- Ist die tägliche Sharpe Ratio mal der Wurzel der Backtest-Tage mindestens 2,326, ist der p-Wert höchstens 0,01.
- Dieses Vorgehen passt zur Überzeugung, dass Strategien mit hoher Sharpe Ratio statistisch signifikanter sind.
- Im praktischen Handel ist ein konstanter Preisdrift, falls vorhanden, meist viel kleiner als die täglichen Schwankungen, deshalb wird β gleich 0 gesetzt.
- Die adf-Funktion verlangt die Preisreihe in zeitlich aufsteigender Ordnung; der zweite Parameter 0 lässt den Offset von null verschieden und den Drift null, der dritte Parameter ist die Lag-Zahl k.
- Man kann mit k gleich 0 beginnen, oft lässt sich die Null aber erst mit k gleich 1 verwerfen.
- Eine Stichprobe auf Intraday-Frequenz erhöht die statistische Signifikanz des ADF-Tests nicht.
- Die Tests auf Mean Reversion oder Stationarität verlangen mindestens 90 Prozent Sicherheit; im praktischen Handel kann man oft mit deutlich weniger Sicherheit profitabel sein.
- Der Johansen-Test bestimmt den Rang r von Λ über die Trace-Statistik und über die Eigen-Statistik und prüft der Reihe nach die Nullen r gleich 0, r kleiner oder gleich 1, bis r kleiner oder gleich n minus 1; werden alle verworfen, ist r gleich n.

## Risiken und Grenzen

- Eine Nullhypothese ist nicht eindeutig. Verschiedene Nullhypothesen können verschiedene Schätzungen der statistischen Signifikanz liefern. Das ist ein Grund, warum viele Kritiker den Hypothesentest für eine fehlerhafte Methode halten, nach Gill 1999.
- Gesucht ist die bedingte Wahrscheinlichkeit, dass die Nullhypothese wahr ist, gegeben die beobachtete Teststatistik R, also P(H0|R). Das beschriebene Verfahren berechnet P(R|H0). Selten gilt P(R|H0) gleich P(H0|R).
- Die Verwerfung einer Nullhypothese ist kein sehr befriedigender Weg, statistische Signifikanz zu schätzen. Das Scheitern, eine Null zu verwerfen, kann dagegen aufschlussreiche Einsichten anregen.
- Beispiel 1.1 zeigt, dass jede zufällige Renditeverteilung mit hoher Kurtosis für Momentum-Strategien günstig sein kann.
- Die Strategien des Buches illustrieren Technik und sind nicht garantiert frei von den Fallstricken aus Kapitel 1; selbst bereinigt können Regimewechsel sie treffen.
- Leser werden zu Out-of-sample-Tests dieser Strategien ermutigt.
- Subjektives Urteil bleibt nötig, weil die statistischen Eigenschaften finanzieller Zeitreihen nicht stationär sind und Wissenschaft eigentlich nur mit stationären Statistiken umgehen kann.

## Beispiele

- Beispiel 1.1 prüft die TU-Momentum-Strategie aus Kapitel 6. Sie kauft den TU-Future bei positiver 12-Monats-Rendite, verkauft ihn bei negativer und hält die Position einen Monat. Gewählt wurde sie wegen der Einfachheit und der festen Haltedauer, sodass der dritte Test nur die Starttage randomisieren muss.
- Im Gauß-Test ist die Teststatistik mean(ret)/std(ret)*sqrt(length(ret)) gleich 2,93. Die Null wird mit besser als 99 Prozent Wahrscheinlichkeit verworfen.
- Im zweiten Test haben die simulierten Tagesrenditen des TU-Futures, nicht die der Strategie, denselben Mittelwert, dieselbe Standardabweichung, dieselbe Schiefe und dieselbe Kurtosis wie die beobachteten Renditen, aber nicht dieselben Korrelationen. Die Preise werden als kumuliertes Produkt aus eins plus simulierte Rendite, minus eins, aufgebaut. Die Strategie läuft 10.000-mal. 1.166 Reihen erreichen eine mindestens ebenso hohe durchschnittliche Strategierendite. Die Null wird nur mit 88 Prozent Wahrscheinlichkeit verworfen.
- Die Form der Renditeverteilung hat damit etwas mit dem Erfolg zu tun. Weniger wahrscheinlich ist der Mittelwert die Ursache, weil die Position zu verschiedenen Zeiten long oder short sein kann.
- Der dritte Test randomisiert die Long- und Short-Einstiegstage, behält die jeweilige Zahl der Long- und Short-Trades bei und zieht 100.000 Stichproben mit randperm.
- Im dritten Test des TU-Beispiels ist die durchschnittliche Strategierendite in keiner von 100.000 Stichproben mindestens so hoch wie die beobachtete.
- Der Text nennt diesen dritten Test für diese Strategie deutlich schwächer.
- Von 10.000 Zufallsrendite-Reihen mit denselben Momenten haben 1.166 eine mindestens ebenso hohe durchschnittliche Strategierendite. Die Null wird nur mit 88 Prozent Wahrscheinlichkeit verworfen.
- Eine erwartete APR von 10 Prozent, signifikant auf 1 Prozent, heißt in der einen Antwort: Von 10.000 simulierten Preisreihen gleicher Länge und mit denselben ersten drei Momenten erreichen nur 100 eine APR von mindestens 10 Prozent.
- In der anderen Antwort heißt es: Bei randomisierten Einstiegstagen erreicht nur eine von 100 Zufallspermutationen eine APR von mindestens 10 Prozent.
- Für die Tagespreise von USD.CAD um 17:00 ET, gezogen aus Ein-Minuten-Bars, ist die ADF-Statistik bei einem Lag etwa minus 1,84, der kritische Wert auf 90 Prozent ist minus 2,594, und die Null λ gleich 0 wird nicht verworfen.
- Die ausgedruckte ADF-Zeile für USD.CAD nennt die t-Statistik minus 1,840744, einen Lag, die AR(1)-Schätzung 0,994120 und die kritischen Werte minus 3,458, minus 2,871 und minus 2,594 auf 1, 5 und 10 Prozent.
- Für USD.CAD liefert der Variance-Ratio-Test h gleich 0 und pValue gleich 0,367281, die Random-Walk-Null wird auf 90 Prozent nicht verworfen.
- Im CADF-Test von EWC auf EWA mit Offset und ohne Drift bei einem Lag ist die t-Statistik minus 3,64346635, die AR(1)-Schätzung minus 0,020411, und die kritischen Werte sind minus 3,880, minus 3,359 und minus 3,038; die Null wird auf 95 Prozent verworfen.
- Für EWA und EWC verwirft der Trace-Test r gleich 0 auf 99 Prozent, Statistik 19,983 gegen 19,935, und r kleiner oder gleich 1 auf 95 Prozent, Statistik 3,983 gegen 3,841; der Eigen-Test verwirft beide Nullen auf 95 Prozent, mit 16,000 gegen 14,264 und 3,983 gegen 3,841.
- Im Trace-Test für EWA, EWC und IGE sind die Statistiken für r ≤ 0, r ≤ 1 und r ≤ 2 gleich 34,429, 17,532 und 4,471; die 95-Prozent-Werte sind 29,796, 15,494 und 3,841, die 99-Prozent-Werte 35,463, 19,935 und 6,635.
- Im Eigen-Test desselben Tripels ist die Statistik für r ≤ 0 gleich 16,897 und liegt unter dem 90-Prozent-Wert 18,893; für r ≤ 1 ist sie 13,061 und liegt über 12,297, aber unter dem 95-Prozent-Wert 14,264; für r ≤ 2 ist sie 4,471 und liegt über 3,841.
- Ein augmentierter Dickey-Fuller-Test zeigt den VIX mit 99 Prozent Sicherheit als stationär.
- Derselbe ADF-Test zeigt, dass die back-adjustierten Front-Month-Preise von VX definitiv nicht mean-reverten.
- Der ADF-Test des 12-Monats-Log-Kalender-Spreads von CL findet Stationarität mit 99 Prozent Wahrscheinlichkeit und eine Halbwertszeit von 36 Tagen.
- Für TU sind die besten Kompromisse aus Korrelation und p-Wert die Paare (60, 10), (60, 25), (250, 10), (250, 25), (250, 60) und (250, 120).
- Bei den Vorzeichen sind die besten Paare (60, 10), (250, 10) und (250, 25), und die Ergebnisse weichen nicht stark von Tabelle 6.1 ab.
- Das Paar 250 zu 25 hat für TU einen Korrelationskoeffizienten von 0,27 bei einem p-Wert von 0,02.
- Der Hurst-Exponent von TU ist 0,44, und der Variance-Ratio-Test verwirft den Random Walk nicht.
- Eintagesrenditen können negativ korreliert sein, während die vergangene 20-Tage-Rendite mit der künftigen 40-Tage-Rendite stark positiv korreliert sein kann.
- Als das ETF-Paar GLD gegen GDX 2008 aufhörte zu kointegrieren, lautete die Hypothese auf den hohen Rohölpreis; mit dem Ölpreis als Input funktionierte das Kointegrationsmodell wieder.
- Als GLD gegen GDX 2008 aufhörte zu kointegrieren, wurde die Hypothese eines hohen Rohölpreises gebildet.
- Mit dem Ölpreis als zusätzlicher Inputvariable funktionierte das Kointegrationsmodell wieder.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 1–20 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-001-p001-p020|S. 1–20]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 20–39 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-002-p020-p039|S. 20–39]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 58–77 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-004-p058-p077|S. 58–77]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 77–96 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-005-p077-p096|S. 77–96]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 96–115 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-006-p096-p115|S. 96–115]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 115–134 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-007-p115-p134|S. 115–134]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 134–153 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-008-p134-p153|S. 134–153]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 153–172 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-009-p153-p172|S. 153–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 172–191 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-010-p172-p191|S. 172–191]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 191–210 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-011-p191-p210|S. 191–210]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 210–229 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-012-p210-p229|S. 210–229]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 229–248 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-013-p229-p248|S. 229–248]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 248–267 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-014-p248-p267|S. 248–267]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 267–286 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-015-p267-p286|S. 267–286]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 305–324 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-017-p305-p324|S. 305–324]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 324–343 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-018-p324-p343|S. 324–343]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 381–400 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-021-p381-p400|S. 381–400]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 419–438 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-023-p419-p438|S. 419–438]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 476–495 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-026-p476-p495|S. 476–495]]

## Verwandte Themen
