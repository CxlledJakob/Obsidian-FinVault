---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Modelle"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Lineare Regression


## Kurzdefinition

- Die wichtigste Art eines wissenschaftlichen Gesetzes ist die funktionale Beziehung: Die zu prognostizierende abhängige Variable Y ist eine Funktion eines oder mehrerer Prädiktoren X, geschrieben Y gleich f von Xi.

## Kernaussagen

- Die geschätzte Beziehung lautet ES mal 50 gleich minus 0,3906 mal VX mal 1.000 plus 77.150 Dollar, mit ES und VX als Settlement-Preisen.
- Die Standardabweichung der Residuen beträgt 2.047 Dollar.
- Aus der Regression folgt ein Portfolio long 0,3906 Kontrakte VX und long einen Kontrakt ES.
- Die Hedge Ratio der VX-ES-Rollrendite-Strategie stammt aus der Regression der Preise von VX gegen ES in Gleichung 5.11 und nicht aus der Regression ihrer Renditen wie im Original von Simon und Campasano, deshalb weicht sie leicht von deren Angabe ab.
- Wenn Experten mehrfaktorielle Entscheidungen subjektiv treffen, stützen sie sich vor allem auf eine lineare Kombinationsregel, aber weniger wirksam als formale lineare Regressionsmodelle.
- Sie sind weniger wirksam, weil sie die Information nicht so konsistent kombinieren wie ein formales mathematisches Modell.
- In einem sequenziellen Problem lässt sich jede Variable für sich deuten, und die Einzelbotschaften werden danach algebraisch addiert; die Botschaft einer Variable hängt dann nicht von den anderen ab.
- In einem konfigurativen Problem steckt die Information im Beziehungsgeflecht der Variablen, die sich nicht isoliert bewerten lassen: ein hoher Wert von A kann bei niedrigem B und hohem C etwas anderes bedeuten als bei hohem B und niedrigem C.
- Eine lineare Funktion ist vergleichsweise einfach, weil sie nur durch zwei Koeffizienten oder Freiheitsgrade definiert ist: ihre Steigung und den Schnitt mit der senkrechten Achse, den y-Achsenabschnitt. Verbessern lässt sich der Fit nur über diese beiden Größen.
- Eine Funktion lässt sich als mathematische Hypothese auffassen, die eine gegebene Menge von Beobachtungen erklärt.
- Wird eine Funktion mit der Methode der Kleinste-Quadrate-Regression an Daten angepasst, ist ein perfekter Fit garantiert, wenn sie so viele Freiheitsgrade, also Koeffizienten, enthalten darf, wie es Datenpunkte gibt.
- Die lineare Funktion berührt nicht jeden beobachteten Punkt, beschreibt aber die allgemeine Tendenz, dass steigende X-Werte mit steigenden Y-Werten einhergehen. Damit erfasst sie das wesentliche Merkmal und ist eher die echte Beziehung zwischen X und Y.
- Unter sonst gleichen Bedingungen ist die einfachere Erklärung eher richtig. Eine aufwendige Kurve kann gerechtfertigt sein, wenn genug Daten vorliegen und ein komplexer Prozess sie erzeugt hat.
- Bei Camerer waren die subjektiven Urteile der Experten am ungenauesten und die mit Regressionsanalyse geschätzten multivariaten linearen Modelle am genauesten, genauer auch als ein mathematisches Modell davon, wie die Experten ihre Urteile bildeten.
- Goldberg zeigte 1968, dass ein lineares Prognosemodell auf Persönlichkeitstestwerten neurotische von psychotischen Patienten besser trennte als erfahrene klinische Diagnostiker.
- Das Modell von Goldberg traf zu 70 Prozent, die Treffer der Experten lagen zwischen 52 und 67 Prozent.

## Funktionsweise

