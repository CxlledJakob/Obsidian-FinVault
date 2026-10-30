---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Zeitreihen"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Kointegration


## Kurzdefinition

- Kointegration ist im Engle-Granger-Sinn der Kunstgriff, der eine Regression auf nichtstationären Reihen ermöglicht und dabei das Gedächtnis erhält.
- Kointegration ist der Kunstgriff, der eine Regression auf nichtstationären Reihen ermöglicht, sodass das Gedächtnis erhalten bleibt.
- Preisreihen heißen kointegrierend, wenn sich eine stationäre lineare Kombination mehrerer nichtstationärer Preisreihen finden lässt, also ein Portfolio, dessen Marktwert mean-reverting ist.
- Die häufigste Kombination sind zwei Reihen: ein Asset long und ein anderes gleichzeitig short, mit passender Kapitalzuteilung; das ist Pairs Trading, und der Begriff trägt auch drei oder mehr Assets.
- Lassen sich zwei oder mehr nichtstationäre Preisreihen zu einem stationären Portfolio verbinden, heißen diese Reihen kointegrierend.
- Kointegration lässt sich mit dem CADF-Test oder mit dem Johansen-Test messen.

## Kernaussagen

- Kointegrationsverfahren sind unter anderem deshalb wichtig, weil sie Reihen mit Gedächtnis modellieren können.
- Der Text fragt, warum gerade die Null-Differenzierung die besten Ergebnisse liefern sollte, und hält sie für ebenso willkürlich wie die Differenzierung um einen Schritt.
- Zwischen keiner Differenzierung und voller Differenzierung liegt ein weiter Bereich, der sich mit fraktionaler Differenzierung für ein prognosestarkes Modell erkunden lässt.
- Log-Preise haben in diesem Paradigma Gedächtnis und sind nicht stationär.
- Für ML-Prognosen hält der Text den Kointegrations-Kunstgriff für unnötig, weil die Fixed-Width-Fracdiff-Methode Stationarität erreicht, ohne das Gedächtnis aufzugeben.
- Im Engle-Granger-Paradigma haben Log-Preise Gedächtnis und sind nicht stationär.
- Die Fixed-Width-Fracdiff-Methode braucht diesen Kunstgriff für ML-Prognosen nicht, weil Stationarität möglich ist, ohne Gedächtnis und Prognosekraft aufzugeben.
- Zur Erkennung der Kointegration eines Portfolios von Instrumenten dienen der kointegrierte Augmented-Dickey-Fuller-Test, CADF, und der Johansen-Test.
- Über die mechanische Anwendung dieser statistischen Tests hinaus soll intuitiv klar werden, was sie wirklich prüfen, samt der einfachen mathematischen Gleichungen dahinter.
- Es wird gezeigt, ob Rohpreise, Log-Preise oder Verhältnisse als Eingaben für diese Tests und Strategien am sinnvollsten sind.
- Mean-Reversion-Strategien sind oft leicht zu bauen, weil man nicht auf von sich aus stationäre Instrumente beschränkt ist und aus vielen kointegrierenden Aktien und ETFs wählen kann.
- Neue ETFs, die sich von bestehenden nur am Rand unterscheiden, vergrößern diese Auswahl jedes Jahr.
- Hinter einem kointegrierenden Paar steht oft eine fundamentale Geschichte, und auch wenn das Paar auseinanderfällt, ist der Grund häufig noch verständlich.
- Echte Stationarität oder Kointegration ist für eine erfolgreiche Mean-Reversion-Strategie nicht notwendig, wenn kurzfristige oder saisonale Rückkehr mitgenommen und die Position vor dem nächsten Gleichgewicht geschlossen wird.
- Umgekehrt trägt nicht jede stationäre oder kointegrierte Reihe, wenn die Halbwertszeit zehn Jahre beträgt.
- Der Spread y gleich h1 y1 plus weitere Glieder ist per Konstruktion stationär, wenn die hi aus Regression oder Johansen-Eigenvektoren stammen, und hi ist dann die Stückzahl.
- Kointegrieren die Logpreise, beschreiben die hi Kapitalgewichte eines Portfolios mit impliziter Kasse, und der Marktwert dieser Konstruktion ist stationär, aber nicht konstant.
- Theoretisch sollten Aktienpaare eines Sektors wegen gemeinsamer ökonomischer Faktoren kointegrieren; praktisch erfüllen tägliche Einzelaktien fast nie die Stationaritätsdefinition aus Kapitel 2, und auch sinnvolle Paare kointegrieren selten out of sample.
- Kointegrierende Aktienpaare lassen sich in einem gewählten Zeitraum leicht finden und verlieren die Kointegration in der folgenden Out-of-Sample-Periode ebenso leicht, weil sich die Lage einer Firma durch Management und Wettbewerb schnell ändert; dieselbe Branche garantiert nicht dasselbe Schicksal, Beispiel AAPL gegen BBRY.
- Einmal als kointegrierend gefundene ETF-Paare fallen out of sample seltener auseinander, weil sich die Fundamentaldaten eines Aktienkorbs viel langsamer ändern als die einer einzelnen Firma.
- Die statistischen Tests der Zeitreihen-Mean-Reversion sind für querschnittliche Mean Reversion weitgehend irrelevant.
- Ein gleichgewichtetes Long-only-Portfolio muss erneut gegen den ETF getestet werden: gleiche Kapitalgewichte erzeugen nicht automatisch eine Preisreihe, die mit SPY kointegriert, selbst wenn jede Einzelaktie mit SPY kointegriert.
- Die meisten Währungs- oder Future-Paare kointegrieren nicht, und die meisten Portfolios aus Währungen oder Futures zeigen keine querschnittliche Mean Reversion.
- Weil EWA und EWC kointegrieren, wäre zu erwarten, dass AUD mit CAD kointegriert; weil Australien und Südafrika große Mineneinnahmen haben, wäre außerdem Kointegration von AUD mit ZAR zu erwarten, und Händler nennen diese Währungen samt der norwegischen Krone Rohstoffwährungen.
- Ein ETF von Rohstoffproduzenten wie XLE kointegriert gewöhnlich mit dem Spot dieser Ware, wegen der Roll-Rendite aber nicht notwendig mit dem Future-Preis dieser Ware.
- Rohstoffwährungen als Gruppe bieten viele Gelegenheiten zur Kointegration.
- Ein Johansen-Test auf einer Mischung der beiden ES-VX-Regime wäre ein Fehler; der Text beschränkt sich auf das zweite Regime, das bis zum Zeitpunkt des Schreibens reicht.
- Bevor ein Johansen-Test auf den vier Kontrakten CL, BZ, RB und HO läuft, wird zuerst der Crack Spread geprüft, dessen ADF vom 20. Mai 2002 bis zum 4. Mai 2012 keine Mean Reversion zeigt.
- ETFs mit Rohstoffproduzenten kointegrieren oft mit dem Spotpreis dieser Rohstoffe, weil die Rohstoffe einen wesentlichen Teil ihrer Assets ausmachen, und dienen deshalb als Proxy des Spotpreises, um die Rollrendite zu extrahieren.
- Die Kointegration zwischen VX und ES wurde in Kapitel 5 für eine profitable Mean-Reversion-Strategie verwendet; hier wird daraus keine Mean-Reversion-, sondern eine Momentum-Strategie gebaut.

