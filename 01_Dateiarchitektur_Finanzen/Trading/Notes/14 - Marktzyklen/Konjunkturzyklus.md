---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/14 - Marktzyklen/14 - Marktzyklen|14 - Marktzyklen]]"
weitere_hauptthemen: []
unterthema: "Zyklusstruktur"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Konjunkturzyklus


## Kurzdefinition

- Komplexe charakteristische Wurzeln eines AR(2) erzeugen das Verhalten stochastischer Konjunkturzyklen und sind in ökonomischen Zeitreihenmodellen deshalb üblich.
- Die saisonbereinigte vierteljährliche zivile US-Arbeitslosenquote von 1948 bis 1993 bewegt sich gegenzyklisch zu den US-Konjunkturzyklen: sie steigt schnell und fällt langsam.

## Kernaussagen

- Hamilton (1989) modelliert aperiodische Übergänge zwischen Zuständen einer Volkswirtschaft mit einer verborgenen Markov-Kette.
- Im Markov-Switching-AR(4) des realen US-GNP entspricht Zustand 1 Quartalen mit positivem Wachstum, also Expansionen, und Zustand 2 Quartalen mit negativem Wachstum, also Kontraktionen.
- Die mittlere Wachstumsrate beträgt 0,965 in der Expansion und −1,288 in der Kontraktion.
- Eine Kontraktion dauert im Mittel etwa 3,69 Quartale, rund ein Jahr, eine Expansion etwa 11,31 Quartale, rund drei Jahre.
- Der Austritt aus einer Kontraktion, Wahrscheinlichkeit 0,286, ist wahrscheinlicher als der Eintritt, Wahrscheinlichkeit 0,118.
- Die Dynamik unterscheidet sich zwischen Expansion und Kontraktion. Der AR-Koeffizient von x_{t−2} liegt bei 0,029 beziehungsweise 0,628.
- Die Reihe ist die saisonbereinigte vierteljährliche Wachstumsrate des realen US-GNP vom zweiten Quartal 1947 bis zum ersten Quartal 1991. Die Mehrheit der Wachstumsraten ist positiv, negative Quartale sind selten, und die Posterior-Standardabweichungen der Kontraktionsparameter sind deshalb groß.
- Im TAR-Modell entspricht ein Sprung der Quotenänderung Δx_{t−2} um 0,1 oder mehr typischerweise der Kontraktionsphase, in der staatliche Eingriffe und industrielle Umstrukturierung wahrscheinlich sind.
- Das AR(2) dieses Kontraktionsregimes hat komplexe charakteristische Wurzeln und damit mögliches zyklisches Verhalten; die Chance eines Wendepunkts steigt, und Kontraktionsphasen bleiben tendenziell kürzer als Expansionsphasen.
- Im Markov-Switching-Modell steht s_t = 1 für die expansiven Phasen und s_t = 2 für die Kontraktionen; die bedingten Mittel der Quotenänderung sind −0,10 und 0,31.
- Die Wahrscheinlichkeit, aus der Expansion in die Kontraktion zu wechseln, ist 0,084, die Wahrscheinlichkeit der Rückkehr aus der Kontraktion in die Expansion 0,126.
- Der Prognosevergleich trennt die Ursprünge danach, ob die US-Wirtschaft zum Prognosezeitpunkt in einer Kontraktion oder in einer Expansion ist.
- Der Prognosegewinn der nichtlinearen Modelle für die vierteljährliche US-Arbeitslosenquote gegenüber dem linearen Modell konzentriert sich auf Ursprünge, an denen die Wirtschaft in der Kontraktion ist.
- In Expansionen schlägt das lineare Modell sowohl das TAR als auch das Markov-Switching-Modell.
- Während der Kontraktionen sind staatliche Eingriffe und industrielle Umstrukturierung am wahrscheinlichsten und können die Nichtlinearität der Arbeitslosenquote erzeugen.
- Diese Phasen wiegen für die Prognose besonders, weil ökonomische Prognosen in Kontraktionen mehr beachtet werden.

