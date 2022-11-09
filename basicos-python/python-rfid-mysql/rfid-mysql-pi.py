from multiprocessing import connection
import mysql.connector

import RPi.GPIO as GPIO
from time import sleep
import sys
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

GPIO.setwarnings(False)

cnx = connection=mysql.connector.connect(
        host='192.168.1.70',
        port=3306,
        user='sergiolan',
        password='1234',
        db='codigoiot'
    )

if connection.is_connected():
        print("Conexión Exitosa")
        #cursor
        cursor=connection.cursor()
        
try:
    while True:
        print("Acerca el Tag al lector")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        
        query_insert = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('Serch Ordaz','" + text + "',"+ str (id) + ");"
        cursor.execute(query_insert)
        cnx.commit()
        print("Query OK")
        sleep(5)
        
except Exception as ex:
    print(ex)
    
except KeyboardInterrupt:
    GPIO.cleanup()
    raise


