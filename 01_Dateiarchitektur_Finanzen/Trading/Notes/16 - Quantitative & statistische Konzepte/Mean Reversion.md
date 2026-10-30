---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Zeitreihen"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Mean Reversion


## Kurzdefinition

- Mean Reversion ist die Rückkehr des Preises ins Gleichgewicht, nachdem eine Bewegung weg von der Value die Auktion abgeschaltet hat.
- Regression zum Mittel bedeutet, dass der Preis nach einem versuchten Bruch mit fallendem Volumen wahrscheinlich zum Mittel zurückkehrt.
- Mean Reversion ist die Annahme, dass der Preis zum Mittel zurückkehrt.
- Der Mean, zu dem der Preis zurückkehrt, ist die Value Area des Tages, an dem der Spike entstand.
- Der Preis folgt einem diskreten Ornstein-Uhlenbeck-Prozess, der ihn mit dem Gewicht 1 minus phi zur Prognose und mit dem Gewicht phi zum vorherigen Preis zieht.

## Kernaussagen

- Sobald eine Value Area steht, sind Verkäufer unter der Value und Käufer über der Value abgeschreckt. Jede Bewegung weg vom Wert stoppt den Auktionsfluss, bis der Preis zurück ist.
- Ein Bracket zeigt sich daran, dass Bewegungen fortlaufend zu derselben Value Area zurückkehren und der Preis monatelang in festen Grenzen bleiben kann.
- Setzt zweiseitiger Handel ein, wird der Preis immer zum zentralen Value zurückgezogen, statistisch das Mittel.
- Schneiden höhere Preise die Aktivität ab, kehrt der Preis in der Regel zum Mittel zurück.
- Ohne Volumen gegen den Sog einer voll entwickelten Verteilung wird der Preis zur etablierten Value Area zurückgezogen.
- Bei einem breiten Mittelwert kehrt der Preis mit hoher Chance zu dessen Gravitationszentrum zurück, wenn der Folgetag nicht bei hohem Volumen auktioniert.
- Ein breiter Mittelwert wirkt dabei als Anker, weil der Preis dort für beide Seiten als fair galt.
- In den Bändern gilt der Durchschnitt als Mean, und oberes wie unteres Band werden zum Kursziel.
- Im Aufwärtstrend wird die Rotation zum unteren Band als überverkaufte Kaufgelegenheit gelesen.
- Ist das Short Covering abgeschlossen, kann der Markt schnell zum Mittel zurückkehren.
- Ein Flight-to-Safety läuft meist weit über Value. Beim Abbau kehrt der Markt schnell in die Bereiche zurück, deren Bewegungen nicht von gesundem Volumen getragen waren, und kann sie durchstoßen.
- Ein Strukturbruch kann ein Mean-Reversion-Muster in ein Momentum-Muster übergehen lassen.
- Im ADF auf Logpreisen ist der Zustand steady, wenn Beta kleiner als 0 ist, und der erwartete Logpreis konvergiert dann gegen minus Alpha geteilt durch Beta.
- Im steady-Zustand ist die Halbwertszeit der Abweichung der Quotient aus minus dem Logarithmus von 2 und dem Logarithmus der Summe aus eins und Beta.

## Funktionsweise

- Phi bestimmt, wie schnell der Einstiegspreis zur Prognose konvergiert.
- Die zufälligen Schocks sind unabhängig und standardnormal verteilt.
- Die Verteilung des Prozesses ist gaußsch.
- Mittelwert und Varianz hängen von phi, der Prognose, dem Einstieg und der Zahl der seit dem Einstieg verstrichenen Schritte ab.
- Der Preisprozess überträgt sich auf den Gewinn der Gelegenheit, weil der Gewinn die Positionsgröße mal der Preisänderung ist.
- Phi und Sigma werden geschätzt, indem der Prozess linear geschrieben und mit der Methode der kleinsten Quadrate angepasst wird.
- Phi ist dann die Kovarianz des nächsten Preises mit der verzögerten Abweichung von der Prognose, geteilt durch die Varianz dieser Abweichung.
- Sigma ist die Standardabweichung der Residuen der Kleinste-Quadrate-Schätzung.

## Voraussetzungen


## Anwendung im Trading

- Im ausbalancierten Markt mit Glockenkurve und Konsens über die Value ist eine Reversion-to-the-Mean-Strategie angemessen.
- Während des Übergangs von Mean Reversion zu Momentum werden die meisten Teilnehmer überrascht und machen kostspielige Fehler, und daraus entstehen Strategien mit günstigem Chance-Risiko-Verhältnis.

## Regeln und Kriterien

