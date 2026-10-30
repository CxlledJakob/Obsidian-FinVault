---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Modelle"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Monte-Carlo-Simulation


## Kurzdefinition

- Die numerische Bestimmung der Handelsregel zieht sehr viele künstliche Gewinnpfade aus den geschätzten Prozessparametern.
- Die Monte-Carlo-Simulation vergleicht hier die Performance von Hierarchical Risk Parity, dem Minimum-Varianz-Portfolio des Critical Line Algorithm und dem Inverse-Varianz-Portfolio außer Stichprobe.
- Snippet 16.5 setzt Monte-Carlo-Experimente für Hierarchical Risk Parity, den Critical Line Algorithm und das Inverse-Varianz-Portfolio um.

## Kernaussagen

- Alle mittleren Portfoliorenditen außer Stichprobe liegen im Wesentlichen bei 0.
- Die Varianzen der Renditen außer Stichprobe betragen 0,1157 für CLA, 0,0928 für das Inverse-Varianz-Portfolio und 0,0671 für Hierarchical Risk Parity.
- CLA hat die höchste Varianz außer Stichprobe, 72,47 Prozent über Hierarchical Risk Parity, obwohl minimale Varianz sein Optimierungsziel ist.
- Diese höhere Out-of-Sample-Varianz von CLA entspricht der historischen Evidenz von De Miguel und Koautoren (2009).
- Hierarchical Risk Parity würde die Sharpe-Ratio einer CLA-Strategie außer Stichprobe um etwa 31,3 Prozent verbessern.
- Die Varianz des Inverse-Varianz-Portfolios liegt noch 38,24 Prozent über Hierarchical Risk Parity.
- Der mathematische Beweis dieser Überlegenheit liegt außerhalb des Kapitels.
- Andere Parameterkonfigurationen führen zu ähnlichen Schlüssen, und die Überlegenheit wird bei größerem Universum, mehr Schocks, stärkerer Korrelation oder Rebalancing-Kosten noch deutlicher.
- Chu, Stinchcombe und White leiten per Monte Carlo die Konstante b bei Alpha 0,05 gleich 4,6 ab, die in den kritischen Wert ihres einseitigen CUSUM-Tests auf Niveaus eingeht.

## Funktionsweise

- Im Beispiel werden 100000 Pfade erzeugt.
- Startwerte sind der beobachtete Einstiegspreis und die Prognose der jeweiligen Gelegenheit.
- Jeder Schritt setzt den Prozess mit einem unabhängigen standardnormalen Schock fort, skaliert mit Sigma.
- Dieselben Pfade werden auf jeden Knoten eines Gitters aus Stop und Gewinnziel gelegt.
- Jeder Gitterknoten liefert aus den auf ihm ausgewerteten Pfaden eine Sharpe Ratio.
- In den berichteten Simulationen wird Sigma auf 1 gesetzt.
- Der Einstiegspreis wird auf 0 gesetzt, weil allein die Distanz zur Prognose die Konvergenz treibt.
- Ein Pfad endet beim ersten Erreichen von Gewinnziel, Stop oder maximaler Haltedauer.
- Erzeugt werden zehn Reihen zufälliger Gauß-Renditen mit 520 Beobachtungen, Mittelwert 0 und einer willkürlichen Standardabweichung von 10 Prozent, entsprechend zwei Jahren Tagesdaten.
- Weil reale Preise häufig springen und Renditen nicht querschnittlich unabhängig sind, kommen zufällige Schocks und eine zufällige Korrelationsstruktur hinzu.
- Die Portfolios werden auf 260 Beobachtungen geschätzt, also ein Jahr, und alle 22 Beobachtungen neu geschätzt und rebalanciert, also monatlich.
- Der Ablauf wird 10.000-mal wiederholt.
- Die Datenerzeugung simuliert korrelierte Reihen mit zwei Schockarten, gemeinsam für mehrere Anlagen und spezifisch für eine Anlage.
- Von jeder Schockart gibt es einen positiven und einen negativen Schock.
- Die Argumente von hrpMC sind willkürlich gewählt: 10.000 Iterationen, 520 Beobachtungen, je fünf unkorrelierte und fünf korrelierte Reihen, Mittelwert 0, Sigma 0,01, sigma1F 0,25, Rückblick 260 und Rebalancing alle 22 Beobachtungen.
- Je Iterationsschritt werden die Portfolios auf dem Rückblickfenster geschätzt und die folgende Rebalancing-Strecke bewertet.
- Gespeichert wird die kumulierte Rendite am Pfadende minus eins, berichtet werden Standardabweichung, Varianz und die Varianz im Verhältnis zu Hierarchical Risk Parity.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Andere Eingabewerte würden andere Zahlen liefern, und die gewählten Kombinationen sollen die allgemeinen Fälle abdecken.
- Fehlt in der simulierten Performance ein stabiles Muster, existiert keine optimale Handelsregel.
- Die Varianzreduktion außer Stichprobe ist für Risk-Parity-Investoren wegen ihres erheblichen Hebels entscheidend.
- Ein einzelner historischer Datensatz, in dem Hierarchical Risk Parity gewinnt, wäre wegen Selection Bias zu leicht gewählt.

## Beispiele

- Untersucht werden die Prognosen 10, 5, 0, minus 5 und minus 10 zusammen mit den Halbwertszeiten 5, 10, 25, 50 und 100.
- Die maximale Haltedauer in diesen Simulationen beträgt 100 Beobachtungen.
- Ein idiosynkratischer Schock bestraft die Konzentration von CLA, ein Schock auf mehrere korrelierte Anlagen bestraft die ignorierte Korrelationsstruktur des Inverse-Varianz-Portfolios.
- Kolanovic und Koautoren (2017) bestätigen die Robustheit zusätzlich mit eigenen Simulationsstudien.
- Der gemeinsame Schock setzt an zwei Zeitpunkten die Werte minus 0,5 und 2 auf zwei Reihen, der spezifische Schock dieselben Werte auf eine Reihe.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 248–267 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-014-p248-p267|S. 248–267]]
- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]

## Verwandte Themen
