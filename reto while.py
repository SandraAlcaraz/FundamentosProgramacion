#reto 1 while
def Funcion(num, lim):
    cuen=0
    cuantos=lim
    while cuantos>0:
        if cuantos%num==0:
            print("El nímero %d, es divisible entre %d"%(cuantos,num))
            cuen+=1
        cuantos-=1
    print(
        
