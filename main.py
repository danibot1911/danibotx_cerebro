from flask import Flask, request
import os
import json
import requests
from danibotx_core import analizar_mensaje

BOT_TOKEN = os.getenv("TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))
BOT_NAME = os.getenv("BOT_NAME", "DANIBOTX")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

app = Flask(__name__)

def enviar_mensaje(chat_id, texto):
    url = f"{API_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": texto,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

@app.route(f'/{BOT_TOKEN}', methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "")
        respuesta = analizar_mensaje(texto)
        if respuesta:
            enviar_mensaje(chat_id, respuesta)
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
