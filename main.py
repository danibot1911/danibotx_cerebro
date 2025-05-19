from flask import Flask, request
import requests
import json
import os
from danibotx_core import analizar_mensaje

BOT_TOKEN = os.environ.get("TOKEN")
OWNER_ID = os.environ.get("OWNER_ID")
BOT_NAME = os.environ.get("BOT_NAME")
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

@app.route("/", methods=["POST"])
def recibir_mensaje():
    data = request.json
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"]["text"]
        respuesta = analizar_mensaje(texto)
        enviar_mensaje(chat_id, respuesta)
    return {"ok": True}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
