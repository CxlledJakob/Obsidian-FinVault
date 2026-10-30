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

## Funktionsweise

- Die Gewichte beginnen bei 1 und entstehen iterativ, indem das vorige Gewicht mit minus (d minus k plus 1) durch k multipliziert wird.
- Beim Expanding Window hängt der relative Gewichtsverlust vom Tempo ab, mit dem die Gewichte gegen null laufen. Zu einer Toleranz wird der Anfang verworfen, dessen Gewichtsverlust die Schwelle überschreitet.
- Bei d gleich 1 genügt es, den ersten Punkt zu streichen. Geht d gegen 0, wird dieser zu verwerfende Vorspann länger.
- Der negative Drift dieses Fensters kommt von negativen Gewichten, die mit der Verbreiterung auf die frühen Beobachtungen gelegt werden. Ohne Kontrolle des Gewichtsverlusts bleibt im Wesentlichen nur dieser Trend sichtbar; mit Kontrolle ist der Drift schwächer, aber immer noch erheblich.
- Das feste Fenster schneidet Gewichte ab, sobald ihr Betrag unter eine Schwelle fällt, und verwendet für alle Zeitpunkte denselben Gewichtsvektor.
- Das Ergebnis ist eine driftfreie Mischung aus Niveau und Rauschen. Wegen Schiefe und Excess-Kurtosis aus dem Gedächtnis ist die Verteilung nicht mehr gaußsch, aber stationär.
- Praktisch wird erst die kumulative Summe gebildet, damit eine Differenzierung nötig ist, dann die Fixed-Width-Reihe für mehrere d zwischen 0 und 1 berechnet und das kleinste d gewählt, dessen ADF-p-Wert unter 5 Prozent liegt.
- Zuerst wird die kumulative Summe gebildet, damit überhaupt eine Differenzierung nötig ist. Dann wird die Fixed-Width-Reihe für mehrere d zwischen 0 und 1 berechnet, und es wird das kleinste d gewählt, bei dem der p-Wert der ADF-Statistik unter 5 Prozent fällt.

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

## Risiken und Grenzen

- Ganzzahlige Differenzierung mit d gleich 1 entfernt in den untersuchten Log-Preis-Reihen mehr Gedächtnis, als für die üblichen ökonometrischen Annahmen nötig ist.
- Das Expanding Window erzeugt einen negativen Drift, der auch nach Kontrolle des Gewichtsverlusts erheblich bleibt, weil jede Schätzung auf einem weiter wachsenden Fenster beruht.

## Beispiele

- Bei den täglich heruntergebrochenen Log-Preisen der E-mini-S&P-500-Futures, fortgeschrieben mit dem ETF-Trick, hat die Originalreihe eine ADF-Statistik von minus 0,3387 und die Renditenreihe eine von minus 46,9114.
- Die ADF-Statistik unterschreitet den kritischen Wert minus 2,8623 in der Nähe von d gleich 0,35. Dort beträgt die Korrelation zur Originalreihe noch 0,995, während sie zwischen Originalreihe und Renditen nur 0,03 beträgt.
- Trade-Bars dieser Futures der Größe 10.000, fraktional differenziert mit d gleich 0,4, zeigen ohne Gewichtsverlustkontrolle einen extremen negativen Drift, mit Expanding Window und Toleranz 0,01 einen gemäßigten Drift und mit festem Fenster bei Toleranz 10 hoch minus 5 eine driftfreie Reihe.
- Bei Orangensaft (JO1 Comdty) und Lebendrind (LC1 Comdty) war nach dem Text gar keine Differenzierung nötig.

## Unterschiedliche Quellenpositionen

- Fast die ganze Literatur macht nichtstationäre Reihen per ganzzahliger Transformation stationär, wie bei Hamilton 1994. Der Text fragt, warum gerade die Ordnung 1 optimal sein soll und ob Überdifferenzierung die Literatur zur Effizienzmarkthypothese hin verzerrt.
- Hosking verallgemeinert 1981 ARIMA auf eine bruchweise Differenzenordnung. Solche Prozesse zeigen langfristige Persistenz und Antipersistenz und sollen gegenüber dem üblichen ARIMA besser prognostizieren.
- Hosking hält fest, dass fraktionale Differenzierung in der Zeitreihenanalyse zuvor, abgesehen von einem Hinweis bei Granger 1978, nicht vorkam. Danach zählt der Text acht Aufsätze von neun Autoren, meist zu technischen Fragen wie schnellen Algorithmen.
- Box-Jenkins: Renditen sind stationär, aber ohne Gedächtnis. Engle-Granger: Log-Preise haben Gedächtnis, sind aber nicht stationär; Kointegration erhält das Gedächtnis, lässt aber nur wenige Variablen zu, und die Vektoren sind instabil.
- Gegenüber Box-Jenkins und Engle-Granger hält der Text fest, dass Stationarität und Gedächtnis nicht gegeneinander aufgegeben werden müssen und dass Kointegration für ML-Prognosen nicht erforderlich ist.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 96–115 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-006-p096-p115|S. 96–115]]
- Advances in Financial Machine Learning.pdf, S. 115–134 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-007-p115-p134|S. 115–134]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]

## Verwandte Themen
