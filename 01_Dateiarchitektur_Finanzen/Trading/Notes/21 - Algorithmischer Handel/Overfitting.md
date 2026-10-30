---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Validierung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Overfitting


## Kurzdefinition

- Overfitting erzeugt vielversprechende Ergebnisse, die sich nicht liefern lassen.
- Overfitting führt zu vielversprechenden Ergebnissen, die sich nicht liefern lassen.
- Overfitting ist der Varianzfehler: Das Modell hat das Trainingsset überangepasst, kleine Änderungen der Trainingsdaten ändern die Prognosen stark, und Rauschen wird als Signal genommen.
- Underfitting ist der zugehörige Biasfehler aus unrealistischen Annahmen, sodass wichtige Beziehungen zwischen Features und Outcomes unerkannt bleiben.
- Backtest-Overfitting lässt sich als Selection Bias auf mehreren Backtests definieren.
- Backtest-Overfitting liegt vor, wenn eine Strategie so entwickelt wird, dass sie auf einem Backtest gut abschneidet, indem sie zufällige historische Muster versilbert.
- Eine Handelsregel ist überangepasst, wenn die erwartete Out-of-Sample-Sharpe-Ratio der in-sample besten Regel unter dem Median der alternativen Regeln liegt.

## Kernaussagen

- Standardverfahren der Kreuzvalidierung versagen in der Finanzwelt.
- Die meisten Entdeckungen in der Finanzwelt sind falsch, wegen Mehrfachtests und Selektionsverzerrung.
- Es gibt drei Backtesting-Paradigmen, von denen die historische Simulation nur eines ist.
- Jeder Backtest ist immer in gewissem Maße überangepasst.
- Das Ausmaß dieser Überanpassung muss quantifiziert werden.
- Die Allokation darf In-Sample-Signale nicht zulasten der Out-of-Sample-Performance überanpassen.
- Die Branche bezahlt nur für Out-of-Sample-Renditen.
- Backtest-Overfitting gehört zu den Hindernissen, die Finanzanwendungen für Machine Learning besonders schwierig machen.
- Wissentlich betrieben ist Overfitting wissenschaftlicher Betrug.
- Backtest-Overfitting ist das wichtigste offene Problem der mathematischen Finanzwelt und das Gegenstück zu P versus NP.
- Mit einem präzisen Verfahren zur Verhinderung wäre ein Backtest fast so gut wie Bargeld und kein Verkaufsargument.
- Hedgefonds könnten Managern dann vertrauensvoll Mittel zuweisen, Anleger weniger Risiko tragen und höhere Gebühren zahlen, und Aufsichten Lizenzen anhand belastbarer Nachweise von Können erteilen.
- Die empirischen Grundlagen von CAPM, APT, Allokationsverfahren und Risikomanagement wurden ausgewählt, ohne die Wahrscheinlichkeiten falscher Entdeckungen zu bestimmen.
- Als Gegenmittel nennt das Buch Backtests auf synthetischen Daten und die deflated Sharpe Ratio.
- Allokationsverfahren sollen In-Sample-Signale nicht auf Kosten der Out-of-Sample-Performance überanpassen.
- Ein Backtest mit annualisiertem Sharpe Ratio über 2 bei 95 Prozent Konfidenz ist laut Übung trotzdem wahrscheinlich falsch, auch wenn er auf demselben Datensatz unabhängig reproduziert wird.
- Entscheidungsbäume neigen zum Overfitting und erhöhen damit die Prognosevarianz. Der Random Forest wurde gebaut, um Ensemble-Prognosen mit niedrigerer Varianz zu erzeugen.
- Bagging senkt die Prognosevarianz und wirkt damit dem Overfitting entgegen. Der Random Forest tut das ebenfalls, solange die mittlere Korrelation der Bäume unter 1 bleibt, und senkt nicht notwendig den Bias einzelner Bäume.
- Boosting senkt Varianz und Bias, die Biaskorrektur erhöht aber das Overfitting-Risiko.
- Auf Finanzdaten ist Overfitting oft das größere Problem, weil das Signal-Rausch-Verhältnis niedrig ist und sich ein Algorithmus leicht überanpassen lässt. Bagging zielt auf Overfitting, Boosting auf Underfitting.
- Sind viele Stichproben redundant und nicht unabhängig und identisch verteilt, überanpasst auch ein Random Forest: Ziehen mit Zurücklegen erzeugt viele nahezu gleiche, jeweils überangepasste Bäume.
- Anders als allgemeines Bagging ist jede Bootstrap-Stichprobe im Random Forest so groß wie das Trainingsset.
- Cross-Validation soll den Generalisierungsfehler schätzen und Overfitting verhindern. Bei Finanzproblemen tritt Overfitting trotzdem auf, die übliche CV erkennt es nicht und verstärkt es durch Hyperparameter-Tuning.
- Leakage wird entwertet, wenn der Klassifikator nicht überangepasst wird, auch falls noch etwas Information hinüberläuft. Der Text nennt dafür frühes Stoppen und diverses Bagging.
- Selbst wenn eine Support Vector Machine auf einer Million Beobachtungen konvergiert, ist weder ein globales Optimum noch Freiheit von Overfitting garantiert.
- Frühes Stoppen der einzelnen Basisschätzer erhöht deren Varianz. Beim Bagging kann die Varianzreduktion vieler unabhängiger Schätzer diesen Anstieg mehr als ausgleichen.
- Eine PCA vor dem Random Forest kann etwas Overfitting abbauen, weil eine achsennahe Drehung des Merkmalsraums typischerweise weniger Baumebenen braucht.
- Viele erfahrene Portfoliomanager erkennen nicht, wie leicht sich ein Backtest überfitten lässt.
- Overfitting ist ein durchgehendes Risiko des Buches, weil ML-Algorithmen immer ein Muster finden, auch wenn es ein statistischer Zufallstreffer ist.
- Angeblich wichtige Features aus MDI, MDA und SFI sind stets mit Skepsis zu betrachten.
- PCA ordnet Features ohne Kenntnis der Labels und damit ohne Overfitting im Sinne einer Klassifikation.
- Stimmen die von MDI, MDA oder SFI als am wichtigsten gewählten Features mit denen überein, die PCA ohne Labels als prinzipiell einstuft, ist das ein bestätigender Hinweis, dass das gefundene Muster nicht vollständig überfittet ist.
- Wären die Features völlig zufällig, hätte die PCA-Rangfolge keine Entsprechung in der Feature-Importance-Rangfolge.
- Weil diese zufälligen Muster in der Zukunft kaum wieder auftreten, wird die so entwickelte Strategie scheitern.
- Jede backgetestete Strategie ist infolge von Selection Bias in gewissem Maß überfittet, denn die einzigen Backtests, die die meisten Leute teilen, sind die angeblich gewinnenden.
- Wie man Backtest-Overfitting begegnet, ist wohl die grundlegendste Frage der quantitativen Finanzwelt.
- Was die Beurteilung so schwer macht, ist, dass sich die Wahrscheinlichkeit falsch positiver Ergebnisse mit jedem neuen Test auf demselben Datensatz ändert und diese Information dem Forscher unbekannt ist oder Investoren und Gutachtern nicht mitgeteilt wird.
- Es gibt keinen leichten Weg, Overfitting zu verhindern; mehrere Schritte können es mindern.
- Selbst ein fehlerfreier Backtest ist wahrscheinlich eine falsche Entdeckung, weil Fachwissen aus Zehntausenden früherer Backtests entsteht und dieses Ergebnis dann nicht der erste Test auf dem Datensatz ist.
- Je besser man im Backtesten wird, desto wahrscheinlicher tauchen falsche Entdeckungen auf.
- Profis können fehlerfreie Backtests erzeugen und dennoch an Multiple Testing, Selection Bias oder Backtest-Overfitting scheitern.
- Das Modell anhand des Backtests nachzubessern, ist gefährlich; scheitert der Backtest, beginnt man von vorn, und die Chance einer falschen Entdeckung sinkt deutlich, wird aber nicht null.
- Die Probability of Backtest Overfitting wird nach Bailey et al. 2017a über die combinatorially symmetric cross-validation geschätzt.
- Sie ist das Integral der Dichte der Rang-Logits von minus unendlich bis 0 und damit die Wahrscheinlichkeit, dass in-sample optimale Strategien out-of-sample unter dem Median liegen.
- Hohe Logits bedeuten Übereinstimmung von In-Sample- und Out-of-Sample-Leistung und damit geringes Backtest-Overfitting; der Logit ist 0, wenn die in-sample beste Variante dem Out-of-Sample-Median entspricht.
- Wer Ein- und Ausstiegsschwellen an historischen Simulationen kalibriert, trifft einzelne Beobachtungen und bindet die Strategie so an die Vergangenheit, dass sie für die Zukunft ungeeignet wird.
- Ein triviales Overfitting entsteht, wenn ein Paar aus Stop und Gewinnziel nur wenige Ausreißer trifft.
- Overfitting ist schwer zu vermeiden, wenn freie Parameter einzelne In-sample-Beobachtungen treffen können oder die Menge der Alternativen groß ist.
- Die Handelsregel führt solche freien Parameter ein, weil Stop und Gewinnziel unabhängig von der Strategie festgelegt werden können.
- Mit zwei freien Schwellen auf einer Stichprobe der Größe I ist die Sharpe Ratio leicht überangepasst.
- Bei serieller Abhängigkeit der Gewinnänderungen entsteht out of sample eine negative Performance.
- Die Wahrscheinlichkeit von Backtest-Overfitting hilft, überflüssige Strategien zu verwerfen.
- Besser ist es, das Overfitting schon bei der Kalibrierung der Handelsregel zu vermeiden.
- Backtest-Overfitting wird als eines der wichtigsten offenen Probleme der mathematischen Finanzwissenschaft bezeichnet.
- Walk-Forward-Backtests haben eine hohe Varianz, weil wenige Beobachtungen die Sharpe Ratio stark gewichten.
- Die hohe Varianz von Walk-Forward-Backtests erzeugt Fehlentdeckungen, weil die höchste geschätzte Sharpe Ratio gewählt wird, auch wenn der wahre Wert null ist.
- Ohne die Zahl der Versuche lassen sich Family-Wise Error Rate, False Discovery Rate und Probability of Backtest Overfitting nicht bestimmen.
- Die kombinatorische purged Cross-Validation erzeugt weniger Fehlentdeckungen als Cross-Validation und als Walk-Forward.
- Eine historische Kalibrierung auf einem Random Walk wählt eine zufällig günstige Kombination aus Stop und Gewinnziel und ist deshalb Overfitting.
- Erkennt die Simulation kein stabiles Leistungsmuster, wird keine vermeintlich optimale Regel aus einem einzelnen Zufallspfad ausgewählt.
- Nähert sich der Prozess einem Random Walk, verflacht die Performance, und das Optimieren der Handelsregel wird eine Übung in Backtest-Overfitting.
- Die experimentell bestimmte Regel wird aus dem Preisprozess abgeleitet und vermeidet so das Overfitting auf einen einzelnen historischen Pfad.
- Die optimale Regel wird aus den Eigenschaften des zugrunde liegenden Preisprozesses abgeleitet.
- Derselbe Weg lässt sich auf andere Prozesse als den Ornstein-Uhlenbeck-Prozess anwenden, der hier zur Anschauung dient.
- Das Kapitel bestimmt die optimale Handelsregel numerisch und lässt eine geschlossene Lösung offen.
- Weil die Regel numerisch innerhalb weniger Sekunden bestimmt werden kann, besteht wenig praktischer Anreiz für eine geschlossene Form.
- Ein Beweis der Vermutung könnte Jahre oder Jahrzehnte dauern, und alle bisherigen Experimente bestätigen sie empirisch.
- Die Wahrscheinlichkeit, dass die Vermutung falsch ist, ist klein gegenüber der Wahrscheinlichkeit, die Handelsregel durch ihr Ignorieren überanzupassen.
- Die rationale Handlungsweise ist, die Vermutung als zutreffend zu behandeln und die Regel auf synthetischen Daten zu bestimmen.
- Im ungünstigsten Fall bleibt die auf synthetischen Daten bestimmte Regel suboptimal und übertrifft dennoch fast sicher eine überangepasste Regel.
- Einfache und lineare Strategien sind das durchgehende Gegenmittel gegen Overfitting und Data-Snooping-Verzerrungen, die komplexe Strategien oft plagen.
- Viele technische Indikatoren oder Regeln auf eine Preisreihe zu werfen, bis eine davon profitabel aussieht, lädt diese Verzerrung ein. Stattdessen wird die grundlegende Eigenschaft der Reihe in einem einfachen mathematischen Modell gefasst.
- Ein Modell mit wenigen Parametern, aber vielen komplizierten Handelsregeln, ist für die Anpassung an zufällige historische Muster ebenso anfällig wie eines mit vielen Parametern.
- Nichtlineare Modelle sind anfälliger als lineare, weil sie komplizierter sind und gewöhnlich mehr freie Parameter haben.
- Bei einfacher Extrapolation der historischen Preise passt ein nichtlineares Modell die Historie besser an. Das garantiert keine bessere Prognose eines künftigen Wertes.
- Selbst bei gleicher Parameterzahl lässt sich ein nichtlineares Modell gewöhnlich durch eine Taylor-Entwicklung approximieren. Zu jedem nichtlinearen Modell gibt es daher meist eine einfachere lineare Näherung, und es braucht einen guten Grund, warum das lineare Modell nicht genügt.
- Die Ausnahmen sind die singulären Fälle, in denen die Terme niedriger Ordnung verschwinden. Solche Fälle beschreiben realistische Finanzzeitreihen selten.
- Lineare Modelle meinen hier nicht nur eine lineare Preisprognose, sondern auch eine lineare Kapitalallokation.
- Wer ein Modell so lange nachjustiert, bis es auf dem vermeintlichen Out-of-Sample-Satz ebenfalls gut aussieht, hat diese Daten in Trainingsdaten verwandelt.
- Beim neuronalen Netz ist die Zahl der mit In-Sample-Trainingsdaten anzupassenden Parameter proportional zur Zahl der Knoten.
- Mit mindestens 100 Parametern lässt sich das Modell an jede gewünschte Zeitreihe anpassen und eine fantastische Sharpe Ratio erzielen, vorwärts aber mit wenig oder keiner Vorhersagekraft wegen Data-Snooping-Bias.
- Der Alarm des Autors geht an, sobald von einem neuronalen Handelsmodell die Rede ist, erst recht bei einem mit 100 Knoten.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- Im Sisyphus-Paradigma bleibt oft ein falsch positives Ergebnis, das in einem überangepassten Backtest gut aussieht.
- Dieselbe Suche endet oft bei überfülltem Faktor-Investing mit niedrigem Sharpe Ratio und akademischer Stützung.
- Der Text hält es für nicht schwierig, einen ML-Algorithmus an Finanzdaten überanzupassen, und begründet damit, Bagging gegenüber Boosting zu bevorzugen.
- Eine Zeitschrift kann die Versuche mit einer kombinatorischen purged Cross-Validation bei vorgegebenem N und k wiederholen lassen.
- Weil die Pfade erst durch das vorgegebene N und k festliegen, wird eine Anpassung an einen einzelnen Walk-Forward-Pfad aufgedeckt.

