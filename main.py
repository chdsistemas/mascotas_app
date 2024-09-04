from os import system
from mascota import Mascota
from propietario import Propietario

def main():
    try:
        while True:
            print('***************MENU MASCOTAS********************')

            print('1 -Registrar nueva mascota')
            print('2 -Buscar una mascota por código')
            print('3 -Buscar mascotas')
            print('4 -Actualizar mascota')
            print('5 -Eliminar una mascota')
            print('6 -Salir del sistema')
            print('7 -Registrar propietario')

            print('***************MENU MASCOTAS********************')

            while True:
                try:
                    opcion = int(input('Seleccione una opción del menú: '))
                    break
                except ValueError:
                    print('Opción no válida')
                except KeyboardInterrupt:
                    print('El usuario canceló la entrada')
                    continue
           
            if opcion == 1:
                system('cls')
                print('1. Registrar Mascota')
                # Crear un objeto mascota para luego insertar en la bd
                mascota1 = Mascota()
                mascota1.registrar_mascota()
            
            elif opcion == 2:
                system('cls')
                mascota1 = Mascota()
                codigo_mascota = int(input('Código de mascota a buscar: '))
                mascota1.buscar_mascota(codigo_mascota)

            elif opcion == 3:
                system('cls')
                mascota1 = Mascota()
                print('Buscando registros...')
                mascota1.buscar_mascotas()

            elif opcion == 4:
                system('cls')
                mascota1 = Mascota()
                codigo_mascota = int(input('Código de la mascota a actualizar: '))
                mascota1.actualizar_mascota(codigo_mascota)         
            
            elif opcion == 5:
                system('cls')
                mascota1 = Mascota()
                codigo_mascota = int(input('Código de la mascota a eliminar: '))
                mascota1.eliminar_mascota(codigo_mascota)

            elif opcion == 7:
                system('cls')
                print('7. Registrar Propietario')
                # Crear un objeto propietario para registrar en la bd
                propietario1 = Propietario()
                propietario1.registrar_propietario()          
            
            elif opcion == 6:
                print('Gracias por usar nuestra app..')
                break

            else:
                system('cls')
                print('Opción no válida. Intente de nuevo')
    
    except KeyboardInterrupt:
        print('El usuario ha cancelado la ejecución, por favor continue')
    except Exception as error:
        print(f'Ha ocurrido error no codificado {error}')
    finally:
        print('Intente de nuevo')

if __name__ == "__main__":
    main()
