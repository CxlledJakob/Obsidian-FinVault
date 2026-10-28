#!/bin/sh
# Hängt eine Quellenzeile an ## Quellen und Fundstellen.
# Aufruf: append_source_link.sh <notes-root> <begriff> <zeile>
set -eu
NOTES_ROOT=$1
BEGRIFF=$2
LINE=$3
TARGET=$(find "$NOTES_ROOT" -type f -name "$BEGRIFF.md" | head -n 1)
if [ -z "$TARGET" ]; then
  printf 'missing %s\n' "$BEGRIFF"
  exit 0
fi
if grep -F "$LINE" "$TARGET" >/dev/null 2>&1; then
  printf 'exists %s\n' "$TARGET"
  exit 0
fi
awk -v line="$LINE" '
  BEGIN { found = 0; done = 0 }
  {
    if (done) { print; next }
    if ($0 == "## Quellen und Fundstellen") { found = 1; print; next }
    if (found && $0 ~ /^## /) { print "- " line; print ""; done = 1 }
    print
  }
  END {
    if (found && !done) print "- " line
    if (!found) exit 2
  }
' "$TARGET" > "$TARGET.tmp"
mv "$TARGET.tmp" "$TARGET"
printf 'appended %s\n' "$TARGET"
