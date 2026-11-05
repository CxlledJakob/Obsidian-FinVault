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

# Compound Annual Growth Rate


## Kurzdefinition

- Die k-Perioden-Bruttorendite ist das Produkt der k Einperioden-Bruttorenditen und heißt Compound Return; die k-Perioden-Nettorendite ist (Pt − Pt−k)/Pt−k.
- Die annualisierte Durchschnittsrendite über k Jahre ist das geometrische Mittel dieser k Einperioden-Bruttorenditen minus eins, also das Produkt hoch 1/k minus 1, gleich exp[(1/k) Summe ln(1 + Rt−j)] minus 1.

## Kernaussagen

- Das Ziel ist die Maximierung des langfristigen Eigenkapitalwachstums; Risiko wird nur vermieden, soweit es dieses Ziel stört.
- Der optimale Hebel maximiert das Nettovermögen oder gleichbedeutend die zusammengesetzte Wachstumsrate.
- Hebel null erzeugt weder Risiko noch Rendite.
- Drei Methoden berechnen diesen Hebel; jede hat eigene Annahmen und Nachteile.
- Ist der maximale Drawdown bei einem Hebel minus 100 Prozent, ist die zusammengesetzte Wachstumsrate ebenfalls minus 100 Prozent, und der Hebel ist nicht optimal.
- Der Hebel muss konstant gehalten werden, mit oder ohne Drawdown-Nebenbedingung, damit die Wachstumsrate optimiert wird.
- Die drei Methoden zur Maximierung der zusammengesetzten Wachstumsrate sind die Kelly-Formel unter Gauß-Annahme, die Monte-Carlo-Optimierung einer nichtgaußschen Verteilung und die direkte Optimierung der historischen Wachstumsrate im Backtest.
- Im Beispiel zweier unkorrelierter gaußscher Strategien mit annualisierten Überschussrenditen von 30 und 60 Prozent und Volatilitäten von 26 und 35 Prozent sind die Kelly-Hebel 4,4 und 4,9, der Bruttohebel 9,3 und die annualisierte Wachstumsrate g = F transponiert mal C mal F geteilt durch 2 gleich 2,1, bei risikofreiem Zins null.
- Wird dieser Bruttohebel proportional auf ein Maximum von 2 gekürzt, auf 0,95 und 1,05, fällt g auf 0,82; Gleichung 8.3 gilt nur bei optimalen Hebeln.
- Unter dieser engen Nebenbedingung ist g mit 0,96 höher, wenn die gesamte Kaufkraft auf die Strategie mit der höchsten Wachstumsrate gelegt wird, also F2 gleich 2 und F1 gleich 0.
- Ist die Rendite gaußisch, reduziert sich g(f) analytisch auf f mal m minus f zum Quadrat mal m zum Quadrat geteilt durch 2, und das Maximum reproduziert Kelly sowie im Ein-Strategie-Fall die maximale Rate aus Gleichung 8.3.
- Für die Mean-Reversion-Strategie liegt das Maximum der auf 100.000 Pearson-Ziehungen geschätzten Wachstumsrate bei einem Hebel von 19, nahe am Kelly-Wert 18,4; die historische Optimierung trifft 18,4.
- Bei Hebel 31 ist die Wachstumsrate minus 1, weil die schlechteste Periodenrendite minus 0,0331 beträgt und jeder Hebel über 1 geteilt durch 0,0331 gleich 30,2 in dieser Periode zum Totalverlust führt.
- In einer CPPI-Simulation über 100.000 Tage mit D gleich 0,5 ist die tägliche Wachstumsrate 0,002484 gegen 0,002525 beim Hebel f mal D auf dem Gesamtkonto.
- Konstanter Hebel 5 auf 100.000 Dollar Eigenkapital verlangt einen Marktwert von 500.000 Dollar. Nach einem Tagesverlust von 10.000 Dollar müssen weitere 40.000 Dollar liquidiert werden, damit der Marktwert 5 mal 90.000 gleich 450.000 Dollar ist; nach einem Gewinn von 20.000 Dollar sind 80.000 Dollar zuzukaufen, weil der Zielwert 550.000 und der aktuelle Wert 470.000 Dollar ist.
- Das US-Value-Portfolio und das Portfolio mit hohem prognostiziertem Wachstum haben seit 1988 sehr ähnliche Renditen erzeugt: Die CAGR des Value-Portfolios beträgt 13,7 Prozent, die des hohen Prognosewachstums 14,0 Prozent.
- Global verdient das Portfolio mit hohem prognostiziertem Gewinnwachstum 10,2 Prozent CAGR pro Jahr, während das Low-PE-Portfolio 15,4 Prozent CAGR pro Jahr erzeugt.
- Die Abbildungen 26.9 und 26.10 zeigen die US- beziehungsweise globalen Portfolios auf der Basis 1987 gleich 100.
- Über die 1990er wuchsen die realen Dividenden nur mit 1,3 % CAGR, während die einbehaltene Gewinnrendite 2,4 % verlangt hätte.
- Von Gipfel zu Gipfel, oder gleichwertig von Tal zu Tal, sind die logarithmierten US-Gewinne nie um mehr als 6 % pro Jahr gewachsen.
- Bottom-up-Analysten erwarteten weiterhin 12 % Gewinnwachstum für das nächste Jahr und 12 % p.a. über die nächsten fünf Jahre.
- Seit 1975 wuchs die US-Marktkapitalisierung mit 13 Prozent CAGR und der Preisindex mit 10 Prozent CAGR; die Differenz ist eine Verwässerung von 3 Prozent pro Jahr.
- Nominales CAGR von Gewinn, Dividende und BIP liegt ohne Ausnahme beim Gewinn und bei der Dividende unter dem BIP, im Schnitt um 1 bis 2 Prozentpunkte pro Jahr; real um 1 bis 3 Prozentpunkte.
- USA, CAGR Gewinn, Dividende, BIP: nominal 1970–2001 gleich 6,0, 5,1 und 7,5 Prozent, 1970–1998 gleich 7,0, 6,0 und 8,1; real 1970–2001 gleich 1,0, 0,2 und 3,1, 1970–1998 gleich 1,5, 0,6 und 3,2.
- Vereinigtes Königreich: nominal 1970–2001 gleich 8,5, 8,0 und 10,2, 1970–1998 gleich 12,0, 10,9 und 13,4; real 1970–2001 gleich 0,9, 0,4 und 2,5, 1970–1998 gleich 1,7, 0,7 und 3,0.
- Deutschland: nominal 1970–2001 gleich 5,8, 6,0 und 6,1, 1970–1998 gleich 5,3, 6,0 und 8,0; real 1970–2001 gleich 2,3, 2,5 und 2,7, 1970–1998 gleich 0,9, 1,6 und 3,5.
- Frankreich ab 1972: nominal bis 2001 gleich 8,0, 7,9 und 8,5, bis 1998 gleich 6,9, 7,4 und 9,0; real bis 2001 gleich 2,0, 1,9 und 2,5, bis 1998 gleich 0,5, 0,9 und 2,5.
- Das Ende der Stichprobe 1998 statt 2001, wegen der schwersten US-Gewinnrezession seit den 1930ern im Jahr 2001, ändert diese CAGR-Schlussfolgerung kaum.
- Die Indexverwässerung, Wachstum des Verhältnisses von Marktkapitalisierung zu Preis 1970–2002, beträgt im Vereinigten Königreich 4,7 Prozent, in Deutschland 4,5, in Frankreich 8,7 und in Japan 3,2 Prozent.
- Die mediane geometrische nominale Zehnjahresrendite beim Kauf im KGV-Quartil 32- bis 20-fach beträgt 5,7 Prozent pro Jahr, im Quartil 13,5- bis 4,0-fach 15 Prozent pro Jahr, Stichprobe 1926–1992.

