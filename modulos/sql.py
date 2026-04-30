from modulos.inteligencia import normalizar


def detectar_sql(texto):
    texto = normalizar(texto)

    if "backup" in texto or "respaldo" in texto:
        return "Respaldo de base de datos", """Comando base:
mysqldump -u root -p nombre_base > backup.sql

Comando mas completo:
mysqldump -u root -p --routines --triggers --events --single-transaction --databases nombre_base > backup.sql"""

    if "migracion" in texto or "migration" in texto:
        return "Migraciones", """Antes de ejecutar:
1. Confirma tabla y nombres de columnas.
2. Revisa tipos de datos.
3. Valida llaves foraneas.
4. Haz backup si hay datos importantes.
5. Evita migrate:fresh en produccion."""

    if "consulta" in texto or "select" in texto:
        return "Consulta SQL", """Ejemplo:
SELECT u.nombre, p.nombre_proyecto
FROM usuarios u
INNER JOIN proyectos p ON u.id = p.usuario_id
WHERE u.status = 'Activo';"""

    if "optimizacion" in texto or "optimizar" in texto or "lento" in texto or "index" in texto:
        return "Optimizacion SQL", """Checklist:
1. Usa EXPLAIN para revisar el plan.
2. Agrega indices donde filtras o haces joins.
3. Evita SELECT *.
4. Pagina resultados grandes.
5. Mide antes y despues."""

    if "diseno" in texto and any(p in texto for p in ["db", "base", "datos"]):
        return "Diseno de base de datos", """Reglas base:
1. Normaliza hasta donde tenga sentido.
2. Usa nombres consistentes.
3. Agrega created_at, updated_at y deleted_at si aplica.
4. Elige tipos correctos.
5. Documenta relaciones importantes."""

    if "transaccion" in texto or "acid" in texto:
        return "Integridad de datos", """Transacciones:
1. START TRANSACTION;
2. Ejecuta operaciones relacionadas.
3. COMMIT si todo salio bien.
4. ROLLBACK si algo falla.

ACID: atomicidad, consistencia, aislamiento y durabilidad."""

    if "seguridad" in texto or "injection" in texto or "inyeccion" in texto:
        return "Seguridad en base de datos", """Proteccion:
1. Usa prepared statements.
2. No concatenes input de usuario.
3. El usuario de la app no debe ser root.
4. Hashea passwords con Argon2 o bcrypt.
5. Registra cambios sensibles."""

    if any(p in texto for p in ["escalabilidad", "sharding", "replicacion", "cluster"]):
        return "Escalabilidad de datos", """Estrategias:
1. Replicas para lectura.
2. Cache para datos frecuentes.
3. Particionamiento si el volumen lo exige.
4. Colas para trabajos pesados.
5. Monitoreo antes de escalar."""

    if any(p in texto for p in ["cte", "window function", "subconsulta"]):
        return "Consultas avanzadas", """Tecnicas:
1. CTEs para organizar consultas complejas.
2. Window functions para ranking, acumulados y comparaciones.
3. Subconsultas cuando simplifican la lectura."""

    return None
