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

# Random Walk


## Kurzdefinition

- Im Chow-Typ-Dickey-Fuller-Test ist die Nullhypothese, dass die Reihe einem Random Walk folgt, also Rho gleich 1 ist.
- Im Roll-Modell folgt der Mid-Price einem Random Walk ohne Drift, mt = mt−1 + ut.
- Ein Random Walk ist definitionsgemäß frei von echten Trends, Mustern oder ausnutzbarer Ordnung jeder Art.

## Kernaussagen

- Mit steigender Halbwertszeit steigt phi, definiert als zwei potenziert mit minus eins durch die Halbwertszeit, und der Prozess rückt an einen Random Walk heran.
- Geht phi gegen 1, bleiben keine erkennbaren Bereiche, in denen eine Handelsregel die Performance zuverlässig maximiert.
- Bei Prognose 0 spreizen sich die Gebiete hoher und niedriger Performance mit wachsender Halbwertszeit, und die Sharpe Ratios sinken.
- Bei Prognose 5 und Halbwertszeit 100 ist der Prozess so nah an einem Random Walk, dass die höchste Sharpe Ratio nur noch 0,32 beträgt.
- Bei Prognose 5 und Halbwertszeit 100 ist der Prozess so nah an einem Random Walk, dass die höchste Sharpe Ratio nur 0,32 beträgt.
- Bei negativer Prognose wirkt die Annäherung an den Random Walk mildernd, weil das schlechteste Gebiet sich spreizt und die Sharpe Ratio weniger negativ wird.
- Bei Prognose minus 5 und Halbwertszeit 10 wird aus dem Rechteck ein Quadrat, und die Sharpe Ratios liegen etwa bei minus 9.
- Steigen die Halbwertszeiten weiter auf 25, 50 und 100, verflacht die Performance.
- Sobald die Performance bei langer Halbwertszeit verflacht, wird das Optimieren der Handelsregel eine Übung in Backtest-Overfitting.
- Bei Prognose minus 10 wiederholt sich das gedrehte Gegenbild des Falls mit positivem langfristigem Gleichgewicht.
- Die Alternative ist, dass die Reihe als Random Walk beginnt und zum Bruchzeitpunkt in einen explosiven Prozess mit Rho größer als 1 wechselt.
- Der Bruchzeitpunkt ist ein Anteil Tau zwischen 0 und 1 der Stichprobenlänge.
- Exponentielles Wachstum oder Kollaps ist mit einem Random Walk unvereinbar und auf Dauer unhaltbar.
- Chows Ansatz unterstellt genau ein Bruchdatum, und die Blase läuft bis zum Stichprobenende, ohne Rückwechsel zum Random Walk.
- Für die Folge Random Walk, Blase, Random Walk ist der Supremum-Augmented-Dickey-Fuller-Test vorgesehen.
- Im Null-Lag-Modell auf Logpreisen verhält sich das System bei Beta gleich 0 als nichtstationäres Martingal.
- Die Änderungen des Mid-Price sind unabhängig und identisch normalverteilt mit Varianz σ²u.
- Die beobachteten Preise weichen vom Mid-Price um die halbe Spanne ab, pt = mt + bt c.
- Empirisch haben Finanzzeitreihen einen Drift, sind heteroskedastisch, zeigen serielle Abhängigkeit, und ihre Renditeverteilung ist nicht normal.
- Mit einem geeigneten Sampling, wie in Kapitel 2 beschrieben, müssen die Random-Walk-Annahmen nicht allzu unrealistisch sein.
- Das Rauschen des unbeobachteten Preises ohne Mikrostrukturrauschen ist σ²u = σ²[Δpt] + 2 σ[Δpt, Δpt−1].
- Die meisten Preisreihen sind geometrische Random Walks; die Renditen verteilen sich gewöhnlich zufällig um einen Mittelwert von null.
- Beim geometrischen Random Walk wächst die Varianz der Logpreisänderung linear mit der Zeitspanne τ, und der Hurst-Exponent ist 0,5.
- Kann die ADF-Null λ gleich 0 nicht verworfen werden, hängt der nächste Schritt nicht vom aktuellen Niveau ab, und ein Random Walk bleibt möglich.
- Stationarität bedeutet, dass Preise langsamer diffundieren als ein geometrischer Random Walk.
- Hurst-Exponent und Variance-Ratio-Test sind dafür gebaut, diese Stationarität gegen den geometrischen Random Walk zu prüfen.
- Aktienkurse folgen langfristig geometrischen Random Walks, auch wenn sie kurzfristig unter normalen Umständen mean-reverting sind.
- Der geometrische Random Walk beschreibt tägliche Einzelaktien gut: einmal weggegangen, kehren sie selten zu ihrem Startpunkt zurück; Intraday- und saisonale Mean Reversion sind Sonderfälle.
- Dass Aktienkurse geometrischen Random Walks folgen, wie es viele Forscher und Malkiel 2008 betonen, gilt nur, wenn die Reihe streng in regelmäßigen Abständen auf Mean Reversion getestet wird, etwa an den täglichen Schlüssen.
- Experten-Chartisten können echte Aktiencharts nicht von Charts unterscheiden, die ein Zufallsprozess erzeugt hat.
- Die inhärente Komplexität und Zufälligkeit der Finanzmärkte und die Unmöglichkeit kontrollierter Experimente machen es unwahrscheinlich, dass die technische Analyse Regeln mit der Präzision physikalischer Gesetze findet.
- Prognosegenauigkeit von der Art physikalischer Gesetze ist nicht die Definitionsbedingung von Wissenschaft; diese besteht in der kompromisslosen Offenheit, falsche Ideen zu erkennen und auszuscheiden.
- Dieselben Muster und Trends, denen die technische Analyse Bedeutung zuschreibt, erscheinen regelmäßig auch in rein zufälligen Daten.
- Studien zeigen, dass geübte Chartleser echte Marktcharts nicht zuverlässig von Charts unterscheiden können, die ein Zufallsprozess erzeugt.
- Solche Charts entstehen durch zufällige Ziehungen aus einer Stichprobe tatsächlicher Preisänderungen, enthalten konstruktionsbedingt keine echten Trends und Muster und sind deshalb unmöglich vorherzusagen, sehen für erfahrene Chartisten aber aus wie echte Preischarts.
- Prognosen auf Basis echter Charts wären auf dieser Grundlage nicht vertrauenswürdig.
- Offensichtliche Gültigkeit ist ein unzureichender Maßstab dafür, ob Marktmuster gültig sind.
- Studien zeigen, dass Experten im Chartlesen echte Marktcharts nicht zuverlässig von Charts eines Zufallsprozesses unterscheiden können.
- Prognosen aufgrund echter Charts wären damit nicht vertrauenswürdig, und offensichtliche Gültigkeit ist kein hinreichender Maßstab für die Gültigkeit von Marktmustern.
- In vielen Fällen ist das, was man erlebt, nichts weiter als die Launen des Zufalls.
- Die Evolution hat das Sehen von Ordnung begünstigt, nicht aber in gleichem Maß die Fähigkeit, gültige von ungültigen Mustern zu unterscheiden, sodass neben gültigem Wissen viele falsche Überzeugungen entstanden.
- Von den beiden Fehlern, eine Falschheit zu lernen oder eine Wahrheit zu verfehlen, neigen wir stärker dazu, Falschheiten zu übernehmen.
- Roberts zeigte, dass dieselben Chartmuster, denen die technische Analyse Bedeutung beimisst, mit großer Regelmäßigkeit in Random Walks erscheinen, darunter Schulter-Kopf-Schulter-Tops und -Böden, Dreieckstops und -böden, Dreifachtops und -böden sowie Trendkanäle.
- Zwei Gründe der Illusion nach Roberts: Die übliche Darstellung zeigt aufeinanderfolgende Kursniveaus statt der Kursänderungen, und Niveaus können einen künstlichen Eindruck von Muster oder Trend erzeugen; außerdem erzeugt das Zufallsverhalten selbst Muster, die zu irrigen Deutungen einladen.
- Ein solcher Chart lässt sich aus Münzwürfen bauen: Start bei einem beliebigen Preis, etwa 100 Dollar, plus ein Dollar bei Kopf und minus ein Dollar bei Zahl; jeder simulierte Preis ist der Startwert plus die kumulative Summe aller bisherigen Zufallsänderungen.
- Nach etwa dreihundert Würfen erscheinen Muster, die denen echter Finanzcharts ähneln, und diese Muster können die weitere Entwicklung des Münzwurf-Charts nicht vorhersagen.
- Wenn dieselben Muster in Random Walks regelmäßig auftreten und dort bekanntermaßen nicht vorhersagen, ist nicht begründet, warum sie vorhersagen sollen, nur weil sie auf einem echten Chart stehen.
- Was nichtzufällig aussieht, ist nicht notwendig nichtzufällig.
- Nur große Stichproben bilden den erzeugenden Prozess verlässlich ab; kleine Stichproben eines Zufallsprozesses sehen oft nach echten Mustern und Trends aus, obwohl es sie konstruktionsbedingt nicht geben kann.
- Ein verlässlicher Schluss, ob eine Stichprobe zufällig oder nichtzufällig erzeugt wurde, lässt sich aus einer kleinen Stichprobe nicht gewinnen.
- Menschen stellen sich Zufallsfolgen mit deutlich mehr Wechseln vor, als wirklich vorkommen; Zufallsprozesse zeigen weniger Wechsel und längere Serien gleicher Ergebnisse, als weithin geglaubt wird.
- Die Folge Kopf, Zahl, Kopf, Zahl, Kopf, Zahl und die Folge Kopf, Kopf, Kopf, Kopf, Kopf, Kopf sind gleich wahrscheinlich; der Eindruck, nur die erste sei zufällig und die zweite ein Trend, ist falsch.
- Weil echt zufällige Folgen weniger wechseln und mehr serien, als das intuitive Bild erwartet, sehen sie nichtzufällig aus.
- Random Walks haben kein Gedächtnis, und frühere Ergebnisse wirken nicht auf nachfolgende Ereignisse.
- Nach dem Einfachheitsprinzip, auch Ockhams Rasiermesser, ist bei gleich guter Anpassung an die Fakten die Theorie mit den wenigsten und am wenigsten verwickelten Annahmen vorzuziehen.
- Die Pseudo-Preisverläufe im Schulter-Kopf-Schulter-Test wurden erzeugt, indem tatsächliche historische Preisänderungen in zufälliger Reihenfolge aneinandergereiht wurden.
- Sie hatten dieselben statistischen Eigenschaften wie echte Aktien, aber jede Vorhersagbarkeit aus echter zeitlicher Struktur, also der Struktur, die TA-Muster ausnutzen sollen, war beseitigt.
- Obwohl diese Verläufe zufällig erzeugt waren, entstanden Schulter-Kopf-Schulter-Muster, die der Definition von Chang und Osler entsprachen.
- Das bestätigt die früheren Ergebnisse von Harry Roberts.
- Die Muster in den echten Aktienkursen verloren etwas mehr Geld als die Signale auf diesen zufällig zusammengesetzten Verläufen.
- Händler, die das Muster verwenden, werden als Noise Trader bezeichnet, weil sie ein Zufallssignal für ein informatives halten.
- Finanzmärkte sind wegen ihrer inhärenten Komplexität und Zufälligkeit extrem schwer vorherzusagen.
- Technische Analyse ist genau dann vertretbar, wenn Preisbewegungen in einigem Grad und während eines Teils der Zeit nichtzufällig sind; wären die Schwankungen vollständig zufällig, wäre sie sinnlos.
- Die EMH behauptet, Kursänderungen seien zufällig und deshalb unvorhersagbar; ihre Pioniere hielten Random Walks für eine notwendige Folge effizienter Märkte.
- In jüngerer Zeit argumentieren manche, die EMH impliziere nicht notwendig unvorhersagbare Random Walks und effiziente Märkte könnten mit Preisvorhersagbarkeit koexistieren.
- Ein effizienter Markt lässt sich nicht schlagen: keine fundamentale oder technische Strategie erzielt eine risikoadjustierte Rendite über einem Benchmark-Index, und das Beste ist Kaufen und Halten des Index, weil der aktuelle Preis alle bekannte und wissbare Information abbildet und die beste Wertschätzung ist.
- Preise ändern sich nur, wenn neue Information eintrifft, und dann fast sofort auf ein neues rationales Niveau; sie ziehen nicht allmählich von einem rationalen Niveau zum nächsten, sondern zeichnen eine Stufenfunktion, und weil günstige oder ungünstige Nachrichten nicht vorhersagbar sind, sind es auch die Kursänderungen nicht.
- Nach Samuelson folgen die Preise einem Random Walk, weil viele intelligente Investoren unterbewertete Anlagen kaufen und überbewertete verkaufen; im Extrem wirft ein verbundener Affe mit Dartpfeilen auf die Finanzseiten ebenso gut wie sorgfältig auswählende Experten.
- Die EMH schließt Handelssysteme auf verfügbarer Information aus, deren erwartete Gewinne die gleichgewichtige erwartete Rendite übersteigen; ein durchschnittlicher Anleger, ob Privatperson, Pensionsfonds oder Publikumsfonds, kann nicht hoffen, den Markt dauerhaft zu schlagen, und der dafür betriebene Aufwand ist verschwendet.
- Ohne Nachrichten oszillieren die Preise zufällig und unverzerrt um das rationale Niveau; weil dieses Niveau selbst unsicher ist, kann kein technischer oder fundamentaler Indikator verlässlich anzeigen, ob der Preis darüber oder darunter liegt, und Aktien mit niedrigem Kurs-Buchwert-Verhältnis steigen nicht eher als solche mit hohem.
- Effizienz verlangt nicht, dass der Marktpreis jederzeit gleich dem rationalen Wert ist, sondern dass die Abweichungen unverzerrt und zufällig sind: positive und negative Abweichungen sind gleich wahrscheinlich, und die Zeitreihe der Fehlbewertungen ist eine Zufallsvariable, deren Verteilung am rationalen Preis zentriert und ungefähr symmetrisch ist.
- In jeder Periode übertreffen etwa 50 Prozent der Investoren den Benchmark und 50 Prozent verfehlen ihn; dass niemand den Markt langfristig schlagen könne, ist ebenfalls falsch.
- Taleb zeigt: selbst wenn Manager nicht besser sind als ein Dartpfeile werfender Affe, mit Wahrscheinlichkeit 0,5 den Markt zu schlagen, und es 10.000 Manager gibt, haben nach fünf Jahren wahrscheinlich etwa 312 Firmen den Markt fünf Jahre in Folge geschlagen; die übrigen 9.682 klopfen seltener an.
- EMH-Vertreter nehmen sich stillschweigend die Freiheit, neue Risikofaktoren zu erfinden, wann immer sie wollen, sodass sich kaum widerlegen lässt, dass Strategien auf veralteter Information den Markt nicht schlagen; einen Faktor erst nach Entdeckung einer solchen Strategie vorzuschlagen, ist eine Ad-hoc-Hypothese zur Immunisierung vor Falsifikation, vorher identifizierte Faktoren sind dagegen kein wissenschaftlicher Fehler, und diese Freiheit entleert die Theorie ihres Informationsgehalts.
- Die für die technische Analyse entscheidende Vorhersage lautet, dass bereits öffentliche, veraltete Information keine Prognosekraft hat; alle von der technischen Analyse genutzte Information gilt als veraltet, also sollten alle ihre Methoden scheitern.
- Die schwache Form, veraltete Preise und daraus abgeleitete Indikatoren wie Preismomentum seien wertlos, stützt sich auf Autokorrelationsstudien; sie bestätigten lineare Unabhängigkeit der Renditen, und EMH-Vertreter schlossen daraus auf einen unvorhersagbaren Random Walk.
- Autokorrelationsstudien entdecken nur lineare Abhängigkeiten; Edgar Peters sowie Andrew Lo und A. Craig MacKinlay zeigen mit anderen Verfahren, dass Finanzzeitreihen sich nicht wie Random Walks verhalten, und die Varianz-Ratio von Lo und MacKinlay kann nichtlineares nichtzufälliges Verhalten sichtbar machen, das Autokorrelationen verborgen bleibt.
- Die EMH muss Überreaktionen und Unterreaktionen auf Nachrichten bestreiten, weil beide eine vorhersagbare Bewegung zurück zum oder hin zum rationalen Niveau erzeugen würden.
- Famas Ereignisstudien zu Unternehmensnachrichten wie Gewinnen, Dividenden, Übernahmen und Fusionen fanden nach der fast sofortigen, nicht ausnutzbaren Anfangsbewegung keine weitere Bewegung und sind damit mit der EMH vereinbar.
- Eine zweite EMH-Vorhersage lautet, dass Preise sich nur ändern, wenn Nachrichten eintreffen, also nicht dramatisch ohne Nachrichten oder als Reaktion auf nichtinformative Ereignisse.
- Gewinne einer Strategie auf veralteter Information widerlegen die EMH erst nach Risikoadjustierung: 20 Prozent im Jahr gegen 10 Prozent des Benchmarks sind kein Sieg, wenn die Strategie das dreifache Risiko zumutet.
- Das CAPM erklärt Renditeunterschiede durch einen Faktor, die Volatilität relativ zum Markt: ist eine Aktie doppelt so volatil, sollte ihre Rendite doppelt so hoch sein, und Überrendite liegt vor, wenn sie mehr als das Doppelte verdient; das misst das Risiko einer einzelnen Aktie oder eines Long-only-Portfolios, nicht das komplexerer Strategien, wofür das APT mehrere unabhängige Risikofaktoren ansetzt.
- Eine Random-Walk-Folge hat kein Gedächtnis. Das Auftreten eines positiven Laufs ändert die Wahrscheinlichkeit des nächsten Ergebnisses in keiner Weise.
- Beobachtet jemand wirklich unabhängige Preisänderungen und glaubt vorher, der Prozess sei zufällig, ist der wahrscheinliche Fehler der Spielerfehlschluss.
- Der gesunde Menschenverstand erwartet bei Zufallsprozessen mehr Wechsel und weniger Läufe, als tatsächlich vorkommen. Nach einem Lauf positiver Preisänderungen schließen naive Beobachter fälschlich, eine Umkehr sei fällig.
- Nach fünfmal Kopf wird fälschlich geschlossen, Zahl sei wahrscheinlicher als 50 zu 50. Am Rouletterad soll eine Serie von Schwarz die Chance von Rot erhöhen. Beides ist falsch.
- Hat der Beobachter keine Vorannahme darüber, ob der datenerzeugende Prozess zufällig oder nichtzufällig ist, entsteht die Clustering-Illusion: Ordnung wird in Daten gesehen, die tatsächlich ein Random Walk sind.
- Kleine Stichproben eines Random Walk wirken oft trendförmiger, als der gesunde Menschenverstand erwartet, analog zur heißen Hand im Basketball.
- Eine Folge positiver Preis- oder Gewinnänderungen wird dann fälschlich als legitimer Trend gelesen, obwohl sie nur ein gewöhnlicher Lauf in einem Random Walk ist.
- Welcher der beiden Fehler entsteht, der Spielerfehlschluss oder die Clustering-Illusion, hängt von der Vorannahme des Beobachters über den beobachteten Prozess ab.
- Der Fehler der kleinen Zahlen missachtet, wie viele Beobachtungen eine Stichprobe enthält. Aus zehn Münzwürfen mit siebenmal Kopf auf eine Kopfwahrscheinlichkeit von 0,7 zu schließen, ist unzulässig.
- Die wahre Kopfrate einer Münze lässt sich verlässlich nur aus einer großen Zahl von Würfen schließen. Eine kleine Gruppe positiver Quartale kann leicht in einem zufälligen Gewinnstrom vorkommen.
- Anleger, die die Stichprobengröße vernachlässigen, täuschen sich leicht, wenn sie entscheiden, ob eine Zeitreihe zufällig ist, und können aus zu wenig Evidenz voreilig einen gültigen Wachstumstrend schließen.
- Das Random-Walk-Modell der Effizienzmarkthypothese sagt voraus, dass systematisches Preisverhalten im Markt nicht beobachtet werden sollte. Die später beschriebenen Hypothesen der Behavioral Finance sagen systematisches Preisverhalten voraus und bieten eine Erklärung, warum es auftreten sollte.
- Keine der Hypothesen ist eine umfassende Theorie des Marktverhaltens, aber sie teilen eine für die technische Analyse wichtige Botschaft: Es gibt guten Grund zur Annahme, dass Finanzmärkte nicht vollständig Random Walks sind.
- Im Modell von Barberis, Shleifer und Vishny folgt der Gewinnstrom einem Random Walk, die Anleger erkennen das aber nicht und ziehen die Möglichkeit eines Random Walk nicht in Betracht. Sie glauben, die Gewinne wechselten zwischen Wachstumstrend und Mean Reversion.
- Ein Random Walk zeigt weniger Mean Reversion als ein echt mittelwertumkehrender Prozess und kürzere Läufe als die eines echt trendenden Prozesses. Dreimal derselbe Ausgang in Folge ist in einem Zufallsprozess nicht ungewöhnlich.
- Nur unter einer speziellen Bedingung erzwingt Markteffizienz notwendig, dass die Preisbewegung zufällig und damit unvorhersagbar ist: wenn alle Anleger dieselbe Haltung zum Risiko haben. Diese Bedingung ist schlicht nicht plausibel.
- Hätten alle Menschen dieselbe Risikohaltung, gäbe es entweder zu viele Testpiloten und Höhenarbeiter oder zu wenige, und entweder würden alle Fallschirm springen und mit Alligatoren ringen oder niemand.
- Es gibt spezielle statistische Verfahren wie den Runs-Test, die Abweichungen von zufälligem Verhalten erkennen.
- Die Beispiele von Roberts enthielten keine Volumendaten, obwohl manche behaupten, Volumen sei für die Mustererkennung notwendig.
- Sind Ereignisse unabhängig, hat das Eintreten eines Ereignisses keinen Einfluss auf das Eintreten eines anderen. Flugzeugabstürze werden als unabhängige Ereignisse genannt.
- Sind Ereignisse abhängig, macht das Eintreten eines Ereignisses ein weiteres wahrscheinlicher. Ein Erdbeben wird typischerweise von einer Reihe kleinerer Beben, den Nachbeben, gefolgt.
- Beschreibungen der schwachen Effizienzmarkthypothese weichen voneinander ab. Manche sagen, nur historische Preisdaten könnten keine Überrenditen erzeugen. Andere Fassungen sagen, keine veralteten Marktdaten, also Preis, Volumen oder irgendeine andere von der technischen Analyse studierte Reihe, könnten Überrenditen erzeugen.
- Samuelson lieferte 1965 einen Beweis, dass richtig antizipierte Preise zufällig schwanken, Proof That Properly Anticipated Prices Fluctuate Randomly, Industrial Management Review 6, Seiten 41–49.
- Der Text stellt die Position dar, dass Random Walks keine notwendige Folge der Effizienzmarkthypothese sind und dass die Effizienzmarkthypothese Preisprognostizierbarkeit zulassen kann.
- In einer zufälligen Reihe fallen die Korrelationen der Preisänderungen mit dem Lag typischerweise sehr schnell. Unterscheiden sich einige Autokorrelationskoeffizienten signifikant von diesem Muster, ist die Reihe der Preisänderungen linear nichtzufällig.
- In echten Random-Walk-Prozessen enthalten frühere Beobachtungen keine Prognoseinformation. In echt trendenden und in echt mean-reverting Prozessen enthalten sie welche.
- Echte Trends sind Strähnen, die länger dauern als die in Random Walks. Echte Mean Reversion bedeutet kürzere Strähnen, also häufigere Wechsel zwischen positiven und negativen Ergebnissen.
- Es gibt drei Formen der Effizienzmarkthypothese: die starke, die halbstrenge und die schwache Form.
- Die starke Form behauptet, dass keine Information, auch keine Insiderinformation, benutzt werden kann, um den Markt auf risikobereinigter Basis zu schlagen.
- Die starke Form ist nicht testbar, weil nicht zuverlässig feststellbar ist, wer was wusste und wann er es wusste. Die Aussagen derer, die auf Insiderinformation handeln, sind notorisch unzuverlässig.
- Die schwache Form spricht typischerweise nur über vergangene Preise und vergangene Preisänderungen. Aronson meint, ihre Vertreter würden zusätzlich behaupten, dass auch jede andere von der technischen Analyse genutzte Datenreihe für die Prognose künftiger Renditen nutzlos sei.
- Ein Verwalter ohne Können hat eine Wahrscheinlichkeit von 0,5, den Markt in einer gegebenen Zeitperiode, zum Beispiel einem Jahr, zu schlagen.

