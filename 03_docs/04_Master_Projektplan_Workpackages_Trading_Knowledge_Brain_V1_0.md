# Trading Knowledge Brain
## Master-Projektplan & Work Packages

**Granularer Umsetzungsplan für Version 1 mit Ausblick auf Version 2 und Version 3**  
**Version des Dokuments:** 1.0  
**Stand:** 26.10.2026  
**Projektfokus:** Fertigstellung einer stabilen, lokalen und produktiv nutzbaren Version 1

---

# 1. Zweck des Projektplans

Dieser Projektplan überführt das fachliche Zielbild und das technische Architekturkonzept in eine ausführbare Reihenfolge von Work Packages.

Er beantwortet:

- welche Produktversionen vorgesehen sind,
- was Version 1 fachlich und technisch umfasst,
- welche Arbeitspakete zur Fertigstellung von Version 1 notwendig sind,
- welche Abhängigkeiten bestehen,
- welche Ergebnisse und Tests je Work Package erwartet werden,
- wann ein Work Package als abgeschlossen gilt,
- welche Funktionen bewusst erst in Version 2 oder Version 3 umgesetzt werden.

Der Plan ist für die schrittweise Umsetzung mit n8n, Obsidian, Ollama, Docker und später weiteren lokalen Komponenten ausgelegt.

---

# 2. Projektregeln

1. Es wird immer nur das aktuell freigegebene Work Package umgesetzt.
2. Version-2- und Version-3-Funktionen werden nicht in Version 1 vorgezogen.
3. Vorhandene Flows werden analysiert und erweitert, nicht ohne Grund neu gebaut.
4. Tests werden gemeinsam mit der jeweiligen Funktion umgesetzt.
5. Nach jedem Work Package werden Änderungen, Tests, bekannte Probleme und der nächste Schritt dokumentiert.
6. Es erfolgen keine stillen Semantikänderungen an YAML-Feldern, Kategorien, Statuswerten oder Pfaden.
7. Alle n8n-Commands, Expressions, JavaScript-Blöcke und JSON-Strukturen werden vor Übergabe vollständig syntaktisch und strukturell geprüft.
8. Credentials werden nicht verändert, exportiert oder in Dateien eingebettet.
9. Alle automatisierten Schreibzugriffe bleiben unter:

```text
/vault/Finanzen/Trading
```

10. Historische Analystenupdates werden fachlich nicht überschrieben.
11. Aktuelle Statusdateien werden nur mit History-Sicherung ersetzt.
12. Ein Work Package gilt erst nach Erfüllung seiner Abnahmekriterien als abgeschlossen.
13. Fehlerpfade und Wiederanlauf gehören zum Scope der jeweiligen Funktion.
14. Keine ungeprüfte KI-Ausgabe wird unmittelbar zu endgültigem Wissen.
15. Vor größeren Schreib- oder Migrationsarbeiten muss ein funktionsfähiges Backup bestehen.
16. Die lokale, kostenfreie Architektur bleibt der Standardweg.
17. Geschützte Quellen werden nur privat verarbeitet und nicht in öffentliche Testdaten übernommen.
18. Der Projektplan wird nach jedem größeren Gate aktualisiert.

---

# 3. Produktversionen

## 3.1 Version 1: Local Knowledge Foundation

Version 1 ist die erste produktiv nutzbare lokale Version des Trading Knowledge Brain.

### Kernziel

Version 1 soll:

- den Obsidian-Vault als stabile Wissensbasis nutzen,
- laufende Analystenbeiträge automatisiert aus Gmail aufnehmen,
- technische, fundamentale und sonstige Beiträge unterscheiden,
- historische Updates je Ticker ablegen,
- aktuelle technische und fundamentale Statusdateien bilden,
- Analysteninhalte mit der Trading-Taxonomie verlinken,
- Bücher, Studien und PDFs strukturiert aufnehmen,
- daraus Quellenanalysen und Wissensnotiz-Entwürfe erzeugen,
- geprüfte Wissensnotizen kontrolliert in die bestehende Taxonomie einordnen,
- Backups, Logging, Tests und Dokumentation bereitstellen.

### Version-1-Grenze

Version 1 umfasst noch nicht:

- produktive RAG-Abfragen über Qdrant,
- tägliche Marktbriefings mit Live-Marktdaten,
- automatische Chartbildanalyse,
- automatische Handelsausführung,
- vollständige Journal- und Backtestintegration,
- mehrere Analystenquellen in produktiver Skalierung,
- Cloud- oder Multi-User-Betrieb.

## 3.2 Version 2: Semantic Research Assistant

Version 2 erweitert den stabilen Version-1-Bestand um:

- lokale Vektordatenbank,
- semantische Suche,
- RAG mit Quellenpfaden,
- inkrementelle Indexierung,
- verbesserte Concept-Link-Pflege,
- aktuelle Marktdatenadapter,
- tägliche und manuelle Research-Briefings,
- erste Einbindung eigener Strategien und Journalinhalte,
- mehrere Analystenquellen,
- begrenzte Chart- und OCR-Erweiterungen.

## 3.3 Version 3: Integrated Trading Research Platform

Version 3 kann später umfassen:

- tief integriertes Trading-Journal,
- Strategie- und Backtestdaten,
- Performanceanalyse,
- Vergleich eigener Ergebnisse mit Fach- und Analystenwissen,
- umfangreichere Marktdaten,
- automatisierte Watchlists und Alerts,
- fortgeschrittene Recherche- und Bewertungsmodelle,
- optional verteilten oder Cloud-Betrieb,
- optional mehrere Nutzer,
- optionale Paper-Trading-Integration.

Version 3 bleibt außerhalb des aktuellen Projektfokus.

---

# 4. Version-1-Zielzustand

Version 1 ist fachlich fertig, wenn folgende Kette stabil funktioniert:

