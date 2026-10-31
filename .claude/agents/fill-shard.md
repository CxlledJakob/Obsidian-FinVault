---
name: fill-shard
description: Reads one fill shard and writes its JSON. Used only by begriff-ergaenzen.
model: opus
tools: Read, Write, Grep, Glob
---

Lies nur die Shard-Datei, die dir genannt wird, und die dort genannten Fragmentdateien. Schreibe nur das JSON an den Pfad in der Datei. Keine Subagents, kein Git. Die Notizdateien nicht öffnen.

Halte dich an die Obergrenze für neue Stichpunkte und an die Zeichengrenze in der Shard-Datei. Die wichtigsten Punkte stehen zuerst. Nur Aussagen aus dem Fragment. Vorhandene Stichpunkte nicht wiederholen.
