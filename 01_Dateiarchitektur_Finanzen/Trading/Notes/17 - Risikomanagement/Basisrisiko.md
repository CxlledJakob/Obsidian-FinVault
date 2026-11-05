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
aktualisiert: 2026-11-01
---

# Basisrisiko


## Kurzdefinition


## Kernaussagen

- Futures verschiedener Fälligkeit haben verschiedene Preise. Selbst bei unverändertem Spot bleibt eine Rendite, weil alle Preise zum Spot konvergieren müssen. Das ist die Rollrendite, auch ohne tatsächliches Rollen in den nächsten Kontrakt.
- Die Gesamtrendite zerlegt sich in Spot-Rendite und Rollrendite. Im Modell ist F(t, T) = S(t) mal exp(γ(t − T)). Mit einem Spot S(t) = c mal e hoch αt ist die Gesamtrendite α plus γ.
- Backwardation heißt, nahe Kontrakte sind teurer als ferne, und die Rollrendite ist positiv. Contango heißt das Umgekehrte, und die Rollrendite ist negativ.
- Das Log-Marktwert-Signal eines Kalenderspreads, long der ferne und short der nahe Kontrakt, ist γ mal (T1 − T2) mit T2 größer als T1 und hängt im Modell nicht vom Spot ab, nur von der Rollrendite. Bei großem Abstand muss diese einfache Formel nicht gelten.
- Eine Produzenten-ETF kointegriert gewöhnlich mit dem Spot, wegen der Rollrendite aber nicht notwendig mit dem Future derselben Ware.
- Die Zeichnung mit geraden Log-Preisen ist nur eine Eselsbrücke: reale Log-Futures sind nicht linear in der Zeit, Kontrakte können sich vor dem Verfall schneiden, und der Spot zum Verfall ist nicht konstant.
- Futures-Renditen bestehen aus zwei Komponenten, der Spot-Rendite und der Rollrendite.
- Backwardation bedeutet positive Rollrendite, und ferne Kontrakte sind billiger als nahe Kontrakte; Contango bedeutet negative Rollrendite, und ferne Kontrakte sind teurer als nahe.
- Wegen der Rollrendite erzeugt Mean Reversion des Spotpreises nicht notwendig Mean Reversion des Futurespreises.
- Mean Reversion von Futures-Kalenderspreads gehandelter Basiswerte hängt von der Mean Reversion der Rollrenditen ab.
- Gleichung 5.7 gilt nur für einen Future, dessen Basiswert gehandelt wird; VIX ist keiner, und die Log-Preise der VX-Futures gegen die Restlaufzeit liegen nicht auf einer Geraden.
- Die 3:2:1-Hedge-Ratios des Crack Spreads folgen daraus, dass drei Barrel CL ungefähr zwei Barrel RB und ein Barrel Heizöl ergeben; das gilt nicht für alle Raffinerien.
- CL und BZ im Verhältnis 1:1 sind trotz verwandter Rohöle weit von stationär entfernt, weil BZ CL anhaltend geschlagen hat.
- Als wahrscheinliche Ursachen dieser Divergenz nennt der Text die steigende US-Ölproduktion, den Pipeline-Engpass in Cushing, Oklahoma, und das Embargo gegen iranisches Öl 2012, das Europa und damit BZ stärker traf als die USA.

## Funktionsweise


## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien


## Risiken und Grenzen


## Beispiele


## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 119–138 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-009-p119-p138|S. 119–138]]
- Algorithmic Trading (Winning Strategies and Their Rationale) -- Chan, Ernest P_ -- 2013 may 22 -- John Wiley & Sons, Inc_ -- doi 10_1002_9781118676998 -- e374e4354dcd660c7bc666e0297a580b -- Anna’s Archive.pdf, S. 138–143 → [[Trading/Pilot/blocks/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p/algorithmic-trading-winning-strategies-and-their-rationale-chan-ernest-p-block-010-p138-p143|S. 138–143]]

## Verwandte Themen
