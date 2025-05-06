#Actividad N° 7

num = input("Ingrese un numero entero mayor a 0 : ")
num = int(num)
print("El numero ingresado es: ", num)

num_2 = input("Ingrese otro numero entero mayor a 0 : ")
num_2 = int(num_2)
print("El numero ingresado es: ", num_2)

SUMA = print("La suma de ambos es: ", num + num_2)

RESTA = print("La resta de ambos es: ", num - num_2)

MULTIPLICACION = print("Su producto ambos es: ", num * num_2)

if num_2 != 0:
    DIVISIÓN = num // num_2
    print("La division ambos es: ", DIVISIÓN)


