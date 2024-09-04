# Importar librerías Python para conectar con MySQL
import mysql.connector
from mysql.connector import Error

# Ejemplo de programación estructurada en Python, con funciones 
def conectar():
    # Intentar una conexión a la base de datos MySQL
    try:
        conexion = mysql.connector.connect(
            host='localhost',  # Dirección del servidor de la BD MySQL
            database='mascotas_db',  # Nombre de la BD MySQL
            user='root',  # Nombre de usuario
            password='12345678',  # Contraseña del usuario
            port=3309
        )
        if conexion.is_connected():
            print("Conexión exitosa")
            return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

conectar()
