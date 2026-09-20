import os

html_file = r"c:\klasa\sanskarak\meeting_insights.html"

new_content = """                
                <div class="mb-8">
                    <h3 class="text-xl font-bold text-gray-900 mb-2">जनार्दन पटेल (Janardan Patel) — नेतृत्व, सहयोग और संस्था निर्माण</h3>
                    <ul class="list-disc list-inside text-gray-700 space-y-2 ml-4">
                        <li><strong>मिशन के 200वें सत्र पर विचार:</strong> उन्होंने पुरोहित प्रशिक्षण मिशन की 200 बैठकों की निरंतरता को एक बड़ी उपलब्धि बताया और इस यात्रा में सहयोग के लिए सभी का धन्यवाद किया।</li>
                        <li><strong>मानव विकास और सहयोग (Collaboration):</strong> युवाल नोआ हरारी की पुस्तक 'सेपियंस' का संदर्भ देते हुए समझाया कि इंसानों की सबसे बड़ी शक्ति उनकी "सहयोग (Collaborate) करने की क्षमता" है। इसी खूबी का उपयोग करके यह मिशन मुंबई से लेकर रीवा और नागपुर तक के लोगों को जोड़ पा रहा है।</li>
                        <li><strong>धर्म का रचनात्मक उपयोग:</strong> उन्होंने स्पष्ट किया कि धर्म और अध्यात्म का उपयोग केवल पूजा-पाठ तक सीमित नहीं रहना चाहिए, बल्कि इसका उपयोग समाज की तीन मुख्य समस्याओं—शिक्षा, स्वास्थ्य और रोजगार—को सुलझाने के लिए एक साधन (Tool) के रूप में किया जाना चाहिए।</li>
                        <li><strong>नकारात्मक प्रचार के बजाय समानांतर संस्थाएं बनाना:</strong> नारायण गुरु जी का ऐतिहासिक उदाहरण दिया, जिन्होंने अपनी जाति को मंदिरों में प्रवेश न मिलने पर केवल विरोध करने के बजाय अपने खुद के मंदिर और संस्थाएं स्थापित कीं, जिससे केरल में उनके समुदाय का शैक्षिक और राजनीतिक उत्थान हुआ।</li>
                        <li><strong>प्रेरणा और भविष्य का विजन:</strong> कर्नाटक के वोक्कालिगा समुदाय (आदिचुनचुनागिरी मठ) का उदाहरण देते हुए बताया कि कैसे एक मठ आज 500 से अधिक शिक्षण संस्थान चला रहा है। उन्होंने पुरोहित मिशन को भी इसी तरह एक मजबूत ब्रांड और संस्था के रूप में विकसित करने का आह्वान किया।</li>
                    </ul>
                </div>

                <div class="mb-8">
                    <h3 class="text-xl font-bold text-gray-900 mb-2">पारस गंगवार (Paras Gangwar) — कृत्रिम बुद्धिमत्ता (AI) का व्यावहारिक उपयोग</h3>
                    <ul class="list-disc list-inside text-gray-700 space-y-2 ml-4">
                        <li><strong>AI का परिचय:</strong> उन्होंने समझाया कि AI (कृत्रिम बुद्धिमत्ता) कोई जटिल या डरावनी तकनीक नहीं है, बल्कि यह हमारे दैनिक जीवन को आसान बनाने वाला एक टूल है।</li>
                        <li><strong>शिक्षा और रिसर्च में AI:</strong> छात्रों के लिए 'NotebookLM' जैसे टूल्स का उदाहरण दिया, जहां कोई भी बुक या PDF अपलोड करके 10 सबसे महत्वपूर्ण प्रश्न और उनके उत्तर आसानी से प्राप्त किए जा सकते हैं।</li>
                        <li><strong>प्रॉम्प्ट इंजीनियरिंग (Prompt Engineering):</strong> AI से सही परिणाम पाने का तरीका बताया—जैसे कि अगर आपको रिज़्यूमे (Resume) बनवाना है, तो AI को अपनी पूरी जानकारी दें और उसे "एक HR की तरह" काम करने का निर्देश (Context/Persona) दें।</li>
                        <li><strong>कंटेंट क्रिएशन और समय की बचत:</strong> उन्होंने लाइव उदाहरण दिया कि किसी मीटिंग के लिए 30 मिनट की स्क्रिप्ट या एक अच्छी PPT जो सामान्यतः 12 घंटे लेती है, वह AI (जैसे ChatGPT, Claude 3.5 Sonnet) की मदद से मात्र 5 मिनट में बनाई जा सकती है।</li>
                    </ul>
                </div>

                <div class="mb-8">
                    <h3 class="text-xl font-bold text-gray-900 mb-2">पूरन सिंह (Pooran Singh) — धर्म सत्ता की ताकत (Concluding Note)</h3>
                    <ul class="list-disc list-inside text-gray-700 space-y-2 ml-4">
                        <li><strong>धर्म सत्ता की सर्वोच्चता:</strong> उन्होंने जोर देकर कहा कि दुनिया में सबसे बड़ी सत्ता "धर्म सत्ता" है। इसके बिना राजनीतिक या आर्थिक सत्ता केवल एक कल्पना मात्र है, या आप हमेशा किसी और के अधीन रहेंगे।</li>
                        <li><strong>पुरोहित की महत्वपूर्ण भूमिका:</strong> एक पुरोहित समाज की जड़ों को खाद-पानी देने का काम करता है। वह हर घर में महिलाओं, बच्चों, युवाओं और बुजुर्गों से सीधे जुड़ा होता है।</li>
                        <li><strong>धर्म, अर्थ, काम, मोक्ष का नया दृष्टिकोण:</strong> 
                            <ul class="list-circle list-inside ml-8 mt-1">
                                <li>सबसे पहले <strong>'धर्म'</strong> के क्षेत्र में काम करें (पुरोहित बनें)।</li>
                                <li>इससे स्वाभाविक रूप से <strong>'अर्थ'</strong> (पैसा, सम्मान, भोजन) आएगा।</li>
                                <li>अर्थ आने पर व्यक्ति अपनी सभी <strong>'कामनाएं'</strong> (घर, सुख-सुविधा) पूरी कर सकता है।</li>
                                <li>जब ये तीनों पूरे होंगे, तो तनाव खत्म होगा और जीते जी मानसिक शांति <strong>(मोक्ष)</strong> प्राप्त होगी।</li>
                            </ul>
                        </li>
                        <li><strong>हिस्सेदारी और संस्थागत विकास:</strong> "जितनी जिसकी संख्या भारी, उतनी उसकी हिस्सेदारी" का नारा देते हुए उन्होंने सभी मंदिरों और धार्मिक स्थलों में अनुपातिक प्रतिनिधित्व और अपने खुद के मठ खड़े करने का विजन साझा किया।</li>
                        <li><strong>अंतिम संदेश:</strong> "धर्म सत्ता हाथ में आ गई तो बाकी सभी सत्ताएं (राज सत्ता, अर्थ सत्ता) आपके पीछे ऐसे चलेंगी जैसे सूरज की ओर चलने पर परछाई पीछे चलती है।"</li>
                    </ul>
                </div>
"""

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# I will replace the previously inserted block with the new richer block.
# The previous block started right after "<h2>💡 मुख्य चर्चा बिंदु (Key Discussion Points)</h2>" and ended before "<!-- Decisions & Next Steps -->"