## Funktionsweise

- Die Hedge Ratio eines Assets ist die Zahl der Einheiten, die im Portfolio long oder short gehalten werden; bei einer Aktie sind das Stücke, und eine negative Hedge Ratio bedeutet eine Short-Position.
- Kointegration bedeutet nicht, dass eine beliebige Linearkombination ein stationäres Portfolio ergibt.
- Engle und Granger (1987) bestimmen die optimale Hedge Ratio durch eine lineare Regression zweier Preisreihen, bilden damit das Portfolio und testen dann dessen Stationarität; die Funktion cadf führt diese Schritte aus.
- Der CADF-Test gilt nur für ein Paar, der Johansen-Test für beliebig viele Reihen.
- Im Johansen-Test ist der Rang r von Λ die Zahl der unabhängigen Portfolios aus Linearkombinationen der kointegrierenden Reihen; die Eigenvektoren dienen als Hedge Ratios.
- Der Johansen-Test hängt nicht von der Reihenfolge der Preisreihen ab und liefert in einem Lauf alle unabhängigen kointegrierenden Beziehungen.
- Zwei kointegrierende Beziehungen bei nur zwei Reihen sind zwei verschiedene Hedge Ratios, die nicht notwendig Kehrwerte voneinander sind, und damit zwei unabhängige stationäre Portfolios.
- Die Eigenvektoren sind nach absteigenden Eigenwerten geordnet; der erste, zum größten Eigenwert, ist der stärkste und hat die kürzeste Halbwertszeit.
- Die Eigenvektoren des Johansen-Tests dienen als Hedge Ratios, und der Eigenvektor mit dem größten Eigenwert hat die kürzeste Halbwertszeit.
- Der Nettomarktwert des Portfolios ist Stückzahl mal Kurs, über die ETFs summiert, und tritt an die Stelle der Einzelreihe in der Halbwertszeit-Regression.
- Das Problem des kanalnormierten Divergenzindikators bei negativ korrelierten Reihen ließe sich mit einer Formulierung auf Basis der Kointegration vermeiden, die Engle und Granger 1987 vorschlugen.
- Dieses Verfahren nutzt eine Regressionsanalyse, um festzustellen, ob zwischen zwei Zeitreihen eine lineare Beziehung besteht.
- Es verkraftet auch Paare, die stark negativ korreliert und damit 180 Grad außer Phase sind, und löst so das Problem falscher Gleichlaufanzeigen bei einem Indikatorwert von null.
- Zuerst wird statistisch geprüft, ob die beiden Reihen verbundene Trends haben; sind sie kointegriert, fällt ein stationärer Divergenzindikator aus der Analyse.
- Dieser Indikator heißt Error-Correction-Modell und misst, wie weit eine Reihe von der typischen linearen Beziehung der beiden Reihen abgewichen ist.
- In den meisten Anwendungen soll die Divergenz zum gemeinsamen Trend zurückkehren, wenn das Error-Correction-Modell extrem positiv oder extrem negativ wird; der Fehler soll auf seinen normalen Wert null zurückkorrigieren.
- Der Indikator einer solchen Beziehung ist eine Zeitreihe der Fehler, also der Residuen, der linearen Beziehung zwischen den zwei Reihen.
- Ein Testtyp, mit dem festgestellt wird, dass eine Zeitreihe stationär ist, ist der Unit-Root-Test, beschrieben bei Alexander, Market Models, Seiten 324–328 und 353–361.

