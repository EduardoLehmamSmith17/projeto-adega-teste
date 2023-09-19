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
        print("Conexão com o banco de dados realizada com sucesso!")
        return connection
    except mysql.connector.Error as err:
        print(f"Erro na conexão com o banco de dados: {err}")
        return None


def close_db_connection(connection):
    if connection:
        connection.close()

# Função para validar se uma string não contém números ou caracteres especiais
def is_valid_string(value):
    # Verifica se a string contém apenas letras e não está vazia
    if not value.strip():  # Verifica se está vazia ou contém apenas espaços em branco
        return False
    if re.search(r'[0-9!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]', value):
        return False
    return True

# Função para validar se uma variável é um float válido
def is_valid_float(value):
    try:
        # Tenta converter o valor em float
        float_value = float(value)
        # Verifica se o valor não é infinito (como resultado de divisão por zero)
        if not math.isinf(float_value):
            return True
        else:
            return False
    except (ValueError, TypeError):
        return False

# Função para validar se uma variável é um inteiro válido
def is_valid_integer(value):
    try:
        # Tenta converter o valor em um inteiro
        int_value = int(value)
        return True
    except (ValueError, TypeError):
        return False

# CREATE - Endpoint para inserir um produto
@app.route('/api/insert/products', methods=['POST'])
def insert_product():
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        value = data.get('value')
        quantity = data.get('quantity')
        category = data.get('category')

        # Validações
        if not is_valid_string(name):
            return jsonify({"error": "Nome inválido"}), 400
        if not is_valid_string(category):
            return jsonify({"error": "Categoria inválida"}), 400
        if not is_valid_string(description):
            return jsonify({"error": "Descrição inválida"}), 400
        if not is_valid_float(value):
            return jsonify({"error": "Valor inválido"}), 400
        if not is_valid_integer(quantity):
            return jsonify({"error": "Quantidade inválida"}), 400

        # Conecte-se ao banco de dados
        connection = get_db_connection()
        cursor = connection.cursor()

        # Componha o comando SQL parametrizado
        command = f'INSERT INTO product (name, description, value, quantity, category) VALUES ("{name}", "{description}", {value}, {quantity}, "{category}")'
        # values = (name, description, value, quantity, category)

        # Execute o comando SQL
        cursor.execute(command)
        connection.commit()

        # fechanco a conexao
        close_db_connection(connection)

        # Crie um dicionário com os atributos do produto inserido
        inserted_product = {
            "name": name,
            "description": description,
            "value": value,
            "quantity": quantity,
            "category": category
        }

        # Retorne os atributos do produto inserido como JSON
        return jsonify(inserted_product)

    except Exception as e:
        return jsonify({"error": str(e)})

# DELETE - Endpoint para excluir um produto
@app.route('/api/delete/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    try:
        # Conecte-se ao banco de dados
        connection = get_db_connection()
        cursor = connection.cursor()

        # Componha o comando SQL parametrizado
        command = f'DELETE FROM product WHERE id = {id}'

        # Execute o comando SQL
        cursor.execute(command)
        connection.commit()

        # Fechando a conexão
        close_db_connection(connection)

        # Produto excluído com sucesso
        return jsonify({"message": "Produto excluído com sucesso!"})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run()
