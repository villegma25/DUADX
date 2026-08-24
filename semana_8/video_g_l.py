n = int(input("¿Cuántos videojuegos quieres ingresar? "))

videojuegos = []

for i in range(n):
    print(f"\nVideojuego #{i+1}")
    nombre = input("Nombre: ")
    genero = input("Género: ")
    desarrollador = input("Desarrollador: ")
    clasificacion = input("Clasificación ESRB: ")
    
    videojuego = [nombre, genero, desarrollador, clasificacion]
    
    videojuegos.append(videojuego)

with open("videojuegos.csv", "w", encoding="utf-8") as archivo:
    archivo.write("nombre,genero,desarrollador,clasificacion\n")
    
    for v in videojuegos:
        linea = ",".join(v) + "\n"
        archivo.write(linea)

print("\nArchivo 'videojuegos.csv' guardado correctamente.")
