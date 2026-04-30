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
}


def normalizar(texto):
    texto = texto.strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
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
    pistas = extraer_codigo_o_error(texto)
    partes = []

    if intencion == "debug":
        partes.append("Diagnostico rapido:")
        partes.append("1. Identificar mensaje exacto del error.")
        partes.append("2. Ubicar archivo, linea y cambio reciente.")
        partes.append("3. Probar una correccion pequena y verificar.")
        if pistas:
            partes.append("")
            partes.append("Pistas detectadas:")
            partes.extend(f"- {pista}" for pista in pistas)
        partes.append("")

    if intencion in {"peticion", "accion"}:
        partes.append("Plan sugerido:")
        partes.append("1. Definir el resultado esperado.")
        partes.append("2. Separar el trabajo en pasos pequenos.")
        partes.append("3. Validar con una prueba o revision final.")
        partes.append("")

    partes.append(respuesta)

    if titulo != "Memoria":
        partes.append("")
        partes.append(construir_contexto(memoria))

    return "\n".join(partes).strip()


def respuesta_general(texto, memoria):
    intencion = detectar_intencion(texto)
    contexto = construir_contexto(memoria)

    if intencion == "pregunta":
        guia = "Puedo ayudarte mejor si me das el archivo, el error o el objetivo concreto."
    elif intencion == "debug":
        guia = "Pegame el error completo y revisamos causa, archivo probable y solucion."
    else:
        guia = "Dime que quieres lograr y lo convertimos en pasos claros."

    return f"""Estoy contigo, Areli. {guia}

Ruta de trabajo:
1. Objetivo
2. Contexto actual
3. Problema o restriccion
4. Siguiente accion
5. Verificacion

{contexto}"""
