import json
from collections import Counter

class GreedyCatAnalyzer:
    def __init__(self):
        # تعريف الأصناف وقيمها
        self.data = {
            "خضار": ["طماطم", "جزر", "فلفل", "درة"],
            "لحوم": {"جمبري": 10, "جموسة": 15, "سمكة": 25, "كتكوت": 45}
        }
        self.history = []

    def add_round(self, item):
        self.history.append(item)
        self.analyze()

    def analyze(self):
        if len(self.history) < 5:
            print("💡 محتاج بيانات أكتر.. سجل كمان.")
            return

        last_5 = self.history[-5:]
        veg_count = sum(1 for x in last_5 if x in self.data["خضار"])
        
        print(f"\n--- تحليل الدور {len(self.history)} ---")
        print(f"آخر الأدوار: {' ← '.join(last_5[::-1])}")
        
        # منطق التوقع
        if veg_count >= 4:
            print("🚨 حالة السيرفر: تبريد حاد (خضار كتير)")
            print("🎯 التوقع: اللحمة قربت! ركز على الجمبري والجموسة.")
        elif veg_count <= 1:
            print("🔥 حالة السيرفر: تسخين (موجة لحوم)")
            print("🎯 التوقع: كمل مع اللحمة أو أمن نفسك بـ (طماطم/فلفل).")
        else:
            print("🛡️ حالة السيرفر: تذبذب (غير مستقر)")

# --- تشغيل تجريبي ---
bot = GreedyCatAnalyzer()

# مثال لإضافة أدوار
current_rounds = ["سمكة", "جزر", "جزر", "درة", "طماطم"]
for r in current_rounds:
    bot.add_round(r)

# إضافة دور جديد يدوي
# bot.add_round("فلفل")

