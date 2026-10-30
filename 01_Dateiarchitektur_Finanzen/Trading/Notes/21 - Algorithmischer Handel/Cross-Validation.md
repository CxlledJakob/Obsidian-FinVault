---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Validierung"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Cross-Validation


## Kurzdefinition

- Cross-Validation soll den Generalisierungsfehler eines ML-Algorithmus bestimmen, damit Overfitting erkannt wird.
- Sie teilt Beobachtungen aus einem unabhängig und identisch verteilten Prozess in Training und Test, und jede Beobachtung gehört genau einem der beiden Sets an.
- Grid-Search-Cross-Validation sucht erschöpfend die Parameterkombination, die die CV-Leistung nach einer vom Nutzer festgelegten Score-Funktion maximiert.
- Beim Backtesting durch Cross-Validation werden T Beobachtungen ohne Umsortieren in N Gruppen geteilt.

## Kernaussagen

- Wer auf denselben Daten trainiert und testet, erhält eine sehr hohe Treue ohne Prognosekraft. Der Text vergleicht das mit verlustbehafteter Kompression.
- Beim k-Fold-CV wird der Datensatz in k Teile geteilt. Für jeden Teil wird auf allen übrigen trainiert und auf diesem Teil getestet; heraus kommt ein Vektor mit k Leistungsmaßen.
- Ein binärer Klassifikator gilt als lernend, wenn die kreuzvalidierte Genauigkeit über ein halb liegt, also über dem fairen Münzwurf.
- In der Finanzanwendung wird CV für die Modellentwicklung, etwa das Hyperparameter-Tuning, und für das Backtesting genutzt.
- Übliche ML-Technik scheitert hier: Overfitting tritt ein, die CV erkennt es nicht, und über das Hyperparameter-Tuning trägt sie selbst zum Overfitting bei.
- k-Fold-CV scheitert in Finance aus zwei Gründen. Die Beobachtungen dürfen nicht als unabhängig und identisch verteilt gelten, und das Testset wird bei der Modellentwicklung mehrfach benutzt, was Multiple Testing und Selection Bias erzeugt.
- Leakage liegt vor, wenn das Training Information enthält, die auch im Test steht. Bei seriell korrelierten Features und überlappenden Labels sind benachbarte Merkmale und benachbarte Labels jeweils ähnlich, und die Trennung von t und t plus 1 lässt Information hinüber.
- Ein Klassifikator, der zuerst auf dem einen Paar trainiert und dann das nächste Label schätzt, trifft dieses leichter, selbst wenn das Feature irrelevant ist.
- Ist das Feature wirklich prognostisch, verstärkt Leakage eine bereits wertvolle Strategie. Bei irrelevanten Features erzeugt es Fehlentdeckungen.
- Für Leakage müssen Feature und Label gemeinsam ähnlich sein. Ähnlichkeit nur der Features oder nur der Labels genügt nicht.
- Tritt Leakage auf, steigt die gemessene Leistung schon dadurch, dass die Zahl der Folds gegen die Zahl der Bars geht, weil dann mehr überlappende Beobachtungen im Training bleiben.
- Purging nennt der Text das Streichen von Trainingsbeobachtungen, deren Labels zeitlich mit Testlabels überlappen. Embargo nennt er das Streichen von Trainingsbeobachtungen, die unmittelbar auf ein Testset folgen.
- K-Fold-Cross-Validation scheitert in Finanzanwendungen unter anderem deshalb, weil Information aus dem Testset in das Trainingsset leckt.
- Die Cross-Validation einer der verbreitetsten ML-Bibliotheken ist nicht fehlerfrei umgesetzt, und deshalb muss der ausgeführte Code gelesen werden.
- Hyperparameter-Tuning ist ein notwendiger Schritt beim Fitten eines ML-Algorithmus; ohne saubere Durchführung überfittet der Algorithmus wahrscheinlich, und die Live-Leistung enttäuscht.
- Die ML-Literatur legt besonderen Wert darauf, jeden getunten Hyperparameter per Cross-Validation zu prüfen.
- Cross-Validation in der Finanzwelt ist besonders schwierig, und Lösungen aus anderen Feldern scheitern dort wahrscheinlich.
- Kapitel 9 stimmt Hyperparameter mit der gepurgten k-Fold-CV ab.
- Weiß man wenig über die zugrunde liegende Datenstruktur, ist die Grid Search ein vernünftiger erster Ansatz.
- sklearn hat diese Logik in GridSearchCV umgesetzt, und die Funktion akzeptiert einen CV-Generator als Argument.
- GridSearchCV muss die Klasse PurgedKFold erhalten, damit der Schätzer nicht auf geleakte Information überfittet.
- Bei einer großen Zahl von Parametern wird eine Grid-Search-CV rechnerisch unhandlich.
- Eine Alternative mit guten statistischen Eigenschaften ist, jeden Parameter aus einer Verteilung zu ziehen, nach Bergstra et al. 2011 und Bergstra und Bengio 2012.
- Das begrenzt die Zahl der gesuchten Kombinationen unabhängig von der Dimension und entspricht damit einem Rechenbudget.
- Parameter, die für die Leistung relativ unerheblich sind, verlängern die Suchzeit dann nicht wesentlich, anders als bei der Grid-Search-CV.
- Der Autor definiert die Log-Gleichverteilung, weil er sie in der Literatur nicht gefunden hat.
- Serielle Bedingtheit der Labels macht die gewöhnliche k-Fold-Cross-Validation unbrauchbar, weil die Zufallsziehung redundante Beobachtungen auf Trainings- und Testset verteilt.
- Es braucht ein anderes, wirklich out-of-sample Validierungsverfahren, das das Modell an den Beobachtungen bewertet, die am wenigsten mit den Trainingsbeobachtungen korreliert oder redundant sind.
- Scikit-learn hat eine Walk-Forward-Timefolds-Methode umgesetzt, bei der der Test in der Zeit vorwärts rückt, um Leakage zu verhindern.
- Das Ziel eines Backtests durch Cross-Validation ist nicht eine historisch genaue Performance, sondern künftige Leistung aus einer Reihe von Out-of-Sample-Szenarien zu erschließen.
- Für jeden Zeitraum des Backtests wird die Leistung eines Klassifikators simuliert, der alles außer diesem Zeitraum kannte.
- Die combinatorial purged cross-validation erzeugt die Kombinationen von Trainings- und Testsets, die für eine gewünschte Zahl von Backtest-Pfaden nötig sind, und purgt Trainingsbeobachtungen mit geleakter Information.
- Bailey et al. 2017a schätzen die Probability of Backtest Overfitting mit der combinatorially symmetric cross-validation.
- Der CV-Test ist nicht das Ergebnis eines einzelnen historischen Szenarios, denn es werden k alternative Szenarien geprüft, von denen nur eines der historischen Folge entspricht.
- Jede Entscheidung beruht auf Mengen gleicher Größe, sodass die Ergebnisse über die Zeiträume nach der Menge der verwendeten Information vergleichbar sind.
- Jede Beobachtung gehört zu genau einem Testset; es gibt kein Aufwärm-Subset, und dadurch wird die längstmögliche Out-of-Sample-Simulation erreicht.
- Cross-Validation trainiert jeden Klassifikator auf gleich großen und großen Teilen der Stichprobe.
- Cross-Validation begegnet der Varianzquelle des Walk-Forward, bei der ein großer Teil der Entscheidungen auf einem kleinen Teil der Daten beruht.
- Cross-Validation erzeugt weniger Fehlentdeckungen als Walk-Forward.
- Die Sharpe Ratio einer Strategie wird weiterhin aus einem einzigen Pfad geschätzt und kann stark schwanken.
- Für k gleich 1 entsteht genau ein Pfad, und die kombinatorische purged Cross-Validation fällt dann mit der gewöhnlichen Cross-Validation zusammen.
- Für k größer als 1 verallgemeinert die kombinatorische purged Cross-Validation die gewöhnliche Cross-Validation.

