from modulos.inteligencia import normalizar


SQL_TEMAS = {
    "backup": {
        "keywords": ["backup", "respaldo", "mysqldump", "dump"],
        "titulo": "Respaldo de base de datos",
        "respuesta": """Comando básico:

mysqldump -u root -p nombre_base > backup.sql

Comando más completo:

mysqldump -u root -p --routines --triggers --events --single-transaction --databases nombre_base > backup.sql

Restaurar respaldo:

mysql -u root -p nombre_base < backup.sql

Recomendación:
Antes de modificar datos reales, crea respaldo y valida que el archivo .sql no esté vacío."""
    },

    "migraciones": {
        "keywords": ["migracion", "migración", "migration", "migrate", "schema"],
        "titulo": "Migraciones",
        "respuesta": """Antes de ejecutar migraciones:

1. Confirma tabla y nombres de columnas.
2. Revisa tipos de datos.
3. Valida llaves foráneas.
4. Haz backup si hay datos importantes.
5. Evita migrate:fresh en producción.
6. Prueba primero en local o staging.
7. Define rollback si algo falla.

Laravel:

php artisan migrate
php artisan migrate:rollback
php artisan migrate:status

Peligro:
php artisan migrate:fresh borra tablas."""
    },

    "consulta": {
        "keywords": ["consulta", "select", "query", "where", "join", "inner join", "left join"],
        "titulo": "Consulta SQL",
        "respuesta": """Ejemplo con JOIN:

SELECT
    u.nombre,
    p.nombre_proyecto
FROM usuarios u
INNER JOIN proyectos p
    ON u.id = p.usuario_id
WHERE u.status = 'Activo';

Buenas prácticas:

1. Evita SELECT * si no necesitas todas las columnas.
2. Usa aliases claros.
3. Filtra con WHERE.
4. Ordena con ORDER BY cuando sea necesario.
5. Pagina resultados grandes con LIMIT/OFFSET."""
    },

    "optimizacion": {
        "keywords": ["optimizacion", "optimización", "optimizar", "lento", "index", "indice", "índice", "explain"],
        "titulo": "Optimización SQL",
        "respuesta": """Checklist de optimización:

1. Usa EXPLAIN para revisar el plan de ejecución.
2. Agrega índices donde filtras o haces JOIN.
3. Evita SELECT *.
4. Pagina resultados grandes.
5. Revisa consultas repetidas.
6. Evita funciones sobre columnas indexadas en WHERE.
7. Mide antes y después.

Ejemplo:

EXPLAIN SELECT * FROM productos WHERE code = 'ABC123';

Índice:

CREATE INDEX idx_productos_code ON productos(code);"""
    },

    "diseno": {
        "keywords": ["diseno db", "diseño db", "diseno base", "diseño base", "modelo datos", "normalizar tabla"],
        "titulo": "Diseño de base de datos",
        "respuesta": """Reglas base:

1. Usa nombres consistentes.
2. Define llaves primarias.
3. Agrega relaciones claras.
4. Usa tipos correctos.
5. Normaliza hasta donde tenga sentido.
6. Agrega created_at y updated_at si aplica.
7. Usa deleted_at si necesitas Soft Delete.
8. Documenta relaciones importantes.

Ejemplo:

usuarios
- id
- nombre
- email
- created_at
- updated_at

proyectos
- id
- usuario_id
- nombre
- status
- created_at
- updated_at"""
    },

    "transacciones": {
        "keywords": ["transaccion", "transacción", "acid", "commit", "rollback"],
        "titulo": "Integridad de datos",
        "respuesta": """Transacción SQL:

START TRANSACTION;

UPDATE inventario
SET stock = stock - 1
WHERE producto_id = 10;

INSERT INTO ventas(producto_id, cantidad)
VALUES (10, 1);

COMMIT;

Si algo falla:

ROLLBACK;

ACID:
- Atomicidad
- Consistencia
- Aislamiento
- Durabilidad

Uso recomendado:
Operaciones donde varios cambios deben guardarse juntos o ninguno."""
    },

    "seguridad": {
        "keywords": ["seguridad", "injection", "inyeccion", "inyección", "sql injection", "password", "root"],
        "titulo": "Seguridad en base de datos",
        "respuesta": """Protección básica:

1. Usa prepared statements.
2. No concatenes input de usuario.
3. El usuario de la app no debe ser root.
4. Hashea passwords con Argon2 o bcrypt.
5. Limita permisos por usuario.
6. No expongas credenciales en el código.
7. Usa variables de entorno.
8. Registra cambios sensibles.

Ejemplo inseguro:

SELECT * FROM usuarios WHERE email = '$email';

Mejor:
Usar parámetros preparados desde backend."""
    },

    "escalabilidad": {
        "keywords": ["escalabilidad", "sharding", "replicacion", "replicación", "cluster", "replica", "réplica"],
        "titulo": "Escalabilidad de datos",
        "respuesta": """Estrategias:

1. Réplicas para lectura.
2. Cache para datos frecuentes.
3. Particionamiento si el volumen lo exige.
4. Colas para trabajos pesados.
5. Monitoreo antes de escalar.
6. Índices bien planeados.
7. Archivado de datos históricos.

Recomendación:
No escales a ciegas. Primero mide cuello de botella."""
    },

    "avanzadas": {
        "keywords": ["cte", "window function", "subconsulta", "rank", "row_number", "partition by"],
        "titulo": "Consultas avanzadas",
        "respuesta": """Técnicas útiles:

1. CTEs para organizar consultas complejas.
2. Window functions para ranking, acumulados y comparaciones.
3. Subconsultas cuando simplifican la lectura.
4. GROUP BY para agregados.
5. HAVING para filtrar agregados.

Ejemplo:

WITH ventas_mes AS (
    SELECT cliente_id, SUM(total) AS total_mes
    FROM ventas
    GROUP BY cliente_id
)
SELECT *
FROM ventas_mes
WHERE total_mes > 10000;"""
    },

    "errores": {
        "keywords": ["error sql", "error mysql", "unknown column", "duplicate entry", "foreign key", "constraint", "syntax error"],
        "titulo": "Errores comunes SQL/MySQL",
        "respuesta": """Errores comunes:

Unknown column:
- La columna no existe.
- Está mal escrita.
- Falta alias correcto.

Duplicate entry:
- Estás insertando un valor único repetido.
- Revisa UNIQUE o PRIMARY KEY.

Foreign key constraint:
- Estás insertando un id que no existe en la tabla padre.
- O intentas borrar un registro relacionado.

Syntax error:
- Revisa comas, paréntesis, comillas y palabras reservadas.

Ruta segura:
1. Copia el error completo.
2. Identifica tabla y columna.
3. Ejecuta una consulta pequeña.
4. Corrige una cosa a la vez."""
    },

    "auditoria": {
        "keywords": ["auditoria", "auditoría", "logs", "historial", "bitacora", "bitácora"],
        "titulo": "Auditoría de datos",
        "respuesta": """Auditoría recomendada:

1. Guardar quién hizo el cambio.
2. Guardar fecha y hora.
3. Guardar acción realizada.
4. Guardar valor anterior y valor nuevo si aplica.
5. Usar tabla de historial para datos críticos.

Ejemplo:

auditoria
- id
- usuario_id
- tabla
- registro_id
- accion
- valor_anterior
- valor_nuevo
- created_at"""
    },
}


def detectar_sql(texto):
    texto = normalizar(texto)

    palabras_base = [
        "sql",
        "mysql",
        "base de datos",
        "bd",
        "database",
        "tabla",
        "consulta",
        "select",
        "insert",
        "update",
        "delete",
        "backup",
        "migracion",
        "migración",
    ]

    if not any(palabra in texto for palabra in palabras_base):
        return None

    for tema in SQL_TEMAS.values():
        if any(keyword in texto for keyword in tema["keywords"]):
            return tema["titulo"], tema["respuesta"]

    return (
        "SQL/MySQL",
        """Puedo ayudarte con SQL y bases de datos.

Opciones disponibles:

- Consultas SELECT
- JOINs
- Backups
- Restauración
- Migraciones
- Optimización
- Índices
- Transacciones
- Seguridad
- Auditoría
- Errores comunes
- Diseño de tablas
- Escalabilidad

Ejemplo:
ayúdame con una consulta SQL
tengo error duplicate entry
cómo hago backup de MySQL
cómo optimizo una consulta lenta"""
    )
