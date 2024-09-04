from usuario import Usuario
from conexion10 import BaseDatos

class Propietario(Usuario):
    # Atributos de la superclase junto a los atributos de Propietario
    def __init__(
        self,
        id_usuario=None,
        nombre=None,
        apellido=None,
        ciudad=None,
        barrio=None,
        direccion=None,
        telefono=None,
        email=None,
        contraseña=None):

        # Función super() invoca los atributos de la superclase Usuario
        super().__init__(
            id_usuario,
            nombre,
            apellido,
            ciudad,
            direccion,
            telefono,
            email,
            contraseña)

        # Atributo de la clase Propietario
        self._barrio = barrio

    # Métodos GET y SET

    def get_barrio(self):
        return self._barrio

    def set_barrio(self, barrio_residencia=None):
        if barrio_residencia is None:
            barrio_residencia = input('Barrio de residencia: ')
        self._barrio = barrio_residencia

    def iniciar_sesion(self):
        print('Propietario inicia sesión')

    def quitar_mascota(self):
        print('Quitando una mascota de su propietario')

    def capturar_datos(self): 
        self.set_id_usuario()
        self.set_nombre()
        self.set_apellido()
        self.set_ciudad()
        self.set_direccion()
        self.set_barrio()
        self.set_telefono()
        self.set_es_propietario()
        self.set_es_veterinario()
        self.set_es_administrador()
        self.set_email()
        self.set_contraseña()

    def registrar_propietario(self):
        self.capturar_datos() 
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_propietario = conexion.cursor()
                cursor_propietario.callproc('InsertarPropietario', [
                    self.get_id_usuario(),
                    self.get_nombre(),
                    self.get_apellido(),
                    self.get_ciudad(),
                    self.get_direccion(),
                    self.get_barrio(),
                    self.get_telefono(),
                    self.get_es_propietario(),
                    self.get_es_veterinario(),
                    self.get_es_administrador(),
                    self.get_email(),
                    self.get_contraseña()
                ])
                conexion.commit()
                print('Propietario registrado correctamente...')
            finally:
                cursor_propietario.close()
                BaseDatos.desconectar()
