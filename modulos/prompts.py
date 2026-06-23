from modulos.inteligencia import normalizar


PROMPTS = {
    "programacion": {
        "keywords": ["codigo", "programacion", "react", "python", "laravel", "firebase", "error"],
        "titulo": "Prompt profesional para programación",
        "respuesta": """Actúa como desarrollador senior.

Necesito [objetivo concreto].

Contexto:
- Proyecto: [nombre del proyecto]
- Framework: [React / Laravel / Firebase / Python]
- Archivo o módulo: [ruta o nombre]
- Error o mejora: [describe el problema]

Reglas:
- Conserva la lógica existente.
- Respeta nombres, rutas y estructura.
- No elimines funciones necesarias.
- Explica los cambios importantes.

Entrega:
- Código listo para usar.
- Pasos de verificación.
- Posibles errores a revisar."""
    },
    "ux": {
        "keywords": ["diseño", "ux", "ui", "interfaz", "pantalla", "dashboard"],
        "titulo": "Prompt profesional para UX/UI",
        "respuesta": """Actúa como diseñador UX/UI senior.

Necesito mejorar esta interfaz.

Contexto:
- Tipo de sistema: [web / móvil / dashboard]
- Usuario objetivo: [administrador / empleado / cliente]
- Problema visual: [se ve cargado / poco claro / informal]

Reglas:
- Mantén un diseño limpio y profesional.
- Mejora jerarquía visual.
- Usa colores sobrios.
- Prioriza legibilidad y facilidad de uso.

Entrega:
- Propuesta visual.
- Componentes mejorados.
- Explicación corta de los cambios."""
    },
    "general": {
        "keywords": ["prompt", "ayuda", "consulta", "pregunta"],
        "titulo": "Prompt profesional",
        "respuesta": """Actúa como [rol].

Necesito [objetivo concreto].

Contexto:
- [proyecto o situación]
- [archivo, módulo o problema]
- [restricciones importantes]

Reglas:
- Sé claro y directo.
- Conserva lo que ya funciona.
- Explica cambios importantes.
- Evita respuestas genéricas.

Entrega:
- Solución lista para usar.
- Pasos de verificación.
- Recomendaciones finales."""
    },
}


def detectar_prompt(texto):
    texto_normal = normalizar(texto)

    if "prompt" not in texto_normal:
        return None

    for config in PROMPTS.values():
        if any(keyword in texto_normal for keyword in config["keywords"]):
            return config["titulo"], config["respuesta"]

    return PROMPTS["general"]["titulo"], PROMPTS["general"]["respuesta"]