## Funktionsweise

- Abbildung 7.1 zeigt die Trainings- und Testaufteilungen einer 5-Fold-CV.
- Zwei Wege gegen Leakage: jede Trainingsbeobachtung streichen, deren Label von Information abhängt, die auch ein Testlabel bestimmt, und den Klassifikator nicht überanpassen.
- Zum zweiten Weg gehören frühes Stoppen der Basisschätzer sowie Bagging, das Oversampling redundanter Beispiele begrenzt, damit die einzelnen Klassifikatoren möglichst verschieden bleiben.
- Scoring-Funktionen kennen das Attribut classes_ nicht, weil sklearn auf NumPy-Arrays statt auf pandas-Serien setzt; das ist scikit-learn-Issue 6231.
- cross_val_score liefert abweichende Ergebnisse, weil Gewichte an die Fit-Methode, nicht aber an log_loss übergeben werden; das ist scikit-learn-Issue 9144.
- Bis zu einer Korrektur dieser Fehler soll die Funktion cvScore aus Snippet 7.4 verwendet und cross_val_score vermieden werden.
- In clfHyperFit wird bei Labels, deren Werte genau die Menge {0, 1} sind, der Score f1 verwendet, sonst neg_log_loss.
- f1 gilt dort für Meta-Labeling, neg_log_loss ist symmetrisch gegenüber allen Fällen.
- Die Suche läuft auf den Trainingsdaten mit einem inneren PurgedKFold; danach wird das validierte Modell auf dem gesamten Datensatz gefittet.
- Dieselbe Funktion kann den getunten Schätzer zusätzlich baggen, und Bagging ist aus den in Kapitel 6 genannten Gründen grundsätzlich sinnvoll.
- Ist rndSearchIter gleich 0, wird GridSearchCV verwendet, sonst RandomizedSearchCV mit dieser Iterationszahl.
- Eine Zufallsvariable x ist zwischen a > 0 und b > a genau dann log-gleichverteilt, wenn log(x) auf dem Intervall von log(a) bis log(b) gleichverteilt ist.
- Die Verteilungsfunktion lautet (log x − log a) / (log b − log a) für x zwischen a und b, ist 0 unterhalb von a und 1 oberhalb von b.
- Die Dichte lautet 1 / (x log(b/a)) für x zwischen a und b und ist sonst 0.
- Die Verteilungsfunktion hängt nicht von der Basis des Logarithmus ab, weil sich die Basis in Zähler und Nenner kürzt.
- Log Loss, auch Cross-Entropy-Loss, ist die Log-Likelihood des Klassifikators gegeben das wahre Label und berücksichtigt die vorhergesagten Wahrscheinlichkeiten.
- Die Schätzung lautet L[Y, P] = −N⁻¹ mal die Doppelsumme von yn,k log(pn,k), wobei pn,k die Wahrscheinlichkeit der Vorhersage n für Label k ist.
- Y ist eine 1-aus-K-Indikatormatrix, in der yn,k gleich 1 ist, wenn Beobachtung n das Label k trägt, und sonst 0.
- Wird Log Loss als Score verwendet, dreht man oft das Vorzeichen und spricht von neg_log_loss, damit ein höherer Wert wie bei der Accuracy besser ist; der Grund ist kosmetisch.
- Die fit-Methode von sklearns Pipeline erwartet kein Argument sample_weight, sondern das Schlüsselwortargument fit_params; der Fehler ist auf GitHub gemeldet.
- MyPipeline überschreibt fit so, dass ein übergebenes sample_weight an den letzten Pipeline-Schritt unter dessen Namen mit dem Suffix __sample_weight weitergereicht wird.
- Zuerst wird eine Matrix M aus den Performancereihen von N Versuchen gebildet; jede Spalte ist der PnL über t = 1 bis T für eine vom Forscher probierte Modellkonfiguration, und M hat die Ordnung T mal N.
- M muss eine echte Matrix mit gleich vielen Zeilen je Spalte sein, und die Beobachtungen sind in jeder Zeile über alle N Versuche synchron.
- Die Metrik, mit der die optimale Strategie gewählt wird, muss sich auf Teilstichproben jeder Spalte schätzen lassen.
- Ist diese Metrik die Sharpe Ratio, wird angenommen, dass die Annahme unabhängig identisch normalverteilter Werte auf verschiedenen Schnitten der berichteten Performance hält.
- Handeln die Modellkonfigurationen mit unterschiedlicher Frequenz, werden die Beobachtungen auf einen gemeinsamen Index t = 1 bis T aggregiert.
- M wird zeilenweise in eine gerade Zahl S disjunkter Teilmatrizen gleicher Dimension zerlegt; jede Teilmatrix hat die Ordnung T/S mal N.
- Es werden alle Kombinationen dieser Teilmatrizen in Gruppen der Größe S/2 gebildet; ihre Anzahl ist der Binomialkoeffizient S über S/2.
- Für S = 16 nennt der Text 12.780 Kombinationen, und jede Kombination besteht aus S/2 Teilmatrizen.
- Für jede Kombination wird das Trainingsset durch Zusammenfügen ihrer S/2 Teilmatrizen gebildet und hat die Ordnung T/2 mal N; das Testset ist das Komplement in M und hat dieselbe Ordnung.
- Aus den Spalten des Trainingssets wird ein Performancevektor gebildet, und n* ist die Spalte mit der maximalen Performance.
- Aus den Spalten des Testsets wird ebenfalls ein Performancevektor gebildet, und der relative Rang der in-sample gewählten Spalte in diesem Vektor liegt in (0, 1).
- Ohne Overfitting sollte die in-sample beste Variante out-of-sample systematisch besser abschneiden als die übrigen, so wie sie es in-sample tat.
- Der Logit dieses relativen Rangs ist der Logarithmus von Rang geteilt durch 1 minus Rang und ist 0, wenn die in-sample beste Variante dem Median der Out-of-Sample-Performances entspricht.
- Hohe Logits bedeuten Übereinstimmung von In-Sample- und Out-of-Sample-Leistung und damit ein geringes Maß an Backtest-Overfitting.
- Die Verteilung der Out-of-Sample-Ränge entsteht, indem alle diese Logits gesammelt werden; ihre Dichte ist die relative Häufigkeit und integriert sich zu 1.
- Die Probability of Backtest Overfitting ist das Integral dieser Dichte von minus unendlich bis 0, also die Wahrscheinlichkeit, dass in-sample optimale Strategien out-of-sample unter dem Median liegen.
- Die Beobachtungen in jeder Teilmenge behalten die ursprüngliche Zeitfolge; die Zufallsziehung erfolgt auf den relativ unkorrelierten Teilmengen, nicht auf den einzelnen Beobachtungen.
- Die ersten N minus 1 Gruppen haben die Länge des nach unten gerundeten Quotienten T/N, und die letzte Gruppe enthält den Rest.
- Für eine Testmenge aus k Gruppen ist die Zahl der Aufteilungen der Binomialkoeffizient aus N und N minus k.
- Jede Gruppe kommt in gleich vielen Trainingsmengen und in gleich vielen Testmengen vor.
- Der Trainingsanteil beträgt 1 minus k/N.
- Der Trainingsanteil steigt, wenn N gegen T geht, und er fällt, wenn k gegen N/2 geht.

