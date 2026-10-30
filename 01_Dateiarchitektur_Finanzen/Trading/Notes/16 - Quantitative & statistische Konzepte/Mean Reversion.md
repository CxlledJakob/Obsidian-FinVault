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
- Mean Reversion und Stationarität sind zwei äquivalente Sichtweisen derselben Preisreihe, führen aber zu zwei verschiedenen Tests.
- Mathematisch ist die Preisänderung der nächsten Periode proportional zur Differenz zwischen mittlerem Preis und aktuellem Preis; liegt der Preis darüber, folgt ein Abwärtsschritt, liegt er darunter, ein Aufwärtsschritt.
- Die in diesem Kapitel behandelte Form ist Time-Series-Mean-Reversion: der Mittelwert stammt aus der eigenen Preishistorie.
- Mean Reversion bedeutet, dass die Preisänderung proportional zur Differenz zwischen mittlerem Preis und aktuellem Preis ist.
- Stationarität bedeutet, dass Preise langsamer diffundieren als ein geometrischer Random Walk.
- Eine lineare Strategie bedeutet hier, dass die Zahl der Einheiten oder Stücke eines Einheitsportfolios proportional zum negativen Z-Score der Preisreihe dieses Portfolios ist, nicht dass der Marktwert der Anlage proportional zum Z-Score ist.

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
- Die Strategien werden grob in ein Mean-Reversion-Lager und ein Momentum-Lager geteilt, mit Standardtechniken für jede Kategorie und den grundlegenden Gründen, warum eine Strategie funktionieren sollte.
- Zur Erkennung von Time-Series-Mean-Reversion oder Stationarität dienen der Augmented-Dickey-Fuller-Test, der Hurst-Exponent, der Variance-Ratio-Test und die Half-Life.
- Über die mechanische Anwendung dieser Tests hinaus wird vermittelt, was sie wirklich prüfen, samt der einfachen mathematischen Gleichungen dahinter.
- Time-Series-Mean-Reversion und Cross-Sectional-Mean-Reversion werden unterschieden.
- Es wird gezeigt, ob Rohpreise, Log-Preise oder Verhältnisse die sinnvollsten Eingaben für die Tests und Strategien sind.
- Die Strategieperformance mean-revertet oft.
- Momentum- und Mean-Reversion-Strategien haben unter verschiedenen Marktregimes der jüngeren Finanzgeschichte diametral verschiedene Risiko-Rendite-Eigenschaften.
- Mean-Reversion-Strategien leben von einem hohen, aber konstanten Volatilitätsniveau.
- Nach der Krise 2008 sanken ihre Gewinne allgemein, weil die durchschnittliche Volatilität sank und plötzliche Ausbrüche häufiger wurden, darunter der Flash Crash im Mai 2010 und die Herabstufung der US-Bonität im August 2011.
- Die Dezimalisierung am 9. April 2001 senkte die Profitabilität vieler Statistical-Arbitrage-Strategien.
- Die meisten Preisreihen sind nicht mean-reverting, sondern geometrische Random Walks; gewöhnlich verteilen sich die Renditen, nicht die Preise, zufällig um einen Mittelwert von null.
- Mean Reversion der Renditen ist nicht handelbar; sie ist zu unterscheiden von der anti-seriellen Korrelation der Renditen, die handelbar ist und dasselbe ist wie die Mean Reversion der Preise.
- Die wenigen mean-reverting Preisreihen heißen stationär; geprüft wird das mit ADF-Test, Hurst-Exponent und Variance-Ratio-Test.
- Fertige stationäre Preisreihen öffentlich gehandelter Assets gibt es wenige; aus zwei oder mehr nicht mean-reverting Reihen lässt sich ein Portfolio bauen, dessen Nettomarktwert mean-reverting ist.
- Cross-sectional Mean Reversion heißt, dass die kumulierten Renditen der Instrumente eines Korbs zur kumulierten Korbrendite zurückkehren; die kurzfristigen relativen Renditen sind dann seriell antikorreliert.
- Die relative Rendite ist die Rendite des Instruments minus der Rendite des Korbs; das Phänomen tritt am häufigsten bei Aktienkörben auf und wird in Kapitel 4 behandelt.
- Der ADF-Test ist für Mean Reversion gebaut, Hurst-Exponent und Variance-Ratio-Test sind für Stationarität gebaut.
- Die Halbwertszeit misst, wie schnell eine Reihe zum Mittel zurückkehrt, und ist ein guter Prädiktor für Profitabilität oder Sharpe Ratio einer Mean-Reversion-Strategie auf dieser Reihe.
- Mean-Reversion-Strategien sind oft leicht zu konstruieren, weil man nicht auf von sich aus stationäre Instrumente beschränkt ist.
- Sie überspannen sehr verschiedene Zeithorizonte, von Market Making in Sekunden bis zu fundamentalen Anlegern, die unterbewertete Aktien jahrelang bis zum fairen Wert halten.
- Eine kurze Zeitskala bringt mehr Trades pro Jahr, höhere statistische Sicherheit, eine höhere Sharpe Ratio und letztlich eine höhere zusammengesetzte Rendite.
- Hinter einem mean-reverting Paar steht oft eine fundamentale Geschichte, im Gegensatz zu vielen Momentum-Strategien, deren einzige Rechtfertigung langsamere Anleger sind.
- Wahre Stationarität oder Kointegration ist nicht nötig: kurzfristige oder saisonale Mean Reversion lässt sich einfangen, wenn vor dem nächsten Gleichgewicht glattgestellt wird.
- Saisonal heißt, dass die Reihe nur in bestimmten Tagesabschnitten oder unter bestimmten Bedingungen zum Mittel zurückkehrt.
- Nicht jede stationäre Reihe ist profitabel, zum Beispiel bei einer Halbwertszeit von zehn Jahren.
- Preis-Spreads sind einfacher als Log-Preis-Spreads, und beide sind gerechtfertigt, wenn Preise und Logpreise kointegrieren.
- Das Verhältnis zweier Preise ist nur im Sonderfall betragsgleicher Hedge Ratios stationär.
- Ist das Paar nicht wirklich kointegriert, der Spread auf kurzer Frist aber mean-reverting, kann das Verhältnis besser passen als Preis- oder Log-Preis-Spread, weil es das Niveau der Preise ausblendet.
- Scaling-in erhöht das Kapital, je weiter der Preis vom Mittel abweicht, und nimmt schon kleine Rückläufe mit, auch wenn die Reihe nie wirklich zum Mittel zurückkehrt.
- Der Aktienmarkt ist theoretisch der fruchtbarste Boden für mean-reverting Instrumente; praktisch haben einfache Mean-Reversion-Strategien bei ETF-Paaren und Triplets bessere Ergebnisse als bei Aktien.
- Kurzfristig zeigen die meisten Aktien unter normalen Umständen, also ohne Nachricht, mean-reverting Eigenschaften, obwohl die Preise langfristig geometrischen Random Walks folgen; daraus wird eine kurzfristige oder saisonale Mean Reversion gebaut.
- Bei der Zeitreihen-Mean-Reversion kehren Preise zu einem aus der eigenen Historie bestimmten Mittel zurück; bei der querschnittlichen Mean Reversion kehren die kumulierten Renditen der Korbbestandteile zur kumulierten Rendite des Korbs zurück, und die Tests der Zeitreihen-Mean-Reversion sind dafür weitgehend irrelevant.
- Weil solche Muster leicht zu finden sind, ziehen sie viele Statistical Arbitrageure an, und die Renditen dieser Strategien sind allgemein gesunken.
- Preisreihen, die auf Tagesbars keine Mean Reversion zeigen, können in bestimmten Perioden starke Mean Reversion zeigen; das ist Saisonalität auf kurzer Zeitskala, und übliche Stationaritäts- oder Kointegrationstests erkennen sie schlecht.
- Ein Momentum-Filter auf Mean-Reversal-Strategien verbessert typischerweise deren Konsistenz.
- Währungen und Futures sind die Domäne von Momentum-Tradern, und die meisten CTAs sind momentum-basiert; die meisten Paare kointegrieren nicht, und die meisten Portfolios zeigen keine querschnittliche Mean Reversion.
- Gelegenheiten für Mean Reversion sind begrenzt, aber nicht inexistent; sie ist hier die Ausnahme, etwa beim Handel von Future-Kalender-Spreads.
- Kalender-Spreads mean-reverten in der Regel nicht, obwohl beide Beine denselben Basiswert verfolgen, weil die Roll-Rendite die Intuition durchkreuzt.
- Renditereihen mean-reverten im Gegensatz zu Preisreihen fast immer; hier wird nur die Roll-Return-Komponente betrachtet, deshalb kann es anders sein, auch wenn das Modell Spot- und Roll-Rendite als konstant ansetzt und sich auf langsam variierende Roll-Renditen anwenden lässt.
- Das Handelssignal eines Kalender-Spreads, definiert als Differenz der Logpreise bei gleich gehaltenem Marktwert der Beine, hängt überhaupt nicht vom Spot ab, sondern nur von der Roll-Rendite.
- Der Log-Marktwert eines Spreads mit langem Far- und kurzem Near-Kontrakt ist nach dem Preismodell γ mal (T1 minus T2) mit T2 größer als T1; die einfache Formel muss nicht gelten, wenn T2 minus T1 groß ist.
- Wegen der Rollrenditen muss Mean Reversion des Spotpreises nicht Mean Reversion des Futurespreises erzeugen.
- Mean Reversion von Futures-Kalenderspreads gehandelter Basiswerte hängt von der Mean Reversion der Rollrenditen ab.
- Futuresrenditen bestehen aus zwei Komponenten, den Spot-Renditen und den Rollrenditen.
- Backwardation bedeutet positive Rollrenditen, und ferne Kontrakte sind billiger als nahe Kontrakte; Contango bedeutet negative Rollrenditen, und ferne Kontrakte sind teurer als nahe Kontrakte.
- Gleichung 5.7 gilt nur für einen Future, dessen Basiswert ein gehandeltes Asset ist; VIX ist das nicht, und die Log-Preise der VX-Futures gegen die Restlaufzeit fallen nicht auf eine Gerade.
- Keine der alternativen Formeln, darunter Dupoyet, Daigler und Chen 2011, erklärt die Mean Reversion der VX-Kalenderspreads angesichts der fehlenden Mean Reversion des VX-Futures selbst.
- Ein ADF-Test auf dem Verhältnis Back zu Front von VX zeigt Stationarität mit 99 Prozent Wahrscheinlichkeit.
- Mean-reverting Futures-Intermarket-Spreads, also Paare aus verschiedenen Basiswerten, sind schwer zu finden.
- In einem bestimmten Markt mean-reverten oft nur Kalenderspreads bestimmter Monate und bestimmter Monatsabstände; diese marktabhängigen Details werden hier nicht verfolgt.
- Hurst-Exponent und Variance-Ratio-Test, in Kapitel 2 zur Erkennung von Mean Reversion beschrieben, dienen hier zugleich als Momentum-Tests.
- Dieselbe Reihe, hier TU, zeigt auf verschiedenen Zeitebenen Momentum und Mean Reversion.
- Eine Kombination aus Mean-Reversion- und Momentum-Regeln kann besser arbeiten als jede Strategie für sich.
- Momentum-Strategien haben gegenüber Mean-Reversion-Strategien diametral entgegengesetzte Ertrags- und Risikoeigenschaften, und profitable Momentum-Strategien haben tendenziell niedrigere Sharpe Ratios als Mean-Reversal-Strategien.
- Nach dem Ende des Kauf- oder Verkaufsdrucks der Fonds kehren die aus Liquiditätsgründen verschobenen Kurse oft zum Mittel zurück.
- Im Schlusskapitel wird die Regression zum Mittel als eine grundlegende Marktunvollkommenheit genannt, aus der sich eine einfache lineare Strategie bauen lässt.

