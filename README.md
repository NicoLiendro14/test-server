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

# Endpoints:
La lista de endpoints para este código son los siguientes:

    POST /whatsapp/login
    POST /message/add
    PUT /message/edit/{job_id}
    DELETE /message/delete/{job_id}
    GET /messages/{group_name}
    GET /message/group

En detalle, cada endpoint tiene las siguientes funciones:

    POST /whatsapp/login: Retorna un archivo imagen en forma de respuesta.
    POST /message/add: Agrega un mensaje programado y retorna información acerca del mensaje.
    PUT /message/edit/{job_id}: Edita un mensaje programado existente y retorna información acerca del mensaje editado.
    DELETE /message/delete/{job_id}: Elimina un mensaje programado existente y retorna información acerca del mensaje eliminado.
    GET /messages/{group_name}: Retorna todos los mensajes programados para el grupo dado.
    GET /message/group: Retorna si el grupo existe o no.

URLs completas:

    POST /whatsapp/login
        http://127.0.0.1:5049/whatsapp/login

    POST /message/add
        http://127.0.0.1:5049/message/add

    PUT /message/edit/{job_id}
        http://127.0.0.1:5049/message/edit/{job_id}

    DELETE /message/delete/{job_id}
        http://127.0.0.1:5049/message/delete/{job_id}

    GET /messages/{group_name}
        http://127.0.0.1:5049/messages/{group_name}

    GET /message/group
        http://127.0.0.1:5049/message/group