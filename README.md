# Contador de Letras

Un programa simple para contar el número de letras alfabéticas en una frase. Ignora espacios, números y signos de puntuación.

## Descripción

Este programa cuenta las letras (a-z, A-Z) en cualquier frase que introduzcas. Es interactivo y continúa pidiendo frases hasta que escribas 'salir'.

## Requisitos

- Python 3.x instalado en tu sistema.

## Instalación

1. Clona o descarga este repositorio.
2. Asegúrate de tener Python 3 instalado.

## Uso

Ejecuta el programa desde la línea de comandos:

```bash
python main.py
```

O si tienes permisos de ejecución:

```bash
chmod +x main.py
./main.py
```

### Ejemplo de ejecución

```
Bienvenido a la aplicación de conteo de letras.
Ingresa una frase (o 'salir' para terminar): Hola mundo!
El número de letras en la frase es: 10
Ingresa una frase (o 'salir' para terminar): salir
¡Hasta luego!
```

## Tests

Para ejecutar los tests unitarios:

```bash
python3 -m unittest test_main.py
```

Los tests verifican la función `contar_letras` con varios casos: cadena vacía, solo letras, con espacios, números, puntuación, etc.

## Funcionalidades

- Cuenta solo letras alfabéticas.
- Interactivo: pide frases repetidamente.
- Termina con 'salir' (case-insensitive).

## Versión en JavaScript

También hay una versión en JavaScript (`main.js`) que requiere Node.js:

```bash
node main.js
```

## Contribuir

Si quieres mejorar el programa, ¡haz un fork y envía un pull request!

## Licencia

Este proyecto está bajo la licencia MIT.