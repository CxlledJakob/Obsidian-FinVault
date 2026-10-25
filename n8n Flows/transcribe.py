import json
import sys
from faster_whisper import WhisperModel

audio_path, model_name, language = sys.argv[1], sys.argv[2], sys.argv[3] or None
model = WhisperModel(model_name, device="cpu", compute_type="int8")
segments, info = model.transcribe(audio_path, language=language, vad_filter=True)
rows = []
for segment in segments:
    text = segment.text.strip()
    if text:
        rows.append({"start": segment.start, "end": segment.end, "text": text})
full_text = " ".join(row["text"] for row in rows)
print(json.dumps({"language": info.language, "language_probability": info.language_probability, "segments": rows, "transcript": full_text}, ensure_ascii=False))
