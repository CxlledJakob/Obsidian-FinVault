---
typ: wissen
status: entwurf
hauptthema: "[[Trading/Notes/17 - Risikomanagement/17 - Risikomanagement|17 - Risikomanagement]]"
weitere_hauptthemen: []
unterthema: "Verlustrisiko"
priorität: A
aliases: []
voraussetzung: []
verwandt: []
quellen: []
erstellt: 2026-10-26
aktualisiert: 2026-10-30
---

# Stop-Loss


## Kurzdefinition

- Der Stop-Loss ist die untere horizontale Barriere und eine dynamische Funktion der geschätzten Volatilität.
- Der Stop-Loss ist die negative Schwelle, bei deren Erreichen die offene Gelegenheit mit Verlust geschlossen wird.
- Der Stop-Loss ist die Bedingung, eine Position mit Verlust zu schließen.
- Der Stop-Loss dieses Kapitels ist der erste schützende Stop. Er steht immer genau an dem Preis, der das Setup ungültig macht.

## Kernaussagen

- Nach einem Bruch durch eine Decke kann der Stop-Loss in den unteren Bereich der Preisstauzone gelegt werden.
- Der neue Boden ist der natürliche Schutz bei einem Rücktest. Ein Weg zurück durch diese Zone bräuchte Aufwand und Volumen.
- Abwärts wird die neue Decke zum Schutz gegen einen kurzen Rücksetzer, und der Stop liegt sinngemäß jenseits dieser neuen Barriere.
- Der Stop unter dem Docht eines Hammers wird vom Markt gesetzt.
- Nach der Shooting-Star-Folge liegt der Stop der Short-Position über dem Docht der ersten Shooting-Star-Kerze.
- Die sichtbaren Stauzonen aus Volume at Price helfen beim Platzieren der Stops. Risiko- und Geldmanagement geben die Regeln vor.
- Nach dem Bruch einer langen Stauzone liegt der Stop unter dem letzten Pivot-Tief, weil darunter ein tiefes natürliches Schutzpolster steht.
- Der beste Platz ist die andere Seite der Stauzone, hinter der Barriere, die der Markt selbst gebaut hat.
- Ist im aufsteigenden Dreieck die Decke zur Unterstützung geworden, ist das die natürliche Barriere für den Stop.
- Das Risiko des Trades ist niedriger, wenn mit dem dominanten Trend der langsameren Zeitebene gehandelt wird, und höher, wenn dagegen gehandelt wird.
- Jede Anlagestrategie hat Stop-Loss-Grenzen, ob der Portfolio-Manager sie selbst setzt, die Risikoabteilung sie erzwingt oder ein Margin Call sie auslöst.
- Gewinne aus Positionen zu modellieren, die an der Börse ausgestoppt worden wären, ist unrealistisch.
- Stop-Loss und Gewinnmitnahme sollen vom Risiko der Wette abhängen.
- Wird die untere Barriere zuerst berührt, ist das Label -1.
- Die Breite der unteren Barriere ist der Faktor ptSl[1] mal dem Ziel trgt.
- Ist dieser Faktor 0, gibt es keine untere Barriere.
- Soll die Seite der Wette gelernt werden, sind die horizontalen Barrieren symmetrisch oder sie entfallen, weil Stop und Gewinnziel ohne Seite nicht unterscheidbar sind.
- Ist die Seite bekannt, wie beim Meta-Labeling, lassen sich Gewinnmitnahme und Stop-Loss unterscheiden, und die horizontalen Barrieren müssen nicht symmetrisch sein.
- Die Stop-Schwelle entspricht einer horizontalen Barriere des Meta-Labeling.
- Bei Prognose null und kurzer Halbwertszeit ist der optimale Stop weit und lässt nicht realisierte Verluste bis zum Fünf- oder Siebenfachen des kleinen Gewinnziels zu.
- Bei Prognose null und kurzer Halbwertszeit ist ein kurzer Stop zusammen mit einem hohen Gewinnziel die schlechteste Regel.
- Bei Prognose 5 und Halbwertszeit 5 liegen die guten Stops zwischen 4 und 10.
- Bei Prognose 5 und Halbwertszeit 10 liegen die guten Stops zwischen 7 und 10.
- Bei Prognose 5 und Halbwertszeit 25 liegen die guten Stops zwischen 9 und 10.
- Ist ein Gewinnziel vorgegeben, wird der passende Stop aus den simulierten Pfaden bestimmt.
- Ist ein maximaler Stop vorgegeben, wird dazu das passende Gewinnziel bestimmt.
- Bei Prognose minus 5 und Halbwertszeit 5 liegt die schlechteste Region um einen Stop von 6, mit Gewinnzielen zwischen 4 und 10.
- Bei Prognose minus 5 und Halbwertszeit 5 markiert das Rechteck die schlechteste Performance.
- Die schlechteste Region bei negativer Prognose ist das gedrehte Gegenbild der besten Region bei positiver Prognose.
- Mit steigender Halbwertszeit spreizt sich das schlechteste Gebiet, und die negativen Sharpe Ratios werden flacher.
- Eine schon bestehende Position mit erwartetem Verlust braucht einen Stop, der diesen Verlust begrenzt.
- Ein rationaler Teilnehmer eröffnet keine neue Position, wenn der erwartete Ausgang ein Verlust ist.
- Auch ohne gesetzten Stop besteht eine implizite Grenze durch einen Margin Call oder durch einen nicht mehr tragbaren Buchverlust.
- Im asymmetrischen Modell liegt die Verlustauszahlung unter der Gewinnauszahlung.
- Wird die Verlustauszahlung bei gleichem Gewinnziel negativer, steigt die Trefferwahrscheinlichkeit, die für eine Ziel-Sharpe-Ratio nötig ist.
- Wird die Verlustauszahlung negativer, steigt auch die Wettfrequenz, die bei gleicher Trefferwahrscheinlichkeit für die Ziel-Sharpe-Ratio nötig ist.
- Verlustschwelle, Gewinnschwelle und Wettfrequenz setzt der Portfoliomanager, während die Trefferwahrscheinlichkeit vom Markt kommt.
- Stop-Losses gehören mit schwarzen Schwänen und Constant Proportion Portfolio Insurance zu der praktischen Erfahrung, mit der die Kelly-Formel im Risikomanagement gemildert wird.
- Der Stop-Loss ist neben dem zeitbasierten Ausstieg eine der zwei üblichen Ausstiegsarten für Momentum-Strategien.
- Er kann die Ausstiegsbedingung selbst oder eine zusätzliche Ausstiegsbedingung sein.
- Stop-Losses sind mit Momentum-Strategien voll verträglich: wechselt das Momentum die Richtung, wird die Gegenposition eröffnet, die ursprüngliche Position hat verloren, und der neue Einstieg hat als Stop-Loss gewirkt.
- Stop-Losses sind mit Mean-Reversion-Strategien nicht verträglich, weil sie deren Einstiegssignalen widersprechen; das wird in Kapitel 8 wieder aufgenommen.
- Durch einen zeitbasierten Ausstieg oder einen Stop-Loss ist der Verlust einer Momentum-Position immer begrenzt, und das Abwärtspotenzial einer Momentum-Strategie ist begrenzt.
- Das Auslösen von Stops ist eine zusätzliche Momentum-Ursache vor allem auf kurzen Horizonten und führt oft zu Breakout-Strategien.
- Viele Stop-Orders liegen auf oder nahe Unterstützung und Widerstand, einschließlich runder Zahlen nahe dem aktuellen Preis.
- Stop Hunting stützt sich auf genau diese Orders.
- Das Buch lehrt, optimale Handelsbedingungen zu erkennen, objektive Einstiegsstrategien mit dem exakten Einstiegs- und Ausstiegspreis und das Führen des Trades mit Stop-Loss-Anpassungen bis zum Ausstieg.
- Die Strategien in Kapitel 6 sollen jedes Raten beseitigen, zu welchem Preis ein Markt betreten wird und welcher Stop-Loss-Preis gelten soll.
- Kapitel 7 lehrt, alle praktischen Strategien anzuwenden: vom Erkennen der Setups hoher Wahrscheinlichkeit über die konkrete Einstiegsstrategie und die Stop-Loss-Anpassung bis zur Ausstiegsstrategie.
- Die zweite tägliche bärische Momentumumkehr, nur einen Tag nach dem Swing-Tief im März, hätte je nach Einstieg und anfänglichem Schutz-Stop zu keinem Trade oder zu einem Verlust geführt.
- Ist eine Momentumumkehr des Indikators Teil des Tradingplan-Setups, bevor ausgeführt werden darf, müssen die Stops bei einer relativ langen Lookback-Periode typischerweise weit vom Einstiegspreis entfernt liegen.
- Der Zweck aller Handelsstrategien ist, Bedingungen mit einem Ergebnis hoher Wahrscheinlichkeit und akzeptablem Kapitaleinsatz zu identifizieren.
- Das Geschäft des Tradings ist, Bedingungen mit einem Ergebnis hoher Wahrscheinlichkeit und akzeptablem Kapitaleinsatz zu identifizieren.
- Man wird nicht immer recht haben, soll es aber die meiste Zeit sein, und wenn nicht, sollen die Kosten akzeptabel sein.
- Strategien sind wichtig, um Verluste zu begrenzen, wenn Daten, Strategie und Plan nicht wie erwartet aufgehen.
- Handelsstrategien und Handelsmanagement sind genauso wichtig wie die technische Analyse, die das Setup hoher Wahrscheinlichkeit identifiziert.
- Später im Buch folgen konkrete Strategien von Einstieg bis Ausstieg, die Verluste klein halten, wenn ein Setup scheitert, und Gewinne vergrößern, wenn es aufgeht.
- Erfolgreiche Trader haben immer einen relativ engen Stop. Ein damit entstandener Verlust ist akzeptabel. Verluste zu minimieren, ist absolut entscheidend.
- Sobald die Hochwahrscheinlichkeitsbedingungen erkannt sind, bestimmen Marktposition und Einstiegsstrategie den Einstiegspreis und den anfänglichen Schutz-Stop-Loss. Das maximale Kapitalrisiko je Einheit ist vor der Ausführung bekannt.

