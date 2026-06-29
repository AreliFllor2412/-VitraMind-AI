from modulos.inteligencia import normalizar


PROYECTOS = {
    "ui": {
        "keywords": [
            "diseno",
            "diseño",
            "ui",
            "ux",
            "interfaz",
            "pantalla",
            "dashboard",
            "vista",
        ],
        "titulo": "Diseño UI/UX",
        "respuesta": """Checklist para una interfaz profesional:

✓ Jerarquía visual clara.
✓ Espaciado consistente.
✓ Colores bien definidos.
✓ Tipografía legible.
✓ Responsive.
✓ Estados de carga.
✓ Estados vacíos.
✓ Estados de error.
✓ Animaciones suaves.
✓ Accesibilidad.
✓ Componentes reutilizables.
✓ Diseño consistente."""
    },

    "modulo": {
        "keywords": [
            "modulo",
            "módulo",
            "crear modulo",
            "nuevo modulo",
        ],
        "titulo": "Nuevo módulo",
        "respuesta": """Estructura recomendada:

1. Ruta.
2. Controlador.
3. Servicio.
4. Modelo.
5. Migración.
6. Seeder.
7. Policies.
8. Requests.
9. Vista.
10. API.
11. Validaciones.
12. Tests.

Objetivo:
Cada módulo debe ser independiente y fácil de mantener."""
    },

    "arquitectura": {
        "keywords": [
            "arquitectura",
            "estructura",
            "organizar",
            "proyecto",
        ],
        "titulo": "Arquitectura del proyecto",
        "respuesta": """Arquitectura recomendada:

📁 app
📁 Components
📁 Services
📁 Hooks
📁 Utils
📁 Helpers
📁 Config
📁 Routes
📁 Models
📁 Controllers
📁 Resources
📁 Tests

Principios:

• Responsabilidad única.
• Bajo acoplamiento.
• Alta cohesión.
• Componentes reutilizables.
• Escalable."""
    },

    "reporte": {
        "keywords": [
            "reporte",
            "pdf",
            "excel",
            "csv",
            "descargar",
            "exportar",
        ],
        "titulo": "Sistema de reportes",
        "respuesta": """Checklist profesional:

✓ Filtros.
✓ Ordenamiento.
✓ Búsqueda.
✓ Totales.
✓ Vista previa.
✓ Exportar PDF.
✓ Exportar Excel.
✓ Exportar CSV.
✓ Firmas.
✓ Fecha y hora.
✓ Usuario que generó.
✓ Código del reporte."""
    },

    "api": {
        "keywords": [
            "api",
            "endpoint",
            "rest",
            "json",
            "backend",
        ],
        "titulo": "Diseño de API",
        "respuesta": """Buenas prácticas:

GET
POST
PUT
PATCH
DELETE

Siempre incluir:

✓ Validaciones.
✓ Respuestas HTTP.
✓ Manejo de errores.
✓ Autenticación.
✓ Logs.
✓ Documentación."""
    },

    "database": {
        "keywords": [
            "mysql",
            "base de datos",
            "tabla",
            "database",
            "sql",
            "migracion",
            "migración",
        ],
        "titulo": "Base de datos",
        "respuesta": """Checklist:

✓ Llave primaria.
✓ Índices.
✓ Relaciones.
✓ Foreign Keys.
✓ Restricciones.
✓ Migraciones.
✓ Seeders.
✓ Soft Deletes.
✓ Auditoría.
✓ Respaldos."""
    },

    "ia": {
        "keywords": [
            "ia",
            "inteligencia",
            "chatbot",
            "asistente",
            "modelo",
        ],
        "titulo": "Proyecto IA",
        "respuesta": """Arquitectura sugerida:

Entrada
↓

Normalización

↓

Detección de intención

↓

Detección de tema

↓

Memoria

↓

Motor de respuestas

↓

Respuesta enriquecida

↓

Aprendizaje futuro

Esto facilita agregar nuevas capacidades sin romper el proyecto."""
    },

    "deploy": {
        "keywords": [
            "deploy",
            "produccion",
            "producción",
            "publicar",
            "servidor",
            "hosting",
        ],
        "titulo": "Despliegue",
        "respuesta": """Antes de producción:

✓ Variables de entorno.
✓ Logs.
✓ HTTPS.
✓ Backups.
✓ Cache.
✓ Optimización.
✓ Monitoreo.
✓ Versionado.
✓ Rollback.
✓ CI/CD."""
    },

    "react": {
        "keywords": [
            "react",
            "react native",
            "expo",
            "componente",
        ],
        "titulo": "Proyecto React",
        "respuesta": """Buenas prácticas:

✓ Componentes pequeños.
✓ Hooks personalizados.
✓ Services.
✓ Context.
✓ Lazy Loading.
✓ Memoización.
✓ Responsive.
✓ Estados separados.
✓ Tipado si usas TypeScript."""
    },

    "erp": {
        "keywords": [
            "erp",
            "inventario",
            "almacen",
            "almacén",
            "compras",
            "ventas",
            "produccion",
            "producción",
        ],
        "titulo": "Proyecto ERP",
        "respuesta": """Módulos sugeridos:

✓ Dashboard.
✓ Usuarios.
✓ Inventario.
✓ Producción.
✓ Calidad.
✓ Compras.
✓ Ventas.
✓ Clientes.
✓ Reportes.
✓ Configuración.
✓ Auditoría.
✓ IA integrada."""
    },
}


def detectar_proyecto(texto):
    texto = normalizar(texto)

    for proyecto in PROYECTOS.values():
        if any(keyword in texto for keyword in proyecto["keywords"]):
            return proyecto["titulo"], proyecto["respuesta"]

    return None
