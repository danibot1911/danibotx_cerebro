
import os
import requests
import threading
import time
from flask import Flask, request
from modo_sombra_real_final import ejecutar_modo_sombra

app = Flask(__name__)

BOT_TOKEN = "8035269107:AAFgS_lGGnbkk92QrvdiGlO72bSD89cpMKw"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
CHAT_ID = 1454815028

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
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"[ERROR ENVÍO] {e}")

def analizar_mensaje(mensaje):
    mensaje = mensaje.lower().strip()
    if "estudia" in mensaje:
        return "Estoy estudiando patrones ocultos. No es carreta."
    elif "estado sistema" in mensaje:
        return "Modo sombra: ACTIVO
Fuentes: FlashScore, SofaScore, OddsPortal
Cazando billete en silencio..."
    elif "jugada" in mensaje:
        return "Dame 2 minutos, estoy revisando todo el mundo para darte algo real."
    elif "alerta" in mensaje:
        return "Estoy escaneando. Si veo algo con valor, te lo lanzo sin filtro."
    return None

def tarea_periodica_modo_sombra():
    while True:
        resultados = ejecutar_modo_sombra()
        for linea in resultados:
            print(f"[MODO SOMBRA] {linea}")
            enviar_mensaje(CHAT_ID, linea)
        time.sleep(60)

if __name__ == "__main__":
    hilo = threading.Thread(target=tarea_periodica_modo_sombra, daemon=True)
    hilo.start()
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)



