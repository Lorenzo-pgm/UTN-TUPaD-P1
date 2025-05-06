#En el siguiente código se pide al usuario que ingrese un número y se imprime por pantalla  "True" si el número ingresado está entre 10 y 20 y "False" si está por fuera del rango 10-20. Complete el código para que sea correcto:

rango_minimo = 10
rango_maximo = 20

numero_usuario = int(input("Ingrese un número: "))
dentro_rango = (rango_minimo <= numero_usuario <= rango_maximo)
print(dentro_rango)

