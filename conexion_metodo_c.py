import mysql.connector
from mysql.connector import Error

class Conexion:
    _conexion = None

    @classmethod
    def obtener_conexion(cls):
        if cls._conexion is None or not cls._conexion.is_connected():
            try:
                cls._conexion = mysql.connector.connect(
                    host='localhost',
                    database='mascotas_db',
                    user='root',
                    password='12345678',
                    port=3309
                )
            except Error as e:
                print(f"Error al conectar a la base de datos: {e}")
                cls._conexion = None
        return cls._conexion

    @classmethod
    def cerrar_conexion(cls):
        if cls._conexion is not None and cls._conexion.is_connected():
            cls._conexion.close()
            cls._conexion = None

    @classmethod
    def insertar_mascota(cls, nombre, especie, edad, propietario_id):
        conexion = cls.obtener_conexion()
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
        else:
            print("No se pudo establecer la conexión con la base de datos.")
        cls.cerrar_conexion()

# Ejemplo de uso:
Conexion.insertar_mascota('LUCAS', 'PERRO', 3, 101)
