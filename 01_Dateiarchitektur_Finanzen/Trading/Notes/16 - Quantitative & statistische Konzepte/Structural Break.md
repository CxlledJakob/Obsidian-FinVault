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

# Structural Break


## Kurzdefinition

- Ein Structural Break entsteht, wenn ein Ereignis die Natur der untersuchten Zeitreihe verändert und nicht sachgerecht behandelt wird.
- Ein Strukturbruch ist der Übergang von einem Marktregime in ein anderes, zum Beispiel von einem Mean-Reversion-Muster zu einem Momentum-Muster.
- Sub- und Super-Martingal-Tests prüfen eine explosive Zeittrendkomponente, ohne die übliche ADF-Spezifikation zu verwenden.

## Kernaussagen

- Unbehandelt leitet ein solcher Bruch die Forschung fehl.
- Das Problem tritt auf bei Spreads mit wechselnden Gewichten, bei Körben mit wiederangelegten Dividenden oder Kupons, bei Rebalancing, bei Wechseln der Indexmitglieder und beim Ersatz ausgelaufener Kontrakte.
- Portfolio-Manager setzen eine Wette typischerweise nach einem Ereignis wie einem Strukturbruch, einem extrahierten Signal oder einem mikrostrukturellen Phänomen.
- Diese Ereignisse können mit einer Makroveröffentlichung, einem Volatilitätssprung oder einer deutlichen Abweichung eines Spreads vom Gleichgewicht verbunden sein.
- Strukturbruchtests fallen in CUSUM-Tests und Explosivitätstests.
- CUSUM-Tests prüfen, ob kumulative Prognosefehler signifikant von weißem Rauschen abweichen.
- Explosivitätstests prüfen, ob der Prozess exponentiell wächst oder kollabiert, was mit Random Walk oder Stationarität unvereinbar und auf Dauer unhaltbar ist.
- Explosivitätstests unterteilen sich in Right-Tail-Unit-Root-Tests unter einer autoregressiven Spezifikation und in Sub- oder Super-Martingal-Tests unter verschiedenen Funktionsformen.
- Zusätzlich unterscheiden sich Explosivitätstests danach, ob sie eine Blase oder mehrere Blasen zulassen.
- Blasen umfassen hier nicht nur Kursanstiege, sondern auch Ausverkäufe.
- Ein Zyklus aus Blase, Platzen und neuer Blase lässt die Reihe für Ein-Blasen-Tests stationär erscheinen, deshalb sind Mehr-Blasen-Tests robuster.
- Strukturbrüche bieten einige der besten Chance-Risiko-Verhältnisse, weil die Verliererseite ihren Fehler typischerweise zu spät erkennt.

## Funktionsweise

- Der Brown-Durbin-Evans-Test schätzt rekursive Kleinste Quadrate auf wachsenden Teilstichproben und bildet standardisierte Ein-Schritt-Prognoseresiduen.
- Unter einer konstanten Beta ist die CUSUM-Statistik des Brown-Durbin-Evans-Tests normalverteilt mit Mittelwert 0 und Varianz t minus k minus 1.
- Der Chu-Stinchcombe-White-Test lässt die Features weg, setzt die Null auf keine prognostizierte Änderung und arbeitet direkt mit den Logpreis-Niveaus.
- Die standardisierte Abweichung des Chu-Stinchcombe-White-Tests ist unter der Null standardnormal.
- Der einseitige kritische Wert dieses Tests ist die Quadratwurzel aus der Summe von b und dem Logarithmus des Abstands der beiden Zeitpunkte.
- Der Chow-Typ-Dickey-Fuller-Test schätzt die Differenz der Reihe auf den verzögerten Stand mal einer Dummyvariablen, die vor dem Bruch 0 und ab dem Bruch 1 ist.
- Die Prüfgröße ist der geschätzte Koeffizient geteilt durch seine Standardabweichung, und bei unbekanntem Bruchdatum nimmt Andrews das Supremum über ein inneres Intervall.
- SADF ist an jedem Endpunkt das Supremum der ADF-Statistiken über rückwärts expandierende Startpunkte bei festem rechtem Rand.
- Der gewöhnliche ADF ist der Spezialfall, in dem die minimale Länge gleich Endpunkt minus 1 ist.
- SADF wird an jedem zulässigen Endpunkt berechnet, der Chow-Supremumstest nur am Stichprobenende, und SADF führt keine Dummyvariable ein.
- QADF ersetzt das Supremum durch ein Quantil der ADF-Werte im Fenster und misst die Dispersion als Abstand der Quantile q plus v und q minus v.
- Der bedingte ADF ist der Mittelwert der ADF-Werte oberhalb eines Quantils und ist nach Konstruktion höchstens so groß wie SADF.
- Die Null ist Beta gleich 0, die Alternative Beta ungleich 0, unter polynomialen, exponentiellen oder Potenztrends.
- Das Polynom ersten Typs regressiert den Stand auf eine Konstante, einen linearen Trend und ein Quadrat der Zeit.
- Das Polynom zweiten Typs regressiert den Logpreis auf eine Konstante, einen linearen Trend und ein Zeitquadrat.
- Der exponentielle Trend schreibt den Stand als Alpha mal e hoch Beta t, gleichbedeutend mit einem linearen Trend im Logpreis.
- Der Potenztrend schreibt den Stand als Alpha mal t hoch Beta, gleichbedeutend mit einem Log-Zeit-Trend im Logpreis.
- Wie bei SADF wird jede Spezifikation an jedem Endpunkt mit rückwärts expandierenden Startpunkten geschätzt, und die Statistik ist das Supremum des Betrags der t-Statistik von Beta.
- Der Betrag wird verwendet, weil explosives Wachstum und Kollaps gleichermaßen interessieren.
- Gegen die Bevorzugung langer Fenster wird die t-Statistik zusätzlich durch die Fensterlänge hoch Phi geteilt, mit Phi zwischen 0 und 1.

