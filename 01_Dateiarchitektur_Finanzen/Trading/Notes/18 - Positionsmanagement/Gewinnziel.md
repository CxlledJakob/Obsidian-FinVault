---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/18 - Positionsmanagement/18 - Positionsmanagement|18 - Positionsmanagement]]"
weitere_hauptthemen: []
unterthema: "Trade Management"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Gewinnziel


## Kurzdefinition

- Das Gewinnziel ist die obere horizontale Barriere der Gewinnmitnahme in der Triple-Barrier-Methode.
- Das Gewinnziel ist die positive Schwelle, bei deren Erreichen die offene Gelegenheit geschlossen wird.
- Das Gewinnziel ist die positive Auszahlung einer Wette, die mit der Trefferwahrscheinlichkeit eintritt.

## Kernaussagen

- Nach dem Bruch werden die verlassenen Stauzonen zu einfachen Zielen für das Führen und Schließen von Positionen.
- Sie sind eine sichtbare Karte der Stellen, an denen der Markt kämpfen, drehen oder Unterstützung finden kann.
- Unterstützung und Widerstand dienen damit als Ziel für den Ausstieg, nicht nur als Einstiegssignal.
- Gewinnmitnahme und Stop-Loss sollen eine Funktion des Risikos der Wette sein.
- Liegt die feste Schwelle weit über der herrschenden Volatilität, ist das Ziel zu hoch, liegt sie weit darunter, ist es zu niedrig.
- Die Breite der oberen Barriere ist der Faktor ptSl[0] mal dem Ziel trgt.
- Ist dieser Faktor 0, gibt es keine obere Barriere.
- Wird die obere Barriere zuerst berührt, erhält die Beobachtung das Label 1.
- Dieselbe Schwelle unabhängig von der beobachteten Volatilität ist ein Grund, die Fixed-Time-Horizon-Methode in den meisten Fällen zu meiden.
- Eine Ersatzschwelle ist ein variables Sigma, geschätzt als rollierende exponentiell gewichtete Standardabweichung der Renditen.
- Volumen- oder Dollar-Bars halten die Volatilität näher an der Konstanz.
- Ohne bekannte Marktseite müssen die horizontalen Barrieren symmetrisch sein oder entfallen, weil Gewinnziel und Stop nicht unterscheidbar sind.
- Gewinnziel und Stop entsprechen den horizontalen Barrieren des Meta-Labeling.
- Bei einer Prognose von null und einer Halbwertszeit von 5 liegt das Leistungsmaximum bei kleinen Gewinnzielen und weiten Stops.
- Die optimale Regel hält das Inventar dann, bis ein kleiner Gewinn entsteht, auch wenn zwischenzeitlich das Fünf- oder Siebenfache als nicht realisierter Verlust ansteht.
- Bei Prognose null und kurzer Halbwertszeit verbindet die schlechteste Regel einen engen Stop mit einem hohen Gewinnziel.
- Auf der Diagonalen, auf der Gewinnziel und Stop symmetrisch sind, liegt die Performance am nächsten bei null.
- Bei Prognose 5 und Halbwertszeit 5 ist das optimale Gewinnziel um 6 zentriert, bei Stops zwischen 4 und 10, und das Gebiet hat eine rechteckige Form.
- Bei Prognose 5 und Halbwertszeit 10 liegt das optimale Gewinnziel um 5, und die guten Stops liegen zwischen 7 und 10.
- Bei Prognose 5 und Halbwertszeit 25 liegt das optimale Gewinnziel um 3, und die guten Stops liegen zwischen 9 und 10.
- Steigt die Halbwertszeit weiter, spreizt sich das Gebiet der besten Performance.
- Bei positiver Prognose gibt es anders als bei Prognose null kein symmetrisches Gebiet der schlechtesten Performance.
- Dasselbe qualitative Muster erscheint bei einer Prognose von 10, wenn die Halbwertszeit von 5 bis 100 steigt.
- Liefert die Strategie ein Gewinnziel, lässt sich der dazu passende Stop aus den Simulationen bestimmen.
- Gibt das Fondsmanagement einen maximalen Stop vor, lässt sich das dazu passende Gewinnziel bestimmen.
- Bei negativer Prognose ist die Heatmap das gedrehte Gegenbild der positiven Prognose, und Gewinne des einen Falls werden zu Verlusten des anderen.
- Der Fall mit negativer Prognose ist das umgekehrte Bild des Falls mit positiver Prognose, so wie der Verlust des Spielers der Gewinn des Hauses ist.
- Bei Prognose minus 5 und Halbwertszeit 5 liegt das schlechteste Gebiet um einen Stop von 6 und bei Gewinnzielen zwischen 4 und 10.
- Bei Prognose minus 5 und Halbwertszeit 10 spreizt sich das Gebiet der schlechtesten Performance, aus dem Rechteck wird ein Quadrat, und die Performance wird weniger negativ.
- Bei Prognose 5 und Halbwertszeit 50 spreizt sich das Gebiet guter Performance.
- Für einen Preis aus einem diskreten Ornstein-Uhlenbeck-Prozess gibt es nach der Vermutung genau eine Kombination aus Gewinnziel und Stop, die die Sharpe Ratio maximiert.
- Die für eine Ziel-Sharpe-Ratio nötige Trefferwahrscheinlichkeit hängt vom Gewinnziel, von der Verlustschwelle und von der Wettfrequenz ab.
- Für die Darstellung der nötigen Trefferwahrscheinlichkeit wird ein Gewinnziel von 0,1 zusammen mit einer Ziel-Sharpe-Ratio von 1,5 verwendet.
- Das Aufwärtspotenzial einer Mean-Reversion-Strategie ist durch die natürliche Gewinnobergrenze begrenzt, gesetzt als das Mittel, zu dem die Preise zurückkehren.
- Das Aufwärtspotenzial einer Momentum-Strategie ist unbegrenzt, außer es wird willkürlich eine Gewinnobergrenze gesetzt, was unratsam ist.
- Feste Ausstiegsziele beseitigen extreme Ergebnisse und verringern damit die Schwere der Ränder in der Stichprobenverteilung der Performancestatistik.
- Nur wenn Regeln an festen Zielen aussteigen, ist der Befund praktisch nützlich, dass eine leichtschwänzige Renditeverteilung den Data-Mining-Bias deutlich mindert; in den meisten Fällen bleiben Forscher an die vom Marktverhalten erzeugten Renditeverteilungen gebunden.
- Geld entsteht erst im geschlossenen Trade. Der bestmögliche Einstieg allein bringt keinen Dollar.
- Nie an einem vorher festgelegten Kursziel aussteigen. Der Markt läuft oft durch ein Ziel, manchmal erheblich. Ein Ausstieg am Ziel kann den weiteren Trend verpassen.
- Kursziele oder andere Bedingungen können ein Grund sein, den Schutzstop näher an den Markt zu ziehen, aber nie ein Grund, zu einem bestimmten Preis auszusteigen.
- Was man zurückgibt, weil der Markt vor dem Ausstieg ein kleines Stück gegen die Position läuft, soll durch die Fälle mehr als ausgeglichen werden, in denen er durch ein Kursziel trendet.
- Die mögliche Belohnung ist nie bekannt, sondern eine beste Schätzung eines Mindestkursziels, gewöhnlich optimistisch, um den Trade zu rechtfertigen.
- Es gibt keine feste Formel für Preisziele oder für die Momentum-Lage, die das Mitdenken beim laufenden Trade ersetzen würde. Manche Lehrer behaupten, das Geheimnis gefunden zu haben. Der Text sagt, sie haben es nicht.
- Preisziele werden nicht immer erreicht. Die Entscheidung folgt der wahrscheinlichen Lage bis zum letzten Bar.
- Einen kleinen Gewinn zu früh sichern, wenn ein großer Gewinn wahrscheinlich ist, widerspricht dem Trade-Ziel. Das Ziel nicht aus den Augen verlieren.
- Das Ziel des Tradings ist, Hochwahrscheinlichkeitsbedingungen zu identifizieren, nicht jedes Kursziel und nicht jeden Trend zu erfassen.
- Das minimale Gewinnziel der ersten Einheit kann das 50-Prozent-Retracement des vorangehenden Rückgangs sein.
- Die Hälfte einer Position kann an einem kleineren Retracement geschlossen werden, die zweite Einheit für ein weiter entferntes Ziel bleiben.
- Ein relativ kleiner Gewinn auf einer Einheit wird schnell mitgenommen, damit der Zwei-Einheiten-Trade auch bei einem Fehlschlag der größeren These netto vorn liegen kann.

