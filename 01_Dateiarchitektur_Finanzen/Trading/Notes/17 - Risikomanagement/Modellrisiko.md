---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/17 - Risikomanagement/17 - Risikomanagement|17 - Risikomanagement]]"
weitere_hauptthemen: []
unterthema: "Risikomessung"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Modellrisiko


## Kurzdefinition


## Kernaussagen

- Die Annahme, die künftige Verteilung der Marktrenditen gleiche der vergangenen, ist meist falsch; quantitative Modelle können es nicht besser.
- Viele Risikotechniken unterstellen zusätzlich, dass die Verteilung der Strategierenditen dieselbe bleibt, am restriktivsten als Gauß-Verteilung.
- Selbst bei gültiger Gauß-Annahme bleiben Schätzfehler für Mittelwert und Varianz, und künftige Momente müssen nicht den historischen entsprechen.
- Ein dadurch überschätzter Hebel kann zum Ruin führen, und nichtgaußische Renditen können den Kelly-Hebel schon im Backtest auf einen maximalen Drawdown von minus 1 bringen.
- In der Finanzwelt ist, was für eine Preisreihe galt, künftig nicht zwingend wahr; eine Mean-Reversion-Reihe kann dauerhaft zum Trend werden.
- Gute Strategien können durch Regimewechsel scheitern, selbst wenn die Fallstricke aus Kapitel 1 entfernt sind.
- Live-Abweichungen vom Backtest entstehen oft durch einen Regime Shift der Marktstruktur infolge von Regulierung oder Makroökonomie, nicht durch Backtest-Fallstricke.
- Auch bei einer algorithmischen Strategie bleiben Entscheidungen nötig, ob die Modelle noch gültig sind.
- Wissenschaft kommt eigentlich nur mit stationären Statistiken zurecht, während die Verteilung der Preise nicht über die Zeit unverändert bleibt.
- Der traditionelle Ansatz nimmt an, die Stichprobenverteilung sei normal und damit glockenförmig. Trifft das nicht zu, werden die Schlüsse ungenau. Deshalb schätzt der Autor die Stichprobenverteilung des Mittelwerts mit einer Computersimulation.
- Je zahlreicher die Annahmen, Bedingungen und Nebenbedingungen einer Erklärung sind, desto eher passt sie eine Menge von Beobachtungen zufällig. Einfachere Erklärungen treffen die wahren Muster eher.
- Bei einer Kleinste-Quadrate-Regression ist ein perfekter Fit garantiert, wenn die Funktion so viele Freiheitsgrade wie Datenpunkte hat. Eine Kurve mit dieser Flexibilität beschreibt dann höchstwahrscheinlich neben der eigentlichen Beziehung die Zufallsschwankungen der Daten.
- Unter sonst gleichen Bedingungen ist die einfachere Erklärung eher richtig. Gibt es genug Daten und stammen sie aus einem komplexen Prozess, kann ein aufwendiges Modell sehr wohl gerechtfertigt sein.
- Dass manchmal geurteilt werden muss, macht quantitative Regeln nicht nutzlos und algorithmische Händler nicht weniger leistungsfähig als diskretionäre: Kahneman schreibt, Experten seien Algorithmen in jedem Bereich mit erheblicher Unsicherheit einheitlich unterlegen, von Fußballsiegern bis zur Lebenserwartung von Krebspatienten, und der Finanzmarkt sei hoffentlich keine Ausnahme.
- Hat das Modell frühere Stressphasen im Backtest überstanden, wird der Hebel vor einer kommenden Krise nicht gesenkt; konservativer wird schon in guten Zeiten gehebelt, weil die unbekannten Unbekannten schaden und das Modell davor nicht abgeschaltet werden kann.
- Underperformance gegenüber dem Backtest soll auf einen fundamentalen Grund zurückgeführt und quantitativ geprüft werden, wie beim Paar GLD gegen GDX, das 2008 die Kointegration verlor und nach Aufnahme des Rohölpreises wieder funktionierte.
- Kelly auf jede Strategie einzeln ist nach der Erfahrung praktischer als die mathematisch optimale Gesamtallokation, sobald ein schwerer Drawdown die Annahme unveränderter erwarteter Renditen und Volatilitäten infrage stellt.
- Der VaR ist eine Punktschätzung des möglichen Verlusts, enthält Unsicherheit und neigt dazu, den tatsächlichen Verlust zu unterschätzen, wenn ein Extremereignis eintritt.
- Die meisten VaR-Verfahren ignorieren die Parameterunsicherheit, weil die prädiktive Verteilung schwer zu erhalten ist, obwohl sie die Parameterunsicherheit eines korrekt spezifizierten Modells berücksichtigen würde.
- Zwei Anlagen können denselben VaR haben und dennoch unterschiedliche Verluste erleiden, sobald der VaR überschritten wird.
- Die Wurzel-der-Zeit-Regel von RiskMetrics wird ungültig, wenn die Annahme eines Mittelwerts null oder das spezielle IGARCH(1,1) ohne Drift nicht gilt.
- Schwere Ränder der Renditen führen dazu, dass die Normalannahme den VaR oft unterschätzt.
- Die VaR-Verfahren liefern für dieselbe IBM-Position deutlich verschiedene Beträge, weil die Schätzung des Schwanzes einer Verteilung erhebliche Unsicherheit enthält. Einen wahren VaR zum Genauigkeitsvergleich gibt es nicht; der Text empfiehlt, mehrere Verfahren zu rechnen, um die Spanne zu sehen.
- Der klassische Extremwert-VaR hängt von der Blocklänge n ab. Ein großes n stützt die Grenzverteilung, lässt bei festem Stichprobenumfang aber weniger Blöcke für die Schätzung von Skala, Lage und Form. Die Stabilität des resultierenden VaR soll geprüft werden.
- Für die täglichen IBM-Logrenditen unterschätzt die klassische Extremwerttheorie den VaR gegenüber dem empirischen Quantil bei 5 und 1 Prozent. Bei 9190 Beobachtungen können diese empirischen Quantile als vorsichtige Untergrenzen gelten; bei 0,1 Prozent ist das empirische Quantil dafür nicht mehr verlässlich.
- Die Schwelle im Peaks-over-Thresholds-Ansatz ist auch eine finanzielle Entscheidung: Institute mit verschiedener Risikotoleranz können für dieselbe Position verschiedene Schwellen wählen.
- Das homogene zweidimensionale Poisson-Modell für die IBM-Überschreitungen bei 2,5 Prozent besteht die Modellprüfung nicht und braucht eine Verfeinerung.
- Der eine gemeinsame Faktor der IBM- und S&P-500-Monatsrenditen erklärt nur etwa 82,5 Prozent der verallgemeinerten Varianz. Das Volatilitätsmodell (10.39) erfasst die bedingte Heteroskedastizität vor allem bei höheren Lags nicht ausreichend.
- Die zweistufige Schätzung, die die Volatilität des Faktors zuerst schätzt und danach als gegeben behandelt, ist einfach, aber nicht notwendig effizient.
- Multivariate gaußsche Innovationen können die Kurtosis der Asset-Renditen verfehlen.
- Allein aus den beobachteten yt ist die Wahl zwischen einem ARIMA-Modell und einem linearen Zustandsraummodell nicht entscheidend.
- Für dieselbe Cisco-Intel-Position liegen die drei 5-Prozent-VaR etwa 1.100 Dollar auseinander: das univariate Modell am niedrigsten, das Modell mit konstanter Korrelation am höchsten.
- Die Branche nimmt Theorie als Fakt, im Widerspruch zu einem wissenschaftlichen Vorgehen, das Modelle an der Empirie prüft; das CAPM ist das Beispiel.
- Die meisten CAPM-Annahmen sind offenkundig abwegig. Die Schlüsselannahmen sind Handel in jeder Größe ohne Preiseinfluss und die universelle Nutzung der Markowitz-Optimierung.
- Die Annahmen im Einzelnen: keine Transaktionskosten, beliebige Position ohne Preiseinfluss, keine Steuern und damit Indifferenz zwischen Dividende und Kursgewinn, Risikoaversion, gemeinsamer Zeithorizont, Aktien nur im Mittelwert-Varianz-Raum, Risikosteuerung durch Diversifikation, alle Assets inklusive Humankapital frei handelbar, Leihen und Verleihen zum risikofreien Satz.
- Einige rationale Marktteilnehmer können den Markt nicht zur CAPM-Lösung schieben; strikt wahr sein muss, dass alle die Markowitz-Optimierung benutzen.
- Selbst Markowitz allokiert nicht nach dem Optimierer, sondern 50 zu 50 in Anleihen und Aktien, um künftiges Bedauern zu minimieren.
- Die Verteidigung, das CAPM lasse sich nicht wirklich testen, oder der Verweis auf eine ICAPM mit unbestimmten Faktoren, ist für Praktiker hohl.
- Analysten rechnen Beta routinemäßig in die Kapitalkosten, obwohl die Evidenz Beta als sehr schlechtes Risikomaß ausweist; Fama und French (2004) sagen, die empirische Bilanz sei schlecht genug, die Anwendung zu entwerten.
- Modigliani und Miller nahmen Mitte der 1950er effiziente Märkte an, bevor die Effizienzmarkthypothese formuliert war, und schlossen auf die Irrelevanz von Dividende und Kapitalstruktur.
- Zu viele Risikomodelle schreiben die jüngeren Marktbedingungen fort. In Turbulenz sind historische Volatilität und Korrelation voraussichtlich schlechte Führer.
- Der zentrale Fehler der meisten Risikomodelle ist die Annahme, Risiko sei exogen wie beim Roulette. In überfüllten Trades ist Risiko endogen wie beim Poker, die Handlungen der anderen sind entscheidend.
- Strategisches Denken, also zu antizipieren, was die anderen tun, ist außergewöhnlich schwierig. Das zeigt Keynes' Schönheitswettbewerb, Global Equity Strategy vom 17. Februar 2004.
- Einfache Rechnungen legen eine Unterschätzung des wahren Risikos durch VaR um 20 bis 30 Prozent allein wegen unpassender Korrelationen nahe. Mit der asymmetrischen Korrelation 1970 bis 2004 wird daraus ein Faktor 1,35 oder 35 Prozent, ab 1995 etwa 21 Prozent, bevor eine Verdopplung oder Verdreifachung der Volatilität hinzukommt.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- Bei einem großen bevorstehenden Ereignis ist zu entscheiden, ob dem Backtest getraut, der Hebel gesenkt oder das Modell vorübergehend abgeschaltet wird.
- Kelly über das Gesamtportfolio ist nur optimal, wenn erwartete Renditen und Volatilitäten unverändert bleiben; nach schwerem Drawdown ist das zweifelhaft.
- Der Autor senkt den Hebel vor einer kommenden Krise nicht, wenn das Modell frühere Stressperioden im Backtest überstanden hat; besser ist von vornherein ein konservativerer Hebel.
- Unknown Unknowns schaden, nicht die Known Unknowns, und die Modelle lassen sich nicht abschalten, bevor Erstere eintreten.
- Praktischer findet er Kelly je Strategie, damit eine underperformende Strategie schnell ausläuft, auch wenn die Mathematik die Allokation über das Gesamtportfolio als optimal ausweist.
- Die Optimalität der gemeinsamen Kelly-Allokation setzt unveränderte erwartete Renditen und Volatilitäten voraus; ein schwerer Drawdown stellt das infrage.

