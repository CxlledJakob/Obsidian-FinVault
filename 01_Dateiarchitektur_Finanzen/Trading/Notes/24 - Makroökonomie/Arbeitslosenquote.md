---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/24 - Makroökonomie/24 - Makroökonomie|24 - Makroökonomie]]"
weitere_hauptthemen: []
unterthema: "Wachstum und Inflation"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Arbeitslosenquote


## Kurzdefinition

- Die saisonbereinigte vierteljährliche zivile US-Arbeitslosenquote von 1948 bis 1993 bewegt sich gegenzyklisch zum US-Konjunkturzyklus, steigt schnell und fällt langsam; Letzteres spricht für eine nichtlineare Dynamik.

## Kernaussagen

- Die saisonbereinigte monatliche zivile Arbeitslosenquote der USA, in Prozent, läuft von Januar 1948 bis März 2009 und umfasst 735 Beobachtungen des Bureau of Labor Statistics.
- Die Reihe zeigt einen langsamen Aufwärtstrend, steigt schnell und fällt langsam. Sie ist nicht zeitumkehrbar und möglicherweise nicht einheitswurzelstationär.
- Weil die Stichprobenautokorrelation langsam fällt, wird die erste Differenz y_t = (1−B) u_t untersucht.
- Das ARIMA der Differenz lautet (1 − 1,13B + 0,27B²)(1 − 0,51B¹²) y_t = (1 − 1,12B + 0,44B²)(1 − 0,82B¹²) a_t mit σ̂_a = 0,187. Alle Schätzungen außer dem AR(2)-Koeffizienten sind auf dem 5-Prozent-Niveau signifikant, dessen t-Ratio −1,66 ist.
- Die Residuen ergeben Q(12) = 12,3 (p = 0,056) und Q(24) = 25,5 (p = 0,11) bei 6 und 18 Freiheitsgraden. Das Modell beschreibt die serielle Abhängigkeit angemessen.
- Die saisonalen AR- und MA-Koeffizienten bleiben hoch signifikant, Standardfehler 0,049 und 0,035, obwohl die Daten saisonbereinigt wurden. Die Güte der Saisonbereinigung verdient weitere Prüfung.
- Die Einschrittprognose für April 2009 beträgt 8,8 und liegt nahe am tatsächlichen Wert 8,9.
- Das TAR auf y_t hat die Schwelle 0,1. Für y_{t−1} ≤ 0,1 gilt y_t = 0,083 y_{t−2} + 0,158 y_{t−3} + 0,118 y_{t−4} − 0,180 y_{t−12} + a_{1t}. Für y_{t−1} > 0,1 gilt y_t = 0,421 y_{t−2} + 0,239 y_{t−3} − 0,127 y_{t−12} + a_{2t}.
- Die Standardabweichungen der Regimeinnovationen sind 0,180 und 0,217. In Regime 1 liegen 460, in Regime 2 liegen 262 Beobachtungen. Die standardisierten Residuen zeigen nur eine geringe serielle Korrelation bei Lag 12.
- Die dynamische Abhängigkeit ist stärker, wenn die Änderung der monatlichen Arbeitslosenquote größer als 0,1 Prozent ist. Ein deutlicher Anstieg zeigt eine Schwächung der US-Wirtschaft an, und die Politik könnte eher eingreifen, was die Dynamik der Reihe verändern kann.
- Die MA-Darstellung des ARIMA ist näherungsweise 1 + 0,01B + 0,18B² + 0,20B³ + 0,18B⁴ + 0,15B⁵ + ⋯. Deshalb fehlt im TAR der Term y_{t−1}.
- Δx_t = x_t − x_{t−1} ist die Änderung der Quote; das lineare Benchmark von Montgomery et al. (1998) ist (1 − 0,31 B⁴)(1 − 0,65 B) Δx_t = (1 − 0,78 B⁴) a_t mit σ̂²_a = 0,090 und Standardfehlern 0,11, 0,06 und 0,07.
- Das Benchmark bleibt ein saisonales Modell, obwohl die Daten saisonbereinigt sind; das verwendete Saisonbereinigungsverfahren hat die Saisonalität nicht erfolgreich entfernt.
- Nichtlinearitätstests auf einem AR(5) für Δx_t verwerfen die Linearität; sie wird für jedes angewandte AR(p) mit p von 2 bis 10 verworfen.
- In Tabelle 4.3, Stichprobe 1948.II bis 1993.IV, betragen Ori-F 2,80 (p = 0,0007), LST 2,83 (p = 0,0002), TAR(1) 2,41 (p = 0,0298), TAR(2) 2,16 (p = 0,0500), TAR(3) 2,84 (p = 0,0121) und TAR(4) 2,98 (p = 0,0088).
- Das TAR-Modell lautet 0,01 + 0,73 Δx_{t−1} + 0,10 Δx_{t−2} + a_{1t}, wenn Δx_{t−2} ≤ 0,1, und sonst 0,18 + 0,80 Δx_{t−1} − 0,56 Δx_{t−2} + a_{2t}; die Stichprobenvarianzen von a_{1t} und a_{2t} sind 0,76 und 0,165.
- Die Standardfehler der drei Koeffizienten sind im ersten Regime 0,03, 0,10 und 0,12 und im zweiten 0,09, 0,1 und 0,16.
- Im ersten Regime, Rückgang oder nur geringer Anstieg der Quote, ist der Lag-2-Koeffizient insignifikant, sodass die Änderung im Wesentlichen einem AR(1) folgt und die Wirtschaft als stabil gilt.
- Im zweiten Regime bedeutet ein Sprung von 0,1 oder mehr typischerweise die Kontraktionsphase; Δx_t folgt einem AR(2) mit positiver Konstante, und das AR(2)-Polynom hat zwei komplexe charakteristische Wurzeln.
- Die komplexen Wurzeln erhöhen die Chance eines Wendepunkts, sodass Phasen großer Anstiege kurz bleiben; Kontraktionsphasen der US-Wirtschaft sind damit tendenziell kürzer als Expansionsphasen.
- Das per Markov-Chain-Monte-Carlo geschätzte Markov-Switching-Modell lautet −0,07 + 0,38 Δx_{t−1} − 0,05 Δx_{t−2} + ε_{1t} für s_t = 1 und 0,16 + 0,86 Δx_{t−1} − 0,38 Δx_{t−2} + ε_{2t} für s_t = 2.
- Die bedingten Mittel von Δx_t sind −0,10 in Zustand 1 und 0,31 in Zustand 2; die Stichprobenvarianzen von ε_{1t} und ε_{2t} sind 0,031 und 0,192.
- Die Standardfehler der drei Parameter sind in Zustand 1 gleich 0,03, 0,14 und 0,11 und in Zustand 2 gleich 0,04, 0,13 und 0,14.
- Die Übergangswahrscheinlichkeiten sind P(s_t = 2 | s_{t−1} = 1) = 0,084 mit Standardfehler 0,060 und P(s_t = 1 | s_{t−1} = 2) = 0,126 mit Standardfehler 0,053.
- Zustand 1 steht für Expansionen mit leicht fallendem Trend und schwächerer Autoregression; Zustand 2 steht für Kontraktionen mit Aufwärtstrend und einem AR(2)-Polynom mit komplexen Wurzeln, analog zum zweiten TAR-Regime.
- Die rollierende Prognose startet bei T = 83, also 1968.II, schätzt lineares, TAR- und MSA-Modell jeweils bis zum Ursprung einschließlich, prognostiziert 1 bis 5 Quartale mit parametrischem Bootstrap für die nichtlinearen Modelle und rückt den Ursprung um ein Quartal vor.
- Für Prognoseursprünge in wirtschaftlichen Kontraktionen verbessert das TAR-Modell das lineare Modell der US-Arbeitslosenquote sowohl beim MSE als auch bei der Verzerrung.
- Das Markov-Switching-Modell verbessert das lineare Modell in Kontraktionen ebenfalls, aber weniger stark als das TAR.
- Für Prognoseursprünge in wirtschaftlichen Expansionen schlägt das lineare Modell beide nichtlinearen Modelle.
- Der Beitrag der nichtlinearen Modelle gegenüber dem linearen liegt damit vor allem in den Kontraktionsphasen.
- In Kontraktionen sind staatliche Eingriffe und industrielle Umstrukturierung am wahrscheinlichsten; diese äußeren Ereignisse können Nichtlinearität in die US-Arbeitslosenquote bringen.
- Gerade diese Verbesserung wiegt schwer, weil Prognosen in Kontraktionen mehr Aufmerksamkeit bekommen.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele

