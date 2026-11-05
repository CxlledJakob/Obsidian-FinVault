---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/11 - Indikatoren/11 - Indikatoren|11 - Indikatoren]]"
weitere_hauptthemen: []
unterthema: "Trendindikatoren"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Simple Moving Average


## Kurzdefinition

- Ein Simple Moving Average ist der Durchschnittspreis eines handelbaren Instruments über einen festgelegten Zeitraum.
- In den Simple Moving Average geht gewöhnlich der Schlusskurs der vergangenen x Bars ein.
- Die Lookback-Periode ist die Zahl der Bars, aus denen dieser gleitende Durchschnitt berechnet wird.

## Kernaussagen

- Neuronale Netze konnten Kauf- und Verkaufssignale einfacher Moving-Average-Regeln zu nichtlinearen Modellen verbinden, die auf dem Dow Jones Average von 1897 bis 1988 gute Prognoseleistung zeigten.
- Beobachtet wird, dass ein Aktienindex wie der Dow-Jones-Durchschnitt oder der S&P 500 nach einem Anstieg über seinen 200-Tage-Durchschnitt über die nächsten mehreren Monate in der Regel weiter zulegt; das wird als probabilistische Verallgemeinerung eingeordnet.
- Die Hypothese 200-H lautet, dass Aufwärtsdurchbrüche des 200-Tage-Durchschnitts durch den DJIA im Durchschnitt über die nächsten drei Monate profitable Long-Positionen erzeugen.
- Die Nullhypothese Null-200 lautet, dass Aufwärtsdurchbrüche eines 200-Tage-Durchschnitts über die folgenden drei Monate keine Gewinne erzeugen.
- Jeder gleitende Durchschnitt, jeder Kanal und jeder Indikator beruht auf historischen Preisdaten, kann nur darstellen, was geschehen ist oder wie die aktuelle Position zur Lookback-Periode steht, hat für sich wenig Vorhersagewert und ist immer ein nachlaufender Indikator der Trendposition, nie ein führender für die wahrscheinliche Zukunft.
- Kreuzungen gleitender Durchschnitte sind berüchtigt für falsche Trendumkehrsignale.
- Gleitende Durchschnitte können den Trend auf historischen Daten zeigen, alarmieren aber nicht zuverlässig auf die Anfangsstadien eines neuen Trends oder darauf, ob ein Trend in der Endphase ist; sie erkennen einen etablierten Trend gewöhnlich lange nach dem optimalen Einstieg.
- Eine Kreuzung gleitender Durchschnitte allein taugt wenig, die wahrscheinliche Trendrichtung einer künftigen Periode zu erkennen; Preisumkehren fallen immer wieder nicht mit diesen Signalen zusammen.
- Die langsame Linie der meisten Zwei-Linien-Momentum-Indikatoren ist gewöhnlich ein gleitender Durchschnitt der schnellen Linie, die gewöhnlich die Rohdaten ist.
- Eine Momentum-Kreuzung ähnelt einer Kreuzung gleitender Durchschnitte, betrifft aber die Indikatorwerte und nicht die Preisdaten selbst.
- In der linearen Mean-Reversion haben gleitender Durchschnitt und gleitende Standardabweichung einen Lookback gleich der Halbwertszeit. Bei 20 Tagen Halbwertszeit wäre ein Lookback von 5 Tagen unpassend; ein kleines Vielfaches der Halbwertszeit ist oft nahe optimal.
- Der gleitende Durchschnitt wird trotz der Annahme eines festen Mittels benutzt, weil sich der Mittelwert durch Wirtschaft oder Unternehmensführung langsam ändern kann.
- Bollinger-Mittel und Bollinger-Standardabweichung werden über einen Lookback berechnet, der frei optimiert oder gleich der Halbwertszeit der Mean Reversion gesetzt wird.
- Ein kurzes gleitendes Fenster lässt den Durchschnitt sprunghaft springen, wenn der älteste Bar durch den neuesten ersetzt wird. Dieselbe Sprungstelle trifft die gleitende Standardabweichung und eine im Fenster geschätzte Hedge Ratio.
- Der GLD-USO-Lookback für die dynamische Hedge Ratio und den Z-Score ist 20 Handelstage und mit Wissen im Nachhinein nahe optimal gewählt. Dieselbe Fensterlänge gilt für die Ratio USO/GLD; die ersten 20 Beobachtungen werden entfernt, damit das Testset mit den Spread-Strategien übereinstimmt.
- Die VX-Kalenderspread-Strategie berechnet den gleitenden Durchschnitt des Verhältnisses Back zu Front mit einem Lookback von 15 Tagen, zusammen mit den Standardabweichungen über dasselbe Fenster.