## Funktionsweise

- Die Hot Hand, eine angebliche Serie überdurchschnittlicher Treffsicherheit, ist nach strenger statistischer Analyse der Spielerleistung eine Illusion; die Intuition erwartet zu Unrecht, dass Zufallsprozesse wechseln statt zu serien.
- Ob ein Wurf trifft, bestimmen nichtzufällige Faktoren, vor allem das Können der beteiligten Spieler, und nicht die jüngste Trefferquote; dass die Serien nicht länger sind, als der Zufall erlaubt, bedeutet nicht, die Leistung sei zufallsbestimmt.
- Das Nervensystem sieht Formen, ob sie real sind oder nicht; John Elder nennt das den Effekt, Hasen in den Wolken zu sehen.
- Intuitive Urteile in hoch unsicheren Lagen wie den Finanzmärkten sind verzerrungsanfällig, und die spezifische Verzerrung subjektiver Techniker ist, Trends und Muster auch dort zu sehen, wo diese Strukturen nicht wirklich vorliegen.
- Die fehlerhafte Kette lautet: Zufallsdaten sollten formlos und ohne Muster aussehen; dieses Bild gelte für jede Stichprobe unabhängig von der Beobachtungszahl; eine kleine Stichprobe passt nicht dazu; also sei sie nichtzufällig erzeugt; nichtzufällige Prozesse seien prognostizierbar, also lohne die Suche nach Mustern.
- Der Hauptfehler dieser Kette ist die Missachtung der Stichprobengröße und damit des Gesetzes der großen Zahlen.
- Auf Basis der Repräsentativität wird angenommen, ein zufälliger Prozess müsse Daten erzeugen, die zufällig aussehen; jede Abweichung von diesem Stereotyp wird als Zeichen eines nichtzufälligen Prozesses gelesen.
- Aktiencharts entsprechen der intuitiven Vorstellung von Ordnung; ob eine prognostizierbare Struktur per Augenschein erkannt werden kann, ist damit nicht beantwortet, denn Märkte können teilweise nichtzufällig sein.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Der Variance-Ratio-Test prüft die Null, dass der Hurst-Exponent wirklich 0,5 ist; h gleich 1 verwirft den Random Walk auf 90 Prozent, h gleich 0 lässt ihn zu.

