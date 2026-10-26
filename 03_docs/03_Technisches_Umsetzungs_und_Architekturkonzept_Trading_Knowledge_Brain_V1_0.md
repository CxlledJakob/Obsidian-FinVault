# Trading Knowledge Brain
## Technisches Umsetzungs- und Architekturkonzept

**Zielarchitektur, Komponenten, Datenverträge, Workflow-Design, Betrieb, Sicherheit und technische Roadmap**  
**Version:** 1.0  
**Stand:** 26.10.2026  
**Dokumentstatus:** Technische Umsetzungsgrundlage  
**Bezug:** Master-Fachkonzept `02_Master_Fachkonzept_Obsidian_Trading_Knowledge_Brain_V1_0.md`

---

# 1. Zweck und technische Leitfrage

Dieses Dokument beschreibt nicht primär, **was** das Trading Knowledge Brain fachlich leisten soll, sondern **wie** das fachliche Zielbild technisch umgesetzt wird.

Es legt fest:

- die technische Zielarchitektur,
- Komponenten und Verantwortungsgrenzen,
- Speicher- und Pfadkonventionen,
- Datenverträge zwischen Workflows,
- konkrete Verarbeitungspipelines,
- Validierung und Zustandsübergänge,
- sichere Schreib- und Historisierungsverfahren,
- KI- und Modellintegration,
- Deployment und lokaler Betrieb,
- Fehlerbehandlung, Logging und Wiederanlauf,
- Teststrategie,
- spätere Dokumenten-, RAG- und Briefing-Architektur.

Das Dokument ist die technische Umsetzungsvorgabe für n8n-Workflow-Entwicklung, Obsidian-Integration, lokale KI-Komponenten und spätere Erweiterungen.

---

# 2. Architekturziele

## 2.1 Primäre Ziele

1. **Lokale Datenhoheit:** Dauerhafte Inhalte bleiben im lokalen Obsidian-Vault.
2. **Modulare Automatisierung:** Jeder Flow besitzt eine klar abgegrenzte Verantwortung.
3. **Nachvollziehbarkeit:** Jeder Verarbeitungsschritt ist über IDs, Pfade, Status und Logs nachvollziehbar.
4. **Idempotenz:** Wiederholte Ausführung erzeugt keine unkontrollierten Dubletten.
5. **Historisierung:** Analystenupdates und Statusversionen bleiben nachvollziehbar.
6. **Kontrollierte KI:** KI extrahiert und strukturiert; deterministische Logik validiert, routet und schreibt.
7. **Sichere Dateiverarbeitung:** Keine unvollständigen oder still überschriebenen Dateien.
8. **Erweiterbarkeit:** Bücher-, Studien-, RAG- und Briefing-Flows lassen sich ergänzen, ohne Flow 1 bis 3 neu zu entwickeln.
9. **Kostenkontrolle:** Standardbetrieb ohne tokenbasierte Cloud-KI-Kosten.
10. **Windows-first:** Die Lösung muss auf dem vorhandenen Windows-Rechner praktikabel laufen.

## 2.2 Qualitätsziele

| Qualitätsmerkmal | Technische Umsetzung |
|---|---|
| Wartbarkeit | kleine Flows, Sub-Workflows, zentrale Schemas und Pfadkonfiguration |
| Robustheit | Validierung, Error Workflow, Idempotenz und Retry-Grenzen |
| Portabilität | Markdown, JSON, JSONL, Docker Volumes und exportierbare n8n-Workflows |
| Sicherheit | lokale Verarbeitung, Credential Store, Vault-Grenze, keine Secrets in Dateien |
| Datenqualität | Pflichtfelder, kontrollierte Kategorien, Hashes, Message IDs und Quellenbezug |
| Erweiterbarkeit | versionierte Datenverträge und lose gekoppelte Flow-Übergaben |
| Performance | serielle lokale KI-Aufrufe, Chunking, begrenzte Batches und inkrementelle Verarbeitung |
| Wiederherstellbarkeit | Backups, Status-History, atomare Schreiboperationen und Workflow-Exporte |

---

# 3. Architekturprinzipien und Entscheidungen

## 3.1 Obsidian ist System of Record für Wissen

Alle finalen oder reviewfähigen Wissensartefakte werden als Markdown im Vault gespeichert.

Nicht als führender Wissensspeicher verwendet werden:

- n8n Execution Data,
- Ollama-Kontext,
- Gmail,
- eine spätere Vektordatenbank.

Diese Systeme sind Verarbeitungs-, Transport- oder Suchkomponenten. Der Vault bleibt die fachliche Wahrheit.

## 3.2 n8n ist Orchestrator, nicht Wissensspeicher

n8n koordiniert:

- Trigger,
- Validierung,
- Dateizugriff,
- KI-Aufrufe,
- Routing,
- Statusübergänge,
- Protokollierung,
- Fehlerbehandlung.

n8n hält keinen dauerhaft führenden Fachzustand, der nicht aus Vault und Logs wiederhergestellt werden kann.

## 3.3 Ollama ist austauschbarer KI-Dienst

Ollama übernimmt semantische Aufgaben:

- Extraktion,
- Klassifikation,
- Synthese,
- Änderungserkennung,
- Konzeptvorschläge.

Deterministische Aufgaben verbleiben in n8n-Code oder Standard-Nodes:

- Pfadberechnung,
- Datumsformatprüfung,
- Hashing,
- Dublettenprüfung,
- Kategorie-Routing,
- Zielpfadvalidierung,
- YAML- und JSON-Schema-Prüfung,
- Dateikonflikte,
- Logging.

## 3.4 KI erzeugt Daten, nicht Infrastrukturpfade

Ollama darf keine freien Zielpfade bestimmen. Zielpfade werden aus:

- Kategorien,
- Ticker,
- zentraler Konfiguration,
- `concept-links.json`,
- vorhandenen Dateilisten

deterministisch erzeugt.

## 3.5 Append-only für Original- und Updatedaten

Historische Analystenupdates und Originalquellen werden grundsätzlich nur hinzugefügt. Fachliche Inhalte werden nicht rückwirkend durch Automatisierung überschrieben.

Ausnahmen sind kontrollierte technische Metadaten:

- Vorgänger,
- Nachfolger,
- Historienliste,
- Linkabschnitte,
- Verarbeitungsstatus.

## 3.6 Abgeleitete Statusdateien sind versionierbar

Aktuelle technische und fundamentale Statusdateien werden aktualisiert. Vor jeder Ersetzung wird die bestehende Version nach `_History` geschrieben.

## 3.7 Dateien werden atomar geschrieben

Produktive Dateien werden nicht direkt schrittweise überschrieben.

Zielverfahren:

```text
Inhalt vollständig erzeugen
→ temporäre Datei schreiben
→ Datei erneut lesen und prüfen
→ bestehenden Stand sichern
→ temporäre Datei auf finalen Namen verschieben
```

## 3.8 Sub-Workflows statt monolithischer Flows

Gemeinsame technische Funktionen werden als intern aufrufbare Sub-Workflows umgesetzt:

- YAML Parsing und Validierung,
- sichere Dateischreiboperation,
- JSONL Logging,
- Concept-Link-Auflösung,
- Ollama-Aufruf mit JSON-Validierung,
- Fehlernormalisierung.

---

# 4. Systemkontext

## 4.1 Laufzeitumgebung

