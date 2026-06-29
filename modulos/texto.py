from modulos.inteligencia import normalizar


PALABRAS_PROMPT = [
    "prompt",
    "prompts",
    "instruccion",
    "instrucción",
    "plantilla",
    "chatgpt",
    "ia",
]


PROMPTS = {
    "programacion": {
        "keywords": [
            "codigo",
            "código",
            "programacion",
            "programación",
            "react",
            "python",
            "laravel",
            "firebase",
            "javascript",
            "error",
            "componente",
        ],
        "titulo": "Prompt profesional para programación",
        "respuesta": """Actúa como desarrollador senior.

Necesito mejorar o corregir este código.

Contexto:
- Proyecto: [nombre del proyecto]
- Tecnología: [React / Laravel / Firebase / Python / React Native]
- Archivo: [ruta del archivo]
- Objetivo: [qué quieres lograr]
- Problema actual: [error, diseño, lógica o mejora]

Reglas:
- Conserva la lógica que ya funciona.
- Respeta nombres, rutas y estructura.
- No elimines funciones necesarias.
- No inventes dependencias si no son necesarias.
- Explica solo los cambios importantes.

Entrega:
- Código completo listo para usar.
- Explicación corta.
- Pasos para probarlo.
- Posibles errores a revisar."""
    },

    "debug": {
        "keywords": [
            "debug",
            "bug",
            "error",
            "falla",
            "no funciona",
            "undefined",
            "exception",
            "traceback",
        ],
        "titulo": "Prompt profesional para debug",
        "respuesta": """Actúa como desarrollador senior especializado en depuración.

Tengo este error y necesito resolverlo paso a paso.

Contexto:
- Proyecto: [nombre]
- Tecnología: [React / Laravel / Python / Firebase / SQL]
- Archivo donde ocurre: [ruta]
- Error exacto: [pega el error completo]
- Qué cambié antes del error: [explica brevemente]

Reglas:
- Identifica la causa probable.
- Dame la solución más segura primero.
- No cambies todo el archivo si solo falla una parte.
- Explica cómo verificar que quedó bien.

Entrega:
- Diagnóstico.
- Código o comando corregido.
- Pasos de prueba.
- Qué revisar si sigue fallando."""
    },

    "ux": {
        "keywords": [
            "diseño",
            "diseno",
            "ux",
            "ui",
            "interfaz",
            "pantalla",
            "dashboard",
            "visual",
            "responsive",
        ],
        "titulo": "Prompt profesional para UX/UI",
        "respuesta": """Actúa como diseñador UX/UI senior.

Necesito mejorar esta interfaz para que se vea más profesional.

Contexto:
- Tipo de sistema: [web / móvil / dashboard / ERP]
- Usuario objetivo: [admin / empleado / cliente / supervisor]
- Problema visual: [muy cargado / poco claro / informal / sin jerarquía]
- Estilo deseado: [formal / moderno / claro / corporativo]

Reglas:
- Mantén un diseño limpio y profesional.
- Usa buena jerarquía visual.
- Evita colores demasiado oscuros o saturados.
- Prioriza legibilidad, orden y facilidad de uso.
- No rompas la lógica del componente.

Entrega:
- Propuesta visual.
- Código mejorado.
- Explicación corta de cambios.
- Recomendaciones de mejora."""
    },

    "git": {
        "keywords": [
            "git",
            "github",
            "commit",
            "push",
            "pull",
            "branch",
            "rama",
            "issue",
            "pull request",
            "pr",
        ],
        "titulo": "Prompt profesional para Git/GitHub",
        "respuesta": """Actúa como mentor senior de Git y GitHub.

Necesito resolver o ejecutar este flujo de Git.

Contexto:
- Rama actual: [main / develop / feature/...]
- Acción que quiero hacer: [commit / push / pull / PR / merge]
- Error o duda: [pega el mensaje exacto]
- Repositorio: [URL o nombre]

Reglas:
- Dame comandos exactos para PowerShell.
- Explica qué hace cada comando de forma breve.
- Evita comandos peligrosos sin advertencia.
- Si hay riesgo de perder cambios, primero pide revisar git status.

Entrega:
- Diagnóstico.
- Comandos en orden.
- Cómo verificar que funcionó.
- Qué hacer si sale error."""
    },

    "sql": {
        "keywords": [
            "sql",
            "mysql",
            "postgres",
            "base de datos",
            "consulta",
            "query",
            "tabla",
            "migracion",
            "migración",
        ],
        "titulo": "Prompt profesional para SQL",
        "respuesta": """Actúa como especialista senior en bases de datos.

Necesito ayuda con una consulta o estructura SQL.

Contexto:
- Motor: [MySQL / PostgreSQL / SQL Server]
- Tabla(s): [nombres]
- Objetivo: [qué necesitas obtener o modificar]
- Problema: [error, lentitud, datos incorrectos]

Reglas:
- No borres datos sin advertencia.
- Si hay UPDATE o DELETE, primero dame un SELECT de verificación.
- Optimiza la consulta si aplica.
- Explica índices necesarios si son útiles.

Entrega:
- Consulta SQL lista.
- Explicación corta.
- Validación previa.
- Riesgos o recomendaciones."""
    },

    "seguridad": {
        "keywords": [
            "seguridad",
            "jwt",
            "token",
            "login",
            "password",
            "contraseña",
            "permisos",
            "roles",
            "auth",
        ],
        "titulo": "Prompt profesional para seguridad",
        "respuesta": """Actúa como especialista senior en seguridad web.

Necesito revisar o mejorar seguridad en mi sistema.

Contexto:
- Tecnología: [Laravel / React / Firebase / Node / Python]
- Módulo: [login / roles / permisos / API]
- Problema o mejora: [describe]
- Datos sensibles involucrados: [usuarios / contraseñas / tokens / roles]

Reglas:
- Prioriza seguridad real en backend.
- No guardes contraseñas en texto plano.
- Valida permisos en servidor, no solo en interfaz.
- Explica riesgos de forma clara.

Entrega:
- Problemas detectados.
- Solución recomendada.
- Código o configuración.
- Checklist de seguridad."""
    },

    "documentacion": {
        "keywords": [
            "documentacion",
            "documentación",
            "readme",
            "manual",
            "arquitectura",
            "resumen",
            "informe",
        ],
        "titulo": "Prompt profesional para documentación",
        "respuesta": """Actúa como redactor técnico senior.

Necesito crear o mejorar documentación del proyecto.

Contexto:
- Proyecto: [nombre]
- Tipo de documento: [README / manual / arquitectura / informe]
- Audiencia: [usuario final / profesor / desarrollador / empresa]
- Contenido base: [pega texto o describe secciones]

Reglas:
- Usa estructura clara.
- Evita relleno.
- Explica términos técnicos cuando sea necesario.
- Mantén tono formal y profesional.

Entrega:
- Documento estructurado.
- Secciones con títulos.
- Resumen ejecutivo si aplica.
- Recomendaciones finales."""
    },

    "general": {
        "keywords": [
            "prompt",
            "ayuda",
            "consulta",
            "pregunta",
            "general",
        ],
        "titulo": "Prompt profesional",
        "respuesta": """Actúa como [rol experto].

Necesito [objetivo concreto].

Contexto:
- Proyecto o situación: [explica]
- Archivo, módulo o tema: [indica]
- Problema actual: [describe]
- Restricciones importantes: [qué no debe cambiar]

Reglas:
- Sé claro y directo.
- Conserva lo que ya funciona.
- Evita respuestas genéricas.
- Explica cambios importantes.
- Da pasos accionables.

Entrega:
- Solución lista para usar.
- Pasos de verificación.
- Riesgos o detalles a revisar.
- Recomendación final."""
    },
}


def detectar_prompt(texto):
    texto_normal = normalizar(texto)

    if not any(palabra in texto_normal for palabra in PALABRAS_PROMPT):
        return None

    for config in PROMPTS.values():
        if any(keyword in texto_normal for keyword in config["keywords"]):
            return config["titulo"], config["respuesta"]

    return PROMPTS["general"]["titulo"], PROMPTS["general"]["respuesta"]
