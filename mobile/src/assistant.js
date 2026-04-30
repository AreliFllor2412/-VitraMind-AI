const QUICK_AREAS = [
  "Debug",
  "React Native",
  "SQL",
  "Git",
  "Seguridad",
  "Tareas",
  "Sueno",
  "Ideas",
  "Prompts",
];

const USER_MODES = [
  {
    id: "normal",
    label: "Normal",
    description: "Equilibrio entre calidez y pasos practicos.",
  },
  {
    id: "cansada",
    label: "Cansada",
    description: "Respuestas suaves, cortas y con mini avances.",
  },
  {
    id: "focus",
    label: "Focus",
    description: "Directo al siguiente paso, con menos vuelta.",
  },
  {
    id: "creativa",
    label: "Creativa",
    description: "Mas ideas, variantes y mejoras visuales.",
  },
];

const SUGGESTIONS = [
  "Tengo un error en React Native",
  "Tengo sueno pero quiero avanzar",
  "Ayudame a ordenar mis tareas",
  "Como protejo un login con JWT",
  "Necesito mejorar una pantalla",
  "Que podemos agregar a la app",
];

const FEATURE_IDEAS = [
  "Modo energia: respuestas distintas si estas cansada, apurada o tranquila.",
  "Memoria por proyecto: guardar contexto de React Native, Laravel, SQL o Vitra.",
  "Favoritos: marcar una respuesta que si te sirvio para volver a verla.",
  "Plantillas: prompts rapidos para commits, bugs, UI, SQL y seguridad.",
  "Modo voz: dictar preguntas como las piensas, sin escribir perfecto.",
  "Boton de salida: convertir una respuesta en checklist, codigo o resumen.",
  "Panel de datos: detectar tecnologia, urgencia, emocion y siguiente accion.",
];

const TYPO_FIXES = [
  ["ahcer", "hacer"],
  ["aser", "hacer"],
  ["ouedo", "puedo"],
  ["pudeo", "puedo"],
  ["poidemos", "podemos"],
  ["podemso", "podemos"],
  ["entendiemnto", "entendimiento"],
  ["poryecto", "proyecto"],
  ["repsuetsa", "respuesta"],
  ["pregu8ntas", "preguntas"],
  ["preg8ntas", "preguntas"],
  ["werb", "web"],
  ["reac native", "react native"],
  ["condiseno", "con diseno"],
  ["dise;o", "diseno"],
  ["qiero", "quiero"],
  ["nesecito", "necesito"],
  ["alluda", "ayuda"],
];

const TOPICS = [
  {
    id: "ideas",
    area: "Ideas",
    score: 104,
    words: ["que podemos agregar", "que le agrego", "ideas", "nuevas funciones", "mas cosas", "aumenta", "mejoralo"],
  },
  {
    id: "understanding",
    area: "Entendimiento",
    score: 103,
    words: ["entendimiento", "entiende", "datos", "contexto", "preguntas", "forma de preguntar"],
  },
  {
    id: "design",
    area: "Diseno",
    score: 100,
    words: ["diseno", "bonito", "ui", "interfaz", "pantalla", "visual", "colores"],
  },
  {
    id: "reactNative",
    area: "React Native",
    score: 98,
    words: ["react native", "expo", "android", "ios", "app movil", "movil"],
  },
  {
    id: "debug",
    area: "Debug",
    score: 96,
    words: ["error", "bug", "falla", "no funciona", "undefined", "exception", "traceback"],
  },
  {
    id: "security",
    area: "Seguridad",
    score: 92,
    words: ["seguridad", "jwt", "token", "password", "contrasena", "owasp", "xss"],
  },
  {
    id: "sql",
    area: "SQL",
    score: 88,
    words: ["sql", "mysql", "consulta", "base de datos", "migracion", "backup"],
  },
  {
    id: "sleep",
    area: "Sueno",
    score: 86,
    words: ["sueno", "dormida", "cansancio", "desvelada", "sin energia", "me duermo"],
  },
  {
    id: "git",
    area: "Git",
    score: 82,
    words: ["git", "commit", "pull", "push", "merge", "rebase", "rama"],
  },
  {
    id: "emotion",
    area: "Emociones",
    score: 80,
    words: ["estres", "cansada", "triste", "frustrada", "ansiedad", "agotada"],
  },
  {
    id: "tasks",
    area: "Tareas",
    score: 76,
    words: ["tarea", "pendiente", "organizar", "ordenar", "prioridad"],
  },
  {
    id: "prompts",
    area: "Prompts",
    score: 70,
    words: ["prompt", "ia", "chatgpt", "instruccion"],
  },
];

