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

## Verwandte Themen
