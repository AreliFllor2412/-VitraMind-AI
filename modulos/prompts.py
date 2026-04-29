def detectar_prompt(texto):
    texto = texto.lower()

    if "prompt" in texto:
        return "Prompt profesional", """Estructura recomendada:

Actúa como [rol].
Necesito mejorar [módulo/vista].
Respeta estas reglas:
- no cambiar lógica
- no cambiar rutas
- no cambiar variables
- solo diseño

Estilo:
- profesional
- moderno
- limpio
- accesible

Entrega:
- código completo
- listo para copiar y pegar
"""

    return None