const REPLIES = {
  ideas: {
    title: "Crecimiento del proyecto",
    body: [
      "Si vamos a aumentar todo el proyecto, yo lo separaria en capas para que crezca bonito y no se vuelva un monton de parches.",
      "",
      "Primero: entendimiento. Que detecte tema, emocion, urgencia, tecnologia y tipo de respuesta.",
      "Segundo: datos. Que tenga memoria por proyecto, favoritos y plantillas.",
      "Tercero: experiencia. Que puedas elegir tono: suave, directo, creativo o tecnico.",
      "",
      "Mi siguiente mejora fuerte seria un panel de perfil: `Areli esta cansada`, `trabaja en React Native`, `prefiere ejemplos`, `quiere respuestas humanas`.",
    ].join("\n"),
    actions: ["Crear memoria por proyecto", "Agregar favoritos", "Agregar modo voz"],
  },
  understanding: {
    title: "Entender mejor tus preguntas",
    body: [
      "Tu forma de escribir trae mucha informacion: cuando dices `todo`, `aumenta`, `haslo`, normalmente quieres accion, no teoria.",
      "",
      "Entonces la IA debe leer senales, no solo palabras exactas:",
      "- Si hay dedazos, corregirlos sin molestarte.",
      "- Si dices `porfa`, responder mas cercano.",
      "- Si dices `todo el proyecto`, proponer capas y ejecutar por partes.",
      "- Si mencionas `datos`, pensar en memoria, perfil y contexto.",
      "",
      "Eso ya lo estoy reforzando en el motor.",
    ].join("\n"),
    actions: ["Detectar dedazos", "Leer urgencia", "Pedir solo el dato que falta"],
  },
  design: {
    title: "Diseno con calma y claridad",
    body: [
      "La app debe sentirse como un lugar donde puedes pensar, no como una pantalla llena de cajas.",
      "",
      "Yo cuidaria tres detalles: aire entre burbujas, acciones visibles y paneles que expliquen que entendio la IA.",
      "",
      "Ejemplo: despues de tu mensaje, mostrar pequenas etiquetas como `React Native`, `mejora`, `energia baja`. Eso da confianza porque ves que la IA si te leyo.",
    ].join("\n"),
    actions: ["Mostrar etiquetas", "Mejorar panel lateral", "Agregar selector de tono"],
  },
  reactNative: {
    title: "Base movil mas fuerte",
    body: [
      "Para React Native, el proyecto puede crecer con una estructura mas clara: componentes, motor de IA y datos separados.",
      "",
      "Lo bonito seria que App.js se encargue de la pantalla, assistant.js de pensar, y luego tengamos un archivo de datos para plantillas, tecnologias y perfiles.",
      "",
      "Asi la app no se rompe cuando agreguemos mas areas.",
    ].join("\n"),
    actions: ["Separar componentes", "Crear datos base", "Preparar historial"],
  },
  debug: {
    title: "Debug sin abrumarte",
    body: [
      "Va. Si hay error, lo volvemos pequeno.",
      "",
      "No necesito que resuelvas todo ahora. Necesito una pista: mensaje exacto, archivo o que cambiaste antes de que fallara.",
      "",
      "Si estas cansada, el avance minimo es copiar el error y dejarlo listo. A veces eso ya salva media hora manana.",
    ].join("\n"),
    actions: ["Pegar error", "Ubicar archivo", "Revisar ultimo cambio"],
  },
  security: {
    title: "Seguridad practica",
    body: [
      "Seguridad no es meter miedo; es cerrar puertas obvias antes de que duelan.",
      "",
      "Para login: passwords con bcrypt o Argon2, token con expiracion, permisos validados en backend y nada sensible en texto plano.",
      "",
      "Ejemplo: ocultar un boton en la app no protege el endpoint. La seguridad real vive en el backend.",
    ].join("\n"),
    actions: ["Revisar tokens", "Validar permisos", "Proteger passwords"],
  },
  sql: {
    title: "Datos y base de datos",
    body: [
      "Si hablamos de datos, hay dos mundos: los datos de tu app y los datos que la IA recuerda.",
      "",
      "Para SQL: tablas claras, indices donde filtras, backup antes de tocar datos reales.",
      "",
      "Para la IA: memoria por proyecto, historial de decisiones y etiquetas automaticas para encontrar conversaciones importantes.",
    ].join("\n"),
    actions: ["Disenar memoria", "Guardar historial", "Etiquetar temas"],
  },
  sleep: {
    title: "Modo energia baja",
    body: [
      "Si tienes sueno, no te voy a mandar a conquistar el mundo ahorita.",
      "",
      "Hagamos una version ligera: agua, brillo bajo, una mini tarea de 10 minutos y una nota de lo que queda pendiente.",
      "",
      "Ejemplo real: `abrir App.js, leer el bloque que falla, escribir sospecha`. Eso cuenta. No todo avance tiene que ser heroico.",
    ].join("\n"),
    actions: ["Mini tarea", "Dejar nota", "Cerrar una cosa"],
  },
  git: {
    title: "Git con ritual tranquilo",
    body: [
      "Git se vuelve mas amable si siempre haces el mismo ritual.",
      "",
      "`git status` para ver el mapa, `git add` para elegir, `git commit` para guardar, `git push` para compartir.",
      "",
      "Para este cambio quedaria algo como: `feat: expand assistant understanding and human responses`.",
    ].join("\n"),
    actions: ["Ver status", "Preparar commit", "Escribir mensaje"],
  },
  emotion: {
    title: "Calma antes de velocidad",
    body: [
      "Te escucho. Si el proyecto se siente grande, no significa que estes atrasada; significa que necesitamos partirlo mejor.",
      "",
      "Una pregunta amable: que parte te pesa mas ahora, el diseno, la logica, los datos o no saber por donde seguir?",
    ].join("\n"),
    actions: ["Bajar presion", "Elegir una parte", "Avanzar 10 minutos"],
  },
  tasks: {
    title: "Orden sin hacerlo enorme",
    body: [
      "Vamos a ordenar por energia y por impacto.",
      "",
      "Si tienes energia: toca la parte dificil. Si estas cansada: cierra algo pequeno. Si estas bloqueada: escribe la duda exacta.",
      "",
      "La app puede ayudarte mostrando una lista viva de `ahora`, `despues` y `cuando tenga energia`.",
    ].join("\n"),
    actions: ["Ahora", "Despues", "Cuando tenga energia"],
  },
  prompts: {
    title: "Prompts con tono humano",
    body: [
      "Un prompt util puede sonar simple.",
      "",
      "`Actua como dev senior. Mira esta pantalla. Mejorala sin romper logica. Explicame claro y dame codigo listo.`",
      "",
      "Y si quieres cercania: `respondeme como si estuvieras trabajando conmigo, no como manual tecnico`.",
    ].join("\n"),
    actions: ["Hacerlo claro", "Pedir codigo", "Pedir ejemplo"],
  },
};