## Regeln und Kriterien

- Stets ist zu fragen, auf welche Weise die eigene Arbeit überanpassen könnte.
- Der eigenen Arbeit ist mit Skepsis zu begegnen, und der Nachweis eines geschaffenen Mehrwerts ist ständig zu verlangen.
- Dass viele Akademiker überanpassen, macht es nicht richtig, denn sie riskieren weder fremdes noch eigenes Vermögen.
- max_features niedriger setzen, damit sich die Bäume unterscheiden.
- min_weight_fraction_leaf groß genug wählen, zum Beispiel 5 Prozent, sodass die Out-of-Bag-Genauigkeit gegen die k-Fold-Genauigkeit außerhalb der Stichprobe konvergiert.
- max_samples auf die mittlere Eindeutigkeit der Beobachtungen setzen.
- Den gewöhnlichen Bootstrap durch den sequenziellen Bootstrap ersetzen.
- Bei einer SVM nennt der Text ein max_iter von 100.000 statt minus 1 oder ein tol über dem Standard von 10 hoch minus 3. Bei anderen Verfahren entsprechen dem die Baumtiefe und der minimale Gewichtsanteil eines Blatts.
- Modelle sollen für ganze Anlageklassen oder Universen statt für einzelne Titel entwickelt werden; ein Fehler, der nur bei einem Titel auftaucht, ist wahrscheinlich eine falsche Entdeckung.
- Bagging soll Overfitting vorbeugen und die Varianz des Prognosefehlers senken; verschlechtert Bagging die Leistung, war die Strategie wahrscheinlich auf wenige Beobachtungen oder Ausreißer überfittet.
- Es soll nicht backgetestet werden, bevor die Forschung abgeschlossen ist.
- Jeder Backtest auf einem Datensatz ist festzuhalten, damit die Probability of Backtest Overfitting des gewählten Ergebnisses geschätzt und die Sharpe Ratio um die Zahl der Versuche deflationiert werden kann.
- Szenarien sollen statt der Geschichte simuliert werden, weil ein historischer Pfad leicht zu überfitten ist und Tausende Was-wäre-wenn-Szenarien schwerer zu überfitten sind.
- Findet der Backtest keine profitable Strategie, wird von vorn begonnen und das Wiederverwenden der Ergebnisse unterlassen.
- Den Lookback auf ein kleines Vielfaches der Halbwertszeit zu setzen, vermeidet die Brute-Force-Optimierung eines freien Parameters anhand der Performance der Handelsstrategie.
- Die lineare Mean-Reversion-Strategie wird als wirklich parameterfrei beschrieben.