## Funktionsweise

- Phi bestimmt, wie schnell der Einstiegspreis zur Prognose konvergiert.
- Die zufälligen Schocks sind unabhängig und standardnormal verteilt.
- Die Verteilung des Prozesses ist gaußsch.
- Mittelwert und Varianz hängen von phi, der Prognose, dem Einstieg und der Zahl der seit dem Einstieg verstrichenen Schritte ab.
- Der Preisprozess überträgt sich auf den Gewinn der Gelegenheit, weil der Gewinn die Positionsgröße mal der Preisänderung ist.
- Phi und Sigma werden geschätzt, indem der Prozess linear geschrieben und mit der Methode der kleinsten Quadrate angepasst wird.
- Phi ist dann die Kovarianz des nächsten Preises mit der verzögerten Abweichung von der Prognose, geteilt durch die Varianz dieser Abweichung.
- Sigma ist die Standardabweichung der Residuen der Kleinste-Quadrate-Schätzung.
- Im Ornstein-Uhlenbeck-Modell ist die Preisänderung dy im nächsten Zeitabschnitt dt proportional zur Differenz aus Mittelpreis und aktuellem Preis: dy(t) = (λy(t−1) + μ)dt + dε. Das Modell wird in Kapitel 2 erklärt.
- Ein Bollinger-Band verkauft, wenn der Preis eine Schwelle überschreitet, und kauft, wenn er darunter fällt.
- Ein lineares Modell kauft oder verkauft bei jedem Preisschritt, sodass der Marktwert ungefähr proportional zur negativen Abweichung vom Mittel ist. Das heißt Averaging-in oder Scaling-in und wird in Kapitel 3 behandelt.
- Für einen mean-reverting Prozess ist λ negativ, und der erwartete Preis fällt exponentiell auf minus μ/λ, mit der Halbwertszeit minus log(2)/λ.
- Ohne Drift und ohne Lag-Differenzen wird aus der diskreten Gleichung der Ornstein-Uhlenbeck-Prozess dy(t) gleich (λ y(t−1) plus μ) dt plus einem gaußschen Störterm.
- λ setzt die natürliche Zeitskala der Strategieparameter; ist die Halbwertszeit 20 Tage, soll der Lookback für Durchschnitt oder Standardabweichung nicht 5 Tage sein, und ein kleines Vielfaches der Halbwertszeit ist oft nahe am Optimum.
- Die lineare Strategie hält eine Stückzahl, die negativ proportional zur normalisierten Abweichung des Preises von seinem gleitenden Durchschnitt ist, also zum negativen Z-Score, und der Lookback kann gleich der Halbwertszeit gesetzt werden.
- Ein Einheitsportfolio, das nur eine Long- und eine Short-Position in zwei Instrumenten hält, heißt gewöhnlich Spread; die mathematische Form steht in Kapitel 3.
- Der Preis eines Einheitsportfolios ist sein Marktwert, wie bei einem Fonds oder ETF.
- Die Zahl der Einheiten ist der negative Z-Score des Einheitsportfolios, mit Lookback gleich der gerundeten Halbwertszeit.
- Für wirklich kointegrierende Reihen reichen lange Historie und OLS oder Johansen; ändert sich die Hedge Ratio, vermeidet der Kalman-Filter den abrupten Wechsel eines gleitenden Fensters.
- Schoenberg und Corwin vergleichen all-in bei L1, all-in bei L2 und average-in unter der Annahme, dass die Rückkehr nach F sicher ist und p konstant bleibt.
- Für den Mean-Reversion-Handel einer einzelnen Preisreihe liefert der Kalman-Filter den mittleren Preis und die Standardabweichung; die Hedge Ratio zweier kointegrierender Reihen wird dabei nicht gesucht.
- Aktien, die nur wenig gefallen sind, kehren eher um als solche, die stark gefallen sind, weil starke Fälle oft negative Nachrichten wie schlechte Gewinnmeldungen haben und solche Fälle seltener zurückkehren.
- Ein Kurs über einem langfristigen gleitenden Durchschnitt zieht Verkaufsdruck größerer Akteure wie Long-only-Fonds an, deren Horizont länger ist; dieser Liquiditätsbedarf kann den Abwärtsdruck übertreiben, und Preisbewegungen aus Liquiditätsbedarf kehren eher zurück als Bewegungen aus einer Verschiebung der Fundamentaldaten.
- Querschnittlich wird Unterperformance von Überperformance erwartet und umgekehrt; Gewinne werden nicht von jeder einzelnen Aktie erwartet, weil manche an manchen Tagen als Hedges dienen, sondern nur aggregiert.

