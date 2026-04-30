from modulos.inteligencia import normalizar


def detectar_tareas(texto):
    texto_normal = normalizar(texto)

    if texto_normal.startswith("tarea:"):
        tarea = texto.split(":", 1)[1].strip()

        with open("tareas.txt", "a", encoding="utf-8") as archivo:
            archivo.write("- " + tarea + "\n")

        return "Tarea guardada", f"Guarde esta tarea:\n{tarea}"

    if "ver tareas" in texto_normal:
        try:
            with open("tareas.txt", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()

            if contenido.strip():
                return "Lista de tareas", contenido

            return "Lista de tareas", "No tienes tareas guardadas."

        except FileNotFoundError:
            return "Lista de tareas", "Todavia no existe archivo de tareas."

    return None
