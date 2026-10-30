---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Statistik"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Erwartungswert


## Kurzdefinition

- Der erwartete Wert der zusammengesetzten Wachstumsrate als Funktion des Hebels f ist bei risikofreiem Zins null der Durchschnitt von log(1 plus f mal R).

## Kernaussagen

- Der Kalman-Filter ist optimal, weil er unter gaußschem Rauschen der beste Schätzer ist und den mittleren quadratischen Fehler der geschätzten Variablen minimiert.
- Der Erwartungswert der verborgenen Variable zur Zeit t ist eine lineare Funktion ihres Erwartungswerts vor der Beobachtung und des beobachteten Werts zur Zeit t.
- Die mathematische Optimalität der Kelly-Allokation über das Gesamtportfolio setzt voraus, dass die erwarteten Renditen und die Volatilitäten der Strategien unverändert bleiben.
- Nach einem jüngeren schweren Drawdown ist zweifelhaft, ob diese Erwartungen noch unverändert sind.

## Funktionsweise

- Die erwartete Lösung des Ornstein-Uhlenbeck-Prozesses ist E(y(t)) gleich y0 mal exp(λt) minus (μ/λ) mal (1 minus exp(λt)).
- Ist λ für einen mean-reverting Prozess negativ, fällt der erwartete Preis exponentiell auf den Wert minus μ/λ.
- Die Halbwertszeit dieses Abfalls ist minus log(2) geteilt durch λ.
- Werden immer zwei Kontrakte gehalten und erst bei F vollständig geschlossen, ist der erwartete Gewinn von all-in bei L1 gleich 2 mal (F minus L1).
- Der erwartete Gewinn von all-in bei L2 ist 2 mal p mal (F minus L2), weil nur mit Wahrscheinlichkeit p investiert wird.
- Der erwartete Gewinn von average-in ist (F minus L1) plus p mal (F minus L2).
- Die Schwelle ist p-Dach gleich (F minus L1) geteilt durch (F minus L2): darunter ist all-in bei L1 besser als all-in bei L2 und besser als average-in, darüber ist all-in bei L2 besser als die beiden anderen.
- Bei p gleich 0 ist all-in bei L1 am profitabelsten, bei p gleich 1 ist all-in bei L2 am profitabelsten, und average-in ist in keinem Fall das profitabelste Verfahren, solange p konstant ist.
- Market Maker aktualisieren mit diesem Modell ihre Schätzung des mittleren Preises eines Assets.
- Ist die Trade-Größe T gleich der Benchmark Tmax, ist der Kalman-Gain 1, und die neue Schätzung des mittleren Preises m(t) ist genau der beobachtete Preis.
- Gemittelt wird über eine Zufallsstichprobe der ungehebelten Rendite pro Bar R(t) der Strategie, nicht der Marktpreise, aus einer Wahrscheinlichkeitsverteilung von R.
- Üblich sind Tagesbars; der Bar kann aber beliebig lang oder kurz sein.
- Ist R gaußisch, lässt sich g(f) analytisch reduzieren, und die Ableitung nach f gleich null reproduziert die Kelly-Formel sowie im Ein-Strategie-Fall die maximale Wachstumsrate.
- Ohne Gauß-Annahme wird dieser Erwartungswert mit einer nichtgaußischen Verteilung per Monte Carlo berechnet.
- Die wahre Verteilung von R ist unbekannt; das Pearson-System modelliert sie aus Mittelwert, Standardabweichung, Schiefe und Kurtosis.
- Im Beispiel dienen 100.000 Zufallsrenditen aus diesem System dazu, den Durchschnitt von g(f) zu berechnen.

## Voraussetzungen


## Anwendung im Trading

- Der erwartete Preis eines Instruments lässt sich anhand des letzten Trades, also Preis und Größe, mit dem Kalman-Filter dynamisch aktualisieren.

## Regeln und Kriterien

- Ist λ positiv, ist die Reihe überhaupt nicht mean-reverting, und eine Mean-Reversion-Strategie soll nicht angesetzt werden.
- Liegt λ sehr nahe bei null, wird die Halbwertszeit sehr lang, und die Strategie ist wenig profitabel, weil in der gegebenen Zeit wenige Round-Trips abgeschlossen werden.

## Risiken und Grenzen

- Die Rangfolge der erwarteten Gewinne gilt nur, wenn p über die Zeit konstant ist; ist die Volatilität nicht konstant, ist auch p nicht konstant, und Scaling-in kann außer Stichprobe besser abschneiden.

## Beispiele


## Unterschiedliche Quellenpositionen

- Die Optimierung dieses Erwartungswerts über eine analytische Verteilung wird der Optimierung der einen historischen Wachstumsrate gegenübergestellt.
- Für Manager eigenen Geldes ist das alleinige Ziel die Maximierung des langfristigen Nettovermögens; Drawdowns und Volatilitäten sind ihnen gleichgültig.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 20–39 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-002-p020-p039|S. 20–39]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 77–96 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-005-p077-p096|S. 77–96]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 96–115 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-006-p096-p115|S. 96–115]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 115–134 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-007-p115-p134|S. 115–134]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 134–153 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-008-p134-p153|S. 134–153]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 153–172 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-009-p153-p172|S. 153–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 172–191 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-010-p172-p191|S. 172–191]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 191–210 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-011-p191-p210|S. 191–210]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 210–229 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-012-p210-p229|S. 210–229]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 229–248 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-013-p229-p248|S. 229–248]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 248–267 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-014-p248-p267|S. 248–267]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 267–286 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-015-p267-p286|S. 267–286]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 286–305 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-016-p286-p305|S. 286–305]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 305–324 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-017-p305-p324|S. 305–324]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 324–343 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-018-p324-p343|S. 324–343]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 381–400 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-021-p381-p400|S. 381–400]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 419–438 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-023-p419-p438|S. 419–438]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 457–476 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-025-p457-p476|S. 457–476]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 476–495 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-026-p476-p495|S. 476–495]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 495–514 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-027-p495-p514|S. 495–514]]

## Verwandte Themen
