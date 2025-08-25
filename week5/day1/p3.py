import psycopg2
from p2 import *
conn=psycopg2.connect(
    database='postgres',
    user='postgres',
    password='mehta1012',
    host='localhost',
    port='1120'
)
cursor=conn.cursor()    
cursor.execute("""INSERT INTO Emp (FIRST_NAME,LAST_NAME,AGE,SEX ,INCOME)
               VALUES('Ramesh','Kumar',32,'M',20000)""")
cursor.execute('''INSERT INTO Emp(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Vinay', 'Battacharya', 20, 'M', 6000)''')
cursor.execute('''INSERT INTO Emp(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Sharukh', 'Sheik', 25, 'M', 8300)''')
cursor.execute('''INSERT INTO Emp(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Sarmista', 'Sharma', 26, 'F', 10000)''')
cursor.execute('''INSERT INTO Emp(FIRST_NAME, LAST_NAME, AGE, SEX,
   INCOME) VALUES ('Tripthi', 'Mishra', 24, 'F', 6000)''')
print("Record Inserted successfully........")
conn.commit()
conn.close()    