import mysql.connector
from mysql.connector import errorcode

class Usuario:
    def __init__(self, user_id, nombre, email):
        self.user_id = user_id
        self.nombre = nombre
        self.email = email

class Propietario(Usuario):
    def __init__(self, user_id, nombre, email, pet_id):
        super().__init__(user_id, nombre, email)
        self.pet_id = pet_id

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def create_usuario(self, usuario):
        try:
            self.connect()
            query = "INSERT INTO usuarios (user_id, nombre, email) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (usuario.user_id, usuario.nombre, usuario.email))
            self.connection.commit()
        except mysql.connector.Error as err:
            self.connection.rollback()
            print("Failed to insert into MySQL table {}".format(err))
        finally:
            self.disconnect()

    def create_propietario(self, propietario):
        try:
            self.connect()
            self.connection.start_transaction()
            query_usuario = "INSERT INTO usuarios (user_id, nombre, email) VALUES (%s, %s, %s)"
            query_propietario = "INSERT INTO propietarios (user_id, pet_id) VALUES (%s, %s)"
            self.cursor.execute(query_usuario, (propietario.user_id, propietario.nombre, propietario.email))
            self.cursor.execute(query_propietario, (propietario.user_id, propietario.pet_id))
            self.connection.commit()
        except mysql.connector.Error as err:
            self.connection.rollback()
            print("Failed to insert into MySQL table {}".format(err))
        finally:
            self.disconnect()