## Funktionsweise

- Der Markt legt mit seinem eigenen Preisverhalten die Barriere, die eine plötzliche Richtungsänderung erst überwinden muss. Deshalb ist Ausbruchshandel verbreitet.
- Das Volumen des Bruchs entscheidet, ob dieser Schutz real ist. Ein Bruch auf niedrigem Volumen ist eine Falle und liefert keinen verlässlichen Stop-Anker.
- Die alten Zonen bleiben als Karte liegen und zeigen später, wo ein Stop an historischem Kampf, an Umkehr oder an Unterstützung orientiert werden kann.
- Bei positivem Faktor liegt der Stop auf dem Negativen von ptSl[1] mal trgt.
- Gemessen wird das an der Pfadrendite, die mit der Positionsseite multipliziert wurde.
- Der Stop-Zeitpunkt ist der früheste Index, an dem diese Pfadrendite unter der Stop-Schwelle liegt.
- Die Vorgabewerte für die Grenzen stammen aus der Tagesvolatilität von getDailyVol.
- Über Nacht oder am Wochenende können Stops auf verschiedenen Preisen an der Eröffnung gleichzeitig ausgelöst werden.
- Die Ausführung kann kaskadieren und weiter vom Open entfernte Stops ebenfalls auslösen.
- Nach einem Bruch der Unterstützung werden Verkaufs-Stops ausgelöst und treiben den Preis weiter nach unten.
- High-Frequency-Händler legen nahe der Unterstützung große Sell Orders, um diese Stops auszulösen, und decken danach die Shorts.
- Die übliche Verwendung schließt eine einzelne Position, wenn ihr unrealisiertes Ergebnis unter eine Schwelle fällt, und erlaubt später einen neuen Einstieg, auch in dieselbe Richtung; die kumulierte Strategie-P&L ist dabei nicht der Gegenstand.
- Die seltenere Verwendung schließt die ganze Strategie, wenn der Drawdown unter eine Schwelle fällt; das kann nur einmal im Leben der Strategie vorkommen und soll idealerweise nie eintreten.
- Für denselben Schutz des Maximal-Drawdowns wird deshalb CPPI vorgezogen.
- Er hält das Verlustlimit nur ein, wenn der Markt während der Position offen ist, etwa ohne Overnight-Positionen oder in Währungen und manchen Futures, die außer an Wochenenden und Feiertagen elektronisch offen sind.
- Eine objektive Ausstiegsform zieht den Stop nach einer Momentum-Umkehr am One-Bar-High oder One-Bar-Low nach.

