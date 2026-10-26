# Technisches Umsetzungskonzept
## n8n-Workflow: Gmail-Analystenposts nach Obsidian

**Projekt:** Trading Knowledge Brain  
**Umsetzungsstufe:** Erster produktiver Automatisierungspilot  
**Status:** Konzept zur Implementierung  
**Zielpfad im n8n-Container:** `/vault/Finanzen/Trading`  

---

# 1. Ziel und Abgrenzung

## 1.1 Ziel

Der Workflow soll neue E-Mail-Benachrichtigungen des definierten Patreon-Analysten aus einem Gmail-Postfach erkennen, den vollständigen verfügbaren E-Mail-Inhalt abrufen, bereinigen und als standardisierte Markdown-Datei im Obsidian-Bereich `Trading` speichern.

Jeder Analystenbeitrag wird als eigenständiger historischer Stand zu einem Wertpapier behandelt. Bestehende Updates dürfen nicht überschrieben werden.

## 1.2 Ergebnis des ersten Workflows

Für jede passende Gmail-Nachricht entsteht genau eine Markdown-Datei unter:

```text
/vault/Finanzen/Trading/Inbox/Reviewed/
```

Beispiel:

```text
2026-09-03 - NVDA - Analysten-Update.md
```

Die Datei folgt den in Obsidian definierten Konventionen und dem Template:

```text
/vault/Finanzen/Trading/Templates/Analysten Updates.md
```

## 1.3 Nicht Bestandteil der ersten Version

- keine automatische Aktualisierung von `NVDA - Aktueller Analystenstand.md`
- keine automatische endgültige Ablage unter `Research/Analysten`
- keine automatische Ableitung allgemeiner Wissensnotizen
- keine automatische Analyse von Chartbildern
- kein Patreon-Webscraping
- kein RAG
- kein automatisches Löschen von E-Mails oder Obsidian-Dateien
- keine Verarbeitung fundamentaler PDF-Anhänge

Diese Funktionen werden nach erfolgreicher Validierung als getrennte Erweiterungsworkflows umgesetzt.

---

# 2. Verbindliche Projektregeln

Der Workflow muss folgende Regeln aus dem Trading-Projekt einhalten:

1. Ausschließlich innerhalb von `/vault/Finanzen/Trading` schreiben.
2. Jede KI-Ausgabe erhält zunächst `status: review`.
3. Neue Dateien werden nur nach `Inbox/Reviewed` geschrieben.
4. Bereits vorhandene Dateien werden nicht überschrieben.
5. Jedes Update bleibt als historischer Stand erhalten.
6. Aussagen werden als Einschätzung des Analysten gekennzeichnet.
7. Nicht genannte Informationen werden nicht erfunden.
8. Fehlende Angaben werden leer gelassen oder als `nicht genannt` vermerkt.
9. Relative Datumsangaben werden nicht ohne Prüfung als exaktes Veröffentlichungsdatum übernommen.
10. Die Verarbeitung muss wiederholbar und gegen Dubletten geschützt sein.

---

# 3. Eingangsquelle Gmail

## 3.1 Empfohlene Gmail-Vorbereitung

In Gmail wird ein eigenes Label angelegt:

```text
Patreon-Analyst-New
```

Optional zusätzlich:

```text
Patreon-Analyst-Processed
Patreon-Analyst-Error
```

Eine Gmail-Filterregel weist passende E-Mails automatisch dem Label `Patreon-Analyst-New` zu.

Empfohlene Filtermerkmale:

- Absenderadresse der Patreon-Benachrichtigung
- Analystenname im Absender oder Betreff
- Patreon-Link oder wiederkehrender Text im Nachrichteninhalt

Die konkrete Absenderadresse muss anhand einer echten E-Mail bestimmt werden. Sie darf nicht geraten werden.

## 3.2 Warum Gmail-Label statt nur Absenderfilter

