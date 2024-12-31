import mysql.connector

connect = mysql.connector.connect(host='localhost',user='root',password='jxgxn_10_@123')

cursor = connect.cursor()
connect.database = 'jagan'

userTable = input("ENTER THE TABLENAME:")

colunms = int(input("ENTER HOW MANY COLUNMS:"))

colunm1 = []
for i in range(colunms):
    user1=input(f"ENTER THE COLUNM {i+1}:")
    userType = input(f"ENTER THE TYPE {i+1}:")
    colunm1.append(f"{user1} {userType}")

CreateTable = f"CREATE TABLE IF NOT EXISTS {userTable}({','.join(colunm1)})"
cursor.execute(CreateTable)
print("Table Created...")

InsertRecord = int(input("How many record:"))
record = []
for i in range(InsertRecord):
    changeofrecord=[]
    for j in colunm1:
        value = input(f"ENTER THE {j.split()[0]} {i+1}:")
        changeofrecord.append(value)
    record.append(tuple(changeofrecord))

result = ['%s']*len(record)
join = ','.join(result)
Insert = f"INSERT IGNORE INTO {userTable} VALUES({join})"
cursor.executemany(Insert,record)
print(cursor.rowcount,"affected")

select = f"SELECT *FROM {userTable}"

cursor.execute(select)

fetch = cursor.fetchall()
for x in fetch:
    print(x)




