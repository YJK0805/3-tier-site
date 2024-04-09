import pymysql

db_settings = {
    "host": "localhost",
    "port": 3306,
    "user": "admin",
    "password": "passwd",
    "db": "testdb",
    "charset": "utf8"
}

conn = pymysql.connect(**db_settings)
with conn.cursor() as cursor:
    sql_std = 'SELECT * FROM `course`'
    cursor.execute(sql_std)
    for row in cursor:
        print(row)
    conn.close()