Das Label bildet eine kontrollierte Eingangswarteschlange. Falls Patreon später Absender oder Betreff ändert, kann die Gmail-Regel angepasst werden, ohne den n8n-Workflow grundlegend umzubauen.

## 3.3 Vollständiger Text oder Vorschau

Der Workflow kann nur den Inhalt verarbeiten, der tatsächlich in der E-Mail enthalten ist. Enthält die Patreon-E-Mail nur eine Vorschau, wird die Markdown-Datei entsprechend als unvollständig markiert:

```yaml
inhalt_vollständig: false
```

Enthält die E-Mail den vollständigen Post:

```yaml
inhalt_vollständig: true
```

Die erste Workflow-Version greift nicht automatisiert auf den geschützten Patreon-Post zu.

---

# 4. Zielarchitektur des Workflows

```text
[Gmail Trigger]
      |
      v
[Filter und Eingangskontrolle]
      |
      v
[Gmail: vollständige Nachricht abrufen]
      |
      v
[HTML/Text normalisieren]
      |
      v
[Nachrichten- und Quellenmetadaten bilden]
      |
      v
[Dublettenprüfung]
      |
      v
[KI-Strukturierung nach Analysten-Template]
      |
      v
[Validierung des KI-Ergebnisses]
      |
      v
[Markdown zusammensetzen]
      |
      v
[Markdown in Binärdatei umwandeln]
      |
      v
[Datei nach Inbox/Reviewed schreiben]
      |
      v
[Gmail-Label aktualisieren]
      |
      v
[Verarbeitung protokollieren]
```

---

# 5. Workflow-Komponenten und Node-Reihenfolge

## Node 1: Gmail Trigger

**Zweck:** Neue passende E-Mails erkennen.

**Konfiguration:**

- Event: `Message Received`
- Polling: zunächst alle 15 Minuten oder manuell während des Tests
- Label: `Patreon-Analyst-New`
- Read Status: vorzugsweise `Unread only`
- Simplify: zunächst `On`
- Max Emails per Poll: zunächst `5`
- Spam und Papierkorb: nicht einschließen

**Ausgabe:**

- Gmail Message ID
- Betreff
- Absender
- Empfangsdatum
- Gmail Labels

**Hinweis:** Der Trigger liefert in der vereinfachten Ausgabe primär Header und Identifikatoren. Der vollständige Nachrichteninhalt wird deshalb im nächsten Node separat abgerufen.

## Node 2: Gmail Get Message

**Zweck:** Vollständige Nachricht anhand der Message ID abrufen.

**Konfiguration:**

- Resource: `Message`
- Operation: `Get`
- Message ID: Expression aus Node 1
- Simplify: abhängig von der tatsächlichen Ausgabe testen; falls im vereinfachten Modus Body oder HTML fehlt, auf Raw-Ausgabe umstellen

**Erwartete Daten:**

- Plain-Text-Body oder HTML-Body
- Betreff
- Absender
- Versandzeitpunkt
- Nachrichten-ID
- Links
- gegebenenfalls Anhänge oder Inline-Bilder

## Node 3: Filter oder IF

**Zweck:** Sicherstellen, dass nur die gewünschte Analystenquelle verarbeitet wird.

**Prüfungen:**

- Label entspricht `Patreon-Analyst-New`
- Absender entspricht der realen Patreon-Absenderadresse
- Analystenname oder Patreon-URL ist im Betreff beziehungsweise Body vorhanden
- Nachrichten-ID ist vorhanden

**Fehlerpfad:** Nicht passende Nachrichten werden nicht verarbeitet und erhalten kein Processed-Label.

## Node 4: Inhalt auswählen und bereinigen

**Zweck:** Bestmöglichen Textkörper bestimmen.

**Logik:**

