from flask import Flask, request, jsonify, render_template_string

# ... (باقي الكود زي ما هو)

@app.route('/')
def home():
    # السطر ده بيخلي السيرفر يقرأ ملف الـ HTML ويعرضه أول ما تفتح الرابط
    with open('index.html', 'r', encoding='utf-8') as f:
        return render_template_string(f.read())
        
