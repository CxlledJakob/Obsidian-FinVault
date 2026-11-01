---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Zeitreihen"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-01
---

# Unit Root


## Kurzdefinition

- Right-Tail-Unit-Root-Tests prüfen exponentielles Wachstum oder Kollaps unter einer autoregressiven Spezifikation.
- Ein Unit-Root-Test ist ein Testtyp, mit dem festgestellt wird, dass eine Zeitreihe stationär ist.

## Kernaussagen

- Enthält die Reihe eine Unit Root, dann ist der kleinste Fixed-Width-Fracdiff-Koeffizient d*, der sie stationär macht, kleiner als 1.
- Ist die Reihe bereits stationär, gilt d* gleich 0. Zeigt sie explosives Verhalten wie in einer Blase, gilt d* größer als 1.
- Der besonders interessierende Fall ist d* wenig über 0 und weit unter 1. Die Originalreihe ist dann nur mild nichtstationär: Differenzierung ist nötig, eine volle ganzzahlige Differenzierung entfernt aber zu viel Gedächtnis und Prognosekraft.
- Die Null des Chow-Typ-Dickey-Fuller-Tests ist ein Unit Root mit Rho gleich 1, die Alternative ein explosiver Prozess mit Rho größer als 1 nach dem Bruch.
- Standard-Unit-Root- und Kointegrationstests erkennen Blasen schlecht, weil periodisch zusammenbrechende Blasen eher wie ein Unit-Root- oder stationärer autoregressiver Prozess aussehen.
- Im Null-Lag-Modell auf Logpreisen ist Beta gleich 0 der Unit-Root-Zustand: das System ist nichtstationär und verhält sich als Martingal.
- Der gewöhnliche ADF-Test ist der Spezialfall von SADF, bei dem die minimale Fensterlänge gleich Endpunkt minus 1 ist.
- SADF testet auf der ADF-Regression mit Konstante und Lag-Differenzen die Null Beta kleiner oder gleich 0 gegen die Alternative Beta größer als 0.
- Für USD.CAD wird die Unit-Root-Null nicht verworfen: ADF-Statistik minus 1,840744, kritischer 10-Prozent-Wert minus 2,594, AR(1)-Schätzung 0,994120. λ ist negativ, ein Trend liegt damit nicht vor.
- Der Drift β wird null gesetzt, der Offset μ nicht, weil der Mittelwert selten null ist und ein konstanter Drift klein gegen die täglichen Schwankungen ist. Oft ist Lag 1 nötig, damit die Null verworfen werden kann.
- Der CADF-Test auf EWC gegen EWA verwirft die Unit Root des Spreads auf 95 Prozent: t-Statistik minus 3,64346635 gegen minus 3,359, AR(1)-Schätzung minus 0,020411.
- Im Vektorfall ist Λ gleich 0 der Zustand ohne Kointegration, analog zur univariaten Unit Root λ gleich 0.
- Ein ADF-Test auf dem Verhältnis Back zu Front von VX zeigt Stationarität mit 99 Prozent Wahrscheinlichkeit.
- Ein ADF-Test auf dem Crack Spread vom 20. Mai 2002 bis zum 4. Mai 2012 zeigt keine Mean Reversion.
- Ein ADF-Test auf CL gegen BZ im Verhältnis 1:1 zeigt, dass der Spread weit von stationär entfernt ist.

## Funktionsweise

- Der ADF-Test ist ein Unit-Root-Test: die Null ist λ gleich 0, und nur ein hinreichend negativer Wert von λ/SE(λ) verwirft sie.
- Die kritischen Werte hängen vom Stichprobenumfang ab und davon, ob ein von null verschiedener Mittelwert oder ein stetiger Drift angenommen wird.
- Im praktischen Handel wird der Driftterm β gleich 0 gesetzt, weil ein konstanter Drift meist klein gegen die täglichen Schwankungen ist.
- Der zweite adf-Parameter 0 bedeutet einen von null verschiedenen Offset und einen Drift von null, der dritte Parameter ist die Lag-Zahl.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Phillips, Wu und Yu (2011) sagen, Standard-Unit-Root-Tests können einen stationären Prozess und ein periodisch zusammenbrechendes Blasenmodell nicht wirksam unterscheiden.

## Beispiele

- Für USD.CAD mit einem Lag ist die ADF-t-Statistik minus 1,840744, die AR(1)-Schätzung 0,994120, und die kritischen Werte sind minus 3,458, minus 2,871 und minus 2,594; die Unit-Root-Null wird nicht verworfen.
- λ ist trotzdem negativ, die Reihe trendet also zumindest nicht.
- Im CADF-Test von EWC auf EWA ist die t-Statistik minus 3,64346635 und die AR(1)-Schätzung minus 0,020411; die Null λ gleich 0 wird auf 95 Prozent verworfen, der kritische Wert ist minus 3,359.
- Der augmentierte Dickey-Fuller-Test weist den VIX mit 99 Prozent Sicherheit als stationär aus.
- Der ADF-Test weist die back-adjustierten Front-Month-Kurse von VX als definitiv nicht mean-reverting aus.
- Der ADF-Test des 12-Monats-Log-Kalender-Spreads von CL findet Stationarität mit 99 Prozent Wahrscheinlichkeit und eine Halbwertszeit von 36 Tagen.
- Ein ADF-Test zeigt den VIX mit 99 Prozent Sicherheit als stationär. Derselbe Test zeigt, dass die back-adjustierten Frontmonatskurse von VX definitiv nicht mean-reverten.
- Der 12-Monats-Log-Kalenderspread von CL ist im ADF-Test mit 99 Prozent stationär, bei einer Halbwertszeit von etwa 36 Tagen.
- Die Halbwertszeit kommt aus der Regression der Änderung der Rollrendite auf ihren verzögerten Wert und ist minus log(2) geteilt durch den Steigungskoeffizienten.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 96–115 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-006-p096-p115|S. 96–115]]
- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 52–71 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-004-p052-p071|S. 52–71]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 119–138 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-009-p119-p138|S. 119–138]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 138–143 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-010-p138-p143|S. 138–143]]

## Verwandte Themen

- Alexander beschreibt diesen Test in Market Models auf den Seiten 324–328 und 353–361.
- Der Operator YY machte, im Unterschied zur Kointegrationsanalyse, keinen expliziten Test darauf, ob die Residuen stationär sind.