## Funktionsweise

- In der Fixed-Time-Horizon-Methode ist das Label 1, wenn die Rendite über den Horizont h größer als Tau ist, -1, wenn sie unter minus Tau liegt, und 0, wenn ihr Betrag höchstens Tau ist.
- getDailyVol liefert die Tagesvolatilität, mit der die Vorgaben für Gewinnmitnahme und Stop-Loss gesetzt werden.
- Beim Meta-Labeling ist die Seite bekannt, deshalb darf die obere Barriere eine andere Breite haben als die untere.

## Voraussetzungen


## Anwendung im Trading

- Hineinkommen ist leicht, hinausgehen ist der schwere Teil. Die historischen Zonen helfen, den Ausstieg an das eigene Preisverhalten des Marktes zu hängen.
- Ein Bruch durch eine Decke macht aus dieser Decke einen Boden, der als natürliches Schutz- und Zielniveau der laufenden Bewegung dient.
- Dieselbe Logik gilt abwärts: der alte Boden wird zur Decke und damit zum Ziel, an dem ein Short-Rücksetzer Widerstand findet.
- Das nahe bei null liegende Ergebnis symmetrischer Schwellen bei Prognose null soll bei der Beschriftung von Beobachtungen mit der Triple-Barrier-Methode beachtet werden.
- Ein positives langfristiges Gleichgewicht entspricht dem Geschäft eines Positionshalters wie eines Hedgefonds oder eines Asset Managers.