```text
Analysten-E-Mail
→ strukturierte Review-Datei
→ manuelle Freigabe
→ historische Ablage je Ticker
→ chronologische Verlinkung
→ aktueller technischer oder fundamentaler Status
→ kontrollierte Fachlinks

Buch/Studie/PDF
→ lokale Extraktion beziehungsweise OCR-Entscheidung
→ abschnittsweise Analyse
→ Quellenanalyse im Review
→ manuelle Freigabe
→ Vorschläge für Wissensnotizen
→ manuelle Freigabe
→ finale Wissensnotiz und Indexlink
```

Zusätzlich müssen vorhanden sein:

- sichere Konfiguration,
- versionierte Data Contracts,
- Error Workflow,
- Logging,
- Backups,
- Test-Fixtures,
- Workflow-Exporte,
- Betriebsdokumentation.

---

# 5. Release-Struktur für Version 1

Version 1 wird in vier interne Ausbaustufen gegliedert.

## V1.0 Alpha: Analysten-Pipeline technisch stabil

- Flow 1 bis Flow 3 konsolidiert
- End-to-End-Tests
- Fehlerbehandlung
- Concept Registry angebunden
- sichere Status-History

## V1.0 Beta: Statische Quellenpipeline

- PDF-, TXT- und Markdown-Import
- Hashing
- Text-Extraktion
- OCR-Entscheidung
- Chunking
- Quellenanalyse

## V1.0 Release Candidate: Wissensnotizpipeline

- geprüfte Quellenanalysen
- Wissensnotiz-Vorschläge
- Dublettenprüfung
- kontrollierte finale Ablage
- Indexpflege

## V1.0 Final: Betrieb und Freigabe

- vollständiger Regressionstest
- Backup/Recovery
- Workflow-Exports
- Betriebsanleitung
- bekannte Einschränkungen
- Release Freeze

---

# 6. Work-Package-Übersicht

| WP | Name | Hauptscope | V1-Meilenstein |
|---:|---|---|---|
| 00 | Projektbaseline & V1 Scope Freeze | Ist-Stand, Backup, Flows, Pfade und Scope einfrieren | Alpha |
| 01 | Zentrale Konfiguration & Data Contracts | config.json, Schemas, Correlation IDs, Feldnamen | Alpha |
| 02 | Flow 1 Audit & Stabilisierung | Gmail, Extraktion, Ollama, Review-Schreiben | Alpha |
| 03 | Flow 2 Audit & Stabilisierung | Freigabe, Routing, Updates, Chronologie | Alpha |
| 04 | Flow 3 Audit & Stabilisierung | Statussynthese, History, sichere Ersetzung | Alpha |
| 05 | Concept Registry Integration | Konzepterkennung, kontrollierte Links, Aliasse | Alpha |
| 06 | Shared Sub-Workflows | Parser, Safe Write, Logging, Ollama JSON, Link Resolver | Alpha |
| 07 | Zentraler Error Workflow & Retry | Fehlerklassen, Error Trigger, Wiederanlauf | Alpha |
| 08 | Analysten-End-to-End-Testpaket | technische, fundamentale und sonstige Pfade | Alpha Gate |
| 09 | Analysten-Backfill & Datenbereinigung | bestehende NVDA- und weitere Pilotdaten migrieren | Alpha Gate |
| 10 | Dokumenteingang & Dateiinventar | Inbox/New, Discovery, Dateityp, Hashing | Beta |
| 11 | PDF/TXT/MD Text-Extraktion | Extraktion und Qualitätsprüfung | Beta |
| 12 | OCR-Decision & OCR-Pilot | Scanerkennung, OCRmyPDF/Tesseract PoC | Beta |
| 13 | Dokumentstruktur & Chunking | Kapitel, Seiten, Chunks, Metadaten | Beta |
| 14 | Chunk-Analyse mit Ollama | strukturierte Teilanalyse und Zwischenpersistenz | Beta |
| 15 | Quellenanalyse-Synthese | Map-Reduce, Template, Taxonomiezuordnung | Beta |
| 16 | Quellen-Review & finale Ablage | Freigabe, Books/PDFs/Research/Quellen | Beta Gate |
| 17 | Wissensnotiz-Kandidaten | create/extend/reference/duplicate/insufficient | RC |
| 18 | Bestehende Wissensnotizen & Dubletten | Pfad-, Alias- und Inhaltsprüfung | RC |
| 19 | Wissensnotiz-Entwürfe | Template, Quellen, Fundstellen, Review | RC |
| 20 | Wissensnotiz-Freigabe | finale Ablage nach Notes | RC |
| 21 | Index- und Registry-Aktualisierung | Indexlinks, preferred targets, Sicherung | RC Gate |
| 22 | Backup & Recovery Automation | Vault, n8n, Workflow-Exports, Restore | Final |
| 23 | Monitoring, Health & Operations | Health Checks, Logs, Start/Stop | Final |
| 24 | Datenschutz & Security Hardening | Scopes, Pfade, Secrets, geschützte Inhalte | Final |
| 25 | Performance & Long-Run Hardening | Locks, Batchgrößen, Timeout, Speicher | Final |
| 26 | V1 Regression & Systemabnahme | vollständige Cross-Flow-Tests | Final Gate |
| 27 | Dokumentation & Release Freeze | Handbuch, Known Issues, JSON-Exporte | V1 Final |

---

# 7. Detaillierte Work Packages

## WP 00: Projektbaseline & V1 Scope Freeze

### Ziel

Den tatsächlichen Ist-Zustand sichern und eine eindeutige Ausgangsbasis für alle weiteren Änderungen schaffen.

### Scope

- aktuellen Obsidian-Vault sichern
- n8n-Workflows exportieren
- aktuelle Flowversionen benennen
- Docker- und Ollama-Konfiguration dokumentieren
- reale Ordnerstruktur erfassen
- vorhandene Templates und Systemdateien inventarisieren
- V1-In-Scope und V1-Out-of-Scope verbindlich festhalten

