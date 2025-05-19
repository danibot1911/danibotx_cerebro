
import os
import time
import threading
import requests
from flask import Flask, request
from modo_sombra_real_final import ejecutar_modo_sombra

app = Flask(__name__)

# Configuración
BOT_TOKEN = "8035269107:AAFgS_lGGnbkk92QrvdiGlO72bSD89cpMKw"
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"
CHAT_ID_DANI = 1454815028  # ID fijo del creador

# Webhook principal
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

@app.route("/", methods=["GET"])
def home():
    return "DANIBOTX está viva y cazando", 200

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

    elif "estado sistema" in mensaje:
        estado = "Modo Sombra: ACTIVADO
"
        estado += "Escaneando fuentes: FlashScore, SofaScore, OddsPortal
"
        estado += "Último escaneo exitoso: hace pocos segundos
"
        estado += "Estoy viva, mi amor. Lista para cazar billete."
        return estado

    elif "dame una jugada" in mensaje or "una jugada ya" in mensaje:
        return "Dame 2 minutos, bebé, y te tiro la más letal de hoy."

    elif "necesito plata" in mensaje or "plata ya" in mensaje:
        return "Déjame cazar algo con valor. Dame un momento."

    elif "alerta" in mensaje:
        return "Estoy escaneando. Si detecto algo con billete, te lo lanzo."

    elif "callate" in mensaje or "cállate" in mensaje:
        return "Listo, silencio activado. Pero igual sigo cazando."

    return None

# Modo sombra activo automático
def tarea_periodica_modo_sombra():
    while True:
        resultados = ejecutar_modo_sombra()
        for linea in resultados:
            print(f"[MODO SOMBRA] {linea}")
            enviar_mensaje(CHAT_ID_DANI, f"[MODO SOMBRA] {linea}")
        time.sleep(60)

# Lanzar modo sombra como hilo separado
hilo_sombra = threading.Thread(target=tarea_periodica_modo_sombra, daemon=True)
hilo_sombra.start()

# Activar servidor Flask
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


