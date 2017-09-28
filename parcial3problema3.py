def Factorial (x):
        v=x
        m=1
        if x==0:
            return 1
        while v>1:
            m=v*m
            v=v-1
        return m

tr=True
while tr==True:
    x=int(input("Dame el valor de x"))
    v=0
    f=0
    r=0
    while f<101:
        v=v+1
        y=Factorial(f)
        w=(x**f)/y
        r=w+r
        f=f+1
    print (r)
    y=str(input("Deseas calcular otro exponente x S/N"))
    if y=="s" or y=="S":
        tr=True
    else:
        tr=False
        
    