## Regeln und Kriterien

- In der Konfiguration [1,1,1] soll ein Gewinn bei begrenzter Verlusttoleranz und begrenzter Haltedauer realisiert werden.
- In der Konfiguration [1,0,0] wird die Position gehalten, bis ein Gewinn entsteht.
- Eine Ausnahme: Steht ein Urlaub an und die Daten können nicht jede Nacht aktualisiert werden, liegen zwei offene Orders im Markt, der Schutzstop und die Take-Profit-Order zum Ausstiegspreis.
- Vor dem Einstieg wird die allgemeine Ausstiegsstrategie beider Units und das Ziel des Trades bestimmt. Das heißt nicht, einen Zielpreis zu wählen und bei Erreichen zu verkaufen, sondern Ziel und Bedingungen für Stop-Anpassung und Ausstieg jeder Unit festzulegen.
- Preisziele werden oft nach den Pivot-Hochs und Pivot-Tiefs angepasst, die der Trend erzeugt.
- Es gibt keine feste, regelbasierte Ausstiegsstrategie für alle Märkte, Bedingungen und Zeitebenen, wenn die mögliche Rendite maximiert werden soll. Eine objektive Regel auf Preis oder Momentum ist leicht gemacht, maximiert die Belohnung aber nicht.
- Der Satz, man könne nichts falsch machen, wenn man einen Gewinn mitnehme, ist absoluter Unsinn. Zu schneller Gewinn auf der vollen Position begrenzt die mögliche Rendite stark und kann den Trend der größeren Zeitebene verpassen.
- Die Mindestbelohnung nach abgeschlossener Korrektur ist ein neues Extrem jenseits des Korrekturbeginns. Die 100-Prozent-Alternate-Price-Projection kann das Belohnungsziel sein und wird oft, nicht immer, erreicht.
- Änderungen der Ausstiegsstrategie müssen eine logische Folge derselben Faktoren sein, auf denen der Einstieg beruhte: Momentum, Muster, Preis und Zeit.
- Ist ein Ziel erreicht, wird der Stop nachgezogen, nicht zum festen Zielpreis verkauft. Die kurzfristige Unit wird an einem Ziel der kleineren Korrektur herausgenommen, die langfristige bleibt auf das größere Ziel ausgerichtet.
- Konkrete Ziele der langfristigen Unit werden nachgesetzt, wenn der Trend fortschreitet. Vorher gilt ein allgemeines Ziel.
- Gewöhnlich ist das kleinste erwartete Korrektur-Retracement 50 Prozent; bei einer möglichen Welle 4 liegt es bei 38,2 bis 50 Prozent der Welle 3, und die Teilziele werden danach gesetzt.
- In einem starken Trend kann die Hälfte am Median eines Regressionskanals und der Rest an dessen Oberseite genommen werden.
- Ein Tagestrade kann das Ziel an der 100-Prozent-APP haben und ohne mehrere Einheiten geführt werden.
- Nach Abschluss eines korrektiven Intraday-Hochs oder -Tiefs folgen oft schnelle Bewegungen, besonders auf der Short-Seite.