## Risiken und Grenzen

- Eine Handelsregel auf einem Random Walk über historische Simulationen zu kalibrieren, führt zu Backtest-Overfitting, weil eine zufällig günstige Schwellenkombination gewählt wird.
- Backtests auf synthetischen Daten sollen verhindern, dass eine Strategie nur wegen eines statistischen Ausreißers auf einem einzelnen historischen Pfad gewählt wird.
- Diese Ergebnisse bedeuten nicht, dass Finanzmärkte zufällig und ohne gültige Trends und Muster sind; es gibt solide empirische Evidenz für Muster mit Vorhersagekraft.
- Die visuelle Inspektion ist trotzdem ein unzureichendes Mittel, solche Muster zu entdecken oder ihre Echtheit zu prüfen: Eine Methode, die echte Charts nicht von Fälschungen trennen kann, kann die echten nicht verlässlich analysieren.
- Finanzmärkte können in einem gewissen Grad nichtzufällig und damit prognostizierbar sein; die offene Frage ist, ob diese Struktur durch Augenschein und intuitive Beurteilung erkannt werden kann.
- Die Repräsentativitätsheuristik erzeugt ein falsches Stereotyp davon, wie Zufallsdaten aussehen sollten, nämlich formlos, ungeordnet und ohne jeden Trend; weicht eine Stichprobe davon ab, wird sie automatisch für das Produkt eines nichtzufälligen Prozesses gehalten.
- Man erwartet, die Wirkung ähnele der Ursache: Ist der erzeugende Prozess zufällig, sollten die Daten zufällig aussehen, und jede Abweichung von diesem Bild gilt als Zeichen eines nichtzufälligen Prozesses.
- Malkiel hält den Markt für zufällig; der Text teilt diese extreme Position nicht, stimmt aber zu, dass Menschen Ordnung in zufälligen Daten falsch wahrnehmen, und deshalb ist die visuelle Inspektion von Preischarts nicht vertrauenswürdig.

