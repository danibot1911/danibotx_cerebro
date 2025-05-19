from flask import Flask, request
import requests
import json
from danibotx_core import analizar_mensaje

# Configuración del bot
BOT_TOKEN = "8035269107:AAFgS_lGGnbkk92Qr vdiGl072"  # Usa tu token real aquí
OWNER_ID = 1454815028
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

app = Flask(__name__)

def enviar_mensaje(chat_id, texto):
    url = f"{API_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": texto,
        "parse_mode": "Markdown"
    }
    headers = {"Content-Type": "application/json"}
    requests.post(url, data=json.dumps(payload), headers=headers)

@app.route(f"/bot{BOT_TOKEN}", methods=["POST"])
def recibir_actualizacion():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "")
        respuesta = analizar_mensaje(texto)
        enviar_mensaje(chat_id, respuesta)
    return {"ok": True}

@app.route("/", methods=["GET"])
def index():
    return "DANIBOTX encendida y cazando billete."
