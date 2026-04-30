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
}

FUNCIONES = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "ceil": math.ceil,
    "floor": math.floor,
}


def evaluar(nodo):
    if isinstance(nodo, ast.Expression):
        return evaluar(nodo.body)
    if isinstance(nodo, ast.Constant) and isinstance(nodo.value, (int, float)):
        return nodo.value
    if isinstance(nodo, ast.BinOp) and type(nodo.op) in OPERADORES:
        return OPERADORES[type(nodo.op)](evaluar(nodo.left), evaluar(nodo.right))
    if isinstance(nodo, ast.UnaryOp) and type(nodo.op) in OPERADORES:
        return OPERADORES[type(nodo.op)](evaluar(nodo.operand))
    if isinstance(nodo, ast.Call) and isinstance(nodo.func, ast.Name) and nodo.func.id in FUNCIONES:
        argumentos = [evaluar(arg) for arg in nodo.args]
        return FUNCIONES[nodo.func.id](*argumentos)

    raise ValueError("Expresion no permitida")


def detectar_calculo(texto):
    texto_normal = normalizar(texto)

    if texto_normal.startswith("calcula"):
        expresion = texto[len("calcula"):].strip().replace("^", "**")

        try:
            arbol = ast.parse(expresion, mode="eval")
            resultado = evaluar(arbol)
            return "Calculadora", f"Resultado: {resultado}"
        except Exception:
            return "Error de calculo", "Expresion no valida. Usa +, -, *, /, %, ** o funciones como sqrt(16)."

    return None