## Voraussetzungen


## Anwendung im Trading

- Eine starke sichtbare Plattform hilft, das Risiko zu beurteilen. Ist sie schwach, kann der Einstieg warten.
- Eine schon bestehende Position, deren erwartetes Ergebnis ein Verlust ist, braucht einen Ausstieg, der diesen Verlust begrenzt.
- Ein rationaler Marktteilnehmer eröffnet keine Position, deren erwartetes Ergebnis ein Verlust ist.
- Weil Devisen von Sonntag 17:00 Uhr ET bis Freitag 17:00 Uhr ET nahezu durchgehend gehandelt werden, lassen sich Stop-Losses dort sinnvoll einsetzen.

## Regeln und Kriterien

- Ein Rücklauf über das Bracket-Extrem hinaus soll den Ausstieg auslösen.
- Den Trade aus eigenem Entschluss beenden, statt zu warten, bis Stops einen herausnehmen.
- Beginnt die anfängliche Zuversicht eines Open-Drive nachzulassen, ist das der Anlass zum Ausstieg.
- Beim Balance-Area-Bruch liegt der Ausstiegsstop ein paar Ticks jenseits des Bruchpunkts, weil die Rückkehr in die Area die Ablehnung anzeigt.
- Beim Gap-Trade liegt der Stop dort, wo eine Preisrotation die Gap vollständig durchhandelt und damit löscht.
- Fehlt die Folge, wird mit kleinem Verlust ausgestiegen, sobald der Preis zurück in die Balance-Area handelt.
- Stops werden an zuvor bekannte Referenzpunkte gelegt.
- Ausgestiegen wird, sobald Bedingungen entstehen, die der angenommenen Marktstimmung widersprechen.
- In der Konfiguration [1,1,1] gibt es neben Gewinnziel und Haltedauer eine maximale Verlusttoleranz.
- In der Konfiguration [0,1,1] endet die Position nach einer Anzahl Bars, sofern sie nicht vorher ausgestoppt wird.
- Die Konfiguration [0,1,0] hält ausschließlich bis zum Stop und gilt als ziellos.
- Die Konfigurationen [1,0,1] und [1,0,0] führen die Position ohne Rücksicht auf zwischenzeitliche nicht realisierte Verluste.
- Für Mean Reversion wird er größer gesetzt als der maximale Intraday-Drawdown des Backtests, sodass die Backtest-Performance unverändert bleibt und ein Black Swan künftig nicht in den Ruin führt.
- Bei Momentum ist er logisch, weil Verluste gedrehtes Momentum anzeigen und Ausstieg oder Umkehr nahelegen.
- Ein fortlaufend aktualisiertes Momentum-Signal ist ein De-facto-Stop-Loss; Momentum-Modelle haben deshalb nicht dasselbe Tail-Risiko.
- Nur CPPI oder ein Stop-Loss können garantieren, dass der künftige Drawdown ein vorgegebenes Maximum nicht überschreitet.
- Die Key Points nennen ihn als Schutz vor Black Swans trotz meist schlechterer Mean-Reversion-Backtests, fordern, dass er im Backtest nie auslöst, und sehen ihn bei Momentum als natürlichen Bestandteil.
- Wird das Extrem von Wave-B genommen, ist das korrektive Hoch oder Tief eher wahrscheinlich abgeschlossen, und daraus wird je nach Hoch oder Tief von Wave-B ein entschiedenes Long- oder Short-Signal.
- Der Stop dieses Signals liegt nicht jenseits des möglichen Extrems von Wave-C.
- Was der Markt tun kann, um die Bedingung des Trades aufzuheben, ist die Stelle des Stops. Wird sie erreicht, wird schnell mit akzeptablem Verlust ausgestiegen, statt einen möglicherweise ruinösen Verlust laufen zu lassen.
- Beim Trailing-One-Bar-Entry und beim Swing Entry liegt der erste Stop einen Tick jenseits des Swing-Hochs oder Swing-Tiefs vor dem Einstieg.
- Nur ein Handel jenseits dieses Extrems hebt das Setup auf. Ein näherer, willkürlicher Stop zwischen Einstieg und Extrem ist nicht zulässig.
- Das Nachziehen des Stop-Loss, wenn der Markt in die erwartete Richtung läuft, und die Ausstiegsstrategie sind nicht Gegenstand dieses Kapitels, sondern von Kapitel 7.
- Erfolgreiche Trader haben immer einen relativ engen Stop. Ein Verlust am Stop muss akzeptabel sein.
- Ein weiter Stop, nur um der Position Luft zu geben, bricht die Risikosregel.
- Der Markt soll die Position über einen nachgezogenen Stop herausnehmen, indem er gegen sie läuft. Ein vorher festgelegtes Kursziel ist nie der Ausstiegspreis, außer man kann die Daten im Urlaub nicht jede Nacht nachführen. Dann liegen Schutzstop und Take-Profit-Order gleichzeitig im Markt.
- Vor dem Einstieg stehen die Bedingungen fest, unter denen der Stop jeder Unit angepasst wird. Konkrete Handlungen folgen, wenn diese Bedingungen eintreten.
- Neue Information darf den Plan ändern. Jede Änderung muss aus denselben Faktoren folgen wie der Einstieg: Momentum, Muster, Preis und Zeit. Entscheidungen lassen sich nicht durch Regeln, Systeme oder Software ersetzen, wenn die Rendite maximiert werden soll.
- Stops werden nie nur wegen einer bestimmten Höhe des nicht realisierten Gewinns angepasst und nie um einen festen, willkürlichen Abstand vom aktuellen Preis. Es gibt immer einen logischen Grund.
- Ein zu nah nachgezogener Stop ist ein Hauptgrund, vor den Abschlussbedingungen ausgestoppt zu werden und die Trendrendite nicht zu maximieren. Solange das Momentum der höheren Zeitebene und fünf Abschnitte den Abschluss nicht anzeigen, bleibt der Stop weit genug, auch ein Welle-4-Retracement von typischerweise 38,2 bis 50 Prozent der Welle 3 auszuhalten.
- Der anfängliche Schutzstop steht vor dem Trade fest. Danach wird er nur angepasst, wenn die Marktposition einen logischen Grund liefert. Es gibt keine feste Formel.
- Die zweite Unit kann zuerst auf Breakeven bleiben, bis die Korrekturstruktur einen engeren logischen Platz ergibt, und erst danach nah an das Ein-Bar-Tief der arbeitenden Zeitebene rücken.
- Nach einer überkauften höheren Zeitebene gehört der Stop nah an den Markt, besonders wenn die niedrigere Zeitebene bärisch umkehrt. Vorher bleibt er weit genug, um die frühe Trendphase nicht zu verlieren.
- Weite Umkehrbars können den Preis deutlich bewegen, bevor ein Momentum-Signal kommt. Hochs und Tiefs entstehen manchmal außerhalb typischer Zeitfaktoren. Der Stop folgt trotzdem der Information bis zum letzten Bar.
- Der Stop der zweiten Einheit bleibt relativ weit vom Markt und wird nur nach einer Momentumumkehr der unteren Zeitebene oder einem anderen technischen Grund angepasst.
- Wer den Stop zu nah nachzieht, wird mit kleinem Gewinn ausgestoppt und verschenkt den größeren Lauf.
- Erfolgreiche Trader halten den Stop auf den meisten Trades weit und ändern ihn erst, wenn ein technischer Grund vorliegt.
- Ist der nötige Anfangsstop für einen Future zu weit, kann der passende ETF die Kapitalbindung begrenzen, statt das Setup wegen des Hebels zu verwerfen.
- Ein nachgezogener Stop, der bei Auslösung mindestens einen kleinen Gewinn lässt, sichert die zweite Einheit, auch wenn die größere Bewegung ausbleibt.
- Erfolgreiche Trader halten den Stop weit vom Markt und passen ihn nur an, wenn eine konkrete Marktaktion das rechtfertigt.
- Die künftige Struktur ist nicht im Voraus bekannt, deshalb darf sich die konkrete Stop-Führung im Lauf des Trades ändern.
- Ein Swing-Tief wird erst nach mindestens zwei Tagen Abverkauf als Strukturpunkt akzeptiert, an den der Stop gezogen werden darf.
- Struktur für Stop-Anpassungen sind Lücken, kleinere Swing-Tiefs und Ausbrüche aus Konsolidierungen.
- Steigt die Volatilität, nimmt der Markt diese Struktur oft mit und stoppt die Position aus; wer die Regel beibehält, fängt Ausreißer und macht in unruhigen Lagen kleine Gewinne oder kleine Verluste.
- Der Stop bleibt relativ weit, bis ein logischer technischer Grund vorliegt, und wird danach häufiger an die jeweils neue Struktur gelegt.
- Nahe einem möglichen Abschluss des Trends wird der Stop näher an den Markt gezogen, um einen vernünftigen Gewinn zu sichern.
- Ist das Setup erfüllt, sind Einstiegsart, Einstiegspreis und erster Schutzstop objektiv festgelegt; darüber fällt keine weitere Entscheidung.
- Bei der Momentumumkehr und beim Swing-Breakout liegt der erste Schutzstop einen Tick jenseits des Swing-Extrems, das vor dem Einstieg entstanden ist.
- Ein objektiver Ausstieg zieht den Stop einer Einheit am Ein-Bar-Tief oder Ein-Bar-Hoch nach, nach der ersten Momentumumkehr der kleineren Zeitebene gegen den Trend der größeren.
- Ein weiterer objektiver Ausstieg zieht den Stop einer Einheit nach, wenn der Markt die 100-Prozent-APP erreicht.
- Diese objektiven Ausstiege leisten gute Dienste; der Großteil der Entscheidungen liegt trotzdem in der weiteren Führung.
- Preis, Zeit und Musterlage gehören zur Führung, und der Plan darf sich ändern, wenn der Trend neue Information liefert.
- Die Kapitalbindung je Einheit ist der Abstand von Einstieg und erstem Schutzstop.
- Greift der erste Schutzstop nicht, werden im weiteren Verlauf die signifikanten Entscheidungspunkte festgehalten und die Stop-Anpassungen notiert.
- Ein mechanisches System legt Einstieg, Stop-Loss und Ausstieg vollständig objektiv fest.
- Beim Swing-Breakout liegt der initiale Schutz-Stop-Loss einen Tick unter beziehungsweise über dem Swing-Hoch oder Swing-Tief, das vor dem Einstieg entstanden ist.
- Bei der Momentum-Reversal-Strategie liegt der initiale Schutzstop nach Ausführung einen Tick unter dem Swing-Tief oder über dem Swing-Hoch vor dem Einstieg.
- Ein Handelssystem bestimmt mit vollständig objektiven Regeln auch den genauen Stop-Loss-Preis.

