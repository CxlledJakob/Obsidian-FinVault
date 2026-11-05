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
aktualisiert: 2026-11-05
---

# Regime Switching


## Kurzdefinition

- Ein Regimewechsel ist der Übergang von einem Marktregime in ein anderes, etwa von einem Mean-Reversion-Muster zu einem Momentum-Muster.

## Kernaussagen

- Der Chow-Typ-Test prüft einen Wechsel vom Random Walk in einen explosiven Prozess und unterstellt danach nur noch dieses eine Regime bis zum Stichprobenende.
- Für drei oder mehr Regimes, Random Walk zu Blase zu Random Walk, reicht ein einzelner Bruch nicht.
- SADF setzt keine bekannte Zahl von Regimewechseln oder Bruchdaten voraus, weil es alle Kombinationen von Start- und Endpunkt prüft.
- Mögliche Bruchpunkte am Anfang und am Ende der Stichprobe müssen ausgespart werden, damit jedes Regime mit genug Beobachtungen geschätzt wird.
- Blasen erzeugen zwischen Regimes deutlich verschiedene Preisniveaus.
- Historisch gibt es Regimewechsel, nach denen selbst der korrekteste Backtest die künftigen Erträge einer Strategie nicht vorhersagt.
- Momentum- und Mean-Reversion-Strategien zeigen unter verschiedenen Marktregimes der jüngeren Finanzgeschichte diametral verschiedene Risiko-Rendite-Eigenschaften.
- Um die Finanzkrise 2008 wechselt das Verhalten von VIX und seinen Futures das Regime, und der abrupte Leistungseinbruch der VX-Kalenderspread-Strategie vor Oktober 2008 kann damit zusammenhängen.
- Im Streudiagramm von ES gegen VX gibt es zwei Hauptregime, 2004 bis Mai 2008 und August 2008 bis 2012.
- Im zweiten Regime ist die Volatilität bei gegebenem Aktienindexstand deutlich niedriger, die Spannweite der Volatilitäten aber größer, sodass extremere Volatilitätstage vorkommen als zuvor.
- Kürzere Zwischenphasen können Übergangsregime sein und werden in der Analyse ignoriert.
- Das zweite Regime reicht bis zum Zeitpunkt des Schreibens.
- Lineare Regression oder Johansen-Test auf der Mischung beider Regime wären ein Fehler; verwendet wird nur das zweite Regime, und die Koeffizienten werden auf dessen ersten 500 Tagen geschätzt.
- Eine mean-reverting Preisreihe kann für längere Zeit, vielleicht dauerhaft, zu einer Trendreihe werden.
- In der Finanzwelt sind Zusammenhänge anders als in der Physik nicht unveränderlich; was früher für eine Preisreihe galt, muss künftig nicht gelten.
- Gute Strategien bleiben Opfer von Regimewechseln, selbst wenn die Fallstricke aus Kapitel 1 entfernt wurden.
- Weicht der Live-Handel vom Backtest ab, ist die Ursache oft ein Regime Shift und nicht ein Fehler beim Backtesten.
- Der Regime Shift ist ein grundlegender Wandel der Marktstruktur durch staatliche Regulierung oder makroökonomische Änderungen.
- Die Manager müssen dann entscheiden, ob die Modelle noch gültig sind.
- Die statistischen Eigenschaften finanzieller Zeitreihen sind nicht stationär: Die Wahrscheinlichkeitsverteilung der Preise bleibt nicht über die Zeit gleich.
- Wissenschaft kann eigentlich nur mit stationären Statistiken umgehen.
- Im Modell von Barberis, Shleifer und Vishny glauben die Anleger, der Gewinnstrom wechsle zwischen zwei nichtzufälligen Regimes hin und her, einer Wachstumstrend-Phase und einer mittelwertumkehrenden Phase, und betrachten einen Random Walk nicht.
- Ihre angenommene Aufgabe ist, herauszufinden, welches dieser beiden Regimes zu einem gegebenen Zeitpunkt gilt.
- Widerspricht die Nachricht dem geglaubten Regime, unterreagieren sie aus dem Konservatismus-Bias. Hält die widersprechende Nachricht an, werden sie überzeugt, das Regime sei umgeschlagen, entweder von Mean Reversion zu Wachstum oder von Wachstum zu Mean Reversion.
- Dann wechseln sie von dem Fehler, an der Vorannahme zu kleben und zu unterreagieren, zu dem Fehler der kleinen Zahlen und zum Überreagieren.
- In der Illustration starten sie im Glauben an ein Mean-Reversion-Regime der Gewinne, unterreagieren auf die ersten beiden positiven Gewinnmeldungen und nehmen nach der dritten positiven Meldung ein Wachstumsregime an.
- Die Prognosekraft eines Backtests setzt voraus, dass die statistischen Eigenschaften der Preisreihe unverändert bleiben; Wirtschaftsaussichten, das Management eines Unternehmens und die Marktstruktur ändern sich und entwerten diese Annahme oft.
- Strategien, die vor einem Regimewechsel hervorragend liefen, können danach aufhören und umgekehrt.
- Eine mean-reverting Preisreihe kann das Regime wechseln und für längere Zeit, vielleicht für immer, zum Trend werden; ein Stop-Loss verhindert dann katastrophale Verluste und gibt Zeit, die Strategie vor einem Verlust von 100 Prozent abzuschalten.
- Solche Wendereihen erscheinen nicht im Katalog profitabler Mean-Reversion-Strategien, weil gescheiterte Backtests nicht aufgenommen wurden.
- Subjektives Urteil bleibt nötig, weil die statistischen Eigenschaften finanzieller Zeitreihen nicht stationär sind und Wissenschaft eigentlich nur mit stationären Statistiken umgehen kann.
- Stationär heißt in diesem Schlusskapitel, dass die Wahrscheinlichkeitsverteilung der Preise über die Zeit unverändert bleibt, und das ist ein anderer Sinn als die Stationarität der Zeitreihe in Kapitel 2.
- Weicht der Live-Handel vom Backtest ab, ist die Ursache oft ein Regimewechsel der Marktstruktur durch staatliche Regulierung oder makroökonomische Änderungen und nicht ein Fallstrick des Backtests.
- Fondsmanager behalten auch bei einer algorithmischen Strategie die Aufgabe, zu beurteilen, ob die Modelle nach diesem Wechsel noch gültig sind.
- Das Paar GLD gegen GDX ist ein Beispiel: die Kointegration endete 2008 und kehrte erst zurück, nachdem der hohe Rohölpreis als Eingabe aufgenommen wurde.
- Das TAR-Modell nähert die bedingte Mittelgleichung durch stückweise lineare Modelle im Schwellenraum, nicht im Zeitraum.
- Ein k-Regime-SETAR mit Schwellenvariable x_{t−d} setzt in Regime j ein eigenes AR an, solange γ_{j−1} ≤ x_{t−d} < γ_j, mit −∞ = γ_0 < ⋯ < γ_k = ∞.
- Die Verzögerung d ist der Delay-Parameter, die γ_j sind die Schwellen. Die AR-Modelle der Regime müssen sich unterscheiden, sonst lässt sich die Regimezahl verringern. Für k > 1 ist das SETAR nichtlinear.
- Die Innovationen der Regime sind untereinander unabhängig und jeweils iid mit Mittel 0 und Varianz σ²_j.
- Ein offenes TAR ersetzt die Schwellenvariable durch ein z_t, das bezüglich F_{t−1} messbar, stationär und auf einer kompakten Menge stetig verteilt ist und dessen z_{t−d} zur Zeit t bekannt ist.
- Für das Zwei-Regime-AR(1) mit Koeffizient −1,5 bei x_{t−1} < 0 und 0,5 sonst, a_t iid N(0,1), ist der Prozess geometrisch ergodisch und stationär, obwohl −1,5 explosiv ist.
- Notwendig und hinreichend für die geometrische Ergodizität dieses Modells ist φ^{(1)}_1 < 1, φ^{(2)}_1 < 1 und φ^{(1)}_1 φ^{(2)}_1 < 1 (Petruccelli und Woolford, 1984; Chen und Tsay, 1991).
- Die simulierte Reihe ist asymmetrisch und nicht zeitumkehrbar. Negative Werte springen wegen des Koeffizienten −1,5 schnell ins Positive, positive Werte brauchen mehrere Schritte, bis sie negativ werden. Regime 2 enthält mehr Beobachtungen und zeigt große Aufwärtssprünge, sobald die Reihe negativ wird.
- Trotz fehlender Konstanten ist E(x_t) ein gewichtetes Mittel der bedingten Regimemittel und nicht null. Das Gewicht ist die stationäre Wahrscheinlichkeit des Regimes. Der Mittelwert null verlangt von null verschiedene Konstanten in einigen Regimes.
- Für die Änderung der US-Arbeitslosenquote ist die Abhängigkeit stärker, wenn die Monatsänderung über 0,1 Prozent liegt: 460 Beobachtungen im unteren und 262 im oberen Regime.
- Schwellenmodelle bilden in der Finanzanwendung die asymmetrische Volatilitätsreaktion auf positive und negative Renditen ab.
- Ein Einwand gegen SETAR ist, dass die bedingte Mittelgleichung an den Schwellen unstetig ist. STAR-Modelle setzen einen glatten Übergang dagegen (Chan und Tong, 1986; Teräsvirta, 1994).
- Ein Zwei-Regime-STAR(p) gewichtet zwei lineare AR-Gleichungen mit einer glatten Funktion F. Praktisch ist F logistisch, exponentiell oder eine Verteilungsfunktion. Lage und Skala des Übergangs sind c und s, die Verzögerung ist d, und 0 ≤ F ≤ 1.
- Eine Voraussetzung der Stationarität ist, dass alle Nullstellen beider AR-Polynome außerhalb des Einheitskreises liegen. Der bedingte Mittelwert ist differenzierbar. Die Übergangsparameter sind schwer zu schätzen, ihre t-Ratios liegen empirisch oft um 1.
- Das MSA von Hamilton (1989) lässt eine verborgene Markov-Kette den bedingten Mittelwert umschalten. Der Wechsel ist stochastisch. Beim SETAR ist er deterministisch über eine beobachtete Verzögerung festgelegt.
- Die Prognose eines MSA ist immer eine Mischung der Zustandsprognosen. Die eines SETAR stammt aus einem Regime, solange x_{t−d} bekannt ist, und mischt erst, wenn der Horizont d übersteigt.
- Man ist im MSA nie sicher, welcher Zustand vorliegt. Bei großer Stichprobe helfen Filter. Die erwartete Verweildauer in Zustand i ist 1/w_i.
- Für das reale US-GNP entsprechen die zwei Zustände Expansion und Kontraktion mit mittleren Wachstumsraten 0,965 und −1,288 und erwarteten Dauern von etwa 11,31 und 3,69 Quartalen.
- Im AR(2)–TAR–GARCH der täglichen IBM-Renditen hängt auch das Gewicht von σ²_{t−1} vom Vorzeichen des vorherigen Schocks ab. Diese Asymmetrie ist stärker als im GJR-Modell.
- McCulloch und Tsay (1993) machen die Übergangswahrscheinlichkeiten zu logistischen oder Probit-Funktionen von Variablen, die bei t−1 bekannt sind. Mehr als zwei Zustände sind möglich, der Rechenaufwand steigt schnell.
- Die Alternative eines Schwellen-Tests ist hier ein Zwei-Regime-SETAR mit Schwellenvariable x_{t−d}: unterhalb von r1 gilt ein AR(p) mit Koeffizienten φ^{(1)}, ab r1 ein zweites AR(p) mit φ^{(2)}.
- Tsays TAR-F-Test hängt nicht davon ab, dass die Zahl der Regime unter der Alternative bekannt ist.
- Für die Änderung der US-Arbeitslosenquote trennt das TAR die Regime an Δx_{t−2} = 0,1: bei Δx_{t−2} ≤ 0,1 liegt ein nahezu AR(1) mit insignifikantem Lag 2, sonst ein AR(2) mit positiver Konstante und komplexen charakteristischen Wurzeln.
- Die Innovationen der beiden TAR-Regime haben die Stichprobenvarianzen 0,76 und 0,165.
- Das Markov-Switching-Modell hat zwei latente Zustände mit bedingten Mitteln −0,10 und 0,31; Zustand 1 sind Expansionen, Zustand 2 Kontraktionen.
- Die Übergangswahrscheinlichkeit von Expansion zu Kontraktion ist 0,084 mit Standardfehler 0,060, die von Kontraktion zu Expansion 0,126 mit Standardfehler 0,053.
- In der Kontraktion hat die Arbeitslosenquote einen Aufwärtstrend und ein AR(2) mit komplexen Wurzeln, ähnlich dem zweiten TAR-Regime; in der Expansion ist der Trend leicht fallend und die Autoregression deutlich schwächer.
- Die Stichprobenvarianzen der Zustandsinnovationen sind 0,031 in der Expansion und 0,192 in der Kontraktion.
- Die Prognoseleistung von linearem Modell, TAR und Markov-Switching für die US-Arbeitslosenquote wechselt mit dem Regime am Ursprung: in Kontraktionen führen die nichtlinearen Modelle, in Expansionen das lineare Modell.
- Ein Übungsmodell für monatliche Logrenditen schaltet die bedingte Varianz: in Zustand 1 gilt 0,10 a²_{t−1} + 0,93 σ²_{t−1}, in Zustand 2 gilt 4,24 + 0,10 a²_{t−1} + 0,78 σ²_{t−1}.
- Die Übergänge dieses Varianzmodells sind P(s_t = 2 | s_{t−1} = 1) = 0,15 und P(s_t = 1 | s_{t−1} = 2) = 0,05.
- Am Ursprung t = 100 sind a_100 = 6,0 und σ²_100 = 50,0; einmal ist s_100 = 2 mit Wahrscheinlichkeit 1,0, einmal nur mit Wahrscheinlichkeit 0,8, und daraus wird jeweils die Ein-Schritt-Volatilitätsprognose gefragt.
- Das Markov-Switching-Modell ist ein ökonometrisches Modell, bei dem MCMC-Methoden gegenüber der traditionellen Likelihood-Methode viele Vorteile haben.
- McCulloch und Tsay (1994b) schätzen per Gibbs ein Markov-Switching-Modell mit in jedem Zustand zeitkonstanter Volatilität für die saisonbereinigte quartalsweise Wachstumsrate des realen US-Bruttosozialprodukts; die Dynamik der Wachstumsrate unterscheidet sich signifikant zwischen Kontraktion und Expansion.
- Für Asset-Renditen betrachtet der Text den Wechsel der Volatilität: Modell (12.55) ist ein Markov-Switching-GARCH-M mit zwei Zuständen, unterschiedlichen Risikoprämien und unterschiedlicher GARCH-Dynamik.
- In Zustand i gilt rt = βi√ht + √ht εt und ht = αi0 + αi1 ht−1 + αi2 a²t−1; die Übergänge sind P(st = 2 | st−1 = 1) = e1 und P(st = 1 | st−1 = 2) = e2 mit 0 < ei < 1, und ein kleines ei bedeutet Verharren im Zustand i mit erwarteter Dauer 1/ei.
- Zur Identifizierbarkeit gilt β2 > β1, sodass Zustand 2 die höhere Risikoprämie trägt; die Beschränkung dient nur der eindeutigen Beschriftung der Zustände.
- Weil die Rendite von der Volatilität abhängt, ist sie seriell korreliert; künftige Zustände sind unbekannt, die Prognose ist eine Mischung über Zustandskonfigurationen, und die Punktprognose hat oft hohe Unsicherheit.

