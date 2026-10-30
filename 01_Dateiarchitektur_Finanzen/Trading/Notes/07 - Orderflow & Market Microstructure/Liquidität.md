---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/07 - Orderflow & Market Microstructure/07 - Orderflow & Market Microstructure|07 - Orderflow & Market Microstructure]]"
weitere_hauptthemen: []
unterthema: "Mikrostruktur"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Liquidität


## Kurzdefinition

- Liquidität meint hier den ständigen Zufluss und Abfluss von Mitteln, nicht nur die Möglichkeit, eine einzelne Order auszuführen.

## Kernaussagen

- Scalper stellen wesentliche Liquidität, weil sie auf den unmittelbaren Bedarf des Marktes reagieren und von allen Timeframes kaufen und verkaufen.
- Day Trader stellen ebenfalls Liquidität, oft zu hohen eigenen Kosten.
- Die kürzeren Timeframes existieren vor allem, um Liquidität zu ermöglichen. Langfristiges Geld ist klebriger, weil es substanzielle Orders in eine Richtung legt.
- Market Profile ist vollständig liquiditätsgetrieben. Fließen Mittel hinein, auktioniert der Markt schließlich höher, und fließen sie hinaus, schließlich tiefer.
- Das Profil erfasst diesen Fluss und damit die sich ändernden Haltungen der Teilnehmer in der Gegenwart.
- Day-Trader stellen wie Scalper Liquidität bereit, sehr oft zu hohen eigenen Kosten.
- Locals handeln vor allem im Day Timeframe und stellen Liquidität, nicht die Richtung. Sie nehmen als Mittler wenige Ticks auf großem Volumen mit.
- Der Local ist typischerweise für über 50 Prozent des Tagesvolumens verantwortlich, doch mit dem elektronischen Handel hat die Bedeutung der Floors stetig abgenommen. Off-Floor-Händler stellen weiter Märkte und erhöhen damit die Liquidität.
- Ein elongiertes Profil zeigt, dass der Handel gut vermittelt wird.
- Wie gut der Markt den Handel vermittelt, entscheidet sich daran, wohin er zu laufen versucht und ob ihm dieser Versuch gelingt.
- Market Making im Hochfrequenzhandel stellt, wie traditionelles Market Making, Liquidität auf beiden Seiten des Buchs und verdient den Spread.
- Die Insider sehen alle Kauf- und alle Verkaufsorders und damit die tatsächliche Marktstimmung, bevor diese in der öffentlichen Preisaktion sichtbar wird.
- Der Bid-Ask-Spread ist eine Funktion der Liquidität, und Rolls Modell ist ein früher Versuch, die Liquidität eines Titels zu messen.
- Modelle der ersten Generation nutzen Bid-Ask-Spread und Volatilität als Proxies für Illiquidität.
- Illiquidität ist ein Risiko mit einer zugehörigen Prämie und deshalb ein informatives Feature in finanziellen Machine-Learning-Modellen.
- In Kyles Modell ist λ ein inverses Liquiditätsmaß: Die Illiquidität steigt mit der Unsicherheit über den Terminalwert v und sinkt mit dem Noise.
- Geringere Liquidität bedeutet ein höheres λ und eine geringere Nachfrage des informierten Händlers.
- Die Probability of Informed Trading ist der kritische Faktor für die Preisspanne, zu der Market Maker Liquidität bereitstellen.
- Hohe Quotestornierungsraten können geringe Liquidität anzeigen, weil Teilnehmer Quotes veröffentlichen, die nicht ausgeführt werden sollen.
- Liquiditätsanbieter tragen Unsicherheit darüber, ob ein Informationsereignis eingetreten ist, ob es negativ ist, und über die Ankunftsraten von Noise Tradern und informierten Händlern.
- Aus Rolls Spreadschätzungen lassen sich Features über die Liquiditätsbedingungen des Marktes ableiten.
- Bei relativ illiquiden Produkten, einschließlich Aktienoptionen, können Quotes lange irrational bleiben, während spärliche Preise informativ sind.
- Die Vorhersagbarkeit, die Cremers und Weinbaum (2010) aus relativ teuren Calls gegenüber relativ teuren Puts ableiten, ist größer, wenn die Optionsliquidität hoch und die Aktienliquidität niedrig ist.

## Funktionsweise

- Der Local steht zwischen externen Kauf- und Verkaufsorders und erhält für die Vermittlung eine kleine Spanne.

## Voraussetzungen


## Anwendung im Trading

- Unter normalen Marktbedingungen erzeugen Market Maker informierte Prognosen mit niedrigem Cross-Entropy-Verlust, während sie Position Takern Liquidität bereitstellen.

## Regeln und Kriterien

