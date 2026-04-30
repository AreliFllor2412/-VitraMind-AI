import os
import sys

from config import NOMBRE_IA, NOMBRE_USUARIO
from modulos.archivos import detectar_archivo
from modulos.calculadora import detectar_calculo
from modulos.devops import detectar_devops
from modulos.emociones import detectar_emocion
from modulos.git import detectar_git
from modulos.horarios import detectar_horario
from modulos.inteligencia import enriquecer_respuesta, normalizar, respuesta_general
from modulos.memoria import guardar_historial, guardar_memoria, obtener_memoria, ver_memoria
from modulos.programacion import detectar_programacion
from modulos.proyectos import detectar_proyecto
from modulos.prompts import detectar_prompt
from modulos.sql import detectar_sql
from modulos.tareas import detectar_tareas
from modulos.texto import detectar_texto
from security import detectar_seguridad


class UI:
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    DIM = "\033[2m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    SEP = "-" * 60


MODULOS = [
    ("Emocion", detectar_emocion, 95),
    ("Programacion", detectar_programacion, 90),
    ("SQL", detectar_sql, 88),
    ("Seguridad", detectar_seguridad, 86),
    ("Git", detectar_git, 82),
    ("DevOps", detectar_devops, 80),
    ("Proyecto", detectar_proyecto, 76),
    ("Horario", detectar_horario, 72),
    ("Prompt", detectar_prompt, 70),
    ("Tareas", detectar_tareas, 68),
    ("Calculadora", detectar_calculo, 66),
    ("Archivos", detectar_archivo, 64),
    ("Texto", detectar_texto, 62),
]


def configurar_terminal():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdin.reconfigure(encoding="utf-8")
    except AttributeError:
        pass


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def mostrar_inicio():
    limpiar()
    print(f"{UI.BLUE}+{'-' * 78}+{UI.RESET}")
    print(f"{UI.BLUE}| {UI.BOLD}{NOMBRE_IA.center(76)}{UI.RESET}{UI.BLUE} |{UI.RESET}")
    print(f"{UI.BLUE}+{'-' * 78}+{UI.RESET}")
    print(f"\n {UI.GREEN}OK{UI.RESET} {UI.BOLD}System Online{UI.RESET} | User: {UI.CYAN}{NOMBRE_USUARIO}{UI.RESET}")
    print(f" {UI.DIM}Asistente tecnico y personal v3.0 cargado.{UI.RESET}\n")

    categorias = {
        "Soft Skills & Management": ["Mindset y emociones", "Horarios", "Backlog y tareas"],
        "Backend & DB Engine": ["Programacion", "SQL", "DevOps e infraestructura"],
        "Security & Engineering": ["CyberSecurity", "Prompts", "Calculadora"],
        "Workflow": ["Proyectos", "Archivos y notas", "Git"],
    }

    for categoria, items in categorias.items():
        print(f"  {UI.BOLD}{UI.BLUE}{categoria}{UI.RESET}")
        for item in items:
            print(f"     {UI.DIM}- {UI.RESET}{item}")
        print()

    print(f"{UI.BLUE}{'-' * 80}{UI.RESET}")
    print(f" {UI.YELLOW}Comandos:{UI.RESET} {UI.DIM}ayuda | memoria | limpiar | salir{UI.RESET}")
    print(f"{UI.BLUE}{'-' * 80}{UI.RESET}")


def mostrar_panel(titulo, contenido):
    print(f"\n{UI.CYAN}{UI.BOLD}{titulo.upper()}{UI.RESET}")
    print(f"{UI.CYAN}{UI.SEP}{UI.RESET}")
    for linea in contenido.split("\n"):
        print(f"{UI.CYAN}|{UI.RESET} {linea}")
    print(f"{UI.CYAN}{UI.SEP}{UI.RESET}\n")


def ayuda():
    return """Escribeme de forma natural. Puedo ayudarte a:

1. Debugear errores de Python, Laravel, React, Vite, SQL o Git.
2. Crear tareas con: tarea: texto de la tarea
3. Guardar notas con: crear nota texto de la nota
4. Leer notas con: leer nota
5. Calcular con: calcula 10 * (5 + 2)
6. Resumir con: resume: texto largo
7. Ordenar con: ordena: punto uno, punto dos, punto tres

Tip: si pegas un error completo, intentare armar un diagnostico antes de responder."""


def ejecutar_modulos(texto):
    respuestas = []

    for etiqueta, funcion, prioridad in MODULOS:
        resultado = funcion(texto)
        if resultado:
            titulo_area, respuesta_area = resultado
            respuestas.append((prioridad, etiqueta, titulo_area, respuesta_area))

    respuestas.sort(reverse=True, key=lambda item: item[0])
    return respuestas


def responder(texto):
    texto_limpio = normalizar(texto)

    if not texto_limpio:
        return "Mensaje vacio", "Escribe algo para poder ayudarte."

    if texto_limpio == "ayuda":
        return "Ayuda", ayuda()

    if texto_limpio == "memoria":
        return "Memoria", ver_memoria()

    respuestas = ejecutar_modulos(texto)

    if respuestas:
        contenido = []
        for _, area, titulo_area, respuesta_area in respuestas[:4]:
            contenido.append(f"{UI.BOLD}{area}{UI.RESET} > {UI.CYAN}{titulo_area}{UI.RESET}")
            contenido.append(respuesta_area)
            contenido.append(f"{UI.DIM}{'-' * 58}{UI.RESET}")

        respuesta = "\n".join(contenido).strip()
        return "Respuesta inteligente", enriquecer_respuesta(
            texto,
            "Respuesta inteligente",
            respuesta,
            obtener_memoria(),
        )

    if "hola" in texto_limpio:
        return "Saludo", (
            "Hola Areli. Que gusto verte por aqui. "
            "Estoy lista para ayudarte con codigo, tareas, ideas o debugging."
        )

    return "Recomendacion general", respuesta_general(texto, obtener_memoria())


def main():
    configurar_terminal()
    mostrar_inicio()

    while True:
        mensaje = input(f"{UI.GREEN}> {UI.BOLD}{NOMBRE_USUARIO}@DevShell{UI.RESET} {UI.DIM}$ {UI.RESET}")
        comando = normalizar(mensaje)

        if comando == "salir":
            print(f"\n{UI.YELLOW}Cerrando sesion. Historial guardado. Hasta luego, Areli.{UI.RESET}")
            break

        if comando == "limpiar":
            mostrar_inicio()
            continue

        guardar_memoria(mensaje)
        titulo, respuesta = responder(mensaje)
        mostrar_panel(titulo, respuesta)
        guardar_historial(mensaje, respuesta)


if __name__ == "__main__":
    main()