- Im Gesamtvergleich beträgt der relative MSE des TAR für 1 bis 5 Schritte 1,00, 1,04, 0,99, 0,98 und 1,03, der des MSA 1,19, 1,39, 1,40, 1,45 und 1,61; der MSE des linearen Benchmarks ist 0,08, 0,31, 0,67, 1,13 und 1,54.
- Die mittleren Prognosefehler im Gesamtvergleich sind für das lineare Modell 0,03, 0,09, 0,17, 0,25 und 0,33, für TAR −0,10, −0,02, −0,03, −0,03 und −0,01 und für MSA 0,00, −0,02, −0,04, −0,07 und −0,12.
- Damit liegen TAR und lineares Modell im MSE nahe beieinander, TAR hat die kleineren Verzerrungen, und MSA hat den höchsten MSE bei den kleinsten Verzerrungen.
- In Kontraktionen beträgt der relative MSE des TAR für 1 bis 5 Quartale 0,85, 0,91, 0,83, 0,72 und 0,72, der des MSA 0,97, 1,03, 0,96, 0,86 und 1,02; der MSE des linearen Benchmarks ist 0,22, 0,97, 2,14, 3,38 und 3,46.
- In Expansionen beträgt der relative MSE des TAR 1,06, 1,13, 1,10, 1,15 und 1,17 und der des MSA 1,31, 1,64, 1,73, 1,84 und 1,87; der lineare MSE ist 0,06, 0,21, 0,45, 0,78 und 1,24.
- Die mittleren Prognosefehler in Kontraktionen lauten für das lineare Modell 0,31, 0,68, 1,08, 1,41 und 1,38, für TAR 0,24, 0,56, 0,87, 1,01 und 0,86 und für MSA 0,20, 0,41, 0,57, 0,52 und 0,14.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 191–210 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-011-p191-p210|S. 191–210]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 229–248 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-013-p229-p248|S. 229–248]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 248–267 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-014-p248-p267|S. 248–267]]

## Verwandte Themen
