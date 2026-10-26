# FinVault Projekt

Ein lokales, KI-gestütztes Wissens- und Research-System für Finanzmärkte, Investitionen und Trading.

## Vision

Das Trading Knowledge Brain soll langfristiges Fachwissen aus Büchern, wissenschaftlichen Studien und Research mit laufenden Analysteneinschätzungen, aktuellen Wertpapieranalysen und später eigenen Trading-Daten verbinden.

Das Ziel ist keine bloße Dokumentensammlung, sondern eine nachvollziehbare und verlinkte Wissensbasis, die unter anderem folgende Fragen beantworten kann:

- Was ist zu einem Trading-Konzept fachlich bekannt?
- Welche Quellen unterstützen oder kritisieren eine Methode?
- Wie hat sich die Einschätzung zu einem Wertpapier verändert?
- Welche technischen oder fundamentalen Bedingungen gelten laut gespeicherten Analysen?
- Welche Chancen, Risiken, Widersprüche und Wissenslücken bestehen?

Das System dient Research, Lernen und Entscheidungsunterstützung. Es erzeugt keine automatischen Kaufentscheidungen und führt keine Trades aus.

## Fachlicher Aufbau

Die Wissensbasis ist in **25 übergeordnete Themengebiete** gegliedert, darunter:

- Marktstruktur und Price Action
- Trendanalyse
- Unterstützungen und Widerstände
- Chart- und Candlestick-Muster
- Volumen, Orderflow und Market Microstructure
- Smart Money Concepts, Wyckoff und Elliott-Wellen
- Indikatoren, Momentum und Volatilität
- quantitative und statistische Konzepte
- Risiko- und Positionsmanagement
- Handelspsychologie und Performanceauswertung
- Fundamentalanalyse, Makroökonomie und Unternehmenskennzahlen

Unter den Hauptthemen befinden sich ungefähr **78 Unterthemen und 821 priorisierte Fachbegriffe**.

Die Lernpriorität wird über drei Stufen abgebildet:

- **A:** zwingend zu beherrschende Grundlagen
- **B:** vertiefende und spezialisierte Inhalte
- **C:** fortgeschrittene oder optionale Inhalte

## Wissensmodell

Das Projekt unterscheidet bewusst mehrere Ebenen:

1. **Originalquelle**  
   Buch, Studie, PDF, Analysten-E-Mail, Chart oder Transkript.

2. **Quellenanalyse**  
   Strukturierte Analyse einer statischen Quelle mit Aussagen, Regeln, Evidenz, Risiken, Fundstellen und Taxonomiezuordnung.

3. **Analystenupdate**  
   Zeitpunktbezogene Einschätzung zu einem konkreten Wertpapier. Jedes Update bleibt historisch erhalten.

4. **Aktueller Wertpapierstatus**  
   Konsolidierter technischer oder fundamentaler Stand aus mehreren Analystenupdates.

5. **Wissensnotiz**  
   Dauerhafte, themenbezogene Notiz, die Erkenntnisse aus mehreren geprüften Quellen verbinden kann.

## Nutzen

Das System ermöglicht:

- eine zentrale und lokal gespeicherte Trading-Wissensbasis,
- nachvollziehbare Quellen- und Analystenhistorien,
- strukturierte Verarbeitung großer Dokumentmengen,
- Verknüpfung von Wertpapieranalysen mit allgemeinem Fachwissen,
- kontrollierte KI-Unterstützung ohne laufende Tokenkosten,
- spätere semantische Fragen über den gesamten geprüften Bestand,
- eine belastbare Grundlage für Research-Briefings, Strategien, Backtests und Journalauswertungen.

## Technischer Überblick

```text
Gmail / PDFs / Bücher / Studien
              ↓
        n8n Workflows
              ↓
     lokale KI mit Ollama
              ↓
 strukturierte Markdown-Dateien
              ↓
      Obsidian Trading Vault
              ↓
 Claude über MCP / später lokales RAG
```

### Kernkomponenten

- **Obsidian:** führender Wissensspeicher und Benutzeroberfläche
- **n8n Self-Hosted:** Workflow-Orchestrierung und Automatisierung
- **Ollama:** lokale KI-Verarbeitung ohne nutzungsabhängige Tokenkosten
- **Docker Desktop:** lokaler Betrieb von n8n und später weiteren Diensten
- **Gmail:** Eingang für laufende Analystenbeiträge
- **Claude Desktop mit MCP:** flexible Abfrage- und Analyseschicht über dem Vault
- **Qdrant, später:** lokale semantische Suche und RAG

Der verbindliche n8n-Basispfad lautet:

```text
/vault/Finanzen/Trading
```

## Vorhandene Analysten-Flows

### Flow 1: Gmail-Analystenbeiträge extrahieren

```text
Flow1_Gmail_Analystenbeitraege_Extrahieren.json
```

Erkennt neue Analysten-E-Mails, bereinigt den Inhalt, strukturiert die Aussagen mit Ollama und erstellt eine Review-Markdown-Datei.

### Flow 2: Analystenbeiträge einsortieren und verlinken

```text
Flow2_Analystenbeitraege_Einsortieren_und_Verlinken.json
```

Validiert freigegebene Review-Dateien, ordnet sie nach Kategorie und Ticker ein, historisiert Updates, berechnet Vorgänger und Nachfolger und ergänzt kontrollierte Wissenslinks.