function normalize(text) {
  let clean = text
    .trim()
    .toLowerCase()
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[¿?¡!.,;:]+/g, " ")
    .replace(/\s+/g, " ");

  TYPO_FIXES.forEach(([from, to]) => {
    clean = clean.replace(new RegExp(`\\b${from}\\b`, "g"), to);
  });

  return clean;
}

function hasAny(text, words) {
  return words.some((word) => text.includes(word));
}

function detectIntent(clean) {
  if (hasAny(clean, ["error", "bug", "falla", "no funciona", "undefined", "traceback"])) {
    return "debug";
  }
  if (hasAny(clean, ["quiero", "necesito", "ayudame", "puedes", "hazme", "mejora", "mejoralo", "haslo"])) {
    return "request";
  }
  if (clean.startsWith("como ") || clean.startsWith("que ") || clean.startsWith("dime ")) {
    return "question";
  }
  return "conversation";
}

function detectEnergy(clean, mode) {
  if (mode === "cansada" || hasAny(clean, ["sueno", "cansada", "agotada", "desvelada", "sin energia"])) {
    return "baja";
  }
  if (mode === "focus" || hasAny(clean, ["rapido", "urgente", "ya", "prisa"])) {
    return "alta";
  }
  if (mode === "creativa" || hasAny(clean, ["ideas", "bonito", "creativo", "diseno"])) {
    return "creativa";
  }
  return "media";
}

