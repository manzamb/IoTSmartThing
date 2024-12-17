import paho.mqtt.client as mqtt
import time

# Configuración del servidor MQTT
BROKER = "192.168.68.104"  # Puedes usar otro servidor público o local
PORT = 1883
TOPIC = "medida"

# Crear cliente MQTT
client = mqtt.Client()

# Conexión al broker
print(f"Conectando al servidor MQTT en {BROKER}:{PORT}...")
client.connect(BROKER, PORT, 60)

# Publicar mensajes en el canal 'medida'
try:
    for i in range(5):
        message = f"Medida {i + 1}: {i * 10} unidades"
        print(f"Publicando: {message}")
        client.publish(TOPIC, message)
        time.sleep(1)  # Espera de 1 segundo entre mensajes
except KeyboardInterrupt:
    print("Publicador detenido manualmente.")
finally:
    client.disconnect()
    print("Conexión terminada.")
