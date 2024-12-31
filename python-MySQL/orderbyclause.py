import mysql.connector

connect = mysql.connector.connect(host='localhost',password='jxgxn_10_@123',user='root',database='jagan')

cursor=connect.cursor()

where = ("SELECT * FROM salary WHERE age>=21 and name like '%a%' ORDER BY name DESC ")

cursor.execute(where)

fetcall=cursor.fetchall()

for i in fetcall:
    print(i)