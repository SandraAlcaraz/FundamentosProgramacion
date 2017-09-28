#tarea2 parte3
#Sandra Guadalupe Alcaraz Amezcua A01631701
lista=[1,2,1,2,3,4,5,6,7,2,8]
def eliminaRepetidos (x):
    print (x)
    nl=x   
    di={}
    for c in range (len(nl)):
        di[nl[c]]=c
    v=di.keys()
    print(v)

c=eliminaRepetidos(lista)
