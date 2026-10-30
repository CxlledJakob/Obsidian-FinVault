---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Strategien und Ausführung"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Trend-Following-System


## Kurzdefinition


## Kernaussagen

- Zeitreihenmomentum ist die positive Korrelation vergangener und künftiger Renditen einer Preisreihe, und Futures zeigen es hauptsächlich wegen der Persistenz des Vorzeichens der Rollrenditen.
- Querschnittliches Momentum ist die positive Korrelation vergangener und künftiger relativer Renditen gegenüber den anderen Reihen eines Portfolios, und ein einfacher Rang auf den Renditen genügt oft.
- Die zwei üblichen Ausstiege sind zeitbasiert und Stop-Loss; alle bisher besprochenen Momentum-Strategien nutzen nur die Haltedauer, ein Stop kann dazukommen.
- Der Einzelverlust ist dadurch begrenzt, das Aufwärtspotenzial ist unbegrenzt, und eine willkürliche Gewinnobergrenze ist unratsam.
- Die Modelle gedeihen an Black Swans und an hoher Kurtosis, und die meisten Futures und Währungen erlauben damit Streuung über Assetklassen und Länder.
- Zusammen mit Mean-Reversion-Strategien entstehen höhere Sharpe Ratios und kleinere Drawdowns als mit jedem Typ allein.
- Profitable News-Sentiment-Strategien zeigen die langsame Nachrichtendiffusion als Ursache des Aktienmomentums, und die Ansteckung erzwungener Fondsverkäufe und -käufe trägt ebenfalls dazu bei.
- Die Kreuzung zweier gleitender Durchschnitte ist eine Formalisierung der Trendfolge.
- Zur breiteren Kategorie gehören auch Kanalausbrüche und Bänder um gleitende Durchschnitte.
- Trendfolge ist eine Kategorie neben Gegentrend- oder Mean-Reversion-Regeln, Extremwertregeln, Divergenzregeln und Diffusionsregeln.
- Teil Zwei untersucht drei Themen: Trends, Extremwerte und Übergänge sowie Divergenz; jedes Thema wird mit einer in Kapitel 8 definierten Regelform umgesetzt.
- Bei Futures-Handelsfonds mit objektiven Trendfolgemethoden scheint die schwächere Regelleistung an Änderungen der Marktvolatilität zu liegen, die nicht mit der Nutzung technischer Systeme zusammenhängen.
- Die Profitabilität technischer Trendfolgesysteme in Rohstoff-Futures lässt sich als Risikoprämie dafür erklären, dass sie kommerziellen Hedgern Risiko abnehmen.
- Die ökonomische Theorie sagt voraus, dass Futures-Märkte genug profitable Trends zeigen sollten, damit Trendfolger bereit sind, die Preisrisiken zu tragen, die Hedger abgeben wollen.
- Nach der EMH ziehen die Preise nicht allmählich von einem rationalen Niveau zum nächsten, sodass ein Trendanalyst aufspringen könnte; sie springen fast sofort und zeichnen eine Stufenfunktion.
- Die risikoadjustierten Renditen des MLM-Index legen nahe, dass die Rohstoff-Futures-Märkte systematische Preisbewegungen enthalten, die mit relativ einfachen Methoden der technischen Analyse ausnutzbar sind.
- Die Sharpe Ratio des Trendfolgers ist etwas besser als die der anderen Anlageklassen-Benchmarks. Der Index ist Evidenz, dass die Futures-Märkte eine Entschädigung in Form systematischer Preisbewegungen bieten.
- Trendfolge ist am wirksamsten in Zeiten, in denen positives Feedback dominiert, weil sie von großräumigen Preisbewegungen abhängt.
- Die Futures-Märkte brauchen Spekulanten als Trendfolger: im Aufwärtstrend, um den überschießenden Verkauf der Commercial Hedger aufzunehmen, im Abwärtstrend, um deren überschießenden Kauf durch Leerverkäufe zu bedienen. Die unsichtbare Hand erzeugt die Trends als Entschädigung.
- Die Kompensation der Rohstoff- und Währungs-Hedge-Prämie sind profitable Trends, die mit relativ einfachen Trendfolge-Strategien erfasst werden.
- Ist diese Risikotransfer-Prämie gültig, sollte Trendfolge in Aktien weniger lohnend sein, weil dort kein Risikotransfer geleistet wird. Kestner vergleicht dazu fünf Systeme vom 1. Januar 1990 bis zum 31. Dezember 2001, 29 Rohstoffe in 8 Sektoren gegen 31 Large Caps in 9 Branchen plus 3 Indizes.
- Die über fünf Trendfolge-Systeme gemittelte Sharpe Ratio beträgt 0,604 in Futures gegen 0,046 in Aktien.
- Der Vergleich von Lars Kestner umfasst den 1. Januar 1990 bis zum 31. Dezember 2001. Die Futures sind 29 Rohstoffe in 8 Sektoren, die Aktien 31 Large Caps in 9 Branchen plus 3 Aktienindizes.
- Die Ergebnisse stützen die Vorstellung, dass Futures-Trendfolger eine Risikoprämie verdienen, die Trendfolgern in Aktien nicht zur Verfügung steht.
- Der MLM-Index liefert einige Evidenz, dass die Futures-Märkte eine Entschädigung in Form systematischer Preisbewegungen bieten. Ein Trendfolger in Aktien erbringt keine Risikotransfer-Leistung, deshalb sollte Trendfolge in Aktien weniger lohnend sein, wenn die Risikotransfer-Prämie die gültige Erklärung ist.
- Der n-Perioden-Kanalausbruch identifiziert Trends und hat sich trotz extremer Einfachheit als so wirksam erwiesen wie komplexere Trendfolge-Methoden.
- Die Fallstudie testet für diesen Operator 11 Rückschauen: 3, 5, 8, 12, 18, 27, 41, 61, 91, 137 und 205 Tage. Größere Rückschauen identifizieren größere Trends und machen den Kanal breiter und unempfindlicher.
- Echte Trends sind Strähnen, die länger dauern als die Strähnen in Random Walks. In echt trendenden Prozessen enthalten frühere Beobachtungen nützliche Prognoseinformation.

