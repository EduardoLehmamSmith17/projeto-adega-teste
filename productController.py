import math
from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bdprojectadegatcc'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Erro na conexão com o banco de dados: {err}")
        return None

def close_db_connection(connection):
    if connection:
        connection.close()

def is_valid_string(value):
    if not value.strip() or re.search(r'[0-9!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]', value) or value == "":
        return False
    return True

def is_valid_float(value):
    try:
        float_value = float(value)
        if not math.isinf(float_value):
            return True
        else:
            return False
    except (ValueError, TypeError):
        return False

def is_valid_integer(value):
    try:
        int_value = int(value)
        return True
    except (ValueError, TypeError):
        return False

@app.route('/api/insert/products', methods=['POST'])
def insert_product():
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        value = data.get('value')
        quantity = data.get('quantity')
        category = data.get('category')
        password = data.get('password')

        if not is_valid_string(name):
            return jsonify({"error": "Nome inválido"}), 400
        if not is_valid_string(category):
            return jsonify({"error": "Categoria inválida"}), 400
        if not is_valid_float(value):
            return jsonify({"error": "Valor inválido"}), 400
        if not is_valid_integer(quantity):
            return jsonify({"error": "Quantidade inválida"}), 400

        connection = get_db_connection()
        cursor = connection.cursor()
        
        command = f'INSERT INTO product (name, description, value, quantity, category, password) VALUES ("{name}", "{description}", {value}, {quantity}, "{category}", {password})'
        
        cursor.execute(command)
        connection.commit()

        close_db_connection(connection)

        inserted_product = {
            "name": name,
            "description": description,
            "value": value,
            "quantity": quantity,
            "category": category,
            "password": password
        }

        return jsonify(inserted_product)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/delete/products/<string:password>/<string:name>', methods=['DELETE'])
def delete_product(password, name):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        product = cursor.execute(f'SELECT * FROM product WHERE password = %s and name LIKE %s', (f'{password}', f'%{name}%'))
        product = cursor.fetchone()

        if product is None:
            response = {"error": "Produto não encontrado"}
            status_code = 404
        else:
            command = f'UPDATE product SET removed = 1 WHERE password = %s and name LIKE %s'
            cursor.execute(command, (f'{password}', f'%{name}%'))
            connection.commit()

            close_db_connection(connection)

            response = {"message": "Produto excluído com sucesso!", "product": product}
            status_code = 200

        return jsonify(response), status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/read/products', methods=['GET'])
def list_product():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        
        command = f'SELECT * FROM product Where Removed = 0 ORDER BY value DESC LIMIT 10'

        cursor.execute(command)
        products = []

        for row in cursor.fetchall():
            product = {
                "id": row[0],
                "name": row[1],
                "description": row[2],
                "value": row[3],
                "quantity": row[4],
                "category": row[5]
            }
            products.append(product)

        close_db_connection(connection)

        return jsonify(products)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()