## Regeln und Kriterien


## Risiken und Grenzen

- Das Pearson-System erfasst nicht alle höheren Momente; die empirische Verteilung kann weitere oder, wie bei Pareto-Levy, unendliche höhere Momente haben.
- Alle höheren Momente zu schätzen lädt wegen knapper Daten zu Data-Snooping ein.
- Der an einer historischen Realisierung optimierte Hebel ist für eine künftige Realisierung im Allgemeinen nicht optimal.
- Simulierte Renditen verfehlen serielle Korrelationen, die fortbestehen und den Drawdown verändern können.
- Der simulierte Maximal-Drawdown kann so selten sein, dass er in einer Million Jahren kaum einmal eintritt.
- Subjektives Urteil bleibt nötig, weil die statistischen Eigenschaften finanzieller Zeitreihen nicht stationär sind; stationär heißt hier, dass die Verteilung der Preise über die Zeit unverändert bleibt, abweichend vom Zeitreihenbegriff in Kapitel 2.
- Wissenschaft kann eigentlich nur mit stationären Statistiken umgehen.
- Unknown Unknowns lassen sich nicht dadurch vermeiden, dass die Modelle vorher abgeschaltet werden.
- Urteil bleibt nötig, macht quantitative Regeln aber nicht nutzlos; Kahneman zufolge sind Experten Algorithmen überall dort unterlegen, wo erhebliche Unsicherheit besteht, und der Finanzmarkt ist hoffentlich keine Ausnahme.
- Die Wissenschaft hat ein berechtigtes Interesse, den Bestand des Wissens vor Verfälschungen und abwegigen Überzeugungen zu schützen. Die Beweislast für neues Wissen liegt bei dem, der es behauptet, analog zur Unschuldsvermutung, bei der der Staat die Schuld über jeden vernünftigen Zweifel hinaus beweisen muss.
- Wird der Extremalindex einer stationären Renditereihe übersehen, besteht die Gefahr, den VaR zu unterschätzen.
- Das homogene Poisson-Modell aus Beispiel 7.8 scheint den VaR der IBM-Long-Position zu unterschätzen, verglichen mit dem inhomogenen Modell, dessen Parameter sich mit den Marktbedingungen ändern.
- Der Blockschätzer des Extremalindex kann empfindlich auf die Wahl der Schwelle und der Blockgröße k reagieren.
- Die Kleinste-Quadrate-Schätzung makroökonomischer Faktormodelle erzwingt nicht, dass die spezifischen Faktoren unkorreliert sind, und ist deshalb im Allgemeinen nicht effizient. Ob die Nebendiagonalen der residualen Kovarianz nahe null liegen, prüft die Angemessenheit.
- Im Marktmodell der 13 Aktien bleiben residuale Kreuzkorrelationen von 0,45 zwischen Caterpillar und Alcoa und von 0,48 zwischen General Motors und Ford. Die Annahme unkorrelierter spezifischer Faktoren trifft nicht zu.
- Das Zwei-Faktor-Modell mit Überraschungen von CPI-Wachstum und Beschäftigung ab 16 Jahren hat durchgängig niedrige R² und eine Korrelationsmatrix nahe der Einheitsmatrix. Die beiden makroökonomischen Variablen erklären die Überschussrenditen der 13 Aktien nur schwach, und die Residuenkorrelation bleibt nahe an der Korrelation der ursprünglichen Überschussrenditen.
- Im BARRA-Branchenmodell überzeichnet die modellbasierte Korrelation den Stichprobenzusammenhang innerhalb der Branche: Caterpillar gegen Procter & Gamble hat in der Stichprobe 0,1 und im Modell 0,6.
- Die Zahl der Faktoren ist in fundamentalen Modellen missverständlich, weil sich mehrere Fundamentals zu einem neuen Merkmal verbinden lassen und das lineare Modell dann als Einfaktormodell erscheinen kann. In statistischen Faktormodellen ist die Faktorzahl klarer bestimmt.
- Die Gewichte des globalen Minimum-Varianz-Portfolios aus der faktormodellimplizierten Kovarianz und aus der Stichprobenkovarianz weichen beim Chicago Tribune deutlich ab, 0,1400 gegen 0,0168.
- Interne VaR-Modelle nach dem Basle-Abkommen nutzen 10 Handelstage oder zwei Kalenderwochen, 99 Prozent Konfidenz und mindestens ein Jahr Historie mit Aktualisierung mindestens einmal je Quartal. Das Fortschreiben dieser Historie erzeugt positives Feedback.
- Beta als Maß relativer Preisvolatilität ist empirisch zweifelhaft und funktioniert nach Montier nicht. Sorgen Anleger sich um negative Renditen, ist auch die Standardabweichung als Risikomaß falsch; zu verwenden ist Abwärtsrisiko.
- Die Lehren wirksamen Risikomanagements scheinen nicht gelernt. Dynamisches Hedging und VaR verstärken Markttrends, statt sie zu bremsen.
- Ohne CAPM misst die beta-adjustierte Rendite nichts und kann das Performancebild erheblich verzerren.

## Beispiele

- In Beispiel 6.8 steigt der europäische Call bei hinzugefügten Sprüngen und sonst festen Parametern von 3,49 auf 3,92 Dollar, und der zugehörige Put liegt bei 3,31 Dollar, ebenfalls höher als ohne Sprünge; in der Anwendung führt der Sprungprozess oft zu einer anderen Schätzung der Volatilität σ.
- Für die negativen täglichen IBM-Logrenditen steigt das 1-Prozent-VaR bei n gleich 63 und θ-Dach gleich 0,823 auf 3,2714, gegenüber 3,0497 in Beispiel 7.6 ohne Extremalindex.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 210–229 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-012-p210-p229|S. 210–229]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 199–214 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-015-p199-p214|S. 199–214]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 343–362 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-019-p343-p362|S. 343–362]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 381–400 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-021-p381-p400|S. 381–400]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 400–419 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-022-p400-p419|S. 400–419]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 495–514 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-027-p495-p514|S. 495–514]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 571–590 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-031-p571-p590|S. 571–590]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 438–457 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-024-p438-p457|S. 438–457]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 457–476 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-025-p457-p476|S. 457–476]]

## Verwandte Themen
