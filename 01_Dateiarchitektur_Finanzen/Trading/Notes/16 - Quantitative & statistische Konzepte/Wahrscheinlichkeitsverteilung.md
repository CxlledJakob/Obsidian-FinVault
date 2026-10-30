---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/16 - Quantitative & statistische Konzepte/16 - Quantitative & statistische Konzepte|16 - Quantitative & statistische Konzepte]]"
weitere_hauptthemen: []
unterthema: "Statistik"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Wahrscheinlichkeitsverteilung


## Kurzdefinition

- Stationär meint in diesem Schlusskapitel, dass die Wahrscheinlichkeitsverteilung der Preise über die Zeit unverändert bleibt.
- Die Wahrscheinlichkeitsdichtefunktion gibt die Wahrscheinlichkeit jeder möglichen positiven oder negativen Abweichung einer nutzlosen Regel von einer Rendite von null an.
- Wahrscheinlichkeit ist die relative Häufigkeit eines Ereignisses auf sehr lange Sicht, bei unendlich vielen Gelegenheiten. Sie ist eine Zahl von 0 bis 1 einschließlich. 0 bedeutet, das Ereignis tritt nie ein, 1,0, dass es immer eintritt.
- Die relative Häufigkeit eines Ereignisses ist die Zahl der tatsächlichen Eintritte geteilt durch die Zahl der Gelegenheiten, bei denen es hätte eintreten können, als Bruch zwischen 0 und 1.
- Eine Wahrscheinlichkeitsverteilung zeigt, wie oft die verschiedenen möglichen Werte einer Zufallsvariablen zu erwarten sind. Sie ist eine relative Häufigkeitsverteilung aus unendlich vielen Beobachtungen.
- Die Stichprobenverteilung ist die Wahrscheinlichkeitsverteilung einer Zufallsvariablen, die eine Stichprobenstatistik ist. Sie zeigt die möglichen Werte der Statistik und die zugehörigen Wahrscheinlichkeiten.

## Kernaussagen

