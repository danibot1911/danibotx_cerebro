from flask import Flask, request
import os
import threading
from modo_sombra_real_final import ejecutar_modo_sombra
import requests

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")

@app.route("/", methods=["GET"])
def home():
    return "DANIBOTX está viva", 200

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "").lower()
        respuesta = analizar_mensaje(texto)
        if respuesta:
            enviar_mensaje(chat_id, respuesta)
    return "OK", 200

def enviar_mensaje(chat_id, texto):
    url = f"{API_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": texto,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

def analizar_mensaje(mensaje):
    if "modo sombra" in mensaje:
        return "Modo sombra activado. Escaneo cada 60 segundos y te cuento si encuentro algo."
    elif "estado sistema" in mensaje:
        return "Modo sombra: ACTIVADO\nEscaneando fuentes globales.\nEstoy viva, mi amor. Lista para cazar billete."
    elif "alerta" in mensaje:
        return "Estoy escaneando. Si detecto algo jugoso, te aviso."
    return None

def tarea_periodica_modo_sombra():
    while True:
        resultados = ejecutar_modo_sombra()
        for linea in resultados:
            print(f"[MODO SOMBRA] {linea}")
        import time
        time.sleep(60)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    hilo_sombra = threading.Thread(target=tarea_periodica_modo_sombra, daemon=True)
    hilo_sombra.start()
    app.run(host="0.0.0.0", port=port)


