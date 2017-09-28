#Actividad 5 Adivina número
#Sandra Alcaraz Amezcua
#A01631701
import random
num=int(input("Dame el límite"))
number=int(num*random.random())+1

x=num+1
h=0
while x!=number:
    x=int(input("Adivina el número"))
    if x<number:
        print("El número es menor que el que se generó")
        h=h+1
        continue
    elif x>number:
        print("El número es mayor al que se generó")
        h=h+1
        continue
    else:
        if h<5:
            print("Felicidades encontraste el número")
        elif h<10:
            print("Lo encontraste, pero puedes hacerlo mejor")
        else:
            print("Lo encontraste, pero debes de mejorar tu estrategia para adivinar")
            
        
    
