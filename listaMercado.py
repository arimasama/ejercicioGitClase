def agregar_producto():
    #Función para solicitar los datos de un producto y devolver un diccionario con la información.
    nombre = input("Ingrese el nombre del producto: ")
    
    # Validación para el valor del producto
    while True:
        try:
            valor = float(input("Ingrese el valor del producto: "))
            break  # Si la conversión es exitosa, salimos del bucle
        except ValueError:
            print("Error: El valor debe ser un número. Inténtelo de nuevo.")

    tipo_producto = input("Ingrese el tipo de producto: ")
    
    # Validación para la cantidad del producto
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad disponible del producto: "))
            break  # Si la conversión es exitosa, salimos del bucle
        except ValueError:
            print("Error: La cantidad debe ser un número entero. Inténtelo de nuevo.")

    print("")

    # Crear un diccionario para el producto
    producto = {
        "nombre": nombre,
        "valor": valor,
        "tipo_producto": tipo_producto,
        "cantidad": cantidad
    }
    return producto


def solicitar_productos():
    #Función principal para solicitar y almacenar al menos 5 productos.
    productos = [] 

    # Bucle para asegurar que se ingresen al menos 2 productos
    while len(productos) < 2:
        print(f"Ingrese el producto número {len(productos)+1}")
        productos.append(agregar_producto())

    # Una vez ingresados 2 productos, preguntar si se desean añadir más
    while True:
        continuar = input("¿Desea ingresar otro producto? (s/n): ")
        if continuar.lower() == 's':
            productos.append(agregar_producto())
        if continuar.lower() == 'n':
            break
        else:
            print("Debe ingresar's' o 'n'.")

    return productos

# Ejemplo de uso de la función
productos_registrados = solicitar_productos()

# Ciclo for para mostrar los productos registrados
for i, producto in enumerate(productos_registrados, start=1):
    print(f"Producto {i}:")
    print(f"  Nombre: {producto['nombre']}")
    print(f"  Valor: {producto['valor']}")
    print(f"  Tipo: {producto['tipo_producto']}")
    print(f"  Cantidad: {producto['cantidad']}")
    print()
