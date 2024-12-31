import mysql.connector
 
connectodb = mysql.connector.connect(host='localhost',user='root',password='jxgxn_10_@123',database='jagan')

cursor = connectodb.cursor()

cursor.execute('CREATE TABLE Customer(id INT AUTO_INCREMENT PRIMARY KEY,cname VARCHAR(1000),age INT,countryofcus VARCHAR(1000))')
createtable = ("CREATE TABLE Orders(id INT AUTO_INCREMENT PRIMARY KEY, oname VARCHAR(300), age INT, countryoford VARCHAR(300))")
alter = ("CREATE TABLE salary(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(300) NOT NULL,age INT NOT NULL,countryofsal VARCHAR(300) NOT NULL )")


cursor.execute('SHOW TABLES')

for i in cursor:
    print(i) 