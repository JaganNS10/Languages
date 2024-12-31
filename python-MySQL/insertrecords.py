import mysql.connector

connect = mysql.connector.connect(host='localhost',password='jxgxn_10_@123',user='root',database='jagan')

connecttocursor = connect.cursor()

insertintocus = ("INSERT INTO Customer (cname,age,countryofcus) VALUES(%s,%s,%s)")
valofcus = [('kamesh',31,'germany'),('jagan',19,'india'),('adhtiya',20,'brazil'),('prashth',19,'america'),('john',22,'america'),('adhiyan',23,'india'),('rajesh',24,'franch'),('kanishkar',22,'japan')]

insertintoor = ("INSERT INTO Orders (oname,age,countryoford) VALUES (%s,%s,%s)")
valofor = [('mohit',20,'franch'),('manoj',25,'china'),('vignesh',21,'canada'),('dhivakar',26,'swzeraland'),('sai',23,'india'),('jon',29,'america'),('pragedeesh',30,'japan'),('sanjay',18,'italy')]
 
connecttocursor.executemany(insertintocus,valofcus)
connecttocursor.executemany(insertintoor,valofor)

connect.commit()

print(connecttocursor.rowcount,"rows affected")





