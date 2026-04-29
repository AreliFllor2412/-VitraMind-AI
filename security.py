def detectar_seguridad(texto):
    texto = texto.lower()

    if any(p in texto for p in ["vulnerabilidad", "owasp", "ataque", "hacker"]):
        return "Seguridad Ofensiva/Defensiva", """Checklist OWASP Top 10:
1. Inyección (SQL, NoSQL, OS).
2. Autenticación rota.
3. Exposición de datos sensibles.
4. Entidades Externas XML (XXE).
5. Control de acceso roto.
"""

    if "jwt" in texto or "token" in texto or "sesion" in texto:
        return "Manejo de Identidad (Auth)", """Best Practices para JWT:
1. No guardar datos sensibles en el payload (es legible).
2. Usar algoritmos fuertes (RS256).
3. Definir 'Expiration Time' (exp) corto.
4. Usar HttpOnly Cookies para evitar XSS.
5. Implementar Refresh Tokens.
"""

    if "hash" in texto or "password" in texto or "encriptar" in texto:
        return "Criptografía Aplicada", """Regla de Oro:
NUNCA uses MD5 o SHA1 para passwords. 
Implementa Argon2 o BCrypt con un factor de costo adecuado (mínimo 10-12).
"""
    return None