## Funktionsweise

- Die einfache Zeitreihen-Momentum-Regel nach Moskowitz, Yao und Pedersen kauft den Future bei positiver und verkauft ihn bei negativer 12-Monats-Rendite und hält einen Monat; hier wird täglich entschieden und jeden Tag nur ein Fünfundzwanzigstel des Kapitals eingesetzt.
- Für TU sind Lookback und Haltedauer 250 und 25 Tage, gewählt wegen einer Korrelation von 0,27 bei einem p-Wert von 0,02.
- Ein saubereres Signal ist die verzögerte Rollrendite: long, wenn sie über einer Schwelle liegt, short, wenn sie unter der negativen Schwelle liegt, sonst wird jede Position geschlossen.
- Weitere Einstiege sind ein neues N-Tage-Hoch, das Überschreiten des N-Tage-Durchschnitts oder des exponentiellen Durchschnitts, das Überschreiten des oberen Bollinger-Bandes und ein Übergewicht der Aufwärtstage in einem gleitenden Fenster.
- Der Alexander-Filter kauft, wenn die Tagesrendite um mindestens x Prozent steigt, und verkauft und geht short, wenn der Preis von einem folgenden Hoch um mindestens x Prozent fällt.
- Der S&P DTI ist long, wenn ein Future über seinem exponentiellen Durchschnitt liegt, und short, wenn er darunter liegt, mit monatlichem Rebalancing über 24 Futures.

## Voraussetzungen


## Anwendung im Trading

- Kointegriert oder korreliert ein ETF oder ein anderer Future mit Spotpreis oder Spot-Rendite eines Rohstoffs, wird dieses Instrument bei Backwardation geshortet und bei Contango gekauft, um die Rollrendite des Rohstoff-Futures zu extrahieren.
- Die fünf getesteten Trendfolge-Systeme waren Channel-Breakout, das Kreuz zweier gleitender Durchschnitte, zwei Fassungen von Momentum und MACD gegen seine Signallinie.
- Die acht getesteten Marktsektoren waren Devisen, Zinsen, Aktienindex, Metalle, Energie, Getreide, Fleisch und Softs.
- Als Branchensektoren nennt der Text Energie, Grundstoffe, zyklischen Konsum, Basiskonsum, Gesundheit, Finanzwerte und Informationstechnologie sowie Telekom, und als drei Aktienindizes den S&P 500, den NASDAQ 100 und den Russell 2000.

## Regeln und Kriterien