## Voraussetzungen

- Am Anfang und am Ende müssen mögliche Bruchpunkte ausgespart werden, damit jedes Regime mit genug Beobachtungen geschätzt wird.
- Für die gezeigte SADF-Schätzung werden Logpreise, eine minimale Stichprobenlänge, eine Trendvorgabe und die Lagzahl gebraucht.
- Die Trendvorgabe ist entweder nur eine Konstante, eine Konstante plus linearer Trend oder eine Konstante plus quadratischer Trend.

## Anwendung im Trading

- Der ML-Algorithmus soll lernen, ob es unter diesen Umständen eine treffende Prognosefunktion gibt.
- Ein CUSUM-Filter kann ein Ereignis markieren, wenn eine Strukturbruchstatistik wie SADF ausreichend von einem vorherigen Reset-Niveau abweicht.
- Bevor die Verliererseite den Verlust akzeptiert, hält sie die Position, hofft auf eine Rückkehr und vergrößert sie manchmal, bis sie zum Stop gezwungen wird.
- Die SADF-Linie des E-mini S&P 500 nach dem ETF-Trick springt bei blasenartigem Verhalten und fällt, wenn die Blase platzt.

## Regeln und Kriterien

- Für den einseitigen Chu-Stinchcombe-White-Test ist die per Monte Carlo bestimmte Konstante b bei Alpha 0,05 gleich 4,6.
- Im Null-Lag-Modell auf Logpreisen ist der Zustand bei Beta kleiner als 0 steady mit Grenzwert minus Alpha geteilt durch Beta, bei Beta gleich 0 ein Martingal und bei Beta größer als 0 explosiv.
- Bei Beta kleiner als 0 ist die Halbwertszeit im steady-Zustand der Quotient aus minus dem Logarithmus von 2 und dem Logarithmus der Summe aus eins und Beta.
- Bei Beta größer als 0 ist der erwartete Logpreis gleich minus Alpha geteilt durch Beta, plus (eins plus Beta) hoch t mal der Summe aus dem Logarithmus des Startpreises und dem Bruch Alpha durch Beta.
- SADF testet die Null Beta kleiner oder gleich 0 gegen die Alternative Beta größer als 0.
- Ein Beispiel für QADF ist das Quantil 0,95 mit v gleich 0,025, und SADF selbst ist das Quantil 1, dessen Dispersion nicht definiert ist.
- Für den bedingten ADF nennt der Text als Beispiel das Quantil 0,95.
- Bei Phi gleich 0,5 wird in der einfachen Regression die mit der Fensterlänge sinkende Standardabweichung von Beta ausgeglichen.
- Geht Phi gegen 0, zeigt die Statistik längere Trends, weil langfristige Blasen kurzfristige überdecken.
- Geht Phi gegen 1, wird die Statistik rauschiger, weil mehr kurzfristige Blasen ausgewählt werden.
- Phi ist damit ein Filter auf Gelegenheiten mit einer bestimmten Haltedauer, und als Merkmale können Schätzungen über viele Phi-Werte dienen.
- Wenn eine Strategie aufhört zu funktionieren, wird eine Hypothese über den Grund gebildet und empirisch geprüft, ob die Daten sie stützen; das Ergebnis ist oft eine geänderte Strategie, die wieder profitabel wird.
- Selbst wenn ein Triplet zu umständlich ist, soll eine Regel den Handel von GLD gegen GDX beenden, sobald der Ölpreis eine bestimmte Schwelle überschreitet.
- Regression und Johansen-Test dürfen nicht auf der Mischung beider ES-VX-Regime laufen.