## Funktionsweise

- Ein Fünf-Tage-Durchschnitt addiert die Schlusskurse der letzten fünf Tage und teilt durch fünf.
- Auch bei einem Hurst-Exponenten zwischen 0 und 0,5 steigt die Varianz mit der Zeit, nur langsamer als bei einem geometrischen Random Walk; der gleitende Durchschnitt passt sich an und nimmt Gewinne schneller mit.
- Der gleitende Durchschnitt ist ein Operator für variable Schwellen und wird bei Zeitreihen mit Trends eingesetzt, großen und lang anhaltenden Niveauänderungen, bei denen feste Schwellen unpraktisch sind.
- Die Moving-Average-Cross-Regel signalisiert, wenn die Zeitreihe von einer Seite ihres gleitenden Durchschnitts auf die andere wechselt; oberhalb ist die Ausgabe +1, sonst −1.
- Bei einer einzigen Schwelle, dem gleitenden Durchschnitt, sind die beiden Zustände darüber und darunter gegenseitig ausschließend und erschöpfend, sodass die Signale nicht im Konflikt stehen können.
- Das Verhältnis einer Zeitreihe zu ihrem gleitenden Durchschnitt erzeugt eine stationäre Version der ursprünglichen Reihe.
- Liegt die Zeitreihe über ihrem gleitenden Durchschnitt, setzt die traditionelle Cross-Regel die Ausgabe auf +1, sonst auf −1.
- Die inverse Cross-Regel setzt −1, wenn die Reihe über dem Durchschnitt liegt, und +1, wenn sie darunter liegt.
- Die Bandregel legt ein oberes und ein unteres Band um den Durchschnitt; +1 gilt vom Aufwärtsdurchstoß des oberen Bandes bis zum Abwärtsdurchstoß des unteren Bandes, der −1 setzt.
- Aus Sicht der technischen Analyse lassen sich durch positives Feedback entstandene Trends als Kaskade immer unempfindlicherer Trendfolge-Signale lesen. Eine Anfangsbewegung löst das empfindlichste Signal aus, etwa ein sehr kurzfristiges Crossover gleitender Durchschnitte.
- Die dadurch ausgelösten Transaktionen schieben die Preise weit genug, um ein etwas weniger empfindliches Trendsignal auszulösen, etwa einen mittelfristigen gleitenden Durchschnitt, das wiederum noch unempfindlichere Signale auslöst.
- In der Fallstudie wird der gleitende Durchschnitt zum Glätten verwendet. Der Kanalausbruch identifiziert Trends; der Durchschnitt kann Trends ebenfalls identifizieren, dient hier aber der Glättung.
- Der gleitende Durchschnitt klärt Trends, indem er hochfrequente, kurzperiodische Schwankungen herausfiltert und niederfrequente, langperiodische Anteile durchlässt. Er funktioniert als Tiefpassfilter.
- Die Ausgabe ist im Wesentlichen der Trend der ursprünglichen Zeitreihe, wobei die hochfrequenten Schwingungen um den Trend entfernt sind. In der Abbildung ist der Durchschnitt zentriert, verzögert um das 0,5-Fache der Periode minus 1.
- Die Glättung entsteht durch Mittelung der Werte in einem gleitenden Datenfenster, der Rückschau. Das beseitigt Schwankungen oder senkt ihre Amplitude, wenn ihre Dauer gleich oder kürzer als die Dauer der Rückschau ist.
- Ein 10-Tage-Durchschnitt senkt die Amplitude von Schwankungen, deren Abstand von Hoch zu Hoch oder von Tief zu Tief unter 10 Tagen liegt, und beseitigt eine Schwankung vollständig, deren Dauer genau 10 Tage beträgt.
- Der Nutzen der Glättung hat einen Preis, die Verzögerung. Schwankungen des Rohpreises, die in der geglätteten Fassung erscheinen, erfahren eine Verzögerung. Ein Tief im Rohpreis erzeugt ein Tief im Durchschnitt erst an einem späteren Datum.
- Das Ausmaß der Verzögerung hängt von der Länge der Rückschau ab. Eine längere Rückschau erzeugt mehr Glättung und mehr Verzögerung.
- Der Moving-Average-Operator der Indicator Scripting Language verlangt zwei Argumente, die Datenreihe und die Zahl der Perioden im Look-back: Moving Average Indicator gleich MA(input series, N).
- Figur 8.8 nennt neben dem einfachen Durchschnitt den linear gewichteten Durchschnitt: Indicator gleich MA oder LMA(Time Series, n), jeweils mit zwei Argumenten.
- Verschachteln macht den Ausgang eines Operators zum Argument des nächsten; die 60-Tage-Kanalnormierung eines 10-Tage-Durchschnitts des Dow Jones Transportation Index ist Indicator gleich CN[MA(DJTA, 10), 60].
- Die Extremwert-Regeln glätten jede Eingabe zuerst mit einem viertägigen linear gewichteten Durchschnitt, auch Reihen, die wie der 30-Tage-Durchschnitt des Negative Volume schon geglättet sind.
- Von den Preis-Volumen-Funktionen wurden gleitende Durchschnitte über 10 und 30 Tage gebaut, darunter On-Balance Volume, Accumulation Distribution, Money Flow, Negative Volume und Positive Volume.
- Ein gleitender Durchschnitt einer Preis-Volumen-Funktion ist stationär und ohne Trend und bleibt nahe null, weil nur das Look-back zählt und die Tageswerte beide Vorzeichen haben.
- Gleitende Durchschnitte gehören mit Moving-Average-Bändern, Channel Breakout und Alexander-Filtern, auch Zickzack-Filter genannt, zu den am weitesten verbreiteten objektiven Indikatoren der Trendrichtung.
- Es gibt intelligentere und sparsamere Suchverfahren, als jede mögliche Kombination zu testen, darunter die Suche mit genetischen Algorithmen, Simulated Annealing und gradientenbasierte geführte Suche.
- Die langsame Linie eines Indikators ist gewöhnlich nur ein gleitender Durchschnitt der schnellen Linie und reagiert langsamer auf Momentumänderungen.
- Der MACD misst die Differenz zwischen zwei gleitenden Durchschnitten.
- Ein Balken auf der anderen Seite der MACD-Mittellinie bedeutet, dass der schnellere gleitende Durchschnitt den langsameren nach oben oder unten gekreuzt hat.
- Graham und Dodd bilden das zyklisch bereinigte Kurs-Gewinn-Verhältnis mit einem gleitenden Durchschnitt der Gewinne von mindestens fünf, vorzugsweise sieben oder zehn Jahren, nicht mit einer einzigen Trailing-Gewinnzahl.
- Das Graham-und-Dodd-Verhältnis teilt den aktuellen Kurs durch den zehnjährigen Durchschnitt der ausgewiesenen Gewinne.
- Ein einfacher gleitender Durchschnitt der Vergangenheit wird einer aufwendigen Trendschätzung vorgezogen. Graham hatte keine verlässlichen Aktienwertberechnungen gesehen, die über einfache Arithmetik oder die elementarste Algebra hinausgingen.
- Fehlt eine volle Gewinnhistorie, wird der Durchschnitt auf dem längsten verfügbaren Zeitraum gerechnet.

