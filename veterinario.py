from usuario import Usuario
class Veterinario(Usuario):
    # Atributos de Usuario y Veterinario
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
        especialidad:str,
        horario: str):

        # Solo atributos de la superclase Usuario
        super().__init__(
        id_usuario,
        nombre,
        apellido,
        ciudad,
        direccion,
        telefono,
        email,
        contraseña)

        # Solo atributos de la clase Veterinario
        self.especialidad = especialidad
        self.horario = horario

    # Métodos GET SET de Veterinario
    def get_especialidad(self):
        return self.__especialidad
    
    def set_especialidad(self, especialidad):
        self.__especialidad = especialidad

    
    def get_horario(self):
        return self.__horario
    
    
    def set_horario(self):
        while True:
            horario = str(input('Horario disponible (Ej. 8-18 lunes a viernes): ' ))
            if(5 < len(horario) <= 30):
                self.__horario = horario
                break
            else:
                print('Horario no válido. Intente de nuevo')

