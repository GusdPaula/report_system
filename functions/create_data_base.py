import sqlite3
import os

PATH = os.getcwd() + '/database/products.db'

print(PATH)

def create_shopping_table():
    # Connect to the database (create it if it doesn't exist)
    conn = sqlite3.connect(PATH)

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create a table for products with columns: product_id, date, product_name, product_price
    cursor.execute('''CREATE TABLE IF NOT EXISTS shopping
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date DATE,
                    product_id INTEGER,
                    price REAL,
                    amount INTEGER,
                    total REAL,
                    FOREIGN KEY(product_id) REFERENCES products(id))''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def create_products_table():
    # Connect to the database (create it if it doesn't exist)
    conn = sqlite3.connect(PATH)

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create a table for products with columns: product_id, date, product_name, product_price
    cursor.execute('''CREATE TABLE IF NOT EXISTS product
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT)''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_products_table()
    create_shopping_table()