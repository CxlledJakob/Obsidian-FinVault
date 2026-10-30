---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/18 - Positionsmanagement/18 - Positionsmanagement|18 - Positionsmanagement]]"
weitere_hauptthemen: []
unterthema: "Positionsgröße"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Kelly-Kriterium


## Kurzdefinition

- Die Kelly-Formel bestimmt den optimalen Hebel und die optimale Kapitalallokation und wägt dabei Renditen gegen Risiken ab.
- Bei gaußverteilten Renditen ist der optimale Hebel f gleich dem mittleren Excess Return m geteilt durch die Varianz s hoch 2 der Excess Returns.

## Kernaussagen

- Das Risikomanagement dieses Buches beruht weiter auf der Kelly-Formel, wird aber durch praktische Erfahrung mit schwarzen Schwänen, Constant Proportion Portfolio Insurance und Stop-Losses gemildert.
- Der Autor bezieht auf die Kelly-Formel das Wort von Robert H. Jackson, doktrinäre Logik sei mit etwas praktischer Weisheit zu mäßigen.
- Gesucht wird der optimale Hebel in realistischen Situationen, in denen keine Gauß-Verteilung der Renditen mehr angenommen werden kann.
- Zusätzlich wird geprüft, ob Risikoindikatoren ein nützlicher Bestandteil eines umfassenden Risikomanagements sein können.
- Das vorherige Buch Quantitative Trading behandelte das Risikomanagement über die Kelly-Formel, neben dem Finden von Strategieideen, dem Backtesting und grundlegenden Fragen der automatisierten Ausführung.
- Thorp (1997) legt die Formel dar, und Chan (2009) widmet ihr in Quantitative Trading ein Kapitel.
- Ist die Gauß-Annahme eine gute Näherung und werden alle Gewinne reinvestiert, erzeugt f die höchste zusammengesetzte Wachstumsrate.
- Schätzfehler bei wahrem Mittelwert und wahrer Varianz sind unvermeidlich, und die künftigen Werte müssen nicht den historischen entsprechen.
- Ein überschätzter Mittelwert oder eine unterschätzte Varianz kann über einen zu hohen Hebel zum Ruin führen; ein zu niedriger Hebel senkt nur die Wachstumsrate.
- Viele Händler nutzen deshalb den halben Kelly-Hebel, und in der Praxis gilt der Kelly-Hebel als Obergrenze.
- Die Formel teilt auch die Kaufkraft optimal auf mehrere Portfolios oder Strategien auf, nicht nur den Hebel einer Strategie.
- Die Mathematik nennt die Allokation über das Gesamtportfolio optimal, unter der Annahme unveränderter erwarteter Renditen und Volatilitäten.
- Nach einem schweren Drawdown ist zweifelhaft, ob diese Erwartungen unverändert sind.

## Funktionsweise

- Für mehrere Portfolios ist der Vektor F gleich C hoch minus 1 mal M, mit der Kovarianzmatrix C der Portfoliorenditen und dem Vektor M der mittleren Excess Returns.
- Bei einem Dollar Eigenkapital und F gleich 3,2 und 1,5 hat das erste Portfolio den Marktwert 3,2 Dollar und das zweite 1,5 Dollar.
- Liegt die Summe der Beträge der Fi über dem Höchsthebel Fmax, ist es nicht wachstumsoptimal, alle Fi proportional auf Fmax zu kürzen.
- Ist Fmax viel kleiner als diese Summe, ist oft die gesamte Kaufkraft auf die Strategie mit dem höchsten mittleren Excess Return optimal.
- Die Formel g gleich F transponiert C F durch 2 gilt nur, wenn die verwendeten Hebel optimal sind; der risikofreie Zins ist im Beispiel null.
- Bei einem Bündel von Strategien ist zu entscheiden, ob das Kapital nach dem Eigenkapital des Gesamtportfolios zugeteilt wird, sodass gute Strategien schlechte kurzfristig subventionieren.
- Die Alternative wendet Kelly auf jede Strategie für sich an, sodass kürzlich schwache Strategien schnell enthebelt werden.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Strategie 1 hat 30 Prozent mittleren Excess Return und 26 Prozent Volatilität, Strategie 2 hat 60 und 35 Prozent, bei Korrelation null und Gauß-Verteilung; die Kelly-Hebel sind 4,4 und 4,9, die Summe 9,3, und g beträgt 2,1.
- Bei Fmax gleich 2 werden sie proportional auf 0,95 und 1,05 gekürzt und g fällt auf 0,82; das Optimum ist F2 gleich 2 mit g gleich 0,96.
- Die Mean-Reversion-Strategie aus Beispiel 5.1 hat auf den Tagesrenditen des Testsets den Kelly-Hebel 18,4; Monte Carlo ergibt etwa 19, die historische Optimierung wieder 18,4.
- Russell 1000 und Russell 2000 haben einen Kelly-Hebel von etwa 1,8; die 3-fach-ETFs BGU und TNA liegen per Konstruktion darüber, und ihr Nettoinventarwert kann auf null gehen.

## Unterschiedliche Quellenpositionen

- Mathematisch ist Kelly auf das gesamte Portfolio optimal, solange erwartete Renditen und Volatilitäten unverändert bleiben.
- Der Autor hält die getrennte Anwendung je Strategie für praktischer, damit eine underperformende Strategie schnell ausläuft; nach einem schweren Drawdown ist unklar, ob die Erwartungen noch dieselben sind.
- Die Erfahrung des Autors ist, dass Kelly je Strategie praktischer ist, damit jede bei Underperformance schnell verkümmert, als die Kelly-Allokation über alle Strategien.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]

## Verwandte Themen