- Die Preisänderung wird als lineares Modell geschrieben: Δy(t) gleich λ mal y(t−1) plus μ plus βt plus den Lag-Differenzen α1 Δy(t−1) bis αk Δy(t−k) plus einem Störterm, mit Δy(t) gleich y(t) minus y(t−1).
- Die ADF-Statistik ist der Koeffizient λ aus der Regression von Δy(t) auf y(t−1), geteilt durch den Standardfehler dieses Fits.
- Ignoriert man Drift und Lag-Differenzen, trägt das in der diskreten Regression bestimmte λ in die stetige Ornstein-Uhlenbeck-Form hinüber.
- λ wird geschätzt, indem y(t) minus y(t−1) auf y(t−1) und eine Konstante regressiert wird; die Halbwertszeit ist minus log(2) geteilt durch den ersten Beta-Koeffizienten.
- Die optimale Hedge Ratio zweier Reihen ist der erste Koeffizient der Regression der abhängigen Reihe auf die unabhängige Reihe und eine Konstante.
- Die Halbwertszeit des Portfolios wird bestimmt, indem die Änderung des Nettomarktwerts auf dessen verzögertes Niveau und eine Konstante regressiert wird.
- Die Halbwertszeit ist minus log(2) geteilt durch den ersten Regressionskoeffizienten.
- Die Hedge Ratio eines Paares kommt aus einer gewöhnlichen Kleinste-Quadrate-Regression oder aus dem ersten Johansen-Eigenvektor.
- Für GLD und USO wird sie jeden Tag neu geschätzt, als Regression der letzten 20 Beobachtungen der einen Reihe auf die andere Reihe und eine Konstante.
- Für den Log-Preis-Spread wird dieselbe Regression auf den Logpreisen gerechnet, und der Portfoliowert ist die gewichtete Summe der Logpreise.
- Für ein wirklich kointegrierendes Paar wird die Regression einmal auf möglichst langer Historie gerechnet.
- Die Messgleichung des Kalman-Filters ist die lineare Beziehung y(t) gleich x(t) mal β(t) plus Rauschen, mit β aus Achsenabschnitt und Steigung.
- Unter der Annahme konstanter Spot- und Roll-Rendite schätzt eine lineare Regression beide: der Log des Spotpreises wird gegen die Zeit regressiert, und die annualisierte durchschnittliche Spot-Rendite ist 252 mal dem Mittel des Steigungskoeffizienten.
- Die Roll-Rendite verlangt einen festen Zeitpunkt und die Regression der Kontraktpreise gegen die Restlaufzeit; praktisch hängt der Koeffizient von diesem Zeitpunkt und von den dann verfügbaren Kontrakten ab, sodass das geschätzte γ trotz der Konstanzannahme langsam variiert.
- Im Programm werden je Tag die Logpreise der fünf nächsten Laufzeiten auf die Restlaufzeit in Monaten regressiert, sofern fünf aufeinanderfolgende Kontrakte vorliegen, und γ ist minus 12 mal dem Steigungskoeffizienten.
- Das Modell setzt F(t, T) gleich S(t) mal exp(γ mal (t minus T)), S(t) gleich c mal e hoch αt, und damit die Gesamtrendite ∂(log F)/∂t gleich α plus γ sowie die Roll-Rendite minus ∂(log F)/∂T gleich γ.
- Die Halbwertszeit von γ kommt aus der Regression der Änderung von γ auf den verzögerten γ-Wert und eine Konstante und ist minus log(2) geteilt durch den Steigungskoeffizienten.
- Typischerweise sind die Werte der Prädiktoren bekannt und der Wert von Y nicht, oft weil Y ein künftiges Ergebnis ist und die X-Werte aktuell bekannt sind.
- Ist die Beziehung einmal gewonnen, lassen sich Werte der abhängigen Variable prognostizieren, indem die bekannten Prädiktorwerte eingesetzt werden.
- Funktionale Beziehungen werden entweder aus erklärenden Theorien abgeleitet oder aus historischen Daten durch Funktionsanpassung geschätzt, zum Beispiel durch Regressionsanalyse.
- Kaufman diskutiert eine objektive Divergenzmethode, die die Steigungen der beiden verglichenen Zeitreihen per linearer Regression schätzt und die Divergenz als Differenz dieser Steigungen definiert.
- Er stellt Computercode dafür bereit, bietet aber keine Leistungsstatistiken.
- Die Kointegrationsmessung von Divergenzen nutzt eine Regressionsanalyse, um festzustellen, ob zwischen zwei Zeitreihen eine lineare Beziehung besteht.
- Das Error-Correction-Modell misst die Abweichung von dieser typischen linearen Beziehung; wird der Fehler extrem, soll er auf seinen normalen Wert null zurückkorrigieren.
- Der Fosback Index signalisiert, wenn die Cash-Quote der Fonds deutlich von dem Niveau abweicht, das die lineare Beziehung zu den kurzfristigen Zinsen vorhersagt.
- Neben der einfachen linearen Kombination gibt es anspruchsvollere lineare Kombinationen, in denen den Variablen Gewichte zugewiesen werden, also eine gewichtete algebraische Summe.
- Algebraisch meint hier, dass Zahlen mit positiven und mit negativen Werten kombiniert werden.

## Voraussetzungen


## Anwendung im Trading