## Voraussetzungen

- Ein Trainingsanteil unter einem Halb ist theoretisch möglich, praktisch wird k aber höchstens als N/2 angesetzt.

## Anwendung im Trading

- Der Text beschränkt sich hier auf CV für die Modellentwicklung. Backtesting wird als eigenes, später in den Kapiteln 10 bis 16 behandeltes Thema genannt.
- Für das Tuning der Hyperparameter einer Investmentstrategie soll neg_log_loss statt Accuracy verwendet werden.
- Accuracy bewertet eine falsche Kaufprognose mit hoher Wahrscheinlichkeit genauso wie eine mit niedriger Wahrscheinlichkeit und kann einen Fehlschuss mit hoher Wahrscheinlichkeit durch einen Treffer mit niedriger Wahrscheinlichkeit ausgleichen.
- Strategien verdienen daran, das richtige Label mit hoher Konfidenz zu treffen; Gewinne aus guten Prognosen mit niedriger Konfidenz gleichen Verluste aus schlechten Prognosen mit hoher Konfidenz nicht aus.
- Die Cross-Validation bewertet den Klassifikator mit Sample-Gewichten, und diese Gewichte wurden als Funktion des absoluten Returns der Beobachtung bestimmt.
- Sample-gewichteter Cross-Entropy-Loss schätzt die Leistung mit dem richtigen Label für die Seite, der Wahrscheinlichkeit für die Positionsgröße und dem Gewicht für Return beziehungsweise Ausgang und ist damit die passende Metrik für Finanzanwendungen, nicht Accuracy.

