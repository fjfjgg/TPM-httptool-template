#!/usr/bin/env python3
# Importamos las librerías necesarias
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import hashlib

# Creamos una instancia de la aplicación
app = Flask(__name__)

# Definimos una ruta para recibir peticiones POST
@app.route("/httptool", methods=["POST"])
def calcular_sha256():
    # Obtenemos el fichero y el nombre que nos envían en la petición multipart
    file = request.files["file"]
    userid = request.form["userid"]
    # Ejemplo de corrección, solo muestra datos recibidos y siempre pone como nota 100
    file_name = secure_filename(file.filename)
    file_content = file.read()
    file_size = len(file_content)
    # Calculamos el sha256sum del fichero usando la librería hashlib
    sha256sum = hashlib.sha256(file_content).hexdigest()
    # Devolvemos el resultado como JSON, incluyendo el nombre del fichero y el nombre del usuario
    return jsonify({"userid": userid, "file": file_name, "size": file_size, "sha256sum": sha256sum, "score": 100})

# Ejecutamos la aplicación
if __name__ == "__main__":
    app.run()


# Instalar dependencias: python3 -m pip install flask requests werkzeug
# Test: curl -F "file=@test.txt" -F "userid=user" http://localhost:5000/httptool
# Example of response:
# {"file":"test.txt","score":100,"sha256sum":"c3f68d96b1bfd8c29aa5b795b8ce292cd44e7883ed71373a9424fd92d1a1d9f9","size":14,"userid":"user"}