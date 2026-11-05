---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/20 - Trading-Performance & Auswertung/20 - Trading-Performance & Auswertung|20 - Trading-Performance & Auswertung]]"
weitere_hauptthemen: []
unterthema: "Renditekennzahlen"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Trefferquote


## Kurzdefinition

- Die Trefferquote ist der Anteil der Wetten mit positivem PnL.
- Die Trefferwahrscheinlichkeit p ist die Wahrscheinlichkeit, mit der die Gewinnauszahlung einer Wette eintritt.

## Kernaussagen

- Die Trefferquote gehört zu den Performance-Kennzahlen ohne Risikoanpassung.
- Bei der Beurteilung von Runs ist eine hohe Trefferquote erwünscht, verbunden mit relativ wenigen Verlustwetten.
- Im Bild eines binären Klassifikators entspricht p der Precision: richtige Positive werden belohnt, falsche Positive werden bestraft, und Negative haben keine Auszahlung.
- Die Sharpe Ratio hängt in diesem Modell von der Precision ab.
- Viele Negative verkleinern die Zahl der Wetten und ziehen die Sharpe Ratio gegen null.
- Die beobachtete Trefferquote ist der Anteil der positiven Ergebnisse an allen Wetten.
- Die kritische Trefferwahrscheinlichkeit ist der Wert, unter dem die Strategie eine vorgegebene Ziel-Sharpe-Ratio verfehlt.
- Die Ausfallwahrscheinlichkeit der Strategie ist die Wahrscheinlichkeit, dass die Trefferquote unter diesem kritischen Wert liegt.
- Im Beispiel traf das Kaufsignal der Regel X in 700 von 1.000 Fällen zu, indem der Markt über die nächsten 10 Tage höher lag, und der induktive Schluss setzt diese Wahrscheinlichkeit für künftige Signale auf 0,7.
- Dieselbe Erfolgsquote von 70 Prozent auf nur 10 statt 1.000 Fällen machte den Schluss mindestens zehnmal unsicherer, sodass die künftige Treffgenauigkeit stark von der historischen Erfolgsquote abweichen kann.
- Je zahlreicher die angeführten Fälle und je höher ihre Qualität, desto wahrscheinlicher verallgemeinert sich die Trefferaussage zutreffend auf künftige Beobachtungen.
- Nichtuniverselle Verallgemeinerungen, auch probabilistische Verallgemeinerungen genannt, haben die Form, dass P Prozent der X die Eigenschaft Y haben oder dass X die Eigenschaft Y mit der Wahrscheinlichkeit P hat.
- Die Genauigkeit einer künstlichen Handelsregel ist der Anteil richtiger Signale und lässt sich experimentell setzen.
- Die erwartete Rendite wird gesteuert, indem die Wahrscheinlichkeit eines profitablen Monats verändert wird.
- Diese Wahrscheinlichkeit zeigt sich über eine sehr große Zahl von Monaten nach dem Gesetz der großen Zahlen; in jeder kleinen Monatsstichprobe schwankt der tatsächliche Anteil profitabler Monate zufällig um die vorgegebene Wahrscheinlichkeit.
- Eine gesetzte Wahrscheinlichkeit von 0,70 entspricht einem Roulette mit 100 Fächern, davon 70 Gewinn und 30 Verlust.
- Bei Gewinnwahrscheinlichkeit 0,50 und 24 Monaten liegt die mittlere Rendite ohne Data Mining im Schnitt bei null; wird die beste aus zwei oder mehr Regeln gewählt, zeigt sie wahrscheinlich eine Rendite über null, obwohl der Erwartungswert null ist.
- Für die Tests mit unterschiedlicher Güte wurde die Wahrscheinlichkeit eines profitablen Monats jeder Regel zufällig aus einer Verteilung gezogen, die der Vermögensverteilung ähnelt und einen langen rechten Rand hat.
- Regeln mit hoher erwarteter Rendite gelten als selten: eine erwartete Jahresrendite von 19 Prozent oder mehr trat etwa einmal unter 10.000 auf.
- Werden nur zwei Monate benutzt, ist die Wahl der Regel mit der besten beobachteten Performance nicht besser, als eine Regel zufällig aus dem Universum zu ziehen, und es ist gleichgültig, wie viele Regeln getestet werden.
- Die besten professionellen Trader haben selten eine Gewinnquote über 50 Prozent. Langfristig erfolgreiche Trader haben gewöhnlich mehr Verlierer als Gewinner.
- Die meisten Amateure akzeptieren diese Realität nicht und begrenzen deshalb den möglichen Verlust eines Trades nicht rücksichtslos.
- Eine Gewinnquote über 50 Prozent über die Zeit gehört zur Elite der Trader.
- Wer gut im Handel wird, hat etwa 30 bis 40 Prozent Gewinntrades.
- Deshalb müssen die Verluste relativ klein und die Gewinne relativ groß sein. Einen anderen Weg nennt der Text nicht.
- Wer gut im Trading wird, hat etwa 30 bis 40 Prozent Gewinntrades.
- Ein Richtungsmaß zählt Treffer und Fehler der Prognose von Auf- und Abwärtsbewegungen in einer 2×2-Tabelle; größere Werte auf der Diagonale, m11 für getroffene Anstiege und m22 für getroffene Rückgänge, bedeuten bessere Prognosen.
- Für das 8–4–1-Netz mit Heaviside-Ausgabe gilt eine Prognose als Anstieg, wenn die prognostizierte Wahrscheinlichkeit mindestens 0,5 ist; die Erfolgsquote dieser Regel beträgt 0,58.
- Diese Erfolgsquote schwankt von Schätzung zu Schätzung erheblich, und das Netz verwendet 49 Parameter.
- In der Tabelle für 24 Monate von Januar 1998 bis Dezember 1999 stehen 12 Treffer und 2 Fehler in der Zeile prognostizierter Anstieg sowie 8 Fehler und 2 Treffer in der Zeile prognostizierter Rückgang.
- Die χ²-Statistik dieser Tabelle ist 0,137 mit p = 0,71; das Netz schlägt eine Zufallswahl damit nicht signifikant.
- Über 500 Schätzläufe desselben Netzes sind Mittel und Median der Zahl der Richtungsfehler 11,28 und 11, bei einem Maximum von 18 und einem Minimum von 4.
- Torngren und Montgomery (2004): Laien und professionelle Investoren sollten monatlich aus einem Paar bekannter Blue Chips die outperformende Aktie wählen, mit Name, Branche und Zwölfmonatsperformance. Beide Gruppen lagen schlechter als ein Münzwurf.
- Die Studierenden waren rund 59 Prozent zuversichtlich, die Profis im Schnitt 65 Prozent. Bei angegebener Sicherheit von 100 Prozent lagen die Profis in weniger als 15 Prozent der Fälle richtig und deutlich hinter den Laien.
- Tyszka und Zielonka: Nur etwa ein Drittel der Finanzanalysten traf den richtigen von drei etwa gleich wahrscheinlichen Ausgängen für den Indexstand in rund eineinhalb Monaten. Bei den Wettervorhersagern für die April-Temperatur waren es etwa zwei Drittel.
- Bei Tetlock lagen Experten, die 80 Prozent oder mehr Konfidenz angaben, nur in etwa 45 Prozent der Fälle richtig. Über alle Prognosen waren sie kaum besser als ein Münzwurf.
- Ärzte, die zu 90 Prozent sicher waren, lagen bei Plous (1991) in weniger als 15 Prozent der Fälle richtig.
- Leli und Filskov (1981): Das Modell erkannte 83 Prozent neuer Fälle fortschreitender Hirnfunktionsstörung; unerfahrene Fachleute lagen bei 63 Prozent, erfahrene bei 58 Prozent.
- Mit der Ausgabe des Modells stiegen die Trefferquoten der Unerfahrenen auf 68 Prozent und der Erfahrenen auf 75 Prozent, beide weiter signifikant unter dem Modell, und die Verbesserung hing vom Ausmaß der Modellnutzung ab.
- Grove et al. (2000): Über 136 Studien lag die durchschnittliche Trefferquote der Fachleute bei 66,5 Prozent und die der Quant-Modelle bei 73,2 Prozent.
- Von den 136 Studien sprachen 64 klar für das Modell, 64 lagen ungefähr gleich, und acht sprachen für den Menschen; in diesen acht hatten die Menschen mehr Information.
- Von den in Pennsylvania auf Bewährung Entlassenen wurden 25 Prozent innerhalb eines Jahres wieder eingesperrt, flüchtig oder erneut verhaftet, und der Ausschuss hatte keinen dieser Fälle vorhergesagt.
- An der University of Texas erhielten 82 Prozent jeder der beiden nach Interviewrang getrennten Gruppen den MD; Honors und die übrigen Stufen zeigten ebenfalls keinen Unterschied, sodass das Interview keine nützliche Funktion hatte.
- Im einfachen Value-Screen auf trailing PE schlagen 50 Prozent der Aktien über ein Jahr den Markt; bei fünf Jahren steigt diese Trefferquote auf 57 Prozent, aber nicht massiv.
- Piotroski (2000) findet, dass nur 42 Prozent der Value-Aktien auf Jahressicht den Markt schlagen.
- Aus den 23 Prozent Big-Value-Aktien, die sich neu bewerten, folgt, dass nur rund ein Viertel der Type-II-Value-Aktien positive Überschussrenditen erzeugt.
- Im Growth-Portfolio haben nur rund 38 Prozent eine über dem Markt liegende Rendite; erfolgreiches Growth-Investing ist das Treffen der Gewinner.
- Die Growth-Trefferquote fällt mit längerem Horizont, weil das Risiko eines Earnings-Torpedos steigt.
- Momentum hebt den Anteil outperformanceender Growth-Aktien auf Einjahressicht von 38 auf 41 Prozent.
- Im Value-Universum steigt die Zwölfmonats-Trefferquote durch Momentum von 50 Prozent auf etwas über 55 Prozent.
- Value-Investing lässt sich als Vermeiden von Verlierern beschreiben; ein Stop-Loss wird als mögliche Lösung genannt und nicht weiter untersucht.
- Der Anteil richtiger Calls ist die Größe f im Informationskoeffizienten, definiert als 2 mal (f minus 0,5).
- Der Informationskoeffizient ist 2 mal (f minus 0,5), wobei f der Anteil der richtigen Calls des Managers ist. Ein Informationskoeffizient von 0,035 entspricht etwa 51 Prozent richtigen Entscheidungen.
- In den dismal years lagen die Informationskoeffizienten bei 0,07 für Value und Momentum, bei −0,02 für nur Value und bei 0,21 für nur Momentum.
- Das Modell billiger Länder erzeugte einen Informationskoeffizienten von etwa 0,17, unabhängig davon, ob das untere Tritil oder der Markt die Vergleichsbasis war.
- Über die von Grove et al. gesichteten Arbeiten lag die mittlere Genauigkeit der menschlichen Teilnehmer bei 66,5 Prozent und die mittlere Hit Ratio der quantitativen Modelle bei 73,2 Prozent.
- Goldbergs Regel auf zehn MMPI-Scores traf die Diagnose neurotisch oder psychotisch außer Stichprobe zu rund 70 Prozent und schlug selbst den besten Psychologen, auch wenn diesem die Regelvorhersage vorlag.
- Die Regel von Leli und Filskov erkannte 83 Prozent neuer Fälle. Unerfahrene Kliniker lagen bei 63 Prozent, erfahrene bei 58 Prozent. Mit der Modellausgabe stiegen die Quoten auf 68 und 75 Prozent und blieben unter dem Modell. Die erfahrenen waren ohne Modell schlechter als die unerfahrenen.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- Bei einem Gewinnziel von 0,1 und einer Ziel-Sharpe-Ratio von 1,5 steigt die nötige Trefferwahrscheinlichkeit, wenn die Verlustauszahlung negativer wird oder die jährliche Wettzahl sinkt.

