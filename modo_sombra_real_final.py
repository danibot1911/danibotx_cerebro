import requests
from bs4 import BeautifulSoup

def extraer_de_flashscore():
    try:
        url = "https://www.flashscore.com/"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        partidos = []
        for match in soup.select(".event__match"):
            texto = match.get_text(strip=True)
            if texto:
                partidos.append(f"[FLASH] {texto}")
        return partidos or ["[FLASH] No hay partidos en vivo."]
    except Exception as e:
        return [f"[FLASH ERROR] {str(e)}"]

def extraer_de_sofas |oai:code-citation|
def extraer_de_sofascore():
    try:
        url = "https://www.sofascore.com/"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        partidos = []
        for div in soup.select("a[href*='/match/']"):
            texto = div.text.strip()
            if texto:
                partidos.append(f"[SOFA] {texto}")
        return partidos or ["[SOFA] No se detectaron partidos."]
    except Exception as e:
        return [f"[SOFA ERROR] {str(e)}"]

def extraer_de_oddsportal():
    try:
        url = "https://www.oddsportal.com/matches/"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        partidos = []
        for match in soup.select(".match-row"):
            texto = match.text.strip()
            if texto:
                partidos.append(f"[ODDS] {texto}")
        return partidos or ["[ODDS] No se encontraron partidos."]
    except Exception as e:
        return [f"[ODDS ERROR] {str(e)}"]

def ejecutar_modo_sombra():
    resultados = []
    resultados += extraer_de_flashscore()
    resultados += extraer_de_sofascore()
    resultados += extraer_de_oddsportal()
    return resultados
