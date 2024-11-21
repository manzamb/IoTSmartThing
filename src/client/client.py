import requests

def fetch_json(server_url, file_name):
    """
    Hace un llamado al servidor y obtiene el contenido de un archivo JSON.
    
    :param server_url: URL base del servidor (por ejemplo, 'http://<ip>:5000')
    :param file_name: Nombre del archivo JSON a solicitar (por ejemplo, 'id.json')
    :return: Contenido del JSON como un diccionario, o None si ocurre un error.
    """
    try:
        # Construir la URL completa
        url = f"{server_url}/{file_name}"
        
        # Hacer la solicitud GET
        response = requests.get(url)
        
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Parsear el contenido JSON recibido
            json_data = response.json()
            print(f"Contenido de {file_name}:")
            print(json_data)
            return json_data
        else:
            print(f"Error al obtener {file_name}: {response.status_code}")
            print(response.text)
            return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None

if __name__ == "__main__":
    # Dirección del servidor (cambia <ip> por la dirección IP del servidor)
    # server_url = "http://192.168.20.33:5000"
    server_url = "http://localhost:5000"

    # Archivos a consultar
    files = ["id.json", "medida.json"]
    
    # Iterar sobre los archivos y obtener su contenido
    for file_name in files:
        fetch_json(server_url, file_name)