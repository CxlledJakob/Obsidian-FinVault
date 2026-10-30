#!/usr/bin/env bash
# Importiert alle Workflows aus ../workflows in das laufende n8n.
# Achtung: Workflows mit gleicher ID werden überschrieben – vorher eigene Änderungen exportieren!
set -euo pipefail
CONTAINER="${N8N_CONTAINER:-n8n-finvault}"
docker exec "$CONTAINER" n8n import:workflow --separate --input=/home/node/workflows/
echo "Fertig. Credentials in n8n ggf. neu zuordnen (rote Nodes)."
