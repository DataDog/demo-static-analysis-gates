import sqlite3
from model import Product

DATABASE_FILE = "db.sqlite"


def connect_database():
    con = sqlite3.connect(DATABASE_FILE, check_same_thread=False)
    return con


def get_products(db_connection):
    cursor = db_connection.cursor()
    res = cursor.execute("SELECT id, title from products")
    return [Product(v[0], v[1]) for v in res]


def get_product_by_id(db_connection, product_id):
    cursor = db_connection.cursor()
    res = cursor.execute(f"SELECT id, title from products WHERE id={product_id}")
    return [Product(v[0], v[1]) for v in res]