- Wird der Local zu long, senkt er zuerst das Gebot, um den Verkaufsfluss zu stoppen. Schneiden tiefere Preise den Verkauf nicht ab, liquidiert er die Longs und verstärkt den Verkauf.
- Fällt die Zahl der Transaktionen unter das Niveau eines liquiden Marktes, wird Volumen nicht mehr als Marktanteil gelesen, sondern als absolute Zahl.

## Risiken und Grenzen

- Verlässt der Markt eine Balance-Area, bewegt sich der Preis anfangs oft schnell und nichtlinear, die Liquidität schrumpft, und die Gelegenheit ist verloren.
- Hat ein großer Verwalter die schwächer werdende Auktion verpasst, ist die Liquidität nach Beginn der Umkehr in der Regel begrenzt und kann das Ergebnis stark verschlechtern.
- Sobald die Veränderung breit erkannt ist, trocknet die Liquidität aus. Für große Verwalter ist es dann meist zu spät, weil die Veränderung bereits der Normalfall ist.
- Als die Floors noch dominierten und Nachrichten die Händler außerhalb langsamer erreichten, hatten die Locals einen zusätzlichen Vorteil.
- Liquidity Squeezers handeln in dieselbe Richtung wie ein notleidender Großanleger, der eine Position abwickeln muss, und entziehen dabei möglichst viel Liquidität.
- Dadurch überschießen die Preise, und die predatären Algorithmen erzielen einen Gewinn.
- Beim Flash Crash vom 6. Mai 2010 stellten Market Maker Verkäufern weiter Liquidität zu übermäßig großzügigen Kursen, bis sie zum Stop-out gezwungen wurden und eine Liquiditätskrise auslösten.

## Beispiele

- Eine SEC-Konzeptveröffentlichung von Ende 2012 ordnet Market Making als eine von vier Gruppen von Hochfrequenzstrategien ein, neben Arbitrage, strukturellen und direktionalen Strategien.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Markets in Profile_ Profiting from the Auction Process.pdf, S. 50–61 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-005-p050-p061|S. 50–61]]
- Markets in Profile_ Profiting from the Auction Process.pdf, S. 80–97 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-007-p080-p097|S. 80–97]]
- Markets in Profile_ Profiting from the Auction Process.pdf, S. 98–117 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-008-p098-p117|S. 98–117]]
- Markets in Profile_ Profiting from the Auction Process.pdf, S. 162–181 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-013-p162-p181|S. 162–181]]
- Mind Over Markets_ Power Trading with Market Generated Information, Updated Edition.pdf, S. 27–46 → [[Trading/Pilot/blocks/mind-over-markets/mind-over-markets-block-003-p027-p046|S. 27–46]]
- Mind Over Markets_ Power Trading with Market Generated Information, Updated Edition.pdf, S. 53–72 → [[Trading/Pilot/blocks/mind-over-markets/mind-over-markets-block-005-p053-p072|S. 53–72]]
- Mind Over Markets_ Power Trading with Market Generated Information, Updated Edition.pdf, S. 72–78 → [[Trading/Pilot/blocks/mind-over-markets/mind-over-markets-block-006-p072-p078|S. 72–78]]
- Mind Over Markets_ Power Trading with Market Generated Information, Updated Edition.pdf, S. 98–117 → [[Trading/Pilot/blocks/mind-over-markets/mind-over-markets-block-008-p098-p117|S. 98–117]]
- Mind Over Markets_ Power Trading with Market Generated Information, Updated Edition.pdf, S. 136–155 → [[Trading/Pilot/blocks/mind-over-markets/mind-over-markets-block-010-p136-p155|S. 136–155]]
- Mind Over Markets_ Power Trading with Market Generated Information, Updated Edition.pdf, S. 174–193 → [[Trading/Pilot/blocks/mind-over-markets/mind-over-markets-block-012-p174-p193|S. 174–193]]
- Mind Over Markets_ Power Trading with Market Generated Information, Updated Edition.pdf, S. 288–296 → [[Trading/Pilot/blocks/mind-over-markets/mind-over-markets-block-018-p288-p296|S. 288–296]]
- Mind Over Markets_ Power Trading with Market Generated Information, Updated Edition.pdf, S. 297–314 → [[Trading/Pilot/blocks/mind-over-markets/mind-over-markets-block-019-p297-p314|S. 297–314]]
- A Complete Guide to Volume Price Analysis.pdf, S. 58–77 → [[Trading/Pilot/blocks/a-complete-guide-to-volume-price-analysis-pdf/a-complete-guide-to-volume-price-analysis-pdf-block-004-p058-p077|S. 58–77]]
- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]

## Verwandte Themen
