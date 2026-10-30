# Windows-Variante von import-workflows.sh
$Container = if ($env:N8N_CONTAINER) { $env:N8N_CONTAINER } else { "n8n-finvault" }
docker exec $Container n8n import:workflow --separate --input=/home/node/workflows/
