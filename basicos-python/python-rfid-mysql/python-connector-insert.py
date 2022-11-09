from multiprocessing import connection
import mysql.connector

try: 
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
        query_insert = "INSERT INTO rfid (nombre,texto,rfid) VALUES ('Sergio Ordaz','Test Python 3',849155697731)"
        cursor.execute(query_insert)
        cnx.commit()
        print("Query OK")


except Exception as ex:
    print(ex)