## Voraussetzungen


## Anwendung im Trading

- Im Buy-on-Gap muss der Eröffnungskurs über dem 20-Tage-Durchschnitt der Schlusskurse liegen; im Code ist der Look-back 20 und der Durchschnitt um einen Tag verschoben.
- Ein Kurs über einem langfristigen gleitenden Durchschnitt zieht Verkaufsdruck größerer Akteure wie Long-only-Fonds an.
- In der SPY-Komponenten-Arbitrage ist der Look-back für den gleitenden Durchschnitt und die Standardabweichung des Portfoliomarktwerts auf 5 fixiert, mit dem Vorteil des Hindsight.
- Im Währungspaar und im AUD.CAD-Beispiel werden gleitender Durchschnitt und Standardabweichung mit einem Look-back von 20 Tagen berechnet.
- Beim CL-Kalender-Spread wird der Look-back des gleitenden Durchschnitts von γ auf die gerundete Halbwertszeit gesetzt, etwa 36 Tage.
- Die lineare Mean-Reversion-Strategie auf dem VX-Kalenderspread verwendet einen Lookback von 15 Tagen für den gleitenden Durchschnitt und die Standardabweichungen.
- Die Beispielregel MA50 verwendet einen 50-Tage-Durchschnitt des S&P 500. Liegt der Schlusskurs darüber, wird eine Long-Position gehalten, sonst eine Short-Position.
- Geprüft wird, ob diese Durchschnittsregel auf trendbereinigten Daten eine erwartete Rendite größer als null hat. Null ist die Rendite, die ohne Vorhersagekraft erwartet wird.
- Eine sinnvolle höhere Benchmark für die Behauptung, eine überlegene Fassung der Double-Moving-Average-Crossover-Regel sei entwickelt worden, wäre die Leistung einer herkömmlichen Fassung dieser Regel.
- Hsu und Kuan nennen als Thema komplexer linearer Regeln unter anderem alle Regeln, die auf einem gleitenden Durchschnitt des On-Balance Volume beruhen, neben allen Regeln auf Channel Breakouts.
- Das Kreuz zweier gleitender Durchschnitte ist eines der fünf getesteten Trendfolge-Systeme, neben Channel-Breakout, zwei Momentum-Fassungen und MACD gegen die Signallinie.
- Der gleitende Durchschnitt gehört zu den Zeitreihenoperatoren, zusammen mit gleitender Kanalnormalisierung, Ausbruchskanälen und gleitenden Steigungen.
- Buy-on-Gap verlangt, dass der Eröffnungskurs über dem 20-Tage-Durchschnitt der Schlusskurse liegt. Im Code ist der Lookback 20 und der Durchschnitt um einen Tag verschoben.
- Dieser Durchschnitt wirkt als Momentum-Filter: Titel über einem langfristigen Mittel ziehen Verkaufsdruck länger orientierter Long-only-Fonds an, und nur wenig gefallene Aktien kehren eher um.
- Die Short-Variante verlangt einen Gap nach oben um eine Standardabweichung bei einem Open, der noch unter dem 20-Tage-Durchschnitt liegt.
- Im SPY-Backtest sind gleitender Durchschnitt und gleitende Standardabweichung des Log-Marktwerts auf einen Lookback von 5 fixiert, mit dem Vorteil des Rückblicks.
- Die beiden Währungsbeispiele nutzen einen Lookback von 20 Tagen für den gleitenden Durchschnitt. Auf AUD.CAD ist das Signal der Schluss minus diesem Durchschnitt.
- Die Hedge Ratio im ungleichen Paar kommt nicht aus diesen 20 Tagen, sondern aus einem Johansen-Fenster von 250 Tagen. Die 20 Tage bleiben für Mittel und Standardabweichung.
- Beim CL-Kalenderspread werden gleitender Durchschnitt und gleitende Standardabweichung der Rollrendite mit einem Lookback gleich der gerundeten Halbwertszeit berechnet, etwa 36 Tage.