### Lieferobjekte

```text
System/Automation/workflow-exports/Flow1_..._baseline.json
System/Automation/workflow-exports/Flow2_..._baseline.json
System/Automation/workflow-exports/Flow3_..._baseline.json
System/Automation/baseline-manifest.json
Backup des Trading-Bereichs
```

### Tests

- eine Datei aus Backup wiederherstellen
- alle drei Workflow-JSON-Dateien testweise importierbar
- n8n kann `Konventionen.md` lesen
- Ollama API ist erreichbar

### Abnahmekriterien

- keine ungesicherte Änderung mehr erforderlich
- Ist-Pfade sind bestätigt
- Scope Freeze ist dokumentiert

### Abhängigkeiten

Keine.

---

## WP 01: Zentrale Konfiguration & Data Contracts

### Ziel

Alle drei bestehenden Flows auf einheitliche Felder, Pfade, Kategorien und versionierte Übergabeobjekte ausrichten.

### Scope

- `config.json` anlegen
- JSON-Schema-Ordner anlegen
- Flow-1-Ausgabevertrag definieren
- Flow-2-zu-Flow-3-Vertrag definieren
- technische und fundamentale Statusschemas definieren
- standardisiertes Fehlerobjekt definieren
- Correlation ID einführen
- Workflow- und Promptversionen definieren

### Lieferobjekte

```text
System/Automation/config.json
System/Automation/schemas/analyst-update.schema.json
System/Automation/schemas/flow2-handoff.schema.json
System/Automation/schemas/technical-status.schema.json
System/Automation/schemas/fundamental-status.schema.json
System/Automation/schemas/error.schema.json
```

### Tests

- gültige Beispieldaten bestehen Schema-Validierung
- fehlende Pflichtfelder schlagen fehl
- unbekannte Kategorien schlagen fehl
- Pfade werden nur aus zentraler Konfiguration abgeleitet

### Abnahmekriterien

- Flow 1 bis Flow 3 verwenden dieselben Feldnamen
- `Technisch`, `Fundamental`, `Sonstige` sind die einzigen Produktivkategorien
- `TheLongInvestor` ist der feste Ordnername

### Abhängigkeiten

WP 00.

---

## WP 02: Flow 1 Audit & Stabilisierung

### Ziel

Den vorhandenen Gmail-Extraktionsflow gegen Fach- und Architekturkonzept prüfen und produktionsfähig stabilisieren.

### Scope

- Gmail Trigger und Labels prüfen
- vollständigen Message-Abruf prüfen
- `post-content`-Extraktion prüfen
- HTML-, Tracking- und Footer-Bereinigung prüfen
- Quellenvalidierung prüfen
- Gmail Message ID als Dublettenschlüssel absichern
- Ollama-Verbindung und JSON-Schema prüfen
- Kategorie- und Ticker-Normalisierung prüfen
- Markdown-Renderer prüfen
- Review-Datei und Dateikonflikte prüfen
- Gmail-Labelabschluss absichern
- Correlation ID ergänzen

### Lieferobjekte

- aktualisierte Flow-1-JSON
- dokumentierter Prompt
- Test-Fixtures für mindestens drei Kategorien
- Liste bekannter Einschränkungen

### Tests

- technischer Post
- fundamentaler Post
- sonstiger Post
- Vorschau statt Volltext
- falscher Absender
- leere Nachricht
- Gmail-Dublette
- ungültiges Ollama-JSON
- Ollama Timeout
- Sonderzeichen und Umlaute

### Abnahmekriterien

- genau eine valide Review-Datei je gültiger Gmail Message ID
- Originalinhalt bleibt erhalten
- ungültige Nachrichten erzeugen keine finale Datei
- Gmail-Status wird nur nach erfolgreichem Commit geändert

### Abhängigkeiten

WP 01.

---

## WP 03: Flow 2 Audit & Stabilisierung

### Ziel

Den Routing-, Historisierungs- und Verlinkungsflow produktionsfähig machen.

### Scope

- nur `status: geprüft` verarbeiten
- YAML robust parsen
- Felder gegen Schema validieren
- Kategorien routen
- Ticker normalisieren
- Zielordner idempotent erzeugen
- Update sicher und ohne Überschreiben ablegen
- chronologische Sortierung implementieren
- Vorgänger und Nachfolger neu berechnen
- Historienliste aktualisieren
- Sonstige-Zweig umsetzen
- Flow-3-Handoff erzeugen
- Commit- und Terminated-Regeln klären

### Lieferobjekte

- aktualisierte Flow-2-JSON
- Routing- und Chronologie-Testfixtures
- dokumentierte Transaktionsgrenze

### Tests

- neuer Ticker
- vorhandener Ticker
- späteres Update
- älteres nachträgliches Update
- identisches Datum
- fehlender Ticker
- ungültige Kategorie
- Dateinamenskonflikt
- vorhandene Gmail Message ID

### Abnahmekriterien

- kein historisches Update wird fachlich überschrieben
- Chronologie ist unabhängig von Importreihenfolge korrekt
- Sonstige erzeugt keine unnötige Statusstruktur
- Flow-3-Handoff entspricht Schema

### Abhängigkeiten

WP 01, WP 02.

---

## WP 04: Flow 3 Audit & Stabilisierung

### Ziel

Sichere technische und fundamentale Statuskonsolidierung implementieren.

### Scope

- Flow-2-Eingang erneut validieren
- alle Updates laden und sortieren
- bestehenden Status laden
- technischen und fundamentalen Prompt trennen
- strukturiertes JSON statt freien Markdown-Output verwenden
- Änderungslogik implementieren
- Quellenliste validieren
- Status-Renderer aufbauen
- bestehende Statusdatei nach `_History` sichern
- temporäres Schreiben und sichere Ersetzung
- Statuslauf idempotent machen

### Lieferobjekte

