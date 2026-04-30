from modulos.inteligencia import normalizar


def detectar_horario(texto):
    texto = normalizar(texto)

    if "hora" in texto or "salgo" in texto or "entro" in texto or "horario" in texto:
        return "Horario", """Puedo ayudarte a calcular horarios.

Ejemplo:
Si entras 8:30 y debes cumplir 9 horas 45 minutos,
la salida aproximada seria 18:15 si no cuentas comida.

Escribeme algo como:
entre 8:30 y debo cumplir 9:45"""

    return None
