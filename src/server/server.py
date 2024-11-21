from flask import Flask, request, jsonify, send_file
import json
import os

app = Flask(__name__)

#@app.route('/get_json', methods=['GET'])
@app.route('/<filename>', methods=['GET'])
def serve_file(filename):
    # Validar que el archivo solicitado sea uno de los permitidos
    allowed_files = ["id.json", "medida.json"]
    if filename not in allowed_files:
        return jsonify({"error": "Invalid file requested. Only id.json or medida.json are allowed"}), 400

    # Ruta en la que se almacena el json
    base_path = os.path.join(os.getcwd(), "src/server/json")
    file_name = os.path.join(base_path, filename)
    
    # Verificar si el archivo existe
    if os.path.exists(file_name):
        return send_file(file_name, as_attachment=True, mimetype='application/json')
    else:
        return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)