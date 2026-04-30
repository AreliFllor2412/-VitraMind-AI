from modulos.inteligencia import normalizar


def detectar_proyecto(texto):
    texto = normalizar(texto)

    if "diseno" in texto or "ui" in texto or "interfaz" in texto:
        return "Diseno UI", """Para mejorar una vista:
1. Jerarquia clara.
2. Menos saturacion visual.
3. Espaciado consistente.
4. Contraste legible.
5. Estados de carga, error y vacio."""

    if "modulo" in texto:
        return "Modulo", """Para crear un modulo:
1. Ruta.
2. Controlador o servicio.
3. Modelo o entidad.
4. Migracion si hay DB.
5. Vista o endpoint.
6. Validaciones y pruebas."""

    if "reporte" in texto or "pdf" in texto or "excel" in texto:
        return "Reportes", """Checklist de reporte:
1. Filtros claros.
2. Datos limpios.
3. Totales si aplica.
4. Exportar PDF/Excel.
5. Vista previa antes de descargar."""

    return None