- Der Mt.-Lucas-Management-Index ist die historische Aufzeichnung der Renditen einer extrem einfachen Trendfolge-Formel auf 25 Rohstoffmärkten, monatlich zurückgerechnet bis in die 1960er Jahre, ohne komplexes Prognosemodell.
- Am Monatsende wird der Nearby-Future jedes Marktes mit seinem 12-Monats-Durchschnitt verglichen. Liegt der Preis darüber, wird für den nächsten Monat long gehalten, liegt er darunter, short.
- Die meisten Trendfolge-Systeme erzeugen in 50 bis 65 Prozent der Fälle unprofitable Signale. Das geschieht, wenn die Märkte trendlos sind, und das ist die Mehrheit der Zeit.
- In Drawdowns verlieren erfolgreiche Trendfolger nicht ungewöhnlich bis zu 30 Prozent ihres Handelskapitals. Großräumige Trends bieten eine Gewinngelegenheit, keine Garantie, und sie verlangt ausreichende Kapitalisierung und richtiges Hebelmanagement.

## Risiken und Grenzen

- Wenige Trades wegen langer Haltedauern erzeugen ein Data-Snooping-Risiko; der eigentliche Test ist echtes Out-of-Sample-Testing.
- Für C trägt die Rollrendite-Erklärung nicht, obwohl ihre Rollrendite betragsmäßig am stärksten gegen die durchschnittliche Spot-Rendite ist.
- Die Wirkungsdauer wird kürzer, je mehr Händler das Momentum aufgreifen, ohne vorhersagbaren Zeitplan für die kürzere Haltedauer; Gewinnmeldungs-Momentum hält kaum noch bis zum Schluss.
- Stop-Losses widersprechen Mean-Reversion-Einstiegen.
- Eine einzelne Mean-Reversion-Position kann einen enormen Drawdown erzeugen, und aufeinanderfolgende Momentum-Verluste können trotzdem ruinös werden.
- In Beispiel 1.1 erreicht eine Reihe mit der Kurtosis der TU-Futures, aber ohne serielle Autokorrelation, in 12 Prozent der Ziehungen dieselben Renditen wie die TU-Momentum-Strategie.

## Beispiele

- TU erzielt vom 1. Juni 2004 bis zum 11. Mai 2012 eine Sharpe Ratio von 1 und 1,7 Prozent annualisiert auf etwa 200.000 Dollar Nominalwert bei etwa 400 Dollar Margin und 2,5 Prozent maximalem Drawdown.
- Tabelle 6.2: BR Lookback 100 und Haltedauer 10 mit 17,7 Prozent, Sharpe Ratio 1,09 und maximalem Drawdown minus 14,8 Prozent; HG 40 und 40 mit 18,0 Prozent, 1,05 und minus 24,0 Prozent; TU 250 und 25 mit 1,7 Prozent, 1,04 und minus 2,5 Prozent.
- Auf TU ergibt die Schwelle von 3 Prozent annualisierter Rollrendite vom 2. Januar 2009 bis zum 13. August 2012 2,5 Prozent annualisiert, eine Sharpe Ratio von 2,1 und einen maximalen Drawdown von 1,1 Prozent.
- Auf CL wird zum Schluss gekauft, wenn der Preis unter dem Stand von vor 30 Tagen und über dem von vor 40 Tagen liegt, umgekehrt für Shorts, sonst wird glattgestellt, mit 12 Prozent annualisiert und einer Sharpe Ratio von 1,1.
- Ein Mean-Reversion-Filter ergänzt IBX, KT, SXF, US, CD, NG und W und verbessert die schon enthaltenen Kontrakte.
- Der DTI hat nach Dever von Januar 1988 bis Dezember 2010 eine Sharpe Ratio von 1,3 und einen maximalen Drawdown von minus 16,6 Prozent, gegen 0,61 und minus 50,96 Prozent beim S&P 500, läuft seit 2008 schlecht und steht seit dem 5. Dezember 2008 mit minus 25,9 Prozent im Drawdown.
- RYMFX und WDTI bilden den DTI ab.
- Nach Kaufman zeigte eine Studie von Dunn & Hargitt 1970, dass ein Channel-Breakout über vier Wochen, Donchians Vier-Wochen-Regel, das beste von mehreren populären Systemen war, getestet auf 16 Jahren Daten von sieben Rohstoffmärkten.
- Im Vergleich von Kaufman an Eurodollars für 1985 bis 1994 hatte Channel-Breakout die höchste risikobereinigte Performance gegenüber exponentieller Glättung, der Steigung der linearen Regression, Swing-Breakout und Point-and-Figure.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 210–229 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-012-p210-p229|S. 210–229]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 248–267 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-014-p248-p267|S. 248–267]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 324–343 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-018-p324-p343|S. 324–343]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 362–381 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-020-p362-p381|S. 362–381]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 381–400 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-021-p381-p400|S. 381–400]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]

## Verwandte Themen

- Für alternative Methoden der Trendanalyse und die daraus abgeleiteten Regeln verweist der Text auf die Kapitel 5 bis 8 bei Kaufman.
