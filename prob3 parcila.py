lista1=[1,2,3,4,2,4,3,5]
lista2=[1,23,2,22,6,7,5,8]
def interseccion(x,y):
    con=0
    lista=[]
    while con<len(x):
        cont=1
        while cont<len(y):
            if x[con]==y[cont]:
                lista.append(x[con])
            cont=cont+1
        con=con+1
        print(lista)
    return(lista)
c=interseccion(lista1,lista2)
print(c)