## Voraussetzungen


## Anwendung im Trading

- Im ausbalancierten Markt mit Glockenkurve und Konsens über die Value ist eine Reversion-to-the-Mean-Strategie angemessen.
- Während des Übergangs von Mean Reversion zu Momentum werden die meisten Teilnehmer überrascht und machen kostspielige Fehler, und daraus entstehen Strategien mit günstigem Chance-Risiko-Verhältnis.
- Die einfachsten Techniken für mean-revertierende Portfolios sind lineare Modelle, Bollinger-Bänder und der Kalman-Filter.
- Der Kalman-Filter ist für Trader auf mehrere Arten und in mehreren Strategien nützlich.
- Beispiele stammen aus Interday- und Intraday-Aktienmodellen, ETF-Paaren und -Triplets, ETFs gegen ihre Komponentenaktien, Währungspaaren sowie Futures-Kalender- und Intermarket-Spreads.
- Fundamentale Überlegungen können das vorübergehende Auseinanderlaufen eines bisher sehr profitablen ETF-Paares erklären und zu einer verbesserten Fassung der Strategie führen.
- Bei Währungen kann schon die Renditeberechnung einem Aktienhändler fremd erscheinen, und Rollover-Zinsen können manchmal wichtig sein.
- Spot-Renditen und Roll-Renditen von Futures werden einander gegenübergestellt, und mehrere Futures-Strategien lassen sich aus einem einfachen mathematischen Modell der Futures-Preise ableiten oder verstehen.
- Backwardation und Contango werden grafisch und mathematisch dargestellt.
- Das Kapitel zur Mean Reversion von Währungen und Futures gipfelt im Volatility-Future VX, der die Grundlage einiger recht lukrativer Strategien bilden kann.
- Die lineare Mean-Reversion-Strategie auf dem CL-12-Monats-Kalenderspread erzielt vom 2. Januar 2008 bis zum 13. August 2012 eine ungehebelte annualisierte Rendite von 8,3 Prozent bei einer Sharpe Ratio von 1,3.
- Die übliche lineare Strategie auf VX mit dem Ratio als Signal und 15 Tagen Lookback für Durchschnitt und Standardabweichungen erzielt vom 27. Oktober 2008 bis zum 23. April 2012 eine annualisierte Rendite von 17,7 Prozent bei einer Sharpe Ratio von 1,5 und schnitt vor Oktober 2008 deutlich schlechter ab.
- Die Bollinger-Band-ähnliche Strategie shortet das Portfolio, sobald sein Wert um eine Standardabweichung der Trainingsresiduen abweicht, und erzielt vom 29. Juli 2010 bis zum 8. Mai 2012 eine annualisierte Rendite von 12,3 Prozent bei einer Sharpe Ratio von 1,4.
- Die lineare Mean-Reversion-Strategie auf dem Crack Spread zeigt negative Renditen in dem Zeitraum, in dem der Spread um den 9. März 2007 bis zum 3. Juli 2008 stark stieg und danach scharf fiel.
- Auf CL wird zum Schluss gekauft, wenn der Preis unter dem von vor 30 Tagen und über dem von vor 40 Tagen liegt, und umgekehrt für Shorts; ist keine Bedingung erfüllt, wird jede bestehende Position glattgestellt, mit einer annualisierten Rendite von 12 Prozent und einer Sharpe Ratio von 1,1.
- Ein Mean-Reversion-Filter auf der Strategie aus Beispiel 6.1 nimmt IBX an der MEFF, KT an der NYMEX, SXF an der DE, US an der CBOT, CD an der CME, NG an der NYMEX und W an der CME in Tabelle 6.2 auf und verbessert Rendite und Sharpe Ratio der dort schon enthaltenen Kontrakte.
- Aktien mit dem stärksten Verkaufsdruck in den Quartalen t minus 4 bis t minus 1 zu kaufen und umgekehrt liefert weitere 7 Prozent annualisiert.
- Momentum, Front-Running und Mean Reversion zusammen ergeben vor Kosten etwa 41 Prozent.
- Das lineare Mean-Reversion-Modell für S&P-500-Aktien aus Kapitel 4 hält weniger als einen Tag und hat eine Sharpe Ratio von 4,7.
- Momentum-Strategien zu einem Portfolio aus Mean-Reversion-Strategien hinzuzufügen ergibt höhere Sharpe Ratios und kleinere Drawdowns als jeder Strategietyp allein.

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
- Ist λ positiv, soll keine Mean-Reversion-Strategie versucht werden; liegt λ sehr nahe bei null, ist die Halbwertszeit so lang, dass wenige Round-Trips die Strategie wenig profitabel machen.
- Die statistischen Tests verlangen mindestens 90 Prozent Sicherheit, im praktischen Handel genügt oft deutlich weniger.
- Auch eine als stationär bezeichnete Reihe mit Hurst-Exponent zwischen 0 und 0,5 hat eine mit der Zeit steigende Varianz, nur langsamer als ein geometrischer Random Walk; gleitender Durchschnitt und gleitende Standardabweichung passen sich dem an.
- Der Mittelwert wird meist als fest angenommen, kann sich in der Praxis aber langsam ändern, etwa durch die Wirtschaft oder das Unternehmensmanagement.
- Die praktische Bollinger-Fassung steigt erst jenseits von entryZscore Standardabweichungen ein und bei einem kleineren exitZscore aus; zu jedem Zeitpunkt liegt null oder eine Einheit im Markt.
- exitZscore gleich 0 ist der Ausstieg am aktuellen Mittel, exitZscore gleich minus entryZscore der Ausstieg jenseits des gegenüberliegenden Bands.
- Kurzer Lookback und kleine Z-Score-Beträge verkürzen die Haltedauer, vermehren die Round-Trips und erhöhen in der Regel den Gewinn.
- Feste Stückzahlen während des Trades verlangen Hedge Ratios aus der Preisreihe, feste Marktwerte je Bestandteil Hedge Ratios aus der Log-Preisreihe.
- Bei Währungspaaren ist oft das Ratio statt des Spreads der Indikator.
- Variieren Hedge Ratio, Mittel und Standardabweichung eines Spreads künftig, werden ein gleitender Look-back oder der Kalman-Filter genutzt.
- Eine praktische lineare Umsetzung sind Bollinger-Bänder mit Scaling-in; Scaling-in ist live oft nützlich, weil Volatilitäten und Wahrscheinlichkeiten sich ändern, auch wenn es im Backtest nicht optimal ist.
- Der Stop-Loss soll größer sein als der maximale Intraday-Drawdown des Backtests, damit er im Backtest nie auslöst, die gemessene Performance nicht verändert und ein künftiges Black-Swan-Ereignis nicht in den Ruin führt.
- Momentum-Strategien profitieren logisch vom Stop-Loss: Verluste bedeuten gedrehtes Momentum, also Ausstieg und vielleicht Umkehr der Position.
- Ein fortlaufend aktualisiertes Momentum-Signal ist ein De-facto-Stop-Loss; deshalb haben Momentum-Modelle nicht dasselbe Tail-Risiko wie Mean-Reversion-Modelle.

