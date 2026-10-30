---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/20 - Trading-Performance & Auswertung/20 - Trading-Performance & Auswertung|20 - Trading-Performance & Auswertung]]"
weitere_hauptthemen: []
unterthema: "Risikoadjustierte Kennzahlen"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Sharpe Ratio


## Kurzdefinition

- Die Sharpe Ratio einer Handelsregel ist der erwartete Gewinn dieser Regel geteilt durch die Standardabweichung des Gewinns.
- Sind die Überschussrenditen über den risikofreien Satz unabhängig, identisch verteilt und gaußsch, ist die Sharpe Ratio ihr Mittelwert geteilt durch ihre Standardabweichung.
- Die Sharpe Ratio einer Handelstrajektorie ist die über die Horizonte summierte erwartete Überschussrendite nach Transaktionskosten, geteilt durch die Wurzel der summierten quadratischen Formen ω′h Vh ωh.

## Kernaussagen

- Ein Backtest garantiert nicht einmal, dass dieselbe Sharpe Ratio erreicht würde, könnte man mit einem rückgerüsteten DeLorean in der Zeit zurückreisen, nach Bailey und López de Prado 2012.
- Die Sharpe Ratio des schließlich gewählten Ergebnisses ist um die Zahl der durchgeführten Versuche zu deflationieren, nach Bailey und López de Prado 2014b.
- Wird in der combinatorially symmetric cross-validation die Sharpe Ratio als Auswahlmetrik verwendet, wird angenommen, dass die Annahme unabhängig identisch normalverteilter Werte auf verschiedenen Schnitten der berichteten Performance hält.
- Die kombinatorische purged Cross-Validation berechnet je Pfad eine Sharpe Ratio und daraus eine empirische Verteilung.
- Auf einem Martingal ist die wahre Sharpe Ratio null.
- Der erwartete höchste Schätzwert über viele Versuche liegt trotzdem über null und wächst mit der Streuung der Schätzungen.
- Für eine große Versuchszahl ist der erwartete Höchstwert standardnormaler Größen höchstens die Quadratwurzel des Produkts aus zwei und dem natürlichen Logarithmus der Versuchszahl.
- Der erwartete beste Sharpe-Wert ist der erwartete Höchstwert einer standardnormalen Stichprobe mal der Standardabweichung der geschätzten Sharpe Ratios.
- Die Heatmaps zeigen die Sharpe Ratios vor einer Annualisierung.
- Die Positionsgröße ändert die Sharpe Ratio nicht, weil sie den Gewinn nur umskaliert.
- Nach der Vermutung gibt es zu einem diskreten Ornstein-Uhlenbeck-Preis genau eine Kombination aus Gewinnziel und Stop, die die Sharpe Ratio der Regel maximiert.
- Unter den gewünschten Eigenschaften der Wettrenditen steht eine hohe Sharpe Ratio.
- Ihr Zweck ist, die Fähigkeit einer Strategie oder eines Investors zu beurteilen.
- Weil Mittelwert und Standardabweichung meist unbekannt sind, bleibt die wahre Sharpe Ratio unsicher.
- Sharpe-Ratio-Berechnungen können deshalb erhebliche Schätzfehler enthalten.
- Die annualisierte Sharpe Ratio multipliziert den Wert mit der Quadratwurzel der mittleren Anzahl Renditen pro Jahr.
- Bei symmetrischer Auszahlung kürzt sich die Höhe von Gewinn und Verlust aus der Sharpe Ratio heraus.
- Bei symmetrischer Auszahlung ist die annualisierte Sharpe Ratio die Wurzel aus der Zahl der Wetten mal die t-Statistik der Trefferwahrscheinlichkeit unter der Nullhypothese, dass diese Wahrscheinlichkeit 0,5 beträgt.
- Schon eine Trefferwahrscheinlichkeit knapp über 0,5 kann bei genügend vielen Wetten eine hohe Sharpe Ratio erzeugen.
- Im Hochfrequenzhandel liegt die Trefferwahrscheinlichkeit nur knapp über 0,5, und der wirtschaftliche Hebel ist eine hohe Zahl von Wetten.
- Bei der symmetrischen Auszahlung ist die Sharpe Ratio eine Funktion der Precision.
- Das Auslassen einer Gelegenheit wird weder direkt belohnt noch direkt bestraft.
- Viele ausgelassene Gelegenheiten verkleinern die Zahl der Wetten und ziehen die Sharpe Ratio gegen null.
- SR[r] = (∑_{h=1}^{H} μ′h ωh − τh[ω]) / √(∑_{h=1}^{H} ω′h Vh ωh), wobei Vh die prognostizierte Kovarianzmatrix des Horizonts ist.
- Gesucht wird die Trajektorie, die diese Sharpe Ratio maximiert.
- Die Nebenbedingung verlangt, dass die absoluten Gewichte in jedem Horizont auf 1 summieren.
- Diese Nebenbedingung beschreibt eine volle Investition ohne Leverage.
- Die Aufgabe sucht ein globales dynamisches Optimum und unterscheidet sich damit vom statischen Optimum der Mean-Variance-Optimierung.
- Die Halbwertszeit der Mean Reversion ist ein guter Prädiktor für die Profitabilität oder die Sharpe Ratio einer Mean-Reversion-Strategie auf dieser Preisreihe.
- Eine kurze Zeitskala erhöht die Zahl der Trades pro Jahr und damit die statistische Sicherheit und die Sharpe Ratio in Backtest und Live-Handel.
- Ist die Wahrscheinlichkeit eines tieferen Einbruchs nicht konstant, liefert Scaling-in voraussichtlich eine bessere realisierte Sharpe Ratio, auch wenn es den erwarteten Gewinn nicht erhöht.
- Die lineare Strategie dient dazu zu prüfen, ob erwartete Rendite oder Sharpe Ratio der Mean-Reversion-Strategie gut genug sind, und ist dafür fast frei von Data-Snooping-Bias.
- Aus Handelssicht sind möglichst kurze Haltedauern vorzuziehen, weil sie die besten Sharpe Ratios erzeugen.
- Weniger unabhängige Handelssignale führen zu einer niedrigeren Sharpe Ratio, und tägliches Rebalancing macht lange Momentum-Signale nicht unabhängiger.
- Profitable Momentum-Strategien haben tendenziell niedrigere Sharpe Ratios als Mean-Reversal-Strategien.
- Momentum-Strategien zu einem Portfolio aus Mean-Reversion-Strategien hinzuzufügen ergibt höhere Sharpe Ratios und kleinere Drawdowns als jeder Strategietyp allein.

