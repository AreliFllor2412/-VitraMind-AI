import ast
import math
import operator

from modulos.inteligencia import normalizar


OPERADORES_BINARIOS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

OPERADORES_UNARIOS = {
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

FUNCIONES = {
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "log": math.log,
    "log10": math.log10,
    "ln": math.log,
    "ceil": math.ceil,
    "floor": math.floor,
    "round": round,
    "abs": abs,
    "pow": pow,
    "min": min,
    "max": max,
}

CONSTANTES = {
    "pi": math.pi,
    "e": math.e,
}

MAX_EXPONENTE = 1000
MAX_LONGITUD_EXPRESION = 200
MAX_ARGUMENTOS = 10


def _normalizar_expresion(expresion):
    return (
        expresion.strip()
        .replace("^", "**")
        .replace("×", "*")
        .replace("÷", "/")
    )


def _validar_numero(valor):
    if not isinstance(valor, (int, float)):
        raise ValueError("Solo se permiten números.")

    if not math.isfinite(valor):
        raise ValueError("El resultado no es válido.")

    return valor


def evaluar(nodo):
    if isinstance(nodo, ast.Expression):
        return evaluar(nodo.body)

    if isinstance(nodo, ast.Constant) and isinstance(nodo.value, (int, float)):
        return _validar_numero(nodo.value)

    if isinstance(nodo, ast.Name):
        if nodo.id in CONSTANTES:
            return CONSTANTES[nodo.id]

        raise ValueError(f"Constante no permitida: {nodo.id}")

    if isinstance(nodo, ast.BinOp) and type(nodo.op) in OPERADORES_BINARIOS:
        izquierda = evaluar(nodo.left)
        derecha = evaluar(nodo.right)

        if isinstance(nodo.op, (ast.Div, ast.FloorDiv, ast.Mod)) and derecha == 0:
            raise ValueError("No se puede dividir entre cero.")

        if isinstance(nodo.op, ast.Pow) and abs(derecha) > MAX_EXPONENTE:
            raise ValueError("El exponente es demasiado grande.")

        resultado = OPERADORES_BINARIOS[type(nodo.op)](izquierda, derecha)
        return _validar_numero(resultado)

    if isinstance(nodo, ast.UnaryOp) and type(nodo.op) in OPERADORES_UNARIOS:
        resultado = OPERADORES_UNARIOS[type(nodo.op)](evaluar(nodo.operand))
        return _validar_numero(resultado)

    if isinstance(nodo, ast.Call) and isinstance(nodo.func, ast.Name):
        nombre_funcion = nodo.func.id

        if nombre_funcion not in FUNCIONES:
            raise ValueError(f"Función no permitida: {nombre_funcion}")

        if nodo.keywords:
            raise ValueError("No se permiten argumentos con nombre.")

        if len(nodo.args) > MAX_ARGUMENTOS:
            raise ValueError("Demasiados argumentos.")

        argumentos = [evaluar(arg) for arg in nodo.args]
        resultado = FUNCIONES[nombre_funcion](*argumentos)

        return _validar_numero(resultado)

    raise ValueError("Expresión no permitida.")


def _formatear_resultado(resultado):
    if isinstance(resultado, float) and resultado.is_integer():
        return str(int(resultado))

    if isinstance(resultado, float):
        return f"{resultado:.10g}"

    return str(resultado)


def detectar_calculo(texto):
    texto_normal = normalizar(texto)

    comandos = ("calcula", "calcular", "resultado de", "cuanto es", "cuánto es")

    if not texto_normal.startswith(comandos):
        return None

    expresion = texto

    for comando in comandos:
        if texto_normal.startswith(comando):
            expresion = texto[len(comando):].strip()
            break

    expresion = _normalizar_expresion(expresion)

    if not expresion:
        return "Error de cálculo", "Escribe una operación. Ejemplo: calcula 8 * 5."

    if len(expresion) > MAX_LONGITUD_EXPRESION:
        return "Error de cálculo", "La operación es demasiado larga."

    try:
        arbol = ast.parse(expresion, mode="eval")
        resultado = evaluar(arbol)

        return "Calculadora", f"Resultado: {_formatear_resultado(resultado)}"

    except Exception as error:
        return "Error de cálculo", f"Expresión no válida: {error}"
