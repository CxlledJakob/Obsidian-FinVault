---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Modelle"
priorität: C
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Entropie


## Kurzdefinition

- Shannon definiert Entropie als die durchschnittliche Informationsmenge einer stationären Quelle und als die kleinste Bitzahl je Zeichen, mit der sich die Nachricht eindeutig dekodierbar beschreiben lässt.
- Für eine diskrete Zufallsvariable ist die Entropie die negative Summe aus Wahrscheinlichkeit mal Logarithmus der Wahrscheinlichkeit zur Basis 2.

## Kernaussagen

- Die Entropie liegt zwischen 0 und dem Zweierlogarithmus der Alphabetgröße.
- Die Entropie ist 0 genau dann, wenn ein Ausgang Wahrscheinlichkeit 1 hat, und sie ist maximal genau dann, wenn alle Ausgänge gleich wahrscheinlich sind.
- Information wird als Zweierlogarithmus von eins durch die Wahrscheinlichkeit gemessen, weil seltene Ausgänge mehr Information tragen als häufige.
- Die Redundanz ist eins minus den Bruch aus der Entropie und dem Zweierlogarithmus der Alphabetgröße und liegt zwischen 0 und 1.
- Kolmogorov verbindet die Redundanz einer Markov-Quelle mit ihrer Komplexität.
- Die Mutual Information ist die Kullback-Leibler-Divergenz der gemeinsamen Dichte zum Produkt der Randdichten und gleich der Summe der beiden Entropien minus der gemeinsamen Entropie.
- Mutual Information ist nichtnegativ, symmetrisch und genau dann 0, wenn die beiden Variablen unabhängig sind.
- Für gemeinsam normale Variablen ist die Mutual Information minus ein Halb mal dem Logarithmus von eins minus der quadrierten Korrelation.
- Mutual Information misst den Zusammenhang auch dann, wenn er nicht linear ist.
- Die normalisierte Variationsinformation ist eine aus der Mutual Information abgeleitete Metrik.
- Die Entropie eines unabhängig und identisch normalverteilten Prozesses ist der halbe Logarithmus des Produkts aus 2, Pi, e und der Varianz und beträgt für die Standardnormalverteilung etwa 1,42.
- Shannon-Entropie ist der Logarithmus der effektiven Anzahl der Ausgänge, wenn der Potenzparameter des verallgemeinerten Mittels gegen 1 geht.
- Entropie misst Information als Vielfalt einer Zufallsvariablen und ist damit ein Spezialfall eines Diversitätsmaßes, was die Verbindung zur Volatilität erklärt.

## Funktionsweise

- Der Plug-in-Schätzer bildet für Wortlänge w die empirischen Worthäufigkeiten und setzt die Entropierate als negative Summe aus Häufigkeit mal Zweierlogarithmus der Häufigkeit, geteilt durch w.
- Weil die empirische Verteilung die Maximum-Likelihood-Schätzung ist, heißt dieser Plug-in-Schätzer auch Maximum-Likelihood-Entropieschätzer.
- Bei einem stationären ergodischen Prozess liegt die empirische Verteilung für festes w und großes n nahe an der wahren, w muss groß genug und n deutlich größer als w sein.
- Lempel-Ziv zerlegt eine Nachricht in nicht redundante Teilstrings, und komplexe Nachrichten brauchen relativ zur Länge ein großes Wörterbuch.
- Ornstein und Weiss zeigen, dass die längste Übereinstimmung geteilt durch den Zweierlogarithmus der Historie gegen eins durch die Entropierate geht.
- Kontoyiannis schätzt den Mittelwert aus längster Übereinstimmung geteilt durch den Zweierlogarithmus der Historie und nimmt davon den Kehrwert als Entropierate.
- Nachrichten mit hoher Entropie erzeugen bei wachsender Historie relativ kürzere nicht redundante Teilstrings, Nachrichten mit niedriger Entropie längere.
- Die modifizierte Lempel-Ziv-Schätzung mittelt den Zweierlogarithmus der Fensterlänge geteilt durch die Matchlänge und vermeidet damit die Doeblin-Bedingung.
- Beim expandierenden Fenster muss die Nachrichtenlänge gerade sein, damit jedes Bit gelesen wird, weil der Index in der Mitte des Fensters liegt.
- Bias und Varianz der Matchlänge sind ausbalanciert, wenn die Zahl der Matches in der Größenordnung des quadrierten Zweierlogarithmus der Fensterlänge liegt.
- Für eine Länge von 2 hoch 8 ergibt das etwa ein Fenster von 198 und etwa 58 Matches.
- Binärcodierung setzt positive Renditen auf 1 und negative auf 0 und lässt Nullrenditen weg.
- Quantilcodierung vergibt die Codes nach Quantilen, deren Grenzen in der Trainingsstichprobe festgelegt werden.
- Sigmacodierung gibt ein festes Renditeintervall vor und vergibt so viele Codes, wie die Spannweite geteilt durch dieses Intervall, aufgerundet, braucht.