```text
Windows 10/11
├── Obsidian Desktop
├── Ollama Windows Service
├── Claude Desktop + Obsidian MCP
└── Docker Desktop / WSL2
    └── n8n Container
```

## 4.2 Hardware

```text
CPU: AMD Ryzen 7 3700X, 8 Kerne / 16 Threads
RAM: 16 GB
GPU: NVIDIA GeForce GTX 1050 Ti, 4 GB VRAM
```

## 4.3 Technische Konsequenzen

- n8n und Ollama werden parallel lokal betrieben.
- KI-Verarbeitung erfolgt vorerst seriell.
- große Bücher werden in Chunks verarbeitet.
- kleine quantisierte Modelle werden bevorzugt.
- hohe Parallelität wird vermieden.
- OCR und Vision werden als separate, ressourcenintensive Pipelines geplant.

---

# 5. Komponentenübersicht

| Komponente | Verantwortung | Persistenz |
|---|---|---|
| Obsidian | Darstellung, manuelle Prüfung, Navigation und Wissensarbeit | Markdown im Vault |
| Vault-Dateisystem | führender fachlicher Speicher | NTFS |
| n8n | Workflow-Orchestrierung | internes n8n Volume |
| Gmail | Eingang dynamischer Analystenquellen | extern, nicht führend |
| Ollama | lokale LLM-Inferenz | lokale Modelle |
| Claude Desktop | Dialog- und Analyseschicht über MCP | keine führende Persistenz |
| Obsidian MCP Connector | lokaler Zugriff auf Vault-Inhalte | Plugin-Konfiguration |
| concept-links.json | kontrolliertes Linkregister | Vault/System/Automation |
| JSONL-Logs | technische Verarbeitungshistorie | Vault/System/Automation |
| Qdrant, später | semantischer Retrieval-Index | Docker Volume |
| Backup-Speicher | Wiederherstellung | ZIP/Kopie/externes Medium |

---

# 6. Physische Zielarchitektur

## 6.1 Container- und Host-Sicht

```text
Windows Host
│
├── Obsidian Vault
│   C:\Users\Kuba\Desktop\Obsidian_Desktop\Jakob_Obsidian_Finanzen
│
├── Ollama
│   http://localhost:11434
│
└── Docker Desktop
    └── n8n Container
        ├── Port 5678 → http://localhost:5678
        ├── n8n_data → /home/node/.n8n
        └── Vault Bind Mount → /vault
```

## 6.2 Verbindliche Pfade

Host:

```text
C:\Users\Kuba\Desktop\Obsidian_Desktop\Jakob_Obsidian_Finanzen\Finanzen\Trading
```

Container:

```text
/vault/Finanzen/Trading
```

Alle Workflowpfade werden aus einer zentralen Basis abgeleitet:

```json
{
  "trading_root": "/vault/Finanzen/Trading",
  "inbox_reviewed": "/vault/Finanzen/Trading/Inbox/Reviewed",
  "inbox_terminated": "/vault/Finanzen/Trading/Inbox/Terminated",
  "analyst_root": "/vault/Finanzen/Trading/Research/Analysten/TheLongInvestor",
  "automation_root": "/vault/Finanzen/Trading/System/Automation"
}
```

Diese Konfiguration soll nicht mehrfach als freie Zeichenkette in vielen Nodes gepflegt werden.

---

# 7. Logische Schichten

| Schicht | Verantwortung |
|---|---|
| Trigger | Gmail, Schedule, Manual, Dateieingang |
| Ingestion | Nachrichten- und Dateiinhalte vollständig laden |
| Normalization | HTML, Encoding, Datums- und Tickerformat normalisieren |
| Validation | Schema, Pflichtfelder, Quelle, Kategorie, Status und IDs prüfen |
| AI Processing | semantische Extraktion, Klassifikation und Synthese |
| Routing | Zielkategorie, Tickerstruktur und Flow-Übergabe bestimmen |
| Persistence | sichere Markdown-, JSON- und Log-Schreiboperationen |
| Linking | Concept Registry und Obsidian-Pfade auflösen |
| State Derivation | aktuellen technischen oder fundamentalen Status bilden |
| Review | manuelle Freigabe in Obsidian |
| Retrieval, später | Chunking, Embeddings, Qdrant und Abfrage |
| Operations | Logging, Error Workflow, Backup, Health Checks |

---

# 8. Dateisystem- und Ablagearchitektur

## 8.1 Zielstruktur

```text
/vault/Finanzen/Trading/
├── Books/
├── Inbox/
│   ├── Analyst New/
│   ├── New/
│   ├── Reviewed/
│   │   └── _Errors/
│   └── Terminated/
│       └── Analysten/YYYY/MM/
├── Journal/
├── Notes/
│   └── 25 Hauptthemenordner
├── PDFs/
├── Research/
│   ├── Analysten/
│   │   └── TheLongInvestor/
│   │       ├── Technisch/<TICKER>/Updates|Status/_History
│   │       ├── Fundamental/<TICKER>/Updates|Status/_History
│   │       └── Sonstige/
│   ├── Quellen/
│   └── Taxonomie/
├── Strategies/
├── System/
│   ├── Automation/
│   │   ├── config.json
│   │   ├── concept-links.json
│   │   ├── schemas/
│   │   ├── logs/
│   │   └── workflow-exports/
│   └── Vault-Struktur.md
└── Templates/
```

## 8.2 Dateinamensschema

### Analystenupdate

```text
YYYY-MM-DD - <TICKER> - Analysten-Update.md
```

### Fundamentales Update

```text
YYYY-MM-DD - <TICKER> - Fundamental-Update.md
```

### Technischer Status

```text
<TICKER> - Aktueller Stand.md
```

### Fundamentaler Status

```text
<TICKER> - Aktueller fundamentaler Stand.md
```

### Konfliktauflösung

```text
YYYY-MM-DD - <TICKER> - Analysten-Update - <short_message_id>.md
```

## 8.3 Windows-inkompatible Zeichen

Aus berechneten Dateinamen werden entfernt oder ersetzt:

```text
< > : " / \ | ? *
```

## 8.4 Encoding

Alle Textdateien werden als UTF-8 ohne verlustbehaftete Umwandlung geschrieben.

---

# 9. Technische Datenverträge

## 9.1 Grundsatz

Flow-Übergaben erfolgen nicht als unstrukturierter Markdown-Text, sondern als versionierte JSON-Objekte. Markdown wird erst an der Persistenzgrenze erzeugt.

Jeder Vertrag enthält:

```json
{
  "schema_version": "1.0",
  "correlation_id": "uuid",
  "created_at": "ISO-8601",
  "payload": {}
}
```

## 9.2 Correlation ID

Die Correlation ID verbindet:

- Gmail-Eingang,
- Ollama-Aufruf,
- Review-Datei,
- finalen Ablagepfad,
- Statuslauf,
- technische Logs.

Für Gmail kann sie deterministisch aus der Message ID abgeleitet oder als UUID erzeugt und mit der Message ID gespeichert werden.

---

# 10. Datenvertrag Flow 1 → Review-Datei

## 10.1 YAML-Mindeststruktur

```yaml
---
schema_version: "1.0"
typ: analysten-update
status: review
quelle: Patreon
analyst: The Long Investor
hauptkategorie: Technisch
veröffentlicht: 2026-09-03
datum_status: bestätigt
instrument: NVIDIA
ticker: NVDA
isin:
analyseart:
  - technisch
zeithorizont: kurzfristig bis mehrwöchig
quell_url:
gmail_message_id: "..."
correlation_id: "..."
inhalt_vollständig: true
importiert_am: 2026-09-03T22:00:00+02:00
vorgänger:
nachfolger:
erkannte_konzepte:
  - begriff: Unterstützung
    gefundene_bezeichnung: Supportzone
    sicherheit: hoch
---
```

