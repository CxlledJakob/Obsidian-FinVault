---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/21 - Algorithmischer Handel/21 - Algorithmischer Handel|21 - Algorithmischer Handel]]"
weitere_hauptthemen: []
unterthema: "Strategien und Ausführung"
priorität: B
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Pairs Trading


## Kurzdefinition

- Pairs Trading ist die übliche Kointegration zweier Preisreihen: ein Asset long und das andere gleichzeitig short, mit passender Kapitalzuteilung.
- Der Begriff der Kointegration lässt sich leicht auf drei oder mehr Assets erweitern.
- Aktien-Pair-Trading ist die erste algorithmische Mean-Reversion-Strategie, die institutionelle Händler erfanden, nach dem Bericht von Gerry Bamberger bei Morgan Stanley (Patterson, 2010).

## Kernaussagen

- Ein Einheitsportfolio mit nur einer Long- und einer Short-Position in zwei Instrumenten heißt gewöhnlich Spread.
- Hinter einem Paar steht oft eine fundamentale Geschichte, und wenn die Kointegration aufhört, ist der Grund häufig noch verständlich.
- Früher war Pair-Trading profitabler, weil der Markt ineffizienter war und die Gewinne der mean-reverting Paare die Verluste der anderen deckten; für bekannte Strategien ist dieser Renditeverfall besonders scharf.
- Dass Aktienpaare in den effizienten US-Märkten wenig profitabel sind, sagt nicht, dass sie in anderen Ländern unprofitabel sind; für die USA ist das profitablere Ausweichmittel der Handel von ETF-Paaren.
- ETF-Paare fallen nach gefundener Kointegration out of sample seltener auseinander; gesucht werden ETFs mit gemeinsamen ökonomischen Faktoren, etwa Länder-ETFs wie EWA und EWC oder Sektor-ETFs wie RTH und XLP.
- Die Mechanik des ETF-Paarhandels ist dieselbe wie bei Aktien; die alte Uptick-Regel nahm ETFs aus, die neue alternative Uptick-Regel gilt für alle an US-Börsen gehandelten Wertpapiere, und die NBBO-Größen sind größer, an einem typischen Tag bei EWC etwa 5.000 Stück.
- Ein weiteres Paar ist ein Commodity-ETF gegen den ETF der Produzenten dieser Ware, etwa GLD gegen GDX, solange der Commodity-Fonds die Ware selbst hält und nicht Futures.
- Ein stationäres Währungsportfolio folgt derselben Idee wie Länder-ETF-Paare: Länder mit ähnlichen Fundamentaldaten, etwa AUD mit CAD wegen EWA und EWC, oder AUD mit ZAR wegen der Mineneinnahmen.
- Gegenüber den ETF-Paaren sind Währungen gewöhnlich liquider, besonders in den Bid-Ask-Größen, erlauben viel höheren Hebel, haben keine Short-Sale-Beschränkung und sind von Sonntag 17:00 Uhr ET bis Freitag 17:00 Uhr ET durchgehend handelbar.
- Beim Cross AUD.ZAR ist AUD die Basiswährung und ZAR die Quotierungswährung; die Merkregel ist B vor Q im Alphabet, also B.Q.
- Eine Quote von 9,58 bedeutet, dass 9,58 Rand einen australischen Dollar kaufen; der Kauf von 100.000 AUD.ZAR bedeutet den Kauf von 100.000 australischen Dollar und den Verkauf des Gegenstücks, 958.000 Rand zur genannten Quote.
- Futures-Intermarket-Spreads sind Paare von Futures verschiedener Basiswerte, und mean-reverting Exemplare sind schwer zu finden.
- Der nächstliegende Kandidat für Futures-Pair-Trading sind Intermarket-Spreads eng verwandter Märkte, im Energiekomplex WTI-Rohöl CL, Brent-Rohöl BZ, bleifreies Benzin RB und Heizöl HO, alle an der NYMEX.
- CL und BZ im Verhältnis 1:1 wirken als Kandidat naheliegend, weil beide Basiswerte Rohöle sind, ein ADF-Test zeigt den Spread aber weit von stationär entfernt.
- BZ hat CL anhaltend geschlagen; als wahrscheinliche Ursachen nennt der Text die steigende US-Ölproduktion nach Friedman 2012, den Pipeline-Engpass in Cushing nach Philips 2012 und das Iran-Embargo 2012, das Europa und damit BZ stärker traf als die USA.
- Eine typische Anwendung der Kointegrationsanalyse ist Pairs Trading.
- Sind die Aktien von Ford und GM als kointegrierte Zeitreihen bestimmt und ist Ford relativ zu GM zu hoch gelaufen, wird eine Short-Position in Ford gegen eine Long-Position in GM gestellt.
- Der Paartrade erzielt einen Gewinn, egal wie die Divergenz korrigiert wird: Ford fällt, GM steigt, oder eine Kombination aus beidem tritt ein.
- In dieser üblichen Anwendung sagt das Error-Correction-Modell das Verhalten des Spreads zwischen den kointegrierten Reihen vorher.
- Fosback wich davon ab und nutzte das aus dem Error-Correction-Modell abgeleitete Maß als Indikator für eine dritte Variable, den S&P 500, statt für den Spread selbst.

