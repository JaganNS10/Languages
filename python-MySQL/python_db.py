import mysql.connector

connect = mysql.connector.connect(host='localhost',user='root',password='jxgxn_10_@123')
cursor = connect.cursor()
create = f"CREATE DATABASE IF NOT EXISTS python_db "
cursor.execute(create)
if connect.is_connected():
    connect.database='python_db'
    createtablehospital = "CREATE TABLE IF NOT EXISTS Hospital(Hospital_id INT,Hospital_Name VARCHAR(500),Bed_count INT PRIMARY KEY)"
    Insertintohospital = "INSERT IGNORE INTO Hospital(Hospital_id,Hospital_Name,Bed_count) VALUES(%s,%s,%s)"
    valuesofhospital = [(1,'Mayo Clinic',200),(2,'Cleveland Clinic',400),(3,'johns Hopkins',1000),(4,'UCLA Medical centre',1500)]
    cursor.execute(createtablehospital)
    cursor.executemany(Insertintohospital,valuesofhospital)
    print("Hospital Table Created and Records Inserted...")

    createtableDoctor = "CREATE TABLE IF NOT EXISTS Doctor(Doctor_id INT PRIMARY KEY,Doctor_Name VARCHAR(500),Hospital_id INT,Joining_Date VARCHAR(500),speciality VARCHAR(500),salary INT)"
    InsertIntoDoctor = "INSERT IGNORE INTO Doctor(Doctor_id,Doctor_Name,Hospital_id,Joining_Date,speciality,salary) VALUES(%s,%s,%s,%s,%s,%s)"
    ValuesofDoctor = [(101,'David',1,'2005-02-10','pediatric',40000),(102,'Michael',1,'2018-07-23','Oncologist',20000),(103,'susan',2,'2016-05-19','Garnacologist',25000),(104,'Robert',2,'2017-12-28','pediatric',28000),(105,'linda',3,'2004-06-04','Gamacologist',42000),(106,'william',3,'20012-09-11','Dermatologist',30000),(107,'Richard',4,'2014-08-21','Garnacologist',32000),(108,'karen',4,'2011-10-17','Radiologist',30000)]
    cursor.execute(createtableDoctor)
    cursor.executemany(InsertIntoDoctor,ValuesofDoctor)
    print("Doctor Table created and records Inserted....")

    select = "SELECT * FROM Hospital"
    cursor.execute(select)
    fetch = cursor.fetchall()
    print("Hospital Table...")
    for x in fetch:
        print(x)

    selectfromdoctor = "SELECT *FROM Doctor"
    cursor.execute(selectfromdoctor)
    fetchfromdoc = cursor.fetchall()
    print("Doctor Table")
    for y in fetchfromdoc:
        print(y)

    