## 10.2 Pflichtfelder

- `schema_version`
- `typ`
- `status`
- `quelle`
- `analyst`
- `hauptkategorie`
- `veröffentlicht` oder dokumentierter Unsicherheitsstatus
- `gmail_message_id`
- `correlation_id`
- nicht leerer Originalinhalt

Zusätzlich bei technisch und fundamental:

- `instrument`
- `ticker`

## 10.3 Zulässige Kategorien

```text
Technisch
Fundamental
Sonstige
```

---

# 11. Datenvertrag Flow 2 → Flow 3

```json
{
  "schema_version": "1.0",
  "correlation_id": "uuid",
  "analyst": "TheLongInvestor",
  "category": "Technisch",
  "ticker": "NVDA",
  "instrument": "NVIDIA",
  "published_date": "2026-09-03",
  "gmail_message_id": "...",
  "new_update_path": "/vault/Finanzen/Trading/Research/Analysten/TheLongInvestor/Technisch/NVDA/Updates/2026-09-03 - NVDA - Analysten-Update.md",
  "updates_directory": "/vault/Finanzen/Trading/Research/Analysten/TheLongInvestor/Technisch/NVDA/Updates",
  "status_directory": "/vault/Finanzen/Trading/Research/Analysten/TheLongInvestor/Technisch/NVDA/Status",
  "status_file": "/vault/Finanzen/Trading/Research/Analysten/TheLongInvestor/Technisch/NVDA/Status/NVDA - Aktueller Stand.md",
  "concept_links": [
    {
      "concept": "Elliott-Wellen",
      "label": "Elliott-Wellen",
      "target": "Trading/Notes/10 - Elliott-Wellen/10 - Elliott-Wellen.md"
    }
  ]
}
```

Flow 3 validiert den Vertrag erneut und vertraut nicht blind auf den Aufrufer.

---

# 12. KI-Ausgabevertrag

## 12.1 Flow-1-Extraktion

Ollama erzeugt ausschließlich JSON gemäß Schema.

```json
{
  "published_date": "2026-09-03",
  "date_status": "confirmed",
  "instrument": "NVIDIA",
  "ticker": "NVDA",
  "isin": "",
  "main_category": "Technisch",
  "analysis_types": ["technisch"],
  "time_horizon": "kurzfristig bis mehrwöchig",
  "source_url": "",
  "content_complete": true,
  "summary": "",
  "market_state": "",
  "primary_scenario": "",
  "alternative_scenario": "",
  "supports": [],
  "resistances": [],
  "observation_zones": [],
  "invalidations": [],
  "targets": [],
  "elliott_wave": "",
  "fundamental_statements": "",
  "reevaluation_conditions": [],
  "uncertainties_and_risks": [],
  "source_facts": [],
  "missing_information": [],
  "recognized_concepts": []
}
```

## 12.2 Regeln

- kein Markdown im JSON-Feld, sofern nicht ausdrücklich erlaubt
- keine Kommentare außerhalb des JSON
- leere Angaben als leere Zeichenkette oder leeres Array
- keine erfundenen Werte
- Geldbeträge mit Währung erhalten
- fachliche Aussagen als Analysteneinschätzung formulieren

## 12.3 JSON-Validierung

Validierungsstufen:

1. JSON parsebar
2. erwarteter Root-Typ `object`
3. Pflichtfelder vorhanden
4. Datentypen korrekt
5. Kategorien aus Allowlist
6. Ticker normalisierbar
7. Arrays enthalten nur zulässige Objekte oder Strings
8. keine unbekannten kritischen Felder
9. Originalinhalt ausreichend, sofern `content_complete=true`

---

# 13. Flow 1: Technische Umsetzung

## 13.1 Trigger

Node:

```text
Gmail Trigger
```

Filter:

- definiertes Eingangslabel
- ungelesene Nachrichten
- keine Spam- oder Trash-Nachrichten
- begrenzte Batchgröße

## 13.2 Nachricht vollständig laden

Node:

```text
Gmail → Message → Get
```

Die Triggerausgabe wird nicht als vollständiger Body vorausgesetzt.

## 13.3 HTML-Extraktion

Priorität:

1. Inhalt des HTML-Elements beziehungsweise Bereichs `post-content`
2. vollständiger Plain-Text-Body
3. bereinigter HTML-Body

Entfernt werden:

- Trackingparameter,
- unsichtbare Pixel,
- Navigationslinks,
- Footer,
- Abmeldetexte,
- allgemeine Patreon-Marketingblöcke.

Der Originalbeitrag wird fachlich nicht umformuliert.

## 13.4 Quellenvalidierung

Prüfungen:

- Message ID vorhanden
- Body nicht leer
- zulässige Patreon-Quelle
- Analystenidentität plausibel
- Inhalt oberhalb einer definierten Mindestlänge

## 13.5 Gmail-Dublette

Primärschlüssel:

```text
gmail_message_id
```

Prüfquellen:

- Importlog
- bestehende Review- und Update-Dateien

## 13.6 Ollama-Aufruf

Verbindung bei n8n in Docker:

```text
http://host.docker.internal:11434
```

Konfiguration wird zentral dokumentiert:

- Modellname
- Temperatur
- Kontextlänge
- Timeout
- maximale Wiederholungen
- erwartetes JSON-Schema

Empfehlung:

- Temperatur niedrig
- eine E-Mail pro KI-Aufruf
- keine parallelen Modellaufrufe in Version 1
- Timeout mit kontrolliertem Fehlerpfad

## 13.7 Ergebnisnormalisierung

Sicher normalisierbar:

- Kategorie-Großschreibung
- Ticker ohne führendes `$`
- leere Arrays
- einfache Datumsformate
- String zu Ein-Element-Array bei erlaubten Feldern

Nicht automatisch zu erraten:

- fehlender Ticker
- fehlende Kursmarke
- unbekanntes Datum
- nicht vorhandener ISIN-Wert

## 13.8 Markdown-Rendering

Markdown wird deterministisch durch einen Code-Node aus validiertem JSON erzeugt.

Der Code-Node:

- escaped YAML-Werte,
- stellt Arrays korrekt dar,
- erzeugt nur relevante Abschnitte,
- hält Originalinhalt als separaten Abschnitt,
- schreibt UTF-8,
- generiert einen Windows-kompatiblen Dateinamen.

## 13.9 Schreiben

Ziel:

```text
/vault/Finanzen/Trading/Inbox/Reviewed
```

Vorher:

- Dateiname prüfen
- Zielpfad gegen Trading-Root validieren
- Existenz prüfen
- keine Überschreibung

## 13.10 Gmail-Abschluss

Nur nach erfolgreichem Schreiben und Loggen:

- Processed-Label hinzufügen
- Eingangslabel entfernen
- optional als gelesen markieren

Bei Fehler:

- Error-Label setzen
- Eingangslabel zunächst erhalten
- nicht als erfolgreich protokollieren

---

# 14. Flow 2: Technische Umsetzung

## 14.1 Triggerstrategie

Pilot:

```text
Manual Trigger
```

Produktiv:

```text
Schedule Trigger
```

