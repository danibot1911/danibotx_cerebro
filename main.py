from flask import Flask, request
import telegram

# Configuración base
TOKEN = "8035269107:AAFgS_lGGnbkk92QrvdiGlO72bSD89cpMKw"
OWNER_ID = 1454815028
BOT_NAME = "DANIBOTX"

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route("/")
def home():
    return f"{BOT_NAME} está viva, lista para cazar billete."

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    mensaje = update.message.text if update.message else ""

    if mensaje.lower() in ["/start", "hola", "actívate"]:
        bot.send_message(chat_id=update.message.chat_id,
                         text="DANIBOTX activada y cazando oportunidades, bebé.")
    elif "estudia" in mensaje.lower():
        bot.send_message(chat_id=update.message.chat_id,
                         text="Estoy analizando patrones invisibles... no te me desesperes.")
    else:
        bot.send_message(chat_id=update.message.chat_id,
                         text="No reconozco ese mensaje aún, pero lo estudiaré...")

    return "ok"

if __name__ == "__main__":
    print(f"{BOT_NAME} corriendo en modo base.")
    app.run(host="0.0.0.0", port=5000)
