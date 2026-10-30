'use strict';
// Bereitet rohe n8n-Exporte fürs Git auf:
// - lesbare Dateinamen statt Workflow-IDs
// - entfernt pinData (könnte Patreon-Inhalte enthalten) und staticData (Trigger-Zustand)
// - entfernt flüchtige Felder, damit Git-Diffs nur echte Änderungen zeigen
// Aufruf: node normalize-workflows.js <raw-dir> <target-dir>

const fs = require('fs');
const path = require('path');

const [rawDir, targetDir] = process.argv.slice(2);
if (!rawDir || !targetDir) {
  console.error('Aufruf: node normalize-workflows.js <raw-dir> <target-dir>');
  process.exit(1);
}

const DROP_KEYS = [
  'pinData', 'staticData', 'createdAt', 'updatedAt', 'versionId', 'activeVersionId',
  'active', 'shared', 'triggerCount', 'isArchived', 'homeProject', 'parentFolder', 'scopes'
];

function slug(name) {
  return String(name || 'unbenannt')
    .normalize('NFKD').replace(/[\u0300-\u036f]/g, '')
    .replace(/ß/g, 'ss')
    .replace(/[^A-Za-z0-9._-]+/g, '_')
    .replace(/_+/g, '_')
    .replace(/^_|_$/g, '')
    .slice(0, 120) || 'unbenannt';
}

function sortKeys(value) {
  if (Array.isArray(value)) return value.map(sortKeys);
  if (value && typeof value === 'object') {
    return Object.keys(value).sort().reduce((acc, key) => { acc[key] = sortKeys(value[key]); return acc; }, {});
  }
  return value;
}

const rawFiles = fs.readdirSync(rawDir).filter(f => f.endsWith('.json'));
const workflows = rawFiles.map(f => JSON.parse(fs.readFileSync(path.join(rawDir, f), 'utf8')));

// Nur Workflows, die nicht archiviert sind
const live = workflows.filter(wf => !wf.isArchived);

const usedNames = new Set();
const written = [];
for (const wf of live) {
  for (const key of DROP_KEYS) delete wf[key];
  // Credential-Zuordnungen in den Nodes bleiben erhalten (nur Name + ID, keine Secrets)
  // Nodes stabil nach Name sortieren, damit die Reihenfolge nicht springt
  if (Array.isArray(wf.nodes)) wf.nodes.sort((a, b) => String(a.name).localeCompare(String(b.name)));

  let base = slug(wf.name);
  if (usedNames.has(base)) base = `${base}__${wf.id}`;
  usedNames.add(base);

  const file = `${base}.json`;
  const ordered = { id: wf.id, name: wf.name, ...sortKeys(wf) };
  fs.writeFileSync(path.join(targetDir, file), JSON.stringify(ordered, null, 2) + '\n', 'utf8');
  written.push(file);
}

// Exporte von Workflows entfernen, die es in n8n nicht mehr gibt
for (const f of fs.readdirSync(targetDir)) {
  if (f.endsWith('.json') && !written.includes(f)) {
    fs.unlinkSync(path.join(targetDir, f));
    console.log('entfernt (in n8n nicht mehr vorhanden):', f);
  }
}

console.log(`${written.length} Workflow(s) exportiert:`);
written.sort().forEach(f => console.log(' -', f));
