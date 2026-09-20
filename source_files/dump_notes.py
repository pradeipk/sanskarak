import re
from collections import defaultdict

input_file = r"c:\klasa\sanskarak\Meeting Transcription.txt"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

transcript_started = False
participant_notes = defaultdict(list)

pattern = re.compile(r"^\s*(\d{2}:\d{2})\s+([^:]+?)\s*:\s*(.*)")
current_speaker = None
current_message = []

def save_message():
    global current_speaker, current_message
    if current_speaker:
        text = " ".join(current_message).strip()
        if text:
            participant_notes[current_speaker].append(text)

for line in lines:
    line = line.strip()
    if line == "## Transcript":
        transcript_started = True
        continue
    
    if transcript_started:
        if line.startswith("Participants :"):
            break
        if not line or line.startswith("![Screenshot]"):
            continue
            
        match = pattern.match(line)
        if match:
            save_message()
            current_speaker = match.group(2)
            current_message = [match.group(3)]
        else:
            if current_speaker:
                current_message.append(line)

save_message()

sorted_participants = sorted(participant_notes.items(), key=lambda x: sum(len(msg) for msg in x[1]), reverse=True)

with open(r"c:\klasa\sanskarak\raw_dump.txt", "w", encoding="utf-8") as f:
    for speaker, messages in sorted_participants:
        text = " ".join(messages)
        text = re.sub(r'\s+', ' ', text)
        if len(text.split()) > 5:
            f.write(f"SPEAKER: {speaker}\n")
            f.write(f"TEXT: {text}\n")
            f.write("-" * 50 + "\n")
