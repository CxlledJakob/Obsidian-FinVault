# Trading Knowledge Brain
## Master-Fachkonzept & Fachliche Spezifikation

**Fachliches Zielbild, Anforderungen, Prozesse, Informationsmodell, Automatisierungsumfang und Roadmap**  
**Version:** 1.0  
**Stand:** 26.10.2026  
**Dokumentstatus:** Verbindliche fachliche Projektgrundlage  
**Systembereich:** `Finanzen/Trading` im persönlichen Obsidian-Vault

---

# 1. Dokumentzweck

Dieses Dokument beschreibt das vollständige fachliche Zielbild des Projekts **Trading Knowledge Brain**. Es dient als verbindliche Grundlage für:

- fachliche Entscheidungen,
- die Weiterentwicklung des Obsidian-Vaults,
- die Umsetzung und Abnahme von n8n-Workflows,
- die Gestaltung von Templates und Metadaten,
- die Verarbeitung statischer und dynamischer Quellen,
- die spätere Einführung semantischer Suche und RAG,
- die Planung weiterer Projektphasen,
- die Übergabe an andere KI-Systeme, Business Analysten und technische Umsetzer.

Das Dokument konsolidiert den bisherigen Projektverlauf. Es unterscheidet ausdrücklich zwischen:

- fachlichem Zielbild,
- verbindlichen Regeln,
- bereits vorhandenem Stand,
- noch zu validierenden Funktionen,
- geplanten Erweiterungen.

Bei Widersprüchen zwischen älteren Chatentscheidungen und diesem Dokument gilt dieses Dokument als aktuelle fachliche Grundlage, sofern eine spätere Entscheidung nicht ausdrücklich dokumentiert wurde.

---

# 2. Vision

Das Trading Knowledge Brain ist eine lokale, KI-gestützte Research- und Wissensplattform für Finanzmärkte, Investitionen und Trading.

Das System soll langfristig unterschiedliche Wissensarten zusammenführen:

1. **dauerhaftes Grundlagenwissen** aus Büchern, Studien und Fachpublikationen,
2. **zeitpunktbezogene Analysteneinschätzungen** zu Aktien und anderen Wertpapieren,
3. **aktuelle Markt- und Unternehmensinformationen** als spätere Erweiterung,
4. **eigene Erkenntnisse, Strategien, Backtests und Journaldaten**,
5. **verknüpfte Fachkonzepte** aus technischer und fundamentaler Analyse.

Das Ziel ist keine bloße Dokumentensammlung. Es soll ein nachvollziehbares, verlinktes und erweiterbares Wissensnetz entstehen, das:

- Quellen historisch korrekt erhält,
- Aussagen ihrem Ursprung zuordnet,
- aktuelle Einschätzungen von dauerhaftem Wissen trennt,
- Beziehungen zwischen Wertpapieren, Analystenupdates und Fachkonzepten sichtbar macht,
- spätere Fragen über den gesamten Wissensbestand ermöglicht,
- Research unterstützt, ohne ungeprüfte Kaufentscheidungen zu automatisieren.

---

# 3. Fachliche Zielsetzung

## 3.1 Hauptziel

Innerhalb eines strukturierten Lern- und Aufbauprozesses soll ein tiefes, breit gefächertes Wissen über Finanzmärkte und Trading aufgebaut werden. Der Schwerpunkt liegt auf:

- technischer Analyse,
- Marktstruktur und Price Action,
- technischem Trading,
- Risiko- und Positionsmanagement,
- quantitativer und statistischer Prüfung,
- Handelspsychologie,
- Fundamentalanalyse,
- Makroökonomie,
- wertpapierbezogenem Research.

## 3.2 Forschung und Lernsystem

Das System soll die Bearbeitung folgender Fragen unterstützen:

- Welche fachlichen Grundlagen gelten für ein Konzept?
- Welche Quellen unterstützen oder kritisieren eine Methode?
- Welche Regeln nennt ein Analyst für ein bestimmtes Wertpapier?
- Wie hat sich eine Analysteneinschätzung über die Zeit verändert?
- Welche technischen oder fundamentalen Bedingungen gelten aktuell innerhalb des gespeicherten Quellenbestands?
- Welche Aussagen sind dauerhaftes Wissen und welche nur zeitpunktbezogen?
- Welche Quellen widersprechen sich?
- Welche Wissenslücken bestehen noch?
- Welche Themen sind aufgrund ihrer Priorität zuerst zu bearbeiten?

## 3.3 Nichtziel

Das System ist keine automatische Handelsmaschine und keine Garantie für profitable Entscheidungen.

Nicht Bestandteil des fachlichen Zielbilds sind aktuell:

- automatische Orderausführung,
- Broker-API-Anbindung,
- autonome Kauf- oder Verkaufsempfehlungen,
- ungeprüftes Live-Trading,
- öffentliche Weitergabe geschützter oder bezahlter Quellen,
- automatische Gleichsetzung von Analystenmeinungen mit objektiven Tatsachen.

---

# 4. Grundprinzipien

## 4.1 Local First

Der dauerhafte Wissensbestand liegt lokal im Obsidian-Vault. Cloud- oder externe KI-Dienste können ergänzend eingesetzt werden, dürfen aber nicht die einzige Wissenskopie darstellen.

## 4.2 Markdown First

Wissens- und Analysedokumente werden als Markdown-Dateien mit YAML-Frontmatter gespeichert.

## 4.3 Source First

Jede aus einer externen Quelle abgeleitete Aussage muss auf ihren Ursprung zurückführbar sein.

## 4.4 Human in the Loop

KI-generierte Inhalte sind zunächst Entwürfe. Fachlich relevante oder finale Inhalte werden kontrolliert freigegeben.

## 4.5 Historisierung statt Überschreiben

Zeitpunktbezogene Analystenupdates werden niemals durch spätere Updates ersetzt. Der aktuelle Status ist ein separates abgeleitetes Dokument.

## 4.6 Progressive Automation

Zuerst werden fachliche Regeln und Formate stabilisiert. Danach werden wiederkehrende Schritte automatisiert.

## 4.7 Kontrollierte Verlinkung

KI darf Konzepte erkennen, aber keine freien Obsidian-Zielpfade erfinden. Zielpfade stammen aus einer kontrollierten Registry.

## 4.8 Free First

Kostenlose und lokal ausführbare Lösungen werden bevorzugt, sofern Qualität, Wartbarkeit und Sicherheit ausreichen.

## 4.9 Nachvollziehbarkeit

Verarbeitungsstatus, Quelldatei, Gmail Message ID, Ablagepfad, Fehler und Änderungen müssen nachvollziehbar bleiben.

## 4.10 Abgrenzung des Vault-Bereichs

Automatisierungen dürfen ausschließlich innerhalb des Bereichs `Finanzen/Trading` arbeiten.