## Risiken und Grenzen


## Beispiele

- Bei Tau gleich 0,01 kann die realisierte Bar-Volatilität in der Nachtsitzung 0,0001 und um die Eröffnung 0,01 betragen.
- Unter einer solchen festen Schwelle wird die große Mehrheit der Labels 0, auch wenn die Rendite vorhersehbar und statistisch signifikant war.
- In der schlechtesten Region bei Prognose minus 5 und Halbwertszeit 5 liegen die Sharpe Ratios um minus 12.
- Bei Prognose minus 5 und Halbwertszeit 10 liegen die Sharpe Ratios etwa bei minus 9.
- Im Rechenbeispiel ist das Gewinnziel 0,005, die Verlustschwelle minus 0,01, die Frequenz 260 Wetten pro Jahr und die Trefferwahrscheinlichkeit 0,7.
- Beim XAU ist das Ziel der kurzfristigen Unit der Ausstieg auf einem Retracement des vorherigen Rückgangs, falls nur eine korrektive Rally entsteht, und das Ziel der langfristigen Unit ein bullischer Trend bis zu einem neuen Hoch.
- Handelt das XAU 179,15 oder macht das Tagesmomentum eine bärische Umkehr, wird der Stop der verbleibenden Unit einen Tick unter dem täglichen Ein-Bar-Tief nachgezogen. Der Ausstieg brachte 46,11 Punkte, 178,45 minus 132,34, drei Tage nachdem das Preisziel erreicht war.
- Das Mindestziel der langfristigen S&P-Unit ist eine Korrektur von 50 Prozent oder mehr des Fünf-Wellen-Rückgangs. Das 50-Prozent-Retracement liegt bei 1501,75.
- Die kurzfristige S&P-Unit wurde mit 35 Punkten geschlossen, Ausstieg 1466,25 bei Einstieg 1431,25.
- Die langfristige S&P-Unit wurde bei 1507,00 ausgestoppt. Der Text nennt den Einstieg vom 27. November dafür mit 1431,75 und einen Gewinn von 75,25 Punkten, denselben Einstieg zuvor auch mit 1431,25.
- OIH: Ziel der kurzfristigen Unit 145,59 bis 146,70, darin die 100-Prozent-Alternate-Price-Projection und das 78,6-Prozent-Retracement, falls nur eine dreiteilige Korrektur entsteht. Allgemeines Ziel der langfristigen Unit ist die Fortsetzung über das Dezember-Hoch.
- Eine bloße Korrektur des EUR/USD sollte etwa das 61,8-Prozent-Retracement bei 1,3657 erreichen. Die ideale Welle-C-Zone ist 1,3636 bis 1,3656.
- Wird 1,3636 erreicht, wandert der Stop der kurzfristigen EUR/USD-Unit auf das 60-Minuten-Ein-Bar-Tief. Am 24. August wurde 1,3636 erreicht, der Ausstieg erfolgte ein paar Bars später bei 1,3625, einen Tick unter dem nachgezogenen Ein-Bar-Tief.
- Die kurzfristige EUR/USD-Unit gewann 156 Pips, Einstieg 1,3469, bei 18 Pips anfänglichem Kapitalrisiko.
- Das Ziel der langfristigen EUR/USD-Unit war ein bullischer Abschnitt über das Juli-Hoch bei 1,3852, und nach den jüngsten Abschnitten viel höher. Ausgestoppt bei 1,4030 mit 561 Pips, Einstieg 1,3469.
- Die zweite S&P-Unit wurde laut Abbildungsunterschrift nahe dem 61,8-Prozent-Retracement auf einem Tr-1BH ausgestoppt. Der Gewinn betrug 75,25 Punkte, Ausstieg 1507,00, Einstieg am 27. November bei 1431,75. Danach lief der Markt bis 1527,00 am 11. Dezember.
- Im EUR/USD wurde die erste Einheit bei 1,4387 geschlossen, 46 Pips, die zweite lief auf 246 Pips; das ausgewiesene Ergebnis war 292 Pips.
- Beim GBP lag das Ziel für die halbe Position am kleineren 50-Prozent-Retracement bei 2,0200; geschlossen wurde bei 2,0217 mit 37 Pips, die zweite Einheit bei 2,0172 mit 82 Pips, zusammen 119 Pips.
- Beim Yen wurden auf einer Einheit 35 Pips am kleineren 50-Prozent-Retracement mitgenommen, als das 60-Minuten-Momentum überverkauft war; die zweite Einheit brachte 26 Pips, zusammen 61 Pips.
- Für das Goldhoch wurden 955 und schließlich 1005 im Februar-Future genannt, 946 und 997 im kontinuierlichen Kontrakt und 1038 im Monatschart; die Gewinnmitnahme sollte um 1000 Dollar liegen.
- Beim ES sollte die erste Einheit bei 1360 aussteigen, knapp unter dem 38,2-Prozent-Retracement, die zweite bei 1390, knapp unter dem 50-Prozent-Retracement; eine Einheit wurde bei 1360 mit 38,75 Punkten Gewinn geschlossen.
- ES-Swing: Einheit 1 bei 1360 mit 38,75 Punkten, das sind 1937,50 Dollar je Future-Kontrakt oder 3,0 Prozent im SPY; Einheit 2 mit 45 Punkten, 2250 Dollar oder 3,4 Prozent im SPY; zusammen 83,75 Punkte und im Schnitt 3,2 Prozent in zwei Tagen, ungehebelt.
- Sojabohnen: Hälfte am 4. Juni an der Medianlinie, Rest am 13. Juli an der Zwei-Standardabweichungs-Obergrenze; Einheit 1 brachte 4287,50 Dollar je Kontrakt, Einheit 2 9100,50 Dollar.
- ES-Tagesshort: Ausstieg an der 100-Prozent-APP, 10 Punkte oder 500 Dollar je Kontrakt, ohne Teilausstiege.
- USD/CAD: erste Einheit bei 1,0119 mit 114 Pips, kurz nach der 100-Prozent-APP bei 1,0145; zweite Einheit bei 0,9980 mit 245 Pips; zusammen 359 Pips.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- A Complete Guide to Volume Price Analysis.pdf, S. 96–115 → [[Trading/Pilot/blocks/a-complete-guide-to-volume-price-analysis-pdf/a-complete-guide-to-volume-price-analysis-pdf-block-006-p096-p115|S. 96–115]]
- Advances in Financial Machine Learning.pdf, S. 58–77 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-004-p058-p077|S. 58–77]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 286–305 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-016-p286-p305|S. 286–305]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 177–196 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-014-p177-p196|S. 177–196]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 196–214 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-015-p196-p214|S. 196–214]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 215–234 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-016-p215-p234|S. 215–234]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 234–250 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-017-p234-p250|S. 234–250]]

## Verwandte Themen