1. Plain Text verwenden, wenn vollständig und lesbar.
2. Andernfalls HTML verwenden.
3. Bei HTML den n8n-Markdown-Node mit `HTML to Markdown` einsetzen.
4. Navigations-, Footer-, Tracking- und Abmeldetexte soweit zuverlässig möglich entfernen.
5. Originaltext nicht inhaltlich umformulieren.

**Ergebnisfelder:**

```text
email_subject
email_from
email_date
email_message_id
email_body_clean
source_url
content_complete
```

## Node 5: Metadaten vorbereiten

**Zweck:** Deterministische Daten vor der KI bilden.

Die folgenden Angaben sollen möglichst ohne KI aus Headern und Betreff ermittelt werden:

- Plattform: Patreon
- Analyst: The Long Investor
- Gmail Message ID
- Empfangsdatum
- Betreff
- Quell-URL, sofern im Text vorhanden

Die KI soll nur fachliche beziehungsweise nicht deterministisch erkennbare Angaben ermitteln:

- Instrument
- Ticker
- Veröffentlichungsdatum des Posts
- Analyseart
- Zeithorizont
- technische Szenarien und Marken

## Node 6: Dublettenprüfung

**Zweck:** Dieselbe E-Mail nicht zweimal verarbeiten.

### Primärer Dublettenschlüssel

```text
Gmail Message ID
```

### Einfache Umsetzung in Version 1

Vor dem KI-Aufruf wird im Zielordner nach einer Datei beziehungsweise Protokollreferenz mit der Message ID gesucht.

Empfohlene Metadatenzeile in jeder Analystendatei:

```yaml
gmail_message_id: "..."
```

Zusätzlich kann ein lokales Verarbeitungsprotokoll geführt werden:

```text
/vault/Finanzen/Trading/System/Automation/processed-analyst-emails.json
```

### Verhalten bei Dublette

- keine neue Markdown-Datei erzeugen
- Gmail optional mit `Patreon-Analyst-Processed` markieren
- Workflow als `duplicate_skipped` protokollieren

## Node 7: KI-Strukturierung

**Zweck:** Den bereinigten Originaltext in die Felder des Analysten-Templates einordnen.

### Empfohlenes Betriebsmodell für den Pilot

Für den ersten funktionsfähigen Workflow kann wahlweise verwendet werden:

- lokal: Ollama mit einem kleinen bis mittleren Instruktionsmodell
- alternativ: Cloud-KI per API, falls die lokale Qualität nicht ausreicht

NotebookLM ist für diesen automatisierten n8n-Schritt nicht vorgesehen.

### Ausgabeformat

Die KI soll kein fertiges freies Markdown erzeugen, sondern zunächst strukturiertes JSON. Dadurch kann n8n Pflichtfelder prüfen und Markdown kontrolliert zusammensetzen.

Vorgesehenes Schema:

```json
{
  "published_date": "YYYY-MM-DD oder leer",
  "date_status": "confirmed|derived|unknown",
  "instrument": "",
  "ticker": "",
  "isin": "",
  "analysis_types": ["technisch"],
  "time_horizon": "",
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
  "missing_information": []
}
```

### Systemprompt für die KI

```text
Du strukturierst einen einzelnen, zeitpunktbezogenen Analystenbeitrag für eine private Obsidian-Wissensdatenbank.

Verwende ausschließlich den bereitgestellten E-Mail-Inhalt und die bereitgestellten Metadaten.
Erfinde keine Kursmarken, Szenarien, Datumsangaben, Instrumente, Ticker, Zeiteinheiten oder Chartdetails.
Kennzeichne fehlende oder unsichere Angaben.
Trenne das Primärszenario vom Alternativszenario.
Behalte Zahlen, Währungen und Bedingungen exakt bei.
Formuliere die Aussagen als Einschätzung des Analysten, nicht als objektive Tatsache oder Kaufempfehlung.
Wenn die E-Mail nur eine Vorschau enthält, setze content_complete auf false.
Gib ausschließlich gültiges JSON gemäß dem vorgegebenen Schema zurück.
```

