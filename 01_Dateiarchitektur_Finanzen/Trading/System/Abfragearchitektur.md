---
typ: system
status: entwurf
version: 0.1
---

# Abfragearchitektur

Wie eine Frage durch den Vault läuft, bevor irgendwer eine Strategie definiert. Die Wissensnotizen bleiben das Gedächtnis. Diese Notiz legt nur fest, wo eine Frage anfängt, welche Notiz als Nächstes geöffnet wird und wer am Ende etwas sagen darf.

## Startknoten

Die Themenübersicht ist der Katalog, nicht der Eingang. Eine Frage öffnet nicht 821 Notizen.

| Was in der Frage steht | Erste Datei |
| --- | --- |
| Ein Ticker, zum Beispiel NBIS | Das jüngste Update unter `Research/Analysten/` zu genau diesem Ticker |
| Ein Begriff, zum Beispiel Orderblock | Die Wissensnotiz dieses Begriffs |
| Weder Ticker noch Begriff | Kein Lauf. Die Frage bleibt offen, bis eines von beiden da ist |

Ein Update ist eine Behauptung eines Analysten. Eine Wissensnotiz ist eine Regel aus den Büchern. Beides wird nicht ineinander geschrieben.

## Weg

Vom Update aus geht es nur über das Feld `konzepte`.

1. Das Update lesen. Kursmarken und Szenario bleiben die Behauptung, sie werden nicht zur Regel.
2. Jede genannte Wissensnotiz öffnen, und dort nur Kurzdefinition, Regeln und Risiken.
3. `Verwandte Themen` nur eine Kante weiter, und nur wenn eine Regel in der ersten Notiz fehlt.
4. Eine Quellenzeile nur öffnen, wenn eine Regel belegt werden muss.
5. Stopp. Kein zweites Buch, kein zweites Hauptthema, kein Nachbar-Ticker.

Von einer Wissensnotiz aus ist der Weg kürzer: die Notiz selbst, dann höchstens die direkten Nachbarn aus `Verwandte Themen`.

## Rollen

Vier Durchgänge, nacheinander. Der nächste beginnt erst, wenn der vorige einen Zettel hinterlassen hat. Keiner davon handelt.

**Eingang.** Liest nur die Frage. Wählt die erste Datei aus der Tabelle oben oder bricht ab. Schreibt keine Meinung und öffnet keine zweite Datei.

**Recherche.** Liest die erste Datei und den Weg aus dem vorigen Abschnitt. Sammelt Sätze mit Pfad: welche Datei, welcher Abschnitt. Was nicht in einer Datei steht, kommt nicht auf den Zettel.

**Prüfung.** Hält die Behauptung des Updates neben die Regeln. Drei Ausgänge, nicht mehr:

- Eine Regel trägt die Behauptung.
- Eine Regel widerspricht der Behauptung.
- Die Notiz schweigt. Schweigen bleibt stehen und wird nicht mit einer Vermutung gefüllt.

**Entscheidung.** Darf als Einziger an dich schreiben. Der Text hat vier Zeilen und sonst nichts:

1. Was die Behauptung war.
2. Welche Regel sie trägt oder ihr widerspricht, mit Pfad.
3. Was den Gedanken ungültig machen würde.
4. Was der Vault dazu nicht weiß.

Kein Kauf, kein Verkauf, keine Kursmarke, die nicht schon im Update stand. Die Hilfe ist der Widerspruch, die offene Frage und der Link, nicht ein Tipp.

## Was diese Notiz noch nicht ist

Sie ist keine Strategie. Sie sagt nicht, wann ein Setup gilt. Sie sagt, welche Datei eine Frage anfassen darf, bevor es Strategien gibt.

Die Oberfläche, in der das später neben einem Chart steht, liegt in einem anderen Projekt. Dort gehören Dashboard, Watchlist und Charts hin. Dieser Vault liefert nur den Entscheidungszettel zu dem Ticker, der in der Watchlist ausgewählt ist.