Der Schedule Trigger ist für einen täglich gestarteten Rechner robuster als ein dauerhaft beobachtender File Trigger.

## 14.2 Eingang lesen

Selector:

```text
/vault/Finanzen/Trading/Inbox/Reviewed/*.md
```

Verarbeitung in begrenzten Batches, initial seriell.

## 14.3 YAML Parsing

Ein zentraler Parser trennt:

- Frontmatter,
- Body,
- Dateiname,
- Pfad.

Für produktive Umsetzung wird eine robuste YAML-Bibliothek oder eine geprüfte Parser-Implementierung benötigt. Ein einfacher Regex darf nur die Trennung des Blocks übernehmen, nicht die vollständige YAML-Semantik.

## 14.4 Freigabeprüfung

Produktiv werden nur Dateien verarbeitet mit:

```yaml
status: geprüft
```

Flow 2 ignoriert `review`, `entwurf` und `archiviert`.

## 14.5 Routing

Switch nach `hauptkategorie`:

```text
Technisch
Fundamental
Sonstige
```

Flow 2 führt keine freie Neuklassifikation durch.

## 14.6 Pfadberechnung

Technisch:

```text
<analyst_root>/Technisch/<TICKER>/Updates
<analyst_root>/Technisch/<TICKER>/Status
```

Fundamental:

```text
<analyst_root>/Fundamental/<TICKER>/Updates
<analyst_root>/Fundamental/<TICKER>/Status
```

Sonstige:

```text
<analyst_root>/Sonstige
```

## 14.7 Verzeichnisse anlegen

Unterordner werden idempotent erzeugt. Erneutes Anlegen eines vorhandenen Ordners ist kein Fehler.

## 14.8 Concept Registry

Flow 2 lädt:

```text
/vault/Finanzen/Trading/System/Automation/concept-links.json
```

Ablauf:

1. `erkannte_konzepte` aus Flow-1-Datei lesen.
2. Begriffe normalisieren.
3. exakten Begriff und Aliasse in Registry suchen.
4. Zielpfad gegen Trading-Root prüfen.
5. Existenz des Ziels prüfen.
6. Links deduplizieren.
7. separaten Abschnitt erzeugen.

Die Registry ist Runtime-Abhängigkeit. Ist sie beschädigt, wird die fachliche Ablage nicht zwingend blockiert; der Linkteil erhält einen kontrollierten Fehlerstatus und wird im Log vermerkt.

## 14.9 Update schreiben

Das geprüfte Update wird in den Zielordner geschrieben. Vor produktiver Ablage wird eine temporäre Datei erzeugt und validiert.

## 14.10 Chronologie neu berechnen

Alle Updates des Tickers und der Kategorie werden geladen.

Sortierschlüssel:

```text
published_date ASC
ausweichend imported_at ASC
ausweichend gmail_message_id ASC
```

Anschließend werden für jede Datei berechnet:

- Vorgänger,
- Nachfolger,
- vollständige Historienliste.

Fachliche Abschnitte bleiben unverändert.

## 14.11 Flow-3-Aufruf

Nur `Technisch` und `Fundamental` lösen Flow 3 aus.

Technisch wird der Execute-Workflow-Node so konfiguriert, dass Fehler aus Flow 3 nicht still als Gesamterfolg behandelt werden.

Die Eingangsdatei wird erst dann nach `Terminated` verschoben, wenn die definierte Transaktionsgrenze erreicht ist.

## 14.12 Transaktionsgrenze

Empfohlene Regel:

- Updateablage und Chronologie gehören zu Flow 2.
- Statusfortschreibung gehört zu Flow 3.
- Flow 2 protokolliert `update_committed`.
- Erst bei erfolgreichem Flow 3 wird `status_committed` protokolliert.
- Scheitert Flow 3, bleibt das historische Update gültig; die Review-Datei wird nicht erneut als neues Update verarbeitet.
- Stattdessen wird ein gezielter `status_pending`-Fehlerdatensatz erzeugt.

Dadurch wird verhindert, dass ein gültiges Update wegen eines Statusfehlers dupliziert wird.

---

# 15. Flow 3: Technische Umsetzung

## 15.1 Eingang

Flow 3 beginnt mit:

```text
Execute Sub-workflow Trigger
```

Der Input entspricht dem versionierten Vertrag aus Kapitel 11.

## 15.2 Updates laden

Alle Markdown-Dateien aus `updates_directory` werden geladen und geordnet.

Für Modellinput werden extrahiert:

- Datum,
- Zusammenfassung,
- Primärszenario,
- Alternativszenario,
- Trigger,
- Unterstützungen,
- Widerstände,
- Ziele,
- Invalidierungen,
- Risiken,
- Originalquellenpfad.

Der vollständige E-Mail-Originaltext wird nur dann in den Modellinput aufgenommen, wenn die strukturierten Abschnitte nicht ausreichen.

## 15.3 Kontextbegrenzung

Bei wenigen kurzen Updates werden alle Updates verwendet.

Bei später wachsender Historie:

- bestehenden Status verwenden,
- neuestes Update vollständig verwenden,
- relevante ältere Updates selektiv verwenden,
- nie ohne Quellenliste synthetisieren.

## 15.4 Synthesevertrag

Die KI gibt strukturiertes JSON aus, nicht direkt finales Markdown.

```json
{
  "status_date": "2026-09-03",
  "latest_update": "...",
  "summary": "",
  "primary_scenario": "",
  "alternative_scenario": "",
  "triggers": [],
  "supports": [],
  "resistances": [],
  "observation_zones": [],
  "targets": [],
  "invalidations": [],
  "elliott_wave": "",
  "trend_structure": "",
  "moving_averages": [],
  "fibonacci_levels": [],
  "new_statements": [],
  "still_valid": [],
  "changed": [],
  "invalidated": [],
  "unclear_or_conflicting": [],
  "risks": [],
  "used_updates": []
}
```

Für Fundamental wird ein eigenes Schema verwendet.

## 15.5 Validierung

- `latest_update` existiert in Update-Liste
- `status_date` entspricht dem neuesten Veröffentlichungsdatum
- `used_updates` sind vorhandene Dateien
- keine unbekannten Kursmarken ohne Quellenbezug
- keine leeren Pflichtfelder bei vorhandenem Quellmaterial
- Kategorie des Status entspricht Kategorie des Inputs

## 15.6 Status rendern

Deterministischer Markdown-Renderer erzeugt:

- YAML,
- Statusabschnitte,
- Änderungsabschnitte,
- verwendete Updates als Obsidian-Links,
- Concept Links.

## 15.7 Sichere Ersetzung

```text
bestehenden Status lesen
→ Hash berechnen
→ nach _History kopieren
→ neuen Status als .tmp schreiben
→ neue Datei validieren
→ .tmp auf finalen Namen verschieben
→ Erfolg loggen
```

Bei Fehler bleibt die bestehende Statusdatei unverändert.

---

# 16. Shared Sub-Workflows

## 16.1 SWF_Parse_Validate_Markdown

Input:

```json
{
  "file_path": "..."
}
```

Output:

```json
{
  "metadata": {},
  "body": "",
  "file_name": "",
  "file_path": "",
  "valid": true,
  "errors": []
}
```

## 16.2 SWF_Ollama_JSON

Verantwortung:

- Prompt zusammensetzen
- Ollama aufrufen
- Antwort bereinigen
- JSON validieren
- begrenzten Reparaturversuch durchführen
- Token- beziehungsweise Laufzeitmetadaten liefern