## Regeln und Kriterien

- Der Lookback von gleitendem Durchschnitt und gleitender Standardabweichung kann gleich der Halbwertszeit der Mean Reversion gesetzt werden.
- Bei einer Halbwertszeit von 20 Tagen soll kein Lookback von 5 Tagen verwendet werden; ein kleines Vielfaches der Halbwertszeit ist oft nahe am Optimum und erspart die Optimierung des freien Parameters.
- Der Mittelwert kann sich langsam ändern, etwa durch die Wirtschaft oder das Unternehmensmanagement, deshalb wird ein gleitender statt ein fester Durchschnitt verwendet.
- Der Lookback des gleitenden Durchschnitts des Portfoliopreises wird auf die gerundete Halbwertszeit gesetzt.
- Dieser Lookback ist eine Eigenschaft der Preisreihe und kein an der Strategie optimierter Parameter.
- Ist 200-H wahr, dann ist ein Backtest profitabel; diese Profitabilität beweist 200-H nicht, weil das die Bejahung des Nachsatzes wäre.
- Ist der Backtest nicht profitabel, ist der Schluss gültig, dass 200-H falsch ist.
- Ist Null-200 wahr, dann ist der Backtest nicht profitabel; ist er es doch, ist Null-200 falsch und nach dem Satz vom ausgeschlossenen Dritten 200-H wahr, weil es kein Drittes gibt.
- Der MLM-Index wendet eine Crossover-Strategie mit einem 12-Monats-Durchschnitt auf 25 Rohstoffmärkte an. Die Monatsrenditen sind bis in die 1960er Jahre zurückgerechnet.
- Am Ende jedes Monats wird der Preis des Nearby-Futures jedes Marktes mit seinem 12-Monats-Durchschnitt verglichen. Liegt der Preis über dem Durchschnitt, wird im nächsten Monat eine Long-Position gehalten. Liegt er darunter, wird eine Short-Position gehalten.
- Der Index nimmt kein spezialisiertes Wissen über ein komplexes Prognosemodell an. Täte er das, könnte er nicht legitim ein Benchmark-Index heißen, dessen Funktion ist, die Rendite einer Anlageklasse ohne besonderes Können zu schätzen.
- Die Verzögerung eines einfachen gleitenden Durchschnitts, der jedem Element im Fenster gleiches Gewicht gibt, beträgt (n minus 1) durch 2. Die Ausgabe eines 11-Tage-Durchschnitts hat eine Verzögerung von 5 Tagen.
- Trendumkehren in der Eingabereihe, die lang genug sind, um im Durchschnitt zu erscheinen, zeigen sich dann erst 5 Tage später.
- Es gibt viele Arten gleitender Durchschnitte, vom einfachen mit gleichem Gewicht bis zu aufwendigen Glättungen mit komplexen Gewichtsfunktionen. Der Nutzen komplexer Gewichte ist bessere Filterleistung, weniger Verzögerung bei gegebenem Glättungsgrad.
- Nach Ehlers beträgt die Verzögerung eines linear gewichteten Durchschnitts mit Rückschau von n Tagen (n minus 1) durch 3, verglichen mit (n minus 1) durch 2 beim einfachen Durchschnitt.
- Ein linear gewichteter Durchschnitt über 10 Tage hat damit eine Verzögerung von 3 Tagen, ein einfacher Durchschnitt derselben Spanne eine von 4,5 Tagen.
- Die lineare Gewichtung gibt dem jüngsten Datenpunkt das Gewicht n und senkt das Gewicht um eins für jeden älteren Tag. Die Summe der Gewichte wird zum Divisor.
- Die Fallstudie verwendet einen linear gewichteten Vier-Tage-Durchschnitt, um Indikatoren zu glätten, die signalisieren, wenn der Indikator eine kritische Schwelle kreuzt. Die Rechnung ist 4 mal der aktuelle Preis plus 3 mal der Preis einen Tag zuvor plus 2 mal der Preis zwei Tage zuvor plus 1 mal der Preis drei Tage zuvor, geteilt durch 10.
- In der Skriptsprache wird ein Durchschnittsindikator als Operator MA mit der Eingabereihe und der Periodenzahl N angegeben. Ehlers behandelt in zwei Büchern digitale Filter, die für die technische Analyse relevant sind.
- Die Möglichkeit, dass die Zeitreihe gleich dem gleitenden Durchschnitt ist, wird beseitigt, indem der gleitende Durchschnitt mit höherer Genauigkeit berechnet wird als das Preisniveau.
- Ein Diffusionsindikator wendet dieselbe Regel, etwa ein Kreuz des gleitenden Durchschnitts, auf alle Reihen eines Universums an, zum Beispiel alle NYSE-Aktien, und stuft jede Reihe nach ihrer Lage zum eigenen gleitenden Durchschnitt als Aufwärts- oder Abwärtstrend ein.
- Der Wert des Diffusionsindikators ist der Prozentsatz der Zeitreihen im Aufwärtstrend und ist auf die Spanne 0 bis 100 beschränkt.
- Eine Regel aus zwei gleitenden Durchschnitten hat eine Bedingung und zwei Parameter. Die Bedingung lautet: Liegt der kurzfristige gleitende Durchschnitt über dem langfristigen, wird eine Long-Position gehalten, sonst eine Short-Position.
- Die zwei Parameter sind die Look-back-Spannen des kurzfristigen und des langfristigen gleitenden Durchschnitts.
- Ein einfacher gleitender Durchschnitt wird zentriert, indem der Durchschnittswert in die Mitte des Datenfensters eingetragen wird.
- Ist N die Zahl der Perioden des Durchschnitts, wird der Durchschnitt so eingetragen, dass er einem um (n − 1)/2 Datenpunkte verzögerten Wert entspricht.

