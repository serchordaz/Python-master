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
        cursor=connection.cursor()
        cursor.execute("SELECT id,nombre,temperatura,fecha,humedad FROM clima WHERE id=1")
        print(cursor.fetchall())

except Exception as ex:
    print(ex)
