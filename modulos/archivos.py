def detectar_archivo(texto):
    texto = texto.lower()

    if "crear nota" in texto:
        contenido = texto.replace("crear nota", "").strip()

        with open("nota_ia.txt", "a", encoding="utf-8") as archivo:
            archivo.write(contenido + "\n")

        return "Archivo creado", "Guardé tu nota en nota_ia.txt"

    if "leer nota" in texto:
        try:
            with open("nota_ia.txt", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()

            return "Nota guardada", contenido if contenido.strip() else "La nota está vacía."

        except FileNotFoundError:
            return "Nota guardada", "No existe nota_ia.txt todavía."

    return None