## Funktionsweise

- K Kapitaleinheiten werden auf N Assets verteilt, wobei K größer als N angenommen wird.
- Die Zahl der nichtnegativen ganzzahligen Lösungen von x1 + … + xN = K ist der Binomialkoeffizient (K + N − 1) über (N − 1).
- Bei sechs Kapitaleinheiten und drei Assets gelten (1, 2, 3) und (3, 2, 1) als verschiedene Allokationen.
- Zu jedem Vektor absoluter Gewichte werden 2^N vorzeichenbehaftete Gewichtungsvektoren gebildet.
- Die Menge der Trajektorien ist das kartesische Produkt dieser Gewichtungsvektoren über H Horizonte.
- Für jede Trajektorie werden zuerst die Transaktionskosten und danach die Sharpe Ratio berechnet.
- Behalten wird die Trajektorie mit der höchsten Sharpe Ratio.
- Das Verfahren bestimmt die global optimale Trajektorie, ohne konvexe Optimierung zu verwenden.
- Eine Lösung wird auch gefunden, wenn die Kovarianzmatrizen schlecht konditioniert sind.
- Für jede Strategie wird die Überschussrendite gebraucht, weil die Sharpe Ratio der Durchschnitt der Überschussrenditen geteilt durch deren Standardabweichung ist, geeignet annualisiert.
- Die Überschussrendite ist die Rendite der gehaltenen Positionen minus die Finanzierungskosten dieser Positionen.
- Bei reinen Intraday-Positionen sind die Finanzierungskosten null.
- Bei einem long-short-dollarneutralen Aktienportfolio können die Finanzierungskosten nahe null gesetzt werden, auch wenn der Habenzins gewöhnlich etwas kleiner ist als der Betrag des Sollzinses.
- Bei Futures sind die Finanzierungskosten null, weil Futures Kontrakte sind und keine Assets, die Cash zur Finanzierung brauchen; die Margin-Kasse wird nicht gezählt, weil dieses Cash auf dem Konto Zinsen erwirtschaftet.
- Bei Währungs-Crosses können die Finanzierungskosten ebenfalls null gesetzt werden, wenn der Rollover-Zins zur prozentualen Änderung des Cross addiert wird.

## Voraussetzungen

