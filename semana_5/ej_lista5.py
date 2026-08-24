# Cree u programa que le pida al usurio 10 mumeros y que al final le de muestre todos los numeros que ingreso, seguido del numero mas alto
my_list = []
counter = 0

while counter < 10:
    num = int(input("Ingrese 10 numeros: "))
    my_list.append(num)
    counter += 1

print(" Numeros ingresados: ", my_list)
print("El numero mas alto fue: ", max(my_list))