## Funktionsweise

- Unter einer guten Gauß-Näherung erzeugt der Kelly-Hebel die höchste zusammengesetzte Wachstumsrate, wenn alle Gewinne reinvestiert werden.
- Bei risikofreiem Zins null ist der Erwartungswert der Wachstumsrate g(f) der Durchschnitt von log(1 plus f mal R).
- Ist R gaußisch, lässt sich dieses g(f) analytisch reduzieren, und das Maximum aus der Ableitung nach f gleich null reproduziert die Kelly-Formel.
- Bei optimalen Hebeln und risikofreiem Zins null ist die annualisierte zusammengesetzte Wachstumsrate g gleich F transponiert mal C mal F, geteilt durch 2.
- Bei stetiger Verzinsung ist der Nettowert A = C exp(r × n), wobei r der Jahreszins, C das Anfangskapital und n die Zahl der Jahre ist. Der Barwert ist C = A exp(−r × n).
- Die Näherung der annualisierten Rendite durch das arithmetische Mittel der Einperiodenrenditen kann in manchen Anwendungen zu ungenau sein.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Ein unterschätzter Hebel lässt nur eine untermaximale Wachstumsrate; ein überschätzter kann zum Ruin führen.
- CPPI erzeugt nicht dieselbe zusammengesetzte Rendite wie der Hebel f mal D auf dem Gesamtkonto, außer jede Periode ist positiv.
- Ob CPPI langfristig dieselbe Wachstumsrate wie der Hebel f mal D hat, ist dem Autor kein mathematischer Beweis bekannt.

