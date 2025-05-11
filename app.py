from flask import Flask, render_template, request, jsonify
import requests
import json
from datetime import datetime

app = Flask(__name__)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"
HISTORY_FILE = "chat_history.jsonl"

def log_conversation(user_msg, bot_msg, lang="es"):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "timestamp": datetime.utcnow().isoformat(),
            "lang": lang,
            "user": user_msg,
            "bot": bot_msg,
            "source": "llama3"
        }) + "\n")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": user_input,
        "stream": False
    })

    data = response.json()
    bot_reply = data.get("response", "(sin respuesta)")
    log_conversation(user_input, bot_reply)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
