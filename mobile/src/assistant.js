const QUICK_AREAS = [
  "Debug",
  "React Native",
  "SQL",
  "Git",
  "Seguridad",
  "Tareas",
  "Emociones",
  "Prompts",
];

const SUGGESTIONS = [
  "Tengo un error en React Native",
  "Ayudame a ordenar mis tareas",
  "Como protejo un login con JWT",
  "Necesito mejorar una pantalla",
];

function normalize(text) {
  return text
    .trim()
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "");
}

function hasAny(text, words) {
  return words.some((word) => text.includes(word));
}

function detectIntent(text) {
  const clean = normalize(text);

  if (hasAny(clean, ["error", "bug", "falla", "no funciona", "undefined", "traceback"])) {
    return "debug";
  }

  if (hasAny(clean, ["quiero", "necesito", "ayudame", "puedes", "hazme", "mejora"])) {
    return "request";
  }

  if (clean.endsWith("?") || clean.startsWith("como ") || clean.startsWith("que ")) {
    return "question";
  }

  return "conversation";
}

function humanOpening(intent) {
  if (intent === "debug") {
    return "Va, respiremos tantito. Esto parece algo que podemos aislar por partes.";
  }

  if (intent === "request") {
    return "Si, Areli. Lo aterrizo contigo en pasos claros para que no se sienta enorme.";
  }

  if (intent === "question") {
    return "Buena pregunta. Te contesto directo y con una ruta practica.";
  }

  return "Aqui estoy. Te leo y vamos ordenando la idea.";
}

const modules = [
  {
    area: "React Native",
    score: 98,
    match: (text) => hasAny(text, ["react native", "expo", "android", "ios", "app movil", "movil"]),
    reply: () => ({
      title: "Base movil",
      body: [
        "Para React Native revisa tres capas:",
        "1. Pantalla: layout, estados y navegacion.",
        "2. Logica: funciones puras para responder y validar.",
        "3. Experiencia: mensajes cortos, botones claros y feedback inmediato.",
        "",
        "Si es Expo, empieza con `npm install` y luego `npm run start` dentro de `mobile`.",
      ].join("\n"),
    }),
  },
  {
    area: "Debug",
    score: 96,
    match: (text) => hasAny(text, ["error", "bug", "falla", "no funciona", "undefined", "exception"]),
    reply: () => ({
      title: "Diagnostico",
      body: [
        "Metodo de debug:",
        "1. Copia el error exacto.",
        "2. Ubica archivo y linea.",
        "3. Recuerda el ultimo cambio.",
        "4. Reduce el caso a una prueba pequena.",
        "5. Cambia una cosa y vuelve a probar.",
      ].join("\n"),
    }),
  },
  {
    area: "Seguridad",
    score: 92,
    match: (text) => hasAny(text, ["seguridad", "jwt", "token", "password", "contrasena", "owasp", "xss"]),
    reply: () => ({
      title: "Proteccion",
      body: [
        "Checklist de seguridad:",
        "1. No guardes datos sensibles en el token.",
        "2. Usa expiracion corta y refresh token.",
        "3. Guarda sesiones en cookies HttpOnly si es web.",
        "4. Hashea passwords con Argon2 o bcrypt.",
        "5. Valida permisos en backend, no solo en UI.",
      ].join("\n"),
    }),
  },
  {
    area: "SQL",
    score: 88,
    match: (text) => hasAny(text, ["sql", "mysql", "consulta", "base de datos", "migracion", "backup"]),
    reply: () => ({
      title: "Base de datos",
      body: [
        "Para SQL vamos por orden:",
        "1. Confirma tabla y columnas.",
        "2. Revisa filtros y joins.",
        "3. Usa `EXPLAIN` si esta lento.",
        "4. Agrega indices donde filtras mucho.",
        "5. Haz backup antes de cambios grandes.",
      ].join("\n"),
    }),
  },
  {
    area: "Git",
    score: 82,
    match: (text) => hasAny(text, ["git", "commit", "pull", "push", "merge", "rebase", "rama"]),
    reply: () => ({
      title: "Flujo seguro",
      body: [
        "Flujo recomendado:",
        "1. `git status`",
        "2. `git pull`",
        "3. `git add .`",
        "4. `git commit -m \"feat: cambio claro\"`",
        "5. `git push`",
      ].join("\n"),
    }),
  },
  {
    area: "Emociones",
    score: 80,
    match: (text) => hasAny(text, ["estres", "cansada", "triste", "frustrada", "ansiedad", "agotada"]),
    reply: () => ({
      title: "Pausa inteligente",
      body: [
        "Te escucho. Antes de exigirnos mas, bajemos el ruido:",
        "1. Una respiracion lenta.",
        "2. Una frase: que esta pasando.",
        "3. Una accion pequena: que sigue ahora.",
        "",
        "No tienes que cargar todo el proyecto en la cabeza a la vez.",
      ].join("\n"),
    }),
  },
  {
    area: "Tareas",
    score: 76,
    match: (text) => hasAny(text, ["tarea", "pendiente", "organizar", "ordenar", "prioridad"]),
    reply: () => ({
      title: "Plan de accion",
      body: [
        "Ordenemos por impacto:",
        "1. Urgente y bloqueante.",
        "2. Importante para entregar.",
        "3. Rapido de cerrar.",
        "4. Puede esperar.",
        "",
        "Elige una sola tarea para iniciar y define como sabras que quedo lista.",
      ].join("\n"),
    }),
  },
  {
    area: "Prompts",
    score: 70,
    match: (text) => hasAny(text, ["prompt", "ia", "chatgpt", "instruccion"]),
    reply: () => ({
      title: "Prompt claro",
      body: [
        "Usa esta estructura:",
        "Actua como [rol].",
        "Necesito [objetivo].",
        "Contexto: [proyecto, archivo, restriccion].",
        "Entrega: [formato esperado].",
        "Verifica: [criterios de calidad].",
      ].join("\n"),
    }),
  },
];

