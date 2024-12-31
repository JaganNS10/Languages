import mysql.connector

connect = mysql.connector.connect(host='localhost',user='root',password='jxgxn_10_@123')

cursor = connect.cursor()

userInputofDB = input("ENTER THE DATABASE NAME:")
userInputofTable1 = input("ENTER THE TABLE1 NAME:")
userInputofTable2 = input("ENTER THE TABLE2 NAME:")
CreateDB = f"CREATE DATABASE IF NOT EXISTS {userInputofDB}"
print("DATABASE CREATED...")

cursor.execute(CreateDB)
if connect.is_connected():
    connect.database=userInputofDB
    print("connected...")
    CreateTable1 = f"CREATE TABLE IF NOT EXISTS {userInputofTable1}(BRAND VARCHAR(300),MODEL VARCHAR(300),PRICE INT)"
    InsertRecord1 = int(input("ENTER HOW MANY RECORDS FOR TABLE1:"))
    Record1 =[]
    for i in range(InsertRecord1):
        changeofRecord1 = []
        for j in range(1):
            val1 = input(f"ENTER THE BRAND NAME {i+1}:")
            val2 = input(f"ENTER THE MODEL NAME{i+1}:")
            val3 = int(input(f"ENTER THE PRICE {i+1}:"))
            changeofRecord1.append(val1)
            changeofRecord1.append(val2)
            changeofRecord1.append(val3)
        Record1.append(tuple(changeofRecord1))
    join1=['%s']*3
    result = ','.join(join1)
    InsertIntoTable1 = f"INSERT IGNORE INTO {userInputofTable1} VALUES({result})"

    cursor.execute(CreateTable1)
    cursor.executemany(InsertIntoTable1,Record1)
    print("TABLE1 CREATED AND RECORDS INSERTED...")

    CreateTable2 = f"CREATE TABLE IF NOT EXISTS {userInputofTable2}(CustomerName VARCHAR(300),Phno BIGINT,Address VARCHAR(300))"
    InsertRecord2 = int(input("ENTER HOW MANY RECORDS FOR TABLE2:"))
    Record2=[]
    for x in range(InsertRecord2):
        changeofRecord2=[]
        for y in range(1):
            value1 = input(f"ENTER THE CUSTOMER NAME {x+1}:")
            value2 = int(input(f"ENTER THE PHONENO {x+1}:"))
            value3 = input(f"ENTER THE ADDRESS {x+1}:")
            changeofRecord2.append(value1)
            changeofRecord2.append(value2)
            changeofRecord2.append(value3)
        Record2.append(tuple(changeofRecord2))
    join2=['%s']*3
    result1=','.join(join2)
    InsertIntoTable2 = f"INSERT IGNORE INTO {userInputofTable2} VALUES({result1})"
    cursor.execute(CreateTable2)
    cursor.executemany(InsertIntoTable2,Record2)
    print("TABLE2 CREATED AND RECORDS INSERTED...")
    SelectTable1 = f"SELECT * FROM {userInputofTable1}"
    cursor.execute(SelectTable1)
    fetchfromTable1 = cursor.fetchall()
    for k in fetchfromTable1:
        print(k)
        
    SelectTable2 = f"SELECT * FROM {userInputofTable2}" 
    cursor.execute(SelectTable2)
    fetchfromTable2 = cursor.fetchall()
    for l in fetchfromTable2:
        print(l)
    connect.commit()



