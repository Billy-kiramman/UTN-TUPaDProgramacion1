#Ejercicio 1
numeros: int = 0
while numeros <= 100:
    print(numeros)
    numeros = numeros + 1

#Ejercicio 2
numero:int = int(input("Ingrese un numero entero"))
cont = 0
while numero != 0:
    numero = abs(numero//10)
    cont += 1
print("El numero ingresado contiene", cont, "digitos.")

#Ejercicio 3
n1:int = int(input("Ingrese un numero entero"))
n2:int = int(input("Ingrese un numero entero"))
if n1 < n2:
    sum = 0
    for i in range(n1+1,n2):
        sum = sum + i
elif n1 > n2:
    sum = 0
    for i in range(n2+1,n1):
        sum = sum + i
else:
    print("Los valores ingresados no son correctos")
print("El resultado de la sumatoria es ", sum)

#Ejercicio 4
sumatoria = 0
bandera = True
while bandera == True:
    num: int = int(input("Ingrese un numero entero"))
    sumatoria = sumatoria + num
    if num == 0:
        bandera = False
print("La sumatoria de los numeros es ", sumatoria)

#Ejercicio 5
import random
numero_de_juego = random.randint(0,9)
bandera = True
intentos: int = 0
numero_usuario = 0
while bandera == True:
    numero_usuario:int = int(input("Ingrese un numero"))
    intentos = intentos + 1
    if numero_usuario == numero_de_juego: 
        print(F"Correcto, El numero es {numero_usuario} en {intentos} intentos")
        bandera = False
    else: 
        print("El numero ingresado es incorrecto, intente nuevamente")

#Ejercicio 6
for i in range(100,-1,-1):
    if i % 2 == 0:
        print(i)
    else:
        continue

#Ejercicio 7
sumatorio: int = 0
numero_positivo:int = int(input(print("Ingrese un numero entero positivo")))
if numero_positivo > 0:
    for i in range(0,numero_positivo+1):
        sumatorio = sumatorio + i
else:
    print("El numero ingresado es invalido")
print(sumatorio)

#Ejercicio 8
positivo:int = 0
negativo:int = 0
par:int = 0
inpar: int = 0
cont: int = 0
num:int = 0
while cont < 100:
    num:int = int(input(print("Ingrese un numero entero")))
    if num > 0:
        positivo = positivo + 1
    elif num < 0:
        negativo = negativo + 1
    if num % 2 == 0:
        par = par + 1
    elif num % 2 != 0:
        inpar = inpar + 1
    else:
        print("El valor ingresado es incorrecto")
    cont = cont + 1
print("Ingreso ", positivo, " numeros positivos")
print("Ingreso ", negativo, " numeros negativo")
print("Ingreso ", par, " numeros par")
print("Ingreso ", inpar, " numeros inpar")

#Ejercicio 9
valor_tope: int = 100
contador:int = 0
numeros:int = 0
suma_valores:int = 0
while contador < valor_tope:
    numeros:int = int(input(print("Ingrese un valor numerico")))
    contador = contador + 1
    suma_valores = suma_valores + numeros
print("La media de los valores ingresados es ", suma_valores / valor_tope)

#Ejercicio 10
nume:int = int(input("Ingrese un numero"))
if nume < 0:
    nume_negativo = True
    nume = nume * -1
else:
    nume_negativo = False
inverso = 0
while nume > 0:
    ulti = nume % 10
    inverso = inverso * 10 + ulti
    nume = nume // 10
if nume_negativo == True:
    inverso = inverso * -1
print("El numero inverso es ", inverso)


















