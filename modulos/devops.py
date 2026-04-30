from modulos.inteligencia import normalizar


def detectar_devops(texto):
    texto = normalizar(texto)

    if "docker" in texto or "contenedor" in texto:
        return "Docker", """Comandos esenciales:
1. docker build -t mi-app .
2. docker run -p 80:80 mi-app
3. docker ps
4. docker stop <id>
5. docker compose up -d

Buenas practicas:
- Usa imagenes base pequenas.
- Aplica multistage builds.
- No ejecutes como root dentro del contenedor."""

    if any(p in texto for p in ["ci/cd", "despliegue continuo", "integracion continua", "github actions"]):
        return "CI/CD", """Principios:
1. Construir automaticamente.
2. Ejecutar pruebas.
3. Revisar calidad.
4. Desplegar con rollback posible.
5. Guardar secretos fuera del repositorio."""

    return None
