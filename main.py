import os

from config import NOMBRE_IA, NOMBRE_USUARIO

from modulos.emociones import detectar_emocion
from modulos.programacion import detectar_programacion
from modulos.proyectos import detectar_proyecto
from modulos.recomendaciones import recomendacion_general
from modulos.memoria import guardar_memoria, ver_memoria, guardar_historial
from modulos.git import detectar_git
from modulos.horarios import detectar_horario
from modulos.prompts import detectar_prompt
from modulos.sql import detectar_sql
from modulos.devops import detectar_devops # Nuevo módulo
from security import detectar_seguridad # Corregido: security.py está en la raíz
from modulos.tareas import detectar_tareas
from modulos.calculadora import detectar_calculo
from modulos.archivos import detectar_archivo
from modulos.texto import detectar_texto

# Configuración de Estética Profesional
class UI:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DIM = '\033[2m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    SEP = "━" * 60

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_inicio():
    limpiar()
    print(f"{UI.BLUE}┏" + "━" * 78 + "┓")
    print(f"┃ {UI.BOLD}{NOMBRE_IA.center(76)}{UI.RESET}{UI.BLUE} ┃")
    print(f"┗" + "━" * 78 + f"┛{UI.RESET}")
    print(f"\n {UI.GREEN}✔{UI.RESET} {UI.BOLD}System Online{UI.RESET} | User: {UI.CYAN}{NOMBRE_USUARIO}{UI.RESET}")
    print(f" {UI.DIM}Engineering Toolset v2.5 cargado.{UI.RESET}\n")

    categorias = {
        "Soft Skills & Management": ["Mindset & Emociones", "Schedule Ops", "Backlog/Tareas"],
        "Backend & DB Engine": ["Core Programming", "Database Engine", "DevOps & Infra"],
        "Security & Engineering": ["CyberSecurity", "Advanced Prompts", "Engineering Calc"],
        "Frontend & Workflow": ["Fullstack Ecosystem", "UI/UX Strategy", "Version Control (Git)"]
    }

    for cat, items in categorias.items():
        print(f"  {UI.BOLD}{UI.BLUE}📂 {cat}{UI.RESET}")
        for i in range(0, len(items), 2):
            col1 = f"{UI.DIM}•{UI.RESET} {items[i]}".ljust(45)
            col2 = f"{UI.DIM}•{UI.RESET} {items[i+1]}" if i+1 < len(items) else ""
            print(f"     {col1} {col2}")
        print()

    print(f"{UI.BLUE}{'━' * 80}{UI.RESET}")
    print(f" {UI.YELLOW}HINT:{UI.RESET} {UI.DIM}ayuda | memoria | limpiar | salir{UI.RESET}")
    print(f"{UI.BLUE}{'━' * 80}{UI.RESET}")

def mostrar_panel(titulo, contenido):
    print(f"\n{UI.CYAN}{UI.BOLD}⚡ {titulo.upper()}{UI.RESET}")
    print(f"{UI.CYAN}{UI.SEP}{UI.RESET}")
    for linea in contenido.split('\n'):
        print(f"{UI.CYAN}┃{UI.RESET} {linea}")
    print(f"{UI.CYAN}{UI.SEP}{UI.RESET}\n")

def ayuda():
    return "Escríbeme de forma natural. Puedo ayudarte a debugear, optimizar SQL,\ngestionar tus ramas de Git o simplemente escucharte si el código te está estresando."

def responder(texto):
    texto_limpio = texto.strip().lower()

    if not texto_limpio:
        return "⚠️ Mensaje vacío", "Escribe algo para poder ayudarte."

    if texto_limpio == "ayuda":
        return "📌 Ayuda", ayuda()

    if texto_limpio == "memoria":
        return "🧠 Memoria", ver_memoria()

    respuestas = []
    modulos = [
    
        ("💙 Emoción", detectar_emocion),
        ("💻 Programación", detectar_programacion),
        ("🗄️ SQL", detectar_sql),
        ("🛡️ Seguridad", detectar_seguridad),
        ("🔄 Git", detectar_git),
        ("🐳 DevOps", detectar_devops),
        ("📁 Proyecto", detectar_proyecto),
        ("⏰ Horario", detectar_horario),
        ("📝 Prompt", detectar_prompt),
        ("✅ Tareas", detectar_tareas),
        ("🧮 Calculadora", detectar_calculo),
        ("📄 Archivos", detectar_archivo),
        ("✍️ Texto", detectar_texto)
    ]

    for etiqueta, funcion in modulos:
        resultado = funcion(texto)
        if resultado:
            respuestas.append((etiqueta, resultado))

    if respuestas:
        contenido = ""

        for area, dato in respuestas:
            titulo_area, respuesta_area = dato
            contenido += f"{UI.BOLD}{area}{UI.RESET} > {UI.CYAN}{titulo_area}{UI.RESET}\n"
            contenido += f"{respuesta_area}\n"
            contenido += f"{UI.DIM}{'─' * 58}{UI.RESET}\n"

        return "🤖 Respuesta avanzada", contenido.strip()

    if "hola" in texto_limpio:
        return "👋 Saludo", f"¡Hola Areli! Qué gusto verte por aquí. El sistema está listo y a tus órdenes. ¿Por dónde quieres que empecemos hoy?"

    return "🤖 Recomendación general", recomendacion_general()


mostrar_inicio()

while True:
    mensaje = input(f"{UI.GREEN}➜ {UI.BOLD}{NOMBRE_USUARIO}@DevShell{UI.RESET} {UI.DIM}$ {UI.RESET}")

    if mensaje.lower().strip() == "salir":
        print(f"\n{UI.YELLOW}Cerrando sesión. Código guardado. ¡Hasta luego, Areli!{UI.RESET}")
        break

    if mensaje.lower().strip() == "limpiar":
        mostrar_inicio()
        continue

    guardar_memoria(mensaje)

    titulo, respuesta = responder(mensaje)

    mostrar_panel(titulo, respuesta)

    guardar_historial(mensaje, respuesta)