- Die technische Analyse ist derzeit vor allem auf die Schätzung aus historischen Daten beschränkt, weil Theorien der technischen Analyse gerade erst formuliert werden.
- Fosback entfernte mit einer Regression den störenden Einfluss der Kurzfristzinsen auf die Barreserven, als er Optimismus und Pessimismus von Fondsmanagern maß, und erhielt so den Fosback-Index als unverfälschtes Maß der Managerpsychologie.
- Jacobs und Levy nutzten multiple Regression, um die Störeinflüsse mehrerer Variablen zu mindern, und leiteten daraus bereinigte Indikatoren für die Prognose der relativen Aktienperformance ab.
- Alpha im Capital-Asset-Pricing-Modell ist der Achsenabschnitt aus der Regression der Strategierenditen auf die Renditen eines Marktindex.
- Kaufman vergleicht die Steigung der linearen Regression als Trendfolge-Methode mit Channel-Breakout, exponentieller Glättung, Swing-Breakout und Point-and-Figure. An Eurodollars von 1985 bis 1994 hatte Channel-Breakout die höchste risikobereinigte Performance.
- Das Arbitrage-Pricing-Modell sagt, ein lineares Modell verknüpfe die Rendite einer Aktie mit einer Reihe von Faktoren, und diese Beziehung entstehe, weil Arbitrageure nach risikolosen Gelegenheiten mit Investment null suchen.
- Der Indikator der Beziehung zweier Reihen ist die Zeitreihe der Residuen der linearen Beziehung zwischen ihnen.
- Der Operator YY normiert seine Werte mit dem Standardfehler der Regression und führte keinen expliziten Test auf die Stationarität der Residuen durch.

## Regeln und Kriterien

- Werden die Rollen von EWA und EWC vertauscht, ist die neue Hedge Ratio nicht der genaue Kehrwert der alten.
- Für das Johansen-Portfolio wird die Halbwertszeit mit derselben Regression bestimmt, nur dass yport an die Stelle von y tritt.
- Ein kurzes gleitendes Regressionsfenster ändert den Koeffizienten abrupt, wenn eine alte Beobachtung herausfällt und eine neue hinzukommt.
- Der exponentielle gleitende Durchschnitt gewichtet neue Daten stärker, aber es ist nicht klar, warum gerade ein exponentieller Abfall optimal ist.
- δ gleich 0 im Kalman-Filter reduziert die fortlaufende Schätzung auf OLS mit festem Offset und fester Steigung.
- Die Regressionskoeffizienten werden nur für die ersten 500 Tage der Daten nach August 2008 geschätzt.
- Vor der Regression werden die VX-Preise mit 1.000 und die ES-Preise mit 50 multipliziert, weil ein Punkt VX 1.000 Dollar und ein Punkt ES 50 Dollar bewegt.
- Eine lineare Regression auf der Mischung der Regime 2004 bis Mai 2008 und August 2008 bis 2012 wäre ein Fehler.

## Risiken und Grenzen


## Beispiele

- Die Regression auf USD.CAD liefert eine Halbwertszeit von etwa 115 Tagen.
- Dieselbe Regression auf dem EWA-EWC-IGE-Portfolio des ersten Eigenvektors liefert eine Halbwertszeit von 23 Tagen.
- Für das Portfolio aus dem ersten Eigenvektor von EWA, EWC und IGE beträgt die so geschätzte Halbwertszeit 23 Tage, gegenüber etwa 115 Tagen bei USD.CAD.
- Der Lookback von 20 Handelstagen für GLD gegen USO ist mit Wissen im Nachhinein nahe am Optimum gewählt.
- Dieselbe Preis-Spread-Regression arbeitet im Beispiel deutlich besser als die Regression der Logpreise und als das einfache Verhältnis.
- Die Log-Future-Preise von CL gegen die Restlaufzeit fallen zu einem festen Zeitpunkt, hier die Kontrakte Januar bis Mai 2007 und nur die fünf nächsten, recht sauber auf eine Gerade; weiter entfernte Laufzeiten können von Gleichung 5.7 abweichen.
- Positive γ zeigen Backwardation, negative Contango; für CL sind die annualisierten γ vom 22. November 2004 bis 13. August 2012 geplottet.
- Haben von sieben Variablen mit den Werten +1 oder −1 fünf den Wert +1 und zwei den Wert −1, ist die lineare Kombination +3, also (+5) + (−2).
- Eine lineare Kombination dreier binärer Variablen kann nur vier verschiedene Werte annehmen, während drei binäre Variablen acht verschiedene Konfigurationen bilden.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 39–58 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-003-p039-p058|S. 39–58]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 96–115 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-006-p096-p115|S. 96–115]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 210–229 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-012-p210-p229|S. 210–229]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 419–438 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-023-p419-p438|S. 419–438]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 457–476 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-025-p457-p476|S. 457–476]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]

## Verwandte Themen
