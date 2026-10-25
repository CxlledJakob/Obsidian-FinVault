# Projektplan: Trading Knowledge Brain

**Status:** Aktualisierte Projektgrundlage  
**Zweck:** Kontextdokument für die weitere Zusammenarbeit mit KI-Systemen sowie Grundlage für Konzeption, Umsetzung und Automatisierung

---

# 1. Projektziel

## 1.1 Gesamtziel

Aufgebaut wird ein persönliches, KI-gestütztes Wissenssystem für Finanzmärkte, Investitionen und Trading. Der fachliche Schwerpunkt liegt auf technischer Analyse und technischem Trading. Ergänzend sollen fundamentale Analyse, Makroökonomie, quantitative Konzepte, Risikomanagement, Handelspsychologie und die Auswertung eigener Trading-Aktivitäten einbezogen werden.

Das System soll innerhalb eines ungefähr zwölfmonatigen Lern- und Aufbauzeitraums dabei helfen, große Mengen an Fachwissen kontrolliert aufzunehmen, zu strukturieren, zu prüfen, miteinander zu verbinden und praktisch nutzbar zu machen.

## 1.2 Gewünschter Nutzen

Das System soll:

- Bücher, Studien, Research-Dokumente, PDFs, Analystenbeiträge und eigene Erkenntnisse zentral verwalten,
- Quellen mit KI analysieren und verdichten,
- Wissen nach einer vorgegebenen Trading-Taxonomie organisieren,
- zwischen Originalquelle, Quellenanalyse und dauerhaftem Fachwissen unterscheiden,
- historische Analysteneinschätzungen wertpapierbezogen dokumentieren,
- später wiederkehrende Verarbeitungsschritte automatisieren,
- langfristig natürliche Sprachabfragen über den eigenen Wissensbestand ermöglichen,
- eigene Strategien, Trading-Journale, Backtests und Performanceauswertungen integrieren.

## 1.3 Leitprinzipien

1. So einfach wie möglich, so komplex wie nötig.
2. Zunächst manuell testen, danach automatisieren.
3. Standardfunktionen vor Eigenentwicklung.
4. Kostenlose und lokale Lösungen werden bevorzugt.
5. Obsidian ist die dauerhafte Wissensbasis.
6. Markdown ist das bevorzugte Speicherformat.
7. KI-Ausgaben gelten zunächst als Entwurf.
8. Bestehende geprüfte Inhalte dürfen nicht ungeprüft überschrieben werden.
9. Originalquellen und daraus abgeleitetes Wissen bleiben getrennt.
10. Das System soll langfristig erweiterbar und nicht von einem einzelnen KI-Anbieter abhängig sein.

---

# 2. Geltungsbereich

## 2.1 Trading als Teil eines größeren Obsidian-Vaults

Der Obsidian-Vault enthält mehrere fachliche Bereiche. Aktuell sind mindestens folgende Bereiche vorhanden:

```text
Immos/
Steuern/
Trading/
```

Das aktuelle Projekt betrifft ausschließlich den Bereich `Trading`. Andere Bereiche dürfen durch Templates, Links, KI-Zugriffe oder spätere Automatisierungen nicht verändert werden.

## 2.2 Inhaltlicher Umfang

Zum Trading-Bereich gehören:

- technische Analyse,
- Marktstruktur und Price Action,
- Trendanalyse,
- Unterstützungen und Widerstände,
- Chart- und Candlestick-Muster,
- Volumen und Orderflow,
- Smart Money Concepts,
- Wyckoff und Elliott-Wellen,
- Indikatoren, Momentum und Volatilität,
- Marktzyklen und Intermarket-Analyse,
- quantitative und statistische Konzepte,
- Risiko- und Positionsmanagement,
- Handelspsychologie,
- Trading-Performance,
- algorithmischer Handel,
- Marktanomalien und Behavioral Finance,
- Fundamentalanalyse,
- Makroökonomie,
- Unternehmenskennzahlen,
- wertpapierbezogene Analysten-Updates,
- später eigene Strategien, Trades und Backtests.

