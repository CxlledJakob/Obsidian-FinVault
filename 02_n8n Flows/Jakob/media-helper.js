'use strict';
const fs = require('fs');
const path = require('path');
const cp = require('child_process');

function input() {
  const encoded = process.argv[3];
  if (!encoded) throw new Error('Eingabedaten fehlen');
  return JSON.parse(Buffer.from(encoded, 'base64').toString('utf8'));
}
function output(value) { process.stdout.write(JSON.stringify(value)); }
function required(x, keys) {
  for (const key of keys) if (typeof x[key] !== 'string' || !x[key].trim()) throw new Error('Pflichtfeld fehlt: ' + key);
}
function mkdir(dir) { fs.mkdirSync(dir, { recursive: true }); }
function readJsonLines(file) {
  if (!fs.existsSync(file)) return [];
  return fs.readFileSync(file, 'utf8').split(/\r?\n/).filter(line => line.trim()).map((line, index) => {
    try { return { ...JSON.parse(line), queue_line: index + 1 }; }
    catch (error) { return { queue_line: index + 1, queue_error: 'invalid_json', parse_error: error.message }; }
  });
}
function run(program, args, options = {}) {
  const result = cp.spawnSync(program, args, { encoding: 'utf8', maxBuffer: 64 * 1024 * 1024, ...options });
  if (result.error || result.status !== 0) throw new Error(program + ' fehlgeschlagen: ' + String(result.stderr || result.error || 'unbekannt').slice(0, 2000));
  return result;
}
function atomicWrite(file, content) {
  mkdir(path.dirname(file));
  if (fs.existsSync(file)) throw new Error('Zieldatei existiert bereits: ' + file);
  const temp = file + '.tmp-' + process.pid;
  fs.writeFileSync(temp, content, 'utf8');
  fs.renameSync(temp, file);
}
function removeJobFiles(jobDir) {
  if (typeof jobDir === 'string' && jobDir.trim() && fs.existsSync(jobDir)) fs.rmSync(jobDir, { recursive: true, force: true });
}
const action = process.argv[2];
const x = input();
if (action === 'read-queue') {
  required(x, ['queue_file']);
  output({ ...x, queue_rows: readJsonLines(x.queue_file) });
} else if (action === 'prepare') {
  required(x, ['work_root','output_root','transcript_root','error_root','archive_root','log_file','job_key','source_url']);
  [x.work_root,x.output_root,x.transcript_root,x.error_root,x.archive_root,path.dirname(x.log_file)].forEach(mkdir);
  let duplicate = false;
  if (fs.existsSync(x.log_file)) duplicate = readJsonLines(x.log_file).some(row => row.source_url === x.source_url && row.status === 'created');
  const job_dir = path.join(x.work_root, x.job_key);
  mkdir(job_dir);
  output({ ...x, duplicate, job_dir });
} else if (action === 'download') {
  required(x, ['job_dir','source_url']);
  const template = path.join(x.job_dir, 'media.%(ext)s');
  run('yt-dlp', ['--no-playlist','--restrict-filenames','--write-info-json','--extract-audio','--audio-format','mp3','--output',template,x.source_url], { timeout: 600000 });
  const files = fs.readdirSync(x.job_dir);
  const audio = files.find(file => file.endsWith('.mp3'));
  const info = files.find(file => file.endsWith('.info.json'));
  if (!audio) throw new Error('Keine MP3-Datei erzeugt');
  let metadata = {};
  if (info) metadata = JSON.parse(fs.readFileSync(path.join(x.job_dir, info), 'utf8'));
  output({ ...x, audio_path:path.join(x.job_dir,audio), info_path:info ? path.join(x.job_dir,info) : '', media_metadata:{id:metadata.id||'',title:metadata.title||'',uploader:metadata.uploader||metadata.channel||'',upload_date:metadata.upload_date||'',duration:metadata.duration??null,webpage_url:metadata.webpage_url||x.source_url} });
} else if (action === 'transcribe') {
  required(x, ['audio_path','whisper_model']);
  const script = path.join(__dirname, 'transcribe.py');
  const result = run('python3', [script,x.audio_path,x.whisper_model,x.whisper_language||''], { timeout: 3600000 });
  const transcript = JSON.parse(result.stdout);
  if (!transcript.transcript || transcript.transcript.trim().length < 20) throw new Error('Transkript ist leer oder zu kurz');
  output({ ...x, ...transcript });
} else if (action === 'finalize') {
  required(x, ['output_path','markdown','transcript_path','transcript_markdown','log_file','source_url','platform']);
  atomicWrite(x.transcript_path, x.transcript_markdown);
  try { atomicWrite(x.output_path, x.markdown); }
  catch (error) { if (fs.existsSync(x.transcript_path)) fs.unlinkSync(x.transcript_path); throw error; }
  if (!fs.existsSync(x.output_path) || !fs.existsSync(x.transcript_path)) throw new Error('Abschlussprüfung der Ausgabedateien fehlgeschlagen');
  const record = {timestamp:new Date().toISOString(),source_url:x.source_url,platform:x.platform,output_file:x.output_path,transcript_file:x.transcript_path,status:'created'};
  mkdir(path.dirname(x.log_file));
  fs.appendFileSync(x.log_file, JSON.stringify(record) + '\n', 'utf8');
  removeJobFiles(x.job_dir);
  output(record);
} else if (action === 'error-report') {
  required(x, ['error_root']);
  mkdir(x.error_root);
  const safeKey = String(x.job_key || Date.now()).replace(/[^A-Za-z0-9_-]/g,'_').slice(0,80);
  const file = path.join(x.error_root, 'media-' + safeKey + '.json');
  const report = {timestamp:new Date().toISOString(),source_url:String(x.source_url||''),queue_line:x.queue_line??null,errors:Array.isArray(x.validation_errors)?x.validation_errors:['Verarbeitung fehlgeschlagen']};
  fs.writeFileSync(file, JSON.stringify(report,null,2), 'utf8');
  output({status:'error_report_created',file});
} else {
  throw new Error('Unbekannte Aktion: ' + action);
}
