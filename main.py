from flask import Flask, request
import telegram
from danibotx_core import analizar_mensaje
from configuracion_base import TOKEN

app = Flask(__name__)
bot = telegram.Bot(token=TOKEN)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    mensaje = update.message.text if update.message else ""
    chat_id = update.message.chat.id if update.message else None

    if mensaje and chat_id:
        respuesta = analizar_mensaje(mensaje)
        if respuesta:
            bot.send_message(chat_id=chat_id, text=respuesta)

    return "ok"

@app.route("/")
def home():
    return "DANIBOTX está viva y conectada."
