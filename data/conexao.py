import mysql.connector
# Existe a opção de usar o próprio ip do pc
mydb = mysql.connector.connect( host = "localhost",
                                user = "root",
                                password = "root")

print(mydb)