function buildFallback(text, intent) {
  const clean = normalize(text);

  if (clean === "hola" || clean.includes("hola")) {
    return {
      title: "Hola, Areli",
      area: "Conversacion",
      body: "Hola, Areli. Me da gusto leerte. Dime que quieres construir, arreglar o pensar y lo hacemos paso por paso.",
    };
  }

  return {
    title: "Siguiente paso",
    area: "General",
    body: [
      "Para ayudarte mejor, lo convierto en una ruta simple:",
      "1. Que quieres lograr.",
      "2. Que tienes ahora.",
      "3. Que te esta bloqueando.",
      "4. Que archivo, pantalla o modulo toca revisar.",
      "5. Como verificamos que quedo bien.",
      "",
      "Dame cualquiera de esos datos y sigo contigo.",
    ].join("\n"),
  };
}

function respond(text, history = []) {
  const clean = normalize(text);
  const intent = detectIntent(text);
  const matches = modules
    .filter((module) => module.match(clean))
    .sort((a, b) => b.score - a.score)
    .slice(0, 3)
    .map((module) => ({ ...module.reply(text), area: module.area }));

  const primary = matches[0] || buildFallback(text, intent);
  const extras = matches.slice(1);
  const recent = history
    .filter((item) => item.role === "user")
    .slice(-2)
    .map((item) => item.text);

  const contextLine = recent.length
    ? `\n\nContexto que tengo presente:\n- ${recent.join("\n- ")}`
    : "";

  const extraLine = extras.length
    ? `\n\nTambien detecte:\n${extras.map((item) => `- ${item.area}: ${item.title}`).join("\n")}`
    : "";

  return {
    area: primary.area,
    title: primary.title,
    text: `${humanOpening(intent)}\n\n${primary.body}${extraLine}${contextLine}`,
  };
}

export { QUICK_AREAS, SUGGESTIONS, respond };