## Risiken und Grenzen

- Alle Preise zählen gleich, ohne Unterschied zwischen Preisen auf niedrigem oder hohem Volumen.
- Auch die Auktionsrichtung des Tages bleibt unberücksichtigt, wodurch die Information stark in die Irre führen kann.
- Auf jedes Beispiel, wie ein solcher Trendindikator den Trend definiert, zeigt der Autor zwei, in denen er schnell versagte, und auf jedes nachträgliche Beispiel mindestens zwei, in denen die Trendumkehr nicht rechtzeitig erkannt wurde.
- Für sich kann ein gleitender Durchschnitt Teil eines umfassenden Tradingplans sein, identifiziert aber allein nicht die wahrscheinliche künftige Trendrichtung.

## Beispiele

- Ein Beispiel verwendet den gleitenden Durchschnitt des Dow Jones Transportation Average mit Bändern bei +3 Prozent und −3 Prozent und ist im S&P 500 nur short, solange der Transportation Average unter dem unteren Band liegt.
- Ein bekanntes Beispiel eines Diffusionsindikators ist der Anteil der Aktien der New York Stock Exchange, die über ihrem 200-Tage-Durchschnitt liegen; der Prozentsatz ist im Wesen eine ungewichtete lineare Kombination.
- Das Beispiel der Komplexitätssuche beginnt mit einer grundlegenden Umkehrregel aus zwei gleitenden Durchschnitten, definiert durch die Look-back-Spanne des kurzen und die des langen Durchschnitts.
- Erhält jeder der beiden Durchschnitte 10 mögliche Parameterwerte, umfasst eine Brute-Force-Suche 100 Tests.
- Die Parameterkombination mit der höchsten Leistung im Trainingssatz wird danach auf dem Testdatensatz geprüft.
- Im Beispiel verdient diese beste Zwei-Durchschnitt-Regel 30 Prozent annualisierte Rendite im Training und 15 Prozent im Test.
- Solange der Testdatensatz nur dieses eine Mal benutzt wird, sind die 15 Prozent eine unverzerrte Schätzung der künftigen Leistung der Regel und nichts weiter als gewöhnliche Parameteroptimierung.
- Die einfache Regel aus zwei gleitenden Durchschnitten verdiente 30 Prozent in den Trainingsdaten und 15 Prozent im Testset.
- Die Vier-Parameter-Regel mit kurzer und langer Durchschnittsspanne sowie rsi_max und rsi_min verdiente 50 Prozent im Training und 20 Prozent im Test.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Markets in Profile_ Profiting from the Auction Process.pdf, S. 120–139 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-010-p120-p139|S. 120–139]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 1–20 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-001-p001-p020|S. 1–20]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 20–39 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-002-p020-p039|S. 20–39]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 134–153 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-008-p134-p153|S. 134–153]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 210–229 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-012-p210-p229|S. 210–229]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 362–381 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-020-p362-p381|S. 362–381]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 381–400 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-021-p381-p400|S. 381–400]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 400–419 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-022-p400-p419|S. 400–419]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 457–476 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-025-p457-p476|S. 457–476]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 23–42 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-003-p023-p042|S. 23–42]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 42–61 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-004-p042-p061|S. 42–61]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 52–71 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-004-p052-p071|S. 52–71]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 71–75 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-005-p071-p075|S. 71–75]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 76–95 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-006-p076-p095|S. 76–95]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 99–118 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-008-p099-p118|S. 99–118]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 119–138 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-009-p119-p138|S. 119–138]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 138–143 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-010-p138-p143|S. 138–143]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 343–362 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-019-p343-p362|S. 343–362]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 12–25 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-002-p012-p025|S. 12–25]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 26–34 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-003-p026-p034|S. 26–34]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 35–47 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-004-p035-p047|S. 35–47]]

## Verwandte Themen