## Risiken und Grenzen

- Wer über Mean Reversion handelt, bleibt nicht profitabel, wenn Abweichungen von der Value zusätzliches Volumen anziehen und die Value neu gesetzt wird.
- Ein nur aus dem Preis gebauter Durchschnitt zeigt die Wanderung des Means unvollständig.
- Vorübergehende Schocks können den wahren Wert über Tage oder über Jahre verdecken.
- Scaling-in hat Vor- und Nachteile, und Datenfehler sind bei Mean-Reversion-Strategien gefährlich, besonders bei solchen, die mit Spreads arbeiten.
- Der Aufstieg von Dark Pools und Hochfrequenzhandel macht den Handel mancher dieser Strategien in den letzten Jahren recht herausfordernd.
- Survivorship Bias ist für mean-revertierende Long-only-Aktienstrategien gefährlicher als für mean-revertierende Long-Short- oder Short-only-Strategien.
- Konsolidierte historische Preise blähen den Backtest eines mean-revertierenden Modells auf, weil wenige Stücke abseits der Primärbörse fern vom Auktionspreis ausgeführt werden können und die Preise des nächsten Tages von diesem Ausreißer gewöhnlich zurücklaufen.
- Schluss und Eröffnung an den US-Primärbörsen entstehen immer durch eine Auktion. Ein Schlussgeschäft an einer Zweitbörse ist keine Auktion.
- Hoch- und Tiefkurse der Historie sind meist konsolidiert und oft übertrieben durch kleine Geschäfte an Zweitbörsen. Der Backtest bläht sich auf, wenn sie verwendet werden.
- Der Backtest eines mean-revertierenden Aktienmodells auf Schlusskursen kann ausgezeichnet aussehen. Eine Abwertung der Ergebnisse ist zu erwarten, wenn erneut mit Daten der Primärbörse getestet wird.
- Ein mean-revertierender Intraday-Futures-Spread kann im Backtest sehr gut und live sehr schlecht abschneiden, wenn barbasierte statt tickbasierte Daten verwendet wurden.
- Ein nichtstationärer Preis muss von einer Mean-Reversion-Strategie nicht abschrecken, und komplizierte Indikatoren sind nicht nötig, um aus einer mean-reverting Reihe Gewinne zu ziehen.
- Die einfachste lineare Strategie ist unpraktisch, weil das Höchstkapital unbekannt ist und infinitesimale Stückzahlen nicht handelbar sind.
- Die hohe Stetigkeit wiegt Trader in Überkonfidenz und zu viel Leverage ein (Dever, 2011; Long Term Capital Management).
- Der Bruch kommt oft beim maximalen Leverage nach einer Erfolgsserie und aus einem erst im Nachhinein sichtbaren fundamentalen Grund; der seltene Verlust kann katastrophal sein.
- Risikomanagement ist hier besonders wichtig und besonders schwierig, weil die üblichen Stop-Losses sich nicht logisch einsetzen lassen; warum, und welche Verfahren passen, steht in Kapitel 8.
- Momentum-Strategien setzen darauf, dass es größere Narren gibt; diese holen irgendwann auf, und die Strategie kann eines Tages ohne Erklärung aufhören zu funktionieren.
- Die lineare Strategie ist unpraktisch wegen ständigen infinitesimalen Rebalancings und unbegrenzter Kaufkraft.
- Unter konstantem p ist average-in nie am profitabelsten; die Schwelle zwischen den beiden All-in-Regeln ist (F minus L1) geteilt durch (F minus L2).
- Ist die Volatilität und damit p nicht konstant, kann Scaling-in außer Stichprobe eine bessere realisierte Sharpe Ratio liefern und ist in der Stichprobe trotzdem nie optimal.
- Datenfehler oder Ausreißer in historischen Daten blähen in der Regel die Backtest-Performance von Mean-Reversion-Strategien auf und unterdrücken zugleich die von Momentum-Strategien.
- Dieselben Fehler lösen im Live-Handel falsche Trades aus und führen oft zu realen Verlusten.
- Strategien auf Spreads sind besonders empfindlich gegen kleine Datenfehler, im Backtest wie im Live-Handel, weil die Quote-Differenz meist viel kleiner ist als die Quotes selbst und der prozentuale Fehler im Spread dadurch viel größer wird.
- Schlechte Ticks in Live-Daten lösen auch bei Momentum-Strategien falsche Orders aus und sind für deren Ausführung ebenso verlustbringend.
- Tägliche Einzelaktien sind fast nie stationär: einmal weggegangen, kehren sie selten zum Start zurück; Intraday- und saisonale Mean Reversion sind Sonderfälle.
- Ein Portfolio vieler Aktienpaare wird vom Gesetz der großen Zahlen nur gerettet, wenn die erwartete Out-of-Sample-Rendite je Paar positiv ist; der Autor fand das nicht, weil die kleinen Gewinne guter Paare von den großen Verlusten schlechter Paare überwogen wurden.
- Saisonalität ist an Rohstoffmärkten oft ausgeprägt, sodass in einem Markt nur Kalender-Spreads bestimmter Monate und bestimmter Abstände mean-reverten; diese marktabhängigen Details werden hier nicht verfolgt.
- Alternative Formeln für den VX-Future, etwa Dupoyet, Daigler und Chen 2011, erklären nach dem Befund des Autors die mean-reverting Eigenschaft der VX-Kalender-Spreads nicht.
- Der Crack Spread ist im ADF vom 20. Mai 2002 bis zum 4. Mai 2012 nicht mean-reverting.
- CL und BZ im Verhältnis 1:1 sind weit von stationär entfernt, weil BZ CL anhaltend geschlagen hat.
- Als wahrscheinliche Ursachen dieser BZ-Outperformance nennt der Text die steigende US-Ölproduktion nach Friedman 2012, den Pipeline-Engpass in Cushing nach Philips 2012 und geopolitische Faktoren wie das Embargo gegen iranisches Öl 2012, das Europa und damit BZ stärker traf als die USA.
- Eine andere VX-gegen-ES-Strategie, die nicht auf der Mean Reversion des Spreads VX-ES beruht, wird als Momentum-Strategie im nächsten Kapitel behandelt.
- Nach dem Börsenkrach 2008 bis 2009 verschwindet das querschnittliche Aktienmomentum und wird durch starke Mean Reversion ersetzt; wie lange dieses Mean-Reversion-Regime dauert, ist offen.
- Nach dem Krach von 1929 erreichte eine repräsentative Momentum-Strategie ihren Höchststand mehr als 30 Jahre lang nicht wieder.
- Stop-Losses sind mit Mean-Reversion-Strategien nicht verträglich, weil sie ihren Einstiegssignalen widersprechen; das wird in Kapitel 8 wieder aufgenommen.
- Mit einer einzigen Mean-Reversion-Position kann ein enormer Drawdown entstehen.
- Das Aufwärtspotenzial ist durch die natürliche Gewinnobergrenze am Mittel begrenzt, das Abwärtspotenzial kann unbegrenzt sein.
- Ob ein Stop-Loss für Mean-Reversion-Strategien sinnvoll ist, ist umstritten, weil er der zentralen Annahme zu widersprechen scheint.
- Fällt der Preis nach dem Long-Einstieg weiter, erwartet Mean Reversion einen späteren Anstieg; der Ausstieg am Tief wirkt dann nicht sinnvoll.
- Der Autor hat nie eine Mean-Reversion-Strategie gebacktestet, deren APR oder Sharpe Ratio durch einen Stop-Loss stieg.
- Das Argument scheitert, wenn das Modell während der Position dauerhaft aufhört zu arbeiten.
- Eine bisher mean-reverting Reihe kann für lange Zeit, vielleicht für immer, zu einer Trendreihe werden, weil finanzwirtschaftliche Zusammenhänge anders als physikalische Gesetze nicht unveränderlich sind.
- Dann verhindert der Stop-Loss katastrophale Verluste und gibt Zeit zu prüfen, ob die Strategie vor einem Verlust von 100 Prozent abgeschaltet werden sollte.
- Solche Reihen, die von Mean Reversion zu Momentum wechseln, fehlen im Katalog profitabler Mean-Reversion-Strategien, weil gescheiterte Backtests nicht aufgenommen wurden.

