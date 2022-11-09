# Bibliotecas
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
from multiprocessing import connection
import mysql.connector
import argparse

# Parser
parser = argparse.ArgumentParser()
parser.add_argument("status")
args = parser.parse_args()

# Inicar el sensor
reader = SimpleMFRC522()

# Conexión
connection=mysql.connector.connect(host='192.168.1.70',port=3306,user='sergiolan',password='1234',db='codigoiot')
if connection.is_connected():
        print("Conexión Exitosa")
# Cursor
cursor=connection.cursor()

# Cuerpo del programa
try:
    # Lectura unica
    id, text = reader.read()
    # print("ID: %s\nText: %s" % (id,text))
    strrr = text.split(",")
    # print (strrr)
    # print (strrr[0])
    sleep(1)
    query_insert = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('" + strrr[0] + "','" + args.status + "'," + str (id) + ");"
    print (query_insert)
    
    # Ejecutar cursor
    cursor.execute (query_insert)
    print(cursor.fetchall())
    # Asegurarse de realizar la operacion en BD
    connection.commit()
    print ("Query Ok")
    sleep (1)

    # Cerrar
    cursor.close()
    connection.close()
    GPIO.cleanup()
    
except KeyboardInterrupt:
    # Cerrar
    cursor.close()
    connection.close()
    GPIO.cleanup()
    raise