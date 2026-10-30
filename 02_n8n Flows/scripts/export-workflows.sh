#!/usr/bin/env bash
# Exportiert alle Workflows aus dem laufenden n8n nach ../workflows (fürs Git)
set -euo pipefail
CONTAINER="${N8N_CONTAINER:-n8n-finvault}"
docker exec "$CONTAINER" sh -c '
  rm -rf /tmp/wf-raw && mkdir -p /tmp/wf-raw &&
  n8n export:workflow --all --separate --pretty --output=/tmp/wf-raw/ >/dev/null &&
  node /home/node/scripts/normalize-workflows.js /tmp/wf-raw /home/node/workflows
'
echo "Fertig. Jetzt prüfen und committen:  git status  →  git add \"02_n8n Flows/workflows\"  →  git commit"
