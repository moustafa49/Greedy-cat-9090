import os
from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
from analyzer import GreedyCatAnalyzer

app = Flask(__name__)
CORS(app) # مهم جداً عشان Vercel يقدر يكلم Railway

bot = GreedyCatAnalyzer()

@app.route('/')
def home():
    with open('index.html', 'r', encoding='utf-8') as f:
        return render_template_string(f.read())

@app.route('/predict', methods=['GET'])
def predict():
    item = request.args.get('item')
    if item:
        bot.add_round(item)
    
    return jsonify({
        "status": "Success",
        "history": bot.history[-10:],
        "stats": bot.get_stats()
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
    
