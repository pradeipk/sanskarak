import re
from collections import defaultdict

input_file = r"c:\klasa\sanskarak\Meeting Transcription.txt"
output_file = r"c:\klasa\sanskarak\participant_notes.html"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

transcript_started = False
participant_notes = defaultdict(list)

pattern = re.compile(r"^\s*(\d{2}:\d{2})\s+([^:]+?)\s*:\s*(.*)")
current_speaker = None
current_time = None
current_message = []

def save_message():
    global current_speaker, current_time, current_message
    if current_speaker:
        text = " ".join(current_message).strip()
        if text:
            participant_notes[current_speaker].append({
                "time": current_time,
                "message": text
            })

for line in lines:
    line = line.strip()
    if line == "## Transcript":
        transcript_started = True
        continue
    
    if transcript_started:
        if line.startswith("Participants :"):
            break
        
        if not line:
            continue
            
        if line.startswith("![Screenshot]"):
            img_url = re.search(r"\((.*?)\)", line)
            if img_url:
                current_message.append(f'<img src="{img_url.group(1)}" alt="Screenshot" class="w-full h-auto mt-4 rounded-lg shadow-sm border border-gray-200">')
            continue
            
        match = pattern.match(line)
        if match:
            save_message()
            current_time = match.group(1)
            current_speaker = match.group(2)
            current_message = [match.group(3)]
        else:
            if current_speaker:
                current_message.append(line)

save_message()

sorted_participants = sorted(participant_notes.items(), key=lambda x: len(x[1]), reverse=True)

# Generate HTML with Tailwind CSS
html_head = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Participant Notes</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    },
                    colors: {
                        brand: {
                            50: '#ecfdf5',
                            100: '#d1fae5',
                            500: '#10b981',
                            600: '#059669',
                            900: '#064e3b',
                        }
                    }
                }
            }
        }
    </script>
    <style>
        body { background-color: #f8fafc; }
        .glass-header {
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(226, 232, 240, 0.8);
        }
        .participant-card {
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
            transition: all 0.25s ease-in-out;
        }
        .participant-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
        }
        .message-list-item:last-child {
            border-bottom: none;
            padding-bottom: 0;
            margin-bottom: 0;
        }
    </style>
</head>
<body class="text-gray-800 antialiased font-sans">
    
    <!-- Header -->
    <header class="glass-header sticky top-0 z-50">
        <div class="max-w-5xl mx-auto px-6 py-5 flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
                <h1 class="text-2xl font-bold text-gray-900 tracking-tight">Collated Participant Notes</h1>
                <p class="text-sm text-gray-500 font-medium mt-1">Organized by Speaker (Most active first)</p>
            </div>
            <div class="bg-brand-50 text-brand-600 px-4 py-2 rounded-full font-semibold text-sm inline-block text-center border border-brand-100 shadow-sm">
                29 Total Participants
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-5xl mx-auto px-4 sm:px-6 py-10">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
"""

html_tail = """
        </div>
    </main>
    
    <!-- Footer -->
    <footer class="mt-12 py-8 text-center text-gray-400 text-sm border-t border-gray-200">
        Generated automatically from Meeting Transcription
    </footer>
</body>
</html>
"""

html_content = [html_head]

for i, (speaker, messages) in enumerate(sorted_participants):
    # Highlight top 3 speakers with a slight gradient border
    top_styles = ""
    if i < 3:
        top_styles = "ring-2 ring-brand-500 ring-offset-2 ring-offset-slate-50"
        
    html_content.append(f'''
            <div class="participant-card bg-white rounded-2xl overflow-hidden {top_styles} border border-gray-100 flex flex-col">
                <!-- Card Header -->
                <div class="bg-gradient-to-r from-gray-50 to-white px-6 py-5 border-b border-gray-100 flex items-center justify-between">
                    <h2 class="text-xl font-bold text-gray-800">{speaker}</h2>
                    <span class="bg-brand-100 text-brand-600 text-xs font-bold px-3 py-1 rounded-full">{len(messages)} notes</span>
                </div>
                
                <!-- Messages List -->
                <div class="p-6 flex-grow bg-white">
                    <ul class="flex flex-col space-y-4">
    ''')
    
    for msg in messages:
        html_content.append(f'''
                        <li class="message-list-item pb-4 border-b border-gray-50">
                            <div class="flex items-start gap-3">
                                <span class="bg-gray-100 text-gray-500 text-xs font-semibold px-2 py-1 rounded mt-0.5 whitespace-nowrap">{msg['time']}</span> 
                                <span class="text-gray-700 text-sm md:text-base leading-relaxed">{msg['message']}</span>
                            </div>
                        </li>
        ''')
        
    html_content.append('''
                    </ul>
                </div>
            </div>
    ''')

html_content.append(html_tail)

with open(output_file, "w", encoding="utf-8") as f:
    f.write("".join(html_content))

print(f"Generated {output_file} successfully.")