---

# 3. Fachliche Taxonomie

## 3.1 Hauptthemen

Unter `Trading/Notes` wurden 25 Hauptthemenordner angelegt:

1. Marktstruktur & Price Action
2. Trendanalyse
3. Unterstützungen & Widerstände
4. Chartmuster
5. Candlestick-Formationen
6. Volumenanalyse
7. Orderflow & Market Microstructure
8. Smart Money Concepts (SMC)
9. Wyckoff-Methode
10. Elliott-Wellen
11. Indikatoren
12. Momentum
13. Volatilität
14. Marktzyklen
15. Intermarket-Analyse
16. Quantitative & statistische Konzepte
17. Risikomanagement
18. Positionsmanagement
19. Handelspsychologie
20. Trading-Performance & Auswertung
21. Algorithmischer Handel
22. Marktanomalien & Behavioral Finance
23. Fundamentalanalyse
24. Makroökonomie
25. Unternehmenskennzahlen

## 3.2 Unterthemen und Schlagwörter

Die vollständige Taxonomie umfasst:

- 25 Hauptthemen,
- ungefähr 78 Unterthemen,
- ungefähr 821 konkrete Begriffe und Spezialthemen.

Die Unterthemen und Begriffe sollen nicht als hunderte Unterordner abgebildet werden. Stattdessen gilt:

- Hauptthemen sind Ordner.
- Pro Hauptthema existiert eine gleichnamige Indexdatei.
- Unterthemen stehen als Überschriften in der Indexdatei.
- Begriffe stehen zunächst als Listeneinträge unter den Unterthemen.
- Erst wenn ein Begriff tatsächlich bearbeitet wird, entsteht eine eigenständige Wissensnotiz.
- Beziehungen zwischen Themen werden über interne Links und Metadaten dargestellt.

## 3.3 Priorisierung

Die Taxonomie verwendet drei Lernstufen:

- **A:** allerwichtigste Grundlagen und zwingend zu beherrschende Themen
- **B:** vertiefende und spezialisierte Themen
- **C:** fortgeschrittene oder optionale Themen

Die Kennzeichnung beschreibt die Lernpriorität. Sie ist keine Aussage über Profitabilität, wissenschaftliche Qualität oder praktische Eignung einer Strategie.

---

# 4. Zielbild der Wissensstruktur

## 4.1 Drei getrennte Wissensebenen

### Ebene 1: Originalquelle

Die unveränderte Quelldatei, beispielsweise:

- Buch oder Buchkapitel,
- Studie,
- Research-PDF,
- Analystenpost,
- E-Mail-Benachrichtigung,
- Chartbild,
- Video-Transkript.

### Ebene 2: Quellenanalyse

Eine strukturierte Markdown-Datei, die die jeweilige Quelle als Ganzes dokumentiert. Sie enthält unter anderem:

- Quellenangabe,
- Zusammenfassung,
- Kernaussagen,
- behandelte Themen,
- Handelsregeln,
- Voraussetzungen,
- Risiken und Grenzen,
- Beispiele,
- Fundstellen,
- Taxonomiezuordnung,
- Vorschläge für Wissensnotizen.

### Ebene 3: Wissensnotiz

Eine dauerhafte, themenbezogene Notiz zu genau einem Konzept. Eine Wissensnotiz kann Erkenntnisse aus mehreren geprüften Quellen zusammenführen.

Beispiel:

```text
Originalbuch.pdf
    -> Quellenanalyse zum gesamten Buch oder Kapitel
        -> Wissensnotiz Marktstruktur.md
        -> Wissensnotiz Swing High.md
        -> Wissensnotiz Impulsbewegung.md
```

## 4.2 Indexdateien

Die 25 Hauptthemen-Indexdateien sind Übersichts- und Navigationsseiten. Sie sollen nicht mit kompletten Buchzusammenfassungen gefüllt werden.

Ein unbearbeitetes Thema bleibt als Text stehen:

```markdown
- [A] Marktstruktur
```

