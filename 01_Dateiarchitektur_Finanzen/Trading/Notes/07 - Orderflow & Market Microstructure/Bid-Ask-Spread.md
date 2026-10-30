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
aktualisiert: 2026-10-30
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


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 173–186 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-013-p173-p186|S. 173–186]]

## Verwandte Themen
