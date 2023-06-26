import sqlite3
from model import Product
DATABASE_FILE = "db.sqlite"

def connect_database():
    con = sqlite3.connect(DATABASE_FILE, check_same_thread=False)
    return con

def get_products(db_connection, limit, offset):
    productFromDatabase = []
    cursor = db_connection.cursor();
    res = cursor.execute(f"SELECT id, title from products LIMIT {limit} OFFSET {offset}");
    for v in res:
        productFromDatabase.append(Product(v[0], v[1]))

    return productFromDatabase


