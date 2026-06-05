import re
import unicodedata


PALABRAS_ACCION = {
    "crear": "crear algo nuevo",
    "hacer": "construir una solucion",
    "arreglar": "corregir un problema",
    "corregir": "corregir un problema",
    "mejorar": "mejorar calidad o diseno",
    "optimizar": "optimizar rendimiento o claridad",
    "explicar": "explicar paso a paso",
    "resumir": "resumir informacion",
    "ordenar": "ordenar informacion",
    "aumentar": "ampliar capacidades",
    "agregar": "sumar una mejora",
}

CORRECCIONES_COMUNES = {
    "ahcer": "hacer",
    "aser": "hacer",
    "ouedo": "puedo",
    "pudeo": "puedo",
    "poidemos": "podemos",
    "podemso": "podemos",
    "entendiemnto": "entendimiento",
    "poryecto": "proyecto",
    "repsuetsa": "respuesta",
    "pregu8ntas": "preguntas",
    "werb": "web",
    "reac native": "react native",
    "condiseno": "con diseno",
    "qiero": "quiero",
    "nesecito": "necesito",
    "alluda": "ayuda",
}

TEMAS = {
    "react native": ["react native", "expo", "android", "ios", "movil"],
    "diseno": ["diseno", "ui", "interfaz", "pantalla", "visual", "bonito"],
    "datos": ["datos", "memoria", "historial", "contexto", "guardar"],
    "debug": ["error", "bug", "falla", "no funciona", "traceback", "undefined"],
    "seguridad": ["seguridad", "jwt", "token", "password", "owasp"],
    "energia": ["sueno", "cansada", "agotada", "desvelada", "sin energia"],
    "ideas": ["ideas", "agregar", "aumentar", "mejorar", "que podemos"],
}


def normalizar(texto):
    texto = texto.strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = re.sub(r"[¿?¡!.,;:]+", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()

    for original, reemplazo in CORRECCIONES_COMUNES.items():
        texto = re.sub(rf"\b{re.escape(original)}\b", reemplazo, texto)

    return texto


def detectar_intencion(texto):
    limpio = normalizar(texto)
    acciones = [accion for accion in PALABRAS_ACCION if accion in limpio]

    if any(p in limpio for p in ["error", "falla", "bug", "no funciona", "traceback"]):
        return "debug"
    if any(p in limpio for p in ["quiero", "necesito", "ayudame", "puedes"]):
        return "peticion"
    if acciones:
        return "accion"
    if limpio.endswith("?") or limpio.startswith(("que ", "como ", "por que ", "cual ")):
        return "pregunta"
    return "conversacion"


def detectar_temas(texto):
    limpio = normalizar(texto)
    encontrados = []

    for tema, palabras in TEMAS.items():
        if any(palabra in limpio for palabra in palabras):
            encontrados.append(tema)

    return encontrados or ["general"]


def detectar_energia(texto):
    limpio = normalizar(texto)

    if any(p in limpio for p in ["sueno", "cansada", "agotada", "desvelada", "sin energia"]):
        return "baja"
    if any(p in limpio for p in ["urgente", "rapido", "prisa", "ya"]):
        return "alta"
    if any(p in limpio for p in ["ideas", "creativo", "bonito", "diseno"]):
        return "creativa"
    return "media"


def detectar_formato(texto):
    limpio = normalizar(texto)

    if any(p in limpio for p in ["codigo", "code", "programa"]):
        return "codigo"
    if any(p in limpio for p in ["resumen", "corto", "rapido"]):
        return "corto"
    if "ejemplo" in limpio:
        return "ejemplo"
    if any(p in limpio for p in ["plan", "pasos"]):
        return "plan"
    return "acompanado"


def extraer_codigo_o_error(texto):
    lineas = [linea.rstrip() for linea in texto.splitlines()]
    pistas = []

    for linea in lineas:
        normal = normalizar(linea)
        if any(p in normal for p in ["error", "exception", "traceback", "syntax", "undefined", "failed"]):
            pistas.append(linea)

    bloques = re.findall(r"```(.*?)```", texto, flags=re.DOTALL)
    if bloques:
        pistas.extend(b.strip() for b in bloques if b.strip())

    return pistas[:3]


def construir_contexto(memoria):
    if not memoria:
        return "No hay contexto previo en esta sesion."

    ultimos = memoria[-3:]
    return "Contexto reciente:\n" + "\n".join(f"- {item}" for item in ultimos)


def enriquecer_respuesta(texto, titulo, respuesta, memoria):
    intencion = detectar_intencion(texto)
    temas = detectar_temas(texto)
    energia = detectar_energia(texto)
    formato = detectar_formato(texto)
    pistas = extraer_codigo_o_error(texto)
    partes = []

    partes.append(f"Lectura rapida: tema={', '.join(temas[:3])} | energia={energia} | formato={formato}")
    partes.append("")

    if intencion == "debug":
        partes.append("Vamos a volver el error pequeno:")
        partes.append("- Identificar mensaje exacto.")
        partes.append("- Ubicar archivo, linea y cambio reciente.")
        partes.append("- Probar una correccion pequena y verificar.")
        if pistas:
            partes.append("")
            partes.append("Pistas detectadas:")
            partes.extend(f"- {pista}" for pista in pistas)
        partes.append("")

    if intencion in {"peticion", "accion"}:
        if energia == "baja":
            partes.append("Modo suave: vamos con una mini tarea, no con todo el mundo encima.")
        elif energia == "alta":
            partes.append("Modo directo: te doy el siguiente movimiento sin rodeo.")
        else:
            partes.append("Plan conversable:")
        partes.append("- Definir resultado esperado.")
        partes.append("- Separar el trabajo en pasos pequenos.")
        partes.append("- Validar con una prueba o revision final.")
        partes.append("")

    partes.append(respuesta)

    if titulo != "Memoria":
        partes.append("")
        partes.append(construir_contexto(memoria))

    return "\n".join(partes).strip()


def respuesta_general(texto, memoria):
    intencion = detectar_intencion(texto)
    temas = detectar_temas(texto)
    energia = detectar_energia(texto)
    contexto = construir_contexto(memoria)

    if intencion == "pregunta":
        guia = "Te respondo mejor si me das archivo, error u objetivo concreto."
    elif intencion == "debug":
        guia = "Pegame el error completo y revisamos causa, archivo probable y solucion."
    elif energia == "baja":
        guia = "Si vienes cansada, lo bajamos a una mini accion manejable."
    else:
        guia = "Dime que quieres lograr y lo convertimos en algo accionable."

    return f"""Estoy contigo, Areli. {guia}

Lo que estoy entendiendo:
- Temas: {", ".join(temas[:3])}
- Energia: {energia}
- Intencion: {intencion}

Podemos seguir asi:
- Version corta
- Version con ejemplo
- Plan listo para implementar

{contexto}"""
