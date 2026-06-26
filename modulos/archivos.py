from pathlib import Path
from datetime import datetime

from modulos.inteligencia import normalizar


NOTAS_DIR = Path("notas")
NOTAS_DIR.mkdir(exist_ok=True)

EXTENSION = ".txt"


def _nombre_seguro(nombre):
    nombre = nombre.strip()

    if not nombre:
        return ""

    nombre = nombre.replace("/", "").replace("\\", "")
    nombre = nombre.replace("..", "")

    if not nombre.endswith(EXTENSION):
        nombre += EXTENSION

    return nombre


def _leer_archivos():
    return sorted(NOTAS_DIR.glob(f"*{EXTENSION}"))


def _crear_nota(contenido):
    if not contenido:
        return "Debes indicar el contenido de la nota."

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archivo = NOTAS_DIR / f"nota_{timestamp}{EXTENSION}"

    with open(archivo, "w", encoding="utf-8") as f:
        f.write(contenido)

    return f"Nota guardada correctamente: {archivo.name}"


def _listar_notas():
    archivos = _leer_archivos()

    if not archivos:
        return "No existen notas guardadas."

    return "\n".join(
        f"{i}. {archivo.name}"
        for i, archivo in enumerate(archivos, 1)
    )


def _leer_nota(nombre):
    nombre = _nombre_seguro(nombre)

    if not nombre:
        return "Indica el nombre de la nota."

    archivo = NOTAS_DIR / nombre

    if not archivo.exists():
        return "La nota no existe."

    with open(archivo, "r", encoding="utf-8") as f:
        contenido = f.read().strip()

    return contenido or "La nota está vacía."


def _eliminar_nota(nombre):
    nombre = _nombre_seguro(nombre)

    if not nombre:
        return "Indica el nombre de la nota."

    archivo = NOTAS_DIR / nombre

    if not archivo.exists():
        return "La nota no existe."

    archivo.unlink()

    return f"Nota eliminada: {nombre}"


def _buscar_notas(termino):
    termino = termino.strip().lower()

    if not termino:
        return "Indica qué quieres buscar."

    resultados = []

    for archivo in _leer_archivos():
        contenido = archivo.read_text(encoding="utf-8").lower()

        if termino in archivo.name.lower() or termino in contenido:
            resultados.append(archivo.name)

    if not resultados:
        return "No encontré notas con ese término."

    return "\n".join(
        f"{i}. {nombre}"
        for i, nombre in enumerate(resultados, 1)
    )


def detectar_archivo(texto):
    texto_normal = normalizar(texto)

    if texto_normal.startswith("crear nota"):
        contenido = texto[len("crear nota"):].strip()
        return "Notas", _crear_nota(contenido)

    if texto_normal in ("listar notas", "ver notas", "notas"):
        return "Notas", _listar_notas()

    if texto_normal.startswith("leer nota"):
        nombre = texto[len("leer nota"):].strip()
        return "Notas", _leer_nota(nombre)

    if texto_normal.startswith("eliminar nota"):
        nombre = texto[len("eliminar nota"):].strip()
        return "Notas", _eliminar_nota(nombre)

    if texto_normal.startswith("buscar nota"):
        termino = texto[len("buscar nota"):].strip()
        return "Notas", _buscar_notas(termino)

    return None
