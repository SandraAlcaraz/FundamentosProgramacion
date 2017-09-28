#Problema 2
#quiz 2
#Sandra Alcaraz
n=int(input("Ingrese un número"))
val=True
def Func(n):
    for y in range(n,0,-1):
        if n%y==0:
            val=False
            print(y," es primo")
        
        else:
            val=True
            print(y,"No es primo")
    return val
x=Func(n)
            
