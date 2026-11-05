---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/07 - Orderflow & Market Microstructure/07 - Orderflow & Market Microstructure|07 - Orderflow & Market Microstructure]]"
weitere_hauptthemen: []
unterthema: "Orderbuch"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-11-05
---

# Bid-Ask-Spread


## Kurzdefinition

- Der Bid-Ask-Spread ist die Spanne zwischen Offer und Bid; im Roll-Modell ist c die Hälfte dieser Spanne.

## Kernaussagen

- Die erste Modellgeneration schätzt Spread und Volatilität als Proxies für Illiquidität, ohne dem Handelsprozess eine strategische oder sequenzielle Struktur zu geben.
- Zwei Grundbausteine dieser Generation sind Handelsklassifikationen wie die Tick Rule und das Modell von Roll (1984).
- In der PIN-Theorie ist der Spread die Prämie dafür, dass Market Maker die Option verkaufen, von informierten Händlern advers selektiert zu werden.
- Im Standardfall δt = 1/2 ist der Break-even-Spread (αt μ) / (αt μ + 2ε) mal (SG − SB).
- Dieser Bruch ist PINt und bestimmt die Preisspanne, in der Market Maker Liquidität stellen.
- Der Spread ist eine Funktion der Liquidität, deshalb ist Rolls Modell ein früher Versuch, die Liquidität eines Titels zu messen.
- Corwin und Schultz (2012) schätzen den Spread als Prozentsatz des Preises aus Hoch- und Tiefkursen.
- Hochs werden fast immer gegen das Offer und Tiefs fast immer gegen das Bid gematcht, daher enthält das Hoch-Tief-Verhältnis fundamentale Volatilität und den Spread.
- Der Volatilitätsanteil dieses Verhältnisses wächst proportional zur Zeit zwischen zwei Beobachtungen.
- In den Endgleichungen von Corwin und Schultz erscheint die Volatilität nicht mehr, weil sie durch den Hoch-Tief-Schätzer ersetzt ist.
- Eisler et al. (2012) finden, dass kleine Aktien auf Market Orders, Limit Orders und Stornierungen anders reagieren als große Aktien, und dass diese Größen für die Dynamik des Spreads relevant sind.
- Hasbrouck (2009) findet eine hohe Rangkorrelation zwischen täglichen Schätzungen von Amihuds Lambda und Intraday-Schätzungen des effektiven Spreads.
- Ob der Bid, der Ask oder der letzte Preis einen Trade auslöst, ist ein Umsetzungsdetail, das veröffentlichte Artikel oft übergehen und das die Profitabilität einer live gehandelten Strategie erheblich beeinflussen kann.
- Für Forex-Strategien wird der Backtest mit Bid-Ask-Quotes empfohlen, weil die Bid-Ask-Spreads desselben Währungspaars zwischen Venues erheblich variieren können.
- Die Transaktionskosten sind dadurch stark venue-abhängig und im Backtest zu berücksichtigen.
- Handelspreise und Handelsgrößen sind bei Währungen im Gegensatz zu Bid- und Ask-Quotes im Allgemeinen nicht verfügbar, zumindest nicht ohne kleine Verzögerung, weil Händler oder ECNs den Handelspreis nicht allen Teilnehmern melden müssen.
- Die Dezimalisierung der US-Aktienkurse am 9. April 2001 senkte die Bid-Ask-Spreads und zugleich die angezeigte Liquidität an den besten Bid- und Ask-Preisen, nach Arnuk und Saluzzi 2012.
- Die meisten Spezial-Backtesting-Plattformen sind nicht dafür ausgerüstet, Daten mit sämtlichen Bid-, Ask- und Last-Tick-Preisen und -Größen zu backtesten.
- Slippage entsteht durch den Bid-Ask-Spread und dadurch, dass die Order des Anlegers den Marktpreis beim Kauf nach oben und beim Verkauf nach unten schiebt.
- Die Dezimalisierung der US-Aktienquotes am 9. April 2001 senkte die Bid-Ask-Spreads und zugleich die angezeigte Liquidität am besten Bid und Ask.
- Vor diesem Datum wurden US-Aktien in Achteln oder Sechzehnteln eines Penny quotiert.
- Die Dezimalisierung der US-Aktienkurse hat die Bid-Ask-Spreads drastisch verengt. Paarhändler, die wie Market Maker auftreten, sehen deshalb auch ihre Market-Making-Gewinne sinken (Serge, 2008).
- Ticking verlangt einen ursprünglichen Bid-Ask-Spread von mehr als zwei Ticks.
- Ticking ist nur profitabel, wenn die Round-Trip-Kommission je Stück kleiner ist als der Bid-Ask-Spread minus zwei Ticks.
- Nach der Kauf-Füllung einen Tick über dem Best Bid wird ein Verkauf einen Tick unter dem Best Ask mit Gewinn von mindestens einem Tick versucht; scheitert er, wird zum ursprünglichen Best Bid mit Verlust von einem Tick verkauft.
- Ist das Zeitintervall zwischen den Intraday-Renditen klein, unterliegen die Renditen Mikrostruktureffekten wie dem Bid-Ask-Bounce, der oft eine verzerrte Volatilitätsschätzung erzeugt.
- Für stark gehandelte US-Assets wird zur Konstruktion der realisierten Volatilität oft ein Intervall von 4 bis 15 Minuten gewählt, weil kürzere Intervalle den Bid-Ask-Bounce verstärken.
- Market Maker stellen Liquidität, indem sie bereitstehen, zu kaufen oder zu verkaufen, wann immer das Publikum handeln will; als Gegenleistung erhalten sie das Monopol, unterschiedliche Kauf- und Verkaufspreise zu stellen.
- Sie kaufen zum Bid P_b und verkaufen zum höheren Ask P_a; P_a − P_b ist der Bid-Ask-Spread und die primäre Vergütung. Typischerweise beträgt er ein oder zwei Cent.
- Liquidität meint hier die Möglichkeit, beträchtliche Stücke schnell, anonym und mit geringem Preiseinfluss zu kaufen oder zu verkaufen.
- Im Modell von Roll (1984) gilt P_t = P*_t + I_t S/2 mit S = P_a − P_b und einem unabhängigen Auftragsindikator I_t = ±1 mit gleichen Wahrscheinlichkeiten.
- Ohne Änderung von P*_t folgt Var(ΔP_t) = S²/2, Cov(ΔP_t, ΔP_{t−1}) = −S²/4 und Cov(ΔP_t, ΔP_{t−j}) = 0 für j > 1, also ρ1 = −0,5 und ρ_j = 0 für j > 1.
- Diese negative Lag-1-Korrelation der beobachteten Preisänderungen heißt Bid-Ask-Bounce; über Lag 1 hinaus erzeugt der Spread keine serielle Korrelation.
- Folgt P*_t einem Random Walk mit Varianz σ² und ist diese Innovation unabhängig von I_t, wird Var(ΔP_t) = σ² + S²/2, während die Autokovarianzen unverändert bleiben, sodass ρ1 = (−S²/4) / (S²/2 + σ²) ≤ 0.
- Der Effekt des Spreads bleibt in Portfoliorenditen und in multivariaten Finanzzeitreihen erhalten; kontemporär positiv korrelierte Auftragsindikatoren können negative Lag-1-Kreuzkorrelationen erzeugen.
- An der NYSE betrug die Tick-Größe vor dem 24. Juni 1997 ein Achtel Dollar und vor dem 29. Januar 2001 ein Sechzehntel Dollar; seit dem Dezimalsystem treten Preisänderungen aufeinanderfolgender Trades tendenziell in Vielfachen von einem Cent auf und lassen sich näherungsweise als diskret behandeln.
- Die Seltenheit aufeinanderfolgender gleichgerichteter Preisänderungen in den IBM-Intraday-Daten ist eine klare Demonstration des Bid-Ask-Bounce und zeigt Preisumkehr.
- Die Autokorrelation der Richtungsreihe beträgt bei Lag 1 gleich −0,389 und ist bei 59.837 Beobachtungen hoch signifikant.
- Für IBM im Dezember 1999 war die Tick-Größe ein Sechzehntel Dollar = 0,0625 Dollar statt zuvor ein Achtel; diese Verkleinerung soll den Bid-Ask-Spread senken.
- Im Ordered Probit der 206.794 IBM-Trades von 1988 beträgt der mittlere Spread 1,9470 Ticks bei einer Standardabweichung von 1,4625, und der Spread zum Zeitpunkt t_{i−1} beeinflusst die bedingte Varianz signifikant.
- Der Varianzkoeffizient des Spreads ist γ2 = 0,52 mit t-Wert 71,1 in σ²_i = 1,0 + γ1² Δt*_i + γ2² AB_{i−1}.
- Im ADS-Modell für IBM vom 1. November 1990 bis 31. Januar 1991 ist der geltende Bid-Ask-Spread dagegen statistisch nicht signifikant und wird nicht verwendet.
- Die Zerlegung der Preisänderung zeigt den Bounce zusätzlich in den Richtungswahrscheinlichkeiten: nach einem Anstieg beträgt die Wahrscheinlichkeit eines erneuten Anstiegs nur 0,085, nach einem Rückgang 0,904, jeweils gegeben dass sich der Preis ändert.
- Die US-Aktienmärkte stellten am 29. Januar 2001 von der Tickgröße 1/16 Dollar auf das Dezimalsystem um; diese Änderung betraf den Bid-Ask-Spread der Aktienkurse.
- Eine größere Tickgröße erhöht tendenziell die beobachtete tägliche Preisspanne.
- Für Apple ist der Interventionszeitpunkt t0 = 522 der 26. Januar 2001, der letzte Handelstag vor der Tickgrößenänderung; die Indikatorvariable ist 1 für i ≤ t0 und 0 sonst.
- Im Interventionsmodell ψi = α0 + γ I(t0)i + α1 xi−1 + β1 ψi−1 bezeichnet γ den Rückgang der erwarteten Duration durch die Dezimalisierung; erwartet wird γ > 0.
- Die Schätzung lautet ψi = 0,0021 + 0,0011 I(522)i + 0,1595 xi−1 + 0,7828 ψi−1, mit Standardfehlern 0,0004, 0,0003, 0,0177 und 0,0264; γ̂ ist auf dem 1-Prozent-Niveau signifikant und positiv.
- Die erwartete Duration vor der Intervention ist (α0 + γ)/(1 − α1 − β1) und danach α0/(1 − α1 − β1).
- Weil γ̂ > 0 ist, senkt die Dezimalisierung den erwarteten Wert der täglichen Range und damit die Volatilität der Apple-Aktie.
- Die negative Abhängigkeit der Future-Logrendite vom eigenen Lag 1 in allen drei Regimen des Schwellenmodells stimmt mit dem Bid-Ask-Bounce aus Kapitel 5 überein.
- Wie groß die Spreadabweichung für ein profitables Pairs-Geschäft sein muss, hängt von Handelskosten, Grenzzinssätzen und den Bid-Ask-Spreads der beiden Aktien ab.
- Die Kostenschwelle η des Pairs-Handels hängt voraussichtlich von Transaktionsgebühren und den Bid-Ask-Spreads der beiden Aktien ab.

