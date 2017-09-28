#Actividad 1
#Arreglos
#Sandra Guadalupe Alcaraz Amezcua
def Captura(x):
    
    if x<=0:
        print("Debe de capturar un número mayor a 0")
        lista=[0]*0
        return lista
    else:
        lista=[0]*x
        p=0
        while p<x:
            lista[p]=input("Capture el nombre")
            p=p+1
        w=Muestra(lista)
        return lista

def Muestra (x):
    f=len(x)
    y=0
    while y<f:
        print(x[y])
        y=y+1

def main ():
        v=True
        while (v):
                r=input("Captture la cantidad de personas")
                if (r.isdigit()):
                    r=int(r)
                    u=Captura(r)
                    a=input("Desea volver a capturar s/n")
                    if a=="s" or a=="S":
                        v=True
                    else:
                        v=False
                    
                else:
                    print("Error")
main()
