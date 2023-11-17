from flask import Flask, jsonify, make_response, request
from bson import json_util
import json
import dbconfig as dbase
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api", methods=["GET"])
def api():
    return jsonify({'msg': 'Hello World'})

@app.route("/api/delete", methods=["POST"])
def eliminar_usuario():
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

        # Obtener datos del formulario enviado mediante POST
        datos = request.form.get('numero_documento')

        # Verificar si se proporcionaron datos
        if not datos:
            raise Exception("Número de documento no proporcionado en la solicitud")

        # Eliminar el usuario
        if (check_user() is None):
            raise Exception("El usuario no existe")
        else:
            collection.delete_one({'numero_documento': datos})


        return jsonify({'mensaje': 'Usuario eliminado correctamente'})
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)
    finally:
        if client:
            client.close()

def check_user():
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

        # Obtener datos del formulario enviado mediante POST
        datos = request.form.get('numero_documento')

        # Verificar si se proporcionaron datos
        if not datos:
            raise Exception("Número de documento no proporcionado en la solicitud")

        # Buscar el usuario
        user = collection.find_one({'numero_documento': datos})

        return user
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)
    finally:
        if client:
            client.close()

    
if __name__ == "__main__":
    app.run(debug=True)