
#Ejercicio 1
producto: list = [("notebook", 1200, 8),
                   ("mouse", 80, 4),
                   ("celular", 300, 10)]

with open("productos.txt","w") as archivo:
    for nombre, precio, cantidad in producto:
        linea = (f"{nombre},{precio},{cantidad}\n")
        archivo.write(linea)


#Ejercicio 2 
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        print(f"Producto:{nombre}|Precio:${precio}|Cantidad:{cantidad}")

#Ejercicio 3
with open("productos.txt","a") as archivo:
    nombre:str = str.lower(input("Ingrese el producto: "))
    precio:float = float(input(f"Ingrese el precio de {nombre}: "))
    cantidad: int = int(input(f"Ingrese la cantidad de {nombre}: "))
    linea = (f"{nombre},{precio},{cantidad}\n")
    archivo.write(linea)

#Ejercicio 4
productos = []
with open("productos.txt","r") as archivo:
    for linea in archivo:
        diccionario = linea.strip().split(",")
        if len(diccionario) == 3:
            nombre = diccionario[0]
            precio = float(diccionario[1])
            cantidad = int(diccionario[2])
            productos.append({
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad
            })
        else:
            print(f"Formato incorrecto en la linea {linea.strip()}")
for i in productos:
    print(i)

#Ejercicio 5
bandera = True
while bandera:
    producto_b:str = str.lower(input("Ingrese el nombre del producto que desea buscar: "))
    for producto in productos:
        if producto["nombre"].lower() == producto_b:
            print(f"Nombre:{producto['nombre']} Precio: {producto['precio']} Cantidad: {producto['cantidad']}")
        elif producto["nombre"].lower() != producto_b:
            continue
        else:
            print("El producto ingresado no existe")
    bandera_2 = True
    while bandera_2:
        opcion: str = str.lower(input("Desea seguir consultado productos? (s/n): "))
        if opcion == "s":
            bandera_2 = False
        elif opcion == "n":
            bandera_2 = False
            bandera = False
        else:
            print("La opcion ingresada es invalida, intente de nuevo")
            bandera_2 = True

#Ejercicio 6
with open("productos.txt","w") as archivo:
    for producto in productos:
        linea = (f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
        archivo.write(linea)



