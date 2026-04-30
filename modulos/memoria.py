import datetime


memoria = []


def guardar_memoria(texto):
    texto = texto.strip()
    if texto:
        memoria.append(texto)


def ver_memoria():
    if not memoria:
        return "Aun no tengo memoria en esta sesion."

    return "Ultimos mensajes:\n- " + "\n- ".join(memoria[-6:])


def obtener_memoria():
    return memoria[:]


def guardar_historial(usuario, respuesta):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("historial.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha}] Tu: {usuario}\n")
        archivo.write(f"[{fecha}] IA: {respuesta}\n\n")
