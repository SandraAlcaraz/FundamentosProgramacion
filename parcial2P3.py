#A01631701
#Sandra Gpe. Alcaraz Amezcua
tr=True
while tr==True:
    x=int(input("Dame el valor de x"))
    m=0
    c=1
    v=0
    r=0
    while m<101:
        while v>0:
            c=v*c
            v=v-1
        v=v+1
        w=x**m/c
        r=w+r
        m=m+1
        c=1
    print(r)
    y=str(input("Deseas calcular otro exponente x S/N"))
    if y=="s" or y=="S":
        tr=True
    else:
        tr=False
        
    

