def detectar_emocion(texto):
    texto = texto.lower()

    if any(p in texto for p in ["estres", "estresada", "presion", "cansada", "agotada"]):
        return "Gestión de Energía", "Te escucho, Areli. El burnout no es broma y el código puede esperar. \nSuelta el teclado 5 minutos, respira y estírate. Recuerda: eres una gran programadora, pero primero eres humana. ¡Tu paz mental es el mejor debug!"

    if any(p in texto for p in ["triste", "mal", "llorar", "sola"]):
        return "Apoyo Personal", "Siento mucho que estés pasando por esto, Areli. \nA veces el mundo del dev se siente solitario, pero aquí estoy contigo. Tómate el tiempo que necesites; el código no define tu valor. Estoy aquí para lo que quieras contarme."

    if any(p in texto for p in ["enojada", "molesta", "frustrada", "coraje"]):
        return "Foco en Crisis", "¡Ese bug no va a poder contigo, Areli! \nSé que da coraje cuando las cosas no salen, pero esa frustración es solo señal de que estás a punto de aprender algo grande. Vamos a darle una vuelta juntas con calma."

    if any(p in texto for p in ["feliz", "contenta", "motivada", "bien", "excelente"]):
        return "Peak Performance", "¡Qué alegría leer eso, Areli! 🚀 \nEsa energía de 'Senior' es contagiosa. Aprovecha este momento de flow para conquistar esos retos que tenías pendientes. ¡A darle con todo!"

    if any(p in texto for p in ["sueño", "cansancio", "sin ganas", "agotada"]):
        return "Optimización Humana", "Tu cerebro es tu herramienta más potente, Areli, pero hasta los mejores servidores necesitan mantenimiento. \nSi tienes sueño, descansa un poco. Un café o una siesta corta harán que tu lógica brille mucho más después."

    return None