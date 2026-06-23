from pathlib import Path
from datetime import datetime

from modulos.inteligencia import normalizar


NOTAS_DIR = Path("notas")
NOTAS_DIR.mkdir(exist_ok=True)


def detectar_archivo(texto):
    texto_normal = normalizar(texto)

    if texto_normal.startswith("crear nota"):
        contenido = texto[len("crear nota"):].strip()

        if not contenido:
            return (
                "Notas",
                "Debes indicar el contenido de la nota."
            )

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        archivo = NOTAS_DIR / f"nota_{timestamp}.txt"

        with open(archivo, "w", encoding="utf-8") as f:
            f.write(contenido)

        return (
            "Notas",
            f"Nota guardada correctamente: {archivo.name}"
        )

    if texto_normal == "listar notas":
        archivos = sorted(NOTAS_DIR.glob("*.txt"))

        if not archivos:
            return (
                "Notas",
                "No existen notas guardadas."
            )

        contenido = "\n".join(
            f"- {archivo.name}"
            for archivo in archivos
        )

        return (
            "Notas",
            contenido
        )

    if texto_normal.startswith("leer nota"):
        nombre = texto[len("leer nota"):].strip()

        if not nombre:
            return (
                "Notas",
                "Indica el nombre de la nota."
            )

        archivo = NOTAS_DIR / nombre

        if not archivo.exists():
            return (
                "Notas",
                "La nota no existe."
            )

        with open(archivo, "r", encoding="utf-8") as f:
            return (
                "Notas",
                f.read()
            )

    if texto_normal.startswith("eliminar nota"):
        nombre = texto[len("eliminar nota"):].strip()

        archivo = NOTAS_DIR / nombre

        if not archivo.exists():
            return (
                "Notas",
                "La nota no existe."
            )

        archivo.unlink()

        return (
            "Notas",
            f"Nota eliminada: {nombre}"
        )

    return None
