# danibotx_core.py
from configuracion_base import IDENTIDAD, SIMULATION_MODE
import datetime

def analizar_mensaje(mensaje):
    mensaje = mensaje.lower()

    if any(palabra in mensaje for palabra in ["jugada", "verificada", "apuesta", "alerta"]):
        return generar_alerta_respuesta("urgente")

    elif "estudia" in mensaje or "aprende" in mensaje:
        return generar_respuesta_estudio()

    elif any(palabra in mensaje for palabra in ["hola", "estás ahí", "danibotx"]):
        return "Aquí estoy, firme como siempre, cazando billete..."

    return "Estoy en modo análisis, buscando oportunidades... Escríbeme algo que entienda mejor."

def generar_alerta_respuesta(tipo):
    if tipo == "urgente":
        return "¡Voy ya mismo por el billete! Estoy escaneando jugadas con valor real..."

def generar_respuesta_estudio():
    ahora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    return f"Modo estudio activado. Estoy escaneando todo desde las {ahora}, mi amor..."