- Beim Suchen des optimalen Hebels kann in realistischen Situationen nicht mehr eine Gauß-Verteilung der Renditen angenommen werden.
- Unter der Nullhypothese wird die Verteilung der Tagesrenditen als bekannt unterstellt, mit Mittelwert null.
- Eine Möglichkeit ist die Gauß-Verteilung mit Mittelwert null und der Stichproben-Standardabweichung der Tagesrenditen. Die Teststatistik ist dann der Mittelwert geteilt durch die Standardabweichung mal der Wurzel der Datenpunktzahl. Eine hohe Sharpe Ratio macht die Verwerfung der Null leicht.
- Die Gauß-Verteilung erfasst Extremereignisse nicht. Jenseits davon stehen viele Alternativen zur Wahl, darunter die Student-t-Verteilung, die Schiefe und Kurtosis erfasst, und die Pareto-Verteilung, die auf ein endliches zweites Moment ganz verzichtet.
- Jede solche Wahl hat ein Element von Willkür und beruht auf endlich vielen Beobachtungen. Occams Rasiermesser gebietet die Gauß-Form, sofern nicht starke theoretische und empirische Gründe für eine nicht-gaußsche Verteilung sprechen.
- Ein zweiter Weg schätzt die Verteilung der Gewinne unter der Null empirisch, indem viele Preisreihen mit denselben ersten Momenten und derselben Länge simuliert und durch die Strategie geschickt werden.
- Ein dritter Weg verteilt dieselbe Zahl langer und kurzer Einstiege mit derselben durchschnittlichen Haltedauer zufällig über die echte historische Preisreihe.
- Die drei Verteilungen vergleichen die Strategie mit verschiedenen Zufallsmaßstäben und können deshalb verschiedene Antworten zur Signifikanz geben.
- Eine Nullhypothese ist nicht eindeutig, und verschiedene angenommene Verteilungen können verschiedene Schätzungen der statistischen Signifikanz liefern. Kritiker halten den Hypothesentest deshalb für fehlerhaft, nach Gill 1999.
- Gesucht ist P(H0|R), die Wahrscheinlichkeit, dass die Null wahr ist, gegeben die Teststatistik. Berechnet wird P(R|H0). Selten sind beide gleich.
- Jede zufällige Renditeverteilung mit hoher Kurtosis kann für Momentum-Strategien günstig sein.
- Alle drei Hebelmethoden unterstellen, dass die künftige Wahrscheinlichkeitsverteilung der Marktrenditen der vergangenen entspricht; das ist meist falsch und dennoch das Beste quantitativer Modelle.
- Restriktiver wird dasselbe für die Strategierenditen unterstellt, am restriktivsten eine Gauß-Verteilung.
- Die restriktivste Annahme erzeugt hier die einfachste Lösung, die Kelly-Formel.
- Ist die Gauß-Annahme eine gute Näherung und werden alle Gewinne reinvestiert, maximiert der Kelly-Hebel die zusammengesetzte Wachstumsrate.
- Nichtgaußische Renditen können denselben Hebel schon im Backtest ruinös machen.
- Stationär im Sinn des Schlusskapitels heißt, dass die Wahrscheinlichkeitsverteilung der Preise über die Zeit unverändert bleibt.
- Die statistischen Eigenschaften finanzieller Zeitreihen sind in diesem Sinn nicht stationär, deshalb bleibt subjektives Urteil nötig.
- Wissenschaft kann eigentlich nur mit stationären Statistiken umgehen.
- Dieser Sprachgebrauch unterscheidet sich von der Stationarität von Zeitreihen in Kapitel 2.
- Dass die Dichte bei null zentriert ist, spiegelt die Nullhypothese, die Regel habe eine erwartete Rendite von null.
- Der Flächenanteil bei Werten gleich der beobachteten Rendite oder darüber ist die Wahrscheinlichkeit, eine so hohe oder höhere Rendite durch Zufall zu erhalten, wenn die Regel keine Vorhersagekraft hat.
- Ein großer Flächenanteil bedeutet eine entsprechend große Wahrscheinlichkeit, dass die positive Performance Zufall war; ein kleiner Flächenanteil weit über null bedeutet, dass eine solche Performance unter der Null unwahrscheinlich wäre.
- Für einen Einzeltest und für die beste von 1.000 Regeln gelten verschiedene Dichten: Dieselbe Performance liegt beim Einzeltest weit im rechten Schwanz und bei der Dichte des besten von 1.000 Ergebnissen nicht mehr im Bereich, der als signifikant gilt.
- Nach Konvention gilt eine Beobachtung als statistisch signifikant, wenn ihre Wahrscheinlichkeit unter der Nullhypothese 0,05 oder kleiner ist.
- Beim Münzwurf ist der erwartete Kopfanteil bei sehr vielen Würfen 0,50, bei wenigen Würfen kann der Anteil erheblich davon abweichen.
- Der zentrale Begriff der statistischen Inferenz ist die Extrapolation von Stichproben: Eine in einer Geschichts-Stichprobe profitable Regel wird als künftig profitabel fortgeschrieben.
- Eine Häufigkeitsverteilung oder ein Histogramm zeigt, wie oft jeder mögliche Wert einer Zufallsvariablen auftrat. Die waagerechte Achse trägt ein Intervall je möglichem Wert, die Balkenhöhe die Anzahl.
- Der Begriff Verteilung passt, weil sie zeigt, wie Beobachtungen einer Zufallsvariablen über deren mögliche Werte verteilt sind.
- Die Fläche aller Balken entspricht sämtlichen Beobachtungen. Der Flächenanteil eines Balkens ist gleich dem Anteil der Beobachtungen, den er darstellt.
- In der relativen Häufigkeitsverteilung ist die Balkenhöhe die Anzahl geteilt durch die Gesamtzahl der Beobachtungen. Die relativen Häufigkeiten aller Balken summieren sich zu 1,0, weil die Zufallsvariable stets irgendeinen Wert im abgedeckten Bereich annimmt.
- Die relative Häufigkeit eines Balkens oder einer Gruppe benachbarter Balken ist gleich ihrem Anteil an der Gesamtfläche der Verteilung.
- Die anteilige Fläche einer Verteilung soll am Ende die Wahrscheinlichkeit messen, dass die Backtest-Gewinne einer Regel unter der Annahme keiner Vorhersagekraft durch Zufall entstehen konnten. Ist diese Wahrscheinlichkeit klein, hat die Regel Vorhersagekraft.
- Eine Häufigkeitsverteilung ist gewöhnlich der erste Analyseschritt. Sie gibt einen visuellen Eindruck von zentraler Tendenz und von der Streuung um diesen zentralen Wert.
- Bei nur 50 Beobachtungen kann eine Zahlentabelle einen Gesamteindruck erlauben. Bei 500 oder 5.000 Beobachtungen ist eine Häufigkeitsverteilung informativer als eine Tabelle.
- Drei Werkzeuge der beschreibenden Statistik, deren Ziel die Datenreduktion ist, sind Häufigkeitsverteilungen, Maße der zentralen Tendenz und Maße der Variation.
- Der Durchschnitt, auch arithmetisches Mittel, ist die Summe der beobachteten Werte geteilt durch die Zahl der Beobachtungen. Er wird in vielen Anwendungen der technischen Analyse genutzt und ist die Kennzahl dieses Buches. Median und Modus sind zwei weitere verbreitete Maße der zentralen Tendenz.
- Der Stichprobenmittelwert ist eine bekannte Statistik und variiert zufällig von Stichprobe zu Stichprobe. Der Populationsmittelwert ist unbekannt und variiert in stationären Problemen nicht. Die Formel ist die Summe der Einzelbeobachtungen geteilt durch ihre Anzahl.
- Zentrale Tendenz und Streuung sind unabhängige Merkmale einer Häufigkeitsverteilung.
- Eine Zufallsvariable nimmt mindestens zwei verschiedene Werte an, möglicherweise unendlich viele. Eine einzelne Beobachtung ist unvorhersagbar, eine große Zahl kann hoch vorhersagbare Merkmale haben.
- Wahrscheinlichkeit ist theoretisch, weil unendlich viele Beobachtungen nie möglich sind. Wird die Zahl der Beobachtungen sehr groß, nähert sich die relative Häufigkeit der theoretischen Wahrscheinlichkeit.
- Das Gesetz der großen Zahlen ist die Tendenz der relativen Häufigkeiten, mit wachsender Beobachtungszahl gegen die theoretischen Wahrscheinlichkeiten zu konvergieren. Bei kleinen Stichproben kann die relative Häufigkeit stark vom theoretischen Wert abweichen, und auch bei vielen Beobachtungen bleiben Abweichungen möglich, werden aber wahrscheinlich kleiner.
- Theoretische Wahrscheinlichkeiten lassen sich mit ziemlicher Sicherheit rein logisch bestimmen, meist aus Symmetrie und unabhängig von Erfahrung. Empirische Wahrscheinlichkeiten beruhen auf beobachteten Häufigkeiten. Die technische Analyse hat es mit empirischen Wahrscheinlichkeiten zu tun.
- Bei empirischen Wahrscheinlichkeiten muss jeder Fall durch dieselbe Bedingungsmenge gekennzeichnet sein. In der technischen Analyse ist das praktisch unmöglich, weil neben der genannten Bedingung stets weitere Bedingungen verschieden sein können. Nimmt man sie auf, sinkt die Zahl vergleichbarer Fälle, und andere bleiben immer draußen.
- Dass sich nicht alle potenziell relevanten Variablen kontrollieren lassen, gehört zu den nichtexperimentellen Beobachtungswissenschaften. Der Experimentator kann dagegen alle oder nahezu alle relevanten Variablen außer der untersuchten konstant halten.
- Bei einer stetigen Zufallsvariablen ist die Wahrscheinlichkeit eines einzelnen exakten Werts gleich null, weil Intervalle der Breite null keine Beobachtungen enthalten. Sinnvoll ist nur die Wahrscheinlichkeit für einen Wertebereich oder dafür, dass der Wert eine Grenze erreicht oder über- beziehungsweise unterschreitet. Die Wahrscheinlichkeit von genau 3,0 ist sinnlos, die von 3,0 oder größer sinnvoll.
- Die Wahrscheinlichkeit, dass eine stetige Zufallsvariable in einen festgelegten Bereich fällt, ist gleich dem Flächenanteil der Dichte über diesem Bereich.
- Die Stichprobenverteilung des Stichprobenmittels ist die Wahrscheinlichkeitsverteilung aller möglichen Mittelwerte aller möglichen Zufallsstichproben einer gegebenen Größe aus einer Population.
- Im Regel-Backtest wäre die exakte Stichprobenverteilung der durchschnittlichen Rendite die relative Häufigkeitsverteilung aus unendlich vielen unabhängigen Geschichtsstichproben. Die gibt es nicht. Mehrere Verfahren nähern sie aus einer Stichprobe und einem Statistikenwert hinreichend an. Zwei werden später im Kapitel behandelt.
- Die drei Verteilungen der Inferenz sind die unendliche Datenverteilung aller möglichen Tagesrenditen der Regel bis in die unmittelbare praktische Zukunft, die endliche Verteilung der N vergangenen Tagesrenditen und die unendliche Stichprobenverteilung der mittleren Rendite über Stichproben der Größe N.
- Populations- und Stichprobenverteilung sind theoretisch und unendlich. Die Datenverteilung der Stichprobe ist die endliche Beobachtungsmenge eines historischen Backtests. In den Datenverteilungen stehen einzelne Tagesrenditen, in der Stichprobenverteilung stehen Mittelwerte über Tage.
- Der zentrale Grenzwertsatz sagt, dass die Stichprobenverteilung des Mittelwerts mit wachsender Stichprobengröße, mit Einschränkungen, gegen die Normalverteilung konvergiert, unabhängig von der Form der Population. Die Normalverteilung, auch Gauß-Verteilung, ist die häufigste Wahrscheinlichkeitsverteilung, wird wegen der Silhouette der Liberty Bell Glockenkurve genannt und kennzeichnet stetige Variablen vieler realer Phänomene.
- Die Normalverteilung, auch Gauß-Verteilung, ist so verbreitet, dass sie ein grundlegendes Merkmal der natürlichen Welt genannt wird. Oft heißt sie Glockenkurve, weil sie die Silhouette der Liberty Bell hat, und sie kennzeichnet stetige Variablen vieler realer Phänomene.
- Ihre Form entsteht durch die additiven Wirkungen vieler unabhängiger Faktoren in derselben Situation.
- Die Normalverteilung ist durch Mittelwert und Standardabweichung vollständig beschrieben. Etwa 68 Prozent der Beobachtungen liegen innerhalb einer Standardabweichung um den Mittelwert, etwa 95 Prozent innerhalb von zwei. Jenseits von drei Standardabweichungen sind Werte selten, jenseits von vier äußerst selten.
- Mit wachsender Stichprobengröße konvergiert die Stichprobenverteilung des Mittelwerts gegen die Normalform, mit Einschränkungen und unabhängig davon, wie die Daten in der Elternpopulation verteilt sind.
- An der Zahl 30 ist nichts Magisches. Die Geschwindigkeit dieser Annäherung hängt von der Form der Elternverteilung ab. In drei Fällen der Abbildung erzeugt schon eine Stichprobengröße von 5 eine nahezu normale Verteilung des Mittelwerts, im untersten Fall erst eine Größe von 30.
- Die Wahrscheinlichkeit, dass der beobachtete Wert der Stichprobenstatistik durch Zufall auftritt, wenn der hypothetische Wert wahr ist, wird als Zahl zwischen 0 und 1,0 angegeben.
- Die Stichprobenverteilung gibt die Wahrscheinlichkeiten für Abweichungen verschiedener Größe zwischen dem beobachteten Wert der Stichprobenstatistik und ihrem erwarteten Wert an, soweit sie vom Stichprobenfehler kommen.
- Ein Konfidenzintervall ist ein Bereich, der den wahren Populationsparameter mit einem festgelegten Konfidenzniveau enthält. Seine Breite stammt aus derselben Stichprobenverteilung wie der Hypothesentest.
- Die Stichprobenverteilung wird so gelegt, dass der wahrscheinlichste Renditewert null ist, weil das der von der Null behauptete Parameterwert ist.
- Der p-Wert ist der Flächenanteil der Stichprobenverteilung bei Werten gleich dem beobachteten Wert der Teststatistik oder größer.
- Die Breite dieser Verteilung entscheidet, ob die Abweichung zwischen beobachteter und hypothetischer Rendite eine Verwerfung trägt.
- Die Breite wächst mit der Streuung der täglichen Regelrenditen in der Grundgesamtheit und schrumpft mit der Zahl der Beobachtungen.
- Bootstrap und Monte-Carlo-Permutation erzeugen etwas verschiedene Stichprobenverteilungen, sodass die Entscheidung über die Null nicht immer gleich ausfällt.
- Das Bootstrap-Theorem sichert unter vernünftigen Bedingungen die Konvergenz gegen die richtige Stichprobenverteilung, wenn die Stichprobengröße gegen unendlich geht.
- Die Verteilung wird aus den computererzeugten Werten der Teststatistik aufgebaut; im Ablauf sind das 5.000 Mittelwerte.
- Für ein Konfidenzintervall wird dieselbe Verteilung vom hypothetischen Wert, etwa null, auf den Stichprobenmittelwert verschoben, etwa 7 Prozent.
- Die Breite des Konfidenzintervalls wird aus der Breite dieser Stichprobenverteilung abgeleitet.
- Von vielen unabhängigen 90-Prozent-Intervallen umschließen etwa 90 Prozent den Parameter und etwa 10 Prozent verfehlen ihn; in der Abbildung mit zehn Intervallen verfehlt eines den Mittelwert.
- Eine schiefe Stichprobenverteilung kann den Hypothesentest am rechten Schwanz und das Konfidenzintervall am linken Schwanz zu verschiedenen Schlüssen führen.
- In der nach links schiefen Abbildung liegt weniger als 5 Prozent der Verteilung über der mittleren Backtest-Rendite, während die Untergrenze des 90-Prozent-Intervalls unter null liegt.
- Nach dem Zentralen Grenzwertsatz tendiert die Stichprobenverteilung des Mittelwerts mit wachsender Stichprobe zu einer symmetrischen Glocke und ist bei großer Stichprobe nicht ernsthaft schief.
- Andere Leistungskennzahlen müssen diese Symmetrie nicht teilen.
- Asymmetrische Verteilungen lassen sich mit Bootstrap-Verfahren schwenken.
- Für ein 90-Prozent-Perzentilintervall werden die höchsten und die niedrigsten 5 Prozent der 5.000 geordneten Resample-Mittelwerte entfernt; für 99 Prozent nur die äußeren 0,5 Prozent je Seite, also 25 Werte.
- Bei nur unverzerrtem Fehler streuen die beobachteten Werte ungeordnet um den wahren Wert, der mittlere Fehler liegt ungefähr bei null, und der wahrscheinlichste beobachtete Wert fällt mit dem wahren zusammen.
- Bei systematischem Fehler liegen die Beobachtungen tendenziell auf einer Seite der Wahrheit, und der wahrscheinlichste beobachtete Wert ist nicht der wahre Wert; in der Abbildung ist der mittlere Fehler, beobachtet minus wahr, positiv.
- Die für einen einzelnen Mittelwert unter der Null verwendete Stichprobenverteilung ist auf null zentriert.
- Die Stichprobenverteilung des Maximums von 50 Mittelwerten ist bei plus 33 Prozent zentriert und bildet das im Data Mining eingebaute Glück ab.
- Auf dieser Verteilung hat plus 37 Prozent den p-Wert 0,45; auf der bei null zentrierten Verteilung eines einzelnen Mittelwerts liegt der p-Wert unter 0,05.
- Für eine Regel mit erwarteter Rendite null ist null die wahrscheinlichste beobachtete Rendite, während viel höhere oder niedrigere Renditen möglich, aber selten sind.
- Bei geringem Zufall sind die Verteilungen um das Verdienst jedes Kandidaten schmal und überlappen nicht, sodass der bessere Kandidat auch am unteren Ende seiner Verteilung gewählt wird.
- Bei hohem Zufall und kleinem Merit-Abstand überlappen die Verteilungen zweier fast gleicher erwarteter Leistungen erheblich, und die schwächere Regel kann die höchste beobachtete Leistung liefern.
- Ist der Merit-Abstand groß, liegt die Verteilung der überlegenen Regel weit genug darüber, dass das Verdienst eher durchscheint.
- Je mehr Regeln gebacktestet werden, desto wahrscheinlicher wird eine außerordentlich glückliche beobachtete Leistung, so wie mehr Lotteriespieler die Chance erhöhen, dass jemand zweimal gewinnt.
- Verteilungen mit Extremwerten haben schwere Ränder, die äußeren rechten und linken Zonen seltener extremer Beobachtungen, und sie reichen weiter vom Zentrum weg als leichte Ränder.
- Die Normalverteilung hat leichte Ränder: Körpergrößen sind normalverteilt, über sieben Fuß ist selten, über zehn Fuß hat niemand gesehen; bei schweren Rändern könnte man jemandem von zwanzig Fuß begegnen.
- Enthält die Verteilung der Tages-, Wochen- oder Monatsrenditen Extremwerte, kann auch der Stichprobenmittelwert extrem werden, wenn einer oder mehrere Extremwerte in die Stichprobe geraten und die Stichprobe klein ist.
- Schwere Ränder der Renditeverteilung erzeugen tendenziell schwere Ränder der Stichprobenverteilung des Mittelwerts.
- Der Stichprobenmittelwert ist nie so extrem wie der extremste Wert in der Stichprobe, wegen der Mittelung; die Stichprobenverteilung der mittleren Rendite hat deshalb immer leichtere Ränder als die Verteilung der Intervallrenditen.
- Die Stichprobengröße ist ein eigener Faktor der Randschwere: je mehr Beobachtungen in den Mittelwert eingehen, desto leichter werden die Ränder der Stichprobenverteilung.
- Eine schwere Stichprobenverteilung bedeutet, dass der Zufall eine große Rolle für die mittlere Rendite spielt; bei erwarteter Rendite null liegt eine mittlere Backtest-Rendite über 30 Prozent noch im Wahrscheinlichkeitsbereich, bei leichten Rändern ist eine so hohe Rendite fast unmöglich.
- Es ist weithin anerkannt, dass die Renditeverteilung des Aktienmarkts und anderer Finanzanlagen relativ schwere Ränder gegenüber einer Normalverteilung hat.
- Im Experiment war der Data-Mining-Bias bei einer absichtlich leichtschwänzigen Renditeverteilung deutlich schwächer ausgeprägt als bei den S&P-500-Monatsrenditen, deren Ränder schwerer sind als die der Normalverteilung.
- Eine Stichprobenverteilung aus weniger Beobachtungen ist breiter, und ein Mittelwert aus einer kurzen Historie erzeugt eher ein sehr glückliches Ergebnis als einer aus mehr Beobachtungen.
- Bei wenigen Beobachtungen kann der Stichprobenmittelwert erheblich über oder unter dem wahren Populationsmittelwert liegen.
- Weil Märkte extremen Ereignissen unterliegen, tendieren mittlere Regelrenditen ebenfalls zu Extremen.
- Die Verteilung der Wahrscheinlichkeiten eines profitablen Monats hat eine Form ähnlich der Vermögensverteilung, mit langem rechtem Rand: eine erwartete Jahresrendite von 19 Prozent oder mehr kommt etwa einmal unter 10.000 vor, und der Mittelwert liegt bei +1,4 Prozent pro Jahr.
- White's Reality Check verschiebt die Verteilung der Tagesrenditen jeder Regel so, dass sie über null zentriert ist, indem die mittlere Tagesrendite von jedem einzelnen Tageswert abgezogen wird.
- Bei wenigen Beobachtungen dominiert der Zufall die Güte, die beobachtete Performance liegt weit über der erwarteten, und die beiden Kurven liegen weit auseinander; mit mehr Beobachtungen nähern sie sich, weil die beobachtete Performance die erwartete wahrheitsgetreuer abbildet.
- Die Kurve der beobachteten Performance liegt immer über der Kurve der erwarteten Performance, weil die Auswahl der besten Regel immer einen positiven Bias erzeugt, solange Glück an der beobachteten Performance beteiligt ist.
- Die Stichprobenverteilung der maximalen mittleren Rendite wird aus den wiederholten Bootstrap-Ziehungen gebildet, im Beispiel aus 500 oder mehr Werten für ein Universum von N Regeln mit erwarteter Rendite null.
- In einem effizienten Markt ist die Zeitreihe der Fehlbewertungen eine Zufallsvariable, deren Wahrscheinlichkeitsverteilung am rationalen Preis zentriert und ungefähr symmetrisch darum ist.
- Zu jedem Zeitpunkt ist die Chance, dass der Preis über seinem rationalen Wert liegt, ungefähr so groß wie die Chance, dass er darunter liegt.
- In jeder gegebenen Periode übertreffen etwa 50 Prozent aller Investoren den Benchmark-Index, und die übrigen 50 Prozent bleiben dahinter.
- Taleb rechnet bei einer Trefferwahrscheinlichkeit von 0,5 und 10.000 Managern nach fünf Jahren mit etwa 312 Firmen, die den Markt fünf Jahre in Folge geschlagen haben.
- Schlechte Wahrscheinlichkeitsurteile gehören neben ungenauen Risikoeinschätzungen und irrationalem Entscheidungsframing zu den drei Bereichen, in die sich die systematischen Abweichungen von der Rationalität einteilen lassen.
- Die Häufigkeitsverteilung eines Indikators auf Basis der Kanalnormierung hat die unerwünschte Eigenschaft, dass Extremwerte erheblich wahrscheinlicher sind als Werte in der Mitte der Spanne.
- Nach Ehlers liegt ein kanalnormierter Indikator nach Anwendung der Fisher-Transformation nahe an der Normalverteilung.
- Eine Normalverteilung hat die erwünschte Eigenschaft, dass Extremwerte selten sind, was sie für einen Indikator zur Erkennung seltener Extreme informativer machen kann.
- Ehlers liefert keine Daten, die diese Verteilungsbehauptung stützen; sie bleibt eine Vermutung, die weitere Untersuchung verdient.
- Die Stichprobenverteilung der mittleren Rendite der besten von N Regeln ist die Verteilung des Maximums von N Mitteln und liegt bei einem positiveren Wert als null.
- Die Bootstrap-Verteilung, die zu einem Backtest einer einzelnen Regel passt, ist dagegen bei null zentriert.
- Bei einem gewöhnlichen Signifikanztest wären etwa 320 der 6.402 Regeln auf dem Niveau 0,05 signifikant, genau die Zahl, die der Zufall vorhersagt.
- Über 15 Prozent annualisierte Rendite hätten in den Verteilungen der besten von 6.402 Regeln bei 0,05 signifikant gelegen, über 17 Prozent mit einem p-Wert unter 0,001.

