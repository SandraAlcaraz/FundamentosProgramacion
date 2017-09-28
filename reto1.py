#Reto 1vwhile
#study hard :)
def Found (num, lim):
    c=0
    while lim>num :
        if lim%num==0:
            print("El número %d es divisible entre %d" %(lim,num))
            lim=lim-1
            c=c+1
            continue
        else:
            lim=lim-1
    return c

limite=int(input("Ingrese el límite"))
numero=int(input("Ingrese el número"))
c=Found(numero,limite)
print("El total de numeros divisibles entre %d son %d" %(numero,c))

        