## Funktionsweise

- Die Hedge Ratio kommt aus einer linearen Regression; das Residuum abhängige Reihe minus Hedge Ratio mal unabhängige Reihe wird dann auf Stationarität geprüft.
- Weil der CADF-Test reihenfolgeabhängig ist und die Hedge Ratio beim Tausch der Variablen nicht der Kehrwert ist, wird jede Reihe einmal als unabhängige Variable probiert und die Ordnung mit der negativsten t-Statistik genommen.
- Der Johansen-Test liefert alle unabhängigen Hedge Ratios in einem Lauf und ist von der Reihenfolge unabhängig.
- Für zwei Aktien ist der Spread y1 minus h mal y2, mit positivem h, wenn eine Seite long und die andere short ist; h kommt aus der Regression oder aus dem Johansen-Eigenvektor.
- Kointegrieren die Logpreise, sind die Gewichte Kapitalgewichte, und das Paar enthält implizit Kasse.
- Das Verhältnis der beiden Preise ist nur stationär, wenn die Hedge Ratios betragsgleich sind.
- Für nicht wirklich kointegrierte Paare wird die Hedge Ratio dynamisch neu geschätzt, oder das Verhältnis ersetzt sie als Signal.
- Beim Verhältnis wird verlangt, dass Long- und Short-Seite dasselbe Dollarkapital haben.
- Wenige Broker bieten AUD.ZAR als Cross; üblich ist, X Einheiten B.ZAR zu kaufen und X Einheiten B.AUD zu verkaufen, mit einer liquiden Basis wie USD oder EUR, und das synthetische Paar als USD.ZAR geteilt durch USD.AUD zu schreiben, weil die Quote von AUD.ZAR genau diesem Verhältnis entspricht.
- Der realisierte Live-Gewinn eines synthetischen Paars lautet auf beide Währungen, ZAR und AUD; der Backtest unterstellt die Heimatwährung, für US-Anleger USD, die weder Basis noch Quote sein muss.
- Damit der reale Gewinn zum Backtest passt, werden Basis und Quote regelmäßig in die Heimatwährung getauscht; nach X Einheiten AUD und Y Einheiten ZAR werden im Text X Einheiten ZAR.USD und Y Einheiten ZAR.AUD gekauft, sonst kann ein großer angesammelter Saldo deutlich abweichen.
- Selbst wenn AUD.CAD fertig handelbar ist, kann es vorteilhaft sein, die Währungen ungleich zu gewichten und AUD.USD gegen USD.CAD getrennt zu handeln.
- Der Johansen-Test läuft auf AUD.USD und CAD.USD, damit der Eigenvektor Kapitalgewichte sind; live wird Kauf 1 CAD.USD zu Verkauf 1/y USD.CAD, mit y als aktueller USD.CAD-Quote.
- Die Rendite einer Einheit Bi.USD ist die Änderung der Quote geteilt durch die alte Quote, weil eine Einheit Bi.USD genau yi,U Dollar wert ist; eine Einheit USD.Qi ist genau einen Dollar wert.
- Für zwei völlig verschiedene Crosses B1.Q1 gegen B2.Q2 ist die Rendite jedes Cross die Differenz der Log-Quotes, und dieselben Formeln gelten, wenn statt USD eine andere Heimatwährung wie EUR verwendet wird.
- Gelegentlich gibt es profitable Gelegenheiten, zwei völlig verschiedene Crosses gegeneinander zu handeln.
- Der Crack Spread ist long drei CL, short zwei RB und short ein HO, weil drei Barrel CL ungefähr zwei Barrel Benzin und ein Barrel Heizöl ergeben, was nicht für jede Raffinerie gilt.
- Ein Portfolio long 0,3906 VX und long ein ES soll stationär sein; die Hedge Ratio stammt aus ES mal 50 gleich minus 0,3906 mal VX mal 1.000 plus 77.150 Dollar.
- Als die Strategie den Backtest unterschritt, wurde ein fundamentaler Grund gesucht und quantitativ geprüft, statt blind weitere Regeln und Indikatoren zu ergänzen.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Beim Intermarket-Pair-Trading von Futures müssen die Schlusskurse beider Märkte zur selben Zeit entstehen.
- Settlement-Preise zweier Futures mit demselben Underlying und damit derselben Schlusszeit sind gleichzeitig. Letzte Handelspreise können zu sehr verschiedenen Zeiten entstehen und den Spread falsch machen.
- Für einen Intraday-Spread braucht es historische Bid- und Ask-Preise beider Kontrakte oder die Intraday-Daten des Spreads selbst, wenn er an der Börse nativ ist. Ein Anbieter historischer Intraday-Kalender-Spreads mit Quote- und Trade-Preisen ist cqgdatafactory.com.
- Kontrakte an verschiedenen Börsen haben oft verschiedene Schlusszeiten. Einen Intermarket-Spread aus ihren Schlusskursen zu bilden ist falsch, ebenso ein Spread aus dem Schluss eines Futures und eines ETF.
- Die Abhilfe sind Intraday-Bid-Ask-Daten, damit die Gleichzeitigkeit gesichert ist. Die andere Möglichkeit ist, einen ETF zu handeln, der den Future hält. Statt des Gold-Futures GC, dessen Settlement um 13:30 Uhr ET gesetzt wird, gegen den Minen-ETF GDX wird der Gold-Trust GLD gegen GDX gehandelt. Beide laufen an Arca, und ihre Schlusskurse werden um dieselbe Zeit, 16:00 Uhr ET, gesetzt.
- Entstehen die Signale aus der Preisdifferenz zweier Kontrakte, ist die Preisrückanpassung nötig, sonst kann die Differenz falsch sein und ein Fehlsignal erzeugen. Entstehen sie aus dem Preisverhältnis, ist die Renditerückanpassung nötig.
- Bei Kalenderspreads, gleiches Underlying und verschiedene Fälligkeit, wiegt das schwerer. Der Spread ist klein gegen den Preis eines Beins, daher ist ein Fehler durch den Rollover ein erheblicher Prozentsatz des Spreads und löst sehr wahrscheinlich ein Fehlsignal aus, im Backtest und live.
- EUR.GBP wird als Verhältnis gehandelt, weil es EUR.USD geteilt durch GBP.USD ist.
- Für ein Kreuz ohne fertigen Cross-Kurs wie MXN.NOK kann das Verhältnis USD.NOK zu USD.MXN wirksamer sein als der Spread, weil MXN.NOK nicht wirklich stationär ist.
- Der Handel der beiden USD-Paare erzeugt Gewinn und Verlust in NOK und in MXN, der direkte Handel von MXN.NOK nur in NOK.
- Bei Währungspaaren ist oft das Ratio statt des Spreads ein guter Indikator.
- Intermarket-Spreads dürfen nur mit synchronen Preisen getestet werden.
- Ein Schlusskurs-Backtest von BZ gegen CL vor dem 5. September 2001 wäre falsch, weil BZ bis dahin in London an der Intercontinental Petroleum Exchange und CL an der NYMEX mit anderer Schlusszeit gehandelt wurde.
- Futures-Preise sind oft mit einem Faktor von Punkten in US-Dollar umzurechnen, bei VX mal 1.000 und bei ES mal 50.
- Der Crack Spread muss auf preisadjustierten und nicht auf renditeadjustierten fortlaufenden Kontrakten getestet werden, sonst springt der Preisspread an den Rolls.

