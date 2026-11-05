---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/13 - Volatilität/13 - Volatilität|13 - Volatilität]]"
weitere_hauptthemen: []
unterthema: "Volatilitätsmessung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Implizite Volatilität


## Kurzdefinition


## Kernaussagen

- Volatilität ist mit dem Aktienindex antikorreliert: fällt der Markt, schießt die Volatilität nach oben, und in geringerem Maß gilt das auch umgekehrt.
- Das Streudiagramm der Front-Month-Preise von ES gegen VX zeigt zwei Hauptregime, 2004 bis Mai 2008 und August 2008 bis 2012.
- Im zweiten Regime ist die Volatilität bei gegebenem Aktienindexstand deutlich niedriger, die Spannweite der Volatilitäten aber größer, sodass extremere Volatilitätstage vorkommen als zuvor.
- Kürzere Abschnitte können Übergangsregime sein und werden in der Analyse ignoriert; das zweite Regime reicht bis zum Zeitpunkt des Schreibens.
- VIX ist kein gehandelter Basiswert, deshalb gilt Gleichung 5.7 für den VX-Future nicht, und die Log-Preise der VX-Futures gegen die Restlaufzeit liegen nicht auf einer Geraden.
- Um die Finanzkrise 2008 ändern VIX und seine Futures das Verhalten, was mit dem Leistungssprung der VX-Kalenderspread-Strategie um Oktober 2008 zusammenhängen kann.
- Eine Regression oder ein Johansen-Test auf der Mischung beider Regime wäre ein Fehler; verwendet wird nur das zweite Regime.
- Akzeptiert man, dass Optionspreise einem Modell wie Black-Scholes folgen, lässt sich aus dem Preis die implizite Volatilität gewinnen.
- Für einen europäischen Call ist sigma t diejenige annualisierte bedingte Standardabweichung, die in der Black-Scholes-Formel den beobachteten Preis erzeugt.
- Die Formel lautet ct gleich Pt mal Phi von x minus K mal e hoch minus r ell mal Phi von (x minus sigma t mal Wurzel ell), mit x gleich [ln von Pt durch K plus r ell] durch (sigma t mal Wurzel ell) plus ein halb sigma t mal Wurzel ell.
- Pt ist der aktuelle Aktienkurs, K der Ausübungspreis, ell die Restlaufzeit in Jahren, r der stetig verzinste risikofreie Zins und Phi die Verteilungsfunktion der Standardnormalverteilung.
- Diese implizite Volatilität setzt voraus, dass der Basiswert einer geometrischen Brownschen Bewegung folgt, und kann von der tatsächlichen Volatilität abweichen; der Ansatz wird kritisiert, weil die Modellannahmen in der Praxis nicht gelten müssen.
- Erfahrungsgemäß liegt die implizite Volatilität einer Anlagerendite über der aus einem GARCH-artigen Modell, möglicherweise wegen einer Volatilitätsrisikoprämie oder wegen der Berechnung der Tagesrenditen.
- Der VIX der CBOE ist eine implizite Volatilität.
- Ein amerikanischer Call darf jederzeit am oder vor dem Verfall ausgeübt werden; die Black-Scholes-Formel im Text gilt dem europäischen Call, der nur am Verfall ausübbar ist.
- Das auf der Brownschen Bewegung beruhende Diffusionsmodell erklärt manche Eigenschaften von Asset-Renditen und Derivatepreisen nicht, darunter das Volatility Smile der impliziten Volatilitäten (Bakshi, Cao und Chen 1997).
- Aus dem Geld und im Geld liegende Optionen haben tendenziell höhere implizite Volatilitäten als am Geld liegende Optionen, besonders an den Devisenmärkten.
- Bei Aktienoptionen ist dieses Smile der impliziten Volatilität weniger ausgeprägt.
- Jump-Diffusion- und stochastische Volatilitätsmodelle wurden vorgeschlagen, um diese Unzulänglichkeit zu beheben (Merton 1976, Duffie 1995).
- Das Sprungdiffusionsmodell von Kou (2002) kann das Smile der impliziten Volatilitäten nachbilden.
- GARCH-Modelle neigen dazu, die Volatilität im Vergleich zur impliziten Volatilität aus der Derivatebewertung zu unterschätzen; ein Grund ist, dass sie die Parameter als fest gegeben behandeln, während die MCMC-Prognose eines stochastischen Volatilitätsmodells die Parameterunsicherheit einbezieht.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Für die monatlichen S&P-500-Logrenditen mit Prognoseursprung Dezember 1999 liegen die GARCH(1,1)-Volatilitätsprognosen der Horizonte 1 bis 5 bei 17,98, 18,12, 18,24, 18,34 und 18,42, die des stochastischen Volatilitätsmodells höher bei 19,31, 19,36, 19,35, 19,65 und 20,13.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 138–143 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-010-p138-p143|S. 138–143]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 134–153 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-008-p134-p153|S. 134–153]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 324–343 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-018-p324-p343|S. 324–343]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 685–704 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-037-p685-p704|S. 685–704]]

## Verwandte Themen
