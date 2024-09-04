import mysql.connector

# Conectar a la base de datos
# Recuerde que conexion es un objeto que necesita guardar los datos de la conexión
conexion = mysql.connector.connect(
    host='localhost',          
    user= 'root',         
    password= '12345678',  
    database='mascotas_db',
    port=3309    
)

# Diseñar un nuevo cursor
cursor = conexion.cursor()

# Ejecutar una consulta general
# Guardar el query en una variable
query = "SELECT * FROM usuarios"
cursor.execute(query)

# Obtener los resultados
resultados = cursor.fetchall()

print(type(resultados))
# Procesar los resultados
for fila in resultados:
    print(fila)

# Cerrar el cursor y la conexión
#cursor.close()
#conexion.close()
