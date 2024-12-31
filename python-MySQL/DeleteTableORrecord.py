import mysql.connector

connect = mysql.connector.connect(host='localhost',user='root',password='jxgxn_10_@123',database='jagan')

cursor = connect.cursor()

delete = ("DELETE FROM salary WHERE id = %s")
val=2
adr=(val,)

cursor.execute(delete,adr)

print(cursor.rowcount,"records was deleted")

connect.commit()