Sobald eine eigenständige Wissensnotiz existiert, wird der Ausdruck verlinkt:

```markdown
- [A] [[Trading/Notes/01 - Marktstruktur & Price Action/Marktstruktur|Marktstruktur]]
```

---

# 5. Besondere Quelle: laufende Analysten-Updates

## 5.1 Besonderheit

Ein wichtiger Analyseanbieter veröffentlicht auf Patreon regelmäßig neue Beiträge zu einzelnen Aktien oder anderen Wertpapieren. Die Beiträge können technische Analysen, Elliott-Wellen, Unterstützungen, Widerstände, Kaufzonen, Kursziele und teilweise fundamentale Inhalte enthalten.

Diese Inhalte unterscheiden sich von Büchern und Studien:

- Sie sind wertpapierbezogen.
- Sie gelten zu einem bestimmten Veröffentlichungszeitpunkt.
- Es können im Abstand weniger Wochen neue Einschätzungen zum selben Wertpapier entstehen.
- Neue Analysen können frühere Szenarien ändern oder ersetzen.
- Alte Beiträge müssen als historischer Stand erhalten bleiben.

## 5.2 Ablageprinzip

Jedes Analysten-Update wird als eigene Datei gespeichert und niemals durch ein späteres Update überschrieben.

Perspektivisches Beispiel:

```text
Trading/Research/Analysten/[Analyst]/NVIDIA/
├── 2026-08-01 - NVIDIA.md
├── 2026-08-21 - NVIDIA.md
└── NVIDIA - Verlauf.md
```

## 5.3 Analysten-Update-Template

Ein eigenes Template `Analysten Updates` wurde bereits angelegt. Es soll mindestens folgende Inhalte ermöglichen:

- Analyst oder Quelle,
- Veröffentlichungsdatum,
- Instrument und Ticker,
- Quell-URL,
- Zusammenfassung,
- Marktstand zum Veröffentlichungszeitpunkt,
- Primärszenario,
- Alternativszenario,
- Unterstützungen,
- Widerstände,
- Kauf- oder Beobachtungszonen,
- Invalidationsmarken,
- Kursziele,
- Elliott-Wellen-Struktur,
- fundamentale Aussagen,
- Änderungen gegenüber dem vorherigen Update,
- Bedingungen für eine Neubewertung,
- Unsicherheiten und Risiken,
- Originalbild oder Anhänge,
- Verknüpfung zum vorherigen und späteren Update.

## 5.4 Geplanter Eingang

Bevorzugter automatischer Eingang ist die Patreon-E-Mail-Benachrichtigung, sofern sie den vollständigen Text enthält. Falls nur eine Vorschau enthalten ist, muss der vollständige Post vorerst manuell ergänzt werden.

Geplanter späterer Prozess:

```text
Patreon-E-Mail
-> E-Mail-Postfach oder Weiterleitung
-> n8n erkennt den Absender
-> Text und Anhänge werden extrahiert
-> Instrument, Datum und Themen werden erkannt
-> Analysten-Update wird als Markdown-Entwurf erzeugt
-> Ablage in Trading/Inbox/Reviewed beziehungsweise Review
-> manuelle Prüfung
-> endgültige Ablage unter Research/Analysten
```

Chartbilder werden möglichst als Originaldatei erhalten und in der Markdown-Datei eingebettet. Die schriftliche Erläuterung bleibt die primäre Grundlage der automatischen Textanalyse.

---

# 6. Geplante Systemarchitektur

## 6.1 Kernkomponenten

### Obsidian

Dauerhafter Wissensspeicher für:

- Taxonomie,
- Quellenanalysen,
- Wissensnotizen,
- Analysten-Updates,
- Strategien,
- Journal,
- Systemdokumentation.

### NotebookLM

Zunächst manuelles Werkzeug für:

- quellenbezogene Analyse von PDFs, Büchern und Studien,
- Zusammenfassungen,
- Extraktion von Kernaussagen,
- Identifikation von Regeln, Risiken und Beispielen,
- Vorbereitung strukturierter Quellenanalysen.

