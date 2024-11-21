import time
import os
import sys
from os import system

sys.path.append('Escenario')

sys.path.append("/usr/local/lib/python3.7/dist-packages")
from Starter import Starter

if __name__ == "__main__":
    print("---------- Main ------------------------")
    try:
        os.system("sudo fuser -k 80/tcp")
        os.system("sudo kill -s 9 $(ps ax | grep ./Escenario" + " | grep -v grep | awk '{print$1}')")
        system("clear")

        print("********************** Main:21 inicia Carga de Objeto: " + time.ctime() + "********************** ")
        S = Starter()
        S.iniciarObjeto()
        print("********************** Main:21 Inicia Hilos " + time.ctime())
        S.iniciarHilosObjeto()
        print("********************** Main:21 Fin " + time.ctime())

    except (KeyboardInterrupt, SystemExit):
        print("INTERRUPCIÓN POR TECLADO")
        os.system("sudo fuser -k 80/tcp")
        os.system("sudo ps ax | grep Main.py | grep -v grep | awk '{print$1}' |xargs  kill -s 9")
        os.system(
            "sudo ps ax | grep ServicioInteligenteIndependiente.py | grep -v grep | awk '{print$1}' |xargs  kill -s 9")
        os.system("sudo ps ax | grep ServidorWebIndependiente | grep -v grep | awk '{print$1}' |xargs  kill -s 9")
        os.system("sudo kill -s 9 $(ps ax | grep ./Escenario" + " | grep -v grep | awk '{print$1}')")

