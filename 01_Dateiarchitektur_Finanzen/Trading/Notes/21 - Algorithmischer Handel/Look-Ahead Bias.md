---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Validierung"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Look-Ahead Bias


## Kurzdefinition

- Look-ahead Bias heißt, Information zu nutzen, die im Zeitpunkt der simulierten Entscheidung nicht öffentlich war.

## Kernaussagen

- Fundamentaldaten werden mit Zeitverzug berichtet.
- Die Analyse darf einen Datenpunkt erst verwenden, nachdem er öffentlich verfügbar war.
- Die Annahme, diese Daten seien am Ende der Berichtsperiode veröffentlicht worden, ist ein Anfängerfehler und trifft nie zu.
- Bloomberg indiziert Fundamentaldaten mit dem letzten Datum im Bericht und weist die Werte damit einem Zeitpunkt zu, an dem sie noch nicht bekannt waren.
- Backfilling weist fehlenden Daten einen Wert zu, auch wenn dieser damals unbekannt war.
- Ein nachträglich berichtigter Wert war am Tag der ersten Veröffentlichung nicht bekannt.
- Häufig wird der endgültige Wert auf den Zeitpunkt der ersten Veröffentlichung oder sogar auf den letzten Tag der Berichtsperiode gelegt.
- Nach korrekter zeitlicher Zuordnung lässt sich ein erheblicher Teil der Befunde in der Faktorliteratur nicht mehr reproduzieren.
- Informationsleckage in der Kreuzvalidierung ist eine Falle, und die genannte Lösung sind Purging und Embargoing in den Kapiteln 7 und 9.
- Dieser Zuordnungsfehler und seine Folgen werden bei den Backtesting-Fehlern in Kapitel 11 wieder behandelt.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Für jeden Datenpunkt ist der Zeitstempel sicher zu bestimmen, und Veröffentlichungsdaten, Verteilungsverzögerungen sowie Backfill-Korrekturen sind zu berücksichtigen.

## Risiken und Grenzen

- Look-ahead Bias ist die zweite der sieben Sünden des quantitativen Investierens bei Luo et al. 2014, und die meisten in Zeitschriften veröffentlichten Arbeiten begehen solche Grundfehler routinemäßig.

## Beispiele

- Bei Bloomberg liegt das letzte im Bericht enthaltene Datum oft etwa 1,5 Monate vor dem Veröffentlichungstag.
- Für eine vierteljährliche BIP-Meldung liegen typischerweise drei Werte vor: der ursprünglich veröffentlichte Wert und zwei monatliche Revisionen.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 39–58 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-003-p039-p058|S. 39–58]]
- Advances in Financial Machine Learning.pdf, S. 115–134 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-007-p115-p134|S. 115–134]]
- Advances in Financial Machine Learning.pdf, S. 134–153 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-008-p134-p153|S. 134–153]]
- Advances in Financial Machine Learning.pdf, S. 172–191 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-010-p172-p191|S. 172–191]]

## Verwandte Themen
