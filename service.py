from flask import Flask, jsonify

import database as db
app = Flask(__name__)

db_connection = db.connect_database()


@app.route("/product/list", methods=["GET"])
def product_list():
    products = db.get_products(db_connection)
    return jsonify(products)


@app.route("/product/<product_id>", methods=["GET"])
def product_list_by_id(product_id):
    products = db.get_product_by_id(db_connection, product_id)
    return jsonify(products)


