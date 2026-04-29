def detectar_proyecto(texto):
    texto = texto.lower()

    if "diseño" in texto or "ui" in texto or "interfaz" in texto:
        return "Diseño UI", """Para mejorar una vista:
1. Orden visual
2. Menos saturación
3. Jerarquía clara
4. Colores consistentes
5. Espaciado uniforme"""

    if "modulo" in texto or "módulo" in texto:
        return "Módulo", """Para crear un módulo:
1. Ruta
2. Controlador
3. Modelo
4. Migración
5. Vista
6. Validaciones"""

    if "reporte" in texto or "pdf" in texto or "excel" in texto:
        return "Reportes", """Para reportes:
1. Filtros
2. Datos limpios
3. Exportar PDF
4. Exportar Excel
5. Vista previa"""

    return None