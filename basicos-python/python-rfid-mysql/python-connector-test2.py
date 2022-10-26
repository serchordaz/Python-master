from multiprocessing import connection
import mysql.connector

try: 
    cnx = connection=mysql.connector.connect(
        host='localhost',
        port=3306,
        user='serchordaz',
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