## 16.3 SWF_Safe_Write

Input:

- Zielpfad
- Inhalt
- Überschreibmodus
- Backupregel
- Correlation ID

Output:

- finaler Pfad
- Hash
- Byteanzahl
- Status

## 16.4 SWF_JSONL_Log

Schreibt genau eine JSON-Zeile pro Ereignis. Logrotation erfolgt später nach Monat oder Dateigröße.

## 16.5 SWF_Resolve_Concept_Links

- Registry laden
- Begriff/Alias matchen
- Pfad prüfen
- existierende Ziele bestätigen
- deduplizierte Linkliste zurückgeben

## 16.6 SWF_Error_Normalize

Erzeugt standardisiertes Fehlerobjekt:

```json
{
  "correlation_id": "...",
  "workflow": "...",
  "stage": "...",
  "error_code": "...",
  "error_message": "...",
  "retryable": false,
  "source_id": "...",
  "timestamp": "..."
}
```

---

# 17. Fehlerarchitektur

## 17.1 Zentraler Error Workflow

Ein eigener n8n-Workflow startet mit dem `Error Trigger` und wird in allen Hauptflows als Error Workflow konfiguriert.

## 17.2 Fehlerklassen

### Retryable

- Gmail temporär nicht erreichbar
- Ollama Timeout
- Docker-Dateisystem kurzzeitig nicht verfügbar
- vorübergehender Lock

### Nicht retryable

- ungültiges YAML
- fehlender Ticker bei technisch/fundamental
- unbekannte Kategorie
- beschädigte Registry
- unzulässiger Zielpfad
- fachlich unzureichender Inhalt

## 17.3 Retry-Policy

```text
Versuch 1: unmittelbar oder im nächsten Lauf
Versuch 2: nach definierter Wartezeit
Versuch 3: finaler technischer Retry
Danach: manueller Fehlerstatus
```

Keine Endlosschleifen.

## 17.4 Fehlerpersistenz

- technisches JSONL-Log
- optional Fehler-Markdown unter `_Errors`
- Gmail Error-Label für Flow 1
- Eingangsdatei bleibt erhalten

## 17.5 Kompensationslogik

Da das Dateisystem keine Datenbanktransaktion über mehrere Dateien bietet, werden Operationen als Saga-artige Schritte behandelt:

1. Schritt beginnt und wird geloggt.
2. Ergebnis wird geschrieben.
3. Ergebnis wird verifiziert.
4. Schritt wird committed.
5. Folgeschritt startet.

Bei Fehler wird nur der noch nicht committete Schritt wiederholt.

---

# 18. Idempotenz und Dublettenschutz

## 18.1 Gmail

Schlüssel:

```text
gmail_message_id
```

## 18.2 Dateien

Schlüssel:

```text
SHA-256 des Originalinhalts
```

## 18.3 Statusläufe

Schlüssel:

```text
category + ticker + latest_update_message_id + flow_version
```

## 18.4 Logs

Jedes Event enthält:

- Correlation ID
- Source ID
- Workflowversion
- Operation
- Ergebnis
- Zielpfad

## 18.5 Wiederanlauf

Ein Workflow prüft vor jeder Seiteneffekt-Operation, ob derselbe Commit bereits existiert.

---

# 19. Konfigurationsarchitektur

## 19.1 Zentrale config.json

```json
{
  "schema_version": "1.0",
  "paths": {
    "trading_root": "/vault/Finanzen/Trading",
    "reviewed": "/vault/Finanzen/Trading/Inbox/Reviewed",
    "terminated": "/vault/Finanzen/Trading/Inbox/Terminated",
    "analyst_root": "/vault/Finanzen/Trading/Research/Analysten/TheLongInvestor",
    "automation": "/vault/Finanzen/Trading/System/Automation"
  },
  "analyst": {
    "display_name": "The Long Investor",
    "folder_name": "TheLongInvestor"
  },
  "categories": ["Technisch", "Fundamental", "Sonstige"],
  "models": {
    "analyst_extraction": "<MODEL_NAME>",
    "status_synthesis": "<MODEL_NAME>",
    "embedding": "nomic-embed-text"
  },
  "workflow": {
    "batch_size": 1,
    "max_retries": 3,
    "timezone": "Europe/Berlin"
  }
}
```

## 19.2 Secrets

Nicht in config.json:

- Gmail Client Secret
- OAuth Tokens
- künftige API Keys
- Credential IDs, sofern exportierte Flows portabel bleiben sollen

Diese Werte bleiben in n8n Credentials oder Umgebungsvariablen.

## 19.3 Schema-Dateien

Empfohlene Ablage:

```text
System/Automation/schemas/
├── analyst-update.schema.json
├── flow2-handoff.schema.json
├── technical-status.schema.json
├── fundamental-status.schema.json
└── error.schema.json
```

---

# 20. Modell- und Promptarchitektur

## 20.1 Promptversionierung

Prompts werden nicht ausschließlich in Nodes verborgen, sondern versioniert abgelegt:

```text
System/Automation/prompts/
├── analyst-extraction-v1.md
├── status-technical-v1.md
├── status-fundamental-v1.md
└── source-analysis-v1.md
```

## 20.2 Prompt-Metadaten

Jede erzeugte Datei speichert optional:

```yaml
processing:
  workflow: Flow1
  workflow_version: "1.0"
  prompt_version: "analyst-extraction-v1"
  model: "..."
```

## 20.3 Modellparameter

Je Use Case getrennt definieren:

- Modell
- Temperatur
- Kontextfenster
- maximale Ausgabe
- Timeout
- JSON-Modus

## 20.4 Reproduzierbarkeit

Lokale LLM-Ausgaben sind nicht vollständig deterministisch. Reproduzierbarkeit wird verbessert durch:

- niedrige Temperatur,
- feste Prompts,
- feste Schemata,
- Modell- und Promptversion,
- gespeicherten Originalinhalt,
- validierte Renderer.

---

# 21. Statische Dokumentenpipeline

## 21.1 Zielarchitektur

```text
Inbox/New
→ File Discovery
→ Hash
→ Format Detection
→ Text Extraction
→ OCR Decision
→ Structure Detection
→ Chunking
→ Chunk Analysis
→ Document Synthesis
→ Taxonomy Mapping
→ Markdown Render
→ Inbox/Reviewed
```

## 21.2 Dateitypen

Version 1:

- PDF
- TXT
- Markdown

Später:

- DOCX
- HTML
- EPUB, sofern rechtlich und technisch zulässig

## 21.3 Hashing

Vor Textverarbeitung wird SHA-256 über die Originaldatei gebildet.

Speicherung:

```yaml
source_hash: "sha256:..."
```

## 21.4 PDF-Extraktion

Textbasierte PDFs:

- `Read/Write Files from Disk`
- `Extract From File`

Bildbasierte PDFs:

- Extraktion liefert zu wenig Text
- Status `ocr_erforderlich`
- Weiterleitung an OCR-Pipeline

## 21.5 OCR-Pipeline

Technische Optionen:

- Tesseract lokal
- OCRmyPDF lokal
- lokales Vision-Modell nur als zweite Option

OCR-Ausgabe wird als abgeleitete Datei gespeichert; Original-PDF bleibt unverändert.

## 21.6 Strukturdetektion

Erkennen von:

- Inhaltsverzeichnis
- Kapitelüberschriften
- Seitenzahlen
- Abschnitten
- Tabellenhinweisen
- Literaturverzeichnis

## 21.7 Chunking

Primär nach Dokumentstruktur, nicht nur nach fixer Zeichenzahl.

Fallback:

- definierte Token- beziehungsweise Zeichengröße
- Überlappung
- Seiten- und Abschnittsmetadata an jedem Chunk

## 21.8 Map-Reduce-Synthese

```text
Map:
Jeder Chunk → strukturierte Teilanalyse

Reduce 1:
Kapitel-Chunks → Kapitelanalyse

Reduce 2:
Kapitelanalysen → Gesamtquellenanalyse
```

## 21.9 Zwischenpersistenz

Teilanalysen werden zwischengespeichert, damit ein Abbruch nicht das gesamte Buch neu starten muss.

```text
System/Automation/work/<source_hash>/
├── manifest.json
├── chunks/
├── analyses/
└── synthesis/
```

## 21.10 Quellenanalyse-Output

Ziel:

```text
Inbox/Reviewed/<Autor> - <Titel> - Quellenanalyse.md
```

Originaldatei bleibt bis zur Freigabe im Eingang.

---

# 22. Wissensnotiz-Architektur

## 22.1 Eingang

Nur geprüfte Quellenanalysen:

```yaml
typ: quelle
status: geprüft
```

## 22.2 Kandidatenerkennung

Für jedes Konzept:

- Taxonomiematch
- vorhandene Notiz suchen
- Alias prüfen
- Quellenstärke bewerten
- Mindestsubstanz prüfen

## 22.3 Entscheidungsobjekt

```json
{
  "concept": "Unterstützung",
  "decision": "create|extend|reference_only|duplicate|insufficient",
  "target_path": "",
  "primary_topic": "03 - Unterstützungen & Widerstände",
  "evidence": [],
  "confidence": "high"
}
```

## 22.4 Neue Notiz

Neue Dateien werden zunächst nach `Inbox/Reviewed` geschrieben, nicht direkt nach `Notes`.

## 22.5 Bestehende Notiz ergänzen

Keine direkte automatische Änderung in Version 1. Stattdessen wird ein Merge-Vorschlag erzeugt:

```text
<Begriff> - Ergänzungsvorschlag - <source>.md
```

## 22.6 Finale Freigabe

Ein separater Flow verschiebt geprüfte Notizen in den Zielordner und aktualisiert den Index mit Backup.

---

# 23. RAG-Zielarchitektur

## 23.1 Komponenten

```text
Obsidian Vault
→ RAG Indexer Workflow
→ Markdown Parser
→ Chunker
→ Ollama Embeddings
→ Qdrant
→ Retrieval Workflow
→ Ollama oder Claude Antwortschicht
```

## 23.2 Collection Design

Empfohlene Trennung:

```text
trading_knowledge
trading_analyst_updates
trading_status
trading_journal
```

Alternativ eine Collection mit starkem Payload-Filtering. Die endgültige Entscheidung erfolgt anhand der erwarteten Retrieval-Queries.

## 23.3 Point ID

Deterministisch aus:

```text
file_path + file_hash + heading_path + chunk_index
```

## 23.4 Payload

```json
{
  "file_path": "...",
  "document_type": "wissen",
  "status": "geprüft",
  "main_topic": "...",
  "subtopic": "...",
  "ticker": "NVDA",
  "analyst": "TheLongInvestor",
  "published_date": "2026-09-03",
  "heading_path": ["Technisches Szenario", "Primärszenario"],
  "source_hash": "...",
  "chunk_index": 3
}
```

## 23.5 Inkrementelle Indexierung

Manifest speichert je Datei:

- Pfad
- Hash
- letzter Indexzeitpunkt
- Chunk IDs
- Embedding-Modellversion

Nur neue oder geänderte Dateien werden re-indexiert.

## 23.6 Löschung

Wird eine Datei gelöscht oder ersetzt, werden die zugeordneten Point IDs entfernt oder als inaktiv markiert.

## 23.7 Retrieval

- Query Embedding
- Payload-Filter
- Top K
- optional Keyword-/Hybrid-Retrieval
- Quellenabschnitte an LLM
- Antwort mit Dateipfaden

## 23.8 Datenschutz

Qdrant und Embeddings werden lokal betrieben. Die Vektordatenbank ist ein abgeleiteter Index und kann aus dem Vault neu aufgebaut werden.

---

# 24. Claude- und MCP-Integration

## 24.1 Rolle

Claude dient als flexible Abfrage-, Analyse- und Interaktionsschicht über dem Vault.

## 24.2 Zugriff

- bevorzugt lesend auf Trading
- Schreibrechte nur kontrolliert und gegebenenfalls auf Reviewbereiche
- keine unbeschränkten Löschrechte
- keine automatische Änderung anderer Vault-Bereiche

## 24.3 Tokensparende Nutzung

- kompakter Projektkontext
- gezielte semantische Suche
- nur relevante Dateien und Abschnitte laden
- voller Projektplan nur bei Bedarf
- RAG für große Dokumentbestände

## 24.4 Abgrenzung zu n8n

Claude ersetzt keine deterministischen n8n-Prozesse. n8n verarbeitet reproduzierbare Pipelines; Claude unterstützt flexible Fragen und punktuelle Analysen.

---

# 25. Deployment-Konzept

## 25.1 Aktueller Betrieb

n8n läuft als Docker-Container mit:

- persistentem n8n Volume,
- Port 5678,
- Vault Bind Mount,
- Zeitzone Europe/Berlin,
- Zugriff auf Ollama über `host.docker.internal`.

## 25.2 Empfohlener Zielbetrieb mit Docker Compose

```yaml
services:
  n8n:
    image: docker.n8n.io/n8nio/n8n:<PINNED_VERSION>
    container_name: n8n
    restart: unless-stopped
    ports:
      - "5678:5678"
    environment:
      - TZ=Europe/Berlin
      - GENERIC_TIMEZONE=Europe/Berlin
      - N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true
      - N8N_RESTRICT_FILE_ACCESS_TO=/vault/Finanzen/Trading
    volumes:
      - n8n_data:/home/node/.n8n
      - "C:/Users/Kuba/Desktop/Obsidian_Desktop/Jakob_Obsidian_Finanzen:/vault"

  qdrant:
    image: qdrant/qdrant:<PINNED_VERSION>
    container_name: qdrant
    restart: unless-stopped
    profiles: ["rag"]
    volumes:
      - qdrant_data:/qdrant/storage
    ports:
      - "6333:6333"

volumes:
  n8n_data:
  qdrant_data:
```

Hinweise:

- konkrete Versionen werden gepinnt, nicht dauerhaft `latest` verwendet
- Qdrant wird erst mit dem RAG-Profil aktiviert
- Secrets werden nicht in diese Datei geschrieben
- produktive Compose-Datei wird versioniert, sensible `.env` nicht

## 25.3 Ollama

Ollama läuft weiterhin nativ auf Windows. n8n greift zu über:

```text
http://host.docker.internal:11434
```

## 25.4 Start und Health Check

PowerShell-Zielskript:

```text
Docker prüfen
→ n8n Container starten
→ n8n Health prüfen
→ Ollama API prüfen
→ benötigte Modelle prüfen
→ optional Workflow-Lauf starten
```

---

# 26. Workflow-Versionierung und Deployment

## 26.1 Export

Jeder produktive Flow wird als JSON exportiert:

```text
System/Automation/workflow-exports/
├── Flow1_Gmail_Analystenbeitraege_Extrahieren.json
├── Flow2_Analystenbeitraege_Einsortieren_und_Verlinken.json
├── Flow3_Aktuellen_Analystenstand_Konsolidieren.json
└── ErrorHandler_Zentral.json
```

## 26.2 Version

Workflowname oder Beschreibung enthält semantische Version:

```text
Flow1_Gmail_Analystenbeitraege_Extrahieren v1.1.0
```

## 26.3 Credential-Portabilität

Exportierte JSON-Dateien enthalten keine Secrets. Credential-Zuordnungen werden nach Import lokal gesetzt.

## 26.4 Git

Empfohlenes späteres Repository:

- Workflow-JSON
- konfigurationsfreie Systemdokumentation
- JSON-Schemas
- Prompts
- Test-Fixtures ohne geschützte Inhalte
- keine Patreon-Volltexte
- keine Credentials

---

# 27. Monitoring und Logging

## 27.1 Ebenen

### n8n Execution Log

Für technische Node- und Laufzeitfehler.

### Fachliches JSONL-Log

Für fachliche Operationen wie Import, Routing, Statusupdate und Indexierung.

### Health Check

Für Erreichbarkeit von:

- n8n,
- Ollama,
- Vault Mount,
- Gmail Credential,
- später Qdrant.

## 27.2 Standard-Logevent

```json
{
  "timestamp": "2026-10-26T22:00:00+01:00",
  "correlation_id": "...",
  "workflow": "Flow2",
  "workflow_version": "1.0.0",
  "event": "update_committed",
  "source_id": "gmail-message-id",
  "ticker": "NVDA",
  "category": "Technisch",
  "target_path": "...",
  "result": "success"
}
```

## 27.3 Logrotation

JSONL-Logs werden monatlich getrennt oder ab definierter Dateigröße rotiert.

## 27.4 Alarmierung

Version 1:

- Error-Label in Gmail
- Fehlerdatei unter `_Errors`
- n8n Execution Ansicht

Später optional:

- lokale Benachrichtigung
- E-Mail an eigenes Konto

---

# 28. Sicherheitskonzept

## 28.1 Prinzip der geringsten Berechtigung

- Gmail nur mit benötigten Scopes
- keine Delete-Operationen
- Vault-Schreibzugriff auf Trading begrenzen
- Claude zunächst read-only oder Review-only

## 28.2 Pfadschutz

Jeder berechnete Zielpfad wird normalisiert. Danach wird geprüft:

```text
normalized_path startsWith /vault/Finanzen/Trading
```

Pfadtraversal mit `..` wird abgewiesen.

## 28.3 Dateitypschutz

Workflow schreibt nur explizit erlaubte Dateitypen:

```text
.md
.json
.jsonl
.tmp
```

## 28.4 HTML-Sicherheit

E-Mail-HTML wird nicht als ausführbarer Inhalt gespeichert. Scripts, Styles und Tracking werden entfernt.

## 28.5 Secret Management

- n8n Credentials
- `.env` für Containerkonfiguration, falls erforderlich
- keine Secrets im Vault
- keine Secrets in Logs
- keine Secrets in Workflow-Exports

## 28.6 Geschützte Inhalte

Test-Fixtures für Git oder externe KI werden anonymisiert und enthalten keine vollständigen Patreon-Inhalte.

---

# 29. Backup- und Recovery-Architektur

## 29.1 Backupobjekte

- Obsidian-Vault
- n8n_data Volume
- Workflow-Exporte
- Compose-Datei
- Prompts
- Schemas
- Concept Registry
- Logs
- später Qdrant Volume, optional neu aufbaubar

## 29.2 Priorität

1. Vault
2. Workflow-JSON und Konfiguration
3. n8n Credential-Datenbank beziehungsweise n8n_data
4. Logs
5. Qdrant Index

## 29.3 Wiederherstellung

Recovery-Test umfasst:

- einzelne Markdown-Datei
- kompletten Tickerordner
- Workflow-Import
- n8n Container mit vorhandenem Volume
- Status aus historischen Updates neu erzeugen
- RAG-Index neu aufbauen

## 29.4 3-2-1

- aktive Vault-Kopie
- lokale zweite Kopie
- getrennte externe oder verschlüsselte Kopie

---

# 30. Testarchitektur

## 30.1 Testebenen

### Unit-artige Code-Node-Tests

- Ticker-Normalisierung
- Dateinamensanierung
- Datumsvalidierung
- YAML Rendering
- Pfadvalidierung
- Sortierung
- Linkdeduplizierung

### Contract Tests

- Flow-1-JSON gegen Schema
- YAML gegen Pflichtfelder
- Flow-2-Handoff gegen Schema
- Flow-3-Statusoutput gegen Schema

### Integration Tests

- Gmail Fixture → Review Markdown
- Review Markdown → Updates
- Updates → Status
- Registry → Links

### End-to-End Tests

vollständiger Pfad über Flow 1 bis 3.

### Recovery Tests

- Fehler zwischen temporärem und finalem Schreiben
- Ollama Timeout
- Flow-3-Fehler nach gültiger Updateablage
- Status-Restore

## 30.2 Test-Fixtures

Ablage ohne geschützte Volltexte:

```text
System/Automation/test-fixtures/
├── gmail/
├── reviewed/
├── expected/
└── errors/
```

## 30.3 Verbindliches Testpaket

1. neuer technischer Ticker
2. zweites technisches Update
3. nachträglich älteres Update
4. fundamentaler Beitrag
5. sonstiger Beitrag
6. Gmail-Dublette
7. Dateinamenskonflikt
8. ungültiges YAML
9. fehlender Ticker
10. Ollama Timeout
11. Registry nicht lesbar
12. gültige Concept Links
13. toter Link wird nicht eingefügt
14. Status-History
15. Neustart und Wiederanlauf

## 30.4 Regression

Vor jeder Änderung an Flow 1 bis 3 werden die vorhandenen Fixtures erneut ausgeführt.

---

# 31. Performance- und Ressourcenarchitektur

## 31.1 Queueing

Version 1 nutzt serielle Verarbeitung mit Batchgröße 1.

## 31.2 Begrenzungen

- nur ein Ollama-Analysejob gleichzeitig
- große PDFs nicht gleichzeitig
- Flow 3 pro Ticker sperren, damit nicht zwei Statusläufe parallel schreiben

## 31.3 Ticker Lock

Ein einfacher Lock kann als temporäre Lockdatei umgesetzt werden:

```text
System/Automation/locks/Technisch_NVDA.lock
```

Der Lock enthält:

- Correlation ID
- Startzeit
- Workflow
- Ablaufzeit

Stale Locks werden kontrolliert erkannt.

## 31.4 Timeout

Je KI-Use-Case getrennte Timeouts. Ein Timeout führt nicht zu einer unvollständigen finalen Datei.

## 31.5 Buchverarbeitung

Chunk-Analysen werden sequenziell oder mit sehr kleiner Parallelität ausgeführt.

---

# 32. Integrationsarchitektur für aktuelle Marktdaten

## 32.1 Spätere Komponente

Ein separater Market Data Adapter liefert:

- Symbol
- Timestamp
- Last Price
- Tagesveränderung
- OHLCV
- gegebenenfalls Corporate Actions

## 32.2 Trennung

