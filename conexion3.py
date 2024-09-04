import mysql.connector
from mysql.connector import errorcode

class ConexionDB:
    _conexion = None
    _cursor = None
    _HOST='localhost'
    _USER='root'
    _PASSWORD='12345678'
    _DATABASE='mascotas_db'
    _PORT=3309


    @classmethod
    def abrir(cls):
        try:
            cls._conexion = mysql.connector.connect(
                host=cls._HOST,
                user=cls._USER,
                password=cls._PASSWORD,
                database=cls._DATABASE,
                port=cls._PORT
            )
            cls._cursor = cls._conexion.cursor()
            print('Conexión abierta')
            
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Nombre o contraseña incorrecta')
            elif error.errno == errorcode.ER_BAD_DB_ERROR:
                print('Base de datos no encontrada')
            else:
                print(error)

    @classmethod
    def cerrar(cls):
        if cls._cursor:
            cls._cursor.close()
        if cls._conexion:
            cls._conexion.close()
            print('Conexión cerrada')

    @classmethod
    def ejecutar_query(cls, query, params=None):
        if cls._conexion is None:
            raise Exception('Base de datos no conectada')
        try:
            cls._cursor.execute(query, params)
            cls._conexion.commit()
        except mysql.connector.Error as error:
            print(f"Error: {error}")
            cls._conexion.rollback()

    @classmethod
    def buscar_uno(cls, query, params=None):
        if cls._conexion is None:
            raise Exception('Base de datos no conectada')
        cls._cursor.execute(query, params)
        return cls._cursor.fetchone()

    @classmethod
    def buscar_todos(cls, query, params=None):
        if cls._conexion is None:
            raise Exception('Base de datos no conectada')
        cls._cursor.execute(query, params)
        return cls._cursor.fetchall()
    
    @classmethod
    def aprobar_query(cls):
        if cls._conexion:
            cls._conexion.commit()

    @classmethod
    def deshacer_query(cls):
        if cls._conexion:
            cls._conexion.rollback()
            print('Operación SQL rechazada')


ConexionDB.abrir()
ConexionDB.ejecutar_query('INSERT INTO usuarios(id_usuario,nombre, apellido,ciudad, direccion,telefono,es_propietario,es_veterinario,es_administrador,email,contraseña) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(2002,'JESUS','HDZ','VILLETA','CALL45','333466',1,1,1,'correo3@','1234'))
ConexionDB.aprobar_query()