- Die übliche Annualisierung mit der Wurzel der Beobachtungen pro Jahr setzt unabhängig und identisch verteilte Renditen voraus.
- Die geschlossenen Formeln für symmetrische und asymmetrische Auszahlungen setzen unabhängig und identisch verteilte Wetten voraus.
- Die Renditen sind in jedem Horizont multivariat normal und über die Zeit unabhängig, aber nicht identisch verteilt.
- Der prognostizierte Mittelwert μh ist bereits um den risikofreien Zinssatz bereinigt.
- Eine Handelstrajektorie ω ist eine N×H-Matrix der Kapitalanteile für N Assets über H Horizonte.

## Anwendung im Trading


## Regeln und Kriterien

- Zu einer Ziel-Sharpe-Ratio lässt sich die nötige Trefferwahrscheinlichkeit aus Frequenz und Schwellen bestimmen.
- Umgekehrt lässt sich die nötige Wettfrequenz aus Trefferwahrscheinlichkeit und Schwellen bestimmen.
- Für ein Gewinnziel von 0,1 und eine Ziel-Sharpe-Ratio von 1,5 steigt die nötige Wettfrequenz, wenn die Verlustauszahlung negativer wird oder die Trefferwahrscheinlichkeit sinkt.
- Modelle mit hoher Sharpe Ratio und kurzer maximaler Drawdown-Dauer bestehen die Cross-Validation fast automatisch, weil sie nur in den seltenen Drawdown-Perioden durchfallen.
- Strategien mit hoher Sharpe Ratio sind nach diesem Hypothesentest statistisch signifikanter.
- Die Teststatistik der Gauß-Null ist der Mittelwert geteilt durch die Standardabweichung, multipliziert mit der Wurzel der Zahl der Datenpunkte. Für die tägliche Sharpe Ratio mal der Wurzel der Tage n gelten die kritischen Werte 1,282 bei p 0,10, 1,645 bei 0,05, 2,326 bei 0,01 und 3,091 bei 0,001.
- Liegt dieses Produkt mindestens bei 2,326, ist der p-Wert höchstens 0,01.
- Im TU-Beispiel beträgt die Teststatistik 2,93. Die Null wird mit besser als 99 Prozent Wahrscheinlichkeit verworfen.
- Die meisten Trader wären zufrieden, wenn der Live-Handel eine Sharpe Ratio besser als die Hälfte des Backtest-Wertes erzeugt.
- Strategien mit hoher Rendite und niedriger Sharpe Ratio lohnen den Backtest nicht.
- Hohe Sharpe Ratios gehören mit Out-of-Sample-Tests und Cross-Validation zu den guten Praktiken gegen Data-Snooping-Bias. Maßgeblicher bleibt der Walk-Forward-Test.
- Der Vergleichsmaßstab einer Long-only-Strategie ist die Information Ratio, nicht die Sharpe Ratio.

## Risiken und Grenzen

- Walk-Forward-Schätzungen haben eine hohe Varianz, weil wenige Beobachtungen die Sharpe Ratio stark beeinflussen.
- Eine Aufwärmphase verkürzt den Walk-Forward-Backtest und kann die Varianz der Sharpe-Schätzung weiter erhöhen.
- Andere Eingabewerte als die simulierten Kombinationen würden andere Sharpe Ratios liefern.
- Wegen der vielen Wetten genügt eine kleine Änderung der Trefferwahrscheinlichkeit, um die Sharpe Ratio stark zu verschieben, deshalb ist die Strategie dagegen anfällig.
- Die Auflösung der Gleichung nach der nötigen Wettfrequenz kann eine Scheinlösung erzeugen und ist zu prüfen.
- Die Maximierung ist kein konvexes quadratisches Programm, weil die Renditen nicht identisch verteilt sind, die Transaktionskosten unstetig sind und sich mit dem Horizont ändern, und weil SR[r] selbst nicht konvex ist.
- Alle Trajektorien zu bewerten ist extrem rechenintensiv und ähnelt dem Problem des Handlungsreisenden.
- Digitale Rechner bewerten die zulässigen Lösungen nacheinander.
- Für diese NP-vollständigen oder NP-harten Aufgaben sind digitale Rechner ungeeignet.
- Quantenrechner können durch lineare Superposition viele Lösungen zugleich bewerten.
- Dieses Kapitel legt die Grundlage für die Quantenlösung der optimalen Handelstrajektorie bei Rosenberg et al. (2016).
- Rosenberg et al. (2016) haben das Problem der optimalen Handelstrajektorie mit einem Quantum Annealer gelöst.

## Beispiele