## Risiken und Grenzen

- Beim Brown-Durbin-Evans-Test ist der Startpunkt willkürlich, und die Ergebnisse können dadurch inkonsistent sein.
- Beim Chu-Stinchcombe-White-Test ist das Referenzniveau etwas willkürlich, als Abhilfe dient das Supremum über rückwärts verschobene Fenster.
- Chow unterstellt nur ein Bruchdatum, und die Blase läuft bis zum Stichprobenende ohne Rückkehr zum Random Walk.
- SADF als Supremum der ADF-Werte reagiert empfindlich auf die Abtastfrequenz und die konkreten Zeitstempel.
- Wächst SADF über minus 1,5, zeigen sich im Vergleich zum bedingten ADF horizontale Verläufe, passend zu einer plötzlichen Verbreiterung des rechten Randes.
- Ausreißer verzerren SADF nach oben, auch wenn der bedingte Mittelwert noch klein ist.
- Der SADF-Algorithmus läuft quadratisch in der Stichprobenlänge.
- In der Literatur werden Strukturbruchtests oft auf Rohpreisen gerechnet, bei langen Reihen mit Blasen sind aber Logpreise vorzuziehen, weil sonst die Renditevarianz vom Preisniveau abhängt.
- In der einfachen Regression geht die Standardabweichung von Beta mit der Fensterlänge gegen 0, weil die Varianz von Beta die Restvarianz geteilt durch die Trendvarianz mal die Fensterlänge ist.
- Deshalb kann eine schwache langfristige Blase eine kleinere Standardabweichung haben als eine starke kurzfristige Blase und die Methode zu langfristigen Blasen verzerren.
- Dasselbe Grenzresultat gilt für die multivariate lineare Regression.

## Beispiele

- Für Dollar Bars des E-mini S&P 500 mit 356.631 Beobachtungen und drei Regressoren braucht eine ADF-Schätzung 11.412.245 Gleitkommaoperationen.
- Ein einzelnes SADF-Update braucht dafür rund 2,035 TFLOPs und die volle Reihe rund 242 PFLOPs, ohne Alignment, Vorverarbeitung und Ein- und Ausgabe.
- Dafür kann ein parallelisierter HPC-Cluster nötig sein, Parallelisierungsstrategien stehen in Kapitel 20.
- Der Kehrwert jedes Preises verwandelt Blasen in Einbrüche und Einbrüche in Blasen.
- GLD gegen GDX kointegriert vom 23. Mai 2006 bis 14. Juli 2008 mit 99 Prozent Wahrscheinlichkeit und verliert die Kointegration vom 15. Juli 2008 bis 9. April 2012.
- Am 14. Juli 2008 erreichte WTI etwa 145 Dollar je Barrel, ein Allzeithoch; teures Öl verteuert die Goldförderung, senkt die Minengewinne und lässt die Minenaktien gegenüber dem Gold-Spot underperformen.
- Nimmt man den Öl-Fonds USO in das Portfolio, kointegrieren GLD, GDX und USO über 2006 bis 2012 laut Johansen mit 99 Prozent Wahrscheinlichkeit in einer Beziehung.
- Um die Finanzkrise 2008 liegt ein Regimewechsel im Verhalten von VIX und seinen Futures, und die VX-Kalenderspread-Strategie läuft vor Oktober 2008 deutlich schlechter.
- Die Beziehung von ES und VX zerfällt in die Regime 2004 bis Mai 2008 und August 2008 bis 2012, mit kürzeren Phasen, die Übergänge sein können.
- Der Crack Spread steigt um den 9. März 2007 bis zum 3. Juli 2008 dramatisch und fällt danach scharf.

## Unterschiedliche Quellenpositionen

- Phillips, Wu und Yu (2011) halten Standard-Unit-Root- und Kointegrationstests für ungeeignet zur Blasenerkennung, weil periodisch zusammenbrechende Blasen wie ein Unit-Root- oder stationärer autoregressiver Prozess aussehen.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 58–77 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-004-p058-p077|S. 58–77]]
- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]
- Advances in Financial Machine Learning.pdf, S. 286–305 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-016-p286-p305|S. 286–305]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]

## Verwandte Themen

- SADF wird im Buch erst in Kapitel 17 definiert, ebenso die weitere Behandlung von Strukturbrüchen.
