# Instrucciones para ejecutar el proyecto

## Clonar el repositorio

```bash
git clone https://github.com/usuario/nombre-del-repo.git
```

## Instalar Python 3

Para descargar Python 3, por favor visite el sitio oficial de Python.
Ir a la carpeta del repositorio e instalar un entorno virtual

```python
cd nombre-del-repo
python -m venv venv
```
Esto creará un entorno virtual en el directorio venv en la carpeta del proyecto.

## Activar el entorno virtual

En Windows:

    venv\Scripts\activate

En macOS/Linux:


    source venv/bin/activate

## Instalar las dependencias del archivo requirements.txt

    pip install -r requirements.txt

Ejecutar el archivo main.py

    python main.py

El servidor se estara ejecutando y te aparecera en consola lo siguiente:
```
    INFO:     Started server process [15284]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:5049 (Press CTRL+C to quit)
```