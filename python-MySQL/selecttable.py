import mysql.connector

connect = mysql.connector.connect(host='localhost',password='jxgxn_10_@123',user='root',database='jagan')

cursor=connect.cursor()

drop = ("SELECT * FROM Orders")

cursor.execute(drop)

fetchall = cursor.fetchall()
fetchone=cursor.fetchone()

for i in fetchall:
    print(i)


