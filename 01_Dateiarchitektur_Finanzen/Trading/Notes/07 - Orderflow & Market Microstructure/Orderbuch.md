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

# Orderbuch


## Kurzdefinition

- Das Orderbuch ist hier das Double-Auction-Buch, in dem Kaufquotes auf Bid-Niveaus und Verkaufsquotes auf Offer-Niveaus stehen.

## Kernaussagen

- Offer-Preise übersteigen die Bid-Preise, weil es sonst sofort zu einem Match käme.
- Ein Trade entsteht, wenn ein Käufer ein Offer oder ein Verkäufer ein Bid matcht, und nur eine Seite initiiert ihn.
- Mikrostrukturdaten umfassen Stornierungen, das Double-Auction-Buch, Warteschlangen, Teilausführungen, die Aggressorseite sowie Korrekturen und Ersetzungen.
- Die Hauptquelle sind FIX-Nachrichten, die von den Börsen gekauft werden können.
- Der Detaillierungsgrad der FIX-Nachrichten zeigt, wie Marktteilnehmer ihre Absichten verbergen und offenlegen.
- Datensätze enthalten Bid-Ask-Preise auf mehreren Buchebenen.
- Im Markt für Corporate Bonds gibt es kein zentrales Orderbuch, und die Trades laufen über Bids Wanted in Competition.
- Die meisten High-Frequency-Momentum-Strategien ziehen Information aus dem Orderbuch: Ist die Bid-Size viel größer als die Ask-Size, wird ein Tick nach oben erwartet, und umgekehrt.
- Ein Ungleichgewicht des gesamten Buchs, nicht nur des NBBO, erzeugt Preisänderungen, gezeigt von Hellström und Simonsen (2006) für eine Aktie in Stockholm.
- Käufe aus dem Buch zum Ask erzeugen positiven Orderflow, Verkäufe negativen.

## Funktionsweise

- Ein tickbasiertes Backtest kann theoretisch eine Hochfrequenzstrategie prüfen, die von jeder Änderung im Orderbuch abhängt, sofern die Hardware stark genug ist.
- Auf Pro-rata-Märkten wie den Eurodollar-Futures an der CME entspricht der Füllungsanteil dem Verhältnis der eigenen Größe zur aggregierten Größe auf dem Bid.
- Auf Märkten mit Zeitpriorität funktioniert Flipping über eine große Buy-Limit-Order am Best Bid, eine kleine Sell-Limit-Order am Best Ask und die anschließende Stornierung der großen Kauforder.
- Private Feeds ITCH von Nasdaq, EDGX Book Feed von Direct Edge und PITCH von BATS zeigen die Lebensgeschichte einer Order inklusive Änderungen und Teilausführungen.
- Wie oft ein großes Bid storniert statt gefüllt wird, ist daraus ablesbar und hilft, Flipping zu erkennen.

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen

- Selbst mit historischen Daten des gesamten Orderbuchs hängt der Gewinn einer Hochfrequenzstrategie noch stark von den Reaktionen der anderen Marktteilnehmer ab.
- Zu fragen ist, ob eine Heisenbergsche Unschärfe wirkt: Das Platzieren oder Ausführen einer Order kann das Verhalten der anderen Teilnehmer verändern.
- Die meisten Spezialplattformen können Level-2-Daten des Orderbuchs nicht backtesten, sodass dafür meist ein eigenes Programm nötig ist.
- Die NBBO-Sizes sind allgemein gesunken; bei AAPL oft nur ein paar hundert Aktien, bei SPY auf ARCA oft unter 10.000.
- Große institutionelle Orders werden in winzige Child Orders zerlegt und über den Tag sowie verschiedene Plätze gestreut.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 305–324 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-017-p305-p324|S. 305–324]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 173–186 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-013-p173-p186|S. 173–186]]

## Verwandte Themen