## Funktionsweise

- Der beobachtete Preis ist pt = mt + bt c, wobei mt der Mid-Price und bt die Aggressorseite in {−1, 1} ist.
- Das Roll-Modell nimmt gleich wahrscheinliche Käufe und Verkäufe an, die seriell unabhängig und unabhängig vom Mid-Price-Rauschen sind.
- Daraus folgt σ²[Δpt] = 2c² + σ²u und die serielle Kovarianz σ[Δpt, Δpt−1] = −c².
- Die halbe Spanne ergibt sich als c = √max{0, −σ[Δpt, Δpt−1]}.
- Der Corwin-Schultz-Spread ist St = 2(e^{αt} − 1) / (1 + e^{αt}).
- Das Spread-Feature S lässt sich über ein rollierendes Fenster fortlaufend schätzen und mit einem Kalman-Filter glätten.
- Market Maker setzen die Bid-Ask-Preise nach dem Orderflow, weil sie daraus fundamentale Information ziehen.

## Voraussetzungen


## Anwendung im Trading

- Roll bleibt nützlich bei selten gehandelten Titeln und dort, wo veröffentlichte Quotes nicht die Niveaus zeigen, zu denen Market Maker Liquidität stellen wollen, etwa bei Corporate-, Municipal- und Agency-Bonds.
- Der Hoch-Tief-Schätzer hilft besonders im Corporate-Bond-Markt, wo kein zentrales Orderbuch besteht und über Bids Wanted in Competition gehandelt wird.
- Für eine Intraday-Spread-Strategie werden historische Bid- und Ask-Preise beider Kontrakte gebraucht oder die Intraday-Daten des Spreads selbst, wenn er an der Börse nativ ist.
- Bei Intermarket-Spreads mit unterschiedlichen Schlusszeiten sind Intraday-Bid-Ask-Daten das naheliegende Mittel, damit die Gleichzeitigkeit der Preise gesichert ist.

