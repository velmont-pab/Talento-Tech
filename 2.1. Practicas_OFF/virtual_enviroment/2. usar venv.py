"""  
✅ Paso 1. Asegúrate de activar tu entorno virtual
    Antes de ejecutar cualquier script, activa el entorno:

?        En Windows (PowerShell o CMD):
!            .venv\\Scripts\\activate

        En Linux/macOS:
!            source .venv/bin/activate


?       Verás algo así en tu terminal:
!            (.venv) C:\\Users\\TuUsuario\\mi_proyecto>

todo     Ese ( .venv ) al inicio indica que estás dentro del entorno correcto.


✅ Paso 2. Crea un archivo Python de prueba

    Dentro de la carpeta mi_proyecto (fuera de .venv), crea un archivo llamado main.py con este contenido:
        from colorama import Fore, Style, init

        # Inicializa colorama
        init()

        print(Fore.GREEN + "¡Hola desde colorama!" + Style.RESET_ALL)
        print(Fore.RED + "Esto es texto rojo." + Style.RESET_ALL)

        
✅ Paso 3. Ejecuta el script

?    Con el entorno virtual activado:
!        python main.py

todo     Deberías ver el texto en colores en tu terminal 💚❤️


💡 Consejos opcionales

?    Si quieres guardar tus dependencias (para otro equipo o futuro):
!        pip freeze > requirements.txt

?    Para instalar las dependencias después:
!        pip install -r requirements.txt

?    Cuando termines de trabajar:
!        deactivate
"""