def detectar_programacion(texto):
    texto = texto.lower()

    if "vite" in texto:
        return "Vite", """Revisión:
1. npm run dev
2. Revisar imports
3. Revisar dependencias
4. Reiniciar terminal"""

    if "laravel" in texto:
        return "Laravel", """Revisión:
1. routes/web.php
2. Controller
3. Modelo
4. storage/logs/laravel.log
5. php artisan optimize:clear"""

    if "react" in texto:
        return "React", """Revisión:
1. Estado inicial
2. Props
3. Imports/exports
4. Consola del navegador"""

    if "sql" in texto or "mysql" in texto or "base de datos" in texto:
        return "SQL/MySQL", """Revisión:
1. Tablas
2. Columnas
3. Migraciones
4. Respaldos
5. Consultas SQL"""

    if "error" in texto:
        return "Error general", """Método:
1. Copia el error completo
2. Ubica archivo y línea
3. Revisa cambios recientes"""

    if any(p in texto for p in ["arquitectura", "solid", "clean code"]):
        return "Arquitectura y Buenas Prácticas", """Principios SOLID:
1. SRP: Responsabilidad Única.
2. OCP: Abierto/Cerrado.
3. LSP: Sustitución de Liskov.
4. ISP: Segregación de Interfaz.
5. DIP: Inversión de Dependencias.

Clean Code:
- Nombres de variables descriptivos.
- Funciones pequeñas (máximo 20 líneas).
- Evita comentarios obvios; el código debe explicarse solo."""

    if "refactor" in texto:
        return "Refactorización", "1. Identifica 'Code Smells'.\n2. Crea tests unitarios.\n3. Aplica cambios pequeños.\n4. Verifica que todo siga funcionando."

    if any(p in texto for p in ["clean architecture", "ddd", "capas"]):
        return "Arquitectura Avanzada", """Estructura de Cebolla (Onion):
1. Domain (Entidades y Reglas de Negocio).
2. Application (Casos de Uso).
3. Infrastructure (DB, APIs externas, Framework).

Beneficio: El core de tu app no depende de si usas Laravel, React o una DB específica.
"""

    if any(p in texto for p in ["patron", "pattern", "diseño"]):
        return "Patrones de Diseño GoF", """Recomendaciones de implementación:

1. Singleton: Para conexiones a DB o Logs.
2. Factory: Para instanciar objetos complejos sin exponer lógica.
3. Observer: Para sistemas de eventos y notificaciones.
4. Strategy: Para cambiar algoritmos en tiempo de ejecución.
5. Adapter: Para integrar interfaces incompatibles.
"""

    if "api" in texto or "rest" in texto:
        return "Diseño de API RESTful", """Best Practices:
1. Usa sustantivos, no verbos (GET /users, no /getUsers).
2. Versionado: /api/v1/resource.
3. Status codes: 200 (OK), 201 (Created), 400 (Bad Request), 404 (Not Found), 500 (Server Error).
4. Stateless: Cada petición debe ser independiente.
5. Paginación y Filtrado: Obligatorios en colecciones grandes.
"""

    if any(p in texto for p in ["test", "testing", "pruebas"]):
        return "Estrategias de Testing", """Tipos de Pruebas Esenciales:
1. Unitarias: Aísla y prueba la unidad más pequeña de código (función/método).
2. Integración: Verifica la interacción entre componentes (ej. DB y ORM).
3. End-to-End (E2E): Simula el flujo completo del usuario en la aplicación.
"""

    return None 
        