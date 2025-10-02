from datetime import datetime


class Venta:
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos  # Lista de productos
        self.fecha = datetime.now()
        self.total = self.calcular_total()

    def calcular_total(self):
        return sum(producto.precio * producto.cantidad for producto in self.productos) 
    
    def registrar_venta(self):
        self.cliente.registrar_compra(self)
        return f"Venta registrada: {self.mostrar_información()}"
    
    def mostrar_información(self):
        productos_lista = ', '.join([producto.nombre for producto in self.productos])
        return f"Cliente: {self.cliente.nombre}, Productos: [{productos_lista}], Total: {self.total}"