## Funktionsweise

- Das Schwellen-Dauer-Modell für die IBM-Intraday-Dauern hat zwei Regime; die Schwellenvariable ist die verzögerte adjustierte Dauer xi−1, der geschätzte Schwellenwert ist 3,79.
- Unterhalb von 3,79 gilt ψi = 0,020 + 0,257 xi−1 + 0,847 ψi−1 mit ϵi ∼ w(0,901), oberhalb ψi = 1,808 + 0,027 xi−1 + 0,501 ψi−1 mit ϵi ∼ w(0,845); die Regime enthalten 2503 und 1030 Beobachtungen.
- Die Standardfehler betragen im ersten Regime 0,043, 0,041, 0,024 und 0,014 und im zweiten 0,526, 0,020, 0,147 und 0,020.
- Das verfeinerte Modell ohne insignifikante Parameter lautet ψi = 0,225 xi−1 + 0,867 ψi−1 mit ϵi ∼ w(0,902), falls xi−1 ≤ 3,79, und ψi = 1,618 + 0,614 ψi−1 mit ϵi ∼ w(0,846) sonst; alle Schätzungen sind hochsignifikant.
- Als Phasen starken und schwachen Handels gelesen, unterscheidet das Schwellenmodell die Handelsdynamik von IBM auch nach Bereinigung des Tagesmusters.
- Für die Apple-Logpreis-Range wird ein TWACD(2;1,1) mit Verzögerung d = 1 und regimeweise verschiedenem Weibull-Formparameter geschätzt; Voranalysen zeigen den Hauptunterschied der Regime in diesem Formparameter.
- Der Schwellenwert 0,04753 ist das 70. Perzentil und wird unter den Perzentilen 60, 65, …, 95 gewählt, weil er die Log-Likelihood maximiert; die Schwellenvariable ist xi−1.
- Die gemeinsame Durationgleichung lautet ψi = 0,0013 + 0,1539 xi−1 + 0,8131 ψi−1, Standardfehler 0,0003, 0,0164 und 0,0215; ϵi folgt W(2,2756) bei xi−1 ≤ 0,04753 und W(2,7119) sonst, Standardfehler 0,0394 und 0,0717.
- Bei derselben Schwelle 0,04753 betragen die Log-Likelihood-Werte für d = 2 und d = 3 6,069×10³ und 6,070×10³ und liegen unter dem Wert bei d = 1.

