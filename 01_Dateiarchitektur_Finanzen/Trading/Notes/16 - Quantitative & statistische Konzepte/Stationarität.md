---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Zeitreihen"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Stationarität


## Kurzdefinition

- Nichtstationarität entsteht hier durch Gedächtnis, also durch eine lange Historie früherer Niveaus, die den Mittelwert der Reihe über die Zeit verschiebt.
- Renditen sind stationär, aber gedächtnislos; Preise haben Gedächtnis, sind aber nicht stationär. Gesucht ist die kleinste Differenzierung, die die Preisreihe stationär macht und möglichst viel Gedächtnis behält.
- Box-Jenkins behandelt Renditen als stationär, aber gedächtnislos. Engle-Granger behandelt Log-Preise als gedächtnisbehaftet, aber nicht stationär.
- Notwendig und hinreichend für die Stationarität des diskreten Ornstein-Uhlenbeck-Prozesses ist ein Koeffizient phi im offenen Intervall von minus 1 bis 1.
- Werden Rohpreise im ADF getestet und die Null verworfen, gelten die Preise als stationär mit endlicher Varianz.
- Die wenigen Preisreihen, die mean-reverting gefunden werden, heißen stationär.
- Stationarität heißt, dass die Varianz der Logpreise langsamer wächst als bei einem geometrischen Random Walk, also sublinear in der Zeit, angenähert durch τ hoch 2H mit H kleiner als 0,5.
- Stationarität ist ein irreführender Name: sie bedeutet nicht, dass die Preise notwendig in einer Spanne liegen und die Varianz zeitunabhängig mit Hurst-Exponent null ist, sondern nur, dass die Varianz langsamer wächst als normale Diffusion.
- Stationarität bedeutet, dass Preise langsamer diffundieren als ein geometrischer Random Walk.

## Kernaussagen