## Risiken und Grenzen

- Eine solche Strategie trägt eigenes Risiko, auch wenn die gehaltenen Instrumente eine niedrige Volatilität haben.
- Bei Mean-Reversion-Strategien ist Risikomanagement besonders wichtig und besonders schwierig, weil sich die üblichen Stop-Losses logisch nicht einsetzen lassen.
- Warum das so ist und welche Verfahren dann passen, wird in Kapitel 8 behandelt.
- Der seltene Verlust nach einer Erfolgsserie beim maximalen Leverage ist oft sehr schmerzhaft und manchmal katastrophal.
- Ist ein Markt lange geschlossen, sind Stop-Losses nutzlos, weil der Markt bei der Wiedereröffnung nach oben oder unten gappen kann.
- Der aufsummierte Verlust aufeinanderfolgender verlierender Momentum-Positionen kann trotzdem in die Insolvenz führen.
- Bei einem Gap zur Wiedereröffnung kann die Ausführung viel schlechter sein als der erlaubte Maximalverlust.
- Optionskäufe können dieses Gap-Risiko beseitigen, sind aber teuer und nur für erwartete Marktschließungen wertvoll.
- Selbst bei offenem Markt ist der Stop-Loss nutzlos, wenn alle Liquiditätsanbieter gleichzeitig die Liquidität abziehen, wie beim Flash Crash am 6. Mai 2010.
- Moderne Market Maker mussten im Stress nur ein Bid von 0,01 Dollar halten, das Stub Quote; eine Verkaufs-Stop-Order auf Accenture wurde an diesem Tag zu 0,01 Dollar je Aktie ausgeführt (Arnuk und Saluzzi, 2012).
- CPPI und Stop-Loss verhindern einen Drawdown im Overnight-Gap oder bei ausgesetztem Handel nicht.
- Bei Mean Reversion scheint der Stop-Loss der Annahme zu widersprechen, und der Autor hat keine solche Strategie gebacktestet, deren APR oder Sharpe Ratio dadurch stieg.
- Ein weiter Stop, nur um der Position Raum zu geben, und weiteres Aufstocken bei Gegenlauf enden in einem großen Verlust oder darin, dass der Broker die Position schließt, wenn das Margin-Kapital aufgebraucht ist.

