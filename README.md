# CRUD Microservices API

Esta aplicación es una API simple construida con Flask que proporciona operaciones la opción de eliminar de un CRUD (Crear, Leer, Actualizar, Eliminar) para usuarios almacenados en una base de datos MongoDB. Está API es creada bajo la arquitectura de microservicios. La API permite a los usuarios realizar las siguientes acciones:

Obtener Saludo: Acceder a un mensaje de saludo básico desde la ruta /api.

Eliminar Usuario: Eliminar un usuario específico mediante una solicitud DELETE a la ruta /api/delete/{numero_documento}.

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://tu-repositorio.git
    cd nombre-de-la-aplicacion
    ```

2. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Configuración

1. Asegúrate de tener Python y pip instalados.

## Uso

1. Inicia la aplicación:

    ```bash
    python main.py
    ```

2. Abre tu navegador y visita [http://localhost:5000/api](http://localhost:5000/api).

3. Puedes eliminar un usuario usando la siguiente URL:

    ```http
    DELETE http://localhost:5000/api/delete/numero-de-documento
    ```

    Reemplaza `numero-de-documento` con el número del documento del usuario que deseas eliminar.

## Endpoints

- **GET /api**: Devuelve un mensaje simple de "Hello World".

- **DELETE /api/delete/{numero_documento}**: Elimina un usuario por su número de documento.

## Contribuciones

Si encuentras algún problema o tienes alguna mejora, siéntete libre de abrir un problema o enviar una solicitud de extracción.

## Licencia

[MIT License]
