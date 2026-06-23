from modulos.inteligencia import normalizar


EMOCIONES = {
    "energia": {
        "area": "Gestión de energía",
        "nivel": "alto",
        "keywords": [
            "estres", "estresada", "presion", "cansada", "agotada",
            "burnout", "saturada", "mucho trabajo", "no puedo", "demasiado"
        ],
        "respuesta": """Te escucho. Parece que traes mucha carga encima.

Acción corta:
1. Pausa 5 minutos.
2. Escribe el problema en una sola frase.
3. Elige únicamente el siguiente paso.

No necesitas resolver todo ahorita; sólo ordenar lo inmediato."""
    },
    "tristeza": {
        "area": "Apoyo personal",
        "nivel": "medio",
        "keywords": [
            "triste", "mal", "llorar", "sola", "ansiedad",
            "desanimada", "decepcion", "vacía", "sin ánimo"
        ],
        "respuesta": """Siento que estés pasando por esto.

Vamos poco a poco:
1. Qué pasó.
2. Qué necesitas ahora.
3. Qué acción pequeña puede devolverte un poco de calma.

Estoy contigo para ordenarlo."""
    },
    "frustracion": {
        "area": "Foco en crisis",
        "nivel": "alto",
        "keywords": [
            "enojada", "molesta", "frustrada", "coraje",
            "hartazgo", "fastidio", "me desespera", "no sale"
        ],
        "respuesta": """Tiene sentido que te frustre.

Vamos a quitarle ruido:
1. Qué esperabas que pasara.
2. Qué pasó realmente.
3. Qué cambiaste justo antes.
4. Cuál es la prueba mínima para encontrar la causa."""
    },
    "motivacion": {
        "area": "Momentum",
        "nivel": "positivo",
        "keywords": [
            "feliz", "contenta", "motivada", "bien",
            "excelente", "emocionada", "orgullosa", "avance"
        ],
        "respuesta": """Qué bueno leerte así.

Aprovechemos esa energía:
1. Cierra una tarea pequeña.
2. Documenta el avance.
3. Deja preparado el siguiente paso.

Ese impulso puede convertirse en progreso real."""
    },
    "recuperacion": {
        "area": "Recuperación",
        "nivel": "medio",
        "keywords": [
            "sueno", "sueño", "cansancio", "sin ganas",
            "dormir", "agotamiento", "me pesa"
        ],
        "respuesta": """Tu cerebro también necesita mantenimiento.

Si puedes:
1. Toma agua.
2. Estírate.
3. Descansa unos minutos.

Si no puedes parar, reduce la tarea a una sola acción verificable."""
    },
}


def detectar_emocion(texto):
    texto = normalizar(texto)

    coincidencias = []

    for emocion, config in EMOCIONES.items():
        score = sum(1 for palabra in config["keywords"] if palabra in texto)

        if score > 0:
            coincidencias.append({
                "emocion": emocion,
                "area": config["area"],
                "nivel": config["nivel"],
                "score": score,
                "respuesta": config["respuesta"],
            })

    if not coincidencias:
        return None

    coincidencias.sort(key=lambda item: item["score"], reverse=True)

    principal = coincidencias[0]

    return principal["area"], principal["respuesta"]


def analizar_emocion(texto):
    texto = normalizar(texto)

    resultados = []

    for emocion, config in EMOCIONES.items():
        score = sum(1 for palabra in config["keywords"] if palabra in texto)

        if score > 0:
            resultados.append({
                "emocion": emocion,
                "area": config["area"],
                "nivel": config["nivel"],
                "score": score,
            })

    resultados.sort(key=lambda item: item["score"], reverse=True)

    return resultados