## Beispiele

- Im SLV lag ein Stop unter dem Docht des Hammers.
- Im AUD/USD auf 15 Minuten lag der Short-Stop über dem Docht der ersten Shooting Star.
- Bei Procter & Gamble lieferten die Volumenunterschiede der beiden Stauzonen einen Anhalt für die Stop-Orders.
- Im GBP/USD auf 15 Minuten saß der Stop unter dem letzten Pivot-Tief der etwa 70 Kerzen langen Stauung.
- Auf der Stunde lag der Schutz über dem Markt, nachdem der alte Boden zur Decke geworden war.
- Im Beispiel beträgt die Verlustschwelle minus 0,01 und das Gewinnziel 0,005.
- Bei Verlustauszahlung minus 0,01 und Gewinnauszahlung 0,005 zehrt ein Rückgang der Trefferwahrscheinlichkeit von 0,7 auf 0,67 den erwarteten Gewinn auf, weil die Schwelle für eine Sharpe Ratio von null bei zwei Dritteln liegt.
- Im 60-Minuten-Long lag der Sell-Stop bei 1406,50, ein Tick unter dem Swing-Tief, bei 24,75 Punkten Abstand zum Einstieg bei 1431,25, ein Tick über dem Ein-Bar-Hoch.
- Im Trailing-Short lag der Buy-Stop einen Tick über dem Hoch von Bar 3. Im IBM-Tages-Short einen Tick über dem Swing-Hoch vor dem Einstieg, und der Trade endete mit kleinem Verlust.
- Im EUR/GBP lag der Buy-Stop einen Pip über dem korrektiven Hoch. Im EUR/USD-Long einen Tick unter dem Swing-Tief vor der bullischen Umkehr.
- Beim Swing Entry im ES lag der Schutz-Sell-Stop bei 1411,25, sobald der Buy-Stop bei 1449,50 ausgeführt wurde.
- Im 5-Minuten-Short lag der Buy-Stop einen Tick über dem Swing-Hoch bei 1362,75.
- Im ES-Beispiel liegt der anfängliche Schutz-Sell-Stop bei 1435,25, einen Tick unter dem Tief, der Einstieg bei 1441,75.
- Im Google-Beispiel liegt der anfängliche Schutz-Sell-Stop einen Tick unter dem kleineren Swing-Tief bei 505,79.
- XAU-Long am 20. August auf dem TR-1BH bei 132,34, einen Tag nach der bullischen Tagesumkehr. Anfänglicher Schutz-Sell-Stop 120,40, einen Tick unter dem Tief vom 16. August, Kapitalrisiko 11,94. Der Ein-Bar-Hoch am 17. August lag bei 132,33, das Swing-Tief bei 120,41, fast 12 Punkte.
- Nachdem das kleinere Swing-Hoch vom 24. August genommen war, wurde der Stop beider XAU-Positionen auf 132,59 gesetzt, einen Tick unter dem kleineren Swing-Tief der bullischen Momentum-Umkehr. Das war nicht eigens im Plan vorgesehen.
- Ein Bruch des Tiefs vom 28. August hätte jedes logische bullische Muster entwertet. Wäre der neue Stop sofort getroffen worden, wäre wenigstens ein kleiner Gewinn entstanden.
- Am 4. September, nach dem 61,8-Prozent-Retracement und vor der zweiten bärischen Tagesumkehr, wird nur der Stop der kurzfristigen XAU-Unit am Ein-Bar-Tief nachgezogen.
- Am 9. September nimmt das XAU dieses nachgezogene Ein-Bar-Tief und stoppt die kurzfristige Unit bei 150,36 aus.
- Der Stop der zweiten XAU-Unit wird auf einen Schluss bei oder unter 139,42 gesetzt, das mögliche Schluss-Hoch von Welle 1 oder A.
- Nach dem weiten Aufwärtstag am 18. September wird dieser Stop auf das Tief vom 5. September gelegt, ein Stück unter dem 61,8-Prozent-Retracement des Hochs vom 18. September und am Tief eines engen Tages vor einem weiteren weiten Aufwärtstag.
- Am 9. Oktober wird der Stop auf 163,48 gesetzt, einen Tick unter dem möglichen Tief der Welle 4.
- Handelt das XAU 179,15 oder macht das Tagesmomentum eine bärische Umkehr, liegt der Stop einen Tick unter dem täglichen Ein-Bar-Tief.
- Die zweite XAU-Unit wurde drei Tage nach Erreichen des Preisziels ausgestoppt, mit 46,11 Punkten Gewinn, 178,45 minus 132,34.
- S&P am 27. November: Einstieg 1431,25, Stop 1406,50, in der Ausführung 24,75 Punkte Kapitalrisiko je Kontrakt. Die Rückschau nennt dasselbe anfängliche Risiko mit 24,25 Punkten.
- Ist dieses Kapitalrisiko je Future-Kontrakt für den Tradingplan zu groß, wird der Trade im SPY-ETF ausgeführt.
- Der Stop der kurzfristigen S&P-Unit geht ans Ein-Bar-Tief, wenn 1462 erreicht ist oder die zweite bärische 60-Minuten-Umkehr vorliegt. Ausstieg am ersten Bar des 29. November bei 1466,25.
- Der Stop der langfristigen S&P-Unit wird auf 1462,75 gesetzt, einen Tick unter dem Tief der Welle B.
- Er geht danach auf das Ein-Bar-Tief, wenn 1510,25 gehandelt wird oder das 60-Minuten-Momentum bärisch umkehrt. Ausgestoppt wurde bei 1507,00.
- 15-Minuten-S&P: Stop 1411,25, einen Tick unter dem Swing-Tief, Einstieg 1422,50, Kapitalrisiko 11,25 Punkte, gegen 24,25 Punkte auf 60 Minuten. Danach Breakeven auf der zweiten Unit, bis zwei ABC-Abschnitte fertig sind, dann das mögliche Tief der Welle B, dann das 60-Minuten-Ein-Bar-Tief bei überkauftem 60-Minuten-Momentum und erreichter Welle-C-Zone.
- OIH: Einstieg am 23. Februar bei 136,93, einen Tick über dem Trailing-One-Bar-High, Stop 132,00, einen Tick unter dem möglichen Welle-C-Tief vom 20. Februar, Risiko 4,93. Am 5. März ausgestoppt, der Stop wurde nicht angepasst. Verlust beider Units 4,93.
- EUR/USD erster Long 1,3479, Stop ausgelöst bei 1,3458, Verlust 21 Pips. Zweiter Long 1,3469, Stop 1,3451, Risiko 18 Pips.
- Nachdem am 22. August über das Hoch von Welle 1 oder A gehandelt wurde, wandert der Stop beider Units auf 1,3465, einen Tick unter dem kleineren Swing-Tief.
- Kurzfristige EUR/USD-Unit: bei 1,3636 das 60-Minuten-Ein-Bar-Tief, und zusätzlich einen Tick unter das Tief vor jeder bullischen 60-Minuten-Umkehr. Am letzten Bar des betreffenden Charts 1,3544. Ausstieg 1,3625, einen Tick unter dem nachgezogenen Ein-Bar-Tief, Gewinn 156 Pips.
- Langfristige Unit: weit vom Markt, bis das Tagesmomentum wieder bullisch umkehrt, dann 1,3549. Bis zur überkauften Wochenlage unter das Swing-Tief vor jeder folgenden bullischen Tagesumkehr. Danach unter das Swing-Tief nach der nächsten bullischen Tagesumkehr, und nach der nächsten bärischen Tagesumkehr einen Tick unter dem täglichen Ein-Bar-Tief.
- Am 5. Oktober Stop auf 1,4030, das Tief vor der bullischen Tagesumkehr. Am 9. Oktober ausgestoppt bei 1,4030, als unter 1,4031 gehandelt wurde. Gewinn 561 Pips bei Einstieg 1,3469. In der frühen Trendphase lag der Stop relativ weit weg. Das Tagesmomentum hatte vor dem Ausstopp weder die überkaufte Zone erreicht noch bärisch umgekehrt.
- Im EUR/USD lag der Long bei 1,4341 am 21. Dezember um 2 Uhr MEZ, mit 35 Pips Stop bei 1,4306; der Stop der zweiten Einheit wurde jeweils ein Tick unter das Tief vor jeder bullischen Umkehr des 34er 60-Minuten-DTosc gesetzt.
- Die erste Einheit wurde mit dem nachgezogenen 60-Minuten-Ein-Bar-Tief geführt, sobald das 50-Prozent-Retracement erreicht war, und ging bei 1,4387 heraus.
- Beim GBP lag der erste Kaufstop ein Tick über dem Hoch vom 24. September bei 2,0322, der Short bei 2,0254; später lag der Stop ein Pip über dem kleineren Swing-Hoch bei 2,0230.
- Beim Yen lag der Einstiegsstop ein Pip unter dem nachgezogenen 60-Minuten-Ein-Bar-Tief, zwei Einheiten bei 115,33; nach der nächsten bärischen 60-Minuten-Umkehr wurde der Stop auf das Swing-Hoch 115,16 gesetzt, die zweite Einheit ging mit 26 Pips heraus.
- Beim ES lag der Einstieg bei 1311,25 und der erste Verkaufsstop bei 1269, ein Tick unter dem kleineren Swing-Tief; empfohlen wurde ersatzweise der SPY-ETF.
- Am Tag nach dem ES-Einstieg sollte der Stop 10 Punkte unter das jüngste Hoch gezogen werden, sodass ein Ausstoppen mindestens einen kleinen Gewinn lässt.
- Der ES-Stop der zweiten Einheit wurde am Morgen des 25. Januar auf 1356,25 gesetzt, ein Tick unter ein kleineres Swing-Tief, und später mit 45 Punkten Gewinn ausgelöst.
- Sojabohnen: erster Stop 743'75, dann Break-even nach dem Tief bei 765, dann auf das Tief vom 30. Mai bei 823, später auf das Tief vom 29. Juni bei 875.
- Vom 18. bis 22. Juni liefen die Bohnen 68 Cent gegen die Position, der Stop blieb bei 823 und wurde knapp nicht erreicht; die Lücke vom 29. Juni nahm den Druck.
- Der ES-Short-Stop lag bei 1294,50; der Ausstiegs-Kaufstop ein Tick über dem Ein-Bar-Hoch bei 1281,75 griff auf der nächsten Bar.
- Im USD/CAD lag der erste Stop bei 1,0328; an der 100-Prozent-APP wurde eine Einheit mit einem Stop 10 Pips über dem Markt geführt und die zweite auf Break-even gesetzt.
- Nachdem das Welle-3-Tief vom 24. Januar genommen war, lag der Stop wenige Pips über dem Welle-4-Hoch vom 28. Januar; am möglichen Welle-5-von-5-Tief wenige Pips über 0,9972, Ausstieg bei 0,9980.

