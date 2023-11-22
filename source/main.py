from flask import Flask, jsonify, make_response, request, session
import dbconfig as dbase
from flask_cors import CORS
import functions as f

app = Flask(__name__)

# Configuración para permitir peticiones desde cualquier origen
CORS(app)

# Ruta base de la API
@app.route("/api", methods=["GET"])
def api():
    return jsonify({'msg': 'Hello World'})

# Ruta para eliminar un usuario
@app.route("/api/delete" ,  methods=["DELETE"])
def eliminar_usuario():
    try:
        client = dbase.establecer_conexion()

        # Verificar si la conexión se estableció correctamente
        if not client:
            raise Exception("No se pudo establecer la conexión con MongoDB")



        # Iniciar la transacción
        with client.start_session() as session:
            # Iniciar la sesión de transacción
            with session.start_transaction():
                # Seleccionar la base de datos y la colección
                db, collection_person = dbase.seleccionar_bd_y_coleccion(client, "crud", "crudmicroservices")

                # Seleccionar la base de datos y la colección
                db, collection_log = dbase.seleccionar_bd_y_coleccion(client, "crud", "microserviceslogs")

                # Obtener el número de documento del usuario a eliminar
                dato = request.args.get('numero_documento')

                # Verificar si se proporcionaron datos
                if not dato:
                    raise Exception("Número de documento no proporcionado en la solicitud")

                # Eliminar el usuario
                if (check_user(dato) is None):
                    raise Exception("El usuario no existe")
                else:
                    collection_person.delete_one({'numero_documento': dato})

                    collection_log.insert_one(f.info_log(check_user(dato).get('tipo_documento'), dato))

        # Respondemos al cliente con un mensaje de éxito
        return jsonify({'mensaje': 'Usuario eliminado correctamente'})
    except Exception as e:
        # Retornar un error
        return make_response(jsonify({'error': str(e)}), 500)
    finally:
        dbase.cerrar_conexion(client)



# Función para verificar si un usuario existe
def check_user(datos):
    try:
        client = dbase.establecer_conexion()

        # Verificar si la conexión se estableció correctamente
        if not client:
            raise Exception("No se pudo establecer la conexión con MongoDB")

        # Seleccionar la base de datos y la colección
        db, collection = dbase.seleccionar_bd_y_coleccion(client, "crud", "crudmicroservices")

        # Verificar si la base de datos y la colección se seleccionaron correctamente
        if db is None or collection is None:
            raise Exception("No se pudo establecer la conexión con MongoDB")

        # Verificar si se proporcionaron datos
        if not datos:
            raise Exception("Número de documento no proporcionado en la solicitud")

        # Buscar el usuario
        user = collection.find_one({'numero_documento': datos})

        # Retornar el usuario encontrado
        return user
    except Exception as e:
        # Retornar un error
        return make_response(jsonify({'error': str(e)}), 500)
    finally:
        if client:
            client.close()

# Iniciamos la aplicación
if __name__ == "__main__":
    app.run(debug=True, port=5002)