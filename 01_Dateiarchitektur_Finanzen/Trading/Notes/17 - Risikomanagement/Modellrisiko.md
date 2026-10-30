---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/17 - Risikomanagement/17 - Risikomanagement|17 - Risikomanagement]]"
weitere_hauptthemen: []
unterthema: "Risikomessung"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Modellrisiko


## Kurzdefinition


## Kernaussagen

- Die Annahme, die künftige Verteilung der Marktrenditen gleiche der vergangenen, ist meist falsch; quantitative Modelle können es nicht besser.
- Viele Risikotechniken unterstellen zusätzlich, dass die Verteilung der Strategierenditen dieselbe bleibt, am restriktivsten als Gauß-Verteilung.
- Selbst bei gültiger Gauß-Annahme bleiben Schätzfehler für Mittelwert und Varianz, und künftige Momente müssen nicht den historischen entsprechen.
- Ein dadurch überschätzter Hebel kann zum Ruin führen, und nichtgaußische Renditen können den Kelly-Hebel schon im Backtest auf einen maximalen Drawdown von minus 1 bringen.
- In der Finanzwelt ist, was für eine Preisreihe galt, künftig nicht zwingend wahr; eine Mean-Reversion-Reihe kann dauerhaft zum Trend werden.
- Gute Strategien können durch Regimewechsel scheitern, selbst wenn die Fallstricke aus Kapitel 1 entfernt sind.
- Live-Abweichungen vom Backtest entstehen oft durch einen Regime Shift der Marktstruktur infolge von Regulierung oder Makroökonomie, nicht durch Backtest-Fallstricke.
- Auch bei einer algorithmischen Strategie bleiben Entscheidungen nötig, ob die Modelle noch gültig sind.
- Wissenschaft kommt eigentlich nur mit stationären Statistiken zurecht, während die Verteilung der Preise nicht über die Zeit unverändert bleibt.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading

- Bei einem großen bevorstehenden Ereignis ist zu entscheiden, ob dem Backtest getraut, der Hebel gesenkt oder das Modell vorübergehend abgeschaltet wird.
- Kelly über das Gesamtportfolio ist nur optimal, wenn erwartete Renditen und Volatilitäten unverändert bleiben; nach schwerem Drawdown ist das zweifelhaft.
- Der Autor senkt den Hebel vor einer kommenden Krise nicht, wenn das Modell frühere Stressperioden im Backtest überstanden hat; besser ist von vornherein ein konservativerer Hebel.
- Unknown Unknowns schaden, nicht die Known Unknowns, und die Modelle lassen sich nicht abschalten, bevor Erstere eintreten.
- Praktischer findet er Kelly je Strategie, damit eine underperformende Strategie schnell ausläuft, auch wenn die Mathematik die Allokation über das Gesamtportfolio als optimal ausweist.
- Die Optimalität der gemeinsamen Kelly-Allokation setzt unveränderte erwartete Renditen und Volatilitäten voraus; ein schwerer Drawdown stellt das infrage.

## Regeln und Kriterien


## Risiken und Grenzen

- Das Pearson-System erfasst nicht alle höheren Momente; die empirische Verteilung kann weitere oder, wie bei Pareto-Levy, unendliche höhere Momente haben.
- Alle höheren Momente zu schätzen lädt wegen knapper Daten zu Data-Snooping ein.
- Der an einer historischen Realisierung optimierte Hebel ist für eine künftige Realisierung im Allgemeinen nicht optimal.
- Simulierte Renditen verfehlen serielle Korrelationen, die fortbestehen und den Drawdown verändern können.
- Der simulierte Maximal-Drawdown kann so selten sein, dass er in einer Million Jahren kaum einmal eintritt.
- Subjektives Urteil bleibt nötig, weil die statistischen Eigenschaften finanzieller Zeitreihen nicht stationär sind; stationär heißt hier, dass die Verteilung der Preise über die Zeit unverändert bleibt, abweichend vom Zeitreihenbegriff in Kapitel 2.
- Wissenschaft kann eigentlich nur mit stationären Statistiken umgehen.
- Unknown Unknowns lassen sich nicht dadurch vermeiden, dass die Modelle vorher abgeschaltet werden.
- Urteil bleibt nötig, macht quantitative Regeln aber nicht nutzlos; Kahneman zufolge sind Experten Algorithmen überall dort unterlegen, wo erhebliche Unsicherheit besteht, und der Finanzmarkt ist hoffentlich keine Ausnahme.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]

## Verwandte Themen
