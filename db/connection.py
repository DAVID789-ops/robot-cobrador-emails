import mysql.connector
from config.settings import DB_CONFIG

def get_connection():
    try:
        conexion = mysql.connector.connect(
            host=DB_CONFIG["host"],          # Cambiar HOST -> host
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"]
        )
        
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
