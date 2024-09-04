
from administrador import Administrador
from mascota import Mascota

# Invocar los SETTER para agregar datos a cada objeto
#Instancias de clase Administrador:
administrador1 = Administrador('','','','','','','','','','')
print('************* INGRESO DE DATOS USUARIO ADMINISTRADOR ****************')
administrador1.set_id_usuario()
administrador1.set_nombre()
administrador1.set_apellido()
administrador1.set_ciudad()
administrador1.set_direccion()
administrador1.set_telefono()
administrador1.set_email()
administrador1.set_contraseña()
administrador1.set_cargo()
administrador1.set_fecha_ingreso()

#Invocar GETTER para retornar e imprimir los datos del objeto
print('******************RETORNO DATOS ADMINSITRADOR************************')
print(f'Id: {administrador1.get_id_usuario()}')
print(f'Nombre: {   administrador1.get_nombre()}')
print(f'Apellido: {administrador1.get_apellido()}')
print(f'Ciudad: {administrador1.get_ciudad()}')
print(f'Direccion: {administrador1.get_direccion()}')
print(f'Telefono: {administrador1.get_telefono()}')
print(f'Correo electrónico: {administrador1.get_email()}')
print(f'Cargo: {administrador1.get_cargo()}')
print(f'Fecha ingreso: {administrador1.get_fecha_ingreso()}')

#Invocando los demás métodos de la clase
print('************ METODOS DE ADMINISTRADOR**************')
administrador1.iniciar_sesion()
administrador1.registrar_usuario()
administrador1.actualizar_perfil()

mascota1 = Mascota('','','','','','','')

print('****************REGISTRO DE MASCOTAS******************')
mascota1.set_codigo()
mascota1.set_nombre()
mascota1.set_especie()
mascota1.set_raza()
mascota1.set_edad()
mascota1.set_peso()

print('***************IMPRESION DE DATOS DE MASCOTA****************')
print(f'Codigo: {mascota1.get_codigo()}')
print(f'Nombre: {mascota1.get_nombre()}')
print(f'Especie: {mascota1.get_especie()}')
print(f'Raza: {mascota1.get_raza()}')
print(f'Edad: {mascota1.get_edad()} años')
print(f'Peso: {mascota1.get_peso()} kg')