## Regeln und Kriterien

- Corwin und Schultz empfehlen, negative Alphas auf 0 zu setzen, weil ein negatives Alpha einen negativen Spread ergäbe.
- Ticking setzt einen ursprünglichen Spread von mehr als zwei Ticks voraus.
- Ticking ist nur profitabel, wenn die Round-Trip-Kommission pro Aktie kleiner ist als der Bid-Ask-Spread minus zwei Ticks.
- Nach dem Kauf zum Best Bid plus einem Tick wird zum Best Ask minus einem Tick verkauft; der angestrebte Gewinn beträgt mindestens einen Tick.
- Bleibt dieser Verkauf ungefüllt, beträgt der Verlust die Kommission plus einen Tick, bei Verkauf zum ursprünglichen Best Bid.
- Am Best Ask kann nach einem Uptick verkauft werden, wenn der Spread größer ist als die Round-Trip-Kommission pro Aktie.

## Risiken und Grenzen

- Die Random-Walk-Annahmen des Roll-Modells stehen gegen die empirischen Eigenschaften Drift, Heteroskedastie, serielle Abhängigkeit und nicht normale Renditen.
- Mit einem geeigneten Sampling, wie in Kapitel 2, können diese Annahmen weniger unrealistisch sein.
- Ein weiterer Spread hätte im Beispiel des Flash Crash den Orderflow-Imbalance beenden können, weil Verkäufer zu diesen Abschlägen nicht mehr verkauft hätten.

