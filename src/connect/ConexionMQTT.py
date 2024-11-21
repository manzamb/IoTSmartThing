
import paho.mqtt.client as mqtt
import threading
import sys

sys.path.append('./Auxiliares')

import AppUtil


class ConexionMQTT:
    broker = AppUtil.broker
    brokerPort = AppUtil.brokerPort
    MqttClient = mqtt.Client()

    def __init__(self):
        self.mensaje = ""
        print("Constructor MQTT")

    def iniciarConexionMQTT(self):

        try:
            # self.MqttClient.connect(self.broker, 1883, 60)
            print("----------------------")
            print(self.broker)
            print("---------------------")
            self.MqttClient.connect(self.broker, self.brokerPort, 60) #puerto para mosquiito local 9001
            self.MqttClient.loop_start()
            print("Conexion MQTT exitosa")
            return True
        except Exception as e:
            print("Desde Conexion MQTT")
            print(e)
            return None

    def publicarMQTT(self, canal, valorPublicar):
        try:
            self.MqttClient.publish(canal, valorPublicar)
            publicaMqtt = threading.Thread(target=self.pub, name=canal, args=(canal, valorPublicar,))
            publicaMqtt.start()
            return True
        except Exception as e:
            print(e)
            return False


    def pub(self, canal,pay):
        # broker_address = "192.168.0.128"

        broker_address= self.broker
        client = mqtt.Client("P1")
        client.connect(broker_address)
        client.loop_start()
        client.publish(canal, pay)
        # time.sleep(2)  # wait
        client.loop_stop()  # stop the loop

    def suscribirMQTT(self, canal):
        try:
            self.MqttClient.subscribe(canal)
            self.MqttClient.on_message = self.__on_message
            print("Esperando Mensajes...")
            return True
        except Exception as e:
            print(e)
            return False

    def unsuscribeMQTT(self, canal):
        try:
            self.MqttClient.unsubscribe(canal)
            self.MqttClient.loop_stop()
            return True
        except:
            return False

    # Pendiente de la llegada de los mensajes
    def __on_message(self, client, userdata, msg):
        self.mensaje = msg.payload
