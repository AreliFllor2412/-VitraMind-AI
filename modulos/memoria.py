import datetime

memoria = []

def guardar_memoria(texto):
    memoria.append(texto)

def ver_memoria():
    if not memoria:
        return "Aún no tengo memoria en esta sesión."

    return "Últimos mensajes:\n- " + "\n- ".join(memoria[-6:])

def guardar_historial(usuario, respuesta):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("historial.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}] Tú: {usuario}\n")
        archivo.write(f"[{fecha}] IA: {respuesta}\n\n")