#Quiz 2 Sandra Alcaraz
#Problema1
x=int(input("Ingresa el número"))
po=int(input("El número se elevará a la potencia"))
h=1
def Pote(x,po,h):
    for y in range(po+1):
        if y!=0:
            h=h*x
    return h
Pot=Pote(x,po,h)
print(Pot)
