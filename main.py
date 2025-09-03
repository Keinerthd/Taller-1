ventas = []
productos = {
    "1": ("Arroz", 2000),
    "2": ("pollo", 5000),
    "3": ("Pescado", 7000),
    "4": ("Leche", 2500)
}

def crear_ventas():
    print("\n---CREANDO NUEVA VENTA---")
    id_venta = input("Ingrese el id de la venta: ")

    print("\n---PRODUCTOS DISPONIBLES---")
    for num, (nombre, precio) in productos.items():
        print(f"{num}. {nombre} - ${precio}")

    opcion = input("Seleccione un producto: ")
    if opcion in productos:
        producto, precio_unitario = productos[opcion]
        cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
        venta = [id_venta, producto, cantidad, precio_unitario]
        ventas.append(venta)
        print("Venta registrada:", venta)
    else:
        print("Opcion invalida")



def listar_ventas():
    print("\n---LISTA DE VENTAS---")
    if not ventas:
        print("No hay ventas registradas.")
    else:
        for v in ventas:
            print(f"ID: {v[0]} | Producto: {v[1]} | Cantidad: {v[2]} | Precio unitario: {v[3]}")
        

def buscar_por_ID():
    print("\n---BUSCANDO VENTAS POR ID")
    id_searchingxd = input("Ingrese la id que desea buscar: ")
    for k in ventas:
        if id_searchingxd == k[0]:
            print(f"venta encontrada: {k}")
        else:
            print("Id no encontrada")
        


def modificar():
    print("\n---MODIFICANDO UNA VENTA---")
    id_existente = input("Ingrese la ID de la venta que desea reemplazar: ")
    for k in ventas:
        if id_existente == k[0]:
            print(f"Venta elegida: {k}")
            n_cantidad = int(input("Ingrese la nueva cantidad: "))
            k[2] = n_cantidad
        else:
            print("ID de venta no encontrada")

def eliminar():
    print("\n---ELIMINANDO UNA VENTA---")
    id_elim = input("Ingrese la ID de la venta que desea eliminar: ")
    for k in ventas:
        if id_elim == k[0]:
            print(f"Venta elegida: {k}")
            print("Eliminando...*")
            ventas.remove(k)
            print("Venta eliminada")
        else:
            print("ID no encontrada")

def calcular_totales():
    print("\n---CALCULANDO TOTALES DE VENTAS---")
    total = sum(k[2] * k[3] for k in ventas)
    print(f"ingreso total: ${total}")

def menu():
    while True:
        print("\n---MENU PRINCIPAL---")
        print("1. Crear nueva venta")
        print("2. Listar ventas")
        print("3. Buscar por ID")
        print("4. Modificar")
        print("5. Eliminar")
        print("6. Calcular totales (ingreso total)")
        print("7. Salir")

        op = input("Elige una opcion: ")
        if op == ("1"):
            crear_ventas()
        elif op ==("2"):
            listar_ventas()
        elif op ==("3"):
            buscar_por_ID()
        elif op ==("4"):
            modificar()
        elif op ==("5"):
            eliminar()
        elif op ==("6"):
         calcular_totales()
        elif op ==("7"):
            print("Saliendo del menu...*")
            break
menu()