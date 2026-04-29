def detectar_git(texto):
    texto = texto.lower()

    if "pull" in texto:
        return "Git Pull", """Para traer cambios:

git pull origin nombre-rama

Si no hay upstream:
git branch --set-upstream-to=origin/nombre-rama nombre-rama
"""

    if "commit" in texto:
        return "Git Commit", """Flujo recomendado:

git status
git add .
git commit -m "feat: describir cambio"
git push
"""

    if "merge" in texto:
        return "Git Merge", """Para unir ramas:

git checkout rama-destino
git pull
git merge rama-origen
"""

    if "rebase" in texto:
        return "Git Rebase", """Cuidado con rebase:

git status
git rebase --continue

Si quieres cancelar:
git rebase --abort
"""

    if "stash" in texto:
        return "Git Stash (Guardado temporal)", """Uso de Stash:

git stash          # Guarda cambios temporalmente
git stash list     # Lista elementos guardados
git stash pop      # Recupera y elimina el último stash
git stash apply    # Recupera sin eliminar
"""

    if "branch" in texto or "rama" in texto:
        return "Gestión de Ramas", """Comandos profesionales:

git checkout -b feature/nueva-funcionalidad  # Crear y cambiar
git branch -D nombre-rama                    # Borrado forzado
git remote prune origin                      # Limpiar ramas remotas borradas
git log --oneline --graph --all              # Visualizar historial pro
"""

    if "flujo" in texto or "workflow" in texto:
        return "Workflows Profesionales", """Estrategias de Ramificación:

1. Gitflow: master (prod), develop (dev), feature/*, release/*, hotfix/*.
2. Trunk-Based: Desarrollo sobre 'main' con pequeñas ramas de vida corta (recomendado para CI/CD).
3. GitHub Flow: Pull Requests directos a main.
"""

    if "version" in texto or "semver" in texto:
        return "Versionado Semántico (SemVer)", """Estructura: MAJOR.MINOR.PATCH

- MAJOR: Cambios que rompen la compatibilidad.
- MINOR: Funcionalidades nuevas compatibles.
- PATCH: Corrección de errores (bugs).
"""

    return None