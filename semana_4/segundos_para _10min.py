def resta(diez_minutos, segundos):
    return diez_minutos - segundos
print("Ingrese el tiempo en segundos: ")
segundos = int(input())
diez_minutos = 600 
sobrante = diez_minutos - int(input)

if segundos < diez_minutos:
    print(f("Faltan ({sobrante}) ,segundos para 10 minutos"))
elif segundos > diez_minutos:
    print(("Mayor"))
else:
    print("Correcto")



