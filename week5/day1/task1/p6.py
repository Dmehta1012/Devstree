import psycopg2
conn = psycopg2.connect(
    database='simple_inventory_system',
    user='postgres',
    password='mehta1012',
    host='localhost',
    port='1120'
)
cur=conn.cursor()
cur.execute("""INSERT INTO products (product_id,product_name,price)values
            (1,'laptop',50000),
            (2,'mouse',500),
            (3,'keyboard',1000),
            (4,'monitor',10000),
            (5,'printer',8000);
""")
cur.execute("""INSERT INTO customers (customer_id,first_name,last_name,email,phone)values
            (1,'Devarsh','Mehta',  'devarsh@example.com', '9876543210'),
            (2,'Anita','Patel', 'anita@example.com', '9123456780' );
""")
conn.commit()
print("Record Inserted successfully........")
conn.close()
cur.close()



