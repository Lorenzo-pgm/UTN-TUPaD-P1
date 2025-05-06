#Actividad N° 8

mts = input("Ingrese su altura: ")
mts = float(mts)
kg = input("Ingrese su peso: ")
kg = int(kg)

IMC = kg // mts**2
IMC = int(IMC)
print(f"Su IMC equivale a: {IMC}")
