from datetime import datetime
class HistorialMedico:
    def __init__(
            self,
            codigo: int,
            fecha,
            descripcion: str,
            tratamiento: str):
        self.__codigo = codigo
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tratamiento = tratamiento
    
    
    def get_codigo(self):
        return self.__codigo
    

    def set_codigo(self):
        codigo = int(input('Codigo del  tratamiento médico: '))
        self.__codigo = codigo

    def get_fecha(self):
        return self.__fecha
    

    def set_fecha(self):
        while True:
            fecha_capturada = input('Fecha del tratamiento (dd-mm-aaaa): ')
            try:
                fecha_procesada = datetime.strptime(fecha_capturada, '%d/%m/%Y')
                print(f'Fecha procesada correctamente: {fecha_procesada}')
                self.__fecha = fecha_procesada
                break
            except ValueError:
                print('Formato de fecha incorrecto. Use dd/mm/aaaa')


    def get_descripcion(self):
        return self.__descripcion
    

    def set_descripcion(self):
        descripcion = str(input('Descripción del tratamiento médico: '))
        self.__descripcion = descripcion


    def get_tratamiento(self):
        return self.__tratamiento
    

    def set_tratamiento(self):
        tratamiento = str(input('Escriba el tratamiento a seguir: '))
        self.__tratamiento = tratamiento



historial1 = HistorialMedico('','','','')
historial1.set_codigo()
historial1.set_fecha()
historial1.set_descripcion()
historial1.set_tratamiento()

print(f'Código del Historial Médico: {historial1.get_codigo()}')
print(f'Fecha del historial: {historial1.get_fecha()}')
print(f'Descripción: {historial1.get_descripcion()}')
print(f'Detalle del tratamiento: {historial1.get_tratamiento()}')