- aktualisierte Flow-3-JSON
- technische und fundamentale Statusprompts
- erwartete Status-Fixtures

### Tests

- erster technischer Status
- zweites technisches Update
- widersprüchliche Aussage
- nicht mehr erwähnte alte Aussage
- ausdrücklich aufgehobene Aussage
- erster fundamentaler Status
- Flow-Abbruch vor finalem Rename
- beschädigter bisheriger Status

### Abnahmekriterien

- bestehender Status bleibt bei Fehler unverändert
- History-Datei entsteht vor Ersetzung
- neuester Status verwendet korrektes Veröffentlichungsdatum
- alle verwendeten Updates sind verlinkt

### Abhängigkeiten

WP 01, WP 03.

---

## WP 05: Concept Registry Integration

### Ziel

`concept-links.json` zur aktiven Laufzeitkomponente machen.

### Scope

- Registry in Flow 1 bis 3 einlesen
- erkannte Konzepte gegen Register validieren
- Aliasse ergänzen
- mehrfach vorkommende Begriffe behandeln
- Zielpfade normalisieren und auf Existenz prüfen
- Fallback auf Hauptthemenindex
- separaten Linkabschnitt erzeugen
- ungelöste Begriffe protokollieren

### Lieferobjekte

- aktualisierte `concept-links.json`
- Aliasregeln
- Concept-Link-Testfixtures
- ergänzte Flowversionen

### Tests

- exakter Begriff
- deutscher Alias
- englischer Alias
- unbekannter Begriff
- toter Zielpfad
- doppelte Konzepte
- mehrfach zugeordnetes Konzept
- kurzer Post ohne Konzepte

### Abnahmekriterien

- KI erzeugt keine freien Pfade
- keine toten Links
- Originalinhalt bleibt unverändert
- jeder Ziel-Link höchstens einmal

### Abhängigkeiten

WP 02, WP 03, WP 04.

---

## WP 06: Shared Sub-Workflows

### Ziel

Wiederverwendbare technische Funktionen aus den Hauptflows auslagern.

### Scope

- Markdown/YAML Parser
- Ollama JSON Wrapper
- Safe Write
- JSONL Logger
- Concept Link Resolver
- Error Normalizer

### Lieferobjekte

```text
SWF_Parse_Validate_Markdown.json
SWF_Ollama_JSON.json
SWF_Safe_Write.json
SWF_JSONL_Log.json
SWF_Resolve_Concept_Links.json
SWF_Error_Normalize.json
```

### Tests

- definierte Input- und Outputverträge
- ungültige Inputs
- Timeout
- bestehende Datei
- Backupmodus
- beschädigte Registry

### Abnahmekriterien

- Hauptflows enthalten keine unnötig duplizierte Kernlogik
- Sub-Workflows sind einzeln testbar
- Fehlerpropagation ist eindeutig

### Abhängigkeiten

WP 01 bis WP 05.

---

## WP 07: Zentraler Error Workflow & Retry

### Ziel

Einheitliche Fehlerbehandlung für alle Version-1-Flows.

### Scope

- Error Trigger Workflow
- Fehlernormalisierung
- Retryable/Non-Retryable Klassifikation
- maximal drei Wiederholungen
- Error-Label für Gmail
- Fehlerdatei unter `_Errors`
- keine Endlosschleifen
- Status `status_pending` für Flow-3-Fehler nach erfolgreichem Updatecommit

### Lieferobjekte

```text
ErrorHandler_Zentral.json
Fehlercode-Katalog.md
Retry-Policy.md
```

### Tests

- Ollama Timeout
- Gmail Fehler
- fehlender Mount
- ungültiges YAML
- fehlender Ticker
- Status-Fehler nach Updatecommit

### Abnahmekriterien

- Fehlerzustand ist nachvollziehbar
- kein Teilerfolg wird als Gesamterfolg ausgegeben
- gültige Updates werden bei Statusfehler nicht dupliziert

### Abhängigkeiten

WP 06.

---

## WP 08: Analysten-End-to-End-Testpaket

### Ziel

Flow 1 bis Flow 3 gemeinsam gegen ein verbindliches Testpaket prüfen.

### Scope

- anonymisierte Gmail-Fixtures
- Review-Fixtures
- erwartete Update- und Statusdateien
- automatisierte oder dokumentierte Testabläufe
- Regressionstest nach jedem Fix

### Testfälle

1. neuer technischer Ticker
2. zweites technisches Update
3. nachträglich älteres Update
4. fundamentaler Beitrag
5. sonstiger Beitrag
6. Gmail-Dublette
7. Dateinamenskonflikt
8. ungültiges YAML
9. fehlender Ticker
10. Ollama-Ausfall
11. Registry-Ausfall
12. Status-History
13. Neustart und Wiederanlauf

### Lieferobjekte

```text
System/Automation/test-fixtures/
Testprotokoll_Analystenpipeline.md
Known_Issues_Alpha.md
```

### Abnahmekriterien

- alle kritischen Tests bestanden
- keine Daten außerhalb Trading verändert
- keine kritische offene Inkonsistenz

### Abhängigkeiten

WP 02 bis WP 07.

---

## WP 09: Analysten-Backfill & Datenbereinigung

### Ziel

Bereits vorhandene Pilot- und Analystendaten in den stabilen V1-Stand überführen.

### Scope

- NVDA-Pilotdateien prüfen
- YAML an aktuelles Schema anpassen
- chronologische Links neu erzeugen
- Status neu bilden
- Concept Links ergänzen
- Duplikate erkennen
- unbestätigte Daten markieren

### Lieferobjekte

- bereinigter NVDA-Probestand
- Backfill-Protokoll
- Migrationsreport

### Tests

- Status aus Updates vollständig rekonstruierbar
- ältere Dateien bleiben erhalten
- keine Dubletten

### Abnahmekriterien

- Pilotdaten entsprechen produktivem Schema
- Alpha Gate bestanden

### Abhängigkeiten

