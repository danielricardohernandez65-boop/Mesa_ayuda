# Mesa_ayuda


Una aplicación para una empresa de telecomunicaciones que les permite hacer una mesa de ayuda en donde clientes puedan crear `tickets` y que eston sean asignados a técnicos para resolver dicho problema.

También hay un usuario administrador que puede crear o eliminar técnicos y tiene relevancia en la asignación de los tickets.


## Instalación y ejecución

El proyecto fue realizado usando `Flask` como framework web, para ello es necesario la versión de `Python 3.12` que puedes descargar [aqui](https://www.python.org/downloads/)

Para usar el proyecto clona el repositorio y accede:

```bash
git clone https://github.com/MontoyaN1/Mesa_ayuda.git

cd Mesa_ayuda

```

Para el tema de las dependencias se recomienda crear un entorno virtual de Python:

```bash
python -m venv .venv

```

O usando:

```bash
python3 -m venv .venv

```

Y ahora accede al entorno:


```bash
source .venv/bin/activate
```

Instala las dependencias en el archivo requeriments.txt usando `pip` :

```bash
pip install -r requeriments.txt
```

Cuando veas que haya terminado la instalación correctamente, ejecuta el proyecto:

```bash
python main.py

```

O usa:
```bash
python3 main.py

```

Y ahora si vaz a `localhost:5000` ya puedes usar el programa


## Servicio de despliegue elegido
Usamos **Render (Web Service)** con el repositorio de GitHub conectado a la rama `main`.  
Render compila el proyecto y lo publica automáticamente cada vez que hay un push.  
URL pública: https://mesa-ayuda-m8nz.onrender.com

- Build Command: `pip install -r requirements.txt`
- Start Command (Flask en producción): `gunicorn -w 2 -k gthread -b 0.0.0.0:$PORT main:app`

> Nota: `$PORT` lo provee Render.

---

## Variables de entorno (cómo las configuramos)
**Local (opcional):**
- Archivo `.env` o variables exportadas, por ejemplo:
  - `FLASK_ENV=development`
  - `SECRET_KEY=<una_clave_segura>`
  - `DATABASE_URL=<si usamos Postgres>`

**En Render (Producción):**  
En *Service → Settings → Environment* agregamos:
- `FLASK_ENV=production`
- `SECRET_KEY=<valor-seguro>`
- `DATABASE_URL=<si aplica>`

> No subimos secretos al repo; solo se configuran como **Environment Variables** en Render.

---

## Dificultades y cómo las resolvimos
1. **No se actualizaba el sitio al editar localmente.**  
   - Causa: Render despliega desde GitHub; los cambios locales no cuentan hasta hacer push.  
   - Solución: activamos **Auto-Deploy** y configuramos **GitHub Actions** con un **Deploy Hook** de Render (guardado como secret en GitHub) para que el deploy sea automático al hacer push.

2. **Error en GitHub Actions: `exit code 127` (“curl: not found”).**  
   - Causa: el runner no tenía `curl` instalado.  
   - Solución: añadimos `sudo apt-get update && sudo apt-get install -y curl` antes de llamar al Deploy Hook.

3. **`flake8: command not found`.**  
   - Causa: `flake8` no estaba instalado en el runner.  
   - Solución: agregamos `pip install flake8 pytest` en el paso de instalación del workflow.

4. **Cambios visuales que no aparecían inmediatamente.**  
   - Causa: caché del navegador/CDN.  
   - Solución: recarga forzada (Ctrl+F5) / modo incógnito; si era necesario, **Clear build cache & deploy** en Render.














