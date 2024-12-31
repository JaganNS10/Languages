import mysql.connector

connect =  mysql.connector.connect(host='localhost',user='root',password='jxgxn_10_@123',database='jagan')

cursor=connect.cursor()

update = "UPDATE salary SET age=20 WHERE id=%s"

val=8

change=(val,) #using comma in change after val 
              #because we are using tuple() only using one val 
              #so after using one val we use, that's only it is considered as tuple

cursor.execute(update,change)

connect.commit()

print(cursor.rowcount,"rows affected")

"""select = "SELECT *FROM salary"

cursor.execute(select)

fetch = cursor.fetchall()

for x in fetch:
    print(x)"""