## Regeln und Kriterien

- Liegt die Wahrscheinlichkeit, die kritische Trefferquote zu unterschreiten, über 0,05, wird die Strategie typischerweise als zu riskant verworfen.
- Die Verwerfungsgrenze von 0,05 gilt auch für Anlagen in Instrumenten mit niedriger Volatilität.
- Soll die Strategie eingesetzt werden, muss die kritische Trefferwahrscheinlichkeit gesenkt werden.
- Gesetze unterscheiden sich in ihrer Vorhersagekraft, und die mit den konsistentesten Beziehungen sind die wertvollsten.
- Bei sonst gleichen Bedingungen ist eine Regel der technischen Analyse, die in 52 Prozent der Fälle erfolgreich ist, weniger wertvoll als eine, die in 70 Prozent der Fälle funktioniert.
- Der Swing Entry sollte eine höhere Trefferquote haben als der Trailing-One-Bar-Entry, bei gewöhnlich größerem Kapitaleinsatz.
- Ein Einstieg sehr bald nach der Momentumumkehr der kleineren Zeitebene kann eine niedrigere Trefferquote haben, dafür einen kleineren Einsatz.

## Risiken und Grenzen

- Der häufigste Induktionsfehlschluss ist die voreilige Verallgemeinerung aus zu wenigen oder qualitativ schlechten Belegen; Regelstudien mit nur wenigen erfolgreichen Signalen gehören vermutlich dazu.
- Es wird viele Setups geben, die gar nicht ausgeführt werden, und viele Verluste, bei denen der Markt sofort dreht und den Trade ausstoppt. Die Verluste sollen dann relativ klein bleiben.

