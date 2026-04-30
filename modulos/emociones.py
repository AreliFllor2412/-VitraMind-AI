from modulos.inteligencia import normalizar


def detectar_emocion(texto):
    texto = normalizar(texto)

    if any(p in texto for p in ["estres", "estresada", "presion", "cansada", "agotada", "burnout"]):
        return "Gestion de energia", """Te escucho, Areli. Si estas saturada, primero bajemos la presion.

Accion corta:
1. Pausa 5 minutos.
2. Escribe el problema en una frase.
3. Elige solo el siguiente paso, no todo el proyecto.

Tu claridad vale mas que avanzar en automatico."""

    if any(p in texto for p in ["triste", "mal", "llorar", "sola", "ansiedad"]):
        return "Apoyo personal", """Siento que estes pasando por esto.

No tienes que resolver todo de golpe. Podemos quedarnos con una cosa pequena:
1. Que paso.
2. Que necesitas ahora.
3. Que accion te devuelve un poco de calma."""

    if any(p in texto for p in ["enojada", "molesta", "frustrada", "coraje"]):
        return "Foco en crisis", """Tiene sentido que te frustre. Vamos a quitarle ruido al problema:

1. Que esperabas que pasara.
2. Que paso realmente.
3. Que cambiaste justo antes.
4. Cual es la prueba minima para confirmar la causa."""

    if any(p in texto for p in ["feliz", "contenta", "motivada", "bien", "excelente"]):
        return "Momentum", """Que bonito leerte asi, Areli. Aprovechemos esa energia:

1. Cierra una tarea pequena.
2. Documenta el avance.
3. Deja preparado el siguiente paso."""

    if any(p in texto for p in ["sueno", "cansancio", "sin ganas"]):
        return "Recuperacion", """Tu cerebro tambien necesita mantenimiento.

Si puedes, toma agua, estirate y descansa unos minutos. Si no puedes parar, reduce la tarea a una sola accion verificable."""

    return None
