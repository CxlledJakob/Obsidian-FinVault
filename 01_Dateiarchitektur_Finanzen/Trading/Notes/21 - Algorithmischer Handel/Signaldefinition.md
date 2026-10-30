---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Systementwicklung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Signaldefinition


## Kurzdefinition

- Das Signal ist der negative Z-Score des Preises des Einheitsportfolios: Nettomarktwert minus gleitender Durchschnitt, geteilt durch die gleitende Standardabweichung, mit negativem Vorzeichen.
- Eine Regel erzeugt ein Signal, wenn sich der Wert der Ausgabezeitreihe ändert.
- Ein Signal verlangt eine Änderung der zuvor empfohlenen Marktposition.
- Das Signal der Regel MA50 lautet: Liegt der Schlusskurs des S&P 500 über einem 50-Tage-Durchschnitt, wird eine Long-Position im S&P 500 gehalten, andernfalls eine Short-Position.
- Die Spezifikationen einer Regel sind die mathematischen oder logischen Operationen auf einer oder mehreren Marktdatenreihen, die sie in eine Zeitreihe der diktierten Positionen überführen.
- Eine Regel verwandelt Eingaben aus einer oder mehreren Zeitreihen in eine Ausgabe aus +1 und −1, die Long und Short im S&P 500 anzeigen. Definiert wird diese Verwandlung durch mathematische, logische oder Zeitreihen-Operatoren.
- Die in der Fallstudie geprüften Regeln fallen in drei Themen der technischen Analyse: Trends, Extremwerte und Übergänge sowie Divergenz.
- Die allgemeinste Form eines Indikatorausdrucks in der Scripting-Sprache ist Indicator gleich Operator(Argument1, Argument2, bis Argumenti), wobei i die Zahl der vom Operator verlangten Argumente ist.

## Kernaussagen

- Ohne objektiv definierte Signale oder Muster und ohne objektiv definierte Maßstäbe für ihre Ergebnisse lassen sich die Zählungen nicht gewinnen, die nötig sind, um die Wirksamkeit des Signals zu bewerten.
- Objektive Definitionen sind die einzige Lösung dieses Problems fehlender Daten.
- Die Alternativhypothese behauptet, MA50 habe Vorhersagekraft und erziele auf trendbereinigten Daten eine erwartete Rendite größer als null. Null ist die erwartete Rendite einer Regel ohne Vorhersagekraft.
- Die Nullhypothese behauptet, die erwartete Rendite von MA50 sei gleich null oder kleiner.
- Die Teststatistik zu diesem Signal ist die mittlere Rendite, die der Backtest der Regel in einer historischen Stichprobe liefert.

## Funktionsweise

- Bei Paar- und anderen Arbitragestrategien hängen die Handelssignale oft von den Differenzen der Preisquotes verschiedener Instrumente ab.
- Bei Währungspaaren ist oft das Ratio statt des Spreads ein guter Indikator.
- Eine praktische Umsetzung einer linearen Handelsstrategie sind Bollinger-Bänder mit Scaling-in.
- Ein Wechsel der Ausgabe von +1 auf −1 verlangt, die bisherige Long-Position zu schließen und eine neue Short-Position zu eröffnen.
- Ein Wechsel von +10 auf +5 verlangt, die Long-Position von 10 Kontrakten auf 5 zu senken, also 5 zu verkaufen.
- Regeln mit Schwelle erzeugen das Signal, wenn die Zeitreihe die Schwelle nach oben oder nach unten kreuzt.
- Bei der Moving-Average-Cross-Regel ist die Ausgabe +1, solange die Zeitreihe über ihrem gleitenden Durchschnitt liegt, und sonst −1.
- Bei einer festen Schwelle von 75 ist die Ausgabe +1, wenn die Reihe über der Schwelle liegt, und −1 zu allen anderen Zeiten.
- Bei mehreren Schwellen löst nicht der bloße Zustand das Signal aus, sondern ein Ereignis: das Kreuzen einer bestimmten Schwelle in einer bestimmten Richtung.
- Das Aufwärtskreuzen der oberen Schwelle setzt +1, und dieser Wert bleibt, bis das Abwärtskreuzen der unteren Schwelle −1 setzt.
- Nach traditioneller Lesart ist das Signal der Moving-Average-Cross-Regel +1, wenn die Reihe über dem Durchschnitt liegt, und −1, wenn sie darunter liegt.
- Die inverse Regel signalisiert genau umgekehrt: −1 oberhalb des Durchschnitts und +1 unterhalb.
- Signale werden aus den tatsächlichen Marktdaten gebildet, nicht aus der detrendeten Reihe; detrendete Daten dienen nur der Renditeberechnung.
- Der technische Analyst legt für das Data Mining die Zielvariable fest, also das Problem, das die Software lösen soll.

