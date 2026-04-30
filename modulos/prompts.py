from modulos.inteligencia import normalizar


def detectar_prompt(texto):
    texto = normalizar(texto)

    if "prompt" in texto:
        return "Prompt profesional", """Estructura recomendada:

Actua como [rol].
Necesito [objetivo concreto].
Contexto:
- [framework/proyecto]
- [archivo o modulo]
- [restricciones]

Reglas:
- conserva la logica existente
- respeta nombres y rutas
- explica cambios importantes

Entrega:
- solucion lista para usar
- pasos de verificacion"""

    return None
