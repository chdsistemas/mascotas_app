class Menu:
    # Clase para imprimir un sistema de menús de la app

    @staticmethod
    def menu_principal():
        while True:
            try:
                print('MENU PRINCIPAL')
                print('1. Propietarios')
                print('2. Veterinarios')
                print('3. Administradores')
                print('4. Mascotas')
                print('5. Historial de la mascosta')
                print('6. Productos')
                print('7. Servicios')
                print('8. Citas')
                print('9. Salir')
                opcion = int(input('Selecciones una opcion: '))
                if opcion == 1:
                    Menu.menu_propietarios()
                elif opcion == 2:
                    print('Menu Veterinarios')
                elif opcion == 3:
                    print('Menu Administradores')
                elif opcion == 4:
                    print('Menu Mascotas')
                elif opcion == 5:
                    print('Menu Historial de Mascotas')
                elif opcion == 6:
                    print('Menu Productos')
                elif opcion == 7:
                    print('Menu Servicios')
                elif opcion == 8:
                    print('Menu Citas')
                elif opcion == 9:
                    print('Gracias por usar la app')
                    break
            except ValueError:
                print('Seleccione un número')

            except KeyboardInterrupt:
                print('Captura cancelada. Seleccione una opcion válida')
                continue


    def menu_propietarios():
        while True:
            try:
                print('Menu Propietarios')
                print('1. Registrar un nuevo propietario')
                print('2. Consultar propietario por id')
                print('3. Consultar propietario por nombre')
                print('4. Consultar propietarios')
                print('5. Actualizar propietario por id')
                print('6. Eliminar propietario')
                print('7. Salir')

                opcion = int(input('Seleccione una opcion'))
                if opcion == 1:
                    from conexion10 import BaseDatos
                    from propietario import Propietario
                    BaseDatos.conectar()
                    propietario1 = Propietario()
                    propietario1.registrar_propietario()
                if opcion == 2:
                    print('En desarrollo')
            except ValueError:
                print('Escriba u valor numérico')
            except KeyboardInterrupt:
                print('Ha cancelado la captura, intente de nuevo')
                continue

Menu.menu_principal()
