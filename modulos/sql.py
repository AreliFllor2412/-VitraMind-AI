def detectar_sql(texto):
    texto = texto.lower()

    if "backup" in texto or "respaldo" in texto:
        return "Database Reliability", """Comando de respaldo profesional:
¡Claro, Areli! Mantener los datos seguros es prioridad. Aquí tienes el comando para que duermas tranquila:

mysqldump -u root -p nombre_base > backup.sql

Profesional:
mysqldump -u root -p --routines --triggers --events --single-transaction --databases nombre_base > backup.sql
"""

    if "migracion" in texto or "migration" in texto:
        return "Migraciones", """Revisa:
¡Ojo con las migraciones! Antes de darle al enter, dale una vuelta a esto:
1. ¿El nombre de la tabla es el correcto?
2. ¿Están todos los campos y sus tipos?
3. ¿Las llaves foráneas tienen sentido?
¡Y por favor, ni se te ocurra el migrate:fresh en producción sin un backup!"""

    if "consulta" in texto or "select" in texto:
        return "Consulta SQL", """Ejemplo base:
¿Buscando datos? Aquí tienes cómo hacer un SELECT que se vea limpio:

Joins Profesionales:
SELECT u.nombre, p.nombre_proyecto 
FROM usuarios u
INNER JOIN proyectos p ON u.id = p.usuario_id
WHERE u.status = 'Activo';
"""

    if "optimizacion" in texto or "lento" in texto or "index" in texto:
        return "Optimización SQL", """¿La base de datos está lenta? Vamos a darle un boost de energía:

1. Índices: CREATE INDEX idx_usuario_email ON usuarios(email);
2. EXPLAIN: Usa 'EXPLAIN SELECT...' para ver cómo actúa el motor.
3. Evita SELECT *: Trae solo las columnas necesarias.
4. Constraints: Asegura integridad con FOREIGN KEY y UNIQUE.
"""

    if "diseño" in texto and "db" in texto:
        return "Diseño de Base de Datos", """Reglas de Oro:
1. Normalización (1NF, 2NF, 3NF).
2. Nombres de tablas en plural o singular consistente.
3. Campos de auditoría: created_at, updated_at, deleted_at.
4. Tipos de datos correctos (no uses VARCHAR(255) para todo).
"""

    if "transaccion" in texto or "acid" in texto:
        return "Integridad de Datos (ACID)", """Gestión de Transacciones:

1. START TRANSACTION; ... COMMIT; / ROLLBACK;
2. Propiedades ACID: Atomicidad, Consistencia, Aislamiento, Durabilidad.
3. Niveles de Aislamiento: Read Uncommitted, Read Committed, Repeatable Read, Serializable.
"""

    if "seguridad" in texto or "injection" in texto:
        return "Seguridad en Base de Datos", """Protección Crítica:

1. Prepared Statements: NUNCA concatenar variables en el string SQL.
2. Sanitize: Limpia inputs de usuario.
3. Privilegios: El usuario de la app no debe ser 'root'. Solo permisos necesarios (SELECT, INSERT, UPDATE).
4. Encriptación: Hashea passwords con Argon2 o Bcrypt (nunca MD5).
5. Auditoría: Implementa logs de quién modificó qué y cuándo.
"""

    if any(p in texto for p in ["escalabilidad", "sharding", "replicacion", "cluster"]):
        return "Escalabilidad de Bases de Datos", """Estrategias Avanzadas:

1. Replicación (Master-Slave/Master-Master): Mejora lectura y disponibilidad.
2. Sharding (Particionamiento Horizontal): Distribuye datos en múltiples servidores.
3. Load Balancing: Distribuye consultas entre réplicas o shards.
4. Caching: Reduce la carga de la DB para datos frecuentemente accedidos.
"""

    if any(p in texto for p in ["cte", "window function", "subconsulta avanzada"]):
        return "Optimización de Consultas Avanzadas", """Técnicas para Queries Complejas:

1. CTEs (Common Table Expressions): Organiza consultas complejas y recursivas.
2. Window Functions: Realiza cálculos sobre un conjunto de filas relacionadas (ej. RANK(), ROW_NUMBER(), LAG(), LEAD()).
3. Subconsultas Correlacionadas: Útiles para comparar filas con un subconjunto de datos.
"""
    return None

    