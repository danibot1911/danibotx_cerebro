from flask import Flask, request
import requests
import json
from danibotx_core import analizar_mensaje  # Asegúrate que este archivo exista

# Configuración del bot
BOT_TOKEN = "8035269107:AAFgS_lGGnbkk92QrvdiGlO72bSD89cpMKw"
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
    requests.post(url, json=payload)

@app.route('/', methods=['POST'])
def recibir_webhook():
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        texto = data['message'].get('text', '')

        if texto:
            respuesta = analizar_mensaje(texto)
            enviar_mensaje(chat_id, respuesta)

    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