NotebookLM ist nicht die dauerhafte Ablage. Die Ergebnisse werden als Markdown in Obsidian übernommen.

### Claude mit Obsidian MCP Connector

Geplanter beziehungsweise vorbereiteter Nutzen:

- gezieltes Lesen des Trading-Bereichs,
- semantische Suche im Vault,
- Zugriff auf Projektplan und Konventionen ohne erneuten Datei-Upload,
- später kontrolliertes Erstellen von Entwürfen.

Der Connector wurde auf Obsidian-Seite vorbereitet. Ob die Verbindung in Claude Desktop vollständig installiert und funktionsfähig getestet wurde, ist noch nicht bestätigt.

### n8n Self-Hosted

Spätere Automatisierungs- und Orchestrierungsschicht für:

- Ordner- oder E-Mail-Trigger,
- Verarbeitung neuer Dateien,
- Text- und PDF-Extraktion,
- KI-Aufrufe,
- Taxonomieklassifikation,
- Markdown-Erzeugung,
- Review-Ablage,
- Verschiebung von Originalquellen,
- Fehlerbehandlung und Protokollierung.

### Optionales RAG-System

Erst für eine spätere Phase vorgesehen. Mögliche Komponenten:

- lokale oder hybride Embeddings,
- Qdrant oder eine vergleichbare Vektordatenbank,
- Ollama oder ein Cloud-LLM,
- OpenWebUI oder eine vergleichbare Oberfläche.

RAG wird erst aufgebaut, wenn ein relevanter Bestand an geprüften Notizen vorhanden ist.

---

# 7. Geplante manuelle Quellenverarbeitung

## 7.1 Bücher, Studien und statische PDFs

Zunächst wird ein manueller Pilot mit wenigen Quellen durchgeführt.

```text
PDF nach Inbox/New
-> PDF in NotebookLM laden
-> standardisierten Analyseauftrag verwenden
-> Quellenanalyse als Markdown exportieren oder kopieren
-> Markdown-Datei in Inbox/Reviewed ablegen
-> Ergebnis manuell prüfen
-> geprüfte Quellenanalyse dauerhaft einsortieren
-> daraus einzelne Wissensnotizen ableiten
-> Indexdateien mit neuen Wissensnotizen verlinken
-> Originalquelle nach Books, PDFs oder Research verschieben
-> Vorgang vorübergehend nach Inbox/Terminated
```

## 7.2 Warum zunächst nur wenige Quellen

Mit drei bis fünf Pilotquellen soll geprüft werden:

- Ist das Quellenanalyse-Template vollständig?
- Liefert NotebookLM konsistente Ergebnisse?
- Werden Fundstellen ausreichend dokumentiert?
- Lassen sich Hauptthema und Unterthema eindeutig zuordnen?
- Wie werden mehrere Themen in einer Quelle behandelt?
- Wie lassen sich Dubletten erkennen?
- Welche Schritte eignen sich später für n8n?

Erst nach dieser Prüfung soll eine größere Quellenmenge verarbeitet werden.

## 7.3 Qualitätsregeln

- Nur Aussagen aus der jeweiligen Quelle übernehmen.
- Interpretationen von Quellenaussagen trennen.
- Fundstellen nach Möglichkeit erhalten.
- Keine Profitabilitätsversprechen erzeugen.
- KI-Ergebnis zunächst als Entwurf behandeln.
- Jede dauerhafte Wissensnotiz mit ihrer Quelle verknüpfen.
- Strategien zunächst als Hypothese kennzeichnen.
- Keine bereits geprüfte Wissensnotiz automatisch überschreiben.

---

# 8. Geplanter automatisierter Prozess

## 8.1 Minimaler n8n-Pilot

Der erste Workflow soll bewusst klein bleiben:

```text
Neue TXT- oder PDF-Datei in Inbox/New
-> Datei nach Processing oder entsprechenden Zwischenstatus verschieben
-> Dateityp erkennen
-> Text extrahieren
-> Quellenmetadaten vorbereiten
-> KI analysiert die Quelle
-> KI schlägt Taxonomiezuordnung vor
-> Markdown-Quellenanalyse erzeugen
-> Ergebnis nach Inbox/Reviewed schreiben
-> bei Fehlern kennzeichnen oder separat ablegen
```

