import urllib.request
import xml.etree.ElementTree as ET
import os

url = "https://www.youtube.com/feeds/videos.xml?playlist_id=PL1ap5oFZycBOqlpUODvamqrjLhd9hrJTh"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

print("Fetching RSS feed...")
try:
    xml_data = urllib.request.urlopen(req).read()
    root = ET.fromstring(xml_data)
    
    # XML namespaces
    ns = {'yt': 'http://www.youtube.com/xml/schemas/2015',
          'media': 'http://search.yahoo.com/mrss/',
          'atom': 'http://www.w3.org/2005/Atom'}
    
    videos = []
    
    for entry in root.findall('atom:entry', ns):
        video_id = entry.find('yt:videoId', ns).text
        title = entry.find('atom:title', ns).text
        videos.append({'videoId': video_id, 'title': title})
        
    print(f"Found {len(videos)} videos.")
    
    # Order: The RSS feed usually has the newest at the top or bottom depending on playlist setting.
    # The user wants descending order of date (newest first). Let's assume the feed order is correct, or just reverse it if it's oldest first.
    # Actually, RSS feeds are typically newest first. But we'll leave it as is or reverse if needed. 
    # Let's reverse it to match YouTube's typical "add to bottom" behavior if it's in order of addition.
    videos.reverse()
    
    html_template = """<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>मीटिंग लाइब्रेरी (Meeting Library)</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        body {
            background-color: #f8fafc;
            background-image: linear-gradient(rgba(255, 255, 255, 0.65), rgba(255, 255, 255, 0.85)), url('bg.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            font-family: 'Outfit', sans-serif;
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.5);
            transition: all 0.3s ease;
        }
        .glass-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
            border-color: rgba(14, 165, 233, 0.3);
        }
        .gradient-text {
            background: linear-gradient(135deg, #0ea5e9, #8b5cf6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .thumbnail-container {
            position: relative;
            overflow: hidden;
            border-radius: 12px 12px 0 0;
            aspect-ratio: 16 / 9;
        }
        .thumbnail-container img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }
        .glass-card:hover .thumbnail-container img {
            transform: scale(1.05);
        }
        .play-overlay {
            position: absolute;
            inset: 0;
            background: rgba(0, 0, 0, 0.3);
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transition: opacity 0.3s ease;
        }
        .glass-card:hover .play-overlay {
            opacity: 1;
        }
    </style>
</head>
<body class="text-gray-800 antialiased min-h-screen py-12 px-4 sm:px-6">

    <div class="max-w-6xl mx-auto space-y-12">
        
        <!-- Header -->
        <div class="text-center space-y-4 mb-12 relative">
            <div class="absolute left-0 top-0">
                <a href="index.html" class="inline-flex items-center text-blue-600 hover:text-blue-800 font-medium transition-colors bg-white/70 px-4 py-2 rounded-lg shadow-sm border border-white">
                    &larr; डैशबोर्ड पर वापस
                </a>
            </div>
            
            <h1 class="text-4xl md:text-5xl font-extrabold tracking-tight text-gray-900 gradient-text pt-10 md:pt-0">
                मीटिंग लाइब्रेरी
            </h1>
            <p class="text-lg md:text-xl text-gray-700 font-medium max-w-2xl mx-auto">
                पुरोहित प्रशिक्षण मिशन की पिछली सभी महत्वपूर्ण बैठकों की वीडियो लाइब्रेरी।
            </p>
        </div>

        <!-- Video Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {video_cards}
        </div>

    </div>
</body>
</html>
"""

    card_template = """
            <a href="https://www.youtube.com/watch?v={video_id}" target="_blank" rel="noopener noreferrer" class="glass-card rounded-2xl flex flex-col h-full cursor-pointer group block">
                <div class="thumbnail-container">
                    <img src="https://img.youtube.com/vi/{video_id}/mqdefault.jpg" alt="Video Thumbnail">
                    <div class="play-overlay">
                        <svg class="w-16 h-16 text-white drop-shadow-lg" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M8 5v14l11-7z" />
                        </svg>
                    </div>
                </div>
                <div class="p-6 flex-grow flex flex-col justify-center">
                    <h2 class="text-lg font-bold text-gray-900 line-clamp-2 leading-tight group-hover:text-blue-600 transition-colors">
                        {title}
                    </h2>
                </div>
            </a>
"""

    video_cards = ""
    for v in videos:
        # Avoid breaking HTML if title has quotes
        safe_title = v['title'].replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
        video_cards += card_template.format(video_id=v['videoId'], title=safe_title)
        
    final_html = html_template.replace("{video_cards}", video_cards)
    
    with open(r"c:\klasa\sanskarak\meeting_library.html", "w", encoding="utf-8") as f:
        f.write(final_html)
        
    print("meeting_library.html generated successfully!")

except Exception as e:
    print("Error generating library:", e)
