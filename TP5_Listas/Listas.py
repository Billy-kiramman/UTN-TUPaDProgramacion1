# EJercicio 1
# Creo una lista vacia antes de proceder con el bucle
# esto para tener el codigo mas ordenado, defino el bucle 
# for entre 1 y 101 ya que el numero fin es excluyente y
# el 100 es multiplo de 4, luego uso la funcion append 
# para agregar los datos que cumplan el if a la lista 
# posteriormente a ello imprime los numeros correspondientes.
list =[]
for i in range(1,101):
    if i % 4 == 0:
        list.append(i)
    else:
        pass
print(list)

#Ejercicio 2
# No hay mucho que explicar solo cree la lista con 5 
# elementos y luego use el print lista con el numero
# negativo para comenzar el indice desde el final. 
lista = [3, 32, 84, "ropa", 1]
print(lista[-2])

#Ejercicio 3
# Inicio con lista vacia y uso un ciclo for ya que se 
# que me solicita una cantidad de veces (3), dentro
# del bucle solicito las tres palabras y luego
# haciendo uso del append agrego las palabras a lista.
list_vacia = []
for i in range(1,4):
    palabra: str = str(input("Ingrese una palabra: "))
    list_vacia.append(palabra)
print(list_vacia)

#Ejercicio 4
# Ya tengo una lista a la cual le reemplazare unos datos
# como ya tengo bastante claro la ubicacion de los datos 
# con indice de principio a fin lo estoy practicando
# con el indice negativo.
animales = ["perro","gato","conejo","pez"]
animales [-1] = "loro"
animales [-3] = "oso"
print(animales)

#Ejercicio 5
# Tenemos una lista con numeros, al mometo de usar la
# funcion max se busca el elemeto de mayor valor en la
# lista y con el remove se la quita de la misma
# por otro lado, al parecer si la lista tiene 
# mas de un elemento con el mismo valor, elimina
# el primero que encuentre y si no existen valores 
# dara un error.
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#Ejercicio 6
# Creamos una variable que contenga una lista generada
# con un range especificando el paso en (5), luego al
# momento de mostrar la lista limito los datos que se 
# mostraran con los dos puntos.
lista_5 = list(range(10,31,5))
print(lista_5[0:2])

#Ejercicio 7
# Para este caso especifico fue util el ciclo for ya que
# el contador (i) pasaba solo por 1 y 2 justo los 
# indices de la lista que necesitaba reemplazar 
# gracias a eso pude usarlo en el indicador del indice a 
# reemplazar por los elementos de la variable "valor"
# si fuera diferente el caso posiblemente deba aplicar 
# o modificar algunos parametros
autos = ["sedan", "polo", "suran", "gol"]
for i in range(1,3):
    valor = input("Ingrese un valor: ")
    autos [i] = (valor)
print(autos)

#Ejercicio 8
# Lista vacia, coloque los valores que su respectivo doble
# debian ser agregados a la lista a saber(5,10,15)
# multiplicados por dos y haciendo uso del append.
dobles= []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#Ejercicio 9
# Importante especificar indice de la lista ya despues con append
# se encuentra el valor a reemplazar, lo mismo ocurre con remove 
# la funcion detecta el valor que se removera, para reemplazar 
# fideos por tallarines le asigne a una variable el indice donde
# este la lista anidada e index para ubicar la palabra. 
# 
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
valor_fideos = compras[1].index("fideos")
compras[1][valor_fideos] = "tallarines"
compras[0].remove("pan")
print(compras)

#Ejercicio 10
# Muy importante tener en cuenta los indices de las listas.
lista_anidada = [[15],[True],[25.5, 57.9, 30.6],[False]]
print(lista_anidada)



