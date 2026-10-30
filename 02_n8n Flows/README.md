# n8n – lokale Entwicklungsumgebung & Flow-Austausch

Jeder von uns betreibt n8n lokal. **Die Flows selbst liegen als JSON in `workflows/`** – darüber sehen wir gegenseitig, was gebaut wurde, und können es importieren.

```text
02_n8n Flows/
├── compose.mac.yml          lokales n8n (Mac, läuft auch unter Windows)
├── workflows/               exportierte Flows – das ist der geteilte Stand
├── scripts/
│   ├── export-workflows.sh  n8n → workflows/   (vor jedem Commit)
│   ├── import-workflows.sh  workflows/ → n8n   (nach jedem Pull)
│   ├── *.ps1                dasselbe für Windows
│   └── normalize-workflows.js
├── compose.yml, Dockerfile, media-helper.js, transcribe.py   (Kubas Media-Setup, unverändert)
└── README.md
```

## Einmalig einrichten

1. **Docker Desktop** installieren (Mac: Apple-Silicon-Version).
2. KI läuft über die **Claude API** (Haiku). API-Key in n8n als Credential anlegen, nie in Dateien.
3. n8n starten – im Ordner `02_n8n Flows`:
   ```bash
   docker compose -f compose.mac.yml up -d
   ```
4. http://localhost:5678 öffnen und Owner-Account anlegen.
5. In n8n Credentials anlegen (z. B. Gmail OAuth2). **Credentials werden nie exportiert** – jeder legt sie bei sich selbst an. Gleiche Namen verwenden, dann ist das Zuordnen nach einem Import schnell erledigt.

Pfade im Container (identisch zum Architekturkonzept, auf jedem Rechner gleich):

| Zweck | Pfad im Container |
|---|---|
| Vault Trading | `/vault/Finanzen/Trading` |

## Arbeitsablauf

**Nach dem Bauen/Ändern eines Flows:**
```bash
./scripts/export-workflows.sh
git add "02_n8n Flows/workflows" && git commit -m "Flow 1: …" && git push
```

**Nach einem Pull (Änderungen vom anderen holen):**
```bash
./scripts/import-workflows.sh
```

### Spielregeln
- Vor dem Import immer erst die eigenen Änderungen exportieren – der Import überschreibt Flows mit gleicher ID.
- Pro Flow arbeitet immer nur einer gleichzeitig (kurz absprechen), sonst gibt es Merge-Konflikte im JSON.
- Der Export entfernt automatisch Testdaten (`pinData`) und Trigger-Zustand (`staticData`), damit keine Patreon-Inhalte oder flüchtigen Werte ins Git kommen.
- Flow-Namen tragen eine Version, z. B. `Flow1 Patreon Ingestion v0.1.0`.

## Claude per MCP mit dem lokalen n8n verbinden

1. In n8n: **Settings → Instance-level MCP → Enable MCP access**.
2. **Connection details → Connect → Tab „API key“** → Token kopieren (wird nur einmal vollständig angezeigt, nicht ins Git und nicht in Chats posten).
3. Jeden Flow, den Claude sehen/bearbeiten soll, freigeben: Workflow → Settings → **Available in MCP**.
4. Claude Desktop: `~/Library/Application Support/Claude/claude_desktop_config.json` (Windows: `%APPDATA%\Claude\claude_desktop_config.json`) ergänzen:
   ```json
   {
     "mcpServers": {
       "n8n": {
         "command": "npx",
         "args": ["-y", "mcp-remote", "http://localhost:5678/mcp-server/http",
                  "--header", "Authorization:${N8N_AUTH}"],
         "env": { "N8N_AUTH": "Bearer <DEIN_TOKEN>" }
       }
     }
   }
   ```
   Voraussetzung: Node.js ist installiert (`npx`).
5. Claude Desktop komplett beenden und neu starten.
