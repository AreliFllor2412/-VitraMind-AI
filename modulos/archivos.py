from modulos.inteligencia import normalizar


def detectar_archivo(texto):
    texto_normal = normalizar(texto)

    if "crear nota" in texto_normal:
        indice = texto_normal.find("crear nota")
        contenido = texto[indice + len("crear nota"):].strip()

        with open("nota_ia.txt", "a", encoding="utf-8") as archivo:
            archivo.write(contenido + "\n")

        return "Nota guardada", "Guarde tu nota en nota_ia.txt"

    if "leer nota" in texto_normal:
        try:
            with open("nota_ia.txt", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()

            return "Nota guardada", contenido if contenido.strip() else "La nota esta vacia."

        except FileNotFoundError:
            return "Nota guardada", "No existe nota_ia.txt todavia."

    return None