## Beispiele

- Beispiel 4.2 ist eine lineare Mean-Reversion-Strategie zwischen einem ETF und seinen Komponentenaktien. Die Beispiele 4.3 und 4.4 sind zwei lineare Long-Short-Statistical-Arbitrage-Strategien auf Aktien.
- Die Einfachheit dieser Modelle soll zeigen, dass die Gewinne aus einer offenliegenden Marktineffizienz kommen und nicht aus subtiler Kompliziertheit der Strategie.
- Für USD.CAD ist die ADF-Statistik etwa minus 1,84 gegen einen 90-Prozent-Wert von minus 2,594, Stationarität lässt sich nicht zeigen.
- λ ist bei USD.CAD negativ, die Reihe trendet also zumindest nicht, und die Halbwertszeit beträgt etwa 115 Tage.
- EWA und EWC kointegrieren, weil beide Volkswirtschaften von Rohstoffen dominiert werden; GDX und GLD kointegrieren, weil der Wert der Goldbergbauer am Gold hängt.
- GDX und GLD fielen Anfang 2008 auseinander, weil hohe Energiepreise den Abbau ungewöhnlich teuer machten.
- Das EWA-EWC-IGE-Portfolio hat 23 Tage Halbwertszeit gegen 115 Tage bei USD.CAD und im linearen Backtest 12,6 Prozent APR bei einer Sharpe Ratio von 1,4.
- GLD und USO sind trotz der Inflationsgeschichte nicht kointegriert; der adaptive Preis-Spread erreicht trotzdem etwa 10,9 Prozent APR und eine Sharpe Ratio von etwa 0,59, der Log-Spread 9 Prozent und 0,5, das Verhältnis eine negative APR.
- Die Bollinger-Strategie auf diesem Spread mit entryZscore 1 und exitZscore 0 erreicht 17,8 Prozent APR und eine Sharpe Ratio von 0,96.
- Der Kalman-Filter auf EWA und EWC erreicht 26,2 Prozent APR und eine Sharpe Ratio von 2,4.
- Aus 10 und 5 gegenüber 100 und 50 bleibt das Verhältnis 2, während der Spread von 5 auf 50 steigt.
- EUR.GBP ist ein Verhältnis aus EUR.USD und GBP.USD; für MXN.NOK kann das Verhältnis wirksamer sein, weil das Kreuz nicht wirklich stationär ist.
- Bei wahren Preisen von je 100 Dollar und einer Historie von 100, 110 und 100 Dollar shortet die Mean-Reversion-Strategie im Backtest bei 110 Dollar und deckt bei 100 Dollar ein, mit einem fiktiven Gewinn von 10 Dollar.
- Ein wahrer Spread von 5 Dollar, der durch einen falschen Ask auf 6 Dollar steigt, liegt 20 Prozent über dem realen Spread und kann eine fehlerhafte Order zum Kauf von X und Verkauf von Y auslösen.
- Der Autor sah mit dem Datenfeed eines Brokers bei einer Aktienpaar-Strategie regelmäßig unerklärliche Verlusttrades; nach dem Wechsel auf Yahoo-Echtzeitquotes und später auch mit Bloombergs Live-Feed traten diese schlechten Trades nicht mehr auf.
- Der 12-Monats-Log-Kalender-Spread von CL ist im ADF mit 99 Prozent stationär, Halbwertszeit 36 Tage; die lineare Strategie hat vom 2. Januar 2008 bis 13. August 2012 eine APR von 8,3 Prozent und eine Sharpe Ratio von 1,3.
- Der VIX ist mean-reverting und im ADF mit 99 Prozent stationär, die back-adjustierten VX-Front-Month-Preise mean-reverten aber nicht; Mean Reversion von VX zeigt sich erst nach den Volatilitätsspitzen um den 20. November 2008, den 20. Mai 2010 und den 3. Oktober 2011, sonst fällt die Reihe unaufhaltsam.
- Gleichung 5.7 gilt nur für einen Future, dessen Basiswert ein gehandeltes Asset ist; der VIX ist keines, und die Logpreise der VX-Futures gegen die Restlaufzeit fallen nicht auf eine Gerade.
- Die Monte-Carlo-Rechnung zum Hebel verwendet die Mean-Reversion-Strategie aus Beispiel 5.1: Kelly 18,4, Monte-Carlo-Optimum 19, historisch 18,4, schlechteste Periodenrendite minus 0,0331.

## Unterschiedliche Quellenpositionen

- Die Aussage, ein Stop-Loss senke immer die Performance von Mean-Reversion-Strategien, ist durch Survivorship Bias verzerrt.
- Genauer senkt er die Performance, solange die Preise mean-reverting bleiben, und verbessert sie, wenn ein Regimewechsel zum Trend einsetzt.
- Jede erfolgreich gebacktestete Mean-Reversion-Strategie trägt diesen Bias und zeigt bei aufgezwungenem Stop-Loss schlechtere Backtest-Performance.

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
