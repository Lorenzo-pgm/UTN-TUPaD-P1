#Presentación del Código en Python.

# Simulador de Puertas Lógicas Básicas:

def obtener_valor_binario(mensaje): 
    while True: 
        valor = input(mensaje) 
        if valor in ('0', '1'): 
            return int(valor) 
        else: 
            print("Entrada inválida. Ingrese 0 o 1.") 

# Solicitar entradas 
a = obtener_valor_binario("Ingrese el primer valor (0 o 1): ") 
b = obtener_valor_binario("Ingrese el segundo valor (0 o 1): ") 

# Resultados Operaciones lógicas 
print("\nResultados:") 
print(f"AND: {a & b}") 
print(f"OR: {a | b}") 
print(f"NOT A: {int(not a)}") 
print(f"NOT B: {int(not b)}") 
print(f"NAND: {int(not (a & b))}") 
print(f"NOR: {int(not (a | b))}") 
print(f"XOR: {a ^ b}") 