## Funktionsweise

- Wird die Gauß-Annahme durch eine andere analytische Form mit endlich vielen Momenten ersetzt, etwa Students t für Fat Tails, folgt ein anderer optimaler Hebel; die Pareto-Levy-Verteilung hat nicht endlich viele Momente.
- Für manche Verteilungen gibt es keine analytische Lösung; dann hilft Monte Carlo.
- g(f) mittelt log(1 plus f mal R) über Ziehungen aus einer Verteilung der ungehebelten Strategierendite pro Bar.
- Bei gaußischem R lässt sich g(f) analytisch reduzieren, und das Maximum reproduziert Kelly.
- Die wahre Verteilung von R ist unbekannt; das Pearson-System bildet aus Mittelwert, Standardabweichung, Schiefe und Kurtosis eine von sieben analytischen Verteilungen, darunter Gauß, Beta, Gamma und Students t.
- Das sind nicht die allgemeinsten Verteilungen; höhere Momente können fehlen oder unendlich sein.
- Im Beispiel war der Pearson-Typ 4, also keine benannte Standardverteilung, und 100.000 Ziehungen dienten der Schätzung von g(f).

## Voraussetzungen


## Anwendung im Trading


## Regeln und Kriterien

- Bei Fat Tails soll die Wachstumsrate per Monte Carlo statt per Kelly optimiert werden.

