def detectar_tareas(texto):
    texto = texto.lower()

    if texto.startswith("tarea:"):
        tarea = texto.replace("tarea:", "").strip()

        with open("tareas.txt", "a", encoding="utf-8") as archivo:
            archivo.write("- " + tarea + "\n")

        return "Tarea guardada", f"Guardé esta tarea:\n{tarea}"

    if "ver tareas" in texto:
        try:
            with open("tareas.txt", "r", encoding="utf-8") as archivo:
                contenido = archivo.read()

            if contenido.strip():
                return "Lista de tareas", contenido

            return "Lista de tareas", "No tienes tareas guardadas."

        except FileNotFoundError:
            return "Lista de tareas", "Todavía no existe archivo de tareas."

    return None