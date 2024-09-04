import mysql.connector
from mysql.connector import Error

class BaseDatos:
    HOST='localhost'
    DATABASE='mascotas_db'
    USER='root'
    PASSWORD='12345678'
    PORT=3309
    conexion = None

    @classmethod
    def abrir(cls):
        if cls.conexion is None or not cls.conexion.is_connected():
            try:
                cls.conexion = mysql.connector.connect(
                    cls.HOST,
                    cls.DATABASE,
                    cls.USER,
                    cls.PASSWORD,
                    cls.PORT                
                )
                if cls.conexion.is_connected():
                    print('Conexión establecida')
                    return cls.conexion
            except Error as e:
                print(f'Ocurrió un error en la conexión: {e}')
                return None
    def cerrar(cls):
        if cls.conexion is not None and cls.conexion.is_conected():
            cls.conexion.close()
            print('Conexión cerrada...')

BaseDatos.abrir()

