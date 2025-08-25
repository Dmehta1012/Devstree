import psycopg2
conn=psycopg2.connect(
    database='postgres',
    user='postgres',
    password='mehta1012',
    host='localhost',
    port='1120'
)
cursor=conn.cursor()
cursor.execute("SELECT * FROM demo")
rows = cursor.fetchall()
for rows in rows:
    print(rows)
cursor.close()
conn.close()