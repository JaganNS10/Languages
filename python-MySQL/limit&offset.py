import mysql.connector

connect = mysql.connector.connect(host='localhost',user='root',password='jxgxn_10_@123',database='jagan')

cursor=connect.cursor()

limit = "SELECT *FROM salary LIMIT 3 OFFSET 2"

cursor.execute(limit)

fetchall=cursor.fetchall()
for x in fetchall:
    print(x)