In dieser Stufe erfolgt noch keine ungeprüfte endgültige Ablage.

## 8.2 Erweiterter Workflow

Später ergänzt:

- Bücher, Studien, Research und Analysten-Updates unterscheiden,
- E-Mail-Trigger für Patreon,
- E-Mail-HTML in Markdown umwandeln,
- Anhänge und Chartbilder speichern,
- Hauptthema, Unterthema und A/B/C-Bezug erkennen,
- Wissensnotizvorschläge erzeugen,
- vorhandene Notizen auf mögliche Dubletten prüfen,
- Qualitätskontrolle durch separaten KI-Schritt,
- menschliche Freigabe,
- Originaldatei und Ergebnis endgültig einsortieren,
- Bearbeitung protokollieren.

## 8.3 Geplante KI-Schritte

1. **Extraktion:** Quellenangaben, Zusammenfassung, Regeln, Risiken, Beispiele.
2. **Klassifikation:** primäres Hauptthema, Unterthemen und vorhandene Taxonomiebegriffe.
3. **Wissensaufbereitung:** Markdown-Quellenanalyse und Vorschläge für atomare Wissensnotizen.
4. **Qualitätsprüfung:** unbelegte Ergänzungen, Widersprüche, fehlende Quellenangaben, Dubletten und unplausible Zuordnungen erkennen.

Komplexe autonome Agenten sind zunächst nicht erforderlich. Klare, aufeinanderfolgende Verarbeitungsschritte werden bevorzugt.

---

# 9. Aktuell tatsächlich umgesetzter Stand

Dieser Abschnitt hat Vorrang vor älteren Planständen.

## 9.1 Erledigt

### Struktur und Taxonomie

- Der größere Obsidian-Vault existiert.
- Der Bereich `Trading` existiert.
- Unter `Trading/Notes` wurden 25 Hauptthemenordner angelegt.
- In jedem Hauptthemenordner wurde eine gleichnamige Markdown-Indexdatei angelegt.
- Eine zentrale `Themenübersicht.md` mit funktionierenden Links wurde erzeugt.
- Die vollständige Taxonomie wurde bereinigt.
- Fehlerhafte Umlaute und Sonderbindestriche wurden korrigiert.
- Doppelte Kennungen wurden auf `[A]`, `[B]` und `[C]` vereinheitlicht.
- Die Bedeutung der Prioritäten A, B und C wurde festgelegt.
- `Trading/System/Vault-Struktur.md` wurde angelegt beziehungsweise abgelegt.

### Inbox

Im Inbox-Ordner wurden genau diese vier Unterordner angelegt:

```text
Trading/Inbox/
├── Analyst New/
├── New/
├── Reviewed/
└── Terminated/
```

Bedeutung nach aktuellem Stand:

- `Analyst New`: neue Analysten- beziehungsweise Patreon-Inhalte
- `New`: neue allgemeine Quellen wie PDFs, Studien und Bücher
- `Reviewed`: erzeugte Analysen und Entwürfe, die geprüft werden sollen oder bereits den Review-Schritt erreicht haben
- `Terminated`: abgeschlossene Verarbeitungsvorgänge; Dateien liegen dort vorübergehend, bevor Originale und Ergebnisse dauerhaft nach Books, PDFs, Research oder andere Zielordner einsortiert werden

### Templates und Regeln

Im Ordner `Trading/Templates` wurden zwei Dateien angelegt:

```text
Konventionen
Analysten Updates
```

Die genaue Dateiendung, der vollständige Inhalt und die praktische Funktionsprüfung dieser beiden Dateien müssen noch geprüft werden.

## 9.2 Noch nicht erledigt oder nicht bestätigt

