import mysql.connector
connection = mysql.connector.connect(host='localhost',password='jxgxn_10_@123',user='root')

if connection.is_connected():
    print("connection established...")