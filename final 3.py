#Sandra Gpe. ALcaraz Amezcua A01631701
#problema3
cadena1="Feria internacional del libro de Guadalajara 2015"
dic={}
def coca(x):
    lon=len(x)
    c=x
    u=0
    while u<lon:
        b=c[u]
        c.strip(b)
        v=x.count(b)
        b=str(b)
        v=str(v)
        g="Del caracter "+ b +" hubo "+v+" ocurrencias"
        dic[b]=g
        u=u+1
    
    print(dic)

x=coca(cadena1)
