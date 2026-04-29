def detectar_texto(texto):
    texto_lower = texto.lower()

    if texto_lower.startswith("resume:"):
        contenido = texto.replace("resume:", "").strip()
        palabras = contenido.split()

        resumen = " ".join(palabras[:25])

        return "Resumen rápido", resumen + "..."

    if texto_lower.startswith("ordena:"):
        contenido = texto.replace("ordena:", "").strip()
        partes = [p.strip() for p in contenido.split(",")]

        resultado = ""
        for i, parte in enumerate(partes, start=1):
            resultado += f"{i}. {parte}\n"

        return "Texto ordenado", resultado

    return None