## Beispiele

- Bei symmetrischer Auszahlung und einer Trefferwahrscheinlichkeit von 0,55 erfordert eine annualisierte Sharpe Ratio von 2 insgesamt 396 Wetten pro Jahr.
- Bei 52 Wetten pro Jahr ist für eine annualisierte Sharpe Ratio von 2 eine Trefferwahrscheinlichkeit von 0,6336 nötig.
- Bei 260 Wetten, Verlustauszahlung minus 0,01 und Gewinnauszahlung 0,005 liefert eine Trefferwahrscheinlichkeit von 0,7 eine annualisierte Sharpe Ratio von 1,173.
- Bei 260 Wetten, Verlustauszahlung minus 0,01 und Gewinnauszahlung 0,005 liefert eine Trefferwahrscheinlichkeit von 0,72 eine annualisierte Sharpe Ratio von 2.
- Bei Verlustauszahlung minus 0,01 und Gewinnauszahlung 0,005 liegt die kritische Trefferwahrscheinlichkeit für eine Sharpe Ratio von null bei zwei Dritteln.
- Bei Verlustauszahlung minus 0,01 und Gewinnauszahlung 0,005 zehrt ein Rückgang der Trefferwahrscheinlichkeit von 0,7 auf 0,67 den erwarteten Gewinn auf.
- Im Value-Portfolio der billigsten 20 % erzeugen nur etwa die Hälfte der Titel die Outperformance im ersten Jahr und fast 60 % nach fünf Jahren.
- Im Portfolio der teuersten 20 % nach dem Kurs-Gewinn-Verhältnis schlagen im ersten Jahr nur 38 % der Titel den Markt und nach fünf Jahren 34 %.
- Von den langfristig besten Fonds lagen auf Basis von Jahresdaten 73 % einmal im untersten Dezil und auf Dreijahressicht einer von dreien.
- Das Portfolio aus Value-Rückkäufen minus Growth-Emittenten hatte nur in 6 von 30 Jahren eine negative Rendite.
- Der Dividendenrendite-Länderkorb trifft in 59 Prozent der Calls, der Kurs-Buchwert-Länderkorb in 56 Prozent.
- Beide Länder-Value-Strategien bestehen den t-Test auf unterschiedliche Mittel und den t-Test, dass die Long-Short-Rendite von null verschieden ist, Schwelle Betrag über 1,6 für 95 Prozent.
- Der Anteil richtiger Calls beträgt 0,57 im Kurs-Gewinn-Länderkorb.
- Der Anteil richtiger Calls beträgt 0,67 im Momentum-Länderkorb.
- Die erneut ausgewiesene Dividendenrendite trifft in 59 Prozent der Calls.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 96–115 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-006-p096-p115|S. 96–115]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 115–134 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-007-p115-p134|S. 115–134]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 286–305 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-016-p286-p305|S. 286–305]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 305–324 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-017-p305-p324|S. 305–324]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 153–172 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-012-p153-p172|S. 153–172]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 172–176 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-013-p172-p176|S. 172–176]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 229–248 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-013-p229-p248|S. 229–248]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 134–153 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-008-p134-p153|S. 134–153]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 248–267 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-014-p248-p267|S. 248–267]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 267–286 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-015-p267-p286|S. 267–286]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 286–305 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-016-p286-p305|S. 286–305]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 381–400 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-021-p381-p400|S. 381–400]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 400–419 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-022-p400-p419|S. 400–419]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 419–438 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-023-p419-p438|S. 419–438]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 438–457 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-024-p438-p457|S. 438–457]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 216–235 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-016-p216-p235|S. 216–235]]

## Verwandte Themen
