def detectar_horario(texto):
    texto = texto.lower()

    if "hora" in texto or "salgo" in texto or "entro" in texto:
        return "Cálculo de horario", """Puedo ayudarte a calcular horarios.

Ejemplo:
Si entras 8:30 y debes cumplir 9 horas 45 minutos:
Salida aproximada: 6:15, considerando comida según tu regla.

Escríbeme:
'entré 8:30 y debo cumplir 9:45'
"""

    return None