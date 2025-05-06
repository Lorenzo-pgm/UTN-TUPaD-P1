#-1
print("Hola Mundo! ")

#-2
nombre = input("Ingrese su nombre: ")
saludo = (f"Hola {nombre}")
print(saludo)

#-3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese lugar de residencia: ")
datos_personales = f"Soy {nombre} {apellido},tengo {edad} años y soy {lugar}. "
print(datos_personales)

#-4
radio = 1
pi = 3.14159

area = pi * radio ** 2
perimetro = 2 * pi * radio

input("Ingrese el valor del radio: ")

print("El área del circulo es: ", area)
print("El perimetro del circulo es: ", perimetro)

#-5
#Solicito al usuario la cantidad de segundos.
segundos = int(input("Ingese la cantidad de segundos: "))

#Calculamos a cuantas horas y minutos equivale
horas = int(segundos / 3600) 
minutos = int(segundos % 3600) // 60

print(f"{segundos} segundos equivale a {horas} horas y {minutos} minutos. ")

#-6
#Solicito al usuario Ingrese un numero. 
numero = int(input("Ingrese un numero y vera su correspondiente tabla: "))
#Se imprime por consola los resultados de la tabla elegida.
print(f"Tabla de multiplicar del {numero}:")
print(f"{numero} x 1 = {numero*1}")
print(f"{numero} x 2 = {numero*2}")
print(f"{numero} x 3 = {numero*3}")
print(f"{numero} x 4 = {numero*4}")
print(f"{numero} x 5 = {numero*5}")
print(f"{numero} x 6 = {numero*6}")
print(f"{numero} x 7 = {numero*7}")
print(f"{numero} x 8 = {numero*8}")
print(f"{numero} x 9 = {numero*9}")
print(f"{numero} x 10 = {numero*10}")

#-7
#Se solicita al usuario ingrese numero entero.
num = input("Ingrese un numero entero mayor a 0 : ")
num = int(num)
print("El numero ingresado es: ", num)
#Se solicita al usuario ingrese otro numero entero.
num_2 = input("Ingrese otro numero entero mayor a 0 : ")
num_2 = int(num_2)
print("El numero ingresado es: ", num_2)
#operaciones matematicas.
SUMA = print("La suma de ambos es: ", num + num_2)
RESTA = print("La resta de ambos es: ", num - num_2)
MULTIPLICACION = print("Su producto ambos es: ", num * num_2)
DIVISIÓN = print("La division ambos es: ", num // num_2)

#-8
#Calculadora de IMC
mts = input("Ingrese su altura: ")
mts = float(mts)
kg = input("Ingrese su peso: ")
kg = int(kg)

IMC = kg // mts**2
IMC = int(IMC)
print(f"Su IMC equivale a: {IMC}")

#-9
#Se calcula la temperatura de Celsius a Fahrenheit
celsius = input("Ingrese un valor en Celsius: ")
celsius = float(celsius)

fahrenheit = (celsius * 9//5 + 32)

print(f"La temperatura en grados fahrenheit es: {fahrenheit} °F")

#-10
#Se calcula el promedio de una materia.
x = float(input("Ingrese un numero: "))
y = float(input("Ingrese el 2do numero: "))
z = float(input("Ingrese el 3er numero: "))

promedio = (x + y + z) // 3
promedio = int(promedio)
print(f"Su promedio es: {promedio}")
