import ast
import math
import operator

from modulos.inteligencia import normalizar


OPERADORES = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

FUNCIONES = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "log10": math.log10,
    "ceil": math.ceil,
    "floor": math.floor,
    "round": round,
    "abs": abs,
}

CONSTANTES = {
    "pi": math.pi,
    "e": math.e,
}

MAX_EXPONENTE = 1000


def evaluar(nodo):
    if isinstance(nodo, ast.Expression):
        return evaluar(nodo.body)

    if isinstance(nodo, ast.Constant) and isinstance(nodo.value, (int, float)):
        return nodo.value

    if isinstance(nodo, ast.Name) and nodo.id in CONSTANTES:
        return CONSTANTES[nodo.id]

    if isinstance(nodo, ast.BinOp) and type(nodo.op) in OPERADORES:
        izquierda = evaluar(nodo.left)
        derecha = evaluar(nodo.right)

        if isinstance(nodo.op, ast.Div) and derecha == 0:
            raise ValueError("No se puede dividir entre cero.")

        if isinstance(nodo.op, ast.Pow) and abs(derecha) > MAX_EXPONENTE:
            raise ValueError("El exponente es demasiado grande.")

        return OPERADORES[type(nodo.op)](izquierda, derecha)

    if isinstance(nodo, ast.UnaryOp) and type(nodo.op) in OPERADORES:
        return OPERADORES[type(nodo.op)](evaluar(nodo.operand))

    if isinstance(nodo, ast.Call) and isinstance(nodo.func, ast.Name):
        nombre_funcion = nodo.func.id

        if nombre_funcion not in FUNCIONES:
            raise ValueError("Función no permitida.")

        if nodo.keywords:
            raise ValueError("No se permiten argumentos con nombre.")

        argumentos = [evaluar(arg) for arg in nodo.args]
        return FUNCIONES[nombre_funcion](*argumentos)

    raise ValueError("Expresión no permitida.")


def detectar_calculo(texto):
    texto_normal = normalizar(texto)

    if not texto_normal.startswith("calcula"):
        return None

    expresion = texto[len("calcula"):].strip().replace("^", "**")

    if not expresion:
        return "Error de cálculo", "Escribe una operación. Ejemplo: calcula 8 * 5."

    try:
        arbol = ast.parse(expresion, mode="eval")
        resultado = evaluar(arbol)

        if isinstance(resultado, float) and resultado.is_integer():
            resultado = int(resultado)

        return "Calculadora", f"Resultado: {resultado}"

    except Exception as error:
        return "Error de cálculo", f"Expresión no válida: {error}"
