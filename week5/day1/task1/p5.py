import psycopg2

# Connect to default DB to create inventory_system
conn = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='mehta1012',
    host='localhost',
    port='1120'
)
conn.autocommit = True
cur = conn.cursor()

# Create database if not exists
cur.execute("DROP DATABASE IF EXISTS simple_inventory_system;")
cur.execute("CREATE DATABASE simple_inventory_system;")
print("✅ Database created successfully")

cur.close()
conn.close()

# Connect to inventory_system database
conn = psycopg2.connect(
    database='simple_inventory_system',
    user='postgres',
    password='mehta1012',
    host='localhost',
    port='1120'
)
cur = conn.cursor()

# Create tables
cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price NUMERIC(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15)
);
""")

conn.commit()
print("✅ Tables created successfully")

cur.close()
conn.close()
