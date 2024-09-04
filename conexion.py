import mysql.connector
from mysql.connector import errorcode

# Clase para gestionar la conexión a una base de datos fija estática
class BaseDatos:
    
    # Conexión con atributos de clase
    HOST='localhost'
    USER='root'
    PASSWORD='12345678'
    DATABASE='mascotas_db'
    PORT=3309
    conexion = None
    cursor = None
    

    # Método para abrir la base de datos
    @classmethod
    def abrir(cls):  
        # Al conectar pasamos las credenciales de la conexión al método abrir():
        try: 
            cls.conexion = mysql.connector.connect(
                host =cls.HOST,
                user = cls.USER,
                password = cls.PASSWORD,
                database = cls.DATABASE,
                port = cls.PORT
            )
            cls.cursor = cls.conexion.cursor()
            print('Conexión abierta...')
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Verifique las credenciales de conexión')
            elif error.errno == errorcode.ER_BAD_DB_ERROR:
                print('Base de datos no existe')
            else:
                print(error)

    # Método para cerrar la base de datos
    @classmethod
    def cerrar(cls):
        if cls.cursor:
            cls.cursor.close()
        if cls.conexion:
            cls.conexion.close()
        print('Conexión cerrada...')


# Probar apertura y cierre de la conexión
BaseDatos.abrir()
# BaseDatos.cerrar()