## Voraussetzungen


## Anwendung im Trading

- Beim Regimewechsel werden die meisten Teilnehmer zu spät auf ihren Fehler aufmerksam, halten die Position, hoffen auf eine Rückkehr und vergrößern sie manchmal, bis sie zum Stop gezwungen werden.

## Regeln und Kriterien

- Sind die GARCH-Koeffizienten in beiden Zuständen gleich, gilt überall dasselbe GARCH-Modell; ersetzt man βi√ht durch βi, entsteht ein einfaches Markov-Switching-GARCH-Modell.

## Risiken und Grenzen

- Backtests auf Daten vor solchen Regimewechseln können ziemlich wertlos sein. Backtests auf jüngeren Daten sind nicht aussagekräftiger für künftige Gewinne, sobald ein weiterer Regimewechsel eintritt.
- Nur weil eine Momentum-Strategie vor 2008 gut abschnitt, folgt nicht, dass sie danach gut abschneidet, selbst wenn der Backtest keine der üblichen Fallstricke zeigt.
- Reihen, die von Mean Reversion zu Momentum wechseln, fehlen im Katalog profitabler Mean-Reversion-Strategien, weil deren Backtests gescheitert wären.
- Ein Stop-Loss ist nach einem solchen Wechsel wirksam gegen katastrophale Verluste und gibt Zeit, die Strategie vor einem Verlust von 100 Prozent abzuschalten.
- Er verbessert die Performance, wenn die Preise nach dem Wechsel trendfolgen, und senkt sie, solange Mean Reversion bestehen bleibt.
- Ein Backtest auf Daten vor einem solchen Wechsel kann wertlos sein, und ein Backtest auf jüngeren Daten ist nicht aussagekräftiger, sobald ein künftiger Wechsel eintritt.