- Die x-Achse von Abbildung 11.1 ist die In-Sample-Sharpe-Ratio der besten ausgewählten Strategie, die y-Achse die Out-of-Sample-Sharpe-Ratio derselben Strategie.
- Die Abbildung zeigt einen starken und anhaltenden Leistungsabfall durch Backtest-Overfitting, und die Wahrscheinlichkeit einer negativen Out-of-Sample-Sharpe-Ratio beträgt 0,74.
- Die eingetragene Anpassung lautet: die Out-of-Sample-Sharpe-Ratio ist 0,87 minus 0,75 mal die In-Sample-Sharpe-Ratio plus einen Fehler, bei einem adjustierten R² von 0,17.
- Bei Prognose 0, Halbwertszeit 5 und Sigma 1 liegen die besten Sharpe Ratios um 3,2.
- Bei Prognose 5 und Halbwertszeit 5 liegen die Sharpe Ratios um 12.
- Bei Prognose 5 und Halbwertszeit 10 liegen die Sharpe Ratios um 9.
- Bei Prognose 5 und Halbwertszeit 25 betragen die Sharpe Ratios 2,7.
- Bei Prognose 5 und Halbwertszeit 50 fallen sie auf etwa 0,8.
- Bei Prognose 5 und Halbwertszeit 100 beträgt das Maximum 0,32.
- Bei Prognose 5 und Halbwertszeit 50 fällt die Sharpe Ratio auf etwa 0,8.
- Bei Prognose minus 5 und Halbwertszeit 5 liegen die schlechtesten Sharpe Ratios um minus 12.
- Bei Prognose minus 5 und Halbwertszeit 10 liegen die Sharpe Ratios etwa bei minus 9.
- Bei einer Trefferwahrscheinlichkeit von 0,55 beträgt der t-Wert unter der Null einer Trefferwahrscheinlichkeit von 0,5 den Wert 0,1005, und eine annualisierte Sharpe Ratio von 2 erfordert 396 Wetten pro Jahr.
- Bei 52 Wetten pro Jahr ist für eine annualisierte Sharpe Ratio von 2 eine Trefferwahrscheinlichkeit von 0,6336 erforderlich.
- Bei 260 Wetten, einer Verlustauszahlung von minus 0,01, einer Gewinnauszahlung von 0,005 und einer Trefferwahrscheinlichkeit von 0,7 beträgt die annualisierte Sharpe Ratio 1,173.
- Bei 260 Wetten, Verlustauszahlung minus 0,01 und Gewinnauszahlung 0,005 hebt eine Trefferwahrscheinlichkeit von 0,72 die annualisierte Sharpe Ratio von 1,173 auf 2.
- Das Zahlenbeispiel verwendet drei Assets und zwei Horizonte.
- Die statische Vergleichslösung bildet je Horizont ein lokales Optimum und skaliert die absoluten Gewichte auf die Summe 1.
- Im Zahlenbeispiel bewertet ein Digitalrechner die Sharpe Ratio der statischen und der dynamischen Lösung nacheinander.
- Ein Quantenrechner würde alle Trajektorien auf einmal bewerten.
- Eine annualisierte Rendite von 30 Prozent bei einer Sharpe Ratio von 0,3 und zwei Jahren maximaler Drawdown-Dauer zeigt eine nicht konsistente Strategie. Die hohe Rendite kann ein Zufall sein.
- Die Long-only-Rohöl-Strategie von 2007 hatte eine Sharpe Ratio von 1,5 bei 20 Prozent Rendite. Buy-and-hold des Front Month hatte 1,7 bei 47 Prozent.
- Ein neuronales Netz mit etwa 100 Knoten kann eine Backtest-Sharpe-Ratio von 6 erzeugen und dennoch vorwärts kaum Vorhersagekraft haben.
- Die Hochfrequenzstrategie auf den E-mini S&P 500 hat im Backtest eine Sharpe Ratio von 6 bei 200 Prozent jährlicher Durchschnittsrendite und 50 Sekunden durchschnittlicher Haltedauer.
- Die lineare Strategie auf EWA, EWC und IGE hat eine Sharpe Ratio von 1,4 bei 12,6 Prozent APR.
- Der Preis-Spread von GLD und USO mit dynamischer Hedge Ratio hat eine Sharpe Ratio von etwa 0,59 bei etwa 10,9 Prozent APR.
- Der Log-Preis-Spread hat eine Sharpe Ratio von 0,5 bei 9 Prozent APR, vor den zusätzlichen Rebalancing-Kosten.
- Die Bollinger-Strategie auf demselben Spread hat eine Sharpe Ratio von 0,96 bei 17,8 Prozent APR.
- Die Kalman-Strategie auf EWA und EWC hat eine Sharpe Ratio von 2,4 bei 26,2 Prozent APR.
- Die lineare Strategie auf dem Verhältnis USO zu GLD hat eine negative APR; eine Sharpe Ratio wird dafür nicht genannt.
- Buy-on-Gap hat vom 11. Mai 2006 bis 24. April 2012 eine Sharpe Ratio von 1,5 bei einer APR von 8,7 Prozent.
- Short-on-Gap hat über denselben Zeitraum eine Sharpe Ratio von 1,27 bei einer APR von 46 Prozent und einen steileren Drawdown.
- Die Arbitrage zwischen SPY und den ausgewählten Komponenten hat eine Sharpe Ratio von 1,3 bei einer APR von 4,5 Prozent.
- Das lineare Long-Short auf dem SPX hat eine Sharpe Ratio von 1,3 bei einer APR von 13,7 Prozent; die Open-to-Close-Variante hat eine Sharpe Ratio von 4,7 bei einer APR von 73 Prozent.
- AUD.USD gegen CAD.USD hat eine Sharpe Ratio von 1,6 bei einer APR von 11 Prozent.
- AUD.CAD mit Rollover hat eine Sharpe Ratio von 0,54 bei einer APR von 6,2 Prozent; ohne Rollover wären es 0,58 und 6,7 Prozent.
- Der CL-Kalender-Spread hat eine Sharpe Ratio von 1,3 bei einer ungehebelten APR von 8,3 Prozent.
- Die lineare Mean-Reversion-Strategie auf dem CL-12-Monats-Kalenderspread hat vom 2. Januar 2008 bis zum 13. August 2012 eine Sharpe Ratio von 1,3 bei einer ungehebelten annualisierten Rendite von 8,3 Prozent.
- Die lineare Mean-Reversion-Strategie auf dem VX-Kalenderspread hat vom 27. Oktober 2008 bis zum 23. April 2012 eine Sharpe Ratio von 1,5 bei einer annualisierten Rendite von 17,7 Prozent.
- Die Bollinger-Band-ähnliche ES-VX-Mean-Reversion-Strategie hat auf dem Testset vom 29. Juli 2010 bis zum 8. Mai 2012 eine Sharpe Ratio von 1,4 bei einer annualisierten Rendite von 12,3 Prozent.
- Die TU-Strategie mit Lookback 250 und Haltedauer 25 hat vom 1. Juni 2004 bis zum 11. Mai 2012 eine Sharpe Ratio von 1 bei 1,7 Prozent annualisierter Rendite.
- Tabelle 6.2 nennt Sharpe Ratios von 1,09 für BR, 1,05 für HG und 1,04 für TU.
- Das TU-Rollrendite-Signal mit Schwelle 3 Prozent hat vom 2. Januar 2009 bis zum 13. August 2012 eine Sharpe Ratio von 2,1 bei 2,5 Prozent annualisierter Rendite.
- Die kombinierte CL-Regel hat eine Sharpe Ratio von 1,1 bei 12 Prozent annualisierter Rendite.
- Der S&P DTI hat nach Dever von Januar 1988 bis Dezember 2010 eine Sharpe Ratio von 1,3, der S&P 500 im selben Zeitraum 0,61.
- XLE gegen USO hat eine Sharpe Ratio von etwa 1 bei 16 Prozent annualisierter Rendite vom 26. April 2006 bis zum 9. April 2012.
- Die VX-ES-Rollrendite-Strategie hat eine Sharpe Ratio von 1 bei 6,9 Prozent annualisierter Rendite vom 29. Juli 2010 bis zum 7. Mai 2012.
- Die querschnittliche Rohstoffstrategie hat vom 1. Juni 2005 bis zum 31. Dezember 2007 eine Sharpe Ratio von 1,37.
- Beispiel 6.2 hat vom 15. Mai 2007 bis zum 31. Dezember 2007 eine Sharpe Ratio von 4,1; Daniel und Moskowitz finden von 1947 bis 2007 eine Sharpe Ratio von 0,83.
- Hafez und Xie erreichen vor Kosten Sharpe Ratios von 3,9 bis 5,3.
- Das lineare Mean-Reversion-Modell für S&P-500-Aktien hat eine Sharpe Ratio von 4,7 bei einer Haltedauer von weniger als einem Tag.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]
- Advances in Financial Machine Learning.pdf, S. 343–362 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-019-p343-p362|S. 343–362]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 191–210 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-011-p191-p210|S. 191–210]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 362–381 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-020-p362-p381|S. 362–381]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 381–400 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-021-p381-p400|S. 381–400]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 476–495 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-026-p476-p495|S. 476–495]]

## Verwandte Themen
