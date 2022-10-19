import mysql.connector

cnx = mysql.connector.connect(user='root', password='sergioFI07',
                              host='127.0.0.1',
                              database='codigoIoT')
print ("conexión realizada")
print (cnx)
print ("cerrar conexión")
cnx.close()
print ("conexión cerrada")