## Beispiele

- Am 9. April 2001 wurden die US-Aktiennotierungen dezimalisiert. Zuvor lauteten sie auf Achtel oder Sechzehntel eines Penny. Die Bid-Ask-Spreads sanken, und die angezeigte Liquidität am besten Bid und Ask sank ebenfalls, nach Arnuk und Saluzzi 2012. Viele Statistical-Arbitrage-Strategien wurden weniger profitabel, viele Hochfrequenzstrategien profitabler.
- Die Finanzkrise 2008 löste einen Einbruch der durchschnittlichen Tagesumsätze um 50 Prozent aus, nach Durden 2012, mit besonders starkem Rückgang von Retail-Handel und Aktienbesitz. Die durchschnittliche Volatilität sank, plötzliche Ausbrüche wie der Flash Crash im Mai 2010 und die Herabstufung der US-Bonität im August 2011 wurden häufiger. Mean-Reversion-Strategien, die ein hohes und konstantes Volatilitätsniveau brauchen, verdienten allgemein weniger.
- Dieselbe Krise leitete einen mehrjährigen Bärenmarkt der Momentum-Strategien ein, behandelt in Kapitel 6.
- Die Regulation NMS der SEC, umgesetzt im Juli 2007, trug zum drastischen Rückgang der durchschnittlichen Trade-Größen und zum Verschwinden des NYSE-Blocktrades bei, nach Arnuk und Saluzzi 2012.
- Die alte Uptick-Regel für Leerverkäufe wurde im Juni 2007 aufgehoben, die Alternative Uptick Rule 2010 wieder eingeführt.
- Genannte Wechsel sind die Dezimalisierung am 9. April 2001, der Volumeneinbruch und der Momentum-Bärenmarkt nach der Krise 2008, die Regulation NMS im Juli 2007 sowie die Abschaffung der alten Uptick-Regel im Juni 2007 und ihre Wiedereinführung 2010.
- Bei den monatlichen GE-Logrenditen von Januar 1926 bis Dezember 1999, 888 Beobachtungen in Prozent, betragen die erwarteten Zustandsdauern etwa 11 und 9 Monate; die Posterior-Mittel sind e1 = 0,089 und e2 = 0,112.
- Die Differenz der Risikoprämien β2 − β1 hat das Posterior-Mittel 0,135 bei Standardfehler 0,063 und ist auf dem 5-Prozent-Niveau signifikant; die Posterior-Mittel sind β1 = 0,111 und β2 = 0,247.
- Die Differenzen der Posterior-Mittel der Volatilitätsparameter erscheinen unsignifikant, die Posterior-Verteilungen unterscheiden sich aber: der Persistenzparameter αi1 + αi2 von Zustand 1 erreicht die Grenze 1,0 häufig, der von Zustand 2 nicht.
- Zustand 1 hat die Posterior-Mittel α10 = 2,070, α11 = 0,844 und α12 = 0,033, Zustand 2 α20 = 2,740, α21 = 0,869 und α22 = 0,068, jeweils aus den letzten 2000 von 5000 plus 2000 Gibbs-Iterationen.
- Die angepassten Volatilitäten des einfachen GARCH-M und des Markov-Switching-GARCH-M folgen beide den quadrierten Logrenditen; das einfache GARCH-M ist glatter und liefert niedrigere geschätzte Volatilitäten.
- Die Priors sind β1 ~ N(0,3, 0,09), β2 ~ N(1,3, 0,09) und ei ~ Beta(5, 95); Abbildung 12.14(b) zeigt die Posterior-Wahrscheinlichkeit für Zustand 2.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 362–381 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-020-p362-p381|S. 362–381]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 1–13 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-001-p001-p013|S. 1–13]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 33–51 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-003-p033-p051|S. 33–51]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 180–199 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-014-p180-p199|S. 180–199]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 199–214 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-015-p199-p214|S. 199–214]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 191–210 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-011-p191-p210|S. 191–210]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 210–229 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-012-p210-p229|S. 210–229]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 229–248 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-013-p229-p248|S. 229–248]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 248–267 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-014-p248-p267|S. 248–267]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 286–305 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-016-p286-p305|S. 286–305]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 305–324 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-017-p305-p324|S. 305–324]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 685–704 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-037-p685-p704|S. 685–704]]

## Verwandte Themen
