class Clase1:
    def metodo_instancia(self):
        print('Este es el ejemplo de un método de instancia, usa el parámetro self')

objeto1 = Clase1()
objeto2 = Clase1()
objeto_n = Clase1()

objeto1.metodo_instancia()
objeto2.metodo_instancia()
objeto_n.metodo_instancia()

# ********************************************
class Clase2:
    atributo1 = 'Soy un atributo de Clase'
    
    @classmethod
    def metodo_clase(cls):
        print('Este es un método de clase')
        print(f'Acceder al atributo de clase desde un método: {cls.atributo1}')

print(Clase2.atributo1)
Clase2.metodo_clase()

Clase2.atributo1 = 'Hola, el atributo se ha modificado'
print(Clase2.atributo1)

objeto10 = Clase2()

print(objeto10.atributo1)
objeto10.metodo_clase()

class Clase3:
    
    @staticmethod
    def metodo_estatico():
        print('Método estático, no tiene parámetros cls ni self')

Clase3.metodo_estatico()


class Clase4:

    @staticmethod
    def raiz_cuadrada(x):
        print(f'La raiz cuadrada de {x} es {x ** 0.5 }')

Clase4.raiz_cuadrada(99)

