import os

html_file = r"c:\klasa\sanskarak\meeting_insights.html"

new_content = """                
                <h3>जनार्दन पटेल (Janardan Patel) — बैठक संचालन एवं मठ इतिहास</h3>
                <ul>
                    <li><strong>भूमिका:</strong> मुख्य संचालक (Host/Facilitator) के रूप में बैठक का मार्गदर्शन।</li>
                    <li><strong>प्रमुख बिंदु:</strong> उन्होंने समुदाय के पद्म विभूषण सम्मान प्राप्तकर्ताओं और मठ की ऐतिहासिक पृष्ठभूमि पर प्रकाश डाला।</li>
                    <li><strong>दृष्टिकोण:</strong> धार्मिक संस्थानों में कृषि समुदाय की भागीदारी (जैसे इस्कॉन मंदिर का उदाहरण) पर चर्चा की और समाज को संगठित होकर संस्थाएं बनाने के लिए प्रेरित किया।</li>
                </ul>

                <h3>पारस गंगवार (Paras Gangwar) — कृत्रिम बुद्धिमत्ता (AI) प्रस्तुतीकरण</h3>
                <ul>
                    <li><strong>परिचय:</strong> एआई (Artificial Intelligence) क्या है और इसे दैनिक जीवन में कैसे उपयोगी बनाया जा सकता है, इस पर एक विस्तृत प्रस्तुति दी।</li>
                    <li><strong>उपयोग:</strong> बताया कि कैसे AI का उपयोग पढ़ाई, रिसर्च, इमेज जेनरेशन, कोडिंग, और इंटरव्यू की तैयारी के लिए किया जा सकता है।</li>
                    <li><strong>व्यावहारिक लाभ:</strong> उदाहरण दिया कि जिस PPT को मैन्युअल रूप से बनाने में घंटों लगते हैं, उसे AI की मदद से मात्र 5 मिनट में तैयार किया जा सकता है।</li>
                </ul>

                <h3>पूरन सिंह (Pooran Singh) — समापन टिप्पणी (Concluding Note)</h3>
                <ul>
                    <li><strong>सारांश:</strong> बैठक के अंत में सभी चर्चाओं का एक सकारात्मक और सारगर्भित निष्कर्ष प्रस्तुत किया।</li>
                    <li><strong>आह्वान:</strong> समुदाय को आधुनिक तकनीकों (जैसे AI और ऑटोमेशन) को अपनाने के साथ-साथ अपनी सांस्कृतिक जड़ों (पुरोहित प्रशिक्षण) से जुड़े रहने के लिए प्रेरित किया।</li>
                    <li><strong>एकता का संदेश:</strong> मिशन को मजबूत करने के लिए नियमित बैठकों में उपस्थिति और आपसी सहयोग पर बल दिया।</li>
"""

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# We want to replace the current Key Discussion points or add to them.
# The user said "update this page with notes from three main speakers"
# The current ones are Aman Patel and Shivendra Kumar Patel. We can replace them or keep them.
# I will replace the existing <ul> and <h3> blocks under <h2>💡 मुख्य चर्चा बिंदु (Key Discussion Points)</h2> with the new speakers.

start_marker = "<h2>💡 मुख्य चर्चा बिंदु (Key Discussion Points)</h2>"
end_marker = "            </div>\n\n            <!-- Decisions & Next Steps -->"

start_idx = html.find(start_marker)
end_idx = html.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    before = html[:start_idx + len(start_marker)]
    after = html[end_idx:]
    new_html = before + "\n" + new_content + "\n" + after
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Updated Insights HTML successfully!")
else:
    print("Markers not found")
