from modulos.inteligencia import normalizar


PALABRAS_GIT = [
    "git",
    "github",
    "status",
    "remote",
    "origin",
    "pull",
    "commit",
    "push",
    "merge",
    "rebase",
    "stash",
    "branch",
    "rama",
    "ramas",
    "workflow",
    "flujo",
    "issue",
    "issues",
    "pull request",
    "pr",
    "develop",
    "main",
    "conflicto",
    "conflictos",
    "fatal",
]


GIT_COMANDOS = {
    "dns": {
        "keywords": [
            "could not resolve host",
            "resolve host",
            "github.com",
            "dns",
            "internet",
            "conexion",
            "conexión",
        ],
        "titulo": "Error de conexión con GitHub",
        "respuesta": """Ese error no significa que tu código esté mal.

Significa que Git no pudo conectarse a GitHub o no pudo resolver el dominio github.com.

Revisa conexión:

ping github.com

Si responde, limpia DNS:

ipconfig /flushdns

Luego revisa tu remoto:

git remote -v

Y vuelve a intentar:

git push

Si el repositorio se movió, actualiza origin:

git remote set-url origin URL_NUEVA_DEL_REPOSITORIO

Ejemplo:

git remote set-url origin https://github.com/AreliFllor2412/-VitraMind-AI.git
git push"""
    },

    "repo_movido": {
        "keywords": [
            "repository moved",
            "repositorio movido",
            "this repository moved",
            "new location",
            "nueva ubicacion",
            "nueva ubicación",
        ],
        "titulo": "Repositorio movido",
        "respuesta": """GitHub está avisando que el repositorio cambió de ubicación.

Primero revisa tu remoto actual:

git remote -v

Después cambia origin a la nueva URL:

git remote set-url origin URL_NUEVA

Ejemplo:

git remote set-url origin https://github.com/AreliFllor2412/-VitraMind-AI.git

Comprueba:

git remote -v

Luego sube tu rama:

git push -u origin nombre-rama"""
    },

    "status": {
        "keywords": ["status", "estado", "cambios", "modificados", "staged", "unstaged"],
        "titulo": "Git status",
        "respuesta": """Para revisar el estado del repositorio:

git status

Te muestra:
- Rama actual.
- Archivos modificados.
- Archivos agregados al stage.
- Archivos pendientes por guardar.
- Si tu rama está adelantada o atrasada respecto a GitHub.

Flujo recomendado:

git status
git add .
git commit -m "feat: describir cambio"
git push"""
    },

    "remote": {
        "keywords": ["remote", "origin", "repositorio", "url", "github"],
        "titulo": "Git remote",
        "respuesta": """Para saber a qué repositorio de GitHub estás conectada:

git remote -v

Para cambiar el repositorio remoto:

git remote set-url origin URL_DEL_REPOSITORIO

Ejemplo:

git remote set-url origin https://github.com/AreliFllor2412/-VitraMind-AI.git

Después revisa:

git remote -v"""
    },

    "pull": {
        "keywords": ["pull", "traer cambios", "actualizar", "bajar cambios"],
        "titulo": "Git pull",
        "respuesta": """Para traer cambios desde GitHub:

git pull

Si quieres indicar rama:

git pull origin nombre-rama

Ejemplo:

git pull origin develop

Si tu rama no tiene upstream:

git branch --set-upstream-to=origin/nombre-rama nombre-rama

Recomendación antes de hacer pull:

git status

Si tienes cambios sin guardar, primero haz commit o stash."""
    },

    "commit": {
        "keywords": ["commit", "guardar cambios", "mensaje", "commitear"],
        "titulo": "Git commit",
        "respuesta": """Flujo recomendado para guardar cambios:

git status
git add .
git commit -m "feat: describir cambio"

Ejemplos de mensajes:

feat: agregar historial de conversaciones
fix: corregir detección de GitHub
refactor: mejorar estructura del asistente
docs: actualizar README
style: mejorar diseño del chat

Si trabajas con Issue:

git commit -m "feat: mejorar ayuda Git #6" """
    },

    "push": {
        "keywords": ["push", "subir", "subir cambios", "publicar"],
        "titulo": "Git push",
        "respuesta": """Para subir tus cambios:

git push

Si es una rama nueva:

git push -u origin nombre-rama

Ejemplo:

git push -u origin feature/issue-6-ayuda-git

Si sale error de conexión:

ping github.com
ipconfig /flushdns
git remote -v"""
    },

    "branch": {
        "keywords": ["branch", "rama", "ramas", "switch", "checkout"],
        "titulo": "Ramas Git",
        "respuesta": """Comandos útiles para ramas:

Ver ramas:

git branch

Crear y cambiar a una rama:

git switch -c feature/nueva-funcionalidad

Cambiar de rama:

git switch nombre-rama

Subir rama nueva:

git push -u origin nombre-rama

Eliminar rama local:

git branch -D nombre-rama

Recomendación:
usa ramas por funcionalidad o Issue.

Ejemplos:

feature/issue-6-ayuda-git
feature/chat-ui
feature/github-flow
fix/error-python-path"""
    },

    "develop": {
        "keywords": ["develop", "development", "desarrollo"],
        "titulo": "Flujo con develop",
        "respuesta": """Si ya tienes rama develop, el flujo recomendado es:

main
  └── develop
        └── feature/nueva-funcionalidad

Pasos:

git switch develop
git pull origin develop
git switch -c feature/nombre-cambio

Haces cambios:

git add .
git commit -m "feat: agregar nueva funcionalidad"
git push -u origin feature/nombre-cambio

Luego en GitHub creas Pull Request:

feature/nombre-cambio  →  develop

Cuando develop esté estable:

develop  →  main"""
    },

    "workflow": {
        "keywords": ["flujo", "workflow", "pull request", "pr", "issue", "issues"],
        "titulo": "Workflow con Issues y Pull Requests",
        "respuesta": """Flujo profesional recomendado:

1. Crear Issue en GitHub.
2. Crear rama desde develop.
3. Hacer cambios.
4. Hacer commit con referencia al Issue.
5. Hacer push.
6. Crear Pull Request hacia develop.
7. Revisar cambios.
8. Hacer merge.
9. Cerrar Issue.

Ejemplo:

git switch develop
git pull origin develop
git switch -c feature/issue-6-ayuda-git

git add .
git commit -m "feat: mejorar ayuda Git #6"
git push -u origin feature/issue-6-ayuda-git

Pull Request:

feature/issue-6-ayuda-git → develop

En la descripción del PR puedes poner:

Closes #6"""
    },

    "pr": {
        "keywords": ["pull request", "pr", "compare", "merge request"],
        "titulo": "Crear Pull Request",
        "respuesta": """Para crear un Pull Request:

1. Asegúrate de estar en una rama distinta a develop o main.

git branch

2. Guarda cambios:

git status
git add .
git commit -m "feat: describir cambio"

3. Sube la rama:

git push -u origin nombre-rama

4. En GitHub da clic en:

Compare & pull request

5. Configura:

base: develop
compare: tu-rama

Ejemplo:

base: develop
compare: feature/issue-6-ayuda-git

Descripción recomendada:

## Cambios
- Se mejoró la ayuda de Git.
- Se agregaron respuestas para errores comunes.
- Se agregó flujo con Issues y Pull Requests.

## Issue
Closes #6

## Pruebas
- Se probó detección de comandos Git.
- Se revisó que no rompa otros módulos."""
    },

    "issue": {
        "keywords": ["issue", "issues", "ticket", "tarea github"],
        "titulo": "Crear Issue",
        "respuesta": """Un Issue sirve para registrar una tarea, error o mejora.

Ejemplo de Issue:

Título:
Mejorar módulo de ayuda Git

Descripción:
Se necesita mejorar el módulo devops.py para detectar mejor errores de GitHub, ramas, develop, Issues y Pull Requests.

Tareas:
- Agregar respuesta para error Could not resolve host.
- Agregar flujo con develop.
- Agregar guía para Pull Request.
- Mejorar comandos de remote y push.

Después crea una rama:

git switch develop
git pull origin develop
git switch -c feature/issue-6-ayuda-git"""
    },

    "merge": {
        "keywords": ["merge", "unir ramas", "fusionar", "mezclar"],
        "titulo": "Git merge",
        "respuesta": """Para unir ramas localmente:

git switch rama-destino
git pull origin rama-destino
git merge rama-origen

Ejemplo:

git switch develop
git pull origin develop
git merge feature/issue-6-ayuda-git

Pero si estás practicando flujo profesional, mejor hazlo desde GitHub con Pull Request:

feature/issue-6-ayuda-git → develop"""
    },

    "rebase": {
        "keywords": ["rebase", "rebasar"],
        "titulo": "Git rebase",
        "respuesta": """Cuidado con rebase en ramas compartidas.

Uso común para actualizar tu rama con main o develop:

git switch feature/mi-rama
git fetch origin
git rebase origin/develop

Si hay conflictos, resuélvelos y luego:

git add .
git rebase --continue

Cancelar rebase:

git rebase --abort

Recomendación:
si estás empezando, usa merge o Pull Request antes que rebase."""
    },

    "stash": {
        "keywords": ["stash", "guardar temporal", "temporal"],
        "titulo": "Git stash",
        "respuesta": """Stash sirve para guardar cambios temporalmente sin hacer commit.

Guardar:

git stash push -m "cambios temporales"

Ver lista:

git stash list

Recuperar último stash:

git stash pop

Aplicar sin borrar de la lista:

git stash apply

Útil cuando necesitas cambiar de rama sin perder cambios."""
    },

    "conflictos": {
        "keywords": ["conflicto", "conflictos", "conflict"],
        "titulo": "Conflictos Git",
        "respuesta": """Cuando Git marca conflicto:

1. Revisa archivos afectados:

git status

2. Abre el archivo y busca marcas:

<<<<<<< HEAD
=======
>>>>>>> nombre-rama

3. Deja solo el código correcto.
4. Guarda.
5. Agrega cambios:

git add .

6. Termina el proceso:

Si era merge:

git commit

Si era rebase:

git rebase --continue"""
    },

    "semver": {
        "keywords": ["version", "versión", "semver", "release", "tag"],
        "titulo": "Versionado SemVer",
        "respuesta": """Estructura de SemVer:

MAJOR.MINOR.PATCH

Ejemplo:

1.4.2

MAJOR: cambios incompatibles.
MINOR: nueva funcionalidad compatible.
PATCH: correcciones pequeñas.

Crear tag:

git tag v1.0.0
git push origin v1.0.0"""
    },
}


def detectar_git(texto):
    texto_normal = normalizar(texto)

    if not any(palabra in texto_normal for palabra in PALABRAS_GIT):
        return None

    for comando in GIT_COMANDOS.values():
        if any(keyword in texto_normal for keyword in comando["keywords"]):
            return comando["titulo"], comando["respuesta"]

    return "Ayuda Git", """Puedo ayudarte con Git y GitHub.

Opciones disponibles:

- git status
- git remote
- git pull
- git commit
- git push
- ramas
- develop
- merge
- rebase
- stash
- conflictos
- Issues
- Pull Requests
- errores de conexión con GitHub
- repositorio movido

Ejemplos:

ayúdame con git commit
me salió Could not resolve host github.com
cómo hago un pull request
cómo trabajo con develop
cómo cambio el remote origin
"""
