---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/13 - Volatilität/13 - Volatilität|13 - Volatilität]]"
weitere_hauptthemen: []
unterthema: "Volatilitätsdynamik"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Mean Reversion der Volatilität


## Kurzdefinition


## Kernaussagen

- Volatilität ist mean-reverting; genauer ist der VIX-Index mean-reverting, und ein ADF-Test zeigt ihn mit 99 Prozent Sicherheit als stationär.
- Daraus folgt nicht, dass der Handel der VX-Futures eine gute Mean-Reversion-Strategie ist: die back-adjustierten Front-Month-Preise mean-reverten laut ADF definitiv nicht.
- Mean Reversion in VX tritt erst auf, nachdem die Volatilität um den 20. November 2008 in der Kreditkrise, um den 20. Mai 2010 nach dem Flash Crash und erneut am 3. Oktober 2011 ihren Höhepunkt erreicht hatte; sonst fällt die Reihe unaufhaltsam.
- Der Unterschied zwischen VIX und dem Front-Month-VX ist vollständig die Roll-Rendite.
- Der VX-Future war etwa drei Viertel der Zeit in Contango, und die durchschnittliche Roll-Rendite ist annualisiert sehr negativ, minus 50 Prozent (Simon und Campasano, 2012).
- Dieses anhaltende Contango ist der Grund, warum eine Momentum-Strategie auf VX ziemlich gut funktioniert, wie Kapitel 6 zeigt.
- VX-Kalenderspreads sind mean-reverting, obwohl der VX-Future selbst nicht mean-reverting ist.
- Gleichung 5.7 erklärt das nicht, weil sie nur für einen Future gilt, dessen Basiswert gehandelt wird, und VIX ist kein gehandeltes Asset; die Log-Preise der VX-Futures gegen die Restlaufzeit liegen nicht auf einer Geraden.
- Auch die alternativen Formeln, etwa von Dupoyet, Daigler und Chen 2011, erklären diese Mean Reversion der Kalenderspreads nicht.
- Ein ADF-Test auf dem Verhältnis Back zu Front von VX zeigt Stationarität mit 99 Prozent Wahrscheinlichkeit.
- Die lineare Ratio-Strategie auf dem VX-Kalenderspread hat in diesem Abschnitt eine Sharpe Ratio von 1,5, und Abbildung 5.8 zeigt ihre kumulierten Renditen.
- Saisonalität kann dazu führen, dass an einem Markt nur Kalenderspreads bestimmter Monate und bestimmter Abstände mean-reverten; der Text verfolgt diese marktabhängigen Einzelheiten nicht weiter.
- Die Mehrschrittprognosen der Volatilität eines GARCH(1,1) laufen gegen die unbedingte Varianz von at, wenn der Horizont gegen unendlich geht und alpha 1 plus beta 1 kleiner als 1 ist, die Varianz also existiert.
- Die geschlossene Form ist alpha 0 mal [1 minus (alpha 1 plus beta 1) hoch (ell minus 1)] durch (1 minus alpha 1 minus beta 1) plus (alpha 1 plus beta 1) hoch (ell minus 1) mal der Ein-Schritt-Prognose.
- Beim IGARCH mit alpha 1 plus beta 1 gleich 1 bleibt die Wirkung der Ein-Schritt-Prognose dauerhaft, und die Varianzprognosen bilden eine Gerade mit der Steigung alpha 0: sigma h von ell gleich sigma h von 1 plus (ell minus 1) mal alpha 0.
- Ist in diesem IGARCH(1,1) zusätzlich alpha 0 gleich 0, bleibt die Varianzprognose auf allen Horizonten gleich der Ein-Schritt-Prognose.
- Für die S&P-500-Überschussrenditen liegt die prognostizierte bedingte Standardabweichung am Ursprung Dezember 1991 bei 0,0536 im ersten Monat und bei 0,0560 im Unendlichen, nahe der unbedingten Varianz 0,00314 des stationären GARCH(1,1).
- Die Mehrschrittprognosen des EGARCH(1,1) für die monatlichen IBM-Logrenditen am Ursprung t = 864 konvergieren allmählich zur Stichprobenvarianz 4,37×10⁻³ des Schockprozesses: 6,05×10⁻³, 5,82×10⁻³, 5,63×10⁻³ und 4,94×10⁻³ an den Horizonten 1, 2, 3 und 10.
- Die univariaten GARCH(1,1)-Gleichungen der Tageslogrenditen von Hang Seng und Nikkei 225 liegen nahe an IGARCH(1,1). Hongkong hat die Koeffizienten 0,143 und 0,855, Japan 0,127 und 0,861. Das wird mit der durch die Subprime-Krise erhöhten Volatilität begründet.
- Im Constant-Correlation-GARCH(1,1) hat das bivariate ARMA(1,1) der quadrierten Schocks einen endlichen Erwartungswert und der Renditeschock eine positiv definite unbedingte Kovarianz, wenn alle Eigenwerte von alpha1 plus beta1 positiv und kleiner als 1 sind.
- Für die Aktienrenditen von IBM und Dell im Vier-Asset-DCC ist die Summe der GARCH-Parameter 0,0372 plus 0,9603 gleich 0,9975. Ihre Volatilitätsreihen zeigen IGARCH-Verhalten, und die Konstanten unterscheiden sich nicht signifikant von null. Die Wechselkursvolatilitäten von Euro und Yen haben einen von null verschiedenen konstanten Term und hohe Persistenz.
- Die Hebeleffekte derselben Aktien sind ebenfalls in IGARCH-Form. Bei einem gemeinsamen Persistenzkoeffizienten von 0,9600 betragen die Hebelkoeffizienten 0,0159 für IBM und 0,0114 für Dell.
- Die univariate Varianzgleichung des gemeinsamen Faktors aus IBM und S&P 500 hat die Koeffizienten 0,110 und 0,825. Die des S&P 500 allein, Tagesdaten 1991 bis 1999, hat 0,092 und 0,894.
- Der Posteriormittelwert von α1 für die monatlichen S&P-500-Logrenditen, Januar 1962 bis Dezember 2009, beträgt 0,837 bei Standardfehler 0,025 und bestätigt starke serielle Abhängigkeit der Volatilitätsreihe.
- Dieser Wert liegt unter dem von Jacquier, Polson und Rossi (1994), die Tagesrenditen des S&P 500 verwendeten.
- Im bivariaten Modell betragen die Posteriormittel α11 = 0,80 und α21 = 0,81, jeweils mit Standardfehler 0,03.
- Die Rückwärtsprognose benutzt η = α0/(1 − α1) mit |α1| < 1 als Niveau der zeitumgekehrten Logvolatilität.
- Im Gauß-GARCH(1,1) derselben Monatsreihe beträgt der Koeffizient von ht−1 0,837, bei t-Ratios aller Koeffizienten über 2,56.
- Die Volatilitätsprognosen eines GARCH(1,1) für die monatlichen S&P-500-Logrenditen steigen mit dem Horizont allmählich zur unbedingten Varianz 3,349/(1 − 0,086 − 0,735) = 18,78.
- Beim GE-GARCH sind die charakteristischen Wurzeln (1 − 0,945B) und (1 − 0,820B) reell und vom Betrag kleiner als 1, deshalb ist die unbedingte Varianz der Rendite endlich.
- Im Markov-Switching-GARCH-M für GE erreicht der Persistenzparameter αi1 + αi2 in Zustand 1 häufig die Grenze 1,0, in Zustand 2 nicht; im Gibbs-Lauf wird αi1 + αi2 < 1 erzwungen.