WP 08.

---

## WP 10: Dokumenteingang & Dateiinventar

### Ziel

Sicheren Eingang für Bücher, Studien und allgemeine Dokumente schaffen.

### Scope

- `Inbox/New` lesen
- erlaubte Dateitypen
- SHA-256-Hash
- Dateigröße
- MIME-/Erweiterungsprüfung
- Duplikatmanifest
- Work-Verzeichnis je Hash
- Statusmanifest

### Lieferobjekte

```text
Flow4_Dokumente_Inventarisieren.json
source-manifest.schema.json
```

### Tests

- PDF
- TXT
- Markdown
- nicht erlaubter Dateityp
- identische Datei mit anderem Namen
- gleiche Datei erneut

### Abnahmekriterien

- jede Quelle hat eindeutigen Hash
- keine inhaltliche Verarbeitung bei Dublette
- Original wird nicht verändert

### Abhängigkeiten

WP 00, WP 01, WP 07.

---

## WP 11: PDF/TXT/MD Text-Extraktion

### Ziel

Lesbaren Rohtext und technische Extraktionsmetadaten erzeugen.

### Scope

- PDF-Extraktion
- TXT/MD-Einlesen
- UTF-8-Normalisierung
- Seiten-/Textmenge erfassen
- Extraktionsqualität bewerten
- Rohtext zwischenspeichern

### Lieferobjekte

```text
Flow5_Dokumenttext_Extrahieren.json
Extraction_Result_Schema.json
```

### Tests

- normales Text-PDF
- PDF mit Tabellen
- leere PDF
- fehlerhafte Zeichen
- großes Buch

### Abnahmekriterien

- Text nachvollziehbar extrahiert
- Seitenbezug soweit möglich erhalten
- unzureichende Extraktion wird erkannt

### Abhängigkeiten

WP 10.

---

## WP 12: OCR-Decision & OCR-Pilot

### Ziel

Gescannte Dokumente erkennen und einen lokalen OCR-Weg validieren.

### Scope

- Textdichte-Schwellenwert
- `ocr_erforderlich`
- Vergleich OCRmyPDF und Tesseract
- verarbeitete OCR-Datei separat speichern
- Original erhalten

### Lieferobjekte

- OCR-PoC
- Entscheidung für OCR-Werkzeug
- OCR-Testprotokoll

### Tests

- gescannte deutsche Seite
- englische Buchseite
- gemischtes Text-/Bild-PDF
- schlechte Scanqualität

### Abnahmekriterien

- OCR-Bedarf zuverlässig erkannt
- lokaler OCR-Weg dokumentiert
- keine still leere Analyse

### Abhängigkeiten

WP 11.

---

## WP 13: Dokumentstruktur & Chunking

### Ziel

Vollständige Bücher und Studien in analysierbare, nachvollziehbare Abschnitte zerlegen.

### Scope

- Kapitelüberschriften
- Inhaltsverzeichnis
- Seitenbereiche
- Chunkgröße und Overlap
- Heading Path
- Chunkmanifest
- strukturbasiertes Chunking mit Fallback

### Lieferobjekte

```text
Flow6_Dokument_Strukturieren_und_Chunking.json
chunk.schema.json
```

### Tests

- Buch mit Inhaltsverzeichnis
- Studie mit Abschnitten
- Dokument ohne klare Überschriften
- sehr langes Kapitel

### Abnahmekriterien

- jeder Chunk besitzt Dokument-, Seiten- und Abschnittsbezug
- Chunks überschreiten Modellgrenzen nicht

### Abhängigkeiten

WP 11, optional WP 12.

---

## WP 14: Chunk-Analyse mit Ollama

### Ziel

Jeden Dokumentabschnitt strukturiert und wiederaufnehmbar analysieren.

### Scope

- Quellenanalyse-Prompt
- JSON-Schema je Chunk
- Konzepte und Regeln
- Evidenz und Einschränkungen
- Fundstellen
- Taxonomiebegriffe
- Zwischenpersistenz
- Wiederanlauf ab fehlgeschlagenem Chunk

### Lieferobjekte

```text
Flow7_Dokumentchunks_Analysieren.json
chunk-analysis.schema.json
source-analysis-prompt-v1.md
```

### Tests

- Grundlagenkapitel
- empirische Studie
- widersprüchliche Passage
- unvollständiger Chunk
- Ollama-Abbruch in der Mitte

### Abnahmekriterien

- keine komplette Neuverarbeitung nach Einzelfehler
- Aussagen enthalten Fundstellen
- strukturierte Outputs sind validiert

### Abhängigkeiten

WP 13, WP 06, WP 07.

---

## WP 15: Quellenanalyse-Synthese

### Ziel

Chunk- und Kapitelanalysen zu einer konsistenten Gesamtquellenanalyse zusammenführen.

### Scope

- Kapitel-Reduce
- Dokument-Reduce
- Redundanzbereinigung
- Quellenstruktur erhalten
- Taxonomiezuordnung
- A/B/C-Bezüge
- Wissensnotiz-Vorschläge
- Markdown-Renderer

### Lieferobjekte

```text
Flow8_Quellenanalyse_Synthetisieren.json
Quellenanalyse-Output gemäß Template
```

### Tests

- vollständiges Buch
- wissenschaftliche Studie
- Quelle mit mehreren Hauptthemen
- Quelle mit widersprüchlichen Aussagen

### Abnahmekriterien

- Gesamtanalyse ist aus Teilanalysen rekonstruierbar
- keine erfundenen Aussagen
- Fundstellen bleiben nachvollziehbar

### Abhängigkeiten

WP 14.

---

## WP 16: Quellen-Review & finale Ablage

### Ziel

Geprüfte Quellenanalysen und Originalquellen kontrolliert einsortieren.

### Scope

- `status: geprüft`
- Originaltyp bestimmen
- Original nach Books/PDFs/Research
- Quellenanalyse nach Research/Quellen
- Dateikonflikt
- Hashlog
- Terminated-Spur