## Beispiele

- USD.CAD sieht in der Abbildung nicht stationär aus; die ADF-Statistik von etwa minus 1,84 verwirft die Null auf 90 Prozent nicht, der kritische Wert ist minus 2,594, und die AR(1)-Schätzung liegt bei 0,994120.
- Der Variance-Ratio-Test auf den Logpreisen von USD.CAD ergibt h gleich 0 und pValue gleich 0,367281, also rund 37 Prozent Wahrscheinlichkeit, dass die Reihe ein Random Walk ist.
- λ ist bei USD.CAD dennoch negativ, die Reihe trendet also zumindest nicht, und der Hurst-Exponent von 0,49 deutet auf schwache Mean Reversion.
- Bei Arditti unterschieden Chartisten echte Charts, gemischt mit Random-Walk-Charts, nicht genauer als ein Raten.
- Siegel legte vier echte und vier zufällige Charts, Abbildung 2.18, Wall-Street-Maklern vor, die sich für kompetente Chartleser hielten; sie konnten echt und zufällig nicht verlässlich trennen, und die echten Charts sind mit X markiert.
- Wirtschaftsstudenten, die gerade einen Kurs in technischer Analyse abgeschlossen hatten, lagen in einem gleichartigen Versuch auf dem Niveau des Ratens.
- Ein durchschnittlicher Basketballspieler trifft etwa 50 Prozent seiner Würfe; bei 20 Würfen in einem Spiel ist die Chance gut, vier, fünf oder sogar sechs Treffer in Folge zu haben, und was als Hot Hand gilt, ist dann nur eine für eine Zufallsfolge typische Serie.
- Eine formale Analyse der V-1- und V-2-Einschläge in London zeigte, dass sie vollständig mit einem Zufallsmuster vereinbar waren, obwohl die Karten sofort Cluster sehen ließen.
- Bei 5.000 Census Tracts in Kalifornien und 80 möglichen umweltbedingten Krebsarten liegen manche Tracts allein durch Zufall weit über dem Durchschnitt; manche solcher Cluster gehen wirklich auf Umweltgifte zurück, aber nicht immer und nicht annähernd so oft, wie die Intuition nahelegt.
- Prechter behauptet, das als Expertensystem umgesetzte EWAVES habe profitable Signale erzeugt und solle echte Preishistorien von Pseudopreishistorien eines Zufallsprozesses unterscheiden können. Stand Juni 2006 waren diese Ergebnisse nicht veröffentlicht.
- Ein Test, der echte von zufälligen Preisdaten unterscheidet, würde die Prognosekraft der objektiven Elliott-Wave-Signale nicht belegen. Nach Prechter wird ein getrennter Test dieser Behauptung ebenfalls durchgeführt.
- Scheitern hieße, dass künstlich erzeugte Zufallscharts von echten Preischarts nicht unterscheidbar sind und dass Elliott-Wave-Signale keine Gewinne erzeugen, die Zufallssignalen überlegen sind.
- Selbst wenn Elliott-Wave-Signale für sich genommen nutzlos sind, haben sie sich in einem multivariaten Modell durch Synergien mit anderen Indikatoren als wertvoll erwiesen.

