import mysql.connector

cnx = mysql.connector.connect(user='serchordaz', password='1234',
                              host='localhost',
                              database='codigoIoT')
print ("conexión realizada")
print (cnx)
print ("cerrar conexión")
cnx.close()
print ("conexión cerrada")