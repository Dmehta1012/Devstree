import psycopg2
conn = psycopg2.connect(
    database='simple_inventory_system',
    user='postgres',
    password='mehta1012',
    host='localhost',
    port='1120'
)
cur=conn.cursor()
print("products table data")
def products():
    cur.execute("SELECT * FROM products")
    rows =cur.fetchall()
    for rows in rows:
        print(rows)
products()
print("Customers table data")
def customers():
    cur.execute("SELECT * FROM customers")
    rows =cur.fetchall()
    for rows in rows:
        print(rows)
customers()
cur.close()
conn.close()