import mysql.connector

cnx = mysql.connector.connect(user='sergiolan', password='1234',
                              host='192.168.1.70',
                              database='codigoIoT')
print ("conexión realizada")
print (cnx)
print ("cerrar conexión")
cnx.close()
print ("conexión cerrada")