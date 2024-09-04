import mysql.connector
from mysql.connector import Error

# Función conectar para establecer una conexión a MySQL
def conectar():   
    try:
        #conexión es un objeto con los datos de la conexión
        conexion = mysql.connector.connect( 
            host='localhost',
            database='mascotas_db',
            user='root',
            password='12345678',
            port=3309
        )
        if conexion.is_connected():# Método is_connected()
            print("Conexión exitosa")
            return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def cerrar_conexion(conexion):
    # Cerrar la conexión libera recursos y aumenta la seguridad
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")

def insertar_administrador(conexion, id_usuario, nombre, apellido, ciudad, direccion, telefono, es_propietario, es_veterinario, es_administrador, email, contraseña, cargo, fecha_ingreso):
    #Inserta un nuevo propietario en la BD
    try:
        cursor = conexion.cursor()
        sql_u = "INSERT INTO usuarios(id_usuario, nombre, apellido, ciudad, direccion, telefono, es_propietario, es_veterinario, es_administrador, email, contraseña) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        datos_u = (id_usuario, nombre, apellido, ciudad, direccion, telefono, es_propietario, es_veterinario, es_administrador, email, contraseña)
        cursor.execute(sql_u, datos_u)
        sql_a = "INSERT INTO administradores(id_usuario, cargo, fecha_ingreso) VALUES (%s, %s, %s, %s)"
        datos_a = (id_usuario, cargo, fecha_ingreso)
        cursor.execute(sql_a, datos_a)
        conexion.commit()
        print(
            "Administrador insertado exitosamente")
    except Error as e:
        print(f"Error al insertar administrador: {e}")

def main():
    conexion = conectar()
    if conexion:
        insertar_administrador(
            conexion,
            input('Id del propietario: '),
            input('Nombre del propietario: '),
            input('Primero Apellido: '),
            input('Ciudad: '),
            input('Dirección: '),
            input('Teléfono: '),
            input('Es propietario (1=SI 0=No): '),
            input('Es veterinario (1=SI 0=No): '),
            input('Es administrador (1=SI 0=No): '),            
            input('Correo electrónico: '),
            input('Contraseña: '),
            input('Id: '),
            input('Cargo: '),
            input('Fecha ingreso (aaaa-mm-dd): ')
        )
        cerrar_conexion(conexion)

if __name__ == "__main__":
    main()