## Beispiele

- Im Beispiel zweier unkorrelierter Strategien beträgt g bei den Kelly-Hebeln 2,1.
- Unter dem Höchsthebel 2 fällt g bei proportionaler Kürzung auf 0,82 und steigt auf 0,96, wenn die gesamte Kaufkraft auf die Strategie mit der höchsten Wachstumsrate geht.
- Für die Mean-Reversion-Strategie aus Beispiel 5.1 liegt das Monte-Carlo-Maximum von g nahe 19 und numerisch bei 19, gegenüber Kelly 18,4.
- Bei Hebel 31 ist die Wachstumsrate minus 1, also Ruin.
- Die historische Optimierung derselben Strategie ergibt ebenfalls den Hebel 18,4.
- Nach 100.000 Tagen liegen CPPI und die Alternative bei D gleich 0,5 in einer Simulation bei 0,002484 gegen 0,002525 Wachstumsrate pro Tag.
- Bei 10 Prozent Jahreszins und 1 Dollar Startkapital beträgt der Wert nach einem Jahr 1,10000 bei jährlicher, 1,10250 bei halbjährlicher, 1,10381 bei vierteljährlicher, 1,10471 bei monatlicher, 1,10506 bei wöchentlicher und 1,10516 bei täglicher Zinszahlung.
- Bei stetiger Verzinsung nähert sich derselbe Wert exp(0,1); der Text nennt 1,1052, Tabelle 1.1 weist für unendlich viele Zahlungen 1,10517 aus. Die Periodenzinsen der Tabelle sind 0,1, 0,05, 0,025, 0,0083, 0,1/52 und 0,1/365.
- Die zusammengesetzte jährliche einfache Bruttorendite des CRSP-Value-Weighted-Index über 996 Monate von 1926 bis 2008 ist das Produkt aller monatlichen Faktoren (1 plus Rt), potenziert mit 12/996, minus 1, ungefähr 0,093.
- Das Produkt der Bruttofaktoren beträgt 1592,953, und diese Zahl hoch (12/996) minus 1 ergibt 0,0929, also etwa 9,3 Prozent pro Jahr.
- Ein Dollar zu Beginn von 1926 wäre Ende 2008 etwa 1593 Dollar wert.
- Tabelle 27.5 nennt unter der Überschrift 1980 bis 2005 die CAGR von Buy-and-hold des Marktes mit 6,6 % bei Risiko 17,9 und Rendite zu Risiko 0,37, von Buy-and-hold des Value-Index mit 7,8 %, 17,2 und 0,45, vom Long-only-Portfolio auf das zehnjährige Graham-und-Dodd-Kurs-Gewinn-Verhältnis mit 17,8 %, 23,1 und 0,77 und vom zugehörigen Long/Short-Portfolio mit 22,4 %, 16,7 und 1,34.
- Der umgebende Text ordnet dieselben Renditen von 6,6 %, 7,8 %, 17,8 % und 22,4 % p.a. einer Anlage von 100 Dollar seit 1990 zu und nennt für das Long/Short-Portfolio den Zeitraum 1990 bis 2004.
- Das Long-only-Portfolio hatte höheres Risiko als die Buy-and-hold-Strategien; wird das Risiko angeglichen, bleibt eine Rendite von 13,2 % p.a.
- Das Long/Short-Portfolio lieferte die Mehrrendite mit weniger Risiko als die Buy-and-hold-Strategien.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 180–199 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-014-p180-p199|S. 180–199]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 20–39 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-002-p020-p039|S. 20–39]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 58–77 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-004-p058-p077|S. 58–77]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 77–96 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-005-p077-p096|S. 77–96]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 324–343 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-018-p324-p343|S. 324–343]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 343–362 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-019-p343-p362|S. 343–362]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 552–571 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-030-p552-p571|S. 552–571]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 571–590 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-031-p571-p590|S. 571–590]]

## Verwandte Themen
