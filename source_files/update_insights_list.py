import re

input_file = r"c:\klasa\sanskarak\source_files\parsed_participants.txt"
html_file = r"c:\klasa\sanskarak\meeting_insights.html"

with open(input_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

participants = []
# Regex to match "Number. Name - Location" or "Number. Name"
pattern = re.compile(r'^\d+\.\s+(.*?)(?:\s+-\s+(.*))?$')

for line in lines:
    line = line.strip()
    match = pattern.match(line)
    if match:
        name = match.group(1).strip()
        location = match.group(2).strip() if match.group(2) else ""
        
        # Clean up quotes if present
        if name.startswith('" '):
            name = name[2:]
            
        participants.append((name, location))

html_output = '<div class="participant-list">\n'
for name, location in participants:
    loc_html = f'<span class="perc" style="background: rgba(14, 165, 233, 0.1); color: #0ea5e9;">{location}</span>' if location else ''
    html_output += f'                <div class="participant-item"><span class="name">{name}</span> {loc_html}</div>\n'
html_output += '            </div>'

with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace the existing list
start_marker = '<div class="participant-list">'
end_marker = '            </div>\n        </section>'

start_idx = html_content.find(start_marker)
end_idx = html_content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_html = html_content[:start_idx] + html_output + '\n' + html_content[end_idx:]
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Successfully updated meeting_insights.html with the parsed list.")
else:
    print("Could not find the participant list section in the HTML.")
