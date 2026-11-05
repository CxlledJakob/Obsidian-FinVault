---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Modelle"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Hidden-Markov-Modell


## Kurzdefinition

- Das Markov-Switching-autoregressive Modell von Hamilton (1989) schaltet den bedingten Mittelwert über eine verborgene zweistufige Markov-Kette erster Ordnung.

## Kernaussagen

- Im zweistufigen Markov-Switching-Modell ist der Zustandsvektor S = (s1, …, sn)' ein Vektor augmentierter Parameter und wird im Gibbs-Sampling mitgeschätzt; die künftigen Zustände der Renditen sind unbekannt.
- Die Übergänge lauten P(st = 2 | st−1 = 1) = e1 und P(st = 1 | st−1 = 2) = e2 mit 0 < ei < 1; ein kleines ei bedeutet Verharren im Zustand i mit erwarteter Dauer 1/ei.
- In Zustand i gilt rt = βi√ht + √ht εt und ht = αi0 + αi1 ht−1 + αi2 a²t−1, mit at = √ht εt und gaußschem weißem Rauschen εt vom Mittel 0 und der Varianz 1; zur eindeutigen Beschriftung wird β2 > β1 gesetzt.
- Eine Prognose ist eine Mischung über die möglichen Zustandskonfigurationen und hat deshalb oft hohe Unsicherheit in der Punktprognose.
- Die Posterior-Verteilung der Übergangswahrscheinlichkeit ei ist Beta(γi1 + ℓi, γi2 + ni − ℓi), mit ℓi Wechseln aus Zustand i und ni Beobachtungen in diesem Zustand.

## Funktionsweise

- Die Übergangswahrscheinlichkeiten sind P(s_t = 2 | s_{t−1} = 1) = w_1 und P(s_t = 1 | s_{t−1} = 2) = w_2. Ein kleines w_i verlängert die Verweildauer, und 1/w_i ist die erwartete Dauer in Zustand i.
- Die Innovationen der beiden Zustände sind voneinander unabhängige iid-Folgen mit Mittel null und endlicher Varianz.
- Anders als beim SETAR, das den Wechsel deterministisch über eine beobachtete Verzögerung steuert, ist das Regime im MSA stochastisch. Man ist nie sicher, in welchem Zustand x_t liegt.
- Bei großer Stichprobe erlauben Filterverfahren einen Rückschluss auf den Zustand. Im SETAR ist das Regime bekannt, sobald x_{t−d} beobachtet ist.
- Prognosen eines MSA sind stets eine Linearkombination der Teilmodelle. Prognosen eines SETAR stammen aus einem einzigen Regime, solange x_{t−d} beobachtet ist, und werden erst zur Linearkombination, wenn der Horizont die Verzögerung d übersteigt.
- Die Zustände sind nicht direkt beobachtbar, die Schätzung ist deshalb schwieriger. Hamilton (1990) nutzt den EM-Algorithmus, McCulloch und Tsay (1994) Markov-Chain-Monte-Carlo.
- McCulloch und Tsay (1993) lassen w_1 und w_2 logistische oder Probit-Funktionen von erklärenden Variablen sein, die zur Zeit t−1 verfügbar sind.
- Das MSA lässt sich auf mehr als zwei Zustände erweitern. Der Rechenaufwand steigt dabei schnell. Hamilton (1994, Kapitel 22) behandelt Markov-Switching in der Ökonometrie.
- Die Zustände werden einzeln aus der bedingten Posterior-Verteilung gezogen: P(sj = 1) setzt die Markov-Wahrscheinlichkeit gegeben sj−1 und sj+1 mit der Likelihood L(sj) ins Verhältnis beider Zustände, und die Ziehung erfolgt über eine Gleichverteilung auf [0, 1].
- L(sj = i) ist proportional zu exp(fji), und fji summiert von t = j bis n die Terme −1/2 [ln ht + a²t/ht]; at ist rt − β1√ht in Zustand 1 und rt − β2√ht sonst.
- Sind e1 und e2 klein, sind benachbarte Zustände stark korreliert, und gemeinsames Ziehen mehrerer Zustände ist effizienter; die Aufzählung aller Konfigurationen wird dabei schnell aufwendig.
- Gegeben h1, die αi und den Zustandsvektor S lässt sich der Volatilitätsvektor H = (h2, …, hn)' rekursiv berechnen.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Für die Wachstumsrate des realen vierteljährlichen US-GNP, zweites Quartal 1947 bis erstes Quartal 1991, mit p = 4, beträgt das mittlere Wachstum 0,965 in der Expansion und −1,288 in der Kontraktion. Die erwarteten Dauern sind etwa 11,31 und 3,69 Quartale.
- Die Wahrscheinlichkeit, eine Kontraktion zu verlassen, ist 0,286, die Wahrscheinlichkeit, in eine zu springen, ist 0,118. Die AR-Koeffizienten bei Lag 2 unterscheiden sich stark, 0,029 gegen 0,628.
- Die Posterior-Schätzungen stammen aus einem Gibbs-Sampler mit 5000 Iterationen. Die großen Posterior-Standardabweichungen im Kontraktionszustand spiegeln die wenigen negativen Quartale.
- Chen, McCulloch und Tsay (1997) nutzen die Markov-Kette zum Vergleich nicht verschachtelter nichtlinearer Modelle, etwa bilinear gegen SETAR, indem jedes Modell ein Zustand ist. Das verallgemeinert das bayesianische Odds-Ratio.
- Bei den monatlichen GE-Logrenditen von Januar 1926 bis Dezember 1999, 888 Beobachtungen, sind die Posterior-Mittel e1 = 0,089 und e2 = 0,112, und die erwarteten Zustandsdauern liegen bei etwa 11 und 9 Monaten.
- Abbildung 12.14(b) zeigt für jede Beobachtung die Posterior-Wahrscheinlichkeit, in Zustand 2 zu sein, berechnet aus den letzten 2000 Iterationen eines Gibbs-Laufs mit insgesamt 5000 plus 2000 Iterationen.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 210–229 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-012-p210-p229|S. 210–229]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 685–704 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-037-p685-p704|S. 685–704]]

## Verwandte Themen