## Risiken und Grenzen

- Ein Spread aus zeitlich versetzten letzten Preisen erzeugt im Backtest Fehltrades wegen eines unrealistisch großen Spreads. Diese Trades wirken unrealistisch profitabel, wenn der Spread später auf den korrekten kleineren Wert zurückgeht, etwa sobald nahezu gleichzeitige Geschäfte stattfinden.
- Viele Futures sind wenig liquide. Die letzten Preise der Kontrakte A und B im selben Bar können Geschäfte meinen, die zeitlich weit auseinanderliegen. Ein Spread aus solchen asynchronen letzten Preisen war zu diesen Preisen nicht kauf- oder verkaufbar. Backtests, die den letzten Preis jedes Beins statt den letzten Preis des Spreads selbst verwenden, blähen die Renditen auf.
- Anders als bei diesem fundamental begründeten Auseinanderfallen kann eine Momentum-Strategie eines Tages ohne Erklärung aufhören, sobald die langsameren Anleger aufgeholt haben.
- Ob ein Verhältnis grundsätzlich besser ist als ein Spread mit adaptiver Hedge Ratio, beantwortet der Text nicht allgemein; im GLD-USO-Beispiel ist der adaptive Preis-Spread deutlich besser.
- Der Unterschied zwischen Spotöl und den Öl-Futures, aus denen USO besteht, wird hier übergangen und in Kapitel 5 wieder aufgenommen.
- Fehlerhafte Live-Bid-Ask-Quotes sind beim Handel von Paaren und anderen Arbitragestrategien besonders gefährlich, weil die Signale oft von Quote-Differenzen abhängen und diese Differenz meist viel kleiner ist als die Quotes selbst.
- Jeder Quote-Fehler erzeugt dadurch einen viel größeren prozentualen Fehler im Spread.
- Steigt der angezeigte Ask von Y von 105 auf 106 Dollar bei einem wahren Bid von X bei 100 Dollar, wächst der Spread von 5 auf 6 Dollar, also um 20 Prozent, und kann eine fehlerhafte Order zum Kauf von X und Verkauf von Y auslösen.
- Der Autor sah das an einem Broker-Datenfeed einer Aktienpaar-Strategie: regelmäßig unerklärliche Verlusttrades, die nach dem Wechsel auf Yahoo-Echtzeitquotes aufhörten; auch Bloombergs Live-Feed löste diese schlechten Trades nicht aus.
- Selbst sinnvolle Paare wie Exxon gegen Chevron oder Citibank gegen Bank of America kointegrieren selten out of sample, weil Management und Wettbewerb die Lage einer Firma schnell ändern; AAPL gegen BBRY zeigt, dass dieselbe Branche kein gemeinsames Schicksal garantiert.
- Ohne fundamentales Verständnis beider Firmen und ohne Ausstieg, bevor schlechte Nachrichten öffentlich werden, ist ein einzelnes Aktienpaar schwer konsistent profitabel.
- Viele Paare retten das Portfolio nur, wenn die erwartete Out-of-Sample-Rendite je Paar positiv ist; die kleinen Gewinne guter Paare wurden von den großen Verlusten schlechter Paare überwogen.
- Die Short-Sale-Beschränkung ist besonders gefährlich, wenn ein schwer zu leiender Titel leerverkauft wird: die Position kann zum ungünstigsten Zeitpunkt zwangsliquidiert werden.
- Springt der geshortete Titel wegen unerwarteter guter Nachrichten, wollen viele Verleiher verkaufen, die geliehene Aktie kann zurückgerufen werden, und man muss mit großem Verlust decken und das Long-Bein verkaufen; das ist der Short Squeeze.
- Die alternative Uptick-Regel seit 2010 verbietet nach ausgelöstem Circuit Breaker im Wesentlichen Short-Market-Orders und erzeugt Unsicherheit in Backtest und Live-Ausführung.
- Intraday sind die NBBO-Größen sehr klein geworden, bei AAPL nicht ungewöhnlich nur 100 Stück, durch Dark Pools, nicht angezeigte Iceberg-Orders, das Zerlegen großer Orders in kleine Child Orders, häufig stornierte Kleinorders von Hochfrequenzhändlern und die Zurückhaltung der Market Maker, große Größen zu zeigen.
- Market Orders auf beiden Seiten nach einem NBBO-Signal können erheblichen Slippage erzeugen; man ist gezwungen, auf einer Seite Limit Orders zu schicken oder beide Seiten in kleinen Bruchteilen mit zeitweise kleinen ungehedgten Positionen und Stornierungen sowie Neueinstellungen aktiv zu führen.
- Die Dezimalisierung der US-Aktienpreise verengte die Bid-Ask-Spreads drastisch, sodass Pair-Trader, die wie Market Maker auftreten, geringere Market-Making-Gewinne haben (Serge, 2008).
- Die Gleichungen ohne Rollover-Zinsen sind nicht streng korrekt; bei der kurzfristigen Strategie ist die Wirkung meist klein.
- Der ADF-Test auf dem Crack Spread vom 20. Mai 2002 bis zum 4. Mai 2012 zeigt keine Mean Reversion, und die lineare Mean-Reversion-Strategie darauf hat negative Renditen.
- Die Suche nach mean-reverting Intermarket-Futures-Spreads bleibt bis zum VX-ES-Spread ohne Erfolg.

