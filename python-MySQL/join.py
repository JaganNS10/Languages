import mysql.connector
connect=mysql.connector.connect(host='localhost',user='root',password='jxgxn_10_@123',database='jagan')

cursor=connect.cursor()

innerjoin = "SELECT Customer.cname,Customer.countryofcus,Orders.oname,Orders.countryoford from Customer INNER JOIN Orders on Customer.age=Orders.age"

leftjoin = "SELECT Customer.cname,Customer.countryofcus,Orders.oname,Orders.countryoford from Customer LEFT JOIN Orders on Customer.age=Orders.age"

rightjoin = "SELECT Customer.cname,Customer.countryofcus,Orders.oname,Orders.countryoford from Customer RIGHT JOIN Orders on Customer.age=Orders.age"


cursor.execute(rightjoin)

fetch = cursor.fetchall()

for x in fetch:
    print(x)

