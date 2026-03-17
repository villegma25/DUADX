def convertir(num, valor):
    if valor == "1":
        return num*5/18
    else:
        return num*18/5    
def medida(valor):
    if valor == "1":
        return "m/s"
    else:
        return "km/h"
    

if __name__ == '__main__':
    num = float(input(("Ingrese el numero a convertir: ")))
valor = input("Inrese 1 para convertir a m/s /n*Ingrese 0 para convertir km/h n/*Elija un opcion: ")
print(f"La conversion es: " , str(convertir(num, valor)), " ", medida(valor))