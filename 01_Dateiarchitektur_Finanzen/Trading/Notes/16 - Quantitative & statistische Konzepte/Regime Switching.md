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
aktualisiert: 2026-10-30
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

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- Beim Regimewechsel werden die meisten Teilnehmer zu spät auf ihren Fehler aufmerksam, halten die Position, hoffen auf eine Rückkehr und vergrößern sie manchmal, bis sie zum Stop gezwungen werden.

## Regeln und Kriterien


## Risiken und Grenzen

- Backtests auf Daten vor solchen Regimewechseln können ziemlich wertlos sein. Backtests auf jüngeren Daten sind nicht aussagekräftiger für künftige Gewinne, sobald ein weiterer Regimewechsel eintritt.
- Nur weil eine Momentum-Strategie vor 2008 gut abschnitt, folgt nicht, dass sie danach gut abschneidet, selbst wenn der Backtest keine der üblichen Fallstricke zeigt.
- Reihen, die von Mean Reversion zu Momentum wechseln, fehlen im Katalog profitabler Mean-Reversion-Strategien, weil deren Backtests gescheitert wären.
- Ein Stop-Loss ist nach einem solchen Wechsel wirksam gegen katastrophale Verluste und gibt Zeit, die Strategie vor einem Verlust von 100 Prozent abzuschalten.
- Er verbessert die Performance, wenn die Preise nach dem Wechsel trendfolgen, und senkt sie, solange Mean Reversion bestehen bleibt.

## Beispiele

- Am 9. April 2001 wurden die US-Aktiennotierungen dezimalisiert. Zuvor lauteten sie auf Achtel oder Sechzehntel eines Penny. Die Bid-Ask-Spreads sanken, und die angezeigte Liquidität am besten Bid und Ask sank ebenfalls, nach Arnuk und Saluzzi 2012. Viele Statistical-Arbitrage-Strategien wurden weniger profitabel, viele Hochfrequenzstrategien profitabler.
- Die Finanzkrise 2008 löste einen Einbruch der durchschnittlichen Tagesumsätze um 50 Prozent aus, nach Durden 2012, mit besonders starkem Rückgang von Retail-Handel und Aktienbesitz. Die durchschnittliche Volatilität sank, plötzliche Ausbrüche wie der Flash Crash im Mai 2010 und die Herabstufung der US-Bonität im August 2011 wurden häufiger. Mean-Reversion-Strategien, die ein hohes und konstantes Volatilitätsniveau brauchen, verdienten allgemein weniger.
- Dieselbe Krise leitete einen mehrjährigen Bärenmarkt der Momentum-Strategien ein, behandelt in Kapitel 6.
- Die Regulation NMS der SEC, umgesetzt im Juli 2007, trug zum drastischen Rückgang der durchschnittlichen Trade-Größen und zum Verschwinden des NYSE-Blocktrades bei, nach Arnuk und Saluzzi 2012.
- Die alte Uptick-Regel für Leerverkäufe wurde im Juni 2007 aufgehoben, die Alternative Uptick Rule 2010 wieder eingeführt.

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

## Verwandte Themen
