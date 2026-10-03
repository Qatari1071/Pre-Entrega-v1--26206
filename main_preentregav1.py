productos = []
print("**"*25)
print(f" Bienvenido al programa de gestion de productos")
print(f" \t             MENU")
print("**"*25)
print("1. Agregar producto\n2. Mostrar productos\n3. Buscar producto\n4. Eliminar producto\n5. Salir")
opcion = input(f"Selecciona una opcion (1-5): ").strip()
opcion_valida = ["1","2","3","4","5"]
while opcion not in opcion_valida or opcion == "":
    print(f"Selecciona una opcion valida (1-5).")
    opcion = input(f"Selecciona una opcion (1-5): ").strip()
    break
while True: 
    if opcion == "1":
        print (f"Seleccionaste la opcion 1: Agregar producto")
        nombre = input(f"Nombre del producto: ").strip().title()
        if nombre == "5":
            print(f"Gracias por utilizar el programa")
            break
        while nombre == "":
            print(f"El nombre no puede estar vacio. Para salir o finalizar escribi '5'")
            nombre = input(f"Nombre del producto: ").strip().title()
            
        categoria = input(f"Nombre la categoria: ").strip().title()
        if categoria == "5":
            print(f"Gracias por utilizar el programa")
            break
        while categoria == "":
            print(f"La categoria no puede estar vacia. Para salir escribi '5'")
            categoria = input(f"Nombre la categoria: ").strip().title()

        precio_str = input (f"Precio $ (sin centavos): ")
        if precio_str == "5":
            print(f"Gracias por utilizar el programa")
            break
        while precio_str == "":
            print(f"El precio no puede estar vacio. Para salir escribi '5'")
            precio_str = input (f"Precio $ (sin centavos): ")
            if not precio_str.isdigit():
                print(f"Ingresar solo numeros positivos sin centavos. Para salir escribi '5'")
        precio = int(precio_str)
        productor_ingresado = [nombre, categoria, precio]
        productos.append (productor_ingresado)
        
    elif opcion == "2":
        print (f"Seleccionaste la opcion 2: Mostrar productos")
        if len(productos) == 0:
            print (f"No hay productos ingresados")
            break
        else:
            print (f"Productos agregados: ")
            for indice,producto in enumerate(productos,1):
                print(f"{indice}. Nombre: {producto[0]}, Categoria: {producto[1]}, Precio: {producto[2]} ")
    elif opcion == "3":
        print (f"Seleccionaste la opcion 3: Buscar producto")
        if len(productos) == 0:
            print (f"No hay productos ingresados")
            break
        producto_buscado = input (f"Ingresa el producto buscado: ").strip().lower()
        for producto_buscado in productos:
            print (f"Producto encontrado: {producto_buscado}")
    elif opcion == "4":
        print (f"Seleccionaste la opcion 4: Eliminar producto")
        if len(productos) == 0:
            print (f"No hay productos ingresados")
            break
        else:
            for i in range(len(productos)):
                print(f"{i+1}. Nombre: {productos[i][0]}, Categoria: {productos[i][1]}, Precio: $ {productos[i][2]}")
            producto_eliminar = input(f"Ingresa el numero del producto a eliminar: ").strip()
            while not producto_eliminar.isdigit():
                print(f"Selecciona un numero valido de producto a eliminar.")
                producto_eliminar = input(f"Ingresa el numero del producto a eliminar: ").strip()
            eliminado = productos.pop(int(producto_eliminar)-1)
            print(f"Producto eliminado: Nombre: {eliminado[0]}, Categoria: {eliminado[1]}, Precio: $ {eliminado[2]}" )
    #Profe>>> no comprendi bien como funciona la logica de eliminar producto, me guie con la IA:
    elif opcion == "5":
        print(f"Gracias por utilizar el programa")
else:
    print(f"Selecciona una opcion valida (1-5).")
