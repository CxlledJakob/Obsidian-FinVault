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
aktualisiert: 2026-11-01
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

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- Die lineare Mean-Reversion-Strategie mit dem Ratio als Signal und einem Lookback von 15 Tagen für Durchschnitt und Standardabweichungen erzielt vom 27. Oktober 2008 bis zum 23. April 2012 eine annualisierte Rendite von 17,7 Prozent bei einer Sharpe Ratio von 1,5.
- Vor Oktober 2008 schnitt diese Strategie deutlich schlechter ab, und der Text hält einen Regimewechsel von VIX und seinen Futures um die Finanzkrise 2008 für einen möglichen Zusammenhang.

## Regeln und Kriterien


## Risiken und Grenzen

- Gleichung 5.7 gilt nur, wenn der Basiswert des Futures ein gehandeltes Asset ist; der VIX ist keines, und die Log-VX-Preise gegen die Restlaufzeit fallen nicht auf eine Gerade.
- Vorgeschlagene alternative Formeln für VX, darunter Dupoyet, Daigler und Chen 2011, erklären nach dem Befund des Autors die mean-reverting Eigenschaft der VX-Kalender-Spreads nicht.

## Beispiele


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
