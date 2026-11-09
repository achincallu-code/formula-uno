# Aula 306

Aplicación Flask para crear cuentas, iniciar sesión y dar la bienvenida a los alumnos del grupo 306.

## Ejecutar en Windows

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe run.py
```

Abre http://127.0.0.1:5001. En tu computadora, las cuentas se guardan en `instance/grupo306.sqlite`.

## Desplegar en Render y Neon

Render gratuito no conserva los archivos de SQLite después de un despliegue. La aplicación usa PostgreSQL cuando se configura `DATABASE_URL`; si no, usa SQLite local.

1. Crea un proyecto y una base de datos PostgreSQL en [Neon](https://neon.com/).
2. En **Connect**, copia la cadena de conexión de la aplicación. La cadena pooled (`-pooler`) es adecuada para el servicio web; conserva `sslmode=require` si Neon lo incluye.
3. En Render, crea un **Blueprint** desde este repositorio y acepta `render.yaml`. El servicio usa Gunicorn y enlaza el puerto que Render proporciona.
4. Cuando Render lo solicite, configura `DATABASE_URL` con la cadena de Neon. `SECRET_KEY` se genera de forma privada por Render.
5. Espera el despliegue y abre la URL pública que Render asigna. La aplicación crea las tablas que necesita al iniciar.

La cadena de conexión contiene credenciales: configúrala solo como variable privada en Render; no la escribas en el repositorio ni la compartas públicamente. Render define `RENDER_EXTERNAL_URL` automáticamente, que se usa como URL base para los enlaces de recuperación. Si usas un dominio propio, puedes definir `PUBLIC_BASE_URL` en Render. El plan gratuito de Neon puede suspender bases inactivas y tiene límites de uso; consulta sus [planes actuales](https://neon.com/docs/introduction/plans).

El archivo `render.yaml` deja la recuperación por correo como opcional. Para activarla, agrega en **Environment** las variables SMTP descritas abajo. Después de agregar o cambiar variables, guarda y vuelve a desplegar el servicio.

## Recuperación de contraseña

La recuperación usa enlaces de un solo uso que vencen después de una hora. Configura estas variables de entorno para habilitar el envío:

- `SMTP_HOST`: servidor SMTP.
- `SMTP_PORT`: puerto SMTP; usa `465` para SSL o `587` para STARTTLS.
- `SMTP_USERNAME` y `SMTP_PASSWORD`: credenciales SMTP, si el servidor las requiere.
- `MAIL_FROM`: dirección remitente verificada.
- `PUBLIC_BASE_URL`: URL pública de la aplicación, por ejemplo `https://tu-dominio.com`.

Sin `SMTP_HOST`, `MAIL_FROM` y `PUBLIC_BASE_URL`, el formulario informa que la recuperación aún no está configurada. Mantén las credenciales SMTP como variables privadas del entorno.