- Als Folge von Arbitrage haben Finanzreihen ein niedriges Signal-Rausch-Verhältnis; ganzzahlige Stationaritätstransformationen senken das Signal weiter, weil sie das Gedächtnis entfernen.
- Sind nach einer solchen Transformation nur Reste des Signals übrig, führen komplexe Verfahren auf den gedächtnislosen Reihen leicht zu Fehlentdeckungen.
- Preisreihen haben Gedächtnis, weil jeder Wert von einer langen Historie früherer Niveaus abhängt; ganzzahlig differenzierte Reihen wie Renditen schneiden diese Historie nach einem endlichen Fenster ab.
- Renditen sind nur eine und in den meisten Fällen suboptimale Preistransformation unter vielen möglichen.
- Null-Differenzierung ist ebenso willkürlich wie die Differenzierung um einen Schritt.
- Bei positivem ganzzahligem d sind alle Gewichte nach k größer als d null. Für d gleich 1, die übliche Renditenrechnung, bleibt die Gewichtsfolge 1, minus 1 und danach nur Nullen.
- Liegt d zwischen 0 und 1, sind alle Gewichte nach dem ersten negativ und größer als minus 1. Für d über 1 ist das zweite Gewicht kleiner als minus 1, und alle weiteren sind positiv.
- Die Gewichte konvergieren asymptotisch gegen null, von links, wenn der ganzzahlige Anteil von d gerade ist, und von rechts, wenn er ungerade ist.
- Im Sonderfall d zwischen 0 und 1 liegt jedes Gewicht nach dem ersten echt zwischen minus 1 und 0. Dieser Vorzeichenwechsel ist nötig, damit die transformierte Reihe stationär wird, während das Gedächtnis langfristig abklingt oder sich ausgleicht.
- Der minimale Fixed-Width-Koeffizient d* misst, wie viel Gedächtnis für Stationarität entfernt werden muss: 0, wenn die Reihe schon stationär ist, unter 1 bei einer Unit Root und über 1 bei explosivem Verhalten wie einer Blase.
- Im Fall einer nur milden Nichtstationarität, d* wenig über 0 und weit unter 1, entfernt die volle ganzzahlige Differenzierung zu viel Gedächtnis und Prognosekraft.
- Nahezu alle genannten Finanzarbeiten erzwingen Stationarität mit d gleich 1 und überdifferenzieren damit. Bei 87 der liquidesten Futures genügt in allen Fällen d unter 0,6, bei der großen Mehrheit schon d unter 0,3.
- Die Fixed-Width-Fracdiff-Methode zeigt, dass nicht das ganze Gedächtnis aufgegeben werden muss, um Stationarität zu gewinnen, und dass der Kointegrations-Kunstgriff für ML-Prognosen nicht nötig ist.
- Die Fixed-Width-Fracdiff-Methode zeigt, dass für Stationarität nicht das ganze Gedächtnis aufgegeben werden muss.
- Dieselbe Methode soll Stationarität sichern, ohne auf Gedächtnis und damit auf Prognosekraft zu verzichten.
- Ein Prozess aus unabhängigen identisch verteilten Gauß-Ziehungen wird als gedächtnislose stationäre Reihe beschrieben. Die kumulative Summe dieser Ziehungen wird als nichtstationäre Reihe ohne Gedächtnis beschrieben.
- Eine Sinusreihe wird als stationäre Reihe mit Gedächtnis beschrieben. Werden alle Werte um dieselbe positive Größe verschoben und danach kumulativ summiert, entsteht nach dem Text eine nichtstationäre Reihe mit Gedächtnis.
- Die zweifache Differenzierung der kumulativen Summe aus der Übung wird als überdifferenziert bezeichnet.
- Die Verteilung des diskreten Ornstein-Uhlenbeck-Prozesses ist gaußsch.
- Exponentielles Wachstum oder Kollaps ist mit einem stationären Prozess unvereinbar und auf Dauer unhaltbar.
- Ein Zyklus aus Blase, Platzen und neuer Blase lässt die Reihe für Tests mit nur einer Blase stationär erscheinen.
- Tests, die mehrere Blasen zulassen, sind deshalb robuster.
- Standard-Unit-Root- und Kointegrationstests können einen stationären Prozess nicht verlässlich von einem periodisch zusammenbrechenden Blasenmodell unterscheiden.
- Solche Muster sehen eher wie ein Unit-Root-Prozess oder eine stationäre Autoregression aus als wie ein explosiver Prozess.
- Im Null-Lag-Modell auf Logpreisen konvergiert der erwartete Logpreis bei Beta kleiner als 0, und bei Beta gleich 0 ist das System nichtstationär.
- Der Augmented-Dickey-Fuller-Test, der Hurst-Exponent, der Variance-Ratio-Test und die Half-Life dienen dazu, Time-Series-Mean-Reversion oder Stationarität zu erkennen.
- Über die mechanische Anwendung hinaus soll intuitiv klar werden, was diese Tests wirklich prüfen, samt der einfachen mathematischen Gleichungen dahinter.
- Als Eingaben kommen Rohpreise, Log-Preise oder Verhältnisse infrage, und es wird gezeigt, welche Wahl am sinnvollsten ist.
- Hurst-Exponent und Variance-Ratio-Test prüfen die Stationarität, der ADF-Test die Mean Reversion.
- Man ist nicht auf von sich aus stationäre Instrumente beschränkt, weil kointegrierende Reihen ein stationäres Portfolio ergeben.
- Der Eigenvektor mit dem größten Eigenwert bildet das stationäre Portfolio mit der kürzesten Halbwertszeit.
- Echte Stationarität ist für eine Mean-Reversion-Strategie nicht notwendig, wenn die Position vor dem nächsten Gleichgewicht geschlossen wird.
- Eine stationäre Reihe mit einer Halbwertszeit von zehn Jahren muss trotzdem keine großen Gewinne tragen.
- Der Spread aus Hedge Ratios der Regression oder des Johansen-Tests ist per Konstruktion eine stationäre Zeitreihe.
- Kointegrieren die Logpreise, bildet der Marktwert des kapitalgewichteten Portfolios samt impliziter Kasse eine stationäre Reihe, konstant ist er nicht.
- Tägliche Preisreihen einzelner Aktien erfüllen fast nie die in Kapitel 2 definierte Stationarität; der geometrische Random Walk beschreibt sie gut.
- Saisonale oder intraday Mean Reversion ist mit den üblichen Stationaritäts- oder Kointegrationstests schwer zu erkennen, kann aber sehr profitabel sein.
- Die statistischen Tests der Zeitreihen-Mean-Reversion sind für querschnittliche Mean Reversion weitgehend irrelevant.
- Nach dem Johansen-Eigenvektor wird aus den ausgewählten Aktien und SPY ein long-short-stationäres Portfolio gebildet.
- Die Grundidee eines stationären Portfolios ausländischer Währungen entspricht dem Handel von Aktienindex-ETF-Paaren verschiedener Länder mit ähnlichen ökonomischen Fundamentaldaten.
- Ein ADF-Test zeigt den VIX mit 99 Prozent Sicherheit als stationär.
- Die back-adjustierten Front-Month-Preise von VX mean-reverten laut ADF definitiv nicht.
- Der 12-Monats-Log-Kalender-Spread von CL ist im ADF mit 99 Prozent Wahrscheinlichkeit stationär und hat eine Halbwertszeit von 36 Tagen.
- Renditereihen mean-reverten im Gegensatz zu Preisreihen fast immer; wird nur die Roll-Return-Komponente betrachtet, kann das anders sein.
- Das Verhältnis Back zu Front von VX ist nach dem ADF-Test mit 99 Prozent Wahrscheinlichkeit stationär.
- Ein Portfolio long 0,3906 Kontrakte VX und long einen Kontrakt ES soll stationär sein.
- Der Crack Spread ist nach dem ADF-Test vom 20. Mai 2002 bis zum 4. Mai 2012 nicht mean-reverting.
- Der Spread aus CL und BZ im Verhältnis 1:1 ist weit von stationär entfernt.
- Die Log-Preise der VX-Futures als Funktion der Restlaufzeit fallen nicht auf eine Gerade, anders als bei einem Future auf einen gehandelten Basiswert.
- Subjektives Urteil ist oft nötig, weil die statistischen Eigenschaften finanzieller Zeitreihen nicht stationär sind.
- Wissenschaft kann eigentlich nur mit stationären Statistiken umgehen.
- Die Hebelverfahren unterstellen, dass die künftige Verteilung der Marktrenditen der vergangenen entspricht; das ist meist falsch.
- Noch restriktiver wird dasselbe für die Strategierenditen unterstellt, am restriktivsten eine Gauß-Verteilung.
- Es gibt keine Garantie, dass künftiger Mittelwert und künftige Varianz den historischen gleichen.
- Kelly über mehrere Strategien ist nur optimal, wenn erwartete Renditen und Volatilitäten unverändert bleiben; nach einem schweren Drawdown ist das zweifelhaft.
- Eine Preisreihe, die bisher mean-reverting war, kann künftig trendfolgen.
- Die Kelly-Optimalität über das Portfolio setzt unveränderte erwartete Renditen und Volatilitäten voraus.
- Nach einem schweren Drawdown ist zweifelhaft, ob diese Erwartungen noch gelten.