- Der aktualisierte Projektplan wurde noch nicht in Obsidian abgelegt.
- Die Konventionen wurden noch nicht abschließend auf Vollständigkeit geprüft.
- Das Analysten-Update-Template wurde noch nicht mit einem echten Patreon-Beitrag getestet.
- Ein allgemeines Quellenanalyse-Template wurde noch nicht angelegt.
- Ein Wissensnotiz-Template wurde noch nicht angelegt.
- Ein Strategie-Template wurde noch nicht angelegt.
- Ein Trading-Journal-Template wurde noch nicht angelegt.
- Die Mastertaxonomie wurde noch nicht nachweislich unter `Trading/Research/Taxonomie` abgelegt.
- Ein vollständiges Backup wurde noch nicht bestätigt.
- Eine Wiederherstellung wurde noch nicht getestet.
- Es wurde noch keine Pilotquelle vollständig verarbeitet.
- NotebookLM wurde noch nicht im standardisierten Prozess getestet.
- Es wurde noch kein Patreon-Update nach dem neuen Template verarbeitet.
- n8n wurde noch nicht eingerichtet.
- Ein E-Mail-Trigger wurde noch nicht eingerichtet.
- Eine KI-Komponente für n8n wurde noch nicht ausgewählt.
- Das optionale RAG-System wurde noch nicht umgesetzt.

---

# 10. Aktuelle Soll-Struktur

Die vorhandene Struktur soll vorerst nicht unnötig geändert werden. Zielbild für die nächste Arbeitsphase:

```text
Trading/
├── Books/
├── Inbox/
│   ├── Analyst New/
│   ├── New/
│   ├── Reviewed/
│   └── Terminated/
├── Journal/
├── Notes/
│   └── 25 Hauptthemenordner mit Indexdateien
├── PDFs/
├── Research/
│   ├── Analysten/
│   ├── Quellen/
│   └── Taxonomie/
├── Strategies/
├── System/
│   ├── Vault-Struktur.md
│   └── Projektplan_Trading_Knowledge_Brain_Aktuell.md
├── Templates/
│   ├── Konventionen.md
│   ├── Analysten-Update.md
│   ├── Quellenanalyse.md
│   ├── Wissensnotiz.md
│   ├── Strategie.md
│   └── Trading-Journal.md
└── Themenübersicht.md
```

Die aktuell verwendeten Namen `Konventionen` und `Analysten Updates` können beibehalten werden. Eine Umbenennung ist nur erforderlich, wenn dadurch die spätere Automatisierung eindeutig verbessert wird.

---

# 11. Kosten- und Betriebsprinzip

## 11.1 Bevorzugte kostenlose Komponenten

- Obsidian für die Wissensbasis
- n8n Self-Hosted für Automatisierung
- NotebookLM für frühe manuelle Quellenanalyse innerhalb verfügbarer Nutzungsmöglichkeiten
- lokale Ordner und Markdown-Dateien
- optional Ollama und Qdrant für spätere lokale KI- beziehungsweise RAG-Verarbeitung

## 11.2 Mögliche Kosten

- Fachbücher und Zugang zu Analysteninhalten
- KI-API-Aufrufe im automatisierten n8n-Prozess
- zusätzliche Hardware für lokale Modelle
- externer Speicher für Backups
- optionale Premiumdienste

## 11.3 Kostenregel

Bevor kostenpflichtige KI-APIs oder Hardware eingesetzt werden, wird mit wenigen realen Dokumenten gemessen:

- Dokumentlänge,
- Verarbeitungszeit,
- Ergebnisqualität,
- Tokenverbrauch,
- Kosten pro Quelle,
- notwendiger manueller Nachbearbeitungsaufwand.

---

# 12. Risiken und Schutzmaßnahmen

## Informationsüberflutung

Nicht alle Quellen gleichzeitig verarbeiten. Zunächst wenige Pilotquellen und A-Themen priorisieren.

## Fehlerhafte KI-Ausgaben

Jede KI-Ausgabe bleibt zunächst im Review-Prozess. Quellenangaben und Fundstellen sind verpflichtend.

## Veraltete Analysteneinschätzungen

