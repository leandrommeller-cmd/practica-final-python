# Funciones para la interfaz de la consola

# Registrar una mascota
from clases.inventario import Inventario
from clases.mascota import Gato, Perro
from clases.cliente import Cliente
from clases.venta import Venta
from clases.producto import Producto


def registrar_mascota(inventario):
    tipo = input("Ingrese el tipo de mascota (gato/perro): ").strip().lower()
    nombre = input("Ingrese el nombre de la mascota: ")
    edad = int(input("Ingrese la edad de la mascota: "))
    salud = input("Ingrese el estado de salud de la mascota: ")
    precio = float(input("Ingrese el precio de la mascota: "))

    if tipo == "perro":
        raza = input("Ingrese la raza del perro: ")
        energia = input("Ingrese el nivel de energía del perro: ")
        mascota = Perro(nombre, edad, salud, precio, raza, energia)
    elif tipo == "gato":
        raza = input("Ingrese la raza del gato: ")
        independencia = input("Ingrese el nivel de independencia del gato: ")
        mascota = Gato(nombre, edad, salud, precio, raza, independencia)
    else:
        print("Tipo de mascota no reconocido.")
        return
    return mascota

# Registrar un cliente

def registrar_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    cliente = Cliente(nombre, direccion, telefono)
    return cliente

# Registrar un producto

def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    producto = Producto(nombre, categoria, precio, cantidad)
    return producto

# Registrar una venta

def registrar_venta(clientes, inventario):
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    cliente = next((c for c in clientes if c.nombre == nombre_cliente), None)
    if not cliente:
        print("Cliente no encontrado.")
        return
    productos = []
    while True:
        nombre_producto = input("Ingrese el nombre del producto (o deje vacío para terminar): ")
        if not nombre_producto:
            break
        producto = next((p for p in inventario.lista_de_productos if p.nombre == nombre_producto), None)
        if producto:
            productos.append(producto)
        else:
            print("Producto no encontrado.")
        
        if productos:
            venta = Venta(cliente, productos)
            venta.registrar_venta()
            print("La venta ha sido registrada exitosamente.")
        else:
            print("No se han registrado productos para la venta.")

def mostrar_menu():
    print("\n--- Menú de gestión de Patas Felices ---")
    print("1. Registrar mascota")
    print("2. Registrar cliente")
    print("3. Registrar producto")
    print("4. Registrar venta")
    print("5. Mostrar información acerca de mascotas")
    print("6. Mostrar información acerca de clientes")
    print("7. Mostrar información acerca de productos")
    print("8. Generar alerta de inventario")
    print("9. Salir")

def main():
    mascotas = []
    clientes = []
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mascota = registrar_mascota(inventario)
            if mascota:
                mascotas.append(mascota)
                print(f"Mascota {mascota.nombre} registrada exitosamente.")
        
        elif opcion == "2":
            cliente = registrar_cliente()
            clientes.append(cliente)
            print(f"Cliente {cliente.nombre} registrado exitosamente.")
        
        elif opcion == "3":
            producto = registrar_producto()
            if producto:
                inventario.agregar_producto(producto)
                print(f"Producto {producto.nombre} registrado exitosamente.")
        
        elif opcion == "4":
            registrar_venta(clientes, inventario)
        
        elif opcion == "5":
            for mascota in mascotas:
                print(mascota.mostrar_información())
                if isinstance(mascota, Perro) or isinstance(mascota, Gato):
                    print(mascota.mostrar_caracteristicas())
        
        elif opcion == "6":
            for cliente in clientes:
                print(cliente.mostrar_información())
        
        elif opcion == "7":
            for producto in inventario.lista_de_productos:
                print(producto.mostrar_información())

        elif opcion == "8":
            umbral = int(input("Ingrese el umbral mínimo para generar alertas: "))
            alerta = inventario.generar_alerta(umbral)
            print(alerta)

        elif opcion == "9":
            print("Saliendo del programa. Gracias por usar Patas Felices app.")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()