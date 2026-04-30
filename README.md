# VitraMind AI

Asistente inteligente en Python para Areli, pensado para trabajo diario de programacion, organizacion y soporte tecnico.

## Que hace

- Entiende texto con o sin acentos gracias a normalizacion de entrada.
- Detecta intencion: pregunta, peticion, accion, conversacion o debugging.
- Corrige dedazos comunes como `ahcer`, `poryecto`, `poidemos`, `werb`.
- Detecta energia: normal, cansada, focus o creativa.
- Detecta formato esperado: corto, ejemplo, codigo, plan o acompanado.
- Prioriza respuestas por modulo para evitar ruido.
- Agrega diagnostico rapido cuando detecta errores.
- Tiene una version movil en React Native con interfaz de chat.
- Muestra etiquetas de entendimiento y acciones sugeridas en cada respuesta.
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
- Selector de tono: Normal, Cansada, Focus y Creativa.
- Panel de entendimiento: tema, energia y formato detectado.
- Acciones sugeridas despues de cada respuesta.
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
