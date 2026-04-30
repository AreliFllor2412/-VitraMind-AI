from modulos.inteligencia import normalizar


def detectar_texto(texto):
    texto_normal = normalizar(texto)

    if texto_normal.startswith("resume:"):
        contenido = texto.split(":", 1)[1].strip()
        palabras = contenido.split()
        resumen = " ".join(palabras[:35])

        if len(palabras) > 35:
            resumen += "..."

        return "Resumen rapido", resumen or "No encontre texto para resumir."

    if texto_normal.startswith("ordena:"):
        contenido = texto.split(":", 1)[1].strip()
        partes = [p.strip() for p in contenido.split(",") if p.strip()]

        if not partes:
            return "Texto ordenado", "No encontre elementos separados por coma."

        resultado = "\n".join(f"{i}. {parte}" for i, parte in enumerate(partes, start=1))
        return "Texto ordenado", resultado

    return None
