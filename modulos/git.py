from modulos.inteligencia import normalizar


GIT_COMANDOS = {
    "status": {
        "keywords": ["status", "estado", "cambios"],
        "titulo": "Git status",
        "respuesta": """Para revisar el estado del repositorio:

git status

Te muestra:
- Rama actual.
- Archivos modificados.
- Archivos pendientes por agregar.
- Si hay commits pendientes por subir."""
    },
    "remote": {
        "keywords": ["remote", "origin", "repositorio", "github"],
        "titulo": "Git remote",
        "respuesta": """Para saber a qué repositorio de GitHub estás conectada:

git remote -v

Para cambiar el repositorio remoto:

git remote set-url origin URL_DEL_REPOSITORIO"""
    },
    "pull": {
        "keywords": ["pull", "traer cambios", "actualizar"],
        "titulo": "Git pull",
        "respuesta": """Para traer cambios:

git pull origin nombre-rama

Si ya tienes upstream configurado:

git pull

Si no hay upstream:

git branch --set-upstream-to=origin/nombre-rama nombre-rama"""
    },
    "commit": {
        "keywords": ["commit", "guardar cambios"],
        "titulo": "Git commit",
        "respuesta": """Flujo recomendado:

git status
git add .
git commit -m "feat: describir cambio"
git push

Ejemplos de mensajes:

feat: agregar historial de conversaciones
fix: corregir detección de notas
refactor: mejorar estructura del asistente
docs: actualizar README"""
    },
    "push": {
        "keywords": ["push", "subir", "subir cambios"],
        "titulo": "Git push",
        "respuesta": """Para subir tus cambios:

git push

Si es una rama nueva:

git push -u origin nombre-rama

Ejemplo:

git push -u origin feature/issue-6-ayuda-git"""
    },
    "merge": {
        "keywords": ["merge", "unir ramas", "fusionar"],
        "titulo": "Git merge",
        "respuesta": """Para unir ramas:

git switch rama-destino
git pull
git merge rama-origen

Ejemplo:

git switch main
git pull
git merge feature/nueva-funcionalidad"""
    },
    "rebase": {
        "keywords": ["rebase", "rebasar"],
        "titulo": "Git rebase",
        "respuesta": """Cuidado con rebase en ramas compartidas.

Uso común:

git switch feature/mi-rama
git fetch origin
git rebase origin/main

Continuar después de resolver conflictos:

git status
git rebase --continue

Cancelar:

git rebase --abort"""
    },
    "stash": {
        "keywords": ["stash", "guardar temporal"],
        "titulo": "Git stash",
        "respuesta": """Uso de stash:

git stash
git stash list
git stash pop
git stash apply

Con mensaje:

git stash push -m "cambios temporales de login"

Útil cuando necesitas cambiar de rama sin perder cambios."""
    },
    "branch": {
        "keywords": ["branch", "rama", "ramas"],
        "titulo": "Ramas",
        "respuesta": """Comandos útiles:

git switch -c feature/nueva-funcionalidad
git branch
git branch -a
git branch -D nombre-rama
git remote prune origin
git log --oneline --graph --all

Recomendación:
usa ramas por Issue.

Ejemplo:

feature/issue-6-ayuda-git"""
    },
    "workflow": {
        "keywords": ["flujo", "workflow", "pull request", "pr", "issue"],
        "titulo": "Workflow GitHub",
        "respuesta": """Flujo recomendado:

1. Crear Issue.
2. Crear rama.
3. Hacer cambios.
4. Commit con referencia al Issue.
5. Push.
6. Crear Pull Request.
7. Code Review.
8. Merge.
9. Cerrar Issue.

Ejemplo:

git switch -c feature/issue-6-ayuda-git
git add .
git commit -m "Mejorar ayuda de comandos Git #6"
git push -u origin feature/issue-6-ayuda-git"""
    },
    "semver": {
        "keywords": ["version", "semver", "release"],
        "titulo": "SemVer",
        "respuesta": """Estructura:

MAJOR.MINOR.PATCH

Ejemplo:

1.4.2

MAJOR: cambios incompatibles.
MINOR: nueva funcionalidad compatible.
PATCH: correcciones pequeñas."""
    },
    "conflictos": {
        "keywords": ["conflicto", "conflictos", "conflict"],
        "titulo": "Conflictos Git",
        "respuesta": """Cuando hay conflicto:

1. Abre los archivos marcados por Git.
2. Busca las marcas:

<<<<<<< HEAD
=======
>>>>>>> rama

3. Deja sólo el código correcto.
4. Guarda el archivo.
5. Ejecuta:

git add .
git commit

Si era rebase:

git rebase --continue"""
    },
}


def detectar_git(texto):
    texto_normal = normalizar(texto)

    if not any(palabra in texto_normal for palabra in ["git", "pull", "commit", "merge", "rebase", "stash", "branch", "rama", "push", "workflow", "flujo"]):
        return None

    for comando in GIT_COMANDOS.values():
        if any(keyword in texto_normal for keyword in comando["keywords"]):
            return comando["titulo"], comando["respuesta"]

    return "Ayuda Git", """Puedo ayudarte con:

- git status
- git remote
- git pull
- git commit
- git push
- ramas
- merge
- rebase
- stash
- conflictos
- workflow con Issues y Pull Requests

Ejemplo:
"ayúdame con git commit"
"""