## Funktionsweise

- Die Gewichte beginnen bei 1 und entstehen iterativ, indem das vorige Gewicht mit minus (d minus k plus 1) durch k multipliziert wird.
- Beim Expanding Window hängt der relative Gewichtsverlust vom Tempo ab, mit dem die Gewichte gegen null laufen. Zu einer Toleranz wird der Anfang verworfen, dessen Gewichtsverlust die Schwelle überschreitet.
- Bei d gleich 1 genügt es, den ersten Punkt zu streichen. Geht d gegen 0, wird dieser zu verwerfende Vorspann länger.
- Der negative Drift dieses Fensters kommt von negativen Gewichten, die mit der Verbreiterung auf die frühen Beobachtungen gelegt werden. Ohne Kontrolle des Gewichtsverlusts bleibt im Wesentlichen nur dieser Trend sichtbar; mit Kontrolle ist der Drift schwächer, aber immer noch erheblich.
- Das feste Fenster schneidet Gewichte ab, sobald ihr Betrag unter eine Schwelle fällt, und verwendet für alle Zeitpunkte denselben Gewichtsvektor.
- Das Ergebnis ist eine driftfreie Mischung aus Niveau und Rauschen. Wegen Schiefe und Excess-Kurtosis aus dem Gedächtnis ist die Verteilung nicht mehr gaußsch, aber stationär.
- Praktisch wird erst die kumulative Summe gebildet, damit eine Differenzierung nötig ist, dann die Fixed-Width-Reihe für mehrere d zwischen 0 und 1 berechnet und das kleinste d gewählt, dessen ADF-p-Wert unter 5 Prozent liegt.
- Zuerst wird die kumulative Summe gebildet, damit überhaupt eine Differenzierung nötig ist. Dann wird die Fixed-Width-Reihe für mehrere d zwischen 0 und 1 berechnet, und es wird das kleinste d gewählt, bei dem der p-Wert der ADF-Statistik unter 5 Prozent fällt.
- Mean Reversion und Stationarität sind äquivalente Sichtweisen, aber der ADF-Test prüft die Mean Reversion und Hurst-Exponent sowie Variance-Ratio-Test die Stationarität.
- Für einen geometrischen Random Walk ist H gleich 0,5 und die Varianz linear in τ; der Variance-Ratio-Test prüft die Null, dass H wirklich 0,5 ist.

