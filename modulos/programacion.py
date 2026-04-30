from modulos.inteligencia import normalizar


def detectar_programacion(texto):
    texto = normalizar(texto)

    if "vite" in texto:
        return "Vite", """Revision rapida:
1. npm run dev
2. Revisa imports y rutas relativas.
3. Verifica dependencias en package.json.
4. Reinicia el servidor si cambiaste configuracion.
5. Mira la consola del navegador y la terminal."""

    if "laravel" in texto:
        return "Laravel", """Revision Laravel:
1. routes/web.php o routes/api.php
2. Controller y metodo correcto.
3. Modelo, relaciones y fillable.
4. storage/logs/laravel.log
5. php artisan optimize:clear"""

    if "react" in texto:
        return "React", """Checklist React:
1. Estado inicial y cambios de estado.
2. Props que llegan al componente.
3. Imports/exports.
4. Keys en listas.
5. Errores en consola del navegador."""

    if "python" in texto:
        return "Python", """Checklist Python:
1. Lee el traceback desde la ultima linea.
2. Revisa archivo y numero de linea.
3. Confirma imports y nombres de variables.
4. Aisla la funcion que falla.
5. Ejecuta una prueba pequena."""

    if "sql" in texto or "mysql" in texto or "base de datos" in texto:
        return "SQL/MySQL", """Revision:
1. Tablas y columnas.
2. Tipos de datos.
3. Migraciones.
4. Indices.
5. Consulta exacta que falla."""

    if "error" in texto or "bug" in texto or "no funciona" in texto:
        return "Debug general", """Metodo:
1. Copia el error completo.
2. Ubica archivo y linea.
3. Revisa el ultimo cambio.
4. Reduce el caso hasta reproducirlo.
5. Aplica una correccion pequena y vuelve a probar."""

    if any(p in texto for p in ["arquitectura", "solid", "clean code"]):
        return "Arquitectura y buenas practicas", """Principios base:
1. SRP: una responsabilidad por modulo.
2. OCP: extender sin romper lo existente.
3. DIP: depender de abstracciones cuando aporte claridad.
4. Nombres descriptivos.
5. Funciones pequenas y con salida verificable."""

    if "refactor" in texto or "refactorizar" in texto:
        return "Refactorizacion", """Ruta segura:
1. Identifica el olor de codigo.
2. Agrega o ejecuta pruebas.
3. Cambia una cosa a la vez.
4. Mantiene el comportamiento.
5. Verifica al final."""

    if any(p in texto for p in ["clean architecture", "ddd", "capas"]):
        return "Arquitectura avanzada", """Estructura por capas:
1. Domain: entidades y reglas de negocio.
2. Application: casos de uso.
3. Infrastructure: DB, APIs y frameworks.
4. Interface: controladores, CLI o UI."""

    if any(p in texto for p in ["patron", "pattern", "diseno"]):
        return "Patrones de diseno", """Patrones utiles:
1. Factory: crear objetos complejos.
2. Strategy: cambiar algoritmos sin condicionales gigantes.
3. Observer: eventos y notificaciones.
4. Adapter: integrar interfaces distintas.
5. Repository: separar acceso a datos."""

    if "api" in texto or "rest" in texto:
        return "API REST", """Buenas practicas:
1. Usa recursos: GET /users, no /getUsers.
2. Versiona si el contrato puede cambiar: /api/v1.
3. Usa codigos HTTP correctos.
4. Valida entrada.
5. Paginacion y filtros en colecciones."""

    if any(p in texto for p in ["test", "testing", "pruebas"]):
        return "Testing", """Tipos de pruebas:
1. Unitarias: funciones o clases pequenas.
2. Integracion: componentes juntos.
3. End-to-end: flujo completo.
4. Regresion: evita que vuelva un bug."""

    return None
