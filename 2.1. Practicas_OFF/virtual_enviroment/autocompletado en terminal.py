"""
Perfecto 💪 — configurar autocompletado e IntelliSense en VS Code para tu entorno virtual es muy sencillo, pero hay que asegurarse de que todo esté alineado.
Te dejo una guía completa paso a paso 👇

🧠 ¿Qué es IntelliSense?

En VS Code, IntelliSense es la función que te da:

Autocompletado inteligente (te sugiere funciones, clases, etc.).

Información sobre parámetros y documentación.

Subrayado de errores o importaciones faltantes.

Para que funcione bien en Python, VS Code necesita saber qué intérprete (entorno) usar, y así acceder a los módulos instalados ahí (como colorama).

⚙️ Paso 1. Verifica que el entorno .venv esté seleccionado

Presiona Ctrl + Shift + P (o Cmd + Shift + P en macOS).

Escribe y selecciona:

Python: Select Interpreter


Elige el que corresponda a tu proyecto, por ejemplo:

.venv\Scripts\python.exe        ← en Windows
.venv/bin/python                ← en Linux / macOS


💡 Si ves (venv) en la parte inferior derecha de la ventana de VS Code (barra de estado), está correcto.

🧩 Paso 2. Instala la extensión oficial de Python

Si aún no lo hiciste:

Abre la pestaña de extensiones (Ctrl+Shift+X).

Busca Python (de Microsoft).

Instálala.

Esta extensión es la que activa IntelliSense, depuración, linting y más.

🔍 Paso 3. Verifica el servidor de lenguaje

VS Code usa Pylance (otro complemento) para la inteligencia de código.
Debería instalarse automáticamente con la extensión de Python, pero si no:

Busca e instala Pylance en las extensiones.

En tu configuración (settings.json), asegúrate de tener:

{
    "python.languageServer": "Pylance"
}

🧪 Paso 4. Prueba IntelliSense en tu código

Abre tu main.py (por ejemplo):

from colorama import Fore, Style

print(Fore.GREEN + "Hola" + Style.RESET_ALL)


Ahora prueba escribir:

Fore.


👉 VS Code debería mostrar una lista desplegable con todas las opciones (GREEN, RED, BLUE, etc.).
Si aparece, IntelliSense está funcionando correctamente ✅

🧰 Paso 5. Configuración automática (opcional)

Si no quieres elegir el intérprete cada vez que abras el proyecto, crea el archivo:

.vscode/settings.json


y pon dentro:

{
    "python.defaultInterpreterPath": ".venv/bin/python",        // macOS / Linux
    // "python.defaultInterpreterPath": ".venv\\Scripts\\python.exe",  // Windows
    "python.languageServer": "Pylance",
    "python.analysis.autoImportCompletions": true
}


Así VS Code sabrá automáticamente qué entorno usar y cargará los módulos del .venv.

🧹 Si aún no funciona

Si después de todo no aparece el autocompletado, haz esto:

Guarda todos los archivos.

Reinicia VS Code.

Abre una terminal integrada y verifica:

which python


o en Windows:

where python


→ debe apuntar a tu .venv.

Espera unos segundos: el servidor de análisis de Python tarda un poco en indexar los paquetes.
"""