## Funktionsweise

- Für ein GARCH(1,1) mit φ = α1 plus β1 < 1 und ohne MA-Teil ist die Varianzprognose der k-Perioden-Rendite [α0 / (1 minus φ)] mal [k minus (1 minus φ hoch k) / (1 minus φ)] plus [(1 minus φ hoch k) / (1 minus φ)] mal der Ein-Schritt-Varianz.
- Die mehrstufige Prognose folgt der Rekursion, dass jede weitere Varianzprognose α0 plus (α1 plus β1) mal der vorherigen Varianzprognose ist.

## Voraussetzungen


## Anwendung im Trading

- Die lineare Mean-Reversion-Strategie mit dem Ratio als Signal und einem Lookback von 15 Tagen für Durchschnitt und Standardabweichungen erzielt vom 27. Oktober 2008 bis zum 23. April 2012 eine annualisierte Rendite von 17,7 Prozent bei einer Sharpe Ratio von 1,5.
- Vor Oktober 2008 schnitt diese Strategie deutlich schlechter ab, und der Text hält einen Regimewechsel von VIX und seinen Futures um die Finanzkrise 2008 für einen möglichen Zusammenhang.

## Regeln und Kriterien


## Risiken und Grenzen

- Gleichung 5.7 gilt nur, wenn der Basiswert des Futures ein gehandeltes Asset ist; der VIX ist keines, und die Log-VX-Preise gegen die Restlaufzeit fallen nicht auf eine Gerade.
- Vorgeschlagene alternative Formeln für VX, darunter Dupoyet, Daigler und Chen 2011, erklären nach dem Befund des Autors die mean-reverting Eigenschaft der VX-Kalender-Spreads nicht.

## Beispiele

- Ab dem Prognoseursprung Dezember 1999 lauten die GARCH-Volatilitätsprognosen der Horizonte 1 bis 5: 17,98, 18,12, 18,24, 18,34 und 18,42.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 119–138 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-009-p119-p138|S. 119–138]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 138–143 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-010-p138-p143|S. 138–143]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 153–172 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-009-p153-p172|S. 153–172]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 362–381 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-020-p362-p381|S. 362–381]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 533–552 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-029-p533-p552|S. 533–552]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 552–571 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-030-p552-p571|S. 552–571]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 666–685 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-036-p666-p685|S. 666–685]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 685–704 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-037-p685-p704|S. 685–704]]

## Verwandte Themen
