from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, email, password, direccion, telefono):
        self._nombre = nombre
        self._email = email
        self._password = password  # En un sistema real, este password debería estar cifrado
        self._direccion = direccion
        self._telefono = telefono

    @abstractmethod
    def iniciar_sesion(self, email, password):
        pass

    def ver_datos(self):
        return {
            "nombre": self._nombre,
            "email": self._email,
            "direccion": self._direccion,
            "telefono": self._telefono
        }

    def modificar_datos(self, nombre=None, email=None, password=None, direccion=None, telefono=None):
        if nombre:
            self._nombre = nombre
        if email:
            self._email = email
        if password:
            self._password = password  # En un sistema real, este password debería estar cifrado
        if direccion:
            self._direccion = direccion
        if telefono:
            self._telefono = telefono

    def __repr__(self):
        return f"Usuario(nombre={self._nombre}, email={self._email}, direccion={self._direccion}, telefono={self._telefono})"

class Propietario(Usuario):
    def __init__(self, nombre, email, password, direccion, telefono):
        super().__init__(nombre, email, password, direccion, telefono)
        self._mascotas = []  # Lista para almacenar las mascotas del propietario

    def agregar_mascota(self, mascota):
        mascota.propietario = self
        self._mascotas.append(mascota)

    def agregar_cita(self, fecha, mascota, veterinario):
        if mascota in self._mascotas:
            cita = Cita(fecha, mascota, veterinario)
            veterinario.agregar_cita(cita)
            return cita
        else:
            raise ValueError("La mascota no pertenece a este propietario.")

    def iniciar_sesion(self, email, password):
        return self._email == email and self._password == password

    def __repr__(self):
        return f"Propietario(nombre={self._nombre}, email={self._email}, direccion={self._direccion}, telefono={self._telefono}, mascotas={self._mascotas})"

class Administrador(Usuario):
    def __init__(self, nombre, email, password, direccion, telefono):
        super().__init__(nombre, email, password, direccion, telefono)
        self._usuarios = []  # Lista para almacenar todos los usuarios
        self._productos = []  # Lista para almacenar los productos

    def agregar_usuario(self, usuario):
        self._usuarios.append(usuario)

    def eliminar_usuario(self, usuario):
        self._usuarios.remove(usuario)

    def actualizar_usuario(self, usuario, nuevos_datos):
        for i, u in enumerate(self._usuarios):
            if u._email == usuario._email:
                self._usuarios[i] = nuevos_datos
                break

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def eliminar_producto(self, producto):
        self._productos.remove(producto)

    def actualizar_producto(self, producto, nuevos_datos):
        for i, p in enumerate(self._productos):
            if p.nombre == producto.nombre:
                self._productos[i] = nuevos_datos
                break

    def iniciar_sesion(self, email, password):
        return self._email == email and self._password == password

    def __repr__(self):
        return f"Administrador(nombre={self._nombre}, email={self._email}, direccion={self._direccion}, telefono={self._telefono}, usuarios={self._usuarios}, productos={self._productos})"

class Veterinario(Usuario):
    def __init__(self, nombre, email, password, direccion, telefono):
        super().__init__(nombre, email, password, direccion, telefono)
        self._citas = []  # Lista para almacenar las citas del veterinario

    def agregar_cita(self, cita):
        self._citas.append(cita)

    def iniciar_sesion(self, email, password):
        return self._email == email and self._password == password

    def __repr__(self):
        return f"Veterinario(nombre={self._nombre}, email={self._email}, direccion={self._direccion}, telefono={self._telefono}, citas={self._citas})"

class Mascota:
    def __init__(self, nombre, especie, edad):
        self._nombre = nombre
        self._especie = especie
        self._edad = edad
        self._propietario = None  # Inicialmente no tiene propietario

    @property
    def propietario(self):
        return self._propietario

    @propietario.setter
    def propietario(self, propietario):
        self._propietario = propietario

    def __repr__(self):
        return f"Mascota(nombre={self._nombre}, especie={self._especie}, edad={self._edad}, propietario={self._propietario._nombre if self._propietario else 'No asignado'})"

class Cita:
    def __init__(self, fecha, mascota, veterinario):
        self._fecha = fecha
        self._mascota = mascota
        self._veterinario = veterinario

    def __repr__(self):
        return f"Cita(fecha={self._fecha}, mascota={self._mascota._nombre}, veterinario={self._veterinario._nombre})"

class Producto:
    def __init__(self, nombre, descripcion, precio):
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio

    def __repr__(self):
        return f"Producto(nombre={self._nombre}, descripcion={self._descripcion}, precio={self._precio})"

# Ejemplo de uso
# Crear usuarios
propietario = Propietario("Juan Pérez", "juan.perez@example.com", "password123", "Calle 123", "555-1234")
admin = Administrador("Maria Admin", "maria.admin@example.com", "adminpass", "Calle Admin 1", "555-5678")
veterinario = Veterinario("Dr. Smith", "dr.smith@example.com", "vetpass", "Calle Vet 2", "555-8765")

# Crear una mascota
mascota1 = Mascota("Fido", "Perro", 3)

# Agregar la mascota al propietario
propietario.agregar_mascota(mascota1)

# El propietario agrega una cita para su mascota
cita1 = propietario.agregar_cita("2024-07-15", mascota1, veterinario)

# Crear productos
producto1 = Producto("Vacuna Rabia", "Vacuna contra la rabia", 50.0)
producto2 = Producto("Desparasitación", "Desparasitación completa", 30.0)

# El administrador gestiona usuarios y productos
admin.agregar_usuario(propietario)
admin.agregar_usuario(veterinario)
admin.agregar_producto(producto1)
admin.agregar_producto(producto2)

# Mostrar la información de los usuarios y las citas
print(propietario)
print(admin)
print(veterinario)
print(cita1)
print(producto1)
print(producto2)

# Intentar iniciar sesión
print("Inicio de sesión propietario:", propietario.iniciar_sesion("juan.perez@example.com", "password123"))
print("Inicio de sesión admin:", admin.iniciar_sesion("maria.admin@example.com", "adminpass"))
print("Inicio de sesión veterinario:", veterinario.iniciar_sesion("dr.smith@example.com", "vetpass"))

# Ver datos del propietario
print("Datos del propietario:", propietario.ver_datos())

# Modificar datos del propietario
propietario.modificar_datos(nombre="Juan P.", telefono="555-4321")
print("Datos modificados del propietario:", propietario.ver_datos())

# Ver datos del administrador
print("Datos del administrador:", admin.ver_datos())

# Modificar datos del administrador
admin.modificar_datos(email="maria.admin@newexample.com")
print("Datos modificados del administrador:", admin.ver_datos())

# Ver datos del veterinario
print("Datos del veterinario:", veterinario.ver_datos())

# Modificar datos del veterinario
veterinario.modificar_datos(direccion="Calle Vet Nueva")
print("Datos modificados del veterinario:", veterinario.ver_datos())
