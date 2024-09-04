from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(
        self,
        id_usuario: int = None, 
        nombre: str = None, 
        apellido: str = None,
        ciudad: str = None,
        direccion: str = None,
        telefono: str = None,
        es_propietario: bool = None,
        es_veterinario: bool = None,
        es_administrador: bool = None,       
        email: str = None,
        contraseña: str = None):

        self.__id_usuario =id_usuario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__ciudad = ciudad
        self.__direccion = direccion
        self.__telefono = telefono
        self.__es_propietario = es_propietario
        self.__es_veterinario = es_veterinario
        self.__es_administrador = es_administrador
        self.__email = email
        self.__contraseña = contraseña

## Métodos GET Y SET

    def get_id_usuario(self):
        return  self.__id_usuario
    


    def set_id_usuario(self):
        while True:
            id_usuario = int(input('Escriba el Id usuario: '))
            if (100 <= id_usuario <= 100000000):
                self.__id_usuario = id_usuario
                break
            else:
                print('Ingrese un número válido:')


    
    def get_nombre(self):
        return self.__nombre


    
    def set_nombre(self):
        while True:
            nombre = str(input('Escriba su nombre: '))
            if (3 <= len(nombre) <= 20): 
                self.__nombre = nombre
                break
            else:
                print('Escriba un nombre válido.')
   

    
    def get_apellido(self):
        return self.__apellido  
    

    
    def set_apellido(self):
           while True:
            apellido = str(input('Escriba su apellido: '))
            if (3 <= len(apellido) <= 20): 
                self.__apellido = apellido
                break
            else:
                print('Apellido no válido. Intente de nuevo')
   
    
    
    def get_email(self):
        return self.__email
    
    
    
    def set_email(self):
        while True:
            email = str(input('Escriba su correo electrónico: '))
            if (5 <= len(email) <= 20): 
                self.__email = email
                break
            else:
                print('Correo no válio. Intente de nuevo')    



    def get_contraseña(self):
        return self.__contraseña
      
    
    
    def set_contraseña(self):
        while True:
            contraseña = str(input('Escriba una contraseña: '))
            if (3 <= len(contraseña) <= 20):
                import bcrypt
                salt = bcrypt.gensalt()
                contraseña_cifrada = bcrypt.hashpw(contraseña.encode('utf-8'), salt)
                print(contraseña_cifrada)
                print(salt)
                self.__contraseña = contraseña_cifrada
                break
            else:
                print('Contrsaeña no válida. Intente de nuevo')

    
    
    def get_direccion(self):
        return self.__direccion
    
    
    
    def set_direccion(self):
        while True:
            direccion = str(input('Escriba la dirección postal (Calle, carrera, vereda): '))
            if (5 <= len(direccion) <= 100): 
                self.__direccion = direccion
                break
            else:
                print('Dirección no válida. Intente de nuevo')
    
    
    
    def get_telefono(self):
        return self.__telefono
    
    
    
    def set_telefono(self):
        while True:
            telefono = str(input('Teléfono de contacto: '))
            if (5 <= len(telefono) <= 15): 
                self.__telefono = telefono
                break
            else:
                print('Número telefónico no válido. Intente de nuevo')



    def get_es_propietario(self):
        return self.__es_propietario
    


    def set_es_propietario(self):
        while True:
            try:
                es_propietario = int(input('¿Es propietario de mascota? 1=Si 0=No: '))
                if (es_propietario in [1,0]):
                    self.__es_propietario = es_propietario
                    break
                else:
                    print('Escriba SI=1; NO=0: ')
            except ValueError:
                print('Entrada no válida, intente de nuevo')
            except KeyboardInterrupt:
                print('Escriba una entrada válidad 1/0')
                break
    
    
    def get_es_veterinario(self):
        return self.__es_veterinario
    


    def set_es_veterinario(self):
        while True:
            try:
                es_veterinario = int(input('¿Es veterinario? 1=Si 0=No: '))
                if (es_veterinario in [1,0]):
                    self.__es_veterinario = es_veterinario
                    break
                else:
                    print('1=SI; 0=NO: ')
            except ValueError:
                print('Entrada no válida, intente de nuevo')
            except KeyboardInterrupt:
                print('Escriba una entrada válida 1/0')
                break



    def get_es_administrador(self):
        return self.__es_administrador
    
    
    def set_es_administrador(self):
        while True:
            try:
                es_administrador = int(input('¿Es administrador? 1=Si 0=No: '))
                if (es_administrador in [1,0]):
                    self.__es_administrador = es_administrador
                    break
                else:
                    print('1 = SI; 0 = No')
            except ValueError:
                print('Entrada no válida, intente de nuevo')
            except KeyboardInterrupt:
                print('Escriba una entrada válida 1/0')
                break
    
    
    def get_ciudad(self):
        return self.__ciudad
    
    
    
    def set_ciudad(self):
        while True:
            ciudad = str(input('Ciudad de residencia: '))
            if (2 < len(ciudad) <= 20): 
                self.__ciudad = ciudad
                break
            else:
                print('Ciudad no válida. Intente de nuevo')
 
    
    
    def get_email(self):
        return self.__email
    
    
    
    def set_email(self):
        while True:
            try:
                email = str(input('Correo electrónico: '))
                if (2 < len(email) <= 20): 
                    self.__email = email
                    break
                else:
                    print('Correo no válido. Intente de nuevo')
            except KeyboardInterrupt:
                print('Entrada cancelada por el usuario')
                continue



#Fin de los métodos SET GET

# Inicio de los métodos generales de la clase Usuario
# Los métodos públicos son accesibles desde cualquier otra clase o código de la app
# Los atributos serán privados van con doble guión bajo.

    @abstractmethod
    def iniciar_sesion(self):
        pass


