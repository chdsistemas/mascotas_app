import mysql.connector
from datetime import date

# Configuración de la conexión
conn = mysql.connector.connect(
    host='localhost',
    user='root',  #
    password='your_password',  # Cambia por tu contraseña
    database='pet_care'  # Cambia por el nombre de tu base de datos
)

try:
    cursor = conn.cursor()

    # Iniciar una transacción
    conn.start_transaction()

    # Insertar un nuevo usuario
    usuario_query = '''
    INSERT INTO usuarios (nombre, email, password_hash)
    VALUES (%s, %s, %s)
    '''
    usuario_data = ('Juan Pérez', 'juan.perez@example.com', 'hashed_password')
    cursor.execute(usuario_query, usuario_data)

    # Obtener el ID del usuario insertado
    id_usuario = cursor.lastrowid

    # Insertar un nuevo administrador
    administrador_query = '''
    INSERT INTO administradores (id_usuario, cargo, fecha_ingreso)
    VALUES (%s, %s, %s)
    '''
    administrador_data = (id_usuario, 'Gerente', date.today())
    cursor.execute(administrador_query, administrador_data)

    # Confirmar los cambios
    conn.commit()
    print("Datos insertados correctamente en ambas tablas.")

except mysql.connector.Error as err:
    # Revertir los cambios si ocurre un error
    conn.rollback()
    print(f"Error: {err}")
finally:
    # Cerrar la conexión
    cursor.close()
    conn.close()