## Beispiele

- EWA und EWC werden geprüft, weil die australische und die kanadische Wirtschaft rohstoffbasiert sind; die Preispunkte liegen im Streudiagramm auf einer Geraden, und das Regressionsresiduum sieht sehr stationär aus.
- Mit EWA als unabhängiger Variable ist die CADF-Statistik etwa minus 3,64 gegen den 95-Prozent-Wert minus 3,359, das Paar kointegriert also mit 95 Prozent Sicherheit.
- Für EWA gegen EWC gilt die Warnung nicht, dass nur eine der beiden Ordnungen stationär sei; Trace- und Eigen-Test finden zwei kointegrierende Beziehungen.
- Mit IGE, einem ETF aus Rohstoffaktien, verwirft der Trace-Test die drei Ranghypothesen auf 95 Prozent, während die Eigen-Statistik für r ≤ 0 unter ihrem 90-Prozent-Wert bleibt; der stärkste Eigenvektor hat 23 Tage Halbwertszeit.
- EWA und EWC passen zusammen, weil Kanada und Australien rohstoffdominierte Volkswirtschaften sind.
- GDX und GLD passen zusammen, weil der Wert der Goldbergbauunternehmen stark vom Goldwert abhängt.
- GDX und GLD fielen Anfang 2008 auseinander, weil hohe Energiepreise den Goldbergbau ungewöhnlich teuer machten; die Ausführung steht in Kapitel 4.
- GLD und USO werden trotz der Geschichte, Öl treibe über die Inflation das Gold, vom Kointegrationstest nicht als Paar bestätigt.
- Der Preis-Spread USO minus Hedge Ratio mal GLD, täglich über 20 Tage neu geschätzt, sieht sehr stationär aus und erreicht etwa 10,9 Prozent APR und eine Sharpe Ratio von etwa 0,59.
- Der Log-Preis-Spread erreicht 9 Prozent APR und eine Sharpe Ratio von 0,5, vor den Kosten des täglichen Rebalancings, und das Verhältnis USO zu GLD sieht nicht stationär aus und hat eine negative APR.
- Die Bollinger-Fassung desselben Spreads mit Einstieg bei einer Standardabweichung und Ausstieg am Mittel erreicht 17,8 Prozent APR und eine Sharpe Ratio von 0,96.
- EWA und EWC mit Kalman-Filter erreichen 26,2 Prozent APR und eine Sharpe Ratio von 2,4; die Steigung schwankt um 1.
- Steigen die Preise eines Paares von 10 und 5 auf 100 und 50, bleibt das Verhältnis 2, der Spread steigt von 5 auf 50.
- AUD.USD gegen CAD.USD mit ungleicher Hedge Ratio: APR 11 Prozent und Sharpe Ratio 1,6 vom 18. Dezember 2009 bis 26. April 2012.
- Das fertige Paar AUD.CAD mit Rollover und Hedge Ratio eins ist deutlich schwächer: APR 6,2 Prozent und Sharpe Ratio 0,54.
- Das ETF-Paar GLD gegen GDX hörte 2008 auf zu kointegrieren.
- Die Hypothese schrieb das dem hohen Rohölpreis zu.
- Mit dem Ölpreis als zusätzlicher Inputvariable funktionierte das Kointegrationsmodell wieder.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 419–438 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-023-p419-p438|S. 419–438]]

## Verwandte Themen
