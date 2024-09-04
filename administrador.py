from datetime import datetime
from usuario import Usuario
from conexion import ConexionDB
class Administrador(Usuario):
    #Declaración de atributos de superclase Usuario y de la subclase Administrador
    def __init__(
        self,
        id_usuario: int,
        nombre: str,
        apellido: str,
        ciudad: str,
        direccion: str,
        telefono: str,
        email: str,
        contraseña: str,
        cargo: str,
        fecha_ingreso):

        #Atributos de la superclase Usuario
        super().__init__(
        id_usuario,
        nombre,
        apellido,
        ciudad,
        direccion,
        telefono,email,
        contraseña)

        #Atributos propios de la clase Administrador
        self.__cargo = cargo
        self.__fecha_ingreso = fecha_ingreso


    def get_cargo(self):
        return self.__cargo
    

    def set_cargo(self):
        while True:
            cargo = str(input('Nombre de su cargo en la empresa: '))
            if (5 <= len(cargo) <= 20):
                self.__cargo = cargo
                break
            else:
                print('Su cargo no es válido. Intente de nuevo')


    def get_fecha_ingreso(self):
        return self.__fecha_ingreso
    
    def set_fecha_ingreso(self):
        while True:
            fecha_capturada = input('Fecha de ingreso a la empresa (dd-mm-aaaa): ')
            try:
                fecha_procesada = datetime.strptime(fecha_capturada, '%d/%m/%Y')
                print(f'Fecha procesada correctamente: {fecha_procesada}')
                self.__fecha_ingreso = fecha_procesada
                break
            except ValueError:
                print('Formato de fecha incorrecto. Use dd/mm/aaaa')
          
    @classmethod
    def registrar_administrador(cls, id_usuario, cargo, fecha_ingreso):
        try:
            ConexionDB.abrir()
            
            






    def gestionar_usuario():
        print('Gestionando la informacion de usuarios')

    
    def gestionar_productos():
        print('Gestionando la informacion de productos')


    def iniciar_sesion(self):
        print('Inicio de sesión de usuario Administrador')



