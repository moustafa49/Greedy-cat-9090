import json
import os

class GreedyCatAnalyzer:
    def __init__(self, filename="history.json"):
        self.filename = filename
        self.history = self._load_data()

    def _load_data(self):
        # بيقرأ البيانات القديمة لو موجودة
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []

    def save_data(self):
        # بيحفظ الأدوار الجديدة في الملف
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, ensure_ascii=False)

    def add_round(self, item):
        self.history.append(item)
        self.save_data()
        self.analyze()

    def analyze(self):
        if len(self.history) < 5:
            print("💡 محتاج بيانات أكتر (سجل 5 أدوار على الأقل)")
            return

        last_5 = self.history[-5:]
        # حساب عدد مرات ظهور الخضار في آخر 5 أدوار
        veg_items = ["طماطم", "جزر", "فلفل", "درة"]
        veg_count = sum(1 for x in last_5 if x in veg_items)

        print(f"\n--- تحليل الشريط ---")
        print(f"آخر الأدوار: {' ← '.join(last_5[::-1])}")
        
        if veg_count >= 4:
            print("🚨 التوقع: السيرفر بارد.. ركز على الجمبري/الجموسة")
        else:
            print("🛡️ التوقع: تأمين خضار (فلفل/طماطم)")
            
