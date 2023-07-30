import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    port = '4400',
    user = 'root',
    passwd = '123456'
)

#prepare a cursor object 
cursorObject = dataBase.cursor()

#Create the database
cursorObject.execute("CREATE DATABASE mthsssdb")

print("All done!")