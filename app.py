from flask import Flask, jsonify
from db import get_db_connection
from routes import main
app = Flask(__name__)

# Middleware hai ye use accordingly
@app.before_request
def log_request():
    print('Middleware logging')
app.register_blueprint(main)
if __name__ == '__main__':
    app.run(debug=True)
