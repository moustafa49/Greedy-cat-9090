class GreedyCatAnalyzer:
    def __init__(self):
        self.history = []
        self.emojis = {
            'corn': "🌽", 'tomato': "🍅", 'carrot': "🥕", 'pepper': "🌶️",
            'shrimp': "🦐", 'cow': "🐄", 'fish': "🐟", 'chicken': "🐔"
        }

    def add_round(self, item):
        self.history.append(item)

    def get_stats(self):
        if not self.history:
            return {}
        
        len_db = len(self.history)
        stats = {}
        for key in self.emojis:
            # حساب الغياب (Distance)
            try:
                last_idx = len(self.history) - 1 - self.history[::-1].index(key)
                abs_val = len_db - 1 - last_idx
            except ValueError:
                abs_val = len_db
            
            # حساب التريند (آخر 10 أدوار)
            trend = self.history[-10:].count(key)
            stats[key] = {"abs": abs_val, "trend": trend}
        
        return stats
        