Marktdaten werden nicht ungeprüft in Analystenupdates geschrieben. Sie werden als eigene Datenquelle mit Abrufzeitpunkt behandelt.

## 32.3 Briefing-Flow

```text
Schedule
→ neue Analystenstatus laden
→ Marktpreise laden
→ Triggernähe berechnen
→ RAG-Fachwissen abrufen
→ Briefing erzeugen
→ Quellen und Datenzeitpunkt darstellen
```

## 32.4 Keine Orderactions

Das Briefing endet bei Research und Beobachtung. Keine automatische Order.

---

# 33. Migrations- und Einführungsplan

## Phase A: Bestehende Architektur stabilisieren

- Flow 1 bis 3 exportieren
- tatsächliche Felder und Pfade gegen dieses Konzept vergleichen
- gemeinsame config.json einführen
- Datenverträge dokumentieren
- zentralen Error Workflow einführen

## Phase B: Tests und Abnahme

- Fixtures erstellen
- End-to-End-Testpaket ausführen
- Fehler beheben
- Flowversion 1.0 freigeben

## Phase C: Concept-System produktiv machen

- Registry laden
- Links validieren
- Aliasse ergänzen
- Backfill-Flow implementieren

## Phase D: Dokumentenpipeline

- PDF-Extraktion
- OCR-Decision
- Chunking
- Map-Reduce-Analyse
- Quellenanalyse

## Phase E: Wissensnotizen

- Kandidatenerkennung
- Review-Entwürfe
- finale Ablage und Indexpflege

## Phase F: RAG

- Qdrant
- Embeddings
- Indexer
- Retrieval-Workflow
- Quellenantworten

## Phase G: Marktbriefing und eigene Daten

- Marktdatenadapter
- Briefing
- Journal
- Strategien
- Backtests

---

# 34. Architekturentscheidungen

## ADR-001: Obsidian als System of Record

**Entscheidung:** Markdown-Vault bleibt führend.  
**Begründung:** Portabilität, direkte Lesbarkeit, lokale Kontrolle, Verlinkung.  
**Konsequenz:** RAG und n8n müssen aus Vault rekonstruierbar sein.

## ADR-002: n8n Self-Hosted

**Entscheidung:** Lokaler Docker-Betrieb.  
**Begründung:** Dateisystemzugriff, Datenschutz, keine laufende n8n-Cloudgebühr.  
**Konsequenz:** Betrieb und Backup liegen beim Nutzer.

## ADR-003: Ollama als primäre KI-Laufzeit

**Entscheidung:** lokale LLM-Verarbeitung.  
**Begründung:** keine Tokenkosten, private Inhalte bleiben lokal.  
**Konsequenz:** Modellqualität und Hardwaregrenzen müssen durch Schema, Chunking und Review kompensiert werden.

## ADR-004: Drei Analysten-Hauptflows

**Entscheidung:** Ingestion, Routing/Historisierung und Statuskonsolidierung getrennt.  
**Begründung:** Testbarkeit, klare Verantwortung, Fehlerisolierung.  
**Konsequenz:** versionierte Übergabeverträge sind erforderlich.

## ADR-005: Concept Registry statt KI-Pfade

**Entscheidung:** Links werden aus kontrollierter Registry erzeugt.  
**Begründung:** keine erfundenen oder toten Obsidian-Pfade.  
**Konsequenz:** Registry muss gepflegt und versioniert werden.

## ADR-006: Append-only Updates, versionierte Statusdateien

**Entscheidung:** Updates unveränderlich, Status aktualisierbar mit History.  
**Begründung:** zeitliche Nachvollziehbarkeit.  
**Konsequenz:** Flow 2 und 3 benötigen unterschiedliche Schreibregeln.

## ADR-007: RAG erst nach geprüfter Wissensbasis

**Entscheidung:** Qdrant nicht Teil der ersten Produktionsstufe.  
**Begründung:** Retrieval auf ungeprüften und instabilen Inhalten würde schlechte Ergebnisse verstärken.  
**Konsequenz:** zuerst Flow 1 bis 3 und statische Quellenpipeline stabilisieren.

---

# 35. Technische Definition of Done

## 35.1 Flow 1

- Gmail-Trigger produktiv
- Volltext zuverlässig extrahiert
- Dublettenschutz
- Ollama JSON-Schema validiert
- Review-Markdown korrekt
- Fehlerlabel und Error Workflow
- Concept-Feld vorhanden

## 35.2 Flow 2

- nur geprüfte Dateien
- Routing korrekt
- Pfade sicher
- Update atomar abgelegt
- Chronologie korrekt
- kontrollierte Links
- Idempotenz
- Flow-3-Handoff validiert

## 35.3 Flow 3

- alle relevanten Updates geladen
- Statusschema validiert
- alte Aussagen korrekt behandelt
- Status-History
- atomare Ersetzung
- keine Beschädigung bei Fehler

## 35.4 Gesamtbetrieb

- Docker-Neustart funktioniert
- Ollama erreichbar
- Backups vorhanden
- Workflows exportiert
- Testpaket bestanden
- Logs nachvollziehbar
- keine Änderungen außerhalb Trading

---

# 36. Unmittelbare technische nächste Schritte

1. Bestehende drei Workflow-JSONs sichern und versionieren.
2. Reale Flowfelder gegen die Datenverträge dieses Dokuments vergleichen.
3. Abweichungen dokumentieren und gemeinsame Feldnamen festlegen.
4. `config.json` und Schemaordner anlegen.
5. zentralen Error Workflow erstellen.
6. Correlation ID durch Flow 1 bis 3 führen.
7. sichere Transaktionsgrenze zwischen Flow 2 und Flow 3 umsetzen.
8. End-to-End-Fixtures erstellen.
9. definiertes Testpaket ausführen.
10. erst danach Bücher- und Studienflow implementieren.

---

# 37. Übergabe an technische Umsetzer

Der Umsetzer soll:

- vorhandene Flows zuerst analysieren und nicht blind neu bauen,
- Unterschiede zwischen Ist-Flow und Zielkonzept dokumentieren,
- Änderungen additiv umsetzen,
- importierbare n8n-JSON-Dateien liefern,
- Expressions, Commands und JavaScript vollständig prüfen,
- keine Credentials verändern,
- keine Pfade außerhalb Trading erzeugen,
- jeden Seiteneffekt idempotent gestalten,
- vorhandene Dateien nicht still überschreiben,
- Fehlerzustände aktiv modellieren,
- für jeden Flow Test-Fälle und erwartete Outputs mitliefern,
- Datenverträge versioniert halten,
- keine KI-Pfade oder fachlichen Fakten erfinden lassen.

---

# 38. Kurzarchitektur

```text
Gmail
  ↓
Flow 1: Ingestion + Ollama Extraction
  ↓
Inbox/Reviewed
  ↓ manuelle Freigabe
Flow 2: Validation + Routing + Updates + Links + Chronology
  ↓ versionierter JSON-Vertrag
Flow 3: Status Synthesis + History + Atomic Replace
  ↓
Obsidian Research/Analysten

Statische PDFs
  ↓
Document Pipeline: Hash + Extract/OCR + Chunk + Analyze + Synthesize
  ↓
Quellenanalysen
  ↓
Wissensnotiz-Pipeline
  ↓
Notes + Indizes

Geprüfter Vault
  ↓
RAG Indexer + Ollama Embeddings
  ↓
Qdrant
  ↓
Claude / lokaler Retrieval-Chat / Daily Briefing
```
