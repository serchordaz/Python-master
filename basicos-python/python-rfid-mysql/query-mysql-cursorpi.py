import mysql.connector

cnx = mysql.connector.connect(host='192.168.1.70',
                              port=3306,
                                user='serchlan',
                                password='1234',
                                db='codigoiot'
                            )
cursor = cnx.cursor()

query = {"SELECT id,nombre,temperatura,fecha,humedad FROM clima WHERE id=1"}

cursor.execute(query)

res = cursor.fetchall ()

for x in res:
    print(x)

cursor.close()
cnx.close()