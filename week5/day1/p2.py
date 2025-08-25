import psycopg2
from p1 import cursor
conn=psycopg2.connect(
    database='postgres',
    user='postgres',
    password='mehta1012',
    host='localhost',
    port='1120'
)
conn.autocommit = True
cursor=conn.cursor()
# conn.autocommit(True)


sql = '''CREATE TABLE Emp(
   FIRST_NAME CHAR(0) NOT NULL,
   LAST_NAME CHAR(0),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''  # Define the SQL statement



# cursor.execute(sql)
print("Table created successfully........")



conn.close()  # Closing the connection