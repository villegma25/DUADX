def open_and_print_file_per_line(path):
    with open(path) as file:
        for line in file.readlines():
            print(f'Linea: {line.strip()}')

open_and_print_file_per_line(r"C:\Users\VillArrt\Desktop\Lyfter\semana_8\\bob_songs.txt")

def list_ord_bobs(path):
    bob_songs = []
    with open(path) as file:
        for line in file:
            bob_songs.append(line.strip())

    bob_songs.sort()

    print("\n Canciones ordenadas:")
    for song in bob_songs:
        print(song)

list_ord_bobs(r"C:\Users\VillArrt\Desktop\Lyfter\semana_8\\bob_songs.txt")



#este el el path de la carpeta de songs    C:\Users\VillArrt\Desktop\Lyfter 
