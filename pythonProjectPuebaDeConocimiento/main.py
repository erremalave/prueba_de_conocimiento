class Producto:
    productos = {}

    def __init__(self, id, nombre, descripcion, costo, cantidad, margen_de_venta):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.margen_de_venta = margen_de_venta
        self.precio_de_venta = None

    def calcular_precio_de_venta(self):
        if self.margen_de_venta <= 0:
            raise ValueError("El margen de venta debe ser mayor que cero")
        self.precio_de_venta = self.costo / (1 - self.margen_de_venta)

    def registrar_producto(self):
        if self.id in Producto.productos:
            raise ValueError(f"El producto con ID {self.id} ya está registrado")
        self.calcular_precio_de_venta()
        Producto.productos[self.id] = {
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "costo": self.costo,
            "cantidad": self.cantidad,
            "precio_de_venta": self.precio_de_venta
        }

    @classmethod
    def obtener_productos(cls):
        return cls.productos

def mostrar_menu():
    print("1. Registrar un producto")
    print("2. Mostrar productos registrados")
    print("3. Salir")
    return input("Elija una opción: ")

while True:
    opcion = mostrar_menu()

    if opcion == "1":
        id = int(input("ID del producto: "))
        nombre = input("Nombre del producto: ")
        descripcion = input("Descripción del producto: ")
        costo = float(input("Costo del producto: "))
        cantidad = int(input("Cantidad disponible: "))
        margen_de_venta = float(input("Margen de venta (como decimal, por ejemplo, 0.2 para 20%): "))

        nuevo_producto = Producto(id, nombre, descripcion, costo, cantidad, margen_de_venta)
        nuevo_producto.registrar_producto()
        print("Producto registrado con éxito.\n")

    elif opcion == "2":
        productos_registrados = Producto.obtener_productos()
        print("\nProductos registrados:")
        for producto_id, producto_info in productos_registrados.items():
            print(f"ID: {producto_id}, Nombre: {producto_info['nombre']}, Precio de Venta: {producto_info['precio_de_venta']}")
        print()

    elif opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, elija una opción válida.\n")
