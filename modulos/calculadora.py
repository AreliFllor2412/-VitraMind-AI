import math

def detectar_calculo(texto):
    texto = texto.lower()

    if texto.startswith("calcula"):
        expresion = texto.replace("calcula", "").strip()

        # Diccionario de funciones permitidas para mayor seguridad que un eval puro
        safe_dict = {"__builtins__": None, "math": math}
        # Permitimos operadores básicos y funciones de math
        # Nota: En un entorno real, usar un parser de expresiones es lo ideal.
        try:
            # Reemplazamos ^ por ** para potencia común en programación
            resultado = eval(expresion.replace("^", "**"), safe_dict, {})
            return "Calculadora", f"Resultado técnico: {resultado}"
        except:
            return "Error de Cálculo", "Expresión no válida. Usa operadores estándar: +, -, *, /, **"

    return None