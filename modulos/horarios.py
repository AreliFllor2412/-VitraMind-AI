import re
from datetime import datetime, timedelta

from modulos.inteligencia import normalizar


def convertir_hora(hora):
    try:
        return datetime.strptime(hora, "%H:%M")
    except ValueError:
        return None


def detectar_horario(texto):
    texto_original = texto
    texto = normalizar(texto)

    if not any(
        palabra in texto
        for palabra in ["hora", "horario", "entro", "entre", "salgo", "salida"]
    ):
        return None

    horas = re.findall(r"\d{1,2}:\d{2}", texto_original)

    if len(horas) >= 2:
        inicio = convertir_hora(horas[0])
        duracion = convertir_hora(horas[1])

        if inicio and duracion:
            salida = inicio + timedelta(
                hours=duracion.hour,
                minutes=duracion.minute,
            )

            return (
                "Horario calculado",
                f"""Hora de entrada: {horas[0]}
Horas a cumplir: {horas[1]}

Salida estimada:
{salida.strftime("%H:%M")}"""
            )

    return (
        "Horario",
        """Puedo ayudarte a calcular horarios.

Ejemplos:

entre 08:30 y debo cumplir 09:45

entro 07:00 y trabajo 08:30

entrare 09:15 y debo cumplir 10:00

También puedo calcular horas extra y tiempos restantes en futuras versiones."""
    )
