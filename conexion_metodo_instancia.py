import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self, host, database, user, password, puerto):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.puerto = puerto
        self.conexion = None

    def obtener_conexion(self):
        if self.conexion is None or not self.conexion.is_connected():
            try:
                self.conexion = mysql.connector.connect(
                    host=self.host,
                    database=self.database,
                    user=self.user,
                    password=self.password
                )
            except Error as e:
                print(f"Error al conectar a la base de datos: {e}")
                self.conexion = None
        return self.conexion

    def cerrar_conexion(self):
        if self.conexion is not None and self.conexion.is_connected():
            self.conexion.close()
            self.conexion = None

    def insertar_mascota(self, nombre, especie, edad, propietario_id):
        conexion = self.obtener_conexion()
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
                self.cerrar_conexion()
        else:
            print("No se pudo establecer la conexión con la base de datos.")

# Ejemplo:  
conexion = Conexion('localhost', 'mascotas_db', 'root', '12345678', 3309)
conexion.insertar_mascota('Minina', 'Gato', 7, 1)