## Voraussetzungen

- Für Inferenz werden invariante Prozesse gebraucht, etwa Renditen, Änderungen von Log-Preisen, Änderungen von Yields oder Änderungen der Volatilität.
- Überwachte Lernverfahren brauchen stationäre Features, sonst lässt sich eine ungesehene Beobachtung nicht auf viele bekannte Beispiele abbilden.
- Stationarität ist für hohe ML-Leistung notwendig und nicht hinreichend, weil sie allein keine Prognosekraft sichert.
- Die Formel für die Halbwertszeit verlangt zusätzlich phi zwischen 0 und 1.

## Anwendung im Trading

- Stationäre Gleichgewichtsmodelle brauchen etwas Gedächtnis, um zu beurteilen, wie weit der Preis vom langfristigen Erwartungswert abgedriftet ist, bevor eine Prognose entsteht.
- Die Fixed-Width-Reihe zum kleinsten d mit ADF-p-Wert unter 5 Prozent wird als prognostisches Feature empfohlen.
- Die so gewählte Fixed-Width-Reihe soll als prognostisches Feature verwendet werden.

## Regeln und Kriterien

- In den Beispielen liegt der kritische Wert des ADF-Tests bei 95 Prozent Konfidenz bei minus 2,8623.
- Als Schwelle für das minimale d dient ein ADF-p-Wert unter 5 Prozent.
- Die Auswahlregel für d ist ein ADF-p-Wert unter 5 Prozent.
- Die SADF-Null Beta kleiner oder gleich 0 umfasst den nicht-explosiven Bereich, die Alternative ist Beta größer als 0.
- Fertige stationäre Reihen öffentlich gehandelter Assets sind selten; stationäre Portfolios lassen sich aus kointegrierenden, einzeln nichtstationären Reihen herstellen.
- Eine Stichprobe auf Intraday-Frequenz erhöht die Signifikanz des ADF-Tests nicht.
- Im praktischen Handel kann eine Reihe auch dann mit Mean Reversion gehandelt werden, wenn die 90-Prozent-Sicherheit des Stationaritätstests fehlt, solange die Halbwertszeit für den Horizont kurz genug ist.
- Hat die Reihe den Stationaritätstest bestanden oder ist die Halbwertszeit kurz genug, lässt sich schließlich eine profitable Strategie finden, möglicherweise nicht die gebacktestete.

## Risiken und Grenzen

- Ganzzahlige Differenzierung mit d gleich 1 entfernt in den untersuchten Log-Preis-Reihen mehr Gedächtnis, als für die üblichen ökonometrischen Annahmen nötig ist.
- Das Expanding Window erzeugt einen negativen Drift, der auch nach Kontrolle des Gewichtsverlusts erheblich bleibt, weil jede Schätzung auf einem weiter wachsenden Fenster beruht.
- Auch eine stationäre Reihe mit Hurst-Exponent zwischen 0 und 0,5 hat eine mit der Zeit steigende Varianz, nur langsamer als ein geometrischer Random Walk.
- Auch eine Reihe, die auf kurzer Frist mean-reverting wirkt, muss nicht im strengen Sinn stationär sein; gleitender Durchschnitt, gleitende Standardabweichung oder ein Verhältnis passen die Schwellen dann an das wandernde Niveau an.

## Beispiele