function detectOutput(clean) {
  if (hasAny(clean, ["codigo", "code", "programa"])) return "codigo";
  if (hasAny(clean, ["resumen", "corto", "rapido"])) return "corto";
  if (hasAny(clean, ["ejemplo", "como se ve"])) return "ejemplo";
  if (hasAny(clean, ["plan", "pasos"])) return "plan";
  return "acompanado";
}

function analyze(text, mode = "normal") {
  const clean = normalize(text);
  const matches = TOPICS
    .filter((topic) => hasAny(clean, topic.words))
    .sort((a, b) => b.score - a.score);

  return {
    clean,
    intent: detectIntent(clean),
    energy: detectEnergy(clean, mode),
    output: detectOutput(clean),
    topics: matches.length ? matches : [{ id: "general", area: "General", score: 1 }],
  };
}

function opening(analysis) {
  if (analysis.energy === "baja") {
    return "Va, lo hacemos suave. No necesitas resolver todo ahorita; buscamos un avance que no te drene.";
  }
  if (analysis.energy === "alta") {
    return "Va directo. Tomo lo importante y te doy el siguiente movimiento sin rodeos.";
  }
  if (analysis.energy === "creativa") {
    return "Me gusta hacia donde va esto. Pensemos en una version mas bonita, mas util y mas tuya.";
  }
  if (analysis.intent === "debug") {
    return "Va, lo partimos en piezas pequenas para que el error deje de sentirse gigante.";
  }
  if (analysis.intent === "request") {
    return "Si, Areli. Te entendi: quieres que lo aterrice y lo mejore, no solo que te explique.";
  }
  return "Aqui estoy. Te leo como venga la idea y la convierto en algo accionable.";
}

function fallbackReply() {
  return {
    title: "Siguiente paso",
    area: "General",
    body: [
      "Puedo seguirte con una pista pequena.",
      "",
      "Dime algo como:",
      "- `quiero mejorar todo el proyecto`",
      "- `tengo sueno pero quiero avanzar`",
      "- `me sale error en App.js`",
      "- `que datos puede recordar la IA`",
      "",
      "No busco una pregunta perfecta. Busco una entrada para ayudarte.",
    ].join("\n"),
    actions: ["Mejorar proyecto", "Agregar datos", "Hacerlo mas humano"],
  };
}

function formatInsights(analysis) {
  const topicNames = analysis.topics.map((topic) => topic.area).slice(0, 3).join(", ");
  return [
    `Entendi: ${topicNames}`,
    `Energia: ${analysis.energy}`,
    `Formato ideal: ${analysis.output}`,
  ];
}

function nextLine(analysis) {
  if (analysis.energy === "baja") {
    return "Siguiente pasito: elige una cosa pequena y la hacemos sin presion.";
  }
  if (analysis.output === "codigo") {
    return "Siguiente: dime el archivo o componente y lo convertimos en codigo.";
  }
  if (analysis.intent === "debug") {
    return "Siguiente: pegam el error exacto o dime en que archivo aparece.";
  }
  return "Siguiente: puedo darte version corta, version con ejemplo o plan listo para implementar.";
}

function respond(text, history = [], mode = "normal") {
  const analysis = analyze(text, mode);
  const primaryTopic = analysis.topics[0];
  const primary = REPLIES[primaryTopic.id] || fallbackReply();
  const extraTopics = analysis.topics.slice(1, 3);
  const recent = history
    .filter((item) => item.role === "user")
    .slice(-2)
    .map((item) => item.text);

  const extras = extraTopics.length
    ? `\n\nTambien estoy viendo: ${extraTopics.map((topic) => topic.area).join(", ")}.`
    : "";

  const context = recent.length
    ? `\n\nContexto reciente que tengo presente:\n- ${recent.join("\n- ")}`
    : "";

  const insights = formatInsights(analysis);

  return {
    area: primary.area || primaryTopic.area,
    title: primary.title,
    insights,
    actions: primary.actions || [],
    text: `${opening(analysis)}\n\n${primary.body}${extras}${context}\n\n${nextLine(analysis)}`,
  };
}

export { FEATURE_IDEAS, QUICK_AREAS, SUGGESTIONS, USER_MODES, respond };
