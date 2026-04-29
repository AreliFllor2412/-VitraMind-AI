def detectar_devops(texto):
    texto = texto.lower()

    if "docker" in texto or "contenedor" in texto:
        return "Docker & Contenedores", """Comandos Esenciales de Docker:

1. docker build -t mi-app .      # Construir imagen
2. docker run -p 80:80 mi-app    # Ejecutar contenedor
3. docker ps                     # Listar contenedores activos
4. docker stop <id>              # Detener contenedor
5. docker-compose up -d          # Orquestar múltiples servicios

Buenas Prácticas Dockerfile:
- Usa imágenes base ligeras (Alpine).
- Multistage builds para reducir tamaño.
- No ejecutes como root dentro del contenedor.
"""

    if any(p in texto for p in ["ci/cd", "despliegue continuo", "integracion continua"]):
        return "CI/CD & Despliegue", """Principios de Integración/Despliegue Continuo:
1. Integración Continua (CI): Automatiza la construcción y prueba del código.
2. Despliegue Continuo (CD): Automatiza el lanzamiento a producción.
3. Herramientas: Jenkins, GitLab CI, GitHub Actions, CircleCI.
"""
    return None