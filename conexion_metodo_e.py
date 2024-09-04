import mysql.connector
from mysql.connector import Error

class Conexion:
    @staticmethod
    def obtener_conexion():
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                database='mascotas_db',
                user='root',
                password='12345678',
                port=3309
            )
            if conexion.is_connected():
                return conexion
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    @staticmethod
    def insertar_mascota(nombre, especie, edad, propietario_id):
        conexion = Conexion.obtener_conexion()
        if conexion is not None:
            try:
                cursor = conexion.cursor()
                query = """
                INSERT INTO mascotas (nombre, especie, edad, propietario_id)
                VALUES (%s, %s, %s, %s)
                """
                valores = (nombre, especie, edad, propietario_id)
                cursor.execute(query, valores)
                conexion.commit()
                print(f"Mascota {nombre} insertada correctamente.")
            except Error as e:
                print(f"Error al insertar mascota: {e}")
            finally:
                cursor.close()
                conexion.close()
        else:
            print("No se pudo establecer la conexión con la base de datos.")

# Ejemplo. La clase invoca el método insertar
# NO se necesitó crear objetos conexion1, conexion2,...
Conexion.insertar_mascota('Pipo', 'Gato', 3, 1)
