from pathlib import Path

from modulos.inteligencia import normalizar

ARCHIVO = Path("tareas.txt")


def leer_tareas():
    if not ARCHIVO.exists():
        return []

    with open(ARCHIVO, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def guardar_tareas(lista):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for tarea in lista:
            f.write(tarea + "\n")


def detectar_tareas(texto):
    texto_normal = normalizar(texto)

    # Agregar tarea
    if texto_normal.startswith("tarea:"):
        tarea = texto.split(":", 1)[1].strip()

        if not tarea:
            return "Tareas", "Debes escribir una tarea."

        tareas = leer_tareas()

        if tarea in tareas:
            return "Tareas", "Esa tarea ya existe."

        tareas.append(tarea)
        guardar_tareas(tareas)

        return (
            "Tarea guardada",
            f"✅ Tarea agregada.\n\n"
            f"Total de tareas: {len(tareas)}"
        )

    # Ver tareas
    if texto_normal in ("ver tareas", "tareas", "lista tareas"):
        tareas = leer_tareas()

        if not tareas:
            return "Lista de tareas", "No tienes tareas guardadas."

        resultado = "\n".join(
            f"{i}. {t}"
            for i, t in enumerate(tareas, 1)
        )

        return (
            "Lista de tareas",
            f"Tienes {len(tareas)} tarea(s).\n\n{resultado}"
        )

    # Eliminar tarea
    if texto_normal.startswith("eliminar tarea:"):
        numero = texto.split(":", 1)[1].strip()

        if not numero.isdigit():
            return "Eliminar tarea", "Debes indicar un número."

        indice = int(numero) - 1
        tareas = leer_tareas()

        if indice < 0 or indice >= len(tareas):
            return "Eliminar tarea", "Número de tarea inválido."

        eliminada = tareas.pop(indice)
        guardar_tareas(tareas)

        return (
            "Eliminar tarea",
            f"🗑️ Se eliminó:\n{eliminada}"
        )

    # Limpiar tareas
    if texto_normal == "limpiar tareas":
        guardar_tareas([])
        return (
            "Lista de tareas",
            "🧹 Todas las tareas fueron eliminadas."
        )

    return None
