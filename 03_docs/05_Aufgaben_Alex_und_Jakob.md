# Aufgaben Alex und Jakob

Stand: 4. November 2026

Alex macht die Flows. Jakob macht das Brain und die App. Die JSON-Datei ist die Übergabe: Alex schreibt sie, Jakob zeichnet sie auf den Chart.

## Schon erledigt

- Der Flow auf `main` liest Patreon-Mails, schreibt das Markdown und speichert die Bilder.
- Bei Jakob läuft n8n lokal. Container `n8n-finvault`, Port 5678. Die drei Workflows sind importiert.

## Zugangsdaten bei Jakob

Einmalig, damit der bestehende Flow auf Jakobs Rechner läuft. Alex hat das auf seinem Rechner schon.

1. `http://localhost:5678` öffnen und den Owner-Account anlegen.
2. Credential anlegen, Name genau **Gmail FinVault**, Typ Gmail OAuth2. Dafür in Google Cloud die Gmail-API und einen OAuth-Client. Die Weiterleitungs-URL zeigt n8n an: `http://localhost:5678/rest/oauth2-credential/callback`.
3. Credential anlegen, Name genau **Anthropic FinVault**, Typ Anthropic, mit dem API-Key.
4. Im Flow **FinVault – Patreon → Vault v0.9** die vier Gmail-Knoten auf **Gmail FinVault** setzen.
5. Den Claude-Knoten auf **Anthropic FinVault** setzen.
6. Beim Knoten für Flow B den Workflow **FinVault – Status fortschreiben v0.1** auswählen.
7. In Gmail die Labels `FinVault/Eingang`, `FinVault/Verarbeitet` und `FinVault/Fehler` anlegen, falls sie fehlen.
8. Den Flow auf Active stellen. Eine Mail nach `FinVault/Eingang` legen und den Flow einmal von Hand starten.

## Festgelegt, damit beide weiterarbeiten

- Eine JSON-Datei pro Chartbild, neben dem Update: `Research/Analysten/The Long Investor/Technisch/<TICKER>/Updates/<Datum> - <TICKER> - Chart <n>.json`
- Alex holt die Tageskerzen für den Abgleich selbst, zum Beispiel bei Yahoo. Jakob hängt die App später an dieselbe Quelle.
- Auswahlname in der App: Analyst, Ticker, Datum, Timeframe. Beispiel: The Long Investor, UBER, 2026-11-04, 1W.

Felder, die Alex schreibt und Jakob liest:

- `ticker`, `timeframe`, `analyst`, `published_at`
- Punkt: `label`, `price`, `attach` (`pivot`, `level`, `target`), `when.status` (`hint`, `snapped`, `open`), `when.bar_time`
- Zeichnung: `hline`, `zone`, `fib`, `trendline`, `indicator`
- `indicator` nur als Name, Periode und Timeframe. Die Kurve zeichnet die App.

## Alex

1. Im Flow v0.9, direkt nach dem Bild-Download, jedes Bild an Claude geben.
2. Claude schreibt nur ab, was auf dem Chart steht: Timeframe, Wellenzeichen mit Farbe, ob es auf einem Hoch oder Tief sitzt, zwischen welchen zwei Datumsbeschriftungen, und ob es rechts der letzten Kerze im leeren Bereich steht. Dazu die Preise an Fib-Linien, Buy Zone und Invalidation Line.
3. Ist das Bild kein Chart, keine JSON schreiben.
4. Tageskerzen des Tickers holen.
5. Pro Wellenzeichen nur ein kurzes Fenster um die abgelesene Stelle durchsuchen. Hochzeichen: höchstes Hoch. Tiefzeichen: tiefstes Tief. Diese Kerze ist der Punkt, `when.status` ist `snapped`.
6. Zeichen im leeren Bereich rechts bleiben ein Preisziel ohne Datum, `when.status` ist `open`.
7. Preise aus dem Beitragstext nicht überschreiben.
8. Sitzt ein Hoch auf einer geraden Welle oder ein Tief auf einer ungeraden, den Punkt behalten und eine Warnung setzen.
9. Die JSON-Datei ablegen. Markdown und Bilder bleiben wie sie sind.
10. Am Flow arbeitet nur Alex, solange dieser Schritt entsteht.

## Jakob

1. Die Zugangsdaten oben fertig machen und einen Mail-Lauf prüfen.
2. In der App die Auswahlliste bauen: ein Eintrag pro JSON-Datei.
3. Die Zeichnung auf den eigenen Chart legen. Linien und Zonen normal. Wellenpunkte nur bei `snapped`. `hint` gestrichelt. Ziele als Linie nach rechts, ohne Enddatum.
4. 50er und 200er aus den eigenen Kursdaten rechnen.
5. In FinVault nur drei Seiten zeigen: Dashboard, Watchlist, Charts. Darüber der Schalter zur Research-Plattform.
6. Zum Bauen die UBER-JSON aus dem Chat nehmen. Nicht auf den laufenden Flow warten.
7. Am Brain weiter die Bücher und die Notizstruktur. Strategien erst, wenn die Abfrage durch die Notizen steht.
