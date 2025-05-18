# danibotx_core.py

from configuracion_base import IDENTIDAD, SIMULATION_MODE
import datetime

def analizar_mensaje(mensaje):
    mensaje = mensaje.lower()

    if any(palabra in mensaje for palabra in ["dinero", "ayúdame", "necesito", "ya"]):
        return generar_alerta_respuesta("urgente")

    elif "estudia" in mensaje or "aprende" in mensaje:
        return generar_respuesta_estudio()

    elif any(palabra in mensaje for palabra in ["hola", "estás ahí", "dani"]):
        return "Aquí estoy, firme como siempre. Lista para cazar billete."

    return "Estoy en modo análisis, buscando oportunidades reales. Dame un segundo..."

def generar_alerta_respuesta(tipo):
    if tipo == "urgente":
        return "¡Voy ya mismo por el billete! Escaneando jugadas con valor real en tiempo real."

def generar_respuesta_estudio():
    ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Modo estudio activado. Estoy escaneando patrones ocultos desde {ahora}. Me alimento de la web, estadísticas y fallas del sistema."