## Regeln und Kriterien

- Die kreuzvalidierte Genauigkeit eines binären Klassifikators soll über ein halb liegen.
- Bei redundanten Beobachtungen wird StratifiedKFold ohne Shuffle vor der Partition empfohlen, und die Out-of-Bag-Genauigkeit wird ignoriert.
- max_samples wird auf die mittlere Eindeutigkeit gesetzt, zusätzlich kann der sequenzielle Bootstrap aus Kapitel 4 verwendet werden.
- Labels sollen keine überlappenden Zeiträume gemeinsam haben, wenn eine Beobachtung im Training und die andere im Test liegt.
- Im Meta-Labeling soll der Score f1 verwendet werden.
- Ein Klassifikator, der bei sehr vielen negativen Fällen stets negativ vorhersagt, erreicht hohe Accuracy oder hohen neg_log_loss, ohne aus den Features zwischen den Fällen zu unterscheiden; Recall ist dann null und Precision undefiniert.
- Der f1-Score korrigiert diese aufgeblähte Leistung, indem er den Klassifikator über Precision und Recall bewertet.
- Außerhalb des Meta-Labelings sind Accuracy oder neg_log_loss vertretbar, weil alle Fälle gleichermaßen interessieren.
- Eine Umbeschriftung der Fälle ändert Accuracy und neg_log_loss nicht, wohl aber f1.
- Beim Score neg_log_loss bleibt der sklearn-Fehler aus Issue 9144 zu beachten; als Umgehung dient die Funktion cvScore aus Kapitel 7.