start_marker = "<h2>💡 मुख्य चर्चा बिंदु (Key Discussion Points)</h2>"
end_marker = "<!-- Decisions & Next Steps -->"

start_idx = html.find(start_marker)
end_idx = html.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    # also we need to keep the closing div of the card that was before <!-- Decisions & Next Steps -->
    # The structure was:
    # <div class="bg-white rounded-3xl p-8 shadow-sm border border-gray-100">
    #     <h2>💡 मुख्य चर्चा बिंदु (Key Discussion Points)</h2>
    #     [content]
    # </div>
    # <!-- Decisions & Next Steps -->
    
    # So we'll find the start_marker, then add the new content, then close the div.
    
    before = html[:start_idx + len(start_marker)]
    after = html[end_idx:]
    
    # Wait, the closing </div> is right before <!-- Decisions & Next Steps -->.
    # We should make sure we don't accidentally delete the closing </div> of the card.
    
    # A safer replacement:
    end_div_idx = html.rfind("</div>", start_idx, end_idx)
    
    if end_div_idx != -1:
        after = html[end_div_idx:]
        new_html = before + "\n<div class='mt-6'>\n" + new_content + "\n</div>\n            " + after
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Updated Insights HTML successfully with rich content!")
    else:
        print("Could not find closing div.")
else:
    print("Markers not found")
