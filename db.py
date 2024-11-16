import psycopg2  # Use psycopg2 instead of psycopg
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the connection string from the environment variable
connection_string = os.getenv('DATABASE_URL')

# Function to establish the database connection
def get_db_connection():
    try:
        connection = psycopg2.connect(connection_string)
        print("Database connected successfully")
        return connection
    except Exception as error:
        print("Database connection error:", error)
        return None
