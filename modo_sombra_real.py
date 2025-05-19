import requests
import threading
import time
from bs4 import BeautifulSoup
import logging

# Configura logger
logging.basicConfig(level=logging.INFO)

def escanear_eventos_deportivos():
    while True:
        try:
            logging.info("DANIBOTX está escaneando eventos activos...")

            # Sitios que se pueden escanear (aquí solo ejemplo con Flashscore)
            urls = [
                "https://www.flashscore.com",
                "https://www.sofascore.com",
                "https://www.oddsportal.com"
            ]

            resultados = []

            for url in urls:
                try:
                    headers = {
                        "User-Agent": "Mozilla/5.0"
                    }
                    r = requests.get(url, headers=headers, timeout=10)
                    if r.status_code == 200:
                        soup = BeautifulSoup(r.text, "html.parser")
                        # Buscar títulos o contenido visible para análisis (esto se personalizará)
                        title = soup.title.string if soup.title else "Sin título"
                        resultados.append(f"{url} → OK: {title}")
                    else:
                        resultados.append(f"{url} → ERROR {r.status_code}")
                except Exception as e:
                    resultados.append(f"{url} → EXCEPCIÓN: {str(e)}")

            for resultado in resultados:
                logging.info(resultado)

        except Exception as general_error:
            logging.error(f"Fallo general en escaneo: {str(general_error)}")

        # Esperar antes de volver a escanear
        time.sleep(60)  # Escanea cada 60 segundos

# Activar el escaneo en un hilo independiente
def iniciar_modo_sombra():
    hilo = threading.Thread(target=escanear_eventos_deportivos, daemon=True)
    hilo.start()