Jedes Update wird mit Datum und Instrument gespeichert. Frühere Dateien werden nicht überschrieben.

## Doppelte Wissensnotizen

Vor der Erstellung einer neuen Wissensnotiz wird geprüft, ob bereits eine entsprechende Datei existiert.

## Datenverlust

Vor einer größeren Quellenverarbeitung muss ein getestetes Backup vorhanden sein.

## Vermischung mit anderen Vault-Bereichen

Automatisierungen und KI-Zugriffe werden auf `Trading` begrenzt.

## Urheberrecht und Vertraulichkeit

Es werden nur rechtmäßig zugängliche Quellen verarbeitet. Bezahlte Patreon-Inhalte bleiben privat und werden nicht öffentlich weitergegeben.

## Trading-Risiko

Analystenaussagen und KI-Ausgaben sind keine Erfolgsgarantie. Strategien werden als Hypothesen behandelt und später durch Backtesting, Paper Trading und Risikomanagement geprüft.

---

# 13. Umsetzungsphasen ab aktuellem Stand

## Phase A: Grundlage vervollständigen

Konventionen und zentrale Templates werden geprüft und ergänzt. Ordner für dauerhafte Quellen, Taxonomie und Analysten werden angelegt. Ein Backup wird erstellt und getestet.

## Phase B: Zwei manuelle Pilotprozesse testen

Es werden zwei unterschiedliche Pilotpfade getestet:

1. eine statische PDF-Quelle wie Studie oder Buchkapitel,
2. ein zeitpunktbezogenes Analysten- beziehungsweise Patreon-Update.

Beide Ergebnisse werden als Markdown in `Reviewed` abgelegt und anschließend manuell geprüft.

## Phase C: Standardprozess stabilisieren

Nach insgesamt drei bis fünf Quellen werden Templates, Dateinamen, Metadaten, Ablageziele und Review-Regeln angepasst. Erst danach gilt der manuelle Prozess als stabil.

## Phase D: n8n-Pilot

Ein kleiner Workflow verarbeitet zunächst nur einen klar begrenzten Eingang, beispielsweise allgemeine PDFs aus `Inbox/New` oder Patreon-E-Mails für `Inbox/Analyst New`.

## Phase E: Erweiterte Automatisierung

Weitere Dateitypen, Wissensnotizvorschläge, Dublettenprüfung, Freigabe und endgültige Ablage werden ergänzt.

## Phase F: Wissensausbau und RAG

Die A-Themen werden systematisch bearbeitet. Ein RAG-System wird erst bei ausreichend großem und geprüftem Wissensbestand umgesetzt.

---

# 14. Nächste Arbeitspakete

## Arbeitspaket 1: Bestehende Grundlagen prüfen

**Ziel:** Sicherstellen, dass die zwei bereits erstellten Dateien praktisch verwendbar sind.

Aufgaben:

1. Vollständigen Inhalt von `Konventionen` prüfen.
2. A-, B- und C-Definition kontrollieren.
3. Ablage-, Quellen-, Review- und Überschreibregeln ergänzen.
4. `Analysten Updates` auf die vorgesehenen Felder prüfen.
5. Beide Dateien als `.md` speichern, falls noch nicht erfolgt.

**Ergebnis:** Verbindliche Konventionen und ein einsatzfähiges Analysten-Template.

## Arbeitspaket 2: Fehlende Basisordner und Templates ergänzen

**Ziel:** Den manuellen Quellenprozess technisch vorbereiten.

Aufgaben:

1. Unter `Trading/Research` die Ordner `Quellen`, `Analysten` und `Taxonomie` anlegen.
2. Bereinigte Taxonomie nach `Research/Taxonomie` kopieren.
3. Template `Quellenanalyse.md` anlegen.
4. Template `Wissensnotiz.md` anlegen.

**Ergebnis:** Allgemeine und analystenbezogene Quellen können getrennt verarbeitet werden.

## Arbeitspaket 3: Backup erstellen

**Ziel:** Den aktuellen Stand vor ersten echten Verarbeitungstests absichern.

