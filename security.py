from modulos.inteligencia import normalizar


def detectar_seguridad(texto):
    texto = normalizar(texto)

    if any(p in texto for p in ["vulnerabilidad", "owasp", "ataque", "hacker", "xss", "csrf"]):
        return "Seguridad ofensiva/defensiva", """Checklist OWASP:
1. Inyeccion SQL/NoSQL/OS.
2. Autenticacion rota.
3. Exposicion de datos sensibles.
4. Control de acceso roto.
5. Configuracion insegura.
6. XSS.
7. Componentes vulnerables.
8. Logs y monitoreo insuficientes."""

    if "jwt" in texto or "token" in texto or "sesion" in texto:
        return "Identidad y autenticacion", """Buenas practicas JWT:
1. No guardes datos sensibles en el payload.
2. Usa expiracion corta.
3. Usa HttpOnly cookies si es una app web.
4. Implementa refresh tokens con rotacion.
5. Valida issuer, audience y firma."""

    if "hash" in texto or "password" in texto or "contrasena" in texto or "encriptar" in texto:
        return "Criptografia aplicada", """Regla de oro:
1. No uses MD5 ni SHA1 para passwords.
2. Usa Argon2 o bcrypt.
3. Agrega salt.
4. Nunca guardes passwords en texto plano."""

    if "https" in texto or "ssl" in texto or "tls" in texto:
        return "Comunicacion segura", """Recomendaciones HTTPS:
1. Usa TLS 1.2 o superior.
2. Configura HSTS.
3. Usa certificados confiables.
4. Deshabilita SSLv3 y TLS antiguos.
5. Revisa renovacion de certificados."""

    return None
