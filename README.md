# VitraMind AI

Asistente inteligente en Python para Areli, pensado para trabajo diario de programacion, organizacion y soporte tecnico.

## Que hace

- Entiende texto con o sin acentos gracias a normalizacion de entrada.
- Detecta intencion: pregunta, peticion, accion, conversacion o debugging.
- Prioriza respuestas por modulo para evitar ruido.
- Agrega diagnostico rapido cuando detecta errores.
- Tiene una version movil en React Native con interfaz de chat.
- Usa memoria de sesion para mostrar contexto reciente.
- Guarda historial en `historial.txt`.
- Maneja tareas, notas, resumenes, calculos, Git, SQL, DevOps, seguridad y soporte emocional.

## Comandos utiles

```txt
ayuda
memoria
limpiar
salir
tarea: revisar login
ver tareas
crear nota recordar revisar backups
leer nota
calcula 10 * (5 + 2)
resume: texto largo...
ordena: punto uno, punto dos, punto tres
```

## Arquitectura

```txt
IA_Areli/
|-- main.py
|-- config.py
|-- security.py
|-- historial.txt
|-- mobile/
|   |-- App.js
|   |-- app.json
|   |-- package.json
|   `-- src/
|       `-- assistant.js
|-- modulos/
|   |-- inteligencia.py
|   |-- emociones.py
|   |-- programacion.py
|   |-- sql.py
|   |-- proyectos.py
|   |-- git.py
|   |-- devops.py
|   |-- horarios.py
|   |-- prompts.py
|   |-- tareas.py
|   |-- calculadora.py
|   |-- archivos.py
|   |-- memoria.py
|   |-- recomendaciones.py
|   `-- texto.py
```

## Ejecutar

```bash
python main.py
```

Si `python` esta bloqueado en Windows, prueba:

```bash
py main.py
```

## App React Native

La app movil vive en `mobile/`. Incluye:

- Chat principal.
- Respuestas mas humanas.
- Accesos rapidos por area.
- Contexto reciente de conversacion.
- Motor local en JavaScript.

Para iniciarla:

```bash
cd mobile
npm install
npm run start
```

Para verla en navegador web:

```bash
cd mobile
npm.cmd run web -- --host localhost --port 8083
```

Abre:

```txt
http://localhost:8083
```
