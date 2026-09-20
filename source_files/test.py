import re

with open('youtube_playlist.html', 'r', encoding='utf-8') as f:
    html = f.read()

# YouTube often minifies JSON. We can extract it by finding all videoIds and titles nearby.
# Using a less strict regex that ignores exact JSON structure
matches = re.findall(r'"videoId":"([a-zA-Z0-9_-]{11})".*?"title":\{"runs":\[\{"text":"([^"]+)"', html)

# Some might be duplicates or navigation endpoints. We'll filter unique videos
videos = []
seen = set()
for vid, title in matches:
    if vid not in seen and title != "Unknown Title":
        videos.append({'videoId': vid, 'title': title})
        seen.add(vid)

print(f"Found {len(videos)} videos")
for v in videos[:5]:
    print(v)
