
#Ejercicio 1
print('Ejercicio 1')
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva':1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

#Ejercicio 2
print('Ejercicio 2')
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300}
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800
print(precios_frutas)

#Ejercicio 3
print('Ejercicio 3')
precios_frutas = {'Banana': 1330, 'Anana': 2500, 'Melon': 2800, 'Uva': 1450, 'Naranja': 1200, 'Manzana': 1700, 'Pera': 2300}

frutas_lista: list = []
for i in precios_frutas.keys():
    frutas_lista.append(i)
print(frutas_lista)

#Ejercicio 4
print('Ejercicio 4')
contactos = {}
for i in range(0,5):
    contacto: str = str(input("Ingrese el nombre del contacto: "))
    numero_contacto: int = int(input("Ingrese el numero del contacto: "))
    contactos[contacto] = numero_contacto
consulta: str = str(input("Ingrese un nombre para consultar numero: "))
if consulta in contactos:
    print(f"El numero de {consulta} es {contactos[consulta]}")
else:
    print("No se tiene registro de este contacto.")

#Ejercicio 5
print('Ejercicio 5')

frase: str = str(input("Ingrese una frase: "))
palabras = frase.lower().split()
palabras_unicas = set(palabras)
cantidad_palabras = {}
for palabra in palabras:
    if palabra in cantidad_palabras:
        cantidad_palabras[palabra] += 1
    else:
        cantidad_palabras[palabra] = 1
print(palabras_unicas)
print(cantidad_palabras)

#Ejercicio 6
print('Ejercicio 6')

def nombre_a_notas_promedio(n1, n2, n3):
    
    promedio = (n1 + n2 + n3)/ 3
    return promedio
for i in range(0,3):
    alumno:str = str(input("Ingrese el nombre del alumno: "))
    n1:float = float(input("Ingrese la primer nota: "))
    n2:float = float(input("Ingrese la segunda nota: "))
    n3:float = float(input("Ingrese la tercer nota: "))
    alumno = (n1, n2, n3)
    print(alumno)
    print("Su promedio es ", nombre_a_notas_promedio(n1, n2, n3))


#Ejercicio 7
print('Ejercicio 7')
parcial_1 = {10, 11, 12, 14, 16, 19, 20 }
parcial_2 = {10, 11, 13, 15, 17, 18, 20}
print("Aprobaron ambos parciales: ", parcial_1 & parcial_2)
print("Aprobaron solo uno de los parciales: ", parcial_1 ^ parcial_2)
print("Aprobaron por lo menos un parcial: ", parcial_1 | parcial_2)


#Ejercicio 8
print('Ejercicio 8')

productos_stock = {'Auriculares': 3, 'Mouse': 6}
bandera: bool = True
while bandera:
    print(productos_stock)
    opcion: str = str(input("""Por favor ingrese una opcion
    1)Agregar un nuevo producto si no existe.
    2)Agregar unidades al stock si el producto ya existe.
    3)Consultar el stock de un producto ingresado
    4)Salir
    : """))
    if opcion == "1":
        bandera_1: bool = True
        while bandera_1:
            producto: str = str.capitalize(input("Ingrese un producto: "))
            if not producto in productos_stock and producto != "":
                productos_stock[producto] = 0
                bandera_1 = False
            elif producto in productos_stock:
                opcio_1:str =  str.upper(input("El producto ya existe, Desea agregar otro producto o salir al menu? (A/S): "))
                if opcio_1 == "A":
                    bandera_1 = True
                elif opcio_1 == "S":
                    bandera_1 = False
            else:
                print("El dato ingresado es incorrecto, intente de nuevo")

    elif opcion == "2":
        bandera_2: bool = True
        while bandera_2:
            producto_add: str = str.capitalize(input("Ingrese el producto para agregar stock: "))
            if producto_add in productos_stock:
                stock_add: int = int(input("Ingrese la cantidad: "))
                productos_stock[producto_add] = stock_add
                bandera_2 = False
            else:
                print("El producto ingresado no existe o es incorrecto, intente de nuevo: ")
            

    elif opcion == "3":
        bandera_3: bool = True
        while bandera_3:
            producto_B: str = str.capitalize(input("Ingrese el producto para consultar stock: "))
            if producto_B in productos_stock:
                print(f"El producto {producto_B} tiene {productos_stock[producto_B]} articulos disponibles")
                bandera_3 = False
            else:
                print("El producto ingresado no existe o es incorrecto, intente de nuevo: ")
    elif opcion == "4":
        bandera = False
    else:
        print("La opcion ingresada es incorrecta, intente nuevamente")

#Ejercicio 9
print('Ejercicio 9')

agenda = {("lunes", "14:45"): "Arquitectura",
          ("martes", "14:40"): "Matematicas",
          ("miercoles", "14:15"): "Programacion",
          ("jueves", "14:50"): "Organizacion",
          ("viernes", "14:30"): "Programacion"
          }
def consulta_agenda(dia, hora):
    llave = (dia, hora)
    evento = agenda.get(llave)
    if evento:
        print(f"Evento programado: {evento}")
    else:
        print("No hay eventos programados en este horario.")
print(agenda)
dia_E:str = str.lower(input("Ingrese el dia: "))
hora_E:str = str(input("Ingrese la hora: "))
consulta_agenda(dia_E, hora_E)

#Ejercicio 10
print('Ejercicio 10')

pais_capital = {'Argentina': 'Buenos aires',
                'Uruguay': 'Monte video',
                'Chile': 'Santiago',
                'Espana': 'Madrid',
                'Corea del sur': 'Seoul',
                'Japon': 'Tokio'}
capital_pais = {valor:llave for llave, valor in pais_capital.items()}
print(pais_capital)
print(capital_pais)




