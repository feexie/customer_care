from flask import Flask, jsonify, g
from flask_mysqldb import MySQL
import os
from dotenv import load_dotenv

# Create Flask application instance
app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Configure MySQL connection parameters
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')

# Initialize MySQL extension
mysql = MySQL(app)

# Database connection handling
@app.before_request
def before_request():
    g.mysql_db = mysql.connection.cursor()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'mysql_db'):
        g.mysql_db.close()

# Define routes for database operations
@app.route('/users')
def get_users():
    g.mysql_db.execute("SELECT * FROM users")
    result = g.mysql_db.fetchall()
    return jsonify(result)

# Define route for the landing page
@app.route('/')
def hello_world():
    return 'Hello, this is insightstream landing page!'

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

