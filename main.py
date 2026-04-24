import json
from analyzer import GreedyCatAnalyzer # بننادي على المحلل اللي إنت عملته

def main():
    bot = GreedyCatAnalyzer()
    print("--- Greedy Cat 9090 Pro ---")
    print("دخل اسم الصنف (جزر، فلفل، جمبري، سمكة...) أو اكتب 'خروج' للقفل")

    while True:
        user_input = input("\nالدور اللي ظهر: ").strip()
        
        if user_input == 'خروج':
            break
            
        # إضافة الدور وتحليله
        bot.add_round(user_input)

if __name__ == "__main__":
    main()
  
