# Python script to generate clean, AI-summarized notes per participant in Hindi.
import json

output_file = r"c:\klasa\sanskarak\participant_notes.html"

# Intelligent summaries of the main content for each speaker in Hindi, stripping out noise/introductions.
summaries = {
    "Janardan Patel": "मानव सहयोग (Collaboration) और नेतृत्व को सामुदायिक विकास की कुंजी बताया। उन्होंने स्थापित सांस्कृतिक और धार्मिक मंचों (जैसे मठों और मंदिरों) का उपयोग करके शैक्षणिक और स्वास्थ्य संस्थान बनाने का सुझाव दिया (नारायण गुरु और ज्योतिबा फुले का उदाहरण देते हुए)। उन्होंने कहा कि पुरानी व्यवस्थाओं का नकारात्मक विरोध करने के बजाय 'सांस्कृतिक गतिशीलता' का सकारात्मक उपयोग करके समाज का विकास करना चाहिए।",
    
    "Pradeip Patel": "समाज को तीन स्तरों में बांटा: वर्कफोर्स (श्रम बल), मैनेजर और थिंकर्स (विचारक)। उन्होंने समाज को केवल वर्कफोर्स से ऊपर उठकर 'थिंकर्स' बनने पर जोर दिया। युवाल नोआ हरारी (Yuval Noah Harari) का हवाला देते हुए समझाया कि कैसे साझा कल्पनाएं और नैरेटिव यथार्थ में बदलते हैं। उन्होंने जनार्दन जी की 'सांस्कृतिक गतिशीलता' का उपयोग करने वाली बात का पुरजोर समर्थन किया।",
    
    "Paras Gangwar": "आर्टिफिशियल इंटेलिजेंस (AI) और उसके व्यावहारिक उपयोग पर एक विस्तृत प्रस्तुति दी। समझाया कि ChatGPT और NotebookLM जैसे टूल्स का उपयोग पढ़ाई, इमेज जनरेशन, कोडिंग और इंटरव्यू की तैयारी के लिए कैसे किया जा सकता है। उन्होंने बेहतर परिणाम पाने के लिए 'प्रॉम्प्ट इंजीनियरिंग' (Prompt Engineering) के टिप्स भी दिए।",
    
    "आचार्य Vinod प्रबुद्ध BC": "उन्होंने सवाल उठाया कि क्या पारंपरिक धार्मिक संस्थान (जैसे मठ और शंकराचार्य पद) पूरी तरह से वर्ण व्यवस्था से बंधे हुए हैं। उन्होंने पूछा कि पिछड़े समुदाय इन स्थानों पर कैसे नेतृत्व हासिल कर सकते हैं, और उन्होंने इस्कॉन (ISKCON) जैसे बड़े स्वतंत्र संस्थान खुद क्यों नहीं बनाए।",
    
    "UPENDRA Singh": "वर्ण व्यवस्था संबंधी चिंताओं का उत्तर देते हुए कर्नाटक का एक सफल उदाहरण दिया। उन्होंने बताया कि वहां वोक्कालिगा (कृषि समुदाय) द्वारा संचालित एक प्रमुख मठ स्वतंत्र रूप से सैकड़ों शैक्षणिक संस्थान और स्वास्थ्य ट्रस्ट चलाता है, जो यह साबित करता है कि धार्मिक मंच ब्राह्मणवादी संरचनाओं के बाहर भी सफलतापूर्वक काम कर सकते हैं।",
    
    "Aman Patel": "भोपाल और इंदौर में स्थित अपने बिजनेस 'अरिष्ट ऑटोमेशन' का परिचय दिया। ऑटोमैटिक गेट्स, रिमोट सिस्टम और पुराने मैनुअल सिस्टम को ऑटोमेटिक बनाने की सेवाओं पर चर्चा की। इसके साथ ही, युवाओं के लिए टेक सेक्टर में ट्रेनिंग और रोजगार के अवसर उपलब्ध कराने का प्रस्ताव रखा।",
    
    "Shivendra kumar Patel": "अमेज़ॅन प्राइम या हॉटस्टार जैसा एक स्वतंत्र ओटीटी (OTT) प्लेटफॉर्म विकसित करने के अपने प्रोजेक्ट की जानकारी साझा की। उन्होंने बताया कि वे पिछले 6 महीनों से सीरीज़ और वर्टिकल ड्रामा बना रहे हैं, और सदस्यों से अपना ऐप डाउनलोड कर समर्थन करने का अनुरोध किया।",
    
    "Sandeep Patel": "वे एक पूर्व सैनिक हैं जो रीवा में सेना और पुलिस भर्ती के लिए फिजिकल ट्रेनिंग अकादमी चलाते हैं। उन्होंने 60 से अधिक युवाओं को नशे से दूर रखकर सेना के लिए तैयार करने की बात कही और सामुदायिक जागरूकता के लिए मैराथन जैसे खेल आयोजन करने का सुझाव दिया।",
    
    "Ashok Kumar Patel": "बैठक के संचालक की भूमिका निभाई। वक्ताओं के बीच तालमेल बिठाया, नए सदस्यों का स्वागत किया, और मिशन के नेटवर्क को मजबूत करने के लिए नियमित रूप से बैठकों में शामिल होने के महत्व पर जोर दिया।",
    
    "ramroop patel": "मिशन के साथ अपने सकारात्मक अनुभव साझा किए और 'अनेकता में एकता' की अवधारणा पर जोर दिया। उन्होंने इस बात की सराहना की कि यह प्लेटफॉर्म कृषि, विज्ञान, चिकित्सा और सेना जैसे विभिन्न क्षेत्रों के पेशेवरों को एक साथ लाता है और बिना किसी कट्टरता के समाज का मार्गदर्शन करता है।"
}

