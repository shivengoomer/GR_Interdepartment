from flask import Blueprint,jsonify
from db import get_db_connection 


main = Blueprint('main', __name__)
@main.route('/')
def dashboard():
    return "Geek Room DashBoard!"
@main.route('/certificates-sender')
def send():
    return "Certificate Sender"
@main.route('/users', methods=['GET'])
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