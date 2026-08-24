def ordenar_canciones(archivo_entrada, archivo_salida):
    canciones = []

    with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            canciones.append(linea.strip())

    canciones.sort()

    with open(archivo_salida, 'w', encoding='utf-8') as archivo:
        for cancion in canciones:
            archivo.write(cancion + '\n')

    print("✅ Canciones ordenadas guardadas correctamente.")


ordenar_canciones(
    r"C:\Users\VillArrt\Desktop\Lyfter\semana_8\\bob_songs.txt",             
    r"C:\Users\VillArrt\Desktop\Lyfter\semana_8\\bob_songs_ordenadas.txt"    
)
