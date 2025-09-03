#Ejercicio 1
edad: int = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

#Ejercicio 2
nota: float = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3
number: int = int(input("Ingrese un numero: "))
if number % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

#Ejercicio 4
edad: int = int(input("Ingrese su edad: "))
if edad > 0 and edad < 12:
    print("Es un niño")
elif edad >= 12 and edad < 18:
    print("Es un adolescente")
elif edad >= 18 and edad < 30:
    print("Es un adulto joven")
elif edad >= 30 and edad < 90:
    print("Es un adulto")
else:
    print("El valor ingresado es invalido")

#Ejercicio 5
password: str = str(input("Ingrese un password: "))
if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado un password correcto")
else:
    print("Por favor, ingrese un password de entre 8 y 14 caracteres.")

#Ejercicio 6
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1, 100) for i in range (50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
print("Numeros aleatorios", numeros_aleatorios)
print(f"moda   : {moda}")
print(f"mediana : {mediana}")
print(f"media : {moda}")
if media > mediana > moda:
    print("Distrubucion con sesgo positivo")
elif media< mediana < moda:
    print("Distribucion con sesgo negativo")
elif media == mediana == moda:
    print("Distribucion sin sesgo")
else: 
    print("No se cumplen los criterios")

#Ejercicio 7
palabra_frase: str = input("Ingrese una frase o palabra: ")
minuscula = palabra_frase.lower()
ultima_letra = minuscula[-1]
if ultima_letra in "aeiouéáíóú":
    print(palabra_frase + "!")
else:
    print(palabra_frase)

#Ejercicio 8
nombre: str = input("Ingrese su nombre por favor:")
seleccion: str = str(input("Seleccione un opcion 1)mayusculas, 2)minusculas, 3)Primer letra Mayus"))
nombre_mayus = nombre.upper()
nombre_minus = nombre.lower()
first_letter = nombre.title()
if seleccion == "1":
    print(nombre_mayus)
elif seleccion == "2":
    print(nombre_minus)
elif seleccion == "3":
    print(first_letter)

#Ejercicio 9
magnitud: float = float(input("Ingrese una magnitud de terremoto"))
if magnitud > 0 and magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print ("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print ("Fuerte")
elif magnitud >=6 and magnitud < 7:
    print("Muy fuerte")
elif magnitud >= 7 and magnitud < 10:
    print ("Extremo")
else:
    print ("Los datos ingresados son incorrectos")

#Ejercicio 10
hemisferio: str = str(input("Ingrese el hemisferio donde se encuentra N: Norte, S: Sur"))
mes: int = int(input("Ingrese el mes (1 - 12)"))
dia: int = int(input("Ingrese el dia (1 - 31)"))
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Otoño")
    else:
        print("Los datos ingresados no concuerdad con lo solicitado")
if hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Primavera")
    else:
        print("Los datos ingresados no concuerdad con lo solicitado")







