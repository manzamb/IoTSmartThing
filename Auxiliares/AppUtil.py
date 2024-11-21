#!/usr/local/bin/python
# -*- coding: utf-8 -*-
##Para obtener la IP
import os
import socket
import fcntl
import struct

########## Conexión Broker e Indice Semántico ##########################
#broker = "iot.eclipse.org"

pathRaiz = "."
broker = "192.168.68.116"##"iot.eclipse.org"##"test.mosquitto.org"
brokerPort = 1883 ##mosquito
indiceSemantico = 'http://facfiet.unicauca.edu.co/SemanticSearchIoT/WSSemanticSearch/WSSemanticSearch.asmx?WSDL'
nameSpaceIndice = 'http://www.unicacuca.edu.co/'

####################################pathontologiaInstanciada = pathRaiz + "/Escenario/ArchivosObjeto/OWL/"
pathOWL = pathRaiz + "/Escenario/ArchivosObjeto/OWL/"
pathOntologiaOriginal = pathRaiz + "/Escenario/OntologiaPck/OntologiaOWL/"
ontologiaInstanciada = pathRaiz + "/Escenario/ArchivosObjeto/OWL/ontologiaInstanciada.owl"


ontologia = pathRaiz + "/Escenario/OntologiaPck/OntologiaOWL/ontologiav18.owl"#ontologia = "./Escenario/OntologiaOWL/ontologiav17.owl"

ontologiaResta = pathRaiz + '/Escenario/OntologiaOWL/resta.owl'
ontologiaPUResta  = pathRaiz + "/Escenario/OntologiaPck/OntologiaOWL/ontologiaPerfilUsuarioresta.owl"#/home/pi/Desktop/escenario/Escenario/OntologiaPck/OntologiaOWL

pathEca=pathRaiz + "/Escenario/ArchivosObjeto/ECA/"
pathState=pathRaiz + "/Escenario/ArchivosObjeto/State/"
pathComandos=pathRaiz + "/Escenario/ArchivosObjeto/Comandos/"
pathMetaData=pathRaiz + "/Escenario/ArchivosObjeto/MetaData/"
pathPeticionesWeb=pathRaiz + "/Escenario/ArchivosObjeto/PeticionesWeb/"
pathSimpleValue=pathRaiz + "/Escenario/ArchivosObjeto/SimpleValue/"
pathEjecutables = pathRaiz + "/Escenario/ArchivosObjeto/Ejecutables/"
# pathAplicacion = "/home/pi/Desktop/ontologia/Tesis/src/"
pathIndependientePck = pathRaiz + "/Escenario/IndependientePck/"

pathArchivosObjeto = pathRaiz + "/Escenario/ArchivosObjeto/"






# broker = "test.mosquitto.org"
# indiceSemantico = 'http://facfiet.unicauca.edu.co/SemanticSearchIoT/WSSemanticSearch/WSSemanticSearch.asmx?WSDL'
# nameSpaceIndice = 'http://www.unicacuca.edu.co/'
#
# pathontologiaInstanciada = "./Escenario/ArchivosObjeto/OWL/"
# ontologiaInstanciada = "./Escenario/ArchivosObjeto/OWL/ontologiaInstanciada.owl"
# ontologia = "./Escenario//OntologiaPck/OntologiaOWL/ontologiav18.owl"#ontologia = "./Escenario/OntologiaOWL/ontologiav17.owl"
# ontologiaResta = './Escenario/OntologiaOWL/resta.owl'
# ontologiaPUResta  = "./Escenario/OntologiaPck/OntologiaOWL/ontologiaPerfilUsuarioresta.owl"#/home/pi/Desktop/escenario/Escenario/OntologiaPck/OntologiaOWL
#
# pathEca="./Escenario/ArchivosObjeto/ECA/"
# pathState="./Escenario/ArchivosObjeto/State/"
# pathComandos="./Escenario/ArchivosObjeto/Comandos/"
# pathMetaData="./Escenario/ArchivosObjeto/MetaData/"
# pathPeticionesWeb="./Escenario/ArchivosObjeto/PeticionesWeb/"
# pathSimpleValue="./Escenario/ArchivosObjeto/SimpleValue/"
# pathEjecutables = "./Escenario/ArchivosObjeto/Ejecutables/"
# pathAplicacion = "/home/pi/Desktop/ontologia/Tesis/src/"
# pathOWL = "./Escenario/ArchivosObjeto/OWL/"
# pathIndependientePck = "./Escenario/IndependientePck/"
# pathArchivosObjeto = "./Escenario/ArchivosObjeto/"

##TODO agregar claves de eca
MetaDatos_Objeto = [("id", str),("title", str), ("description", str),  ("lon", float), ("lat", float),("ele",float),('name',str),('domain',str), ("created",str),("creator",str), ("feed",str),("private",str), ("status",str), ("title",str), ("updated",str),("version",str), ("website",str), ("tags", list)]
MetaDatos_Recurso = [("datastream_id", str), ("label", str), ("symbol", str), ("datastream_type", str),("min_value",str),("max_value",str), ("datastream_format", str), ("featureofinterest", str), ("entityofinterest",str), ("tags", list)]
formatos_soportados = ["int","float","string","char","bool","boolean"]
tipos_recursos_soportados = ["sensor", "actuador"]
#service_state_soportado = ["on", "off"]
Metadatos_Eca =['name_eca','eca_state','osid_object_event','ip_event_object','name_event_object','id_event_resource','name_event_resource','comparator_condition','variable_condition','type_variable_condition','unit_condition','meaning_condition','osid_object_action','ip_action_object','name_action_object','id_action_resource','name_action_resource','comparator_action','variable_action','type_variable_action','unit_action','meaning_action' ]



def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s',ifname[:15]))[20:24])

def getIpObjeto():
    try:
        return get_ip_address('wlan0')
    except:
        try:
            return get_ip_address('eth0')
        except:
            return ""

def killProcess (nombreProceso):
    os.system("sudo kill -s 9 $(ps ax | grep " + nombreProceso + " | grep -v grep | awk '{print$1}')")
