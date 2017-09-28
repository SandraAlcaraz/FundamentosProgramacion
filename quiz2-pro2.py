n=int(input("Ingrese un número"))
def Func(n,):
    for y in range(n,0,-1):
        if y==2 or y%2!=0:
            print("Número ",y,"Es primo")
        elif y%2==0 or y%n==0:
                print("Número ",y,"No es primo")
                  
    
x=Func(n)
            