### Flow 3: Aktuellen Analystenstand konsolidieren

```text
Flow3_Aktuellen_Analystenstand_Konsolidieren.json
```

Vergleicht die historischen Updates eines Wertpapiers und erzeugt einen aktuellen technischen oder fundamentalen Gesamtstatus mit Versionshistorie.

## Versionen

### Version 1: Local Knowledge Foundation

Version 1 liefert die lokale, produktiv nutzbare Grundlage:

- stabile Analystenpipeline
- Verarbeitung von Büchern, Studien und PDFs
- Quellenanalysen
- Wissensnotiz-Entwürfe
- kontrollierte Freigabe und Indexpflege
- Verlinkungen über die Trading-Taxonomie
- Backup, Logging, Tests und Betriebsdokumentation

### Version 2: Semantic Research Assistant

Geplant sind unter anderem:

- lokale RAG- und Vektorsuche
- Qdrant und lokale Embeddings
- Quellenabfragen über den gesamten Wissensbestand
- aktuelle Marktdaten
- tägliche Research-Briefings
- mehrere Analystenquellen

### Version 3: Integrated Trading Research Platform

Mögliche spätere Erweiterungen:

- Trading-Journal
- Strategiebibliothek
- Backtests und Performanceanalyse
- Watchlists und Alerts
- Vergleich eigener Trades mit Fach- und Analystenwissen
- optionale Paper-Trading-Integration

## Work Packages für Version 1

Version 1 umfasst **28 Work Packages**:

- **WP 00–09:** bestehende Analystenpipeline stabilisieren, testen und abnehmen
- **WP 10–16:** Bücher-, Studien- und PDF-Pipeline einschließlich OCR, Chunking und Quellenanalyse
- **WP 17–21:** Wissensnotizen, Dublettenprüfung, Freigabe sowie Index- und Registry-Pflege
- **WP 22–27:** Backup, Monitoring, Sicherheit, Performance, Systemabnahme und Release

Die internen V1-Meilensteine sind:

```text
V1 Alpha             Analystenpipeline stabil
V1 Beta              statische Quellenpipeline funktionsfähig
V1 Release Candidate Wissensnotizpipeline vollständig
V1 Final             getestet, gesichert und dokumentiert
```

## Aktueller Projektstand

### Bereits vorhanden

- Obsidian-Trading-Bereich und grundlegende Ordnerstruktur
- 25 Hauptthemenordner und Indexdateien
- bereinigte Taxonomie mit A/B/C-Priorisierung
- Templates und Konventionen
- Docker Desktop, n8n und lokaler Vault-Zugriff
- lokale KI-Verarbeitung über Ollama
- Claude-Obsidian-Verbindung über MCP
- drei Analysten-Workflows
- NVDA-Pilot mit historischen Updates und aktuellem Status
- zentrale `concept-links.json` mit 821 Taxonomieeinträgen
- fachliches Masterkonzept
- technisches Architekturkonzept
- Work-Package-Projektplan

### Aktueller Meilenstein

```text
V1 Alpha: Analystenpipeline stabilisieren und vollständig abnehmen
```

### Unmittelbar nächste Schritte

1. **WP 00:** Baseline, Workflow-Exporte und Backup sichern
2. **WP 01:** Feldnamen, Pfade, Schemas und Datenverträge vereinheitlichen
3. **WP 02–04:** Flow 1 bis Flow 3 einzeln auditieren und stabilisieren
4. **WP 05:** Concept Registry produktiv anbinden
5. **WP 06–07:** gemeinsame Sub-Workflows und zentrale Fehlerbehandlung
6. **WP 08:** vollständiges End-to-End-Testpaket
7. **WP 09:** bestehende Pilotdaten in den stabilen V1-Stand migrieren

Erst danach beginnt die automatisierte Bücher- und Studienpipeline.

## Zentrale Projektregeln

- Obsidian bleibt die fachliche Quelle der Wahrheit.
- KI-Ausgaben werden zunächst als `review` gespeichert.
- Historische Updates werden nicht fachlich überschrieben.
- Statusdateien werden nur mit Sicherung ersetzt.
- KI darf keine Obsidian-Pfade erfinden.
- Originalquellen und abgeleitetes Wissen bleiben getrennt.
- Nur geprüfte Inhalte werden endgültig eingeordnet.
- Alle Automatisierungen bleiben innerhalb von `Finanzen/Trading`.
- Credentials und geschützte Quelleninhalte bleiben privat.
- Das System unterstützt Research und Lernen, führt jedoch keine Trades aus.

## Zentrale Dokumentation

```text
02_Master_Fachkonzept_Obsidian_Trading_Knowledge_Brain_V1_0.md
03_Technisches_Umsetzungs_und_Architekturkonzept_Trading_Knowledge_Brain_V1_0.md
04_Master_Projektplan_Workpackages_Trading_Knowledge_Brain_V1_0.md
```

## Projektstatus in einem Satz

> Das Trading Knowledge Brain befindet sich in der V1-Alpha-Phase: Die fachliche Struktur, lokale technische Plattform und drei Analysten-Flows sind vorhanden; als Nächstes werden die Flows konsolidiert, vollständig getestet und anschließend um die automatisierte Bücher-, Studien- und Wissensnotizpipeline erweitert.