---

# 5. Scope und Roadmap

## 5.1 Phase 1: Wissensgrundlage und Analysten-Pipeline

- Obsidian-Struktur
- Trading-Taxonomie
- Templates und Konventionen
- Gmail-Import von Analystenbeiträgen
- lokale KI-Strukturierung
- Review-Prozess
- Routing nach technisch, fundamental und sonstige
- Historisierung je Ticker
- Fortschreibung des aktuellen Analystenstands
- fachliche Verlinkungen

## 5.2 Phase 2: Statische Literatur- und Quellenpipeline

- Bücher
- wissenschaftliche Studien
- institutionelles Research
- sonstige PDFs
- Transkripte und Textquellen
- Quellenanalysen
- Taxonomiezuordnung
- Ableitung von Wissensnotiz-Vorschlägen

## 5.3 Phase 3: Wissensnotizen und Indexpflege

- atomare Wissensnotizen
- Zusammenführung mehrerer Quellen
- Quellenpositionen und Gegenpositionen
- kontrollierte Aktualisierung der Hauptthemenindizes
- Alias- und Linkpflege

## 5.4 Phase 4: Semantische Suche und RAG

- lokale Embeddings
- Vektordatenbank
- inkrementelle Indexierung
- quellengestützte Antworten
- Claude oder lokale Oberfläche als Abfrageschicht

## 5.5 Phase 5: Research-Briefings und aktuelle Marktintegration

- aktuelle Markt- und Kursdaten
- neue Analystenentwicklungen
- wertpapierbezogene Statusänderungen
- tägliche oder manuelle Research-Briefings
- Beobachtungskandidaten mit Bedingungen, Risiken und Quellen

## 5.6 Phase 6: Eigene Trading-Daten

- Trading-Journal
- Strategien und Hypothesen
- Backtests
- Performanceauswertung
- Verknüpfung eigener Ergebnisse mit Fachwissen und Analysteneinschätzungen

---

# 6. Fachliche Taxonomie

## 6.1 Struktur

Das Wissenssystem verwendet 25 übergeordnete Themengebiete. Darunter liegen Unterthemen sowie konkrete Fachbegriffe.

Die vollständige bereinigte Taxonomie umfasst:

- 25 Hauptthemen,
- ungefähr 78 Unterthemen,
- 821 priorisierte Fachbegriffe,
- 816 eindeutige Begriffsnamen aufgrund einzelner Mehrfachzuordnungen.

## 6.2 Hauptthemen

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

## 6.3 Prioritäten

- **A:** allerwichtigste Grundlagen und zwingend zu beherrschende Themen
- **B:** vertiefende und spezialisierte Themen
- **C:** fortgeschrittene oder optionale Themen

## 6.4 Fachliche Bedeutung der Priorität

Die Priorität bestimmt:

- Lernreihenfolge,
- Recherchepriorität,
- Bearbeitungstiefe,
- Reihenfolge der Wissensnotizerstellung.

Die Priorität bestimmt nicht:

- Profitabilität,
- wissenschaftliche Belastbarkeit,
- allgemeine Richtigkeit,
- Eignung für jedes Marktumfeld.

## 6.5 Abbildung in Obsidian

- Hauptthemen werden als Ordner abgebildet.
- Jeder Hauptthemenordner besitzt eine gleichnamige Indexdatei.
- Unterthemen werden als Überschriften geführt.
- Fachbegriffe werden zunächst als Listeneinträge geführt.
- Eine eigene Wissensnotiz entsteht erst bei substanzieller Bearbeitung.
- Verknüpfungen bilden Beziehungen ab.
- Es werden keine 821 leeren Notizen vorsorglich angelegt.

---

# 7. Fachliches Informationsmodell

## 7.1 Originalquelle

Eine Originalquelle ist der unveränderte oder nachvollziehbar erhaltene Ausgangsinhalt.

Beispiele:

- PDF eines Buches,
- wissenschaftliche Studie,
- institutionelles Research,
- Patreon-E-Mail,
- Analystenpost,
- Chartbild,
- Video-Transkript.

## 7.2 Quellenanalyse

Eine Quellenanalyse beschreibt eine statische Quelle als Ganzes.

Pflichtinhalte:

- bibliografische Angaben,
- Quellentyp,
- analysierter Bereich,
- Zusammenfassung,
- Kernaussagen,
- Definitionen,
- Modelle,
- Regeln und Kriterien,
- Voraussetzungen,
- Beispiele,
- Risiken und Einschränkungen,
- empirische Evidenz,
- Kritik und Gegenpositionen,
- Fundstellen,
- Taxonomiezuordnung,
- Vorschläge für Wissensnotizen.

## 7.3 Analystenupdate

Ein Analystenupdate ist eine zeitpunktbezogene Einschätzung zu einem Instrument oder Markt.

Pflichtmerkmale:

- Quelle,
- Analyst,
- Veröffentlichungsdatum,
- Instrument,
- Ticker, soweit anwendbar,
- Kategorie,
- Gmail Message ID,
- strukturierter Inhalt,
- vollständiger verfügbarer Originalinhalt,
- Bearbeitungsstatus.

## 7.4 Wertpapierstatus

Ein Wertpapierstatus ist ein abgeleitetes Dokument aus mehreren Updates desselben Analysten, Tickers und derselben Kategorie.

Eigenschaften:

- kein Originaldokument,
- aktualisierbar,
- historisierbar,
- verweist auf alle verwendeten Updates,
- unterscheidet neue, weiterhin gültige, geänderte, nicht mehr gültige und unklare Aussagen.

## 7.5 Wissensnotiz

Eine Wissensnotiz behandelt ein klar abgegrenztes Fachkonzept.

Pflichtinhalte:

- Definition,
- Kernaussagen,
- Funktionsweise,
- Voraussetzungen,
- Anwendung,
- Regeln und Kriterien,
- Risiken und Grenzen,
- Beispiele,
- Quellen und Fundstellen,
- unterschiedliche Quellenpositionen,
- verwandte Themen.

## 7.6 Themenindex

Ein Themenindex ist die Navigations- und Übersichtsseite eines Hauptthemas.

Der Themenindex:

- strukturiert Unterthemen,
- zeigt A/B/C-Begriffe,
- verlinkt vorhandene Wissensnotizen,
- dient als Fallback-Linkziel,
- enthält nicht die vollständigen Inhalte ganzer Quellen.

## 7.7 Strategie

Eine aus einer Quelle übernommene Strategie wird zunächst als Hypothese gespeichert:

```yaml
status: hypothese
getestet: false
```

Eine Strategie gilt erst nach eigener Prüfung, Backtesting und gegebenenfalls Paper Trading als bewertet.

## 7.8 Trade und Journal

Eigene Trades werden später mit Strategie, Setup, Marktumfeld, Risiko, Ergebnis, Regelkonformität, Fehlern und Erkenntnissen verknüpft.

