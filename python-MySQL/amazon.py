import mysql.connector

connection = mysql.connector.connect(host='localhost',user='root',password='jxgxn_10_@123')

cursor = connection.cursor()



createDb = "CREATE DATABASE IF NOT EXISTS AMAZON"

cursor.execute(createDb)

if connection.is_connected():
    connection.database = "AMAZON"
    print("connected")
    createtable = "CREATE TABLE IF NOT EXISTS Products(ID INT PRIMARY KEY,BRAND VARCHAR(400),MODEL VARCHAR(300),PRICE INT)"
    Insertintoproducts="INSERT IGNORE INTO Products(ID,BRAND,MODEL,PRICE) VALUES(%s,%s,%s,%s)"
    Valueofproducts = [(1,'Realme','Realme12pro5g',29999),(2,'POCO','pocox65g',21999),(3,'Motorola','Edge40',22999),(4,'vivo','vivox100',63999),(5,'iPhone','iPhone15',68999)]

    createtable2 = "CREATE TABLE IF NOT EXISTS Customers(ID INT ,CustomerName VARCHAR(300),Phoneno BIGINT PRIMARY KEY,Address VARCHAR(300))"
    InsertintoCustomers="INSERT IGNORE INTO Customers(ID,CustomerName,Phoneno,Address) VALUES(%s,%s,%s,%s)"
    ValueofCustomers = [(1,'Jagan',7904136090,'297:Rajaji Street'),(2,'Hemanth',9089790990,'102:Balaji nagar perambur'),(3,'Sakar',8768546790,'233:Muthumariamman kovil'),(4,'Praveen',6545789023,'908:avadiStreet'),(5,'Heman',7890654321,'313:Highcourt Streer')]

    cursor.execute(createtable)
    cursor.executemany(Insertintoproducts,Valueofproducts)

    cursor.execute(createtable2)
    cursor.executemany(InsertintoCustomers,ValueofCustomers)
    connection.commit()

    user=input("products or customers:")
    String1 = "products"
    String2 = "customers"

    if user==String1.lower() or user ==String1.upper() or user== String1.title():
        select = "SELECT *FROM Products AS PRODUCTSTABLE ORDER BY ID"
        cursor.execute(select)
        fetchall = cursor.fetchall()
        for x in fetchall:
             print(x)
    elif user==String2.upper() or user==String2.lower() or user==String2.title():
         select1 = "SELECT *FROM Customers AS CUSTOMERSTABLE ORDER BY ID"
         cursor.execute(select1)
         fetchall = cursor.fetchall()
         for y in fetchall:
             print(y)



     