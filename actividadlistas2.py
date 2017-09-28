#A01631701 Sandra Alcaraz Amezcua
#Actividad
def evaluaLista (x,lista):
    nl=[]
    y=0
    f=len(lista)
    while y<f:
        if x==(lista[y]):
            nl.append(y)
        y=y+1    
    return nl
lista=[2,3,3,7,9,8,7,3,2,3,1,3,2,5,6,6,6,5,5,1,4,1,3,2]
c=int(input("Capure el número a encontrar en la lista"))
dato=lista.count(c)
if dato==0:
    print("Eldato no se encuentra en la lista")
else:
    f=len(lista)
    h=evaluaLista(c,lista)
    print(h)
        
