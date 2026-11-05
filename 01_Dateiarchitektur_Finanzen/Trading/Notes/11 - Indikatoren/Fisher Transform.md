---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/11 - Indikatoren/11 - Indikatoren|11 - Indikatoren]]"
weitere_hauptthemen: []
unterthema: "Oszillatoren"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Fisher Transform


## Kurzdefinition

- Zweck der Fisher-Transformation ist, einen Indikator mit nominalem Nullmittelwert, begrenzt auf −1 bis +1, in der Amplitude so umzurechnen, dass der transformierte Indikator annähernd normalverteilt ist.
- Eine Indikatortransformation formt den Indikator, um seine Interpretation und Nutzung zu erleichtern. Außer der Darstellung hat sie keinen Einfluss auf den Indikator und erzeugt keinen Lag.
- Ehlers nennt drei für Trader interessante Transformationen: die Fisher-Transformation, die inverse Fisher-Transformation und die Kubik-Transformation.

## Kernaussagen


## Funktionsweise

- Ehlers diskutiert die Fisher-Transformation für Indikatoren, die Extreme messen sollen.
- Die Häufigkeitsverteilung eines Indikators auf Basis der Kanalnormierung hat eine unerwünschte Eigenschaft: Extremwerte sind erheblich wahrscheinlicher als Werte in der Mitte der Spanne des Indikators.
- Das ist kaum das Verhalten, das man von einem Indikator will, der seltene Extreme erkennen soll.
- Wendet man die Fisher-Transformation auf kanalnormierte Daten an, liegt der resultierende Indikator nach Ehlers nahe an der Normalverteilung.
- Ein normalverteilter Indikator hat die erwünschte Eigenschaft, dass seine Extremwerte selten sind, und das kann sie informativer machen.
- Die Gleichung lautet Output = 0,5 · ln[(1 + Input) / (1 − Input)].
- Weil ein Input von 1 das Verhältnis gegen unendlich gehen lässt, wird der Input auf 0,999 begrenzt, was einem Output von etwa drei Standardabweichungen entspricht. Da das Argument des Logarithmus nicht null werden darf, wird der Input auch bei −0,999 begrenzt.
- Bei Inputs mit Betrag unter 0,5 ist der Output fast gleich dem Input. Je näher der Input dem Betrag 1 kommt, desto stärker wird der Output vergrößert; diese nichtlineare Vergrößerung erzeugt die langen Enden und damit die Normalverteilung.

## Voraussetzungen

- Ein verbreiteter Irrtum ist, dass technische Indikatoren normalverteilt seien; das lässt sich an ausreichend Daten widerlegen. Sind die Daten nicht normalverteilt, beruht die Berechnung einer Standardabweichung auf einer falschen Prämisse.
- Stochastic und CCI sind keine guten Kandidaten, weil sie kurzfristig keinen Nullmittelwert haben.

## Anwendung im Trading

- Hat der transformierte Indikator den Wert −1, liegt er eine Standardabweichung im Minus und es besteht eine Chance von 32 Prozent auf tiefere Preise. Bei −2 sind es nur 8 Prozent, eine Kaufgelegenheit mit hoher Wahrscheinlichkeit; bei −3 nur 2 Prozent.
- Die transformierten Werte sind symmetrisch: Positive Abweichungen sind Signale hoher Wahrscheinlichkeit, eine Long-Position zu schließen oder short zu gehen.
- Für den adaptiven RSI wird MyRSI (0 bis 1) mit 2 · (MyRSI − 0,5) auf −1 bis +1 verschoben, mit 1,5 verstärkt, auf ±0,999 begrenzt und dann transformiert; im Display stehen Linien bei +2 und −2.
- Schöpft MyRSI den Bereich 0 bis 1 nicht voll aus, kann der RSI-Lookback auf weniger als die Hälfte des gemessenen dominanten Zyklus verkürzt oder ein Verstärkungsfaktor eingesetzt werden. Der Faktor wurde so gewählt, dass der Indikator die Zwei-Sigma-Punkte selten überschreitet.
- Im Beispiel kündigt ein Fall des fisherisierten adaptiven RSI unter −2 den Aufwärtstrend an, ein Anstieg über +2 den Abwärtstrend. Diese großen Wendepunkte sind relativ seltene Ereignisse und am besten zusammen mit Trendhandel zu nutzen.

## Regeln und Kriterien


## Risiken und Grenzen

- Ehlers legt keine Daten vor, die die Wirksamkeit der Fisher-Transformation stützen.
- Zum Zeitpunkt des Textes ist der Nutzen der Fisher-Transformation nur eine interessante Vermutung, die weitere Untersuchung verdient.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]
- Cycle Analytics for Traders (Advanced Technical Trading -- Ehlers, John F_ -- 10_1002_9781118728611, 2013 nov 18 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118728611 -- 1af2315757f5680b2f83029a006fd7ab -- Anna’s .pdf, S. 197–216 → [[Trading/Pilot/blocks/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f/cycle-analytics-for-traders-advanced-technical-trading-ehlers-john-f-block-015-p197-p216|S. 197–216]]

## Verwandte Themen

- Die inverse Fisher-Transformation komprimiert den Indikator nahe den Extremen statt ihn zu dehnen, entfernt so viele überflüssige Zacken und wirkt als weicher Begrenzer. Ihre Gleichung ist Output = (e^(2·K·Input) − 1) / (e^(2·K·Input) + 1), K ist ein optionaler Verstärkungsterm.
- Beim inversen Fisher des adaptiven Stochastic (Verstärkung 3) ist die Triggerlinie der um einen Bar verzögerte, auf 90 Prozent gedämpfte Wert. Kreuzt die inverse Fisher-Linie über die Triggerlinie, wird gekauft; kreuzt sie darunter, wird short gegangen oder die Long-Position geschlossen.
- Einzige Bedingung der inversen Fisher-Transformation ist ein Input mit nahezu Nullmittelwert; eventuell muss er verstärkt werden, für einen digitalen Output stark.
- Die Kubik-Transformation komprimiert Werte nahe null bei einem Indikator zwischen −1 und +1, etwa beim adaptiven Bandpassfilter. Sie wirkt nur bei nominalem Nullmittelwert und wenn die spektrale Dilatation durch einen Roofing-Filter entfernt wurde.
