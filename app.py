import os
from flask import Flask, request, jsonify
from analyzer import GreedyCatAnalyzer

app = Flask(__name__)

# استدعاء كلاس التحليل اللي عملناه
bot = GreedyCatAnalyzer()

@app.route('/')
def home():
    return "Greedy Cat 9090 Server is Running Successfully! 🚀"

@app.route('/predict', methods=['GET'])
def predict():
    item = request.args.get('item')
    if item:
        # إضافة الصنف للتحليل
        bot.add_round(item)
    
    # جلب آخر التاريخ والنتائج
    history = bot.history[-10:] if hasattr(bot, 'history') else []
    
    return jsonify({
        "status": "Success",
        "last_item_added": item,
        "recent_history": history,
        "message": "Send ?item=name to add new rounds"
    })

if __name__ == "__main__":
    # أهم سطر عشان Railway يشتغل: سحب المنفذ من البيئة المحيطة
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
    
