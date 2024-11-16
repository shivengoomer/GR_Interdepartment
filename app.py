from flask import Flask, jsonify
from db import get_db_connection

app = Flask(__name__)

# Middleware hai ye use accordingly
@app.before_request
def log_request():
    print('Middleware logging')


@app.route('/')
def hello():
    return "Hello, Flask!"

# example route lgaya hai change this accordingly
@app.route('/login', methods=['POST'])
def login():
    return "Login route"

# to check postgres connection
@app.route('/users', methods=['GET'])
def get_users():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users;")  # just created a random table users
        users = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(users)  # Returns data as JSON
    else:
        return "Failed to connect to the database", 500


if __name__ == '__main__':
    app.run(debug=True)
