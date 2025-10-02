class Mascota:
    def __init__(self, nombre, edad, salud, precio):
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.precio = precio

    def actualizar_información(self, edad=None, salud=None, precio=None):
        if edad is not None:
            self.edad = edad
        if salud is not None:
            self.salud = salud
        if precio is not None:
            self.precio = precio

    def mostrar_información(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salud: {self.salud}, Precio: {self.precio}"

class Perro(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, energia):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza
        self.energia = energia

    def mostrar_caracteristicas(self):
        return f"Raza: {self.raza}, Nivel de energía: {self.energia}"
    
class Gato(Mascota):
    def __init__(self, nombre, edad, salud, precio, raza, independencia):
        super().__init__(nombre, edad, salud, precio)
        self.raza = raza
        self.independencia = independencia

    def mostrar_caracteristicas(self):
        return f"Raza: {self.raza}, Independencia: {self.independencia}"