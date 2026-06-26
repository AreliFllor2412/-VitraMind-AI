from modulos.inteligencia import normalizar

MAX_PALABRAS = 35


def _obtener_contenido(texto):
    partes = texto.split(":", 1)
    return partes[1].strip() if len(partes) > 1 else ""


def _resumir(contenido):
    if not contenido:
        return "No encontré texto para resumir."

    palabras = contenido.split()

    if len(palabras) <= MAX_PALABRAS:
        return contenido

    return " ".join(palabras[:MAX_PALABRAS]) + "..."


def _ordenar(contenido):
    if not contenido:
        return "No encontré elementos para ordenar."

    if "," in contenido:
        elementos = [x.strip() for x in contenido.split(",")]
    else:
        elementos = [x.strip() for x in contenido.splitlines()]

    elementos = [x for x in elementos if x]

    if not elementos:
        return "No encontré elementos para ordenar."

    return "\n".join(
        f"{i}. {item}"
        for i, item in enumerate(elementos, 1)
    )


def _ordenar_alfabeticamente(contenido):
    if not contenido:
        return "No encontré elementos para ordenar."

    if "," in contenido:
        elementos = [x.strip() for x in contenido.split(",")]
    else:
        elementos = [x.strip() for x in contenido.splitlines()]

    elementos = sorted([x for x in elementos if x], key=str.lower)

    return "\n".join(
        f"{i}. {item}"
        for i, item in enumerate(elementos, 1)
    )


def _mayusculas(contenido):
    return contenido.upper() if contenido else "No encontré texto."


def _minusculas(contenido):
    return contenido.lower() if contenido else "No encontré texto."


def _titulo(contenido):
    return contenido.title() if contenido else "No encontré texto."


def _contar(contenido):
    if not contenido:
        return "No encontré texto."

    palabras = len(contenido.split())
    caracteres = len(contenido)

    return (
        f"Palabras: {palabras}\n"
        f"Caracteres: {caracteres}"
    )


def detectar_texto(texto):
    texto_normal = normalizar(texto)

    comandos = {
        "resume:": ("Resumen rápido", _resumir),
        "resumen:": ("Resumen rápido", _resumir),
        "ordena:": ("Texto ordenado", _ordenar),
        "abc:": ("Orden alfabético", _ordenar_alfabeticamente),
        "mayus:": ("Texto en MAYÚSCULAS", _mayusculas),
        "minus:": ("Texto en minúsculas", _minusculas),
        "titulo:": ("Texto tipo título", _titulo),
        "contar:": ("Estadísticas del texto", _contar),
    }

    for comando, (titulo, funcion) in comandos.items():
        if texto_normal.startswith(comando):
            contenido = _obtener_contenido(texto)
            return titulo, funcion(contenido)

    return None
