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
from modulos.security import detectar_seguridad # Nuevo módulo de seguridad
from modulos.tareas import detectar_tareas
from modulos.calculadora import detectar_calculo
from modulos.archivos import detectar_archivo
from modulos.texto import detectar_texto

# Configuración de Estética Profesional
class UI:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    BORDER = "◈" * 60

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_inicio():
    limpiar()
    print(f"{UI.CYAN}╔" + "═" * 78 + "╗")
    print(f"║ {UI.BOLD}{NOMBRE_IA.center(76)}{UI.RESET}{UI.CYAN} ║")
    print("╚" + "═" * 78 + f"╝{UI.RESET}")
    print(f"\n{UI.GREEN}●{UI.RESET} {UI.BOLD}Status: Online{UI.RESET} | Bienvenida, Ingeniera {NOMBRE_USUARIO}.")
    print(f"{UI.YELLOW}Sistemas de arquitectura y lógica listos para operar.{UI.RESET}\n")
    
    menu = [
        "1. Mindset & Emociones", "2. Core Programming", "3. Database Engine",
        "4. Fullstack Ecosystem", "5. Project Management", "6. UI/UX Strategy",
        "7. Data Reporting", "8. Version Control (Git)", "9. Schedule Ops",
        "10. Advanced Prompts", "11. Backlog/Tareas", "12. Engineering Calc", "13. DevOps & Infra", "14. CyberSecurity"
    ]
    
    for i in range(0, len(menu), 2):
        col1 = menu[i].ljust(35)
        col2 = menu[i+1] if i+1 < len(menu) else ""
        print(f"   {col1} {col2}")

    print(f"\n{UI.CYAN}{'━' * 80}{UI.RESET}")
    print(f"{UI.YELLOW}Comandos rápidos:{UI.RESET} ayuda | memoria | limpiar | salir")
    print(f"{UI.CYAN}{'━' * 80}{UI.RESET}")

def mostrar_panel(titulo, contenido):
    print(f"\n{UI.CYAN}{UI.BORDER}")
    print(f"  {UI.BOLD}{UI.GREEN}⚡ {titulo.upper()}{UI.RESET}")
    print(f"{UI.CYAN}{UI.BORDER}{UI.RESET}")
    print(f"{UI.BOLD}{contenido}{UI.RESET}")
    print(f"{UI.CYAN}{UI.BORDER}{UI.RESET}\n")

def ayuda():
    return "Escríbeme de forma natural. Puedo ayudarte a debugear, optimizar SQL,\ngestionar tus ramas de Git o simplemente escucharte si el código te está estresando."


def agregar_respuesta(respuestas, etiqueta, resultado):
    """
    Cada módulo debe regresar:
    ("Título", "Respuesta")
    """
    if resultado:
        respuestas.append((etiqueta, resultado))


def responder(texto):
    texto_limpio = texto.strip().lower()

    if not texto_limpio:
        return "⚠️ Mensaje vacío", "Escribe algo para poder ayudarte."

    if texto_limpio == "ayuda":
        return "📌 Ayuda", ayuda()

    if texto_limpio == "memoria":
        return "🧠 Memoria", ver_memoria()

    respuestas = []
    
    # Sistema de registro dinámico para evitar código repetitivo
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
            contenido += f"{area}: {titulo_area}\n{respuesta_area}\n\n"

        return "🤖 Respuesta avanzada", contenido.strip()

    if "hola" in texto_limpio:
        return "👋 Saludo", f"Hola Areli. El entorno está configurado. ¿En qué módulo trabajamos hoy?"

    return "🤖 Recomendación general", recomendacion_general()


mostrar_inicio()

while True:
    mensaje = input(f"{UI.GREEN}Areli@DevShell{UI.RESET}:~$ ")

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