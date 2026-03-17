# Cree un programa que elimine todos los numeros impares de una lista 
my_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
filtered_list = []

for num in my_list:
    if num % 2 == 0:
        filtered_list.append(num)

print(filtered_list)   