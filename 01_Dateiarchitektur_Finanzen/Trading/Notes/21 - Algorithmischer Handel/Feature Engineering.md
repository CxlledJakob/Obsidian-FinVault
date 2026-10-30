---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Strategien und Ausführung"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Feature Engineering


## Kurzdefinition

- Feature Analysts verwandeln Rohdaten in informative Signale mit Vorhersagekraft für Finanzvariablen.
- Indikatorentwurf ist die Festlegung der Transformationen, die auf Rohmarktdaten angewendet werden, bevor sie dem Data-Mining-Werkzeug vorgelegt werden. Data Miner nennen das Preprocessing.

## Kernaussagen

- Ein solcher Befund ist für sich genommen keine Anlagestrategie.
- Dieselben Signale lassen sich für die Ausführung, die Überwachung des Liquiditätsrisikos, Market Making oder das Eingehen von Positionen verwenden.
- Die Annahme, Feature Analysts entwickelten die Strategien, ist ein verbreiteter Fehler.
- Feature Analysts sammeln und katalogisieren Bibliotheken von Befunden, die mehreren Stationen nützen.
- Der Forschungsprozess soll Features identifizieren, die über Assetklassen hinweg relevant sind, und die Multikollinearität finanzieller Features behandeln.
- Eine notwendige Bedingung für Erfolg im Data Mining ist ein guter Satz von Kandidatenindikatoren. Nicht jede Eingabe muss informativ sein, aber einige der vorgeschlagenen Variablen müssen nützliche Information über die Zielvariable enthalten.
- Die größten Leistungsgewinne entstehen oft dadurch, prädiktivere Features zu beschreiben. Der Mensch legt die Menge der Features fest und untersucht, wie ursprüngliche Features in bessere verwandelt werden.
- Der Rechner ist klug beim Löschen schwacher Features und vergleichsweise dumm bei der anspruchsvolleren Aufgabe, neue Features zu bilden oder Rohdaten in prädiktivere Formen zu transformieren.
- Die Zusammensetzung der Features bestimmt die Qualität der Ergebnisse stärker als das konkrete Prognoseverfahren, das diese Ergebnisse erzeugt.
- In den meisten Fällen hängt die Bildung von Features vom Wissen über die Anwendung ab.
- Nach Dorian Pyle ist die Datenaufbereitung, nachdem das richtige Problem gefunden wurde, oft der Schlüssel und kann den Unterschied zwischen brauchbaren Prognosen und nutzlosen Vermutungen ausmachen.
- Nach Timothy Masters ist Preprocessing der Schlüssel zum Erfolg: Selbst ein primitives Prognosemodell kann gut arbeiten, wenn die Variablen so vorverarbeitet wurden, dass die wichtige Information klar hervortritt.

## Funktionsweise

- Die richtige Rolle des technischen Analysten ist zweifach: einen informationsreichen Satz von Kandidateneingaben für die Data-Mining-Software vorzuschlagen und die Zielvariable, also das zu lösende Problem, festzulegen.
- Verschiedene Algorithmen haben verschiedene Anforderungen. Eingaben eines neuronalen Netzes müssen richtig skaliert sein, Eingaben von Entscheidungsbaum-Algorithmen nicht.

## Voraussetzungen

- Gebraucht werden Informationstheorie, Signalgewinnung und Signalverarbeitung, Visualisierung, Labeling, Gewichtung, Klassifikatoren und Verfahren der Feature Importance.

## Anwendung im Trading

- Strategen durchsuchen die Bibliotheken der Features nach Ideen für eine Anlagestrategie.
- Der Wettbewerbsvorteil liegt inzwischen bei den Analysten mit den besten Einsichten zum Vorschlagen von Indikatoren und zum Festlegen von Zielvariablen, weil Rechenleistung und Data-Mining-Software zur allgemein zugänglichen Ware geworden sind.

## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Die Wahrscheinlichkeit eines Ausverkaufs ist besonders hoch, wenn quotierte Angebote durch Market-Sell-Orders ersetzt werden und quotierte Kaufaufträge durch tiefer im Buch liegende Limit-Kauforders ersetzt werden.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 20–39 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-002-p020-p039|S. 20–39]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 457–476 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-025-p457-p476|S. 457–476]]

## Verwandte Themen

- Teil 4 kehrt zu den Daten zurück und beschreibt Wege, informative Features zu extrahieren, darunter Strukturbrüche, Entropie und Mikrostruktur.