## Voraussetzungen

- Es wird angenommen, dass alle vom Verfahren benötigten Marktinformationen bekannt und öffentlich verfügbar sind, wenn das Verfahren die Empfehlung erzeugt.

## Anwendung im Trading


## Regeln und Kriterien

- Der Lookback von Durchschnitt und Standardabweichung wird auf die gerundete Halbwertszeit gesetzt und nicht frei optimiert.
- Der Preis des Einheitsportfolios ist sein Marktwert, analog zum Preis eines Fonds oder ETF.
- Linear bedeutet, dass die Stückzahl proportional zum Z-Score ist, nicht der Marktwert der Anlage.
- Weil diese Regel nur eine Schwelle verwendet, sind die Signale gegenseitig ausschließend und die Zustände erschöpfend: die Reihe liegt entweder darüber oder darunter, und die Signale können nicht miteinander in Konflikt stehen.
- Eine gehaltvolle Prognose muss ausdrücklich oder klar implizit machen, welche Ergebnisse sie als falsch erweisen.
- Eine Prognose, die nicht klar macht, welche künftigen Ereignisse Vorhersagefehler sind, sagt im Kern, dass jedes Ergebnis eintreten kann.
- Drei Wege, einer subjektiven Prognose Gehalt zu geben, sind ein künftiger Bewertungszeitpunkt, das höchste noch zulässige gegenläufige Ausmaß und die Vorhersage eines festgelegten günstigen Ausmaßes vor einem festgelegten ungünstigen Ausmaß, also X Prozent günstig vor Y Prozent ungünstig.
- Die Prüffragen lauten, wie viel gegenläufige Bewegung die Prognose als Irrtum erwiese, welche Ergebnisse ausgeschlossen sind, und wann sowie unter welchen Bedingungen sie bewertet werden kann, etwa nach Zeitablauf, Preisänderung oder einer bestimmten Indikatorentwicklung.
- Die objektiven Regeln stufen einen Kandidaten eindeutig als Schulter-Kopf-Schulter oder als Nicht-Schulter-Kopf-Schulter ein.
- Das Verkaufssignal der Abbildung ist die Kreuzung der Nackenlinie, ein Short-Signal ist aber erst zulässig, nachdem der Zigzag die rechte Schulter erkannt hat.
- Liegt die rechte Schulter nur 4 Prozent über der Nackenlinie und die Filterschwelle bei 10 Prozent, ist ein Einstieg 4 Prozent unter der Schulter kein zulässiges Signal; gewartet wird auf die Bewegung, die die rechte Schulter identifiziert.
- Ohne die Erfüllung von Kopfhöhe, vorherigem Aufwärtstrend, vertikaler und horizontaler Symmetrie sowie der Abschlusszeit gibt es kein gültiges Signal.
- Trendregeln erzeugen Long- und Short-Positionen anhand des aktuellen Trends der von der Regel untersuchten Datenreihe. Der Kanalausbruch geht long, wenn die Reihe das Maximum der letzten n Perioden ohne die aktuelle Periode überschreitet, und short, wenn sie unter das entsprechende Minimum fällt.
- Die getesteten Rückschauen des Kanalausbruchs sind 3, 5, 8, 12, 18, 27, 41, 61, 91, 137 und 205 Tage, getrennt um ungefähr den Faktor 1,5.
- Extrem- und Übergangsregeln erzeugen Long und Short, wenn die untersuchte Reihe einen extrem hohen oder extrem niedrigen Wert erreicht oder wenn sie einen Übergang zwischen Extremwerten vollzieht.
- Divergenzregeln erzeugen Signale, wenn der S&P 500 in die eine Richtung trendet und eine begleitende Datenreihe in die andere. Nach Heiby lag eine Divergenz vor, wenn eine kanalnormierte Reihe über 74 lag, oberes Quartil der 50-Tage-Spanne, und die andere unter 26, unteres Quartil.
- Die Kanalnormierung skaliert die aktuelle Lage im Kanal auf den Bereich 0 bis 100. Am Maximum der Rückschau ist der Wert 100, am Minimum 0, und 50 bedeutet die Mitte. Die Formel teilt die Differenz aus aktuellem Wert und Minimum durch die Differenz aus Maximum und Minimum und multipliziert mit 100.
- Ein linear gewichteter gleitender Durchschnitt über vier Tage glättet Indikatoren, die signalisieren, wenn der Indikator eine kritische Schwelle über- oder unterschreitet. Die Glättung mildert zu viele Signale, die eine ungegättete Fassung durch Hin- und Herpendeln um die Schwelle erzeugen würde.
- Die Grundform einer Indikatorformel in der Skriptsprache ist der Operator, gefolgt von seinen Argumenten. Der gleitende Durchschnitt braucht zwei Argumente, die Datenreihe und die Zahl der Perioden der Rückschau.
- Verschachtelung macht die Ausgabe eines Operators zum Argument des nächsten. Die 60-Tage-Kanalnormierung eines 10-Tage-Durchschnitts des Dow Jones Transportation Index wird als Kanalnormierung des Durchschnitts dieser Reihe geschrieben.
- Zweigs Volumenregel signalisiert Long, wenn das tägliche Verhältnis von Aufwärts- zu Abwärtsvolumen an der NYSE innerhalb von drei Monaten an zwei Fällen den Wert 9 überschreitet.
- Ein Grundsatz der technischen Analyse in diesem Abschnitt ist, dass Preise und Renditen in Trends laufen, die rechtzeitig genug erkennbar sind, um Gewinne zu erzeugen.
- Die Trendregeln nutzen den Channel-Breakout-Operator und geben +1 oder −1 aus; von 40 Reihen wurden 39 verwendet, der Eröffnungskurs des S&P 500 wurde als redundant zum Schluss ausgeschlossen.
- Getestet wurden die Look-backs 3, 5, 8, 12, 18, 27, 41, 61, 91, 137 und 205 Tage, etwa um den Faktor 1,5 gestuft, woraus 858 Trendregeln entstehen, 429 traditionelle und 429 inverse.
- Die Namenssyntax, verschieden von der Syntax der Indicator Scripting Language, lautet Regel TT oder TI, Eingabereihennummer, Look-back.
- TT-15-137 ist die traditionelle Trendregel auf Eingabereihe 15, Cumulative Money Flow, mit einem Look-back von 137 Tagen; TI-40-41 ist die inverse Trendregel auf Reihe 40, den Quality Spread, mit 41 Tagen.
- Extremwert-Regeln beruhen darauf, dass eine Reihe Information trägt, wenn sie ein extremes Hoch oder Tief annimmt oder zwischen Extremen wechselt.
- Hohe und tiefe Extreme lassen sich über feste Schwellen definieren, wenn Mittelwert und Schwankungsbreite relativ stabil sind, die Reihe also stationär ist.
- Alle Eingaben der Extremwert-Regeln wurden mit dem Kanalnormierungsoperator stationär gemacht, nachdem ein viertägiger linear gewichteter Durchschnitt geglättet hatte: CN(LMA(Input Series, 4), N-days).
- Vier Schwellenübertritte sind möglich, und jede Extremwert-Regel definiert Long-Einstieg und Short-Ausstieg sowie Short-Einstieg und Long-Ausstieg über je eines davon, was 12 Typen ergibt.
- Weil die 12 Typen alle Möglichkeiten abdecken, wurden keine zusätzlichen inversen Extremwert-Regeln aufgenommen; Typ 7 ist die Umkehrung von Typ 1, Typ 8 die von Typ 2, und so weiter.
- Die komplexere Signalregel nimmt eine Long-Position und wird durch vier optimierbare Parameter festgelegt: Spanne des kurzen gleitenden Durchschnitts, Spanne des langen gleitenden Durchschnitts, rsi_max und rsi_min.
- Ein Diffusionsindikator wendet dieselbe Regel, etwa ein Kreuz des gleitenden Durchschnitts, auf alle Zeitreihen eines festgelegten Universums an, zum Beispiel alle NYSE-Aktien.
- Jede Reihe wird als Aufwärtstrend oder Abwärtstrend eingestuft, je nach ihrer Lage zum eigenen gleitenden Durchschnitt. Der Wert des Diffusionsindikators ist der Prozentsatz der Reihen im Aufwärtstrend und liegt zwischen 0 und 100.

