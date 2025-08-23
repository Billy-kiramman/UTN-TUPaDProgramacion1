
#Ejercicio 1
print("Hola mundo")

#Ejercicio 2
nombre: str = input("Por favor ingrese su nombre: ")
print(f"Hola {nombre}")

#Ejercicio 3
nombre: str = input("Ingrese su nombre: ")
apellido: str = input("Ingrese su apellido: ")
edad: str = input("Ingrese su edad: ")
residencia: str = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio 4
radio: float = float(input("Ingrese el radio de un circulo: "))
area = 3.14 * radio ** 2
perimetro = 2*3.14*radio
print("El area del circulo es de ", area)
print("El perimetro del circulo es de ", perimetro)

#Ejercicio 5
segundos: int = int(input("Ingrese una cantidad de tiempo expresada en segundo: "))
horas = segundos / 3600
print("Los segundos ingresados son ", horas," horas")

#Ejercicio 6
numero: int = int(input("Ingrese un numero: "))
print("Su tabla de multiplicar es: ")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#Ejercicio 7
num1: int = int(input("Ingrese un numero distinto de 0: "))
num2: int = int(input("ingrese un numero distinto de 0: "))
print("Sus operaciones dar como resultado: ")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")

#Ejercicio 8
altura: float = float(input("Ingrese su altura: "))
peso: float = float(input("Ingrese su peso: "))
imc = peso / (altura ** 2)
print("Su indice de masa corporal es de: ", imc,"kg/m^2")

#Ejercicio 9
celsius: float = float(input("Ingrese un valor de temperatura en Celsius: "))
Fahrenheit = 9/5 * celsius + 32
print("La temperatura de celsius a fahrenheit es de: ", Fahrenheit)

#Ejercicio 10
print("Por favor ingrese 3 numeros")
numero1: int = int(input("primero: "))
numero2: int = int(input("segundo: "))
numero3: int = int(input("tercero: "))
promedio = (numero1 + numero2 + numero3) / 3
print("El promedio de los numeros ingresados es: ", promedio)