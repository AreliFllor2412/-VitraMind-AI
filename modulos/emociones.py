def detectar_emocion(texto):
    texto = texto.lower()

    if any(p in texto for p in ["estres", "estresada", "presion", "cansada", "agotada"]):
        return "Gestión de Energía", "Entiendo perfectamente, Areli. El burnout es real en el desarrollo. \nSuelta el teclado 5 minutos, camina, hidrátate y recuerda: ningún bug es más importante que tu paz mental. Considera una técnica Pomodoro."

    if any(p in texto for p in ["triste", "mal", "llorar", "sola"]):
        return "Apoyo Personal", "Siento que te sientas así. A veces programar puede ser solitario. \nRecuerda que el código es solo una parte; tu bienestar es prioridad. Estoy aquí para procesar lo que necesites, no eres solo una programadora, eres humana."

    if any(p in texto for p in ["enojada", "molesta", "frustrada", "coraje"]):
        return "Foco en Crisis", "La frustración es el combustible del aprendizaje, Areli. \nEse error de Laravel o React va a caer. Respira profundo, vamos a revisarlo juntas paso a paso. A veces, un pequeño descanso y una nueva perspectiva lo resuelven."

    if any(p in texto for p in ["feliz", "contenta", "motivada", "bien", "excelente"]):
        return "Peak Performance", "¡Esa es la actitud de una Senior, Areli! \nAprovecha este estado de 'flow' para resolver los tickets más complejos del backlog ahora mismo. ¡Mantén esa energía!"

    if any(p in texto for p in ["sueño", "cansancio", "sin ganas", "agotada"]):
        return "Optimización Humana", "Tu cerebro es tu hardware más valioso. Si tiene poca batería, el código saldrá con errores. \nToma una siesta, hidrátate o estírate. El código seguirá aquí cuando vuelvas, y tú estarás más eficiente."

    return None