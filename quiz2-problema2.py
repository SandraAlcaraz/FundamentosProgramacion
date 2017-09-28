#Problema 2 Quiz 2
#Sandra Alcaraz
n=int(input("Ingrese un número"))
def Prim(n):
    primo=True
    for nu in range(1,n):
        if n%nu==0:
            primo=False
            continue
        else:
            if primo==True:
                print(n,"es primo")
            else:
                print(n,"No es primo")
    return n
d=Prim(n)
            