## Risiken und Grenzen

- Wissentlich betrieben ist Overfitting wissenschaftlicher Betrug.
- Dass viele Akademiker überanpassen, macht es nicht richtig, denn sie riskieren weder fremdes noch eigenes Vermögen.
- Overfitting verschwendet Zeit, Ressourcen und Chancen.
- Falsch eingesetzte ML-Verfahren halten statistische Zufallstreffer für Muster.
- Diese Verwechslung erzeugt zusammen mit dem niedrigen Signal-Rausch-Verhältnis der Finanzmärkte bei unvorsichtigen Anwendern falsche Entdeckungen in immer höherem Tempo.
- Missbrauchte ML-Algorithmen verwechseln statistische Zufallstreffer mit Mustern.
- Ist Backtest-Overfitting schon in der ökonometrischen Analyse ein Problem, macht die Flexibilität von ML es zu einer ständigen Bedrohung.
- In der Finanzwelt gilt das besonders, weil die Datensätze kürzer sind, das Signal-Rausch-Verhältnis niedriger ist und Labore fehlen, die alle Umgebungsvariablen kontrollieren.
- Ein ML-Buch, das diese Gefahr nicht behandelt, kann der Laufbahn mehr schaden als nützen.
- Die Korrektur des Bias durch Boosting geht mit einem höheren Overfitting-Risiko einher.
- Übliche Cross-Validation auf Finanzdaten erkennt Overfitting nicht zuverlässig und kann es über die Wahl der Hyperparameter verstärken.
- Bei hoher Redundanz bleibt Overfitting trotz Ensemble bestehen, weil die gezogenen Mengen nahezu dieselben überangepassten Bäume ergeben.
- MDI ist ein In-Sample-Verfahren, und jedes Feature erhält eine gewisse Importance, selbst wenn es keinerlei Vorhersagekraft hat.
- Feature-Stacking liefert allgemeinere Schlüsse und ist weniger durch Ausreißer oder Overfitting verzerrt als die Mittelung über einzelne Instrumente.
- Einen Klassifikator auf einer Menge von Instrumenten zu fitten, senkt die Wahrscheinlichkeit, den Schätzer auf ein einzelnes Instrument oder einen kleinen Datensatz zu überfitten.
- Ein Walk-Forward lässt sich leicht überfitten, weil es ohne Zufallsziehung nur einen Testpfad gibt, der bis zu einem falsch positiven Ergebnis wiederholt werden kann.
- Ein gewöhnlicher Backtest prüft nur den historischen Pfad, und dieser einzelne Pfad lässt sich leicht überfitten.
- Ein Walk-Forward-Backtest lässt sich ebenso leicht überfitten wie ein Walk-Backward-Backtest; widersprüchliche Ergebnisse bei geänderter Beobachtungsfolge sind ein Beleg für dieses Overfitting.
- Abbildung 11.1 zeigt einen starken und anhaltenden Leistungsabfall, verursacht durch Backtest-Overfitting.
- In dieser Abbildung ist die Wahrscheinlichkeit einer negativen Out-of-Sample-Sharpe-Ratio 0,74, und die angepasste Beziehung ist eine Out-of-Sample-Sharpe-Ratio von 0,87 minus 0,75 mal die In-Sample-Sharpe-Ratio plus Fehler, bei einem adjustierten R² von 0,17.
- Abbildung 11.2 zeigt für dieselbe Auswahl eine Probability of Overfit von 0,74.
- Bei genügend vielen Pfaden kann die Wahrscheinlichkeit einer Fehlentdeckung vernachlässigbar werden.
- Eine Varianz von genau null bleibt unerreichbar, weil die Zahl der Pfade nach oben begrenzt ist.

## Beispiele

- Im Beispiel korrelieren die Eigenwerte mit den MDI-Werten mit einem Pearson-Koeffizienten von 0,8491 bei einem p-Wert unter 1E-150, was belegt, dass PCA informative Features ohne Overfitting richtig geordnet hat.
- Das Beispiel eines neuronalen Handelsnetzes mit etwa 100 Knoten hat eine Backtest-Sharpe-Ratio von 6.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 20–39 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-002-p020-p039|S. 20–39]]
- Advances in Financial Machine Learning.pdf, S. 39–58 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-003-p039-p058|S. 39–58]]
- Advances in Financial Machine Learning.pdf, S. 115–134 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-007-p115-p134|S. 115–134]]
- Advances in Financial Machine Learning.pdf, S. 134–153 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-008-p134-p153|S. 134–153]]
- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]

## Verwandte Themen
