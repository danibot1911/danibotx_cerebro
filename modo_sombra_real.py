import requests
from bs4 import BeautifulSoup
import time

sitios_a_escanear = [
    "https://www.flashscore.com",
    "https://www.sofascore.com",
    "https://www.oddsportal.com"
]

def ejecutar_modo_sombra():
    resultados = []

    for url in sitios_a_escanear:
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                title = soup.title.string if soup.title else "Sin título"
                resultados.append(f"{url} → OK: {title}")
            else:
                resultados.append(f"{url} → ERROR {response.status_code}")
        except Exception as e:
            resultados.append(f"{url} → EXCEPCIÓN: {str(e)}")

    return resultados
