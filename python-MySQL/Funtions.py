import mysql.connector

def get_connection():
    connection = mysql.connector.connect(host='localhost',user='root',password='jxgxn_10_@123')
    return connection
def connect():
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("SELECT version()")
    db_version = cursor.fetchone()
    print(db_version)
connect()