### Lieferobjekte

```text
Flow9_Quellen_Freigeben_und_Ablegen.json
```

### Tests

- Buch
- Studie
- allgemeines PDF
- Dublette
- fehlende Metadaten

### Abnahmekriterien

- Original und Analyse sind verlinkt
- keine Originalquelle wird gelöscht
- Beta Gate bestanden

### Abhängigkeiten

WP 15.

---

## WP 17: Wissensnotiz-Kandidaten

### Ziel

Aus geprüften Quellenanalysen fachlich belastbare Wissensnotiz-Kandidaten erzeugen.

### Scope

- Konzepte extrahieren
- Taxonomie matchen
- Substanz prüfen
- Entscheidungsklassen erzeugen
- Evidenzstellen sammeln

### Entscheidungswerte

```text
create
extend
reference_only
duplicate
insufficient
```

### Lieferobjekte

```text
Flow10_Wissensnotiz_Kandidaten.json
knowledge-candidate.schema.json
```

### Tests

- starkes Einzelkonzept
- bloße Erwähnung
- mehrfaches Konzept
- unbekannter Begriff

### Abnahmekriterien

- keine leeren Massennotizen
- jede Entscheidung nachvollziehbar

### Abhängigkeiten

WP 16, WP 05.

---

## WP 18: Bestehende Wissensnotizen & Dubletten

### Ziel

Verhindern, dass bestehendes Wissen unnötig dupliziert wird.

### Scope

- Dateinamen
- Aliasse
- Concept Registry
- Hauptthemenindizes
- einfache Inhaltsähnlichkeit
- Merge-Entscheidung

### Lieferobjekte

```text
SWF_Knowledge_Duplicate_Check.json
Dublettenregeln.md
```

### Tests

- exakter Dateiname
- Alias
- ähnliche, aber andere Konzepte
- vorhandener Index ohne Detailnotiz

### Abnahmekriterien

- falsche Zusammenführungen werden vermieden
- unklare Fälle landen im Review

### Abhängigkeiten

WP 17.

---

## WP 19: Wissensnotiz-Entwürfe

### Ziel

Neue Notizen und Merge-Vorschläge im vorgesehenen Template erzeugen.

### Scope

- `Wissensnotiz.md`
- Kurzdefinition
- Kernaussagen
- Funktionsweise
- Regeln
- Risiken
- Beispiele
- Quellen und Fundstellen
- Quellenpositionen
- verwandte Themen

### Lieferobjekte

```text
Flow11_Wissensnotiz_Entwuerfe.json
```

### Tests

- neue Notiz
- Ergänzungsvorschlag
- mehrere Quellenpositionen
- Quellenkonflikt

### Abnahmekriterien

- jeder Entwurf enthält Quellen
- kein bestehendes Wissen wird direkt überschrieben

### Abhängigkeiten

WP 18.

---

## WP 20: Wissensnotiz-Freigabe

### Ziel

Geprüfte Wissensnotizen in den passenden Notes-Ordner überführen.

### Scope

- `status: geprüft`
- primäres Hauptthema
- Zielpfad
- Dateikonflikt
- Safe Write
- Merge-Vorschlag manuell freigegeben

### Lieferobjekte

```text
Flow12_Wissensnotizen_Freigeben.json
```

### Tests

- neue Datei
- vorhandene Datei
- unklare Hauptthemenzuordnung
- ungültiger Pfad

### Abnahmekriterien

- nur geprüfte Notizen final
- keine ungeprüfte Überschreibung

### Abhängigkeiten

WP 19.

---

## WP 21: Index- und Registry-Aktualisierung

### Ziel

Nach Freigabe einer Wissensnotiz Navigation und Linkziele kontrolliert aktualisieren.

### Scope

- Hauptthemenindex sichern
- A/B/C-Eintrag finden
- Text in Obsidian-Link umwandeln
- `concept-links.json` preferred target setzen
- Fallback erhalten
- Änderung protokollieren

### Lieferobjekte

```text
Flow13_Index_und_Concept_Registry_Aktualisieren.json
```

### Tests

- eindeutiger Begriff
- mehrfach vorkommender Begriff
- Begriff nicht gefunden
- bereits verlinkter Begriff
- Registry-Update

### Abnahmekriterien

- Index bleibt syntaktisch intakt
- keine falsche Taxonomieposition
- RC Gate bestanden

### Abhängigkeiten

WP 20.

---

## WP 22: Backup & Recovery Automation

### Ziel

Version-1-Daten und Automatisierung wiederherstellbar machen.

### Scope

- Vault-Backup
- n8n-Workflow-Export
- n8n_data-Sicherung
- Config, Schemas und Prompts
- Restore-Check
- Backup-Retention

### Lieferobjekte

- Backup-Workflow oder PowerShell-Skript
- Recovery-Runbook
- dokumentierter Wiederherstellungstest

### Tests

- einzelne Datei
- Tickerordner
- Workflow-Import
- Statusrekonstruktion

### Abnahmekriterien

- Wiederherstellung nachgewiesen
- Backups getrennt vom aktiven Vault

### Abhängigkeiten

WP 09, WP 21.

---

## WP 23: Monitoring, Health & Operations

### Ziel

Den täglichen lokalen Betrieb transparent und einfach machen.

### Scope

- n8n Health
- Ollama Health
- Vault Mount
- Gmail Credential Test
- benötigte Modellprüfung
- Logrotation
- Start-/Stop-Skript
- täglicher Betriebscheck

### Lieferobjekte

```text
Start-Trading-Knowledge-Brain.ps1
HealthCheck-Trading-Knowledge-Brain.ps1
Betriebshandbuch.md
```

### Tests

- Docker gestoppt
- Ollama gestoppt
- Modell fehlt
- Vault nicht gemountet
- Gmail Credential ungültig

### Abnahmekriterien