### Userprompt

```text
E-Mail-Betreff:
{{email_subject}}

Absender:
{{email_from}}

E-Mail-Datum:
{{email_date}}

Gmail Message ID:
{{email_message_id}}

Bereinigter Originaltext:
{{email_body_clean}}
```

## Node 8: Ergebnisvalidierung

**Zweck:** Fehlerhafte KI-Ausgaben abfangen.

### Pflichtprüfungen

- JSON ist syntaktisch gültig.
- `instrument` oder `ticker` ist vorhanden.
- `summary` ist vorhanden.
- `source_facts` ist nicht leer.
- Veröffentlichungsdatum entspricht `YYYY-MM-DD` oder ist leer.
- Arrays enthalten nur Textwerte.
- Keine Datei wird ohne eindeutigen Namen geschrieben.

### Warnungen statt harter Fehler

Folgende fehlende Werte verhindern die Speicherung nicht:

- ISIN
- Zeithorizont
- Elliott-Wellen-Struktur
- Fundamentale Aussagen
- Kursziele
- Invalidationsmarken

### Fehlerpfad

Bei ungültigem Ergebnis:

```text
/vault/Finanzen/Trading/Inbox/Reviewed/_Errors/
```

Mindestinhalt des Fehlerberichts:

- Gmail Message ID
- Betreff
- Zeitpunkt
- Fehlermeldung
- rohe KI-Ausgabe

## Node 9: Sicherer Dateiname

**Zweck:** Eindeutigen und Windows-kompatiblen Dateinamen erzeugen.

### Format

```text
YYYY-MM-DD - TICKER - Analysten-Update.md
```

### Fallback

Wenn Datum oder Ticker fehlen:

```text
YYYY-MM-DD - UNBEKANNT - Analysten-Update - <kurze-message-id>.md
```

### Bereinigung

Aus Dateinamen entfernen oder ersetzen:

```text
< > : " / \ | ? *
```

### Dateikonflikt

Existiert der Dateiname bereits, wird nicht überschrieben. Stattdessen:

```text
YYYY-MM-DD - TICKER - Analysten-Update - <kurze-message-id>.md
```

## Node 10: Markdown erzeugen

**Zweck:** Das geprüfte JSON in ein kontrolliertes Obsidian-Dokument überführen.

### Zielstruktur

```markdown
---
typ: analysten-update
status: review
quelle: Patreon
analyst: The Long Investor
veröffentlicht: 2026-09-03
datum_status: confirmed
instrument: NVIDIA
ticker: NVDA
isin:
analyseart:
  - technisch
zeithorizont: kurzfristig bis mehrwöchig
quell_url:
gmail_message_id: "..."
inhalt_vollständig: true
vorgänger:
nachfolger:
importiert_am: 2026-09-03T22:00:00+02:00
---

# 2026-09-03 – NVIDIA – Analysten-Update

## Zusammenfassung

...

## Marktstand zum Veröffentlichungszeitpunkt

...

## Technisches Szenario

### Primärszenario

...

### Alternatives Szenario

...

## Unterstützungen

- ...

## Widerstände

- ...

## Kauf- oder Beobachtungszonen

- ...

## Invalidationsmarken

- ...

## Kursziele

- ...

## Elliott-Wellen-Struktur

...

## Fundamentale Aussagen

...

## Änderungen gegenüber dem vorherigen Update

Noch nicht automatisch bewertet. Dies erfolgt in einem späteren Status-Workflow.

## Bedingungen für eine Neubewertung

- ...

## Unsicherheiten und Risiken

- ...

## Originalinhalt

> Bereinigter Originaltext der E-Mail, damit die strukturierte Auswertung überprüfbar bleibt.

## Quellenangabe

- Plattform: Patreon
- Analyst: The Long Investor
- Gmail Message ID: ...
- Originalbeitrag: ...
- Importart: Gmail-Automation

## Verknüpfungen

- [[Trading/Research/Analysten/The Long Investor/<TICKER>/Status/<TICKER> - Aktueller Analystenstand|Aktueller Analystenstand]]
```