- Preise, die sich an den meisten Tagen ohne höheres Volumen zu weit von Value entfernen, laufen zum Mittel zurück.
- Erwartet wird, dass höhere Preise die Nachfrage abnehmen lassen und der Preis zum Tagesmittel zurückläuft.
- Tiefere Preise verringern in der Regel das Angebot, und der Preis läuft zum Tagesmittel oder zur Value Area zurück.
- Ausnahme: Steigendes Volumen beim versuchten Bruch zeigt neue aggressive Teilnehmer. Dann entstehen wahrscheinlich neue Value Areas statt einer Rückkehr zum Mittel.
- Ziehen höhere Preise mehr Nachfrage an, statt sie abzuschneiden, ist die Auktion nicht abgeschlossen, und die Rückkehr zum Mittel bleibt aus.
- Im Bracket sind die Chancen, sich um das Bracket-Mittel nach oben oder unten zu bewegen, etwa gleich.
- Ziehen in einem Aufwärtstrend höhere Preise neue Käufer und zusätzliches Volumen an, steigt das Mittel mit dem Preis.
- Ziehen höhere Preise weniger Volumen an, ist das Mittel unter dem aktuellen Preis geblieben. Die Chance ist dann hoch, dass der Preis auf diese Niveaus zurückkehrt.
- Nach einem Spike auf niedrigem Volumen sprechen die Chancen für diese Rückkehr.
- Nach einem Spike auf hohem Volumen wandert der Mean zum neuen Preis. Dann kehrt nicht der Preis zur Value zurück, sondern die Value zum Preis.
- Bei jedem Spike ist zu prüfen, ob der Preis zu Value zurückkehrt oder Value zum Preis gezogen wird.
- Wird die Value zum tieferen Preis gezogen, setzt sich die Abwärtsauktion fort.
- Schwaches Volumen beim Ausbruchsversuch und das Verfehlen des Vortageshochs sind die zwei Indikatoren, die einen Reversion-to-the-Mean-Trade vorbereiten.
- Entweder wird die Value zum neuen Preis gezogen, oder der Preis kehrt zur Value zurück.
- Der Bauch der b-Formation ist der Mean des Tages. Ohne Wegbewegung auf beträchtlichem Volumen werden diese Preise wahrscheinlich wieder besucht.
- Am nächsten Tag wird über dem b verkauft oder unter dem b gekauft, mit der Erwartung, dass dieses Niveau wieder besucht wird.
- Beim spiegelbildlichen p wird über dem p verkauft oder darunter gekauft, mit der Erwartung, dass der Preis in den dicken Teil der Schleife zurückkehrt.
- Kurzfristige Verhaltenskräfte können den Preis weit vom fundamentalen Wert entfernen, besonders am Ende extremer Bewegungen, wo das Risiko der Preisbewegung am größten ist.
- Je weiter diese Kräfte den Preis treiben, desto interessierter werden Fundamentalisten, die nach dem wahrgenommenen Wert entscheiden.
- Sind die Preise zu tief getrieben, erscheinen aggressive Value-Käufer.
- Die Halbwertszeit ist der negative natürliche Logarithmus von 2, geteilt durch den natürlichen Logarithmus von phi.
- Die Halbwertszeitformel gilt für phi zwischen 0 und 1.
- Zu einer Halbwertszeit tau gehört phi gleich zwei potenziert mit minus eins durch tau.
- Eine kleinere Halbwertszeit bedeutet einen kleineren autoregressiven Koeffizienten.
- Eine größere Halbwertszeit schiebt phi gegen 1 und den Prozess näher an einen Random Walk.

## Risiken und Grenzen

- Wer über Mean Reversion handelt, bleibt nicht profitabel, wenn Abweichungen von der Value zusätzliches Volumen anziehen und die Value neu gesetzt wird.
- Ein nur aus dem Preis gebauter Durchschnitt zeigt die Wanderung des Means unvollständig.
- Vorübergehende Schocks können den wahren Wert über Tage oder über Jahre verdecken.

## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Markets in Profile_ Profiting from the Auction Process.pdf, S. 36–49 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-004-p036-p049|S. 36–49]]
- Markets in Profile_ Profiting from the Auction Process.pdf, S. 50–61 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-005-p050-p061|S. 50–61]]
- Markets in Profile_ Profiting from the Auction Process.pdf, S. 62–79 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-006-p062-p079|S. 62–79]]
- Markets in Profile_ Profiting from the Auction Process.pdf, S. 80–97 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-007-p080-p097|S. 80–97]]
- Markets in Profile_ Profiting from the Auction Process.pdf, S. 98–117 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-008-p098-p117|S. 98–117]]
- Markets in Profile_ Profiting from the Auction Process.pdf, S. 117–119 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-009-p117-p119|S. 117–119]]
- Markets in Profile_ Profiting from the Auction Process.pdf, S. 120–139 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-010-p120-p139|S. 120–139]]
- Markets in Profile_ Profiting from the Auction Process.pdf, S. 139–158 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-011-p139-p158|S. 139–158]]
- Markets in Profile_ Profiting from the Auction Process.pdf, S. 162–181 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-013-p162-p181|S. 162–181]]
- Markets in Profile_ Profiting from the Auction Process.pdf, S. 181–200 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-014-p181-p200|S. 181–200]]
- Markets in Profile_ Profiting from the Auction Process.pdf, S. 200–213 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-015-p200-p213|S. 200–213]]
- Markets in Profile_ Profiting from the Auction Process.pdf, S. 214–225 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-016-p214-p225|S. 214–225]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 267–286 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-015-p267-p286|S. 267–286]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 57–76 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-004-p057-p076|S. 57–76]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 81–100 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-006-p081-p100|S. 81–100]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 100–104 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-007-p100-p104|S. 100–104]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 105–124 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-008-p105-p124|S. 105–124]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 144–150 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-010-p144-p150|S. 144–150]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 151–170 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-011-p151-p170|S. 151–170]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]

## Verwandte Themen

- Balance
- Seitwärtsmarkt
- Anchoring Level
- Bollinger Bands
- Spike Reversal
