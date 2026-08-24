# Cree una funcion que inprima el numero de mayuscules y minusculas en un string
st_name = 'I love Nation Sushi'


def low_low(st_name):
    counter_lower = 0
    for char in st_name:
        if char.islower():
            counter_lower += 1
    return counter_lower


def upup(st_name):
    counter_upper = 0
    for char in st_name:
        if char.isupper():
            counter_upper += 1
    return counter_upper


def main(st_name):
    counter_lower = low_low(st_name)
    counter_upper = upup(st_name)
    print(f"Esta es la cantidad de letras mayusculas: {counter_upper} y la cantidad de letras minusculas: {counter_lower}")


main(st_name)