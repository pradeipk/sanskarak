import re

input_file = r"c:\klasa\sanskarak\Meeting Transcription.txt"
output_file = r"c:\klasa\sanskarak\meeting_transcript.html"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

transcript_started = False
transcript_lines = []

pattern = re.compile(r"^\s*(\d{2}:\d{2})\s+([^:]+?)\s*:\s*(.*)")
current_speaker = None
current_time = None
current_message = []

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
                current_message.append(f'<img src="{img_url.group(1)}" alt="Screenshot" class="w-full h-auto mt-4 rounded-xl shadow-lg border border-gray-200">')
            continue
            
        match = pattern.match(line)
        if match:
            if current_speaker:
                transcript_lines.append({
                    "time": current_time,
                    "speaker": current_speaker,
                    "message": " ".join(current_message)
                })
            current_time = match.group(1)
            current_speaker = match.group(2)
            current_message = [match.group(3)]
        else:
            if current_speaker:
                current_message.append(line)

if current_speaker:
    transcript_lines.append({
        "time": current_time,
        "speaker": current_speaker,
        "message": " ".join(current_message)
    })

# HTML Generation using Tailwind CSS via CDN for a highly polished, responsive look.
html_head = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meeting Transcript</title>
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
                            50: '#eff6ff',
                            100: '#dbeafe',
                            500: '#3b82f6',
                            600: '#2563eb',
                            900: '#1e3a8a',
                        }
                    }
                }
            }
        }
    </script>
    <style>
        body { background-color: #f3f4f6; }
        .glass-header {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-bottom: 1px solid rgba(255,255,255,0.3);
        }
        .chat-bubble {
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
            transition: all 0.3s ease;
        }
        .chat-bubble:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -2px rgba(0, 0, 0, 0.04);
        }
    </style>
</head>
<body class="text-gray-800 antialiased font-sans">
    
    <!-- Header -->
    <header class="glass-header sticky top-0 z-50 shadow-sm">
        <div class="max-w-4xl mx-auto px-6 py-5 flex items-center justify-between">
            <div>
                <h1 class="text-2xl font-bold text-gray-900 tracking-tight">Meeting Transcript</h1>
                <p class="text-sm text-gray-500 font-medium mt-1">Detailed conversation log</p>
            </div>
            <div class="bg-brand-100 text-brand-600 px-4 py-2 rounded-full font-semibold text-sm">
                September 20, 2026
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-4xl mx-auto px-4 sm:px-6 py-8">
        <div class="flex flex-col space-y-6">
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

# Generate alternating chat colors for visual distinction
colors = ["bg-white border-l-4 border-brand-500", "bg-gray-50 border-l-4 border-purple-500"]

for i, msg in enumerate(transcript_lines):
    color_class = colors[i % 2]
    
    html_content.append(f'''
            <!-- Message Item -->
            <div class="chat-bubble {color_class} rounded-r-2xl rounded-bl-2xl p-5 md:p-6 w-full">
                <div class="flex items-center justify-between mb-3">
                    <span class="font-semibold text-gray-900 text-base md:text-lg">{msg['speaker']}</span>
                    <span class="text-xs font-medium text-gray-500 bg-gray-100 px-3 py-1 rounded-full">{msg['time']}</span>
                </div>
                <div class="text-gray-700 leading-relaxed text-sm md:text-base whitespace-pre-wrap">{msg['message']}</div>
            </div>
    ''')

html_content.append(html_tail)

with open(output_file, "w", encoding="utf-8") as f:
    f.write("".join(html_content))

print(f"Generated {output_file} successfully.")
