
""" 
🐍 1. .venv → Entorno virtual de Python

Un entorno virtual es una carpeta que contiene su propia instalación de Python y sus módulos.
Sirve para aislar dependencias de un proyecto y evitar que se instalen globalmente (como querías).

🔧 Cómo crear y usar uno:
#todo    python -m venv .venv

Esto crea una carpeta llamada .venv dentro del proyecto.
Luego activas el entorno:
?Windows:
#todo    .venv\\Scripts\\activate 
Linux/macOS:
         source .venv/bin/activate

Tu prompt cambiará, indicando que estás “dentro” del entorno virtual.


Ahora puedes instalar módulos sin afectar al sistema:
#todo    pip install requests

Cuando terminas:
#todo    deactivate


!Si borras la carpeta .venv, desaparecen todas las instalaciones.
👉 Nada se guarda permanentemente.
"""