## Unterschiedliche Quellenpositionen

- Praktisch keine Veröffentlichung berücksichtigt den Stop-Loss, wenn sie Beobachtungen labelt, und das kennzeichnet für den Autor den Zustand der Anlage-Literatur.
- Die pauschale Aussage, der Stop-Loss senke immer die Performance von Mean-Reversion-Strategien, ist durch Survivorship Bias verzerrt.
- Er senkt sie, solange Mean Reversion bleibt, und verbessert sie, wenn ein Regimewechsel zum Trend einsetzt.

## Eigene Erkenntnisse


## Quellen und Fundstellen

- Markets in Profile_ Profiting from the Auction Process.pdf, S. 181–200 → [[Trading/Pilot/blocks/markets-in-profile/markets-in-profile-block-014-p181-p200|S. 181–200]]
- Mind Over Markets_ Power Trading with Market Generated Information, Updated Edition.pdf, S. 269–288 → [[Trading/Pilot/blocks/mind-over-markets/mind-over-markets-block-017-p269-p288|S. 269–288]]
- Mind Over Markets_ Power Trading with Market Generated Information, Updated Edition.pdf, S. 288–296 → [[Trading/Pilot/blocks/mind-over-markets/mind-over-markets-block-018-p288-p296|S. 288–296]]
- A Complete Guide to Volume Price Analysis.pdf, S. 96–115 → [[Trading/Pilot/blocks/a-complete-guide-to-volume-price-analysis-pdf/a-complete-guide-to-volume-price-analysis-pdf-block-006-p096-p115|S. 96–115]]
- A Complete Guide to Volume Price Analysis.pdf, S. 115–134 → [[Trading/Pilot/blocks/a-complete-guide-to-volume-price-analysis-pdf/a-complete-guide-to-volume-price-analysis-pdf-block-007-p115-p134|S. 115–134]]
- A Complete Guide to Volume Price Analysis.pdf, S. 134–153 → [[Trading/Pilot/blocks/a-complete-guide-to-volume-price-analysis-pdf/a-complete-guide-to-volume-price-analysis-pdf-block-008-p134-p153|S. 134–153]]
- Advances in Financial Machine Learning.pdf, S. 58–77 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-004-p058-p077|S. 58–77]]
- Advances in Financial Machine Learning.pdf, S. 191–210 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-011-p191-p210|S. 191–210]]
- Advances in Financial Machine Learning.pdf, S. 210–229 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-012-p210-p229|S. 210–229]]
- Advances in Financial Machine Learning.pdf, S. 229–248 → [[Trading/Pilot/blocks/advances-in-financial-machine-learning-pdf/advances-in-financial-machine-learning-pdf-block-013-p229-p248|S. 229–248]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 1–18 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-001-p001-p018|S. 1–18]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 76–80 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-005-p076-p080|S. 76–80]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 125–144 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-009-p125-p144|S. 125–144]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 170–172 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-012-p170-p172|S. 170–172]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 173–186 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-013-p173-p186|S. 173–186]]
- Algorithmic Trading_ Winning Strategies and Their Rationale.pdf, S. 187–206 → [[Trading/Pilot/blocks/algorithmic-trading/algorithmic-trading-block-014-p187-p206|S. 187–206]]
- Evidence-based Technical Analysis_ Applying the Scientific Method and Statistical Inference to Trading Signals.pdf, S. 20–39 → [[Trading/Pilot/blocks/evidence-based-technical-analysis/evidence-based-technical-analysis-block-002-p020-p039|S. 20–39]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 17–22 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-002-p017-p022|S. 17–22]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 42–61 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-004-p042-p061|S. 42–61]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 63–82 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-006-p063-p082|S. 63–82]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 153–172 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-012-p153-p172|S. 153–172]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 172–176 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-013-p172-p176|S. 172–176]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 177–196 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-014-p177-p196|S. 177–196]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 196–214 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-015-p196-p214|S. 196–214]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 215–234 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-016-p215-p234|S. 215–234]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 234–250 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-017-p234-p250|S. 234–250]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 251–270 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-018-p251-p270|S. 251–270]]
- High Probability Trading Strategies_ Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf, S. 270–289 → [[Trading/Pilot/blocks/high-probability-trading-strategies/high-probability-trading-strategies-block-019-p270-p289|S. 270–289]]

## Verwandte Themen