## Beispiele

- Bei IBM vom 1. November 1990 bis 31. Januar 1991, Tick-Größe 1/8 Dollar = 0,125 Dollar, liegen die Häufigkeiten der Intraday-Preisänderung bei 0,66, 1,33, 14,53, 67,06, 14,53, 1,27 und 0,63 Prozent für ≤ −3, −2, −1, 0, 1, 2 und ≥ 3 Ticks.
- Rund zwei Drittel der Intraday-Transaktionen hatten keine Preisänderung, etwa 29 Prozent änderten sich um einen Tick, 2,6 Prozent um zwei Ticks und etwa 1,3 Prozent um drei oder mehr Ticks; positive und negative Änderungen sind näherungsweise symmetrisch.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 173–186 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-013-p173-p186|S. 173–186]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 20–39 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-002-p020-p039|S. 20–39]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 33–51 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-003-p033-p051|S. 33–51]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 99–118 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-008-p099-p118|S. 99–118]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 166–179 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-013-p166-p179|S. 166–179]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 172–191 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-010-p172-p191|S. 172–191]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 248–267 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-014-p248-p267|S. 248–267]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 267–286 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-015-p267-p286|S. 267–286]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 286–305 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-016-p286-p305|S. 286–305]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 305–324 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-017-p305-p324|S. 305–324]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 457–476 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-025-p457-p476|S. 457–476]]
- Analysis of Financial Time Series, Third Edition (Wiley -- Ruey S_ Tsay -- Wiley series in probability and statistics, 3rd ed_, -- John Wiley & Sons, -- isbn13 9780470414354 -- 9f99b80c7b2dedd477f463dc5323f3b6 -- An.pdf, S. 476–495 → [[Trading/Pilot/blocks/analysis-of-financial-time-series-third-edition-wiley-ruey-s/analysis-of-financial-time-series-third-edition-wiley-ruey-s-block-026-p476-p495|S. 476–495]]

## Verwandte Themen
