import paho.mqtt.client as mqtt

# Configuración del servidor MQTT
BROKER = "192.168.68.104"  # Debe coincidir con el broker del publicador
PORT = 1883
TOPIC = "medida"

# Función de callback cuando se recibe un mensaje
def on_message(client, userdata, message):
    print(f"Mensaje recibido: {message.payload.decode()} en el canal {message.topic}")

# Crear cliente MQTT
client = mqtt.Client()

# Asignar callback
client.on_message = on_message

# Conexión al broker y suscripción al canal
print(f"Conectando al servidor MQTT en {BROKER}:{PORT}...\")")
client.connect(BROKER, PORT, 60)

client.subscribe(TOPIC)
print(f"Suscrito al canal '{TOPIC}'. Esperando mensajes...")

# Mantener el cliente suscrito en funcionamiento
try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Suscriptor detenido manualmente.")
finally:
    client.disconnect()
    print("Conexión terminada.")
