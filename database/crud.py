import sqlite3

def connect_db():
    return sqlite3.connect("products.db")

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            description TEXT,
            price TEXT,
            address TEXT,
            image_id TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_product(name, description, price, address, image_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO products (name, description, price, address, image_id)
        VALUES (?, ?, ?, ?, ?)
    """, (name, description, price, address, image_id))
    conn.commit()
    conn.close()

def get_all_products():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name, description, price, address, image_id FROM products")
    products = cursor.fetchall()
    conn.close()
    return products

create_table()