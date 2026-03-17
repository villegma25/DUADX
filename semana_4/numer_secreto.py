import random
sec_num = random.randint(1,10)
intentos = 0
print("Adivine un numero del 1 al 10: ")

while True:
    guess = int(input(" Numero: "))
    intentos += 1
    if guess < sec_num:
        print("El numero del 1 al 10 es % s" % (sec_num))
    elif guess > sec_num:
        print("El numero del 1 al 10 es % s" % (sec_num))
        intentos += 1
    else:  
        print("Correcto!")

    break

#5
#while input("Quieres vover a jugar? (Si/No)") == 'Si':


print("Gracias por jugar!")
    

   





    




















 





 