## Funktionsweise

- Bei einem Paar komplexer charakteristischer Wurzeln ist die mittlere Länge der stochastischen Zyklen k gleich 2π geteilt durch den Arkuskosinus von phi1 geteilt durch (2 mal der Wurzel aus minus phi2), mit dem Arkuskosinus im Bogenmaß.
- Schreibt man die komplexen Lösungen als a plus oder minus b i, dann gilt phi1 gleich 2a und phi2 gleich minus (a zum Quadrat plus b zum Quadrat), und k gleich 2π geteilt durch den Arkuskosinus von a geteilt durch den Betrag von a plus oder minus b i.
- Sind beide charakteristischen Wurzeln reell, lässt sich das AR(2) als ein AR(1) auf einem weiteren AR(1) lesen, und die Autokorrelation ist eine Mischung zweier exponentieller Abfälle; ist phi1 zum Quadrat plus 4 phi2 kleiner als 0, sind die Wurzeln ein konjugiert komplexes Paar und die Autokorrelation zeigt gedämpfte Sinus- und Kosinuswellen.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Das angepasste AR(3) der saisonbereinigten vierteljährlichen Wachstumsrate des realen US-Bruttosozialprodukts von 1947.II bis 1991.I lautet rt gleich 0,0047 plus 0,348 rt−1 plus 0,179 rt−2 minus 0,142 rt−3 plus at, mit Residualstandardabweichung 0,0097.
- Die charakteristische Gleichung faktorisiert ungefähr als (1 plus 0,521 B) mal (1 minus 0,869 B plus 0,274 B zum Quadrat) gleich 0; für den quadratischen Faktor ist phi1 zum Quadrat plus 4 phi2 gleich minus 0,341 und damit kleiner als 0, was stochastische Konjunkturzyklen bestätigt.
- Die mittlere Länge dieser stochastischen Zyklen beträgt ungefähr 10,62 Quartale, also etwa 3 Jahre; die Rechnung mit den Beträgen der Wurzeln ergibt 10,65638.
- Trennt ein nichtlineares Modell Expansion und Kontraktion, dauern die Kontraktionen im Mittel etwa drei Quartale und die Expansionen etwa 3 Jahre; 10,62 Quartale sind ein Kompromiss zwischen diesen beiden Dauern.
- Dasselbe periodische Merkmal ist bei Wachstumsraten nationaler Volkswirtschaften verbreitet und findet sich ähnlich bei vielen OECD-Ländern.
- Das Modell (1 minus 0,6 B plus 0,4 B zum Quadrat) rt gleich at hat phi1 zum Quadrat plus 4 phi2 gleich minus 1,24 und damit zwei komplexe charakteristische Wurzeln; seine Autokorrelation zeigt gedämpfte Sinus- und Kosinuswellen.
- Die Lösungen des charakteristischen Polynoms des BSP-AR(3) sind 1,590253 plus 1,063882 i, minus 1,920152 und 1,590253 minus 1,063882 i, mit Beträgen 1,913308, 1,920152 und 1,913308.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 58–77 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-004-p058-p077|S. 58–77]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 210–229 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-012-p210-p229|S. 210–229]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 229–248 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-013-p229-p248|S. 229–248]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 248–267 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-014-p248-p267|S. 248–267]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 343–362 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-019-p343-p362|S. 343–362]]
- Behavioural Investing_ A Practitioners Guide to Applying -- James Montier -- Wiley finance series, Chichester, West Sussex, England, 2007 -- Wiley ; -- isbn13 9780470490297 -- 552a06a98fb1ad4320dc7c3128ea169b -- Ann.pdf, S. 590–609 → [[Trading/Pilot/blocks/behavioural-investing/behavioural-investing-block-032-p590-p609|S. 590–609]]

## Verwandte Themen
