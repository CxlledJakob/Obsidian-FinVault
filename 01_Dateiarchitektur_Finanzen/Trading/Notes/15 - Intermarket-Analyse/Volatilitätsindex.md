---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/15 - Intermarket-Analyse/15 - Intermarket-Analyse|15 - Intermarket-Analyse]]"
weitere_hauptthemen: []
unterthema: "Risikoindikatoren"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Volatilitätsindex


## Kurzdefinition


## Kernaussagen

- Der VIX-Index ist mean-reverting und im ADF-Test mit 99 Prozent Sicherheit stationär.
- VX ist der Future auf den VIX an der Futures-Börse der CBOE, der CFE.
- Die back-adjustierten Front-Month-Preise von VX mean-reverten laut ADF definitiv nicht und fallen außerhalb weniger Spitzen unaufhaltsam.
- Mean Reversion der VX-Preise zeigt sich erst nach den Spitzen um den 20. November 2008 in der Kreditkrise, den 20. Mai 2010 nach dem Flash Crash und den 3. Oktober 2011.
- Der Unterschied zwischen VIX und dem Front-Month-VX ist vollständig die Roll-Rendite.
- VX war etwa drei Viertel der Zeit in Contango, und die durchschnittliche Roll-Rendite ist annualisiert minus 50 Prozent (Simon und Campasano, 2012).
- Dieses Contango ist der Grund, warum eine Momentum-Strategie auf VX ziemlich gut funktioniert.
- VIX ist kein gehandelter Basiswert, deshalb gilt Gleichung 5.7 für den VX-Future nicht, und die Log-Preise der VX-Futures gegen die Restlaufzeit liegen nicht auf einer Geraden.
- VX-Kalenderspreads sind mean-reverting, obwohl der VX-Future selbst nicht mean-reverting ist; die Formeln von Dupoyet, Daigler und Chen 2011 erklären das nicht.
- Ein ADF-Test auf dem Verhältnis Back zu Front von VX zeigt Stationarität mit 99 Prozent Wahrscheinlichkeit.
- Volatilität ist mit dem Aktienindex antikorreliert: fällt der Markt, steigt die Volatilität stark, und in geringerem Maß gilt das auch umgekehrt.
- Ein Punkt Bewegung im VX-Future entspricht 1.000 Dollar.
- Die Rollrendite von VX kann bis minus 50 Prozent annualisiert betragen.
- VX ist mit ES hoch antikorreliert, der Korrelationskoeffizient der Tagesrenditen erreicht minus 75 Prozent.
- Die Rollrendite von ES beträgt nur etwa 1 Prozent annualisiert, deshalb hat ES fast dieselben Renditen wie der Basiswert.
- Einen Optionskorb zu halten, der den VIX nachbildet, ist sehr teuer, und kein ETF-Sponsor tut das.
- Gleichung 5.7 gilt für VX nicht, die Forward-Preise liegen nicht auf einer Geraden, und die Rollrendite wird als Preisdifferenz zwischen VIX und VX geteilt durch die Zeit bis zur Fälligkeit gemessen.
- Ist der Frontkontrakt teurer als der Spot, ist die Rollrendite negativ.
- In Kapitel 5 lieferte die Kointegration von VX und ES eine Mean-Reversion-Strategie; hier werden der große Rollrendite-Betrag von VX, der kleine von ES und die Antikorrelation für eine Momentum-Strategie genutzt.
- Der VIX, der Index der impliziten Volatilität, wurde als führender Risikoindikator für die Rendite des nächsten Tages getestet.
- Führende Risikoindikatoren sagen voraus, ob die nächste Periode riskant wird; allgemeine Risikoindikatoren fallen nur mit der riskanten Phase zusammen.
- Es gibt keinen Risikoindikator für alle Strategien: Was für eine Strategie riskant ist, kann für eine andere hoch profitabel sein.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- Die lineare Ratio-Strategie mit 15 Tagen Lookback erzielt auf VX vom 27. Oktober 2008 bis zum 23. April 2012 eine annualisierte Rendite von 17,7 Prozent bei einer Sharpe Ratio von 1,5 und lief vor Oktober 2008 deutlich schlechter.
- Die Regression ES mal 50 gleich minus 0,3906 mal VX mal 1.000 plus 77.150 Dollar hat eine Residuen-Standardabweichung von 2.047 Dollar.
- Long 0,3906 VX und long ein ES soll ein stationäres Portfolio sein.
- Die Bollinger-Band-ähnliche Strategie auf diesem Portfolio erzielt vom 29. Juli 2010 bis zum 8. Mai 2012 eine annualisierte Rendite von 12,3 Prozent bei einer Sharpe Ratio von 1,4.
- Vom 29. Juli 2010 bis zum 7. Mai 2012, einem Zeitraum, der nicht für die Hedge Ratio verwendet wurde, beträgt die annualisierte Rendite 6,9 Prozent bei einer Sharpe Ratio von 1.
- SPY korreliert mit dem VIX-Spot passend, gehandelt wird aber ES, weil Futures leichter zu handeln sind als ein ETF.

