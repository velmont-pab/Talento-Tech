""" 
Perfecto 😎 Vamos a configurar VS Code para que use tu entorno virtual .venv automáticamente cuando ejecutes o depures tus scripts.

🧩 Paso 1. Abre tu proyecto en VS Code

Abre VS Code.

En el menú:
👉 Archivo → Abrir carpeta...
Selecciona la carpeta de tu proyecto (la que contiene .venv y tus archivos .py).

    Tu estructura debería verse así:
                mi_proyecto/
                ├── .venv/
                └── main.py

⚙️ Paso 2. Selecciona el intérprete de Python correcto
?       Presiona Ctrl + Shift + P 
    Escribe:
todo        Python: Select Interpreter

Te aparecerá una lista de intérpretes.
Busca el que diga algo como:

todo        .venv\\Scripts\\python.exe  
Haz clic en ese. ✅ 

?VS Code recordará esta elección para esa carpeta.

🧰 Paso 3. Verifica que está activo

Abre una nueva terminal dentro de VS Code (desde el menú Terminal → Nueva terminal).
Si todo está bien, deberías ver algo así:

todo        (.venv) PS C:\\Users\\TuUsuario\\mi_proyecto>

Si ves el prefijo (.venv) al inicio, significa que VS Code ya está usando tu entorno virtual.

🧪 Paso 4. Ejecuta tu script

Con main.py abierto, simplemente haz clic en el botón ▶️ (Ejecutar arriba a la derecha)
o ejecuta desde la terminal integrada:

todo        python main.py

Deberías ver el texto de Colorama en colores 🎨.

⚡ Extra: configurar para que VS Code lo detecte automáticamente

Si quieres que VS Code detecte siempre tu .venv sin tener que seleccionarlo cada vez,
puedes crear una carpeta .vscode en tu proyecto con un archivo settings.json dentro:

mi_proyecto/
├── .venv/
├── main.py
└── .vscode/
    └── settings.json


Y dentro del archivo settings.json, escribe:

{    
"python.defaultInterpreterPath": ".venv/bin/python",        // macOS / Linux
"python.defaultInterpreterPath": ".venv\\Scripts\\python.exe"  // Windows
}


VS Code usará siempre ese entorno virtual automáticamente.

"""