## Voraussetzungen

- Der Johansen-Eigenvektor ist nur dann als Kapitalgewicht lesbar, wenn beide Preisreihen dieselbe Quotierungswährung haben; sonst haben Punktbewegungen nicht denselben Wert, und der Test ist bedeutungslos.
- Deshalb läuft der Test auf AUD.USD und CAD.USD und nicht auf USD.AUD gegen USD.CAD.

## Anwendung im Trading

- Findet sich ein Instrument, etwa ein ETF oder ein anderer Future, das mit dem Spotpreis oder der Spot-Rendite eines Rohstoffs kointegriert oder korreliert, lässt sich die Rollrendite des Rohstoff-Futures extrahieren, indem dieses Instrument bei Backwardation geshortet und bei Contango gekauft wird.
- Aus Gründen der Einfachheit wurde die Kointegration für die Divergenzindikatoren der Fallstudie nicht verwendet.
- Es wurde angenommen, eine nicht mit dem S&P 500 verbundene Begleitreihe zeige sich an der schlechten finanziellen Leistung der Divergenzregel.
- Der Autor hält die Kointegrationsmethodik für weiter untersuchenswert bei der Entwicklung von Indikatoren.
- Als mögliche Verbesserung der Indikatorspezifikation nennt der Text, Divergenzen könnten besser mit Indikatoren auf Basis der Kointegration gemessen werden; das Wort steht dort als conintegration.
- Diese Anregung steht neben dem Vorschlag, Extremindikatoren mit der von Ehlers diskutierten Fisher-Transformation zu untersuchen.

