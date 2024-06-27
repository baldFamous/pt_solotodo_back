# Blog API

Este es el backend de la aplicación Blog, construido con Django y Django REST Framework. 
Proporciona una API para gestionar publicaciones de blog.

## Requisitos

- Python 3.10 o superior
- pip (Python package installer)
- virtualenv

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/baldFamous/pt_solotodo_back.git
    cd blog_backend
    ```

2. Crea y activa un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: .\venv\Scripts\activate
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Realiza las migraciones:
    ```bash
    python manage.py migrate
    ```

5. Crea un superusuario:
    ```bash
    python manage.py createsuperuser
    ```

## Uso

Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```

La API cuenta con los siguientes endpoints:
- `http://localhost:8000/api/posts/` (GET, POST)
- `http://localhost:8000/api/posts/<id>/` (GET)

Accede al panel de administración en `http://localhost:8000/admin/`.
