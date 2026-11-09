# Aula 306

Aplicación Flask para crear cuentas, iniciar sesión y dar la bienvenida a los alumnos del grupo 306.

## Ejecutar en Windows

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe run.py
```

Abre http://127.0.0.1:5000. En tu computadora, las cuentas se guardan en `instance/grupo306.sqlite`.

## Guardar las cuentas en Render gratis

Render gratuito no conserva los archivos de SQLite después de un despliegue. La aplicación usa PostgreSQL cuando se configura `DATABASE_URL`; si no, usa SQLite local.

1. Crea un proyecto PostgreSQL en [Neon](https://neon.com/) y copia la cadena de conexión desde **Connect**.
2. En Render, abre el servicio web y ve a **Environment**.
3. Agrega `DATABASE_URL` y pega ahí la cadena de conexión de Neon. Si creas el servicio con este `render.yaml`, Render puede pedirte este valor durante la configuración.
4. Guarda los cambios y espera a que Render despliegue la aplicación.

La cadena de conexión es una contraseña: guárdala solo en las variables privadas de Render y no la publiques en GitHub. El plan gratuito de Neon tiene límites de uso y puede poner la base en reposo cuando está inactiva; consulta sus [planes y límites actuales](https://neon.com/docs/introduction/plans).