## Voraussetzungen

- Der unveränderte Lempel-Ziv-Schätzer setzt Stationarität, Ergodizität, endlich viele Werte und die Doeblin-Bedingung voraus.
- Doeblin verlangt, dass nach endlich vielen Schritten jeder Ausgang positive Wahrscheinlichkeit hat, unabhängig von der Vergangenheit.
- Die entropieimplizierte Volatilität gilt nur, wenn die Renditen tatsächlich normalverteilt sind.
- Es ist ratsam, fraktional differenzierte Reihen zu codieren, weil sie noch Gedächtnis enthalten.

## Anwendung im Trading

- Die Entropie einer Preiszeichenkette misst den Grad der Markteffizienz zu einem Zeitpunkt: hohe Entropie bedeutet wenig Redundanz und viel Information.
- Ein dekomprimierter Markt ist effizient, weil die Preisinformation nicht redundant ist, ein komprimierter Markt ist ineffizient.
- Blasen entstehen in komprimierten Märkten mit niedriger Entropie.
- Als Beispiel kann ein Lernverfahren Momentum-Wetten profitabler finden, wenn Preise wenig Information tragen, und Mean-Reversion-Wetten, wenn sie viel Information tragen.
- Fiedor schätzt die Entropie nach Kontoyiannis (1997) und argumentiert, der entropiemaximierende künftige Ausgang könne am profitabelsten sein, weil frequentistische Modelle ihn am wenigsten vorhersagen.
- Meucci definiert eine entropieinspirierte Portfoliokonzentration aus den Risikoanteilen der Hauptkomponenten.
- Die Entropie einer quantisierten Folge von Kaufvolumenanteilen liefert über ihre Verteilungsfunktion ein Merkmal für Adverse Selection.
- Aus der Gauß-Formel folgt eine entropieimplizierte Volatilität gleich e hoch (Entropie minus ein Halb), geteilt durch die Quadratwurzel aus 2 Pi.

## Regeln und Kriterien

- Bei Preisbars zwischen zwei symmetrischen Barrieren um den Startpreis ist der Renditebetrag ungefähr konstant, deshalb liegt Binärcodierung dort nahe.
- Quantilcodes sind in der Stichprobe gleich häufig und außer Stichprobe nahezu gleich häufig und erhöhen die Entropiewerte im Mittel.
- Sigmacodes decken jeweils denselben Renditebereich ab, sind nicht gleich häufig und liefern im Mittel kleinere Entropiewerte, ein seltener Code erzeugt aber Ausreißer nach oben.
- Kontoyiannis beweist Konvergenz zur Shannon-Rate mit Wahrscheinlichkeit 1, wenn die Fensterlänge gegen unendlich geht, eine Monotonie wird nicht behauptet.

## Risiken und Grenzen

- Die Entropierate ist ein Grenzwert, bei kurzen Nachrichten kann man dieselbe Nachricht mehrfach wiederholen.
- Wegen des symmetrischen Matchfensters wird das letzte Bit nur bei gerader Länge berücksichtigt, bei ungerader Länge kann man das erste Bit entfernen.
- Stehen vor dem Ende unregelmäßige Folgen, fallen letzte Bits heraus: Die Raten von 10000111 und 10000110 stimmen überein, weil die 11 an sechster und siebter Stelle nicht matcht.
- Ist das Ende der Nachricht besonders wichtig, hilft die Entropie der umgekehrten Nachricht: 11100001 hat die Rate 0,96 und 01100001 die Rate 0,84.
- Binärcodierung verwirft Information, wenn der Renditebetrag stark streut, besonders bei Intraday-Zeitbars mit Heteroskedastizität aus ungleichmäßigen Ticks.
- Ein zu kleines Alphabet unterschätzt die Entropie, weil Information weggeworfen wird.

## Beispiele

- Mit Kontoyiannis' Methode auf Nachrichten der Länge 100 liefert ein Alphabet von mindestens 10 Buchstaben den theoretischen Wert, kleinere Alphabete unterschätzen ihn.
- Im Bootstrap liegt der Mittelwert bei zehn Buchstaben bei 1,43 und bei zwei Buchstaben bei 0,46, gegenüber dem theoretischen Wert 1,42.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Advances in Financial Machine Learning.pdf, S. 286–305 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-016-p286-p305|S. 286–305]]

## Verwandte Themen
