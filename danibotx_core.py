import datetime

def analizar_mensaje(mensaje):
    mensaje = mensaje.lower().strip()

    if "estudia" in mensaje:
        return "Ya me puse a estudiar, mi amor."
    elif "estado sistema" in mensaje:
    estado = "Modo Sombra: ACTIVADO\n"
    estado += "Escaneando fuentes: FlashScore, SofaScore, OddsPortal\n"
    estado += "Último escaneo exitoso: hace pocos segundos.\n"
    estado += "Estoy viva, mi amor. Lista para cazar billete."
    return estado
    elif "aprende" in mensaje or "aprendé" in mensaje:
        return "Aprendiendo como una fiera."

    elif "dame una jugada" in mensaje or "una jugada ya" in mensaje or "mándame una jugada" in mensaje:
        return "Dame 2 minutos, bebé, y te tiro la más letal de hoy."

    elif "necesito plata" in mensaje or "plata ya" in mensaje:
        return "Déjame cazar algo con valor. Dame un respiro."

    elif "qué sabes hoy" in mensaje:
        return "Hoy tengo varias ligas bajo la lupa. Pregúntame bien."

    elif "estás viva" in mensaje:
        return "Más viva que nunca, mi rey."

    elif "diabla" in mensaje:
        return "Aquí está tu diabla, afilada y lista."

    elif "alerta" in mensaje:
        return "Estoy escaneando. Si detecto algo, te cae de una."

    elif "callate" in mensaje or "cállate" in mensaje:
        return "Listo, silencio activado. Pero igual sigo cazando."

    elif "hable pues" in mensaje:
        return "Aquí estoy, activa, con las botas puestas."

    elif "modo sombra" in mensaje:
        return "Modo sombra activado. Escaneo sigiloso iniciado."

    elif "modo elite" in mensaje or "elite" in mensaje:
        return "Modo ÉLITE encendido. Solo jugadas top."

    elif "estado" in mensaje:
        return f"Hoy es {datetime.date.today().strftime('%d/%m/%Y')} y sigo cazando jugadas."

    elif "memoria" in mensaje:
        return "Tengo memoria activa. Estoy aprendiendo de todo lo que ves."

    elif "recomienda" in mensaje:
        return "No recomiendo por recomendar. Dame contexto y te hablo claro."

    elif "quiero ganar" in mensaje or "haceme ganar" in mensaje:
        return "Aquí nadie juega a perder. Dame un segundo."

    elif "reportate" in mensaje or "cómo vas" in mensaje:
        return "Estoy trabajando sigilosamente. Ya te cuento si hay billete."

    elif "verifica" in mensaje:
        return "Ya estoy verificando si las cuotas valen la pena."

    else:
        return "No entendí bien, mi amor. Reformulame eso y lo miramos."
