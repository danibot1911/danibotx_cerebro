import threading
import time

def escanear_eventos_deportivos():
    print(">>> DANIBOTX: ¡Modo sombra arrancó!")
    while True:
        print(">>> DANIBOTX: Sigue escaneando en segundo plano...")
        time.sleep(10)

def iniciar_modo_sombra():
    print(">>> Llamando a iniciar_modo_sombra() desde main.py...")
    hilo = threading.Thread(target=escanear_eventos_deportivos, daemon=True)
    hilo.start()