## Regeln und Kriterien

- Liegt der VX-Frontkontrakt um 0,1 Punkte mal der Zahl der Handelstage bis zum Settlement über dem VIX, werden 0,3906 Frontkontrakte VX und ein Frontkontrakt ES geshortet und einen Tag gehalten.
- Liegt der VX-Frontkontrakt um dieselbe Schwelle unter dem VIX, werden 0,3906 Frontkontrakte VX und ein Frontkontrakt ES gekauft und einen Tag gehalten.
- Die Hedge Ratio folgt der Preisregression in Gleichung 5.11 und nicht der Renditeregression von Simon und Campasano 2012, das Settlement ist der Tag nach dem Kontraktverfall.

## Risiken und Grenzen

- Das Future-Preismodell mit konstanter Roll-Rendite gilt nur, wenn der Basiswert ein gehandeltes Asset ist; der VIX ist keines, und die Log-VX-Preise gegen die Restlaufzeit liegen nicht auf einer Geraden.
- Alternative Formeln für VX, etwa von Dupoyet, Daigler und Chen 2011, erklären nach dem Befund des Autors die mean-reverting Eigenschaft der VX-Kalender-Spreads nicht.
- Um die Finanzkrise 2008 wechselt das Regime von VIX und seinen Futures.
- Von August 2008 bis 2012 ist die Volatilität bei gegebenem Indexstand niedriger als von 2004 bis Mai 2008, die Spannweite der Volatilitäten aber größer.
- Backtests solcher Indikatoren sind wegen seltener Paniken anfällig für Data-Snooping.
- Kein Finanzindikator sagt natürliche oder andere nichtfinanzielle Katastrophen voraus.

## Beispiele

- Die Buy-on-Gap-Aktienstrategie aus Kapitel 4 hatte vom 11. Mai 2006 bis 24. April 2012 etwa 8,7 Prozent annualisierte Durchschnittsrendite und eine Sharpe Ratio von 1,5.
- Lag der VIX des Vortags über 35, einer üblichen Schwelle für hoch riskante Phasen, betrug die annualisierte Durchschnittsrendite dieses Tages 17,2 Prozent bei einer Sharpe Ratio von 1,4; die Strategie profitiert also von diesem sogenannten Risiko.
- Die FSTX-Opening-Gap-Strategie hatte vom 16. Juli 2004 bis 17. Mai 2012 etwa 13 Prozent annualisierte Durchschnittsrendite und eine Sharpe Ratio von 1,4.
- Bei einem VIX des Vortags über 35 fallen diese Werte auf 2,6 Prozent und eine Sharpe Ratio von 0,16; der VIX sagt hier, am Folgetag nicht zu handeln.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]

## Verwandte Themen