## Risiken und Grenzen

- Auf Finanzdaten erkennt die übliche Cross-Validation Overfitting nicht und kann es durch Hyperparameter-Tuning verstärken.
- Die zweite Fehlerursache, die mehrfache Nutzung des Testsets mit Selection Bias, wird in diesem Kapitel nur benannt und auf die Kapitel 11 bis 13 verschoben.
- Wer eintausend Konfigurationen derselben Investmentstrategie per Cross-Validation prüft, erhält allein durch Zufall einige gut aussehende Ergebnisse.
- Werden nur diese positiven Ergebnisse veröffentlicht und der Rest verborgen, kann das Publikum nicht erkennen, dass es sich um falsch positive Zufallstreffer handelt; dieses Phänomen heißt Selection Bias.
- Die Behebung des Pipeline-Fehlers kann dauern, weil dafür viel Funktionalität umgeschrieben und getestet werden muss.
- Wie beim Walk-Forward wird nur ein einzelner Backtest-Pfad simuliert, wenn auch nicht der historische, und je Beobachtung entsteht genau eine Prognose.
- Die Cross-Validation hat keine klare historische Deutung: Das Ergebnis simuliert nicht, wie die Strategie in der Vergangenheit gelaufen wäre, sondern wie sie künftig unter verschiedenen Stressszenarien abschneiden kann.
- Weil das Trainingsset dem Testset nicht nachläuft, ist Leakage möglich, und Purging sowie Embargo aus Kapitel 7 sollen verhindern, dass Testinformation ins Training gelangt.
- Ein Nachteil des Walk-Forward ist, dass er sich leicht überfitten lässt, weil es ohne Zufallsziehung nur einen Testpfad gibt, der wiederholt werden kann, bis ein falsch positives Ergebnis erscheint.
- Wie bei der gewöhnlichen Cross-Validation ist etwas Zufall nötig, um dieses Performance-Targeting zu vermeiden, ohne Beispiele in den Test zu lassen, die mit dem Trainingsset korreliert sind.

## Beispiele

- Liegen t und t plus 1 wegen serieller Korrelation und überlappender Labels in verschiedenen Sets, kann ein irrelevantes Feature im Test trotzdem treffend wirken, weil beide Zeitpunkte nahezu dieselbe Information tragen.
- Parameter wie C in der SVC und gamma im RBF-Kernel akzeptieren nur nichtnegative Werte.
- Zieht man C gleichverteilt aus dem Intervall von 0 bis 100, liegen erwartungsgemäß 99 % der Werte über 1.
- Eine SVC kann auf einen Anstieg von C von 0,01 auf 1 ebenso reagieren wie auf einen Anstieg von 1 auf 100, deshalb ist die Ziehung aus der Gleichverteilung U[0, 100] ineffizient.
- Snippet 9.4 testet die Log-Gleichverteilung auf dem Intervall von 1E−3 bis 1E3, und Abbildung 9.1 zeigt die Gleichverteilung der Stichprobe auf der Log-Skala.
- Sagt ein Klassifikator zwei Einsen voraus, obwohl die wahren Labels 1 und 0 sind, beträgt die Accuracy 50 %, während der Log Loss groß wird, wenn der Fehlschuss mit hoher Wahrscheinlichkeit erfolgt; Abbildung 9.2 variiert diese Wahrscheinlichkeiten von 0,5 bis 0,9.
- Ein Klassifikator kann auf dem 1. Januar 2009 bis 1. Januar 2017 trainiert und auf dem 1. Januar 2008 bis 31. Dezember 2008 getestet werden; die Leistung für 2008 ist historisch nicht korrekt, weil das Training Daten nutzt, die erst nach 2008 verfügbar waren.
- Historische Genauigkeit war in diesem Beispiel nicht das Ziel; die Strategie sollte einem Stressszenario wie 2008 ausgesetzt werden, ohne 2008 gekannt zu haben.
- Abbildung 11.1 zeigt einen starken und anhaltenden Leistungsabfall durch Backtest-Overfitting, und Abbildung 11.2 die daraus abgeleitete Probability of Backtest Overfitting.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 115–134 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-007-p115-p134|S. 115–134]]
- Advances in Financial Machine Learning.pdf, S. 134–153 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-008-p134-p153|S. 134–153]]
- Advances in Financial Machine Learning.pdf, S. 153–172 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-009-p153-p172|S. 153–172]]
- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]

## Verwandte Themen