## Node 11: Markdown in Datei umwandeln

**Zweck:** Text für den Dateisystem-Node als Binärdatei bereitstellen.

Empfohlener Node:

```text
Convert to File
```

Konfiguration:

- Operation: Text to File
- Eingabefeld: erzeugter Markdown-Text
- Dateiname: berechneter sicherer Dateiname
- Encoding: UTF-8
- MIME Type: `text/markdown`

## Node 12: Datei schreiben

**Node:** `Read/Write Files from Disk`

**Operation:** `Write File to Disk`

**Ziel:**

```text
/vault/Finanzen/Trading/Inbox/Reviewed/<berechneter-dateiname>
```

**Regel:** Append deaktivieren. Vorherige Dubletten- und Dateikonfliktprüfung ist Pflicht.

## Node 13: Gmail kennzeichnen

Nach erfolgreichem Schreiben:

- Label `Patreon-Analyst-Processed` hinzufügen
- Label `Patreon-Analyst-New` entfernen
- Nachricht optional als gelesen markieren

Die E-Mail wird nicht gelöscht.

Bei Fehler:

- optional Label `Patreon-Analyst-Error` hinzufügen
- Label `Patreon-Analyst-New` zunächst behalten

## Node 14: Verarbeitung protokollieren

Empfohlene Protokolldatei:

```text
/vault/Finanzen/Trading/System/Automation/analyst-import-log.jsonl
```

Pro Ausführung eine JSON-Zeile:

```json
{
  "timestamp": "2026-09-03T22:00:00+02:00",
  "gmail_message_id": "...",
  "subject": "...",
  "ticker": "NVDA",
  "output_file": "/vault/Finanzen/Trading/Inbox/Reviewed/2026-09-03 - NVDA - Analysten-Update.md",
  "status": "created"
}
```

Keine E-Mail-Inhalte vollständig in das Log schreiben.

---

# 6. Ordnerstruktur für den Workflow

Vor Implementierung anlegen:

```text
/vault/Finanzen/Trading/System/Automation/
/vault/Finanzen/Trading/Inbox/Reviewed/_Errors/
```

Vorhanden und zu verwenden:

```text
/vault/Finanzen/Trading/Inbox/Analyst New/
/vault/Finanzen/Trading/Inbox/Reviewed/
/vault/Finanzen/Trading/Templates/Analysten Updates.md
/vault/Finanzen/Trading/Templates/Konventionen.md
/vault/Finanzen/Trading/Research/Analysten/
```

Der Gmail-basierte Workflow benötigt `Inbox/Analyst New` technisch nicht zwingend, weil Gmail selbst die Eingangswarteschlange bildet. Der Ordner bleibt für manuell importierte Posts und Tests erhalten.

---

# 7. Gmail-Authentifizierung

## 7.1 Ziel

n8n benötigt ein Gmail-OAuth2-Credential mit den für Lesen und Labelverwaltung erforderlichen Berechtigungen.

## 7.2 Vorgehen auf hoher Ebene

1. In Google Cloud ein Projekt für die private n8n-Integration anlegen.
2. Gmail API aktivieren.
3. OAuth-Zustimmungsbildschirm konfigurieren.
4. OAuth Client ID für eine Webanwendung erstellen.
5. Die von n8n angezeigte OAuth Redirect URL in Google Cloud eintragen.
6. Client ID und Client Secret in n8n als Gmail Credential speichern.
7. Gmail-Konto verbinden.
8. Verbindung mit `Get Many Messages` oder Gmail Trigger testen.

## 7.3 Sicherheitsregeln