## Unterschiedliche Quellenpositionen

- Lässt sich ein Abschnitt der Marktgeschichte entweder als Random Walk erklären, der sehr wenig annimmt, oder als Elliott-Wellen-Muster mit Wellen in Wellen, goldenen Schnitten, Fibonacci-Folgen und weiteren Komplexitäten, ist der Random Walk vorzuziehen, es sei denn, das Elliott-Wellen-Prinzip prognostiziert genauer als die Random-Walk-Theorie.
- Um ausnutzbare Ordnung zu finden, die in den Schwankungen der Finanzmärkte existieren mag, braucht es strengere Methoden als visuelle Analyse und Intuition.
- Manche Ökonomen halten systematische Preisbewegungen auch dann für möglich, wenn die Märkte vollständig effizient sind. Nichtzufälliges Preisverhalten und die Möglichkeit der Preisvorhersage bedeuten nicht notwendig, dass die Finanzmärkte ineffizient sind.
- Andere Ökonomen sagen es schärfer: Ein gewisses Maß an Vorhersagbarkeit sei nicht nur möglich, sondern nötig, damit Märkte richtig funktionieren. Lo und MacKinlay schreiben in A Non-Random Walk Down Wall Street, Vorhersagbarkeit sei das Öl, das die Zahnräder des Kapitalismus schmiert.
- Grossman und Stiglitz argumentieren, effiziente Märkte müssten Gewinngelegenheiten bieten, um Anleger zu den kostspieligen Tätigkeiten der Informationsverarbeitung und des Handelns zu motivieren, denn genau diese Tätigkeiten treiben die Preise zu rationalen Bewertungen.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]
- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 1–20 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-001-p001-p020|S. 1–20]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 20–39 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-002-p020-p039|S. 20–39]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 39–58 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-003-p039-p058|S. 39–58]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 58–77 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-004-p058-p077|S. 58–77]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 77–96 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-005-p077-p096|S. 77–96]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 96–115 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-006-p096-p115|S. 96–115]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 153–172 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-009-p153-p172|S. 153–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 324–343 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-018-p324-p343|S. 324–343]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 343–362 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-019-p343-p362|S. 343–362]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 362–381 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-020-p362-p381|S. 362–381]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 476–495 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-026-p476-p495|S. 476–495]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]

## Verwandte Themen

- Alexander untersucht in zwei Arbeiten von 1961 und 1964, ob Preisbewegungen in spekulativen Märkten Trends oder Random Walks sind.
- Lo und MacKinlay stellen die Gegenthese in A Non-Random Walk Down Wall Street (1999) dar.
- Malkiel wird mit A Random Walk Down Wall Street angeführt.
