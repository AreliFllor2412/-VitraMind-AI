import re
from datetime import datetime, timedelta

from modulos.inteligencia import normalizar


PALABRAS_HORARIO = [
    "hora",
    "horario",
    "entro",
    "entre",
    "entrada",
    "salgo",
    "salida",
    "cumplir",
    "trabajo",
    "turno",
    "jornada",
    "comida",
    "descanso",
    "faltan",
    "restan",
]


def convertir_hora(hora):
    try:
        partes = hora.strip().split(":")
        hora_formateada = f"{int(partes[0]):02d}:{int(partes[1]):02d}"
        return datetime.strptime(hora_formateada, "%H:%M")
    except (ValueError, IndexError):
        return None


def formatear_timedelta(delta):
    total_minutos = int(delta.total_seconds() // 60)
    horas = total_minutos // 60
    minutos = total_minutos % 60
    return f"{horas:02d}:{minutos:02d}"


def extraer_horas(texto):
    return re.findall(r"\b\d{1,2}:\d{1,2}\b", texto)


def extraer_comida(texto):
    texto_normal = normalizar(texto)

    if not any(p in texto_normal for p in ["comida", "descanso"]):
        return timedelta()

    hora_match = re.search(
        r"(comida|descanso).*?(\d{1,2}:\d{1,2})",
        texto_normal,
    )

    if hora_match:
        hora = convertir_hora(hora_match.group(2))
        if hora:
            return timedelta(hours=hora.hour, minutes=hora.minute)

    horas_match = re.search(
        r"(comida|descanso).*?(\d+)\s*(hora|horas|hr|hrs)",
        texto_normal,
    )

    if horas_match:
        return timedelta(hours=int(horas_match.group(2)))

    minutos_match = re.search(
        r"(comida|descanso).*?(\d+)\s*(min|minuto|minutos)",
        texto_normal,
    )

    if minutos_match:
        return timedelta(minutes=int(minutos_match.group(2)))

    return timedelta()


def calcular_salida(inicio, duracion, comida=None):
    comida = comida or timedelta()
    return inicio + timedelta(hours=duracion.hour, minutes=duracion.minute) + comida


def calcular_diferencia(inicio, fin):
    if fin < inicio:
        fin += timedelta(days=1)

    return fin - inicio


def es_pregunta_diferencia(texto_normal):
    palabras = [
        "cuantas horas",
        "cuántas horas",
        "cuanto tiempo",
        "cuánto tiempo",
        "de",
        "hasta",
        "salgo a",
        "salida a",
    ]

    return any(p in texto_normal for p in palabras)


def es_pregunta_salida(texto_normal):
    palabras = [
        "cumplir",
        "trabajo",
        "debo",
        "jornada",
        "turno",
        "a que hora salgo",
        "a qué hora salgo",
    ]

    return any(p in texto_normal for p in palabras)


def detectar_horario(texto):
    texto_normal = normalizar(texto)

    if not any(palabra in texto_normal for palabra in PALABRAS_HORARIO):
        return None

    horas = extraer_horas(texto)
    comida = extraer_comida(texto)

    if len(horas) < 2:
        return (
            "Horario",
            """Puedo ayudarte a calcular horarios.

Ejemplos:

entro 08:30 y debo cumplir 09:45
entro 7:00 y trabajo 8:30
entre 09:15 y debo cumplir 10:00
entro 08:30, comida 1 hora y debo cumplir 09:45
cuantas horas son de 08:30 a 18:15

Usa formato HH:MM para que pueda calcularlo bien."""
        )

    primera = convertir_hora(horas[0])
    segunda = convertir_hora(horas[1])

    if not primera or not segunda:
        return (
            "Horario inválido",
            """No pude leer bien una de las horas.

Usa formato HH:MM.

Ejemplos:
08:30
8:30
18:15"""
        )

    if es_pregunta_diferencia(texto_normal) and not es_pregunta_salida(texto_normal):
        diferencia = calcular_diferencia(primera, segunda)

        return (
            "Horas calculadas",
            f"""Entrada: {horas[0]}
Salida: {horas[1]}

Tiempo trabajado:
{formatear_timedelta(diferencia)}"""
        )

    salida = calcular_salida(primera, segunda, comida)

    respuesta = f"""Hora de entrada: {horas[0]}
Horas a cumplir: {horas[1]}"""

    if comida.total_seconds() > 0:
        respuesta += f"""

Tiempo de comida/descanso:
{formatear_timedelta(comida)}"""

    respuesta += f"""

Salida estimada:
{salida.strftime("%H:%M")}"""

    return "Horario calculado", respuesta
