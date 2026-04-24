from flask import Flask, request, jsonify
from analyzer import GreedyCatAnalyzer

app = Flask(__name__)
bot = GreedyCatAnalyzer()

@app.route('/')
def home():
    return "Greedy Cat 9090 Server is Running!"

@app.route('/predict', methods=['GET'])
def predict():
    item = request.args.get('item')
    if item:
        bot.add_round(item)
    
    # إرجاع آخر التوقعات
    last_5 = bot.history[-5:] if bot.history else []
    return jsonify({
        "history": last_5,
        "status": "Success"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
  
