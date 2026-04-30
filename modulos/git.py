from modulos.inteligencia import normalizar


def detectar_git(texto):
    texto = normalizar(texto)

    if "pull" in texto:
        return "Git pull", """Para traer cambios:
git pull origin nombre-rama

Si no hay upstream:
git branch --set-upstream-to=origin/nombre-rama nombre-rama"""

    if "commit" in texto:
        return "Git commit", """Flujo recomendado:
git status
git add .
git commit -m "feat: describir cambio"
git push"""

    if "merge" in texto:
        return "Git merge", """Para unir ramas:
git checkout rama-destino
git pull
git merge rama-origen"""

    if "rebase" in texto:
        return "Git rebase", """Cuidado con rebase en ramas compartidas.

Continuar despues de resolver conflictos:
git status
git rebase --continue

Cancelar:
git rebase --abort"""

    if "stash" in texto:
        return "Git stash", """Uso:
git stash
git stash list
git stash pop
git stash apply"""

    if "branch" in texto or "rama" in texto:
        return "Ramas", """Comandos:
git checkout -b feature/nueva-funcionalidad
git branch
git branch -D nombre-rama
git remote prune origin
git log --oneline --graph --all"""

    if "flujo" in texto or "workflow" in texto:
        return "Workflows", """Opciones:
1. GitHub Flow: simple y practico.
2. Trunk-Based: ideal con CI/CD.
3. Gitflow: util para releases formales."""

    if "version" in texto or "semver" in texto:
        return "SemVer", """Estructura: MAJOR.MINOR.PATCH

MAJOR: cambios incompatibles.
MINOR: funcionalidad compatible.
PATCH: correcciones."""

    return None
