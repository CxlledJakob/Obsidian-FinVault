---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/18 - Positionsmanagement/18 - Positionsmanagement|18 - Positionsmanagement]]"
weitere_hauptthemen: []
unterthema: "Portfolioführung"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Time Stop


## Kurzdefinition

- Der Time Stop ist die vertikale Barriere, also eine Ablaufgrenze nach einer Zahl von Bars oder Tagen seit der Positionsaufnahme.
- Der Time Stop ist eine maximale Haltedauer, nach der die Position unabhängig von Stop und Gewinnziel geschlossen wird.

## Kernaussagen

- h legt diese vertikale Barriere fest.
- Der Zeitpunkt der ersten Berührung liegt nicht nach ti,0 plus h.
- Wird die vertikale Barriere zuerst berührt, kann das Label das Vorzeichen der Rendite oder 0 sein.
- Der Autor bevorzugt das Vorzeichen der Rendite.
- Ein fehlender Zeitstempel für die vertikale Barriere schaltet sie ab.
- Wird für die vertikalen Barrieren False übergeben, sind sie abgeschaltet.
- Die Konfiguration nur mit vertikaler Barriere, [0,0,1], entspricht der Fixed-Time-Horizon-Methode.

## Funktionsweise

- Für jeden Ereigniszeitpunkt ist die vertikale Barriere der nächste Preis-Bar bei oder unmittelbar nach einer Anzahl von numDays Tagen.
- Liegt dieser Index hinter dem Ende der Schlusskurs-Serie, bleibt am Ende ein fehlender Wert.
- Die maximale Haltedauer begrenzt, wie lange eine Position offen bleiben kann.
- Am Ende der Frist wird geschlossen, auch wenn der Gewinn noch zwischen Stop und Gewinnziel liegt.
- Im Beispiel beträgt die Frist 100 Beobachtungen.
- Die maximale Haltedauer entspricht der vertikalen Barriere der Triple-Barrier-Methode.
- Geschlossen wird beim ersten Treffer von Gewinnziel, Stop oder Haltedauer.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- In der Konfiguration [1,1,1] begrenzen Gewinnziel, Stop und die maximale Haltedauer den Ausstieg gemeinsam.
- In der Konfiguration [0,1,1] endet die Position nach einer Anzahl Bars, sofern nicht vorher der Stop greift.
- In der Konfiguration [1,0,1] wird bis zu einem Gewinn oder bis zum Überschreiten der maximalen Haltedauer gehalten, ohne Rücksicht auf zwischenzeitliche Buchverluste.
- In der Konfiguration [1,1,0] ist die vertikale Barriere aus, Gewinn wird mitgenommen, solange kein Stop greift, und die Haltedauer ist nicht begrenzt.

## Risiken und Grenzen

- Die Regel könnte alle drei Barrieren verwenden und das Gitter dadurch auf 20 mal 20 mal 20 Knoten erweitern.
- Das Kapitel beschränkt das Gitter auf die beiden horizontalen Barrieren, damit die Darstellung anschaulich bleibt.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 58–77 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-004-p058-p077|S. 58–77]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]

## Verwandte Themen