- Bei den täglich heruntergebrochenen Log-Preisen der E-mini-S&P-500-Futures, fortgeschrieben mit dem ETF-Trick, hat die Originalreihe eine ADF-Statistik von minus 0,3387 und die Renditenreihe eine von minus 46,9114.
- Die ADF-Statistik unterschreitet den kritischen Wert minus 2,8623 in der Nähe von d gleich 0,35. Dort beträgt die Korrelation zur Originalreihe noch 0,995, während sie zwischen Originalreihe und Renditen nur 0,03 beträgt.
- Trade-Bars dieser Futures der Größe 10.000, fraktional differenziert mit d gleich 0,4, zeigen ohne Gewichtsverlustkontrolle einen extremen negativen Drift, mit Expanding Window und Toleranz 0,01 einen gemäßigten Drift und mit festem Fenster bei Toleranz 10 hoch minus 5 eine driftfreie Reihe.
- Bei Orangensaft (JO1 Comdty) und Lebendrind (LC1 Comdty) war nach dem Text gar keine Differenzierung nötig.
- USD.CAD sieht nicht stationär aus; die ADF-Statistik von etwa minus 1,84 verwirft die Null auf 90 Prozent nicht, der kritische Wert ist minus 2,594, der Hurst-Exponent ist 0,49, und der Variance-Ratio-Test lässt den Random Walk mit pValue 0,367281 zu.
- Das Regressionsresiduum von EWC minus Hedge Ratio mal EWA sieht sehr stationär aus, und der CADF-Test verwirft die Null auf 95 Prozent.
- Der erste Johansen-Eigenvektor von EWA, EWC und IGE bildet ein stationäres Portfolio mit 23 Tagen Halbwertszeit, gegenüber etwa 115 Tagen bei USD.CAD.
- Das mit dem besten Eigenvektor gebildete Portfolio aus EWA, EWC und IGE ist die Grundlage der linearen Strategie und hat 23 Tage Halbwertszeit, gegenüber 115 Tagen bei USD.CAD.
- Der Preis-Spread von USO und GLD mit täglicher Hedge Ratio sieht sehr stationär aus, obwohl GLD und USO nicht kointegriert sind.
- Das Verhältnis USO zu GLD sieht daneben nicht stationär aus, und die lineare Strategie darauf hat eine negative APR.
- Das Verhältnis zweier Preise ist nur im Sonderfall betragsgleicher Hedge Ratios stationär; im Beispiel 10 zu 5 gegen 100 zu 50 bleibt das Verhältnis 2, während der Spread von 5 auf 50 steigt.

## Unterschiedliche Quellenpositionen

- Fast die ganze Literatur macht nichtstationäre Reihen per ganzzahliger Transformation stationär, wie bei Hamilton 1994. Der Text fragt, warum gerade die Ordnung 1 optimal sein soll und ob Überdifferenzierung die Literatur zur Effizienzmarkthypothese hin verzerrt.
- Hosking verallgemeinert 1981 ARIMA auf eine bruchweise Differenzenordnung. Solche Prozesse zeigen langfristige Persistenz und Antipersistenz und sollen gegenüber dem üblichen ARIMA besser prognostizieren.
- Hosking hält fest, dass fraktionale Differenzierung in der Zeitreihenanalyse zuvor, abgesehen von einem Hinweis bei Granger 1978, nicht vorkam. Danach zählt der Text acht Aufsätze von neun Autoren, meist zu technischen Fragen wie schnellen Algorithmen.
- Box-Jenkins: Renditen sind stationär, aber ohne Gedächtnis. Engle-Granger: Log-Preise haben Gedächtnis, sind aber nicht stationär; Kointegration erhält das Gedächtnis, lässt aber nur wenige Variablen zu, und die Vektoren sind instabil.
- Gegenüber Box-Jenkins und Engle-Granger hält der Text fest, dass Stationarität und Gedächtnis nicht gegeneinander aufgegeben werden müssen und dass Kointegration für ML-Prognosen nicht erforderlich ist.
- Stationär bedeutet im Schlusskapitel, dass die Wahrscheinlichkeitsverteilung der Preise über die ganze Zeit unverändert bleibt, und ist ausdrücklich ein anderer Sinn als die Stationarität von Zeitreihen in Kapitel 2.
- Stationär heißt hier, dass die Wahrscheinlichkeitsverteilung der Preise über die Zeit unverändert bleibt, und unterscheidet sich von der Stationarität von Zeitreihen in Kapitel 2.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 96–115 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-006-p096-p115|S. 96–115]]
- Advances in Financial Machine Learning.pdf, S. 115–134 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-007-p115-p134|S. 115–134]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 20–39 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-002-p020-p039|S. 20–39]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 172–191 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-010-p172-p191|S. 172–191]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 248–267 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-014-p248-p267|S. 248–267]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 305–324 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-017-p305-p324|S. 305–324]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 400–419 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-022-p400-p419|S. 400–419]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 419–438 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-023-p419-p438|S. 419–438]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 476–495 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-026-p476-p495|S. 476–495]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]

## Verwandte Themen
