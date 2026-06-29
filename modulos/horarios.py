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
    """
    Convierte texto tipo 8:30 o 08:30 a datetime.
    """
    try:
        return datetime.strptime(hora.zfill(5), "%H:%M")
    except ValueError:
        return None


def formatear_timedelta(delta):
    """
    Convierte un timedelta a formato HH:MM.
    """
    total_minutos = int(delta.total_seconds() // 60)
    horas = total_minutos // 60
    minutos = total_minutos % 60

    return f"{horas:02d}:{minutos:02d}"


def extraer_horas(texto):
    """
    Extrae horas tipo:
    8:30
    08:30
    18:15
    """
    return re.findall(r"\b\d{1,2}:\d{2}\b", texto)


def extraer_comida(texto):
    """
    Detecta comida/descanso en formato:
    comida 1 hora
    comida 60 minutos
    descanso 00:30
    """
    texto_normal = normalizar(texto)

    hora_match = re.search(r"(comida|descanso).*?(\d{1,2}:\d{2})", texto_normal)
    if hora_match:
        hora = convertir_hora(hora_match.group(2))
        if hora:
            return timedelta(hours=hora.hour, minutes=hora.minute)

    horas_match = re.search(r"(comida|descanso).*?(\d+)\s*(hora|horas)", texto_normal)
    if horas_match:
        return timedelta(hours=int(horas_match.group(2)))

    minutos_match = re.search(r"(comida|descanso).*?(\d+)\s*(min|minuto|minutos)", texto_normal)
    if minutos_match:
        return timedelta(minutes=int(minutos_match.group(2)))

    return timedelta()


def calcular_salida(inicio, duracion, comida=None):
    comida = comida or timedelta()
    return inicio + timedelta(hours=duracion.hour, minutes=duracion.minute) + comida


def calcular_diferencia(inicio, fin):
    """
    Calcula diferencia entre dos horas.
    Si la salida es menor que entrada, asume que salió al día siguiente.
    """
    if fin < inicio:
        fin += timedelta(days=1)

    return fin - inicio


def detectar_horario(texto):
    texto_original = texto
    texto_normal = normalizar(texto)

    if not any(palabra in texto_normal for palabra in PALABRAS_HORARIO):
        return None

    horas = extraer_horas(texto_original)
    comida = extraer_comida(texto_original)

    if len(horas) >= 2:
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

        pregunta_diferencia = any(
            palabra in texto_normal
            for palabra in [
                "cuantas horas",
                "cuántas horas",
                "de",
                "hasta",
                "salgo a",
                "salida a",
            ]
        )

        pregunta_salida = any(
            palabra in texto_normal
            for palabra in [
                "cumplir",
                "trabajo",
                "debo",
                "jornada",
                "turno",
            ]
        )

        if pregunta_diferencia and not pregunta_salida:
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

    return (
        "Horario",
        """Puedo ayudarte a calcular horarios.

Ejemplos:

entro 08:30 y debo cumplir 09:45

entro 07:00 y trabajo 08:30

entre 09:15 y debo cumplir 10:00

entro 08:30, comida 1 hora y debo cumplir 09:45

cuantas horas son de 08:30 a 18:15

También puedo ayudarte a calcular salida, horas trabajadas y descansos."""
    )
