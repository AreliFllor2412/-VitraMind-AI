from modulos.inteligencia import normalizar


def _contiene(texto, palabras):
    return any(palabra in texto for palabra in palabras)


def detectar_seguridad(texto):
    texto = normalizar(texto)

    if _contiene(texto, [
        "owasp", "vulnerabilidad", "ataque", "hacker",
        "pentest", "penetracion", "xss", "csrf",
        "rce", "ssrf", "idor", "lfi", "rfi"
    ]):
        return "Seguridad Web (OWASP)", """OWASP Top 10

1. Broken Access Control.
2. Cryptographic Failures.
3. Injection (SQL, NoSQL, OS, LDAP).
4. Insecure Design.
5. Security Misconfiguration.
6. Vulnerable Components.
7. Authentication Failures.
8. Software & Data Integrity Failures.
9. Logging and Monitoring Failures.
10. Server-Side Request Forgery (SSRF).

Buenas prácticas:
• Mantén dependencias actualizadas.
• Valida toda entrada del usuario.
• Usa el principio de mínimo privilegio.
• Registra eventos críticos.
"""

    if _contiene(texto, [
        "jwt", "token", "bearer",
        "sesion", "session", "refresh token"
    ]):
        return "Autenticación y JWT", """Buenas prácticas

• Usa HTTPS siempre.
• Tokens con expiración corta.
• Implementa Refresh Token.
• Rota Refresh Tokens.
• Valida firma, issuer y audience.
• No guardes información sensible en el payload.
• Usa HttpOnly + Secure Cookies cuando sea posible.
• Revoca tokens comprometidos.
"""

    if _contiene(texto, [
        "password", "contrasena", "contraseña",
        "hash", "bcrypt", "argon2",
        "encriptar", "cifrar"
    ]):
        return "Contraseñas y Criptografía", """Checklist

✔ Usa Argon2id o bcrypt.
✔ Genera un Salt automáticamente.
✔ Nunca guardes contraseñas en texto plano.
✔ No uses MD5.
✔ No uses SHA1.
✔ Usa claves largas y únicas.
✔ Considera MFA para cuentas importantes.
"""

    if _contiene(texto, [
        "https", "ssl", "tls", "certificado"
    ]):
        return "HTTPS y TLS", """Comunicación segura

• Usa TLS 1.2 o TLS 1.3.
• Deshabilita SSL antiguos.
• Configura HSTS.
• Fuerza HTTPS.
• Usa certificados válidos.
• Renueva certificados antes de expirar.
• Activa Perfect Forward Secrecy cuando sea posible.
"""

    if _contiene(texto, [
        "sql injection", "inyeccion sql",
        "inyeccion", "prepared statement"
    ]):
        return "SQL Injection", """Prevención

✔ Usa Prepared Statements.
✔ Usa parámetros enlazados.
✔ Nunca concatenes SQL.
✔ Valida entradas.
✔ Limita permisos del usuario de BD.
✔ Registra intentos sospechosos.

Incorrecto:

SELECT * FROM usuarios
WHERE email='""" + "' + email + '" + """';

Correcto:

SELECT * FROM usuarios
WHERE email = ?;
"""

    if _contiene(texto, [
        "xss", "cross site scripting"
    ]):
        return "Cross Site Scripting (XSS)", """Prevención

• Escapa HTML.
• Sanitiza entradas.
• Usa Content Security Policy.
• Evita innerHTML cuando sea posible.
• Valida datos del usuario.
• Usa frameworks actualizados.
"""

    if _contiene(texto, [
        "csrf", "cross site request forgery"
    ]):
        return "CSRF", """Protección

• Usa CSRF Tokens.
• Cookies SameSite.
• Valida origen de la petición.
• Usa HTTPS.
• Evita peticiones sensibles por GET.
"""

    if _contiene(texto, [
        "cors", "cross origin"
    ]):
        return "CORS", """Configuración segura

• No uses Access-Control-Allow-Origin: *
• Permite solo dominios autorizados.
• Restringe métodos HTTP.
• Restringe encabezados.
• Usa credenciales solo cuando sea necesario.
"""

    if _contiene(texto, [
        "api key", "apikey", "secret",
        "credenciales", "token github"
    ]):
        return "Secretos y Credenciales", """Buenas prácticas

• Nunca subas secretos a Git.
• Usa variables de entorno.
• Rota credenciales periódicamente.
• Usa gestores de secretos.
• Revoca claves comprometidas.
• Agrega .env al .gitignore.
"""

    if _contiene(texto, [
        "firewall", "waf", "ddos"
    ]):
        return "Protección de Infraestructura", """Checklist

• Firewall configurado.
• WAF para aplicaciones web.
• Protección DDoS.
• IDS/IPS.
• Monitoreo continuo.
• Backups periódicos.
"""

    if _contiene(texto, [
        "backup", "respaldo",
        "recuperacion", "restore"
    ]):
        return "Respaldo y Recuperación", """Buenas prácticas

• Haz respaldos automáticos.
• Prueba restauraciones.
• Guarda copias fuera del servidor.
• Cifra los respaldos.
• Documenta el proceso de recuperación.
"""

    if _contiene(texto, [
        "docker", "contenedor",
        "kubernetes", "k8s"
    ]):
        return "Seguridad en Contenedores", """Checklist

✔ Usa imágenes oficiales.
✔ No ejecutes como root.
✔ Mantén imágenes actualizadas.
✔ Escanea vulnerabilidades.
✔ Usa secretos seguros.
✔ Limita capacidades del contenedor.
"""

    if _contiene(texto, [
        "linux", "servidor",
        "ssh", "ubuntu"
    ]):
        return "Seguridad en Servidores", """Checklist

• Deshabilita acceso root por SSH.
• Usa autenticación por llaves.
• Cambia el puerto SSH si aplica.
• Mantén el sistema actualizado.
• Configura Fail2Ban.
• Revisa logs periódicamente.
"""

    if _contiene(texto, [
        "auditoria", "logs",
        "monitor", "monitoreo"
    ]):
        return "Auditoría y Monitoreo", """Buenas prácticas

• Registra accesos.
• Registra errores.
• Monitorea intentos fallidos.
• Conserva logs importantes.
• Configura alertas.
• Centraliza registros.
"""

    return None
