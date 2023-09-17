from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

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

if __name__ == '__main__':
    app.run()