## Regeln und Kriterien

- Im CADF-Test ist die Hedge Ratio nicht der genaue Kehrwert, wenn abhängige und unabhängige Variable getauscht werden; oft ist nur eine der beiden Ordnungen stationär, und man nimmt die Ordnung mit der negativsten t-Statistik.
- Für EWA und EWC gilt diese Ein-Ordnungs-Einschränkung nicht, was der Johansen-Test später bestätigt.
- Für den Johansen-Test wird p gleich 0 gesetzt, also ein konstanter Offset M ungleich 0, aber kein konstanter Drift, und die Lag-Zahl k gleich 1; ein konstanter Drift im Preis eines stationären Portfolios gilt als unpraktisch.
- Der Nettomarktwert yport ist die über alle ETFs summierte Stückzahl mal dem jeweiligen Kurs.
- Preis-Spreads sind einfacher als Log-Preis-Spreads; beide sind theoretisch gerechtfertigt, wenn sowohl Preise als auch Logpreise kointegrieren.
- Das Verhältnis y1/y2 ist nur stationär, wenn die Hedge Ratios betragsgleich sind; das ist ein Sonderfall und nicht die normale Erwartung.
- Für ein wirklich kointegrierendes Paar genügen möglichst lange Historie und eine einmalige OLS- oder Johansen-Schätzung.
- Für Paare, die nicht wirklich kointegrieren, braucht der Spread oft eine dynamische Hedge Ratio; das Verhältnis als Signal erspart das.

## Risiken und Grenzen

- Die Zahl kointegrierter Variablen ist begrenzt, und die kointegrierenden Vektoren sind notorisch instabil.
- Der Handel von USD.NOK und USD.MXN erzeugt P&L in NOK und in MXN, der direkte Handel von MXN.NOK nur P&L in NOK; die beiden Wege sind nicht identisch.
- Log-Preis-Kointegration hält den Marktwert nur stationär, wenn fortlaufend rebalanciert und dabei Gewinn oder Verlust in die Kasse gebucht wird.
- Die dem Autor bekannte Johansen-Implementierung akzeptiert höchstens 12 Symbole (LeSage, 1998).
- Mean-Reversion-Handel eines Commodity-Fonds gegen den Produzentenfonds wäre weniger riskant, wenn der Fonds die physische Ware hält und nicht die Futures.
- Die Schwierigkeit liegt in der richtigen Aufbereitung der Reihen für den Kointegrationstest und in der richtigen Renditeformel.
- Dass ein Produzenten-ETF mit dem Spot kointegrieren und mit dem Future trotzdem auseinanderlaufen kann, kostete den Autor mehr als 100.000 Dollar und ruinierte 2006.

## Beispiele

