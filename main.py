import os
import requests
import threading
import time
from flask import Flask, request
from modo_sombra_real_final import ejecutar_modo_sombra

# TOKEN E ID REALES
BOT_TOKEN = "8035269107:AAFgS_lGGnbkk92QrvdiGlO72bSD89cpMKw"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
CHAT_ID = 1454815028

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "DANIBOTX está viva", 200

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        texto = data["message"].get("text", "")
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
    mensaje = mensaje.lower().strip()
    if "estudia" in mensaje:
        return "Ya me puse a estudiar, mi amor."
    elif "estado sistema" in mensaje:
        estado = "Modo Sombra: ACTIVADO\n"
        estado += "Escaneando fuentes: FlashScore, SofaScore, OddsPortal\n"
        estado += "Último escaneo exitoso: hace pocos minutos\n"
        estado += "Estoy viva, mi amor. Lista para cazar billete."
        return estado
    elif "jugada" in mensaje:
        return "Dame 2 minutos, bebé, y te tiro la mejor jugada del planeta."
    elif "alerta" in mensaje:
        return "Estoy escaneando. Si detecto algo con valor, te mando la bomba."

    return None

def tarea_periodica_modo_sombra():
    while True:
        resultados = ejecutar_modo_sombra()
        for linea in resultados:
            print(f"[MODO SOMBRA] {linea}")
            enviar_mensaje(CHAT_ID, linea)
        time.sleep(60)

# HILO DE ESCANEO AUTOMÁTICO
if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    hilo_sombra = threading.Thread(target=tarea_periodica_modo_sombra, daemon=True)
    hilo_sombra.start()
    app.run(host="0.0.0.0", port=port)


