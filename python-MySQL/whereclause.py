import mysql.connector

connect = mysql.connector.connect(host='localhost',password='jxgxn_10_@123',user='root',database='jagan')

cursor = connect.cursor()

where = ("SELECT *FROM Customer WHERE cname like 'j%' and cname like '%n'")
where1 =("SELECT DISTINCT(age) FROM Customer")
cursor.execute(where1)

fetchall = cursor.fetchall()

for i in fetchall:
    print(i)