## Risiken und Grenzen

- Die Fläche spricht für die Wahrscheinlichkeit des Belegs unter der Annahme, die Null sei wahr, nicht für die Wahrscheinlichkeit, dass die Hypothese wahr ist.

## Beispiele

- Im TU-Beispiel wird die Gauß-Null mit der Teststatistik 2,93 verworfen, besser als 99 Prozent. Die momentgleiche Simulation ohne die Korrelationen verwirft die Null nur mit 88 Prozent, weil 1.166 von 10.000 Reihen mindestens die beobachtete durchschnittliche Strategierendite erreichen.
- Die kritischen Werte der standardisierten Gauß-Teststatistik sind 1,282 bei p 0,10, 1,645 bei 0,05, 2,326 bei 0,01 und 3,091 bei 0,001.
- Die Monte-Carlo-Deutung einer auf 1 Prozent signifikanten erwarteten APR von 10 Prozent benutzt 10.000 simulierte Preisreihen derselben Länge und mit denselben ersten drei Momenten wie die historische Reihe. Nur 100 davon erreichen eine APR von mindestens 10 Prozent.
- Die alternative Deutung randomisiert die Einstiegstage. Nur eine von 100 Permutationen erreicht eine APR von mindestens 10 Prozent.
- In der Perlen-Schachtel sind Gesamtzahl sowie die Zahlen grauer und weißer Perlen unbekannt; F-G bezeichnet den Anteil grauer Perlen in der ganzen Schachtel.
- Der gesamte Inhalt darf nicht auf einmal betrachtet werden, deshalb ist F-G nicht direkt beobachtbar; diese Beschränkung erzeugt den Bedarf an statistischer Inferenz, weil die Vollerhebung in echten Problemen unmöglich oder unpraktisch ist.
- Erlaubt sind Stichproben von 20 Perlen, und es werden 50 Stichproben gezogen; f-g ist der Grauanteil einer Stichprobe.
- Ein Schieber am Boden trägt 20 Vertiefungen für je eine Perle und wird durch einen gleichen Schieber ersetzt, damit die übrigen Perlen nicht herausfallen.
- Nach dem Ablesen kommt die Stichprobe zurück, und die Schachtel wird gründlich geschüttelt, damit jede Perle dieselbe Chance hat, in die nächste Stichprobe von 20 zu gelangen; dadurch ist jede Stichprobe zufällig.
- Der Vorgang aus Ziehen, Notieren von f-g, Zurücklegen und Schütteln wird 50-mal wiederholt und liefert 50 verschiedene Werte von f-g, einen je Stichprobe.
- Im ersten Perlenexperiment kann f-g 21 Werte annehmen, von 0 bis 1,0. In den 50 Stichproben zu je 20 Perlen trat 0,50 neunmal auf, 0,55 achtmal, 0,60 zehnmal und der Wert 0,65 der ersten Stichprobe fünfmal. Werte von 0,40 bis 0,65 kamen oft vor, Werte unter 0,40 und über 0,65 fast nie.
- Der Balken für f-g gleich 0,60 hat die Anzahl 10, also 10 von 50 oder 20 Prozent der Beobachtungen, und damit auch 0,20 der Gesamtfläche.
- Die relative Häufigkeit von f-g gleich 0,60 ist 10/50 oder 0,20. Die relative Häufigkeit aller Werte von 0,65 und größer ist 0,10 plus 0,06 plus 0,02 plus 0,02, also 0,20.
- Nach 50 Stichproben ballen sich die f-g-Werte um einen zentralen Wert. Es liegt nahe, dass der unbekannte Anteil F-G irgendwo zwischen 0,40 und 0,65 liegt.
- Die Verteilung der ersten Schachtel ist nahe 0,55 zentriert, die der zweiten nahe 0,15. Die zweite streut enger, deshalb ist ihr Grauanteil mit größerer Sicherheit bekannt als der der ersten.
- Bei tausend Münzwürfen ist hoch vorhersagbar, dass die Zahl der Kopfwürfe in einer festgelegten Spanne um 500 liegt, während ein einzelner Wurf nicht vorhersagbar ist.
- Die Wahrscheinlichkeit von Kopf bei einer fairen Münze ist theoretisch 0,50. Zwei Seiten, Fairness und die geringe Chance, auf der Kante zu landen, genügen, ohne sie zehntausendmal zu werfen.
- Empirische Wahrscheinlichkeiten wie Neuschnee am Mount Hood im Juli oder ein Aktienanstieg nach einem Zinsrückgang von 2 Prozent lassen sich nur aus vergangenen Fällen derselben Bedingungen bestimmen. Ein Rückgang um 2 Prozent kann von 5 Prozent oder von 10 Prozent aus erfolgen, und diese Fälle teilen nur die genannte Bedingung.In den Abbildungen ist die Wahrscheinlichkeit, dass die stetige Zufallsvariable X zwischen A und B liegt, gleich 0,70, und die Wahrscheinlichkeit, dass sie B oder größer ist, gleich 0,15.
- Beim Signifikanztest einer vergangenen Rendite interessiert die Wahrscheinlichkeit, dass plus 10 Prozent oder mehr durch Zufall entstehen konnten, wenn die Regel keine Vorhersagekraft hat.
- Der systolische Blutdruck hängt von genetischen Faktoren, Ernährung, Gewicht, Lebensstil, aerober Kondition und vielen weiteren Faktoren ab. Wirken sie zusammen, hat der Blutdruck in einer großen zufällig ausgewählten Gruppe die glockenförmige Verteilung.
- Wäre die erwartete Rendite einer Regel wirklich null, kann die Wahrscheinlichkeit 0,03 betragen, dass der Backtest eine Rendite von plus 20 Prozent oder mehr liefert.
- Bei einer beobachteten mittleren Rendite von 15 Prozent könnte das 95-Prozent-Konfidenzintervall die wahre Rendite zwischen 5 und 25 Prozent eingrenzen. In einem anderen Beispiel ist die geschätzte Rendite 10 Prozent, mit einer Wahrscheinlichkeit von 95 Prozent für den Bereich von 5 bis 15 Prozent.
- Bei einer beobachteten Rendite von plus 3,5 Prozent und einem Flächenanteil von 0,10 ist der p-Wert 0,10.

## Unterschiedliche Quellenpositionen


## Eigene Erkenntnisse


## Quellen und Fundstellen

- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 19–38 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-002-p019-p038|S. 19–38]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 38–56 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-003-p038-p056|S. 38–56]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 206–225 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-015-p206-p225|S. 206–225]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 153–172 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-009-p153-p172|S. 153–172]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 172–191 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-010-p172-p191|S. 172–191]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 191–210 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-011-p191-p210|S. 191–210]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 210–229 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-012-p210-p229|S. 210–229]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 229–248 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-013-p229-p248|S. 229–248]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 248–267 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-014-p248-p267|S. 248–267]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 267–286 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-015-p267-p286|S. 267–286]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 286–305 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-016-p286-p305|S. 286–305]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 305–324 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-017-p305-p324|S. 305–324]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 324–343 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-018-p324-p343|S. 324–343]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 438–457 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-024-p438-p457|S. 438–457]]

## Verwandte Themen