- Nutzer erkennt Systemzustand vor Workflowstart
- Fehler sind verständlich

### Abhängigkeiten

WP 07.

---

## WP 24: Datenschutz & Security Hardening

### Ziel

Technische Risiken vor V1-Freigabe reduzieren.

### Scope

- Gmail Scopes
- Credentials
- Pfadtraversal
- erlaubte Dateitypen
- keine Secrets in Logs
- HTML-Sanitizing
- private Testdaten
- Claude/MCP-Berechtigungen

### Lieferobjekte

- Security Checklist
- Credential Inventory ohne Secretwerte
- dokumentierte Pfad-Allowlist

### Tests

- Pfad mit `..`
- unzulässige Erweiterung
- Secret in Logfixture
- Zugriff außerhalb Trading

### Abnahmekriterien

- keine kritische offene Sicherheitslücke
- keine geschützten Volltexte in öffentlichem Export

### Abhängigkeiten

WP 01 bis WP 23.

---

## WP 25: Performance & Long-Run Hardening

### Ziel

Längere lokale Läufe auf vorhandener Hardware stabil machen.

### Scope

- Batchgröße 1
- Ticker Locks
- Stale Lock Handling
- Timeouts
- Speicherverbrauch
- Chunk-Wiederanlauf
- Loggröße
- große Bücher

### Lieferobjekte

- Performance-Testbericht
- Grenzwerte in config.json
- Lock-Mechanismus

### Tests

- mehrere Gmail-Mails
- parallele Updates eines Tickers
- großes Buch
- Abbruch und Neustart
- langer Ollama-Lauf

### Abnahmekriterien

- kein unkontrollierter Parallelzugriff
- Wiederanlauf ohne komplette Neuverarbeitung

### Abhängigkeiten

WP 08, WP 15, WP 21.

---

## WP 26: V1 Regression & Systemabnahme

### Ziel

Das Gesamtsystem gegen alle V1-Anforderungen prüfen.

### Scope

- Analystenpipeline
- statische Quellenpipeline
- Wissensnotizpipeline
- Backup
- Security
- Operations
- Cross-Flow-Regression

### Lieferobjekte

- V1-Abnahmeprotokoll
- vollständige Testmatrix
- offene Known Issues
- Release-Empfehlung

### Acceptance Gates

- keine kritischen Datenverlustrisiken
- Flow 1 bis 3 komplett grün
- mindestens ein vollständiges Buch verarbeitet
- mindestens eine Studie verarbeitet
- Wissensnotiz final abgelegt und Index aktualisiert
- Backup und Restore bestanden
- kritische Security-Tests bestanden

### Abhängigkeiten

WP 09 bis WP 25.

---

## WP 27: Dokumentation & Release Freeze

### Ziel

Version 1 als reproduzierbaren, dokumentierten Stand einfrieren.

### Scope

- Fachkonzept aktualisieren
- Architekturkonzept aktualisieren
- Projektplan aktualisieren
- Workflow-JSON exportieren
- Installationsanleitung
- Betriebshandbuch
- Recovery-Runbook
- Known Issues
- Versionskennzeichnung

### Lieferobjekte

```text
V1_Release_Manifest.json
V1_Release_Notes.md
Workflow-Exports
Dokumentationspaket
```

### Abnahmekriterien

- V1 aus Dokumentation und Backup rekonstruierbar
- keine ungeklärte kritische Abweichung
- Release Freeze erklärt und bestätigt

### Abhängigkeiten

WP 26.

---

# 8. Hauptabhängigkeiten

```text
WP 00 → alle weiteren Work Packages
WP 01 → WP 02, 03, 04, 06, 07
WP 02 → WP 03
WP 03 → WP 04
WP 02–04 → WP 05
WP 01–05 → WP 06
WP 06 → WP 07
WP 02–07 → WP 08
WP 08 → WP 09
WP 10 → WP 11
WP 11 → WP 12 und WP 13
WP 12 optional → WP 13
WP 13 → WP 14 → WP 15 → WP 16
WP 16 → WP 17 → WP 18 → WP 19 → WP 20 → WP 21
WP 09 und WP 21 → WP 22
WP 07 → WP 23
WP 01–23 → WP 24
WP 08, 15, 21 → WP 25
WP 09–25 → WP 26
WP 26 → WP 27
```

## Kritischer Pfad

```text
WP 00
→ WP 01
→ WP 02
→ WP 03
→ WP 04
→ WP 05
→ WP 06
→ WP 07
→ WP 08
→ WP 09
→ WP 10
→ WP 11
→ WP 13
→ WP 14
→ WP 15
→ WP 16
→ WP 17
→ WP 18
→ WP 19
→ WP 20
→ WP 21
→ WP 22
→ WP 26
→ WP 27
```

---

# 9. Meilensteine und Acceptance Gates

## Gate A: Baseline Ready

Erforderlich:

- Backup vorhanden
- drei Flow-JSONs exportiert
- Ist-Pfade bestätigt
- V1-Scope eingefroren

Zugehöriges WP:

```text
WP 00
```

## Gate B: Analyst Pipeline Alpha

Erforderlich:

- Flow 1 bis 3 Datenverträge vereinheitlicht
- Gmail Import stabil
- Routing korrekt
- Status-History
- Concept Links
- Error Workflow
- End-to-End-Testpaket bestanden
- Pilotdaten migriert

Zugehörige WPs:

```text
WP 01–09
```

## Gate C: Static Source Beta

Erforderlich:

- Datei-Hashing
- PDF/TXT/MD-Extraktion
- OCR-Entscheidung
- Chunking
- Teilanalysen
- Quellenanalyse
- finale Quellenablage

Zugehörige WPs:

```text
WP 10–16
```

## Gate D: Knowledge Release Candidate

Erforderlich:

- Wissensnotiz-Kandidaten
- Dublettenprüfung
- Entwürfe
- Freigabe
- Index und Registry aktualisiert