- OAuth-Secret ausschließlich in n8n Credentials speichern.
- Keine Zugangsdaten in Obsidian ablegen.
- Nur das benötigte Gmail-Konto anbinden.
- Löschen von Nachrichten nicht in den Workflow aufnehmen.

---

# 8. Lokales KI-Modell und Hardware

## 8.1 Vorhandene Hardware

- AMD Ryzen 7 3700X, 8 Kerne und 16 Threads
- 16 GB RAM
- NVIDIA GTX 1050 Ti mit 4 GB VRAM

## 8.2 Realistische Nutzung

Die Hardware reicht für:

- n8n und Gmail-Verarbeitung
- HTML- und Markdown-Konvertierung
- Dateierstellung
- kleinere quantisierte lokale Sprachmodelle
- serielle Verarbeitung weniger Analystenposts

Die GPU ist für große Modelle begrenzt. Der erste lokale Test sollte mit einem kleinen quantisierten Modell erfolgen. Die Analystenposts sind relativ kurz, weshalb dieser Anwendungsfall deutlich geeigneter für lokale Verarbeitung ist als vollständige Bücher.

## 8.3 Betriebsentscheidung

Der Workflow soll jeweils nur eine Nachricht gleichzeitig verarbeiten. Parallelverarbeitung wird zunächst deaktiviert beziehungsweise vermieden.

Falls das lokale Modell fachlich unzuverlässig arbeitet, kann ausschließlich der KI-Node später durch eine Cloud-API ersetzt werden. Gmail-, Validierungs-, Markdown- und Dateisystemschritte bleiben unverändert.

---

# 9. Testkonzept

## Test 1: Manuelle Gmail-Testnachricht

Eine vorhandene Analystenmail erhält manuell das Label:

```text
Patreon-Analyst-New
```

Workflow manuell ausführen.

**Erwartung:** Eine `.md`-Datei entsteht in `Inbox/Reviewed`.

## Test 2: Dublette

Dieselbe Nachricht erneut mit dem Eingangslabel versehen und Workflow erneut ausführen.

**Erwartung:** Keine zweite identische Datei; Logstatus `duplicate_skipped`.

## Test 3: Fehlender Ticker

Eine Testmail ohne eindeutig erkennbaren Ticker verarbeiten.

**Erwartung:** Datei mit `UNBEKANNT` oder Fehlerpfad; keine erfundene Zuordnung.

## Test 4: Vorschau statt Volltext

Eine kurze Patreon-Vorschau verarbeiten.

**Erwartung:** `inhalt_vollständig: false` und Hinweis unter Unsicherheiten.

## Test 5: Bestehender Dateiname

Eine gleichnamige Testdatei vorher im Zielordner anlegen.

**Erwartung:** Bestehende Datei bleibt unverändert; neuer Dateiname enthält kurze Message ID.

## Test 6: Nicht passende E-Mail

Eine beliebige andere Gmail-Nachricht mit falschem Absender testen.

**Erwartung:** Keine Obsidian-Datei.

## Test 7: Sonderzeichen und Umlaute

Text mit Umlauten, Dollarzeichen, Gedankenstrichen und Prozentwerten verarbeiten.

**Erwartung:** UTF-8-Datei wird in Obsidian korrekt angezeigt.

---

# 10. Abnahmekriterien

Der erste Workflow ist abgenommen, wenn:

- Gmail OAuth funktioniert,
- nur E-Mails mit dem vorgesehenen Label verarbeitet werden,
- der vollständige verfügbare E-Mail-Text extrahiert wird,
- HTML-Artefakte weitgehend entfernt werden,
- eine gültige Markdown-Datei nach `Trading/Inbox/Reviewed` geschrieben wird,
- die Datei dem Analysten-Template entspricht,
- Quelle, Datum, Instrument, Ticker und Gmail Message ID gespeichert werden,
- fehlende Informationen nicht erfunden werden,
- Dubletten keine zweite identische Datei erzeugen,
- bestehende Dateien nicht überschrieben werden,
- erfolgreiche E-Mails ein Processed-Label erhalten,
- Fehler nachvollziehbar protokolliert werden,
- kein anderer Bereich des Obsidian-Vaults verändert wird.

