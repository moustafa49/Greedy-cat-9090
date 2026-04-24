from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__)

# ملف تخزين البيانات (CSV لسهولة التعامل على Railway)
DB_FILE = 'history_data.csv'

# وظيفة التأكد من وجود الملف وتهيئته
def init_db():
    if not os.path.exists(DB_FILE):
        df = pd.DataFrame(columns=['item', 'timestamp'])
        df.to_csv(DB_FILE, index=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_move', methods=['POST'])
def add_move():
    try:
        data = request.json
        item = data.get('item')
        
        # حفظ الحركة مع توقيت حدوثها
        new_row = pd.DataFrame([{'item': item, 'timestamp': pd.Timestamp.now()}])
        new_row.to_csv(DB_FILE, mode='a', header=False, index=False)
        
        # قراءة البيانات للتحليل
        df = pd.read_csv(DB_FILE)
        
        # تحليل سريع: حساب أكثر الأصناف تكراراً (بصمة الماكينة)
        counts = df['item'].value_counts().to_dict()
        total_moves = len(df)
        
        # توقع بسيط: الصنف الغائب الأكبر (الجعفلة)
        # ملاحظة: المنطق ده هيتطور مع الوقت لما نجمع داتا أكتر
        ai_suggestion = "جاري تجميع البيانات للتحليل العميق..."
        if total_moves > 10:
            top_item = df['item'].value_counts().idxmin() # الأقل ظهوراً حالياً
            ai_suggestion = f"الرادار يرجح تحرك نحو: {top_item}"

        return jsonify({
            "status": "success",
            "total": total_moves,
            "suggestion": ai_suggestion,
            "counts": counts
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    init_db()
    # استخدام التمرير الديناميكي للمنفذ (Port) عشان يشتغل على Railway/Vercel
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

