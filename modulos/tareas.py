from pathlib import Path

from modulos.inteligencia import normalizar


DATA_DIR = Path("data")
ARCHIVO = DATA_DIR / "tareas.txt"


def asegurar_archivo():
    DATA_DIR.mkdir(exist_ok=True)

    if not ARCHIVO.exists():
        ARCHIVO.write_text("", encoding="utf-8")


def leer_tareas():
    asegurar_archivo()

    tareas = []

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()

            if not linea:
                continue

            if "|" in linea:
                estado, texto = linea.split("|", 1)
            else:
                estado, texto = "pendiente", linea

            tareas.append({
                "estado": estado.strip(),
                "texto": texto.strip(),
            })

    return tareas


def guardar_tareas(tareas):
    asegurar_archivo()

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        for tarea in tareas:
            estado = tarea.get("estado", "pendiente")
            texto = tarea.get("texto", "").strip()

            if texto:
                archivo.write(f"{estado}|{texto}\n")


def obtener_texto_despues_de_dos_puntos(texto):
    if ":" not in texto:
        return ""

    return texto.split(":", 1)[1].strip()


def tarea_duplicada(tareas, nueva_tarea):
    nueva_normal = normalizar(nueva_tarea)

    return any(
        normalizar(tarea["texto"]) == nueva_normal
        for tarea in tareas
    )


def formatear_tareas(tareas, solo_pendientes=False):
    if solo_pendientes:
        tareas = [
            tarea for tarea in tareas
            if tarea["estado"] != "completada"
        ]

    if not tareas:
        return "No tienes tareas guardadas."

    lineas = []

    for indice, tarea in enumerate(tareas, 1):
        icono = "✅" if tarea["estado"] == "completada" else "🟡"
        lineas.append(f"{indice}. {icono} {tarea['texto']}")

    return "\n".join(lineas)


def agregar_tarea(texto_tarea):
    tarea = texto_tarea.strip()

    if not tarea:
        return "Tareas", "Debes escribir una tarea."

    tareas = leer_tareas()

    if tarea_duplicada(tareas, tarea):
        return "Tareas", "Esa tarea ya existe."

    tareas.append({
        "estado": "pendiente",
        "texto": tarea,
    })

    guardar_tareas(tareas)

    return (
        "Tarea guardada",
        f"✅ Tarea agregada.\n\nTotal de tareas: {len(tareas)}"
    )


def eliminar_tarea(numero):
    if not numero.isdigit():
        return "Eliminar tarea", "Debes indicar un número de tarea."

    tareas = leer_tareas()
    indice = int(numero) - 1

    if indice < 0 or indice >= len(tareas):
        return "Eliminar tarea", "Número de tarea inválido."

    eliminada = tareas.pop(indice)
    guardar_tareas(tareas)

    return (
        "Eliminar tarea",
        f"🗑️ Se eliminó:\n{eliminada['texto']}"
    )


def completar_tarea(numero):
    if not numero.isdigit():
        return "Completar tarea", "Debes indicar un número de tarea."

    tareas = leer_tareas()
    indice = int(numero) - 1

    if indice < 0 or indice >= len(tareas):
        return "Completar tarea", "Número de tarea inválido."

    tareas[indice]["estado"] = "completada"
    guardar_tareas(tareas)

    return (
        "Tarea completada",
        f"✅ Se completó:\n{tareas[indice]['texto']}"
    )


def detectar_tareas(texto):
    texto_normal = normalizar(texto)

    if texto_normal.startswith("tarea:"):
        return agregar_tarea(obtener_texto_despues_de_dos_puntos(texto))

    if texto_normal.startswith("agregar tarea:"):
        return agregar_tarea(obtener_texto_despues_de_dos_puntos(texto))

    if texto_normal.startswith("nueva tarea:"):
        return agregar_tarea(obtener_texto_despues_de_dos_puntos(texto))

    if texto_normal in ["ver tareas", "tareas", "lista tareas", "mostrar tareas"]:
        tareas = leer_tareas()

        return (
            "Lista de tareas",
            f"Tienes {len(tareas)} tarea(s).\n\n{formatear_tareas(tareas)}"
        )

    if texto_normal in ["pendientes", "ver pendientes", "tareas pendientes"]:
        tareas = leer_tareas()
        pendientes = [t for t in tareas if t["estado"] != "completada"]

        return (
            "Tareas pendientes",
            f"Tienes {len(pendientes)} pendiente(s).\n\n{formatear_tareas(tareas, solo_pendientes=True)}"
        )

    if texto_normal.startswith("eliminar tarea"):
        numero = texto_normal.replace("eliminar tarea", "").replace(":", "").strip()
        return eliminar_tarea(numero)

    if texto_normal.startswith("completar tarea"):
        numero = texto_normal.replace("completar tarea", "").replace(":", "").strip()
        return completar_tarea(numero)

    if texto_normal == "limpiar tareas":
        guardar_tareas([])

        return (
            "Lista de tareas",
            "🧹 Todas las tareas fueron eliminadas."
        )

    return None
