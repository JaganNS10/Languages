import mysql.connector

connect=mysql.connector.connect(user='root',password='jxgxn_10_@123',host='localhost')
if connect.is_connected():
    list=[]
    for i in range(1):
        Name=input("Enter Your Name:")
        Age=int(input("Enter Your Age:"))
        sal=int(input("Enter Your salary:"))
        list.append((Name,Age,sal))
    create_Database=f'CREATE DATABASE IF NOT EXISTS {list[0][0]}'
    using_cursor=connect.cursor()
    using_cursor.execute(create_Database)
    print('Database Created....')
    connect.database=f'{list[0][0]}'
    create_Table=f'CREATE TABLE IF NOT EXISTS {list[0][0]}(ID INT AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(500),AGE INT,SAL INT)'
    using_cursor.execute(create_Table)
    print("Table Created.....")
    record=['%s']*len(list[0])
    join=','.join(record)
    Insert_record=f'INSERT INTO {list[0][0]}(NAME,AGE,SAL) VALUES({join})'
    using_cursor.executemany(Insert_record,list)
    connect.commit()
    print("Records Inserted....")
    select=f'SELECT *FROM {list[0][0]}'
    using_cursor.execute(select)
    fetch=using_cursor.fetchall()
    print("You Are Login To The Server....")
    for j in fetch:
        print(j)