## Risiken und Grenzen

- Ein Datenfehler, der einen Spread von 5 auf 6 Dollar erhöht, also um 20 Prozent, kann ein Signal auslösen, das der wahre Spread nicht ausgelöst hätte.
- Eine vorherige Festlegung, wann und wie die Prognose bewertet wird, nimmt den nachträglichen Spielraum.
- Selbst ein profitabler Track Record solcher Prognosen lässt offen, was er darstellt, weil subjektive Prognosen unbestimmt abgeleitet werden und Studien zeigen, dass Experten Information von Urteil zu Urteil nicht konsistent verbinden.
- Bei demselben Marktdatenmuster zu verschiedenen Zeiten ist es gut möglich, dass derselbe subjektive Analyst nicht dieselbe Prognose gibt, unter anderem wegen Ermüdung und Langeweile.
- Bedeutungsvolle Track Records können auch aus konkreten Echtzeit-Transaktionsempfehlungen entstehen.

## Beispiele

- Hayes leitet aus sechs einander ausschließenden Zuständen eines Diffusionsindikators ein binäres Signal ab, indem er einem Zustand +1 und den anderen fünf −1 zuweist.
- Die sechs Zustände entstehen aus der Zone zwischen Schwellen wie 40 und 60 und aus der Richtung über die jüngsten fünf Wochen.
- Ist Big Mo über 60 und die Richtung aufwärts, nennt Hayes eine Jahresrendite des Value Line Composite Index von 50 Prozent, und dieser Zustand trat zwischen 1966 und 2000 etwa 20 Prozent der Zeit auf.
- Ist Big Mo über 60 und die jüngere Änderung negativ, ist die annualisierte Marktrendite null, und dieser Zustand trat etwa 16 Prozent der Zeit auf.
- Tabelle 2.1 ordnet subjektiven Signalen ein erwartetes Ergebnis zu: einem Head-and-Shoulders-Top einen Abwärtstrend, einer vollendeten fünften Elliott-Welle eine Korrekturwelle, einem starken Aufwärtstrend mit anschließender Flagge die Fortsetzung des Aufwärtstrends und extrem bullischen Stimmungswerten einen Bärenmarkt.
- Die Prognose, der Markt steige um mehr als 10 Prozent vom aktuellen Niveau, bevor er um mehr als 5 Prozent fällt, wird durch jeden Rückgang von mehr als 5 Prozent vor einem Anstieg von 10 Prozent als Fehler eingestuft.
- Die Prognose, der Markt steige um unendlich viel Prozent, falle um 100 Prozent oder tue irgendetwas dazwischen, ist nicht falsifizierbar, und dieser Mangel ist offensichtlich.
- Die Aussage, auf Basis der Indikatoren bullisch zu sein, lässt unklar, wann der Anstieg eintreten könnte und unter welchen Umständen sie falsch wäre.
- Das Beispiel geht long im S&P 500, wenn der Schlusskurs des Dow-Jones-Transportation-Average geteilt durch den Schlusskurs des S&P 500 größer ist als der 50-Tage-Durchschnitt dieses Verhältnisses, sonst short.
- Verwendet werden Verhältnis, gleitender Durchschnitt, der Vergleich Größer-als, die Bedingung Wenn-dann-sonst, die Konstante 50 und zwei Datenreihen.
- Das Data Mining fand, dass dieser Spezifikationssatz besser abschnitt als jede andere geprüfte Alternative.
- Bei der Kreuzung zweier Durchschnitte ist das Signal das Kreuzen des kurzen Durchschnitts über oder unter den längeren; die Parameter sind die beiden Rückblickfenster.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 1–20 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-001-p001-p020|S. 1–20]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 20–39 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-002-p020-p039|S. 20–39]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 77–96 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-005-p077-p096|S. 77–96]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 134–153 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-008-p134-p153|S. 134–153]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 153–172 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-009-p153-p172|S. 153–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 210–229 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-012-p210-p229|S. 210–229]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 248–267 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-014-p248-p267|S. 248–267]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 381–400 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-021-p381-p400|S. 381–400]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 400–419 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-022-p400-p419|S. 400–419]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 457–476 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-025-p457-p476|S. 457–476]]

## Verwandte Themen