---

# 8. Metadaten- und Statuskonzept

## 8.1 Inhaltstypen

```text
quelle
analysten-update
analysten-wertpapierstatus
wissen
strategie
trade
übersicht
system
```

## 8.2 Statuswerte

```text
inbox
entwurf
review
geprüft
archiviert
aktiv
```

## 8.3 Bedeutungen

- `inbox`: eingegangen, noch nicht verarbeitet
- `entwurf`: erstellt, fachlich nicht geprüft
- `review`: wartet auf manuelle Prüfung
- `geprüft`: fachlich freigegeben
- `archiviert`: bleibt erhalten, wird nicht mehr aktiv gepflegt
- `aktiv`: aktuell gültiges System- oder Statusdokument

## 8.4 Freigaberegel

Der Zielprozess lautet:

```text
Flow 1 erzeugt status: review
→ Nutzerprüfung
→ Statusänderung auf geprüft
→ Flow 2 übernimmt die endgültige Ablage
```

Eine technische Testausnahme darf nicht unbemerkt in den Produktivbetrieb übergehen.

---

# 9. Obsidian-Zielstruktur

## 9.1 Basispfad

Windows:

```text
C:\Users\Kuba\Desktop\Obsidian_Desktop\Jakob_Obsidian_Finanzen\Finanzen\Trading
```

n8n/Docker:

```text
/vault/Finanzen/Trading
```

