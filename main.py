
import os
import time
import requests
import threading
from flask import Flask, request
from modo_sombra_real import ejecutar_modo_sombra

app = Flask(__name__)

# Datos verificados
BOT_TOKEN = "8035269107:AAFgS_lGGnbkk92QrvdiGlO72bSD89cpMKw"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
CHAT_ID_DANI = 1454815028  # ID real de Daniel

@app.route("/", methods=["GET"])
def home():
    return "DANIBOTX está online", 200

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
        return "Ya me puse a estudiar, mi amor."
    elif "dame una jugada" in mensaje or "mándame una jugada" in mensaje:
        return "Dame 2 minutos, bebé, y te tiro la más letal de hoy."
    elif "modo sombra" in mensaje:
        return "Modo sombra activado. Escaneo cada 60 segundos y te cuento si encuentro algo."
    else:
        return "No entendí bien, mi amor. Reformulame eso y lo miramos."

# Modo sombra activado automáticamente al iniciar
def tarea_periodica_modo_sombra():
    while True:
        resultados = ejecutar_modo_sombra()
        for linea in resultados:
            print(f"[MODO SOMBRA] {linea}")
            enviar_mensaje(CHAT_ID_DANI, f"[MODO SOMBRA] {linea}")
        time.sleep(60)

# Lanzar el hilo del modo sombra
hilo_sombra = threading.Thread(target=tarea_periodica_modo_sombra, daemon=True)
hilo_sombra.start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)