# Generate HTML with Tailwind CSS
html_head = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>कार्यकारी सारांश: प्रतिभागी विचार (Executive Summary)</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Outfit', 'sans-serif'],
                    },
                    colors: {
                        primary: {
                            50: '#f0f9ff',
                            100: '#e0f2fe',
                            500: '#0ea5e9',
                            600: '#0284c7',
                            900: '#0c4a6e',
                        }
                    }
                }
            }
        }
    </script>
    <style>
        body { background-color: #f8fafc; }
        .glass-header {
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border-bottom: 1px solid rgba(226, 232, 240, 0.8);
        }
        .note-card {
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
            transition: all 0.25s ease-in-out;
            position: relative;
        }
        .note-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 20px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
        }
        .quote-icon {
            position: absolute;
            top: 1.5rem;
            right: 1.5rem;
            opacity: 0.05;
            font-size: 4rem;
            line-height: 1;
            font-family: serif;
            pointer-events: none;
        }
    </style>
</head>
<body class="text-gray-800 antialiased font-sans">
    
    <!-- Header -->
    <header class="glass-header sticky top-0 z-50">
        <div class="max-w-4xl mx-auto px-6 py-5 flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
                <h1 class="text-3xl font-bold text-gray-900 tracking-tight">कार्यकारी सारांश (Executive Summary)</h1>
                <p class="text-base text-gray-500 font-medium mt-1">प्रत्येक प्रतिभागी द्वारा दिए गए मुख्य विचार</p>
            </div>
            <div class="bg-primary-50 text-primary-600 px-4 py-2 rounded-full font-semibold text-sm border border-primary-100">
                Filtered & Summarized
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-4xl mx-auto px-4 sm:px-6 py-10">
        <div class="flex flex-col space-y-6">
"""

html_tail = """
        </div>
    </main>
    
    <!-- Footer -->
    <footer class="mt-12 py-8 text-center text-gray-400 text-sm border-t border-gray-200">
        AI-Summarized Meeting Insights
    </footer>
</body>
</html>
"""

html_content = [html_head]

for speaker, summary in summaries.items():
    html_content.append(f'''
            <div class="note-card bg-white rounded-2xl overflow-hidden border border-gray-100">
                <div class="quote-icon text-primary-500">"</div>
                
                <div class="p-6 md:p-8">
                    <div class="flex items-center gap-4 mb-4">
                        <div class="w-12 h-12 rounded-full bg-gradient-to-br from-primary-100 to-primary-500 flex items-center justify-center text-white font-bold text-xl shadow-inner shrink-0">
                            {speaker[0].upper()}
                        </div>
                        <div>
                            <h2 class="text-xl font-bold text-gray-900">{speaker}</h2>
                            <p class="text-xs font-semibold text-primary-600 uppercase tracking-wider">मुख्य बिंदु (Key Takeaways)</p>
                        </div>
                    </div>
                    
                    <div class="text-gray-700 text-lg leading-relaxed bg-gray-50/50 p-5 rounded-xl border border-gray-50">
                        {summary}
                    </div>
                </div>
            </div>
    ''')

html_content.append(html_tail)

with open(output_file, "w", encoding="utf-8") as f:
    f.write("".join(html_content))

print(f"Generated {output_file} successfully in Hindi.")