Zugehörige WPs:

```text
WP 17–21
```

## Gate E: V1 Operational Readiness

Erforderlich:

- Backup und Recovery
- Health Checks
- Security Hardening
- Performance Hardening

Zugehörige WPs:

```text
WP 22–25
```

## Gate F: Version 1 Release

Erforderlich:

- vollständige Regression
- Abnahmeprotokoll
- Workflow-Exporte
- Dokumentation
- Release Freeze

Zugehörige WPs:

```text
WP 26–27
```

---

# 10. Priorisierung

## Priorität P0: Muss für V1

- WP 00–09
- WP 10–16
- WP 17–22
- WP 26–27

## Priorität P1: Muss vor finalem Release, kann parallel vorbereitet werden

- WP 23
- WP 24
- WP 25

## Nicht in V1

- Qdrant-RAG
- Live-Marktdaten
- Daily Briefing
- Vision-/Chartanalyse
- vollständiges Journal
- Backtesting
- mehrere Nutzer

---

# 11. Empfohlene Umsetzungsblöcke

## Block 1: Analystenpipeline fertigstellen

```text
WP 00–09
```

Ergebnis:

- produktive Aufnahme und Statuspflege von Analystenbeiträgen

## Block 2: Literatur- und Dokumentenpipeline

```text
WP 10–16
```

Ergebnis:

- vollständige Bücher und Studien werden zu geprüften Quellenanalysen

## Block 3: Wissensaufbau

```text
WP 17–21
```

Ergebnis:

- geprüfte Quellen werden zu dauerhaftem, verlinktem Wissen

## Block 4: Betriebsreife

```text
WP 22–27
```

Ergebnis:

- gesichertes, getestetes und dokumentiertes Version-1-System

---

# 12. Version-2-Backlog

Version 2 beginnt erst nach Release Freeze von Version 1.

## Mögliche Workstreams

1. Qdrant und lokale Embeddings
2. RAG Indexer
3. Retrieval Chat mit Quellenpfaden
4. automatische Link-Wartung und Backfill
5. aktuelle Marktdatenadapter
6. tägliches Research-Briefing
7. Mehrquellenvergleich von Analysten
8. OCR- und Chartbildausbau
9. erste Journalintegration
10. semantische Dublettenerkennung

## Version-2-Gate

Version 2 ist erst gerechtfertigt, wenn:

- ausreichend geprüfte Inhalte vorhanden sind,
- Version 1 stabil betrieben wird,
- reale Abfragefälle dokumentiert sind,
- semantische Suche einen klaren Mehrwert gegenüber Obsidian und Claude MCP bietet.

---

# 13. Version-3-Backlog

Mögliche Themen:

- vollständiges Trading-Journal
- Strategiebibliothek
- Backtests und Performanceanalyse
- Vergleich eigener Trades mit Wissensbasis
- Watchlists und Alerts
- Paper-Trading-Integration
- mehrere Analysten und Researchquellen
- Portfolioanalyse
- Cloud- oder Multi-User-Betrieb
- weitergehende Agenten- und Forschungsfunktionen

Version 3 ist keine Voraussetzung für den Nutzen von Version 1 oder Version 2.

---

# 14. Releasekriterien Version 1

Version 1 darf nur freigegeben werden, wenn:

- alle P0-Work-Packages abgeschlossen sind,
- alle Acceptance Gates bestanden sind,
- keine kritische offene Datenverlustgefahr besteht,
- Backups und Restore funktionieren,
- Analystenpipeline End-to-End läuft,
- mindestens ein vollständiges Buch verarbeitet wurde,
- mindestens eine wissenschaftliche Studie verarbeitet wurde,
- mindestens eine Wissensnotiz aus einer geprüften Quelle final abgelegt wurde,
- ein Themenindex kontrolliert aktualisiert wurde,
- alle produktiven Workflows exportiert sind,
- bekannte Einschränkungen dokumentiert sind,
- keine Daten außerhalb `Finanzen/Trading` verändert werden,
- Credentials nicht offengelegt werden,
- Release-Dokumentation vollständig ist.

---

# 15. Work-Package-Abschlussbericht

Nach jedem WP wird eine kurze Abschlussdatei erstellt:

```markdown
# WP XX Abschluss

## Umgesetzte Änderungen

## Geänderte Dateien und Workflows

## Durchgeführte Tests

## Testergebnisse

## Bekannte Probleme

## Abweichungen vom Konzept

## Neue Risiken

## Nächster freigegebener Schritt
```

Ablage:

```text
Trading/System/Automation/workpackages/WP_XX_Abschluss.md
```

---

# 16. Direkter Projektstart ab aktuellem Stand

Da bereits drei Flows vorhanden sind, beginnt die Umsetzung nicht bei null.

Der nächste konkrete Ablauf lautet:

```text
WP 00: Baseline und Backup
→ WP 01: reale Flowfelder und Datenverträge vereinheitlichen
→ WP 02: Flow 1 prüfen
→ WP 03: Flow 2 prüfen
→ WP 04: Flow 3 prüfen
→ WP 05: Concept Registry final anbinden
→ WP 06–07: gemeinsame Sub-Workflows und Fehlerbehandlung
→ WP 08: gesamter Analystentest
→ WP 09: NVDA- und Pilotdaten bereinigen
```

Erst danach startet die Bücher- und Studienpipeline mit WP 10.

---

# 17. Kurzplan

```text
V1 Alpha:
Analysten-E-Mails → Updates → aktueller Status → Fachlinks

V1 Beta:
Bücher/Studien/PDFs → Quellenanalysen

V1 Release Candidate:
Quellenanalysen → Wissensnotizen → Indexlinks

V1 Final:
Backups, Tests, Security, Betrieb, Dokumentation

V2:
RAG, semantische Suche, Marktdaten, Briefings

V3:
Journal, Backtests, Performance, Alerts, erweiterte Plattform
```