- ETFs sind ein ergiebiges Feld für kointegrierende Reihen; die kanadische und die australische Wirtschaft sind rohstoffbasiert, deshalb werden EWA und EWC als Kandidaten geprüft, und ihr Streudiagramm liegt auf einer Geraden.
- Mit EWA als unabhängiger und EWC als abhängiger Variable ist die CADF-Statistik etwa minus 3,64 und damit negativer als der 95-Prozent-Wert minus 3,359, das Paar kointegriert also mit 95 Prozent Sicherheit.
- Für EWA und EWC schließen Trace- und Eigen-Test auf zwei kointegrierende Beziehungen: die Trace-Null r gleich 0 wird auf 99 Prozent verworfen, r kleiner oder gleich 1 auf 95 Prozent, und beide Eigen-Nullen auf 95 Prozent.
- Mit dem Rohstoffaktien-ETF IGE zusätzlich verwirft der Trace-Test r ≤ 0, r ≤ 1 und r ≤ 2 auf 95 Prozent, Statistiken 34,429, 17,532 und 4,471 gegen 29,796, 15,494 und 3,841; die Eigen-Statistik für r ≤ 0 ist 16,897 und liegt unter dem 90-Prozent-Wert 18,893.
- Die Eigenwerte des Tripels sind 0,0112, 0,0087 und 0,0030; die zugehörigen Eigenvektoren, in der Ordnung EWC, EWA, IGE, lauten minus 1,0460, 0,7600 und 0,2233 für den ersten, minus 0,5797, minus 0,1120 und 0,5316 für den zweiten, sowie minus 0,2647, minus 0,0790 und 0,0952 für den dritten.
- Die Halbwertszeit des Portfolios aus dem ersten Eigenvektor beträgt 23 Tage und ist damit deutlich kürzer als die 115 Tage von USD.CAD.
- EWA kointegriert mit EWC, weil die kanadische und die australische Wirtschaft von Rohstoffen dominiert werden.
- GDX kointegriert mit GLD, weil der Wert der Goldbergbauunternehmen stark vom Goldwert abhängt.
- GDX und GLD fielen Anfang 2008 auseinander, weil hohe Energiepreise den Goldbergbau ungewöhnlich teuer machten; die Erklärung steht in Kapitel 4.
- Das Portfolio aus dem stärksten Eigenvektor von EWA, EWC und IGE hat 23 Tage Halbwertszeit, gegenüber 115 Tagen bei USD.CAD.
- Steigen zwei Preise von 10 und 5 auf 100 und 50, bleibt das Verhältnis 2, während der Spread von 5 auf 50 steigt und dann wahrscheinlich nicht stationär ist.
- GLD und USO sind nicht kointegriert, obwohl hohe Ölpreise über die Inflation mit dem Goldpreis begründet werden; der Unterschied von Spotöl und den Öl-Futures in USO wird auf Kapitel 5 verschoben.
- Trotzdem erreicht der Preis-Spread mit adaptiver Hedge Ratio etwa 10,9 Prozent APR und eine Sharpe Ratio von etwa 0,59, der Log-Preis-Spread 9 Prozent und 0,5, und das Verhältnis eine negative APR.
- Der Preis-Spread mit wechselnder Hedge Ratio sieht sehr stationär aus, das Verhältnis USO zu GLD nicht.
- EUR.GBP ist ein Verhältnis aus EUR.USD und GBP.USD; für ein nicht wirklich stationäres Kreuz wie MXN.NOK kann das Verhältnis wirksamer sein als der Spread, auch wenn man USD.NOK und USD.MXN handeln muss.
- EWA und EWC sind Kandidaten, weil Australien und Kanada rohstoffbasierte Ökonomien sind; ihre Kointegration wurde in Kapitel 3 bestätigt, 2009 im Blog genannt und bestand beim Schreiben im November 2012 weiter.
- Neben Länder-ETFs sind Sektor-ETFs ergiebig; der Retail-Fonds RTH kointegriert mit dem Consumer-Staples-Fonds XLP, und mit mehr ETFs auf denselben Sektor nehmen die Gelegenheiten zu.
- GLD gegen GDX kointegriert im Johansen-Test vom 23. Mai 2006 bis 14. Juli 2008 mit 99 Prozent Wahrscheinlichkeit und verliert die Kointegration vom 15. Juli 2008 bis 9. April 2012.
- Am 14. Juli 2008 erreichte WTI etwa 145 Dollar je Barrel, ein Allzeithoch; teures Öl verteuert die Goldförderung, senkt die Gewinne der Minen und lässt deren Aktien gegenüber dem Gold-Spot underperformen.
- Das Triplet GLD, GDX und USO kointegriert über 2006 bis 2012 laut Johansen mit 99 Prozent Wahrscheinlichkeit für eine kointegrierende Beziehung.
- USO gegen XLE ist kein sauberes Ware-gegen-Produzent-Paar: GLD hält Gold und spiegelt den Spot, USO hält kein Öl, sondern Öl-Futures; selbst wenn XLE mit dem Öl-Spot kointegriert, muss es nicht mit USO kointegrieren, und das gilt für jeden Commodity-Futures-Fonds gegen einen Produzentenfonds.
- Im Training vom 1. Januar 2007 bis 31. Dezember 2007 kointegrieren 98 SPX-Aktien im Johansen-Test jeweils einzeln mit SPY bei mindestens 90 Prozent Wahrscheinlichkeit; der zweite Test auf Logpreisen, wegen täglichen Rebalancings auf konstantes Kapital je Aktie, zeigt Kointegration des Long-only-Portfolios mit SPY mit besser als 95 Prozent, und es gibt zwei kointegrierende Relationen.
- Das ETF-Paar GLD gegen GDX hörte 2008 auf zu kointegrieren, verwiesen auf Kapitel 4.
- Die Hypothese führte den Stopp auf den hohen Rohölpreis zurück.
- Wurde der Ölpreis als Inputvariable ergänzt, funktionierte das Kointegrationsmodell wieder.
- Ein typisches Beispiel ist Pairs Trading: Sind die Aktien von Ford und GM kointegriert und Ford relativ zu GM zu hoch, wird Ford short und GM long gestellt.
- Der Paartrade gewinnt unabhängig davon, wie die Divergenz korrigiert wird, ob Ford fällt, GM steigt oder eine Kombination aus beidem eintritt.
- Fosback nutzte die Kointegrationsanalyse innovativ, um eine dritte Variable, den S&P 500, vorherzusagen, statt das Verhalten des Spreads zwischen den kointegrierten Reihen.
- Sein Fosback Index nutzt, dass Zinssätze und die Cash-Quoten von Fonds kointegrierte Reihen sind, und entstand mehr als ein Jahrzehnt vor der Veröffentlichung von Engle und Granger.
- Der Index signalisiert, wenn die Cash-Quote der Fonds deutlich von dem Niveau abweicht, das ihre lineare Beziehung zu den kurzfristigen Zinsen vorhersagt.
- Übermäßiger Pessimismus heißt, die Fondsmanager halten deutlich mehr Cash, als die kurzfristigen Zinsen vorhersagen, und übermäßiger Optimismus ist der umgekehrte Fall.
- Fosback fand, dass sowohl übermäßiger Pessimismus als auch übermäßiger Optimismus, so gemessen, mit künftigen Renditen des Aktienmarkts korrelierten.
- Der Index entfernt den Einfluss der kurzfristigen Zinsen aus den Cash-Quoten und misst die Stimmung der Fondsmanager reiner als die rohe Cash-Quote, die von den Zinsen verfälscht ist.
- Der Autor entwickelte 1983 zusammen mit der Raden Research Group den Zeitreihenoperator YY, der im Konzept der Kointegrationsanalyse ähnlich ist, mit der Ausnahme, dass die YY-Werte durch den Standardfehler der Regression normiert wurden und kein expliziter Test auf die Stationarität der Residuen gemacht wurde.
- Die Entwicklung von YY wurde angeregt durch Arthur Merrill, DFE: Deviation from Expected (Relative Strength Corrected for Beta), Market Technician Journal, August 1982, Seiten 21–28.
- Die auf YY beruhenden Indikatoren dienten als Kandidateneingaben für verschiedene Prognosemodelle. Ein Beispiel war ein Sentiment-Indikator auf der Beraterstimmung zu T-Bonds.
- Die Prognosekraft der rohen Konsensinformation wurde durch eine YY-Transformation verbessert, die vergangene Marktänderungen als Regressorvariable nutzte.
- Der Return-Reversal-Effekt ähnelt dem Residual-Reversal-Effekt, der auf der Kointegrationsanalyse beruht.

## Unterschiedliche Quellenpositionen

- Box-Jenkins behandelt Renditen als stationär, aber gedächtnislos; Engle-Granger behandelt Log-Preise als gedächtnisbehaftet, aber nicht stationär, und nutzt Kointegration, damit die Regression trotzdem geht.
- Der Text stellt Engle-Granger, wo Log-Preise Gedächtnis behalten und nicht stationär sind, dem Box-Jenkins-Bild gegenüber, in dem Renditen stationär und gedächtnislos sind.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 96–115 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-006-p096-p115|S. 96–115]]
- Advances in Financial Machine Learning.pdf, S. 115–134 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-007-p115-p134|S. 115–134]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 419–438 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-023-p419-p438|S. 419–438]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]

## Verwandte Themen

- Engle und Granger, Co-integration and Error-Correction: Representation, Estimation and Testing, Econometrica 55 (1987), Seiten 251–276, ist die angeführte Grundlage der Kointegration.