Aufgaben:

1. Vollständige Kopie des Trading-Bereichs oder gesamten Vaults anlegen.
2. Eine Testdatei aus dem Backup wiederherstellen.
3. Backupdatum dokumentieren.

**Ergebnis:** Getestete Wiederherstellbarkeit.

## Arbeitspaket 4: Analysten-Pilot durchführen

**Ziel:** Das besondere Analysten-Template mit einem echten Beitrag testen.

Aufgaben:

1. Einen vorhandenen Patreon-Post oder eine vollständige Benachrichtigungs-E-Mail nach `Inbox/Analyst New` legen.
2. Text, Veröffentlichungsdatum, Instrument und Bild beziehungsweise Anhänge erfassen.
3. Analysten-Update nach Template als Markdown erzeugen.
4. Ergebnis nach `Inbox/Reviewed` legen.
5. Inhalt manuell prüfen und notwendige Templateänderungen notieren.

**Ergebnis:** Erstes geprüftes Analysten-Update und validiertes Template.

## Arbeitspaket 5: Allgemeinen PDF-Pilot durchführen

**Ziel:** Den Ablauf für Bücher, Studien und Research testen.

Aufgaben:

1. Ein kurzes PDF oder einzelnes Buchkapitel nach `Inbox/New` legen.
2. Quelle in NotebookLM laden.
3. Standardisierten Quellenanalyse-Prompt verwenden.
4. Ergebnis als Markdown nach `Inbox/Reviewed` übernehmen.
5. Quellenangaben, Kernaussagen, Risiken, Fundstellen und Taxonomiezuordnung prüfen.
6. Maximal drei bis fünf Wissensnotizen daraus ableiten.

**Ergebnis:** Erste vollständige Quellenanalyse und erste echte Wissensnotizen.

## Arbeitspaket 6: n8n-Pilot planen

**Ziel:** Nur die wiederkehrenden und validierten Schritte automatisieren.

Voraussetzung:

- mindestens ein funktionierender Analysten-Pilot,
- mindestens drei allgemeine oder insgesamt drei bis fünf Pilotquellen,
- stabile Templates.

Aufgaben:

1. Ersten automatisierten Eingang auswählen.
2. Trigger festlegen: Ordner oder E-Mail.
3. KI-Betriebsmodell festlegen: lokal, Cloud oder hybrid.
4. Ausgabe und Fehlerfälle definieren.
5. Minimalen Workflow bauen, der nur nach `Reviewed` schreibt.

**Ergebnis:** Sicherer Automatisierungspilot ohne ungeprüfte finale Ablage.

---

# 15. Direkt nächster Schritt

Als Nächstes wird nur **Arbeitspaket 1** bearbeitet.

Dafür werden die tatsächlichen Inhalte dieser beiden Dateien benötigt:

```text
Trading/Templates/Konventionen.md
Trading/Templates/Analysten Updates.md
```

Danach werden beide Dateien gemeinsam geprüft und bei Bedarf gezielt angepasst. Erst anschließend werden neue Templates und Ordner angelegt.

---

# 16. Anweisung für eine andere KI

Eine weiterarbeitende KI soll:

- diesen Plan als aktuellen Stand verwenden,
- ältere, umfangreichere Planstände nicht ungeprüft als bereits umgesetzt behandeln,
- klar zwischen erledigt, geplant und offen unterscheiden,
- ausschließlich im Bereich `Trading` arbeiten,
- bestehende Ordnernamen nicht ohne Not ändern,
- kleine, direkt ausführbare Schritte vorschlagen,
- pro Antwort nach Möglichkeit nur ein Arbeitspaket behandeln,
- keine große Automatisierung vor den Pilotprozessen bauen,
- KI-Ergebnisse zunächst nach `Trading/Inbox/Reviewed` schreiben,
- keine geprüften Dateien ungefragt überschreiben,
- keine Inhalte aus bezahlten Quellen öffentlich reproduzieren,
- den Nutzer nicht mit unnötig langen nächsten-Schritte-Listen überladen.