## 9.2 Fachliche Ordnerstruktur

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
│   └── 25 Hauptthemenordner
├── PDFs/
├── Research/
│   ├── Analysten/
│   ├── Quellen/
│   └── Taxonomie/
├── Strategies/
├── System/
│   ├── Automation/
│   └── Vault-Struktur.md
├── Templates/
└── Themenübersicht.md
```

## 9.3 Analystenstruktur

Der verbindliche Ordnername lautet zusammengeschrieben:

```text
TheLongInvestor
```

### Technisch

```text
Research/Analysten/TheLongInvestor/Technisch/<TICKER>/
├── Status/
│   ├── <TICKER> - Aktueller Stand.md
│   └── _History/
└── Updates/
```

### Fundamental

```text
Research/Analysten/TheLongInvestor/Fundamental/<TICKER>/
├── Status/
│   ├── <TICKER> - Aktueller fundamentaler Stand.md
│   └── _History/
└── Updates/
```

### Sonstige

```text
Research/Analysten/TheLongInvestor/Sonstige/
```

## 9.4 Inbox-Bedeutung

- `Analyst New`: manuell bereitgestellte Analystenquellen und Tests
- `New`: allgemeine statische Quellen
- `Reviewed`: KI-Entwürfe beziehungsweise zur Prüfung bereitgestellte Dokumente
- `Terminated`: abgeschlossene Verarbeitungsspur vor oder nach endgültiger Einsortierung

---

# 10. Templates

## 10.1 Vorhandene Templates

- `Konventionen.md`
- `Analysten Updates.md`
- `Analysten-Wertpapierstatus.md`
- `Quellenanalyse.md`
- `Wissensnotiz.md`

## 10.2 Analystenupdate

Das Analystenupdate umfasst abhängig von der Kategorie:

- Zusammenfassung,
- Marktstand,
- Primär- und Alternativszenario,
- Unterstützungen und Widerstände,
- Kauf- und Beobachtungszonen,
- Invalidationsmarken,
- Kursziele,
- Elliott-Wellen-Struktur,
- fundamentale Aussagen,
- Neubewertungsbedingungen,
- Risiken und Unsicherheiten,
- Originalinhalt,
- Quellenangabe,
- Verknüpfungen.

## 10.3 Technischer Wertpapierstatus

- Kurzüberblick
- aktives Primärszenario
- Alternatives Szenario
- Trigger
- Unterstützungen
- Widerstände
- Kauf- und Beobachtungszonen
- Kursziele
- Invalidationsbedingungen
- Elliott-Wellen-Stand
- Trendstruktur
- gleitende Durchschnitte
- Fibonacci-Niveaus
- offene Bestätigungen
- Änderungen
- Unsicherheiten
- verwendete Updates

## 10.4 Fundamentaler Wertpapierstatus

- Kurzüberblick
- Investmentthese
- Geschäftsentwicklung
- Wachstumstreiber
- Umsatz und Gewinn
- Margen und Cashflow
- Bilanz und Verschuldung
- Bewertung
- Chancen
- Risiken
- Neubewertungsbedingungen
- Änderungen
- Unsicherheiten
- verwendete Updates

---

# 11. Quellenarten

## 11.1 Statische Quellen

- Bücher
- Buchkapitel als Bestandteil vollständiger Bücher
- wissenschaftliche Studien
- institutionelles Research
- Fach-PDFs
- Webseiten und Fachartikel
- Video- und Audio-Transkripte
- eigene Notizen

## 11.2 Dynamische Quellen

- Patreon-E-Mails
- Analystenposts
- technische Wertpapierupdates
- fundamentale Wertpapierupdates
- allgemeine Markt-, Makro- und Portfolioinformationen

## 11.3 Quellenklassifikation

Statische und dynamische Quellen dürfen nicht gleich behandelt werden:

- Statische Quellen erzeugen Quellenanalysen und Wissensnotizen.
- Dynamische Analystenquellen erzeugen historische Updates und aktuelle Wertpapierstatus.
- Ein Analystenpost ist keine allgemeine Fachdefinition.
- Eine Buchaussage ist nicht automatisch empirischer Nachweis.
- Eine Strategiequelle ist keine Profitabilitätsgarantie.

---

# 12. Literatur- und Quellenrecherche

## 12.1 Ziel

Für jedes Hauptthema und Unterthema sollen schrittweise die fachlich wichtigsten Literaturquellen identifiziert werden.

## 12.2 Mengenregel

Es gibt keine feste Anzahl von Quellen je Thema.

- Wenn drei Werke ein Thema hochwertig abdecken, werden drei empfohlen.
- Wenn fünf oder mehr Quellen erforderlich sind, werden entsprechend mehr empfohlen.
- Qualität und Abdeckung sind wichtiger als eine künstliche Anzahl.

## 12.3 Bevorzugte Quellen

- wissenschaftliche Fachbücher
- Standardwerke
- wissenschaftliche Studien
- empirische Untersuchungen
- Veröffentlichungen von Universitäten
- Börsen, Zentralbanken und Finanzinstitutionen
- methodisch belastbares Research
- hochwertige technische Fachliteratur
- geeignete praxisorientierte Trading-Literatur

## 12.4 Qualitätsanforderungen

- bibliografische Angaben überprüfbar
- keine erfundenen Quellen
- ISBN oder DOI, soweit vorhanden
- wissenschaftliche Evidenz von Praxismeinung trennen
- Aktualität abhängig vom Thema bewerten
- Redundanz vermeiden
- Schwächen und Kontroversen nennen
- legalen Zugangsweg angeben
- kostenlose Quellen kennzeichnen

## 12.5 Ergebnis je Quelle

- Titel
- Autor
- Erscheinungsjahr
- Quellentyp
- Verlag, Journal oder Institution
- ISBN oder DOI
- behandelte Themen
- Kurzbeschreibung
- Nutzen für das Wissenssystem
- fachliches Niveau
- wissenschaftliche Qualität
- Stärken
- Einschränkungen
- Priorität
- Zugangsart
- legaler Fundort

---

# 13. n8n-Flow-Landschaft

## 13.1 Flow 1: Gmail-Analystenbeiträge extrahieren

**Dateiname:**

```text
Flow1_Gmail_Analystenbeitraege_Extrahieren.json
```

### Ziel

Neue Patreon-Analystenbeiträge aus Gmail erkennen, bereinigen, mit Ollama strukturieren und als Review-Markdown in Obsidian speichern.

### Kernablauf

1. Gmail Trigger sucht ungelesene Nachrichten mit Eingangslabel.
2. Vollständige Nachricht wird über Gmail Message ID geladen.
3. Betreff, Absender, Datum, Inhalt und Patreon-Link werden extrahiert.
4. Bei HTML wird bevorzugt `post-content` verwendet.
5. HTML, Tracking und irrelevante Bestandteile werden entfernt.
6. Quelle und Inhalt werden validiert.
7. Gmail Message ID wird auf Dublette geprüft.
8. Ollama erzeugt strukturiertes JSON.
9. Hauptkategorie wird auf `Technisch`, `Fundamental` oder `Sonstige` gesetzt.
10. KI-Ausgabe wird validiert und gegebenenfalls sicher normalisiert.
11. Markdown mit YAML und Originalinhalt wird erzeugt.
12. Dateikonflikt wird geprüft.
13. Datei wird nach `Inbox/Reviewed` geschrieben.
14. Import wird protokolliert.
15. Gmail-Labels werden aktualisiert.
16. Fehler gelangen in den Fehlerpfad.

### Zusätzliche Konzepterkennung

Flow 1 soll `erkannte_konzepte` erzeugen.

Beispiel:

```json
{
  "erkannte_konzepte": [
    {
      "begriff": "Unterstützung",
      "gefundene_bezeichnung": "Supportzone",
      "sicherheit": "hoch"
    }
  ]
}
```

Flow 1 erkennt nur. Flow 1 erzeugt keine freien Obsidian-Pfade und setzt keine finalen Links im Originaltext.

---

## 13.2 Flow 2: Analystenbeiträge einsortieren und verlinken

**Dateiname:**

```text
Flow2_Analystenbeitraege_Einsortieren_und_Verlinken.json
```

### Ziel

Geprüfte Review-Dateien validieren, nach Kategorie und Ticker einsortieren, unveränderlich archivieren, chronologisch verlinken und Flow 3 vorbereiten.

### Kernablauf

1. Markdown-Dateien aus `Inbox/Reviewed` lesen.
2. YAML und Inhalt parsen.
3. Pflichtfelder und `status: geprüft` validieren.
4. Metadaten normalisieren.
5. Gmail Message ID auf Dublette prüfen.
6. Nach `Technisch`, `Fundamental` oder `Sonstige` routen.
7. Tickerordner und Unterordner bei Bedarf anlegen.
8. Einzelupdate unter `Updates` speichern.
9. alle Updates derselben Kategorie und desselben Tickers laden.
10. chronologisch sortieren.
11. Vorgänger und Nachfolger berechnen.
12. Historienliste aktualisieren.
13. kontrollierte Wissenslinks ergänzen.
14. Übergabeobjekt für Flow 3 erzeugen.
15. Verarbeitung protokollieren.
16. Eingangsdatei nach `Terminated` verschieben.

### Schutzregeln

- keine fachlichen Inhalte historischer Updates überschreiben
- nur Navigations-, Link- und Verarbeitungsmetadaten kontrolliert ändern
- nachträglich importierte ältere Beiträge korrekt einsortieren
- `TheLongInvestor` immer zusammengeschrieben verwenden

---

## 13.3 Flow 3: Aktuellen Analystenstand konsolidieren

**Dateiname:**

```text
Flow3_Aktuellen_Analystenstand_Konsolidieren.json
```

### Ziel

Aus historischen Updates einen aktuellen technischen oder fundamentalen Wertpapierstatus erzeugen beziehungsweise fortschreiben.

### Kernablauf

1. Übergabeobjekt von Flow 2 empfangen.
2. Updates derselben Kategorie und desselben Tickers laden.
3. bisherigen Status laden, falls vorhanden.
4. Aussagen chronologisch vergleichen.
5. Aussagen klassifizieren als:
   - neu,
   - weiterhin gültig,
   - geändert,
   - nicht mehr gültig,
   - widersprüchlich oder unklar.
6. neuen Status vollständig erzeugen.
7. Quellen- und Konzeptlinks einfügen.
8. Status validieren.
9. bisherigen Status nach `_History` sichern.
10. aktuellen Status kontrolliert schreiben.
11. Ergebnis protokollieren.

### Fachliche Regel

Eine ältere Aussage ist nicht automatisch aufgehoben, wenn das neueste Update die Aussage nicht erwähnt. Eine Aufhebung setzt eine ausdrückliche Änderung oder einen klaren Widerspruch voraus.

---

# 14. Kategorien und Routing

## 14.1 Technisch

- Charttechnik
- Marktstruktur
- Elliott-Wellen
- Trendlinien
- Moving Averages
- Fibonacci
- Unterstützungen
- Widerstände
- Kursziele
- Trigger
- Invalidationsbedingungen

## 14.2 Fundamental

- Geschäftsentwicklung
- Finanzzahlen
- Wachstum
- Margen
- Cashflow
- Bilanz
- Bewertung
- Unternehmensrisiken
- Investmentthese

## 14.3 Sonstige

- allgemeine Kommentare
- Makrothemen
- Portfolioinformationen
- gemischte Inhalte
- nicht eindeutig klassifizierbare Beiträge

Sonstige Beiträge werden zunächst flach abgelegt. Für Sonstige besteht in Version 1 keine Pflicht zu tickerbezogenen Statusdateien.

---

# 15. Historisierung und Chronologie

## 15.1 Unveränderliche Updates

Jedes technische und fundamentale Analystenupdate bleibt als eigenständiges Quelldokument unter `Updates` erhalten.

## 15.2 Sortierung

1. Veröffentlichungsdatum
2. Importzeitpunkt
3. Gmail Message ID

## 15.3 Vorgänger und Nachfolger

```yaml
vorgänger: "[[vorherige Datei]]"
nachfolger: "[[nächste Datei]]"
```

## 15.4 Historienliste

Jede Update-Datei kann eine vollständige chronologische Liste aller Updates derselben Kategorie und desselben Tickers erhalten.

## 15.5 Nachträglicher Altimport

Neu importierte Dateien sind nicht zwingend die neuesten Beiträge. Bei einem älteren Beitrag wird die gesamte Reihenfolge neu berechnet.

## 15.6 Status-Historie

Vor dem Ersetzen eines aktuellen Status wird die vorherige Version nach `Status/_History` gesichert.

---

# 16. Concept-Link-System

## 16.1 Ziel

Analystenupdates und Wertpapierstatus sollen mit den relevanten Fachkonzepten im Wissenssystem verbunden werden.

## 16.2 Registry

Die zentrale Datei lautet:

```text
/vault/Finanzen/Trading/System/Automation/concept-links.json
```

Sie enthält:

- 25 Hauptthemen,
- 821 Taxonomiebegriffe,
- A/B/C-Priorität,
- Unterthema,
- Hauptthema,
- gültigen Zielpfad,
- Zieltyp,
- Aliasfeld.

## 16.3 Aufgabenverteilung

- Flow 1 erkennt Konzepte.
- Flow 2 validiert und setzt Links in Einzelupdates.
- Flow 3 setzt Links im konsolidierten Status.
- Ein späterer Wartungsflow ergänzt oder repariert alte Links.

## 16.4 Linkpriorität

1. konkrete vorhandene Wissensnotiz
2. Hauptthemen-Indexdatei als Fallback
3. kein Link bei fehlender kontrollierter Zuordnung

## 16.5 Schutzregeln

- keine KI-generierten Zielpfade
- keine toten Links
- Originalinhalt nicht durch Inline-Links verändern
- Links in separatem Abschnitt
- jeder Link höchstens einmal je Dokument
- keine leeren Wissensnotizen erzeugen

## 16.6 Noch offene Aliasarbeit

Die Registry enthält aktuell überwiegend leere Aliaslisten. Kontrolliert zu ergänzen sind unter anderem:

- Support
- Supportzone
- Resistance
- Wellencount
- Wellenzählung
- 50 WMA
- Moving Average
- Fibonacci Extension
- Fibonacci Retracement

Doppeldeutige Aliasse benötigen Kontextregeln.

---

# 17. Statische Quellenpipeline

## 17.1 Ziel

Vollständige Bücher, Studien und PDFs sollen automatisiert oder halbautomatisiert in strukturierte Quellenanalysen überführt werden.

## 17.2 Eingangsprozess

```text
Datei nach Inbox/New
→ Dateityp bestimmen
→ SHA-256-Dublette prüfen
→ Text extrahieren
→ OCR-Bedarf erkennen
→ Struktur erkennen
→ in Abschnitte teilen
→ Teilanalysen erzeugen
→ Gesamtanalyse zusammenführen
→ Taxonomie zuordnen
→ Quellenanalyse nach Reviewed
```

## 17.3 Vollständige Bücher

Der Nutzer möchte vollständige Bücher als PDF bereitstellen. Technisch werden diese zur Modellverarbeitung kapitel- oder abschnittsweise verarbeitet. Das Gesamtwerk bleibt die fachliche Einheit.

## 17.4 OCR

Bildbasierte oder gescannte PDFs müssen als `ocr_erforderlich` erkannt werden. Ohne verlässliche OCR erfolgt keine inhaltliche Automatisierung.

## 17.5 Fundstellen

Seiten-, Kapitel- und Abschnittsbezüge sollen möglichst erhalten bleiben.

## 17.6 Review

Quellenanalysen werden zunächst mit `status: review` gespeichert.

---

# 18. Wissensnotizpipeline

## 18.1 Ziel

Geprüfte Quellenanalysen sollen in Vorschläge für dauerhafte Wissensnotizen überführt werden.

## 18.2 Entscheidung je Konzept

- neue Wissensnotiz
- bestehende Wissensnotiz ergänzen
- nur Quellenverweis
- Dublette
- zu wenig Substanz

## 18.3 Erstellungskriterium

Eine Wissensnotiz entsteht nur, wenn ausreichende fachliche Substanz vorhanden ist:

- Definition oder klare Erklärung
- relevante Aussagen
- nachvollziehbare Quelle
- sinnvolle Abgrenzung
- Mehrwert gegenüber vorhandenem Inhalt

## 18.4 Indexpflege

Nach Freigabe einer Wissensnotiz wird der passende Begriff in der Hauptthemen-Indexdatei kontrolliert verlinkt.

## 18.5 Quellenpluralität

Widersprüchliche Quellenpositionen bleiben sichtbar. Das System erzeugt keine künstliche Einigkeit.

---

# 19. Qualitätssicherung

## 19.1 Quellenqualität

Quellen werden unterschieden nach:

- wissenschaftlichem Fachbuch,
- wissenschaftlicher Studie,
- institutionellem Research,
- Bildungsinhalt einer Börse oder Institution,
- Fachartikel,
- Analystenmeinung,
- Social-Media-Inhalt,
- eigener Notiz.

## 19.2 KI-Regeln

- keine unbelegten Ergänzungen
- keine erfundenen Kursmarken
- keine erfundenen Datumswerte
- Unsicherheit sichtbar machen
- Quellenaussage und Interpretation trennen
- strukturiertes JSON validieren
- optionales Feld darf Kernverarbeitung nicht zerstören

## 19.3 Dateischutz

- keine ungeprüften Überschreibungen
- keine automatische Löschung von Originalquellen
- Status-History vor Ersetzen
- Indexsicherung vor Änderung
- atomare oder sichere Schreibstrategie

## 19.4 Dublettenschutz

- Gmail Message ID für Analysten-E-Mails
- SHA-256-Hash für statische Dateien
- Dateinamenskonflikt ist nicht automatisch eine Dublette

## 19.5 Datumsqualität

Relative Angaben wie `vor 3 Tagen` dürfen nicht unkontrolliert in ein exaktes Datum umgewandelt werden. Datum und Datumsstatus werden getrennt behandelt.

---

# 20. Fehlerbehandlung

## 20.1 Fehlerklassen

- Gmail-Zugriff
- ungültiger Inhalt
- unzulässige Quelle
- Dublette
- Ollama nicht erreichbar
- ungültiges KI-JSON
- fehlender Ticker
- ungültige Kategorie
- ungültiges YAML
- Dateikonflikt
- Schreibfehler
- Linkregisterfehler
- ungültiger Zielpfad
- Statuskonsolidierung fehlgeschlagen
- OCR erforderlich

## 20.2 Verhalten

- keine falsche Erfolgsmeldung
- keine teilweise finale Ablage
- Eingangsdatei erhalten
- Fehler protokollieren
- Error-Label oder Fehlerordner setzen
- Retry nur für technisch vorübergehende Fehler
- fachlich unklare Fälle manuell prüfen

## 20.3 Fehlerordner

```text
Trading/Inbox/Reviewed/_Errors/
```

## 20.4 Retry

Wiederholungen werden begrenzt. Gmail Message ID beziehungsweise Datei-Hash bleiben unverändert.

---

# 21. Logging und Auditierbarkeit

## 21.1 Importlog

Dokumentiert mindestens:

- Zeitstempel
- Gmail Message ID
- Betreff
- Zieldatei
- Status

## 21.2 Routinglog

Empfohlener Pfad:

```text
Trading/System/Automation/analyst-routing-log.jsonl
```

## 21.3 Linklog

Zusätzliche Felder:

```json
{
  "detected_concepts": [],
  "inserted_links": 0,
  "unresolved_concepts": []
}
```

## 21.4 Datenschutz

Vollständige geschützte Quellentexte werden nicht zusätzlich in technische Logs kopiert.

---

# 22. Sicherheit und Datenschutz

## 22.1 Credentials

Credentials und Tokens werden ausschließlich in n8n Credentials, Ollama-Konfiguration oder dafür vorgesehenen sicheren Systemen gespeichert.

## 22.2 Vault-Grenze

Alle automatisierten Pfade müssen mit folgendem Basispfad beginnen:

```text
/vault/Finanzen/Trading
```

## 22.3 Bezahlte Quellen

Patreon-Inhalte bleiben privat. Das System dient der persönlichen Wissensverwaltung.

## 22.4 Cloud-Nutzung

Lokale Verarbeitung wird bevorzugt. Bei späterer Cloud-KI-Nutzung müssen Datenschutz, Kosten und Quellenvertraulichkeit neu bewertet werden.

## 22.5 Löschschutz

Originalquellen, geprüfte Notizen und Analystenupdates werden nicht automatisch gelöscht.

---

# 23. Betriebsmodell

## 23.1 Technische Umgebung

- Windows
- Docker Desktop
- n8n Self-Hosted Community Edition
- Ollama lokal
- Obsidian lokal
- Gmail als Analysten-Eingang
- Claude Desktop mit Obsidian-MCP als Dialog- und Analyseschicht

## 23.2 Hardware

- AMD Ryzen 7 3700X
- 8 Kerne / 16 Threads
- 16 GB RAM
- NVIDIA GTX 1050 Ti
- 4 GB VRAM

## 23.3 Ausführungsmodell

Der Rechner kann täglich gestartet werden. Workflows dürfen seriell und über längere Zeit laufen.

## 23.4 Performanceprinzipien

- kurze Analystenposts lokal mit Ollama
- keine unnötige Parallelverarbeitung
- Bücher in Abschnitten
- OCR und Vision getrennt behandeln
- große Prozesse in nachvollziehbare Flows zerlegen

## 23.5 Startreihenfolge

```text
Docker Desktop
→ n8n prüfen
→ Ollama prüfen
→ Workflows ausführen
→ Review durchführen
→ Fehlerlogs prüfen
```

---

# 24. Backup und Recovery

## 24.1 Sicherungsumfang

- gesamter Obsidian-Vault oder mindestens Trading-Bereich
- n8n-Daten
- n8n-Workflow-JSON-Dateien
- Automation-Systemdateien
- Taxonomie
- Concept Registry
- Import- und Routinglogs

## 24.2 Kritische Dateien

```text
Trading/System/Vault-Struktur.md
Trading/Templates/Konventionen.md
Trading/Research/Taxonomie/Trading_Themenstruktur_bereinigt.txt
Trading/System/Automation/concept-links.json
n8n-Flow-JSON-Dateien
```

## 24.3 Recovery-Test

Ein Backup gilt erst als funktionsfähig, wenn eine Testdatei erfolgreich wiederhergestellt wurde.

## 24.4 Status- und Indexänderungen

Vor Änderungen an aktuellen Statusdateien oder Themenindizes wird eine Sicherung beziehungsweise Vorversion erzeugt.

---

# 25. RAG-Zielbild

## 25.1 Zweck

Das spätere RAG-System soll relevante Abschnitte aus geprüften Inhalten abrufen und Antworten mit Quellenbezug erzeugen.

## 25.2 Indexierbare Inhalte

- geprüfte Wissensnotizen
- geprüfte Quellenanalysen
- Analystenupdates
- aktuelle Wertpapierstatus
- Strategien
- Journal und Backtestergebnisse

## 25.3 Nicht ungeprüft indexieren

- fehlerhafte Dokumente
- ungeprüfte Entwürfe, sofern nicht ausdrücklich als separater Index
- beschädigtes YAML
- Quellen ohne nachvollziehbaren Status

## 25.4 Technisches Zielbild

```text
Markdown
→ YAML und Text lesen
→ nach Überschriften chunking
→ Metadaten erhalten
→ lokale Embeddings
→ Qdrant oder vergleichbare Vektordatenbank
→ Retrieval
→ LLM-Antwort mit Quellenpfaden
```

## 25.5 RAG-Metadaten

- Dokumenttyp
- Hauptthema
- Unterthema
- Ticker
- Analyst
- Veröffentlichungsdatum
- Quellenart
- Status
- Dateipfad
- Fundstelle
- Aktualität

---

# 26. Tägliches Research-Briefing

## 26.1 Ziel

Aktuelle Entwicklungen mit dem langfristigen Wissensbestand verbinden.

## 26.2 Voraussetzung

Eine aktuelle und verlässliche Marktdatenquelle ist erforderlich. Analystenposts und Bücher allein reichen nicht für die Aussage, was heute im Markt relevant ist.

## 26.3 Inhalt

- wichtigste Veränderungen
- neue Analystenupdates
- Wertpapiere an relevanten Kursmarken
- Beobachtungskandidaten
- bullische Bedingungen
- Risiken und Gegenargumente
- fehlende Bestätigungen
- Fachwissen aus Büchern und Studien
- verwendete Quellen
- Datenzeitpunkt

## 26.4 Begrenzung

Das Briefing erzeugt keine automatische Kaufentscheidung und keine Order.

---

# 27. Aktueller Projektstand

## 27.1 Erledigt

### Obsidian und Fachstruktur

- Trading-Bereich eingerichtet
- 25 Hauptthemenordner angelegt
- 25 Indexdateien angelegt
- Themenübersicht erstellt
- Taxonomie bereinigt
- A/B/C-Priorisierung definiert
- Vault-Struktur dokumentiert
- Konventionen definiert
- Templates für Analysten, Status, Quellenanalyse und Wissensnotiz erstellt
- Research-Unterordner vorbereitet

### Infrastruktur

- Docker Desktop installiert
- Virtualisierung und WSL eingerichtet
- n8n lokal gestartet
- Vault-Mount erfolgreich getestet
- Ollama lokal vorgesehen und in der Analystenanalyse verwendet
- Claude-Obsidian-MCP-Verbindung eingerichtet beziehungsweise vorbereitet

### Analystenprozess

- Gmail-Importworkflow erstellt
- Kategorien technisch, fundamental und sonstige definiert
- Review-Ausgabe implementiert
- Gmail Message ID als Dublettenschlüssel definiert
- Routing- und Ablageworkflow erstellt
- Statuskonsolidierungsworkflow erstellt
- NVDA-Pilot mit mehreren Updates und Status durchgeführt
- Concept Registry erzeugt

## 27.2 Vorhandene Flows

```text
Flow1_Gmail_Analystenbeitraege_Extrahieren.json
Flow2_Analystenbeitraege_Einsortieren_und_Verlinken.json
Flow3_Aktuellen_Analystenstand_Konsolidieren.json
```

## 27.3 Noch nicht vollständig abgenommen

- End-to-End-Test aller drei Flows
- neuer technischer Ticker
- zweites Update
- nachträglich älteres Update
- fundamentaler Beitrag
- sonstiger Beitrag
- Dublette
- Dateikonflikt
- ungültiges YAML
- Ollama-Ausfall
- Concept-Registry-Laufzeitintegration
- Status-History und sichere Ersetzung
- Neustartverhalten
- vollständiger Backup-Test

## 27.4 Aktueller Meilenstein

```text
Flow 1 bis Flow 3 konsolidieren, testen und fachlich abnehmen.
```

---

# 28. Noch erforderliche Flows

## 28.1 Link-Wartung und Backfill

- alte Dateien prüfen
- fehlende Links ergänzen
- tote Links melden
- neue Detailnotizen gegenüber Index-Fallbacks priorisieren

## 28.2 Statische Quellen importieren

- Bücher
- Studien
- PDFs
- OCR-Erkennung
- Chunking
- Quellenanalyse
- Taxonomiezuordnung

## 28.3 Quellenanalyse zu Wissensnotizen

- Konzepte extrahieren
- Dubletten prüfen
- neue oder ergänzende Wissensnotizen vorschlagen
- Review-Dateien erzeugen

## 28.4 Wissensnotizen freigeben und Index aktualisieren

- geprüfte Wissensnotizen final ablegen
- Index sichern
- Taxonomiebegriff verlinken
- Änderungen protokollieren

## 28.5 RAG-Index aktualisieren

- geprüfte Dateien erkennen
- Hash vergleichen
- chunking
- Embeddings
- Vektordatenbank

## 28.6 Tägliches Briefing

- aktuelle Marktdaten
- neue Analystenänderungen
- Wissensabruf
- strukturierte Research-Ausgabe

## 28.7 Fehler-Retry

- technische Fehler erneut versuchen
- maximale Versuche
- fachliche Fehler nicht erzwingen

## 28.8 Backup und Integritätsprüfung

- Backups
- Workflow-Export
- YAML-Prüfung
- tote Links
- Dubletten
- Prüfbericht

---

# 29. End-to-End-Testkatalog

## Test 1: Neuer technischer Ticker

Erwartung:

- Flow 1 erzeugt Review-Datei.
- Flow 2 erzeugt Tickerstruktur und Update.
- Flow 3 erzeugt ersten technischen Status.

## Test 2: Zweites technisches Update

Erwartung:

- Historie wächst.
- Vorgänger und Nachfolger stimmen.
- Status wird aktualisiert.
- alter Status wird gesichert.

## Test 3: Nachträglich älteres Update

Erwartung:

- korrekte chronologische Einordnung.
- aktuelle Statuszeit bleibt korrekt.

## Test 4: Fundamental

Erwartung:

- separater Fundamentalpfad.
- technischer Status bleibt unverändert.

## Test 5: Sonstige

Erwartung:

- flache Ablage.
- kein Statuszwang.

## Test 6: Dublette

Erwartung:

- keine zweite Datei.
- kein erneuter Statuslauf.

## Test 7: Dateikonflikt

Erwartung:

- bestehende Datei bleibt erhalten.
- sicherer Alternativname.

## Test 8: Ungültiges YAML

Erwartung:

- keine finale Ablage.
- verständlicher Fehler.

## Test 9: Ollama-Ausfall

Erwartung:

- kein fälschlicher Erfolg.
- Gmail nicht als erfolgreich markieren.

## Test 10: Konzeptlinks

Erwartung:

- Konzepte erkannt.
- nur gültige Links gesetzt.
- Originaltext unverändert.

---

# 30. Fachliche Anforderungen

## 30.1 Muss

- lokale Obsidian-Wissensbasis
- nachvollziehbare Quellenherkunft
- Trennung der Wissensebenen
- 25-Themen-Taxonomie
- Analystenupdates historisieren
- technische und fundamentale Status getrennt führen
- Review und Freigabe
- Dublettenschutz
- keine automatische Überschreibung geprüfter Inhalte
- lokale KI-Verarbeitung für Analystenposts
- Fehlerprotokollierung
- nur Trading-Bereich verändern

## 30.2 Soll

- kontrollierte Fachverlinkungen
- automatische Tickerordner
- Vorgänger-/Nachfolgerlinks
- Status-History
- Quellenanalysen für Bücher und Studien
- atomare Wissensnotizen
- automatische Indexpflege nach Freigabe
- semantische Suche
- Backup-Prüfung

## 30.3 Kann

- Chartbildanalyse
- OCR
- automatische Aliaserweiterung
- RAG
- tägliche Briefings
- Marktdatenintegration
- eigene Journal- und Backtestauswertung
- mehrere Analysten
- weitere Assetklassen

---

# 31. Nichtfunktionale Anforderungen

- geringe laufende Kosten
- lokale Ausführbarkeit
- Nachvollziehbarkeit
- Wartbarkeit
- modulare Flows
- UTF-8-Kompatibilität
- Windows-kompatible Dateinamen
- sichere Wiederholbarkeit
- begrenzte Parallelität
- fehlertolerante optionale Felder
- Schutz vor Datenverlust
- erweiterbare Taxonomie
- austauschbares KI-Modell
- portable Markdown-Daten

---

# 32. Offene Entscheidungen

1. verbindliches Ollama-Modell
2. Modellparameter und Kontextlänge
3. praktischer Review-Auslöser
4. Trigger zwischen Flow 2 und Flow 3
5. Rollback bei Flow-3-Fehler
6. Aliasstrategie
7. Behandlung mehrfach zugeordneter Begriffe
8. Detailnotiz-Priorisierung in der Concept Registry
9. OCR-Werkzeug
10. Chartbildverarbeitung
11. Marktdatenquelle
12. Assetklassenumfang
13. Aufbewahrung von `Terminated`
14. Git-Versionierung
15. Mindestqualität statischer Quellen
16. Freigabeverfahren für Quellenanalysen
17. Zeitpunkt der RAG-Einführung
18. Backupfrequenz und Aufbewahrung

---

# 33. Risiken und Gegenmaßnahmen

## 33.1 Informationsüberflutung

**Gegenmaßnahme:** A-Themen priorisieren, keine leeren Massennotizen, Quellen kuratieren.

## 33.2 KI-Halluzination

**Gegenmaßnahme:** Quellbindung, JSON-Schema, Validierung, Review, Originalinhalt erhalten.

## 33.3 Falsche Taxonomiezuordnung

**Gegenmaßnahme:** kontrollierte Taxonomie, primäres Hauptthema, manuelle Prüfung bei Unsicherheit.

## 33.4 Doppelte Dateien

**Gegenmaßnahme:** Gmail Message ID und SHA-256-Hash.

## 33.5 Verlust historischer Aussagen

**Gegenmaßnahme:** unveränderliche Updates, Status separat, Status-History.

## 33.6 Tote oder falsche Links

**Gegenmaßnahme:** Registry, Existenzprüfung, Backfill-Flow.

## 33.7 Technische Überkomplexität

**Gegenmaßnahme:** separate Flows, stufenweise Umsetzung, klare Verantwortlichkeit.

## 33.8 Hardwarebegrenzung

**Gegenmaßnahme:** kleine Modelle, serielle Verarbeitung, Chunking.

## 33.9 Datenverlust

**Gegenmaßnahme:** Backup, Recovery-Test, sichere Schreiboperationen.

## 33.10 Unzulässige Nutzung geschützter Inhalte

**Gegenmaßnahme:** nur privater Gebrauch und rechtmäßig bezogene Inhalte.

## 33.11 Veraltete Analystenmeinung

**Gegenmaßnahme:** Zeitstempel, Historie, aktueller Status, keine Gleichsetzung mit Marktdaten.

---

# 34. Definition of Done

## 34.1 Aktuelle Analystenphase

- Flow 1 bis Flow 3 laufen End-to-End.
- alle Expressions und Codeblöcke sind geprüft.
- Kategorien routen korrekt.
- neue Tickerstrukturen entstehen automatisch.
- Updates bleiben unverändert erhalten.
- Chronologie stimmt.
- Status wird sicher fortgeschrieben.
- Status-History funktioniert.
- Concept Registry wird verwendet.
- Dubletten und Fehlerpfade funktionieren.
- andere Vault-Bereiche bleiben unverändert.
- Testkatalog ist bestanden.

## 34.2 Statische Quellenphase

- vollständige PDFs werden aufgenommen.
- Text und OCR-Bedarf werden erkannt.
- Chunking funktioniert.
- Quellenanalyse entspricht Template.
- Fundstellen bleiben erhalten.
- Dublettenschutz funktioniert.
- Review ist möglich.

## 34.3 Wissensphase

- Wissensnotizen sind atomar und quellenbezogen.
- unterschiedliche Quellenpositionen bleiben sichtbar.
- Hauptthemenindex wird kontrolliert gepflegt.
- keine unnötigen Dubletten.

## 34.4 RAG-Phase

- nur geprüfte Inhalte werden indexiert.
- Antworten enthalten Quellenpfade.
- Aktualisierungen werden inkrementell übernommen.
- sensible Inhalte bleiben im vorgesehenen Betriebsmodell.

---

# 35. Empfohlene nächste Arbeitspakete

## Arbeitspaket 1: Flow 1 bis Flow 3 konsolidieren

- Feldnamen vereinheitlichen
- Kategorien vereinheitlichen
- Pfade prüfen
- Concept Registry anbinden
- Statussicherung prüfen

## Arbeitspaket 2: End-to-End-Testpaket

- technischer Neuticker
- Folgeupdate
- älteres Update
- Fundamental
- Sonstige
- Dublette
- Fehlerfall

## Arbeitspaket 3: Review-Prozess finalisieren

- klare Änderung von `review` auf `geprüft`
- Trigger von Flow 2 definieren
- Fehler- und Rollbackregeln definieren

## Arbeitspaket 4: Linksystem abnehmen

- Konzepterkennung
- Registry-Validierung
- Zielprüfung
- Aliasergänzung
- Backfill planen

## Arbeitspaket 5: Backup und Recovery

- Vault sichern
- n8n exportieren
- Wiederherstellung testen

## Arbeitspaket 6: Bücher- und Studienflow

Erst nach Abnahme der Analystenpipeline.

---

# 36. Übergaberegeln für weitere KI-Chats

Eine weiterarbeitende KI muss:

1. dieses Dokument als fachliche Grundlage verwenden.
2. zwischen umgesetzt, getestet und geplant unterscheiden.
3. die bestehenden drei Flows nicht grundlos neu entwerfen.
4. additive, rückwärtskompatible Änderungen bevorzugen.
5. ausschließlich unter `/vault/Finanzen/Trading` arbeiten.
6. `TheLongInvestor` exakt verwenden.
7. historische Updates nicht überschreiben.
8. Status vor Ersetzung sichern.
9. `concept-links.json` als kontrollierte Linkquelle verwenden.
10. Credentials nicht verändern.
11. bei n8n-Erstellung importierbares JSON liefern.
12. alle Commands, Expressions und JavaScript-Blöcke vor Ausgabe vollständig prüfen.
13. Fehlerursachen intern analysieren und einen eindeutigen Fix liefern.
14. keine Quellen erfinden.
15. keine automatischen Kaufentscheidungen ausgeben.
16. bei Literaturrecherche ISBN ohne Bindestriche ausgeben.
17. Antworten kompakt halten, sofern kein umfassendes Dokument verlangt wird.

---

# 37. Kurzstatus

```text
Projekt:
Lokales, KI-gestütztes Trading Knowledge Brain in Obsidian.

Fachliche Basis:
25 Hauptthemen, ungefähr 78 Unterthemen und 821 priorisierte Begriffe.

Vorhandene Automatisierung:
Flow 1 = Gmail → strukturierte Analysten-MD in Reviewed
Flow 2 = Reviewed → Routing, Updates, Links und Historisierung
Flow 3 = Updates → aktueller technischer oder fundamentaler Status

Technik:
Windows, Docker Desktop, n8n, Ollama, Obsidian, Gmail, Claude MCP.

Aktueller Stand:
Grundstruktur und drei Analystenflows aufgebaut; vollständige End-to-End-Abnahme steht aus.

Nächster Meilenstein:
Flow 1 bis Flow 3 konsolidieren und mit definiertem Testpaket abnehmen.

Danach:
Bücher- und Studienpipeline, Wissensnotizen, Indexpflege, RAG und tägliche Briefings.
```
