# connect.py
import psycopg2
from config import db_params

def get_connection():
    try:
        conn = psycopg2.connect(**db_params)
        return conn
    except psycopg2.DatabaseError as error:
        print(f"Database connection error: {error}")
        return None