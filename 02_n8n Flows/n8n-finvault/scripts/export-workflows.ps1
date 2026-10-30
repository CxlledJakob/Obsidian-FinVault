# Windows-Variante von export-workflows.sh
$Container = if ($env:N8N_CONTAINER) { $env:N8N_CONTAINER } else { "n8n-finvault" }
docker exec $Container sh -c "rm -rf /tmp/wf-raw && mkdir -p /tmp/wf-raw && n8n export:workflow --all --separate --pretty --output=/tmp/wf-raw/ >/dev/null && node /home/node/scripts/normalize-workflows.js /tmp/wf-raw /home/node/workflows"