---

# 11. Implementierungsreihenfolge

## Arbeitspaket 1: Gmail vorbereiten

1. Labels anlegen.
2. Eine echte Analysten-E-Mail prüfen.
3. Absender, Betreff und Vollständigkeit des Bodys dokumentieren.
4. Gmail-Filterregel anlegen.

## Arbeitspaket 2: Gmail mit n8n verbinden

1. Gmail API aktivieren.
2. OAuth Credential erstellen.
3. Gmail Trigger testen.
4. Vollständige Nachricht abrufen.

## Arbeitspaket 3: Textpipeline

1. Plain Text oder HTML auswählen.
2. HTML in Markdown umwandeln.
3. Footer und technische Artefakte bereinigen.
4. Originaltextfelder vereinheitlichen.

## Arbeitspaket 4: Deterministische Dateiablage

1. Metadaten setzen.
2. Dateinamen berechnen.
3. Dublettenprüfung implementieren.
4. zunächst eine Test-Markdown-Datei ohne KI schreiben.

## Arbeitspaket 5: KI ergänzen

1. lokales Modell anbinden.
2. strukturiertes JSON erzeugen.
3. Pflichtfelder validieren.
4. Markdown aus JSON zusammensetzen.

## Arbeitspaket 6: Gmail-Status und Logging

1. Processed-Label setzen.
2. Eingangslabel entfernen.
3. Fehlerlabel ergänzen.
4. JSONL-Protokoll schreiben.

## Arbeitspaket 7: Pilotabnahme

Die sieben definierten Tests durchführen und Ergebnisse dokumentieren.

---

# 12. Folgeworkflows nach erfolgreichem Pilot

## Workflow 2: Wertpapierstatus aktualisieren

```text
neues geprüftes Analysten-Update
-> ältere Updates desselben Tickers laden
-> Unterschiede klassifizieren
-> neuen Statusentwurf erzeugen
-> nach Reviewed schreiben
-> erst nach manueller Prüfung bisherigen Status ersetzen
```

## Workflow 3: Anhänge und Chartbilder

```text
E-Mail-Anhänge oder Inline-Bilder
-> Original lokal speichern
-> mit Analysten-Update verknüpfen
-> optional lokales Vision-Modell
-> chartbasierte Aussagen getrennt kennzeichnen
```

## Workflow 4: Fundamentale Analysten-PDFs

```text
PDF-Anhang
-> PDF-Text extrahieren
-> Quellenanalyse-Template verwenden
-> mit Instrument und Analysten-Update verknüpfen
```

## Workflow 5: Freigabe und endgültige Ablage

```text
status geprüft
-> Update nach Research/Analysten/<Analyst>/<Ticker>/Updates verschieben
-> Statusdatei aktualisieren lassen
-> Vorgang nach Terminated protokollieren
```

---

# 13. Unmittelbar nächster Umsetzungsschritt

Noch keine KI und keine Markdown-Datei bauen.

Zuerst wird in Gmail Folgendes angelegt:

```text
Patreon-Analyst-New
Patreon-Analyst-Processed
Patreon-Analyst-Error
```

Danach wird genau eine bestehende vollständige Analysten-E-Mail mit `Patreon-Analyst-New` markiert. Anschließend wird in n8n nur diese Minimalstrecke aufgebaut:

```text
Manual Trigger
-> Gmail: Get Many Messages mit Label Patreon-Analyst-New
-> Gmail: Get Message
-> Ausgabe kontrollieren
```

Erst wenn Betreff, Datum und vollständiger Body zuverlässig in n8n sichtbar sind, wird die Markdown- und KI-Verarbeitung ergänzt.
