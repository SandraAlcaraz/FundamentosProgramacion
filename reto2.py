#reto2
#Sandra Alcaraz Amezcua
#A01631701

def Prom (x):
    w=0
    m=0
    while w<x:
        ca=int(input("Ingrese la calificación de la materia"+str(w)+ " "))
        if ca<0 or ca>100:
            print("La calificación que debe ingresar debe estar entre 0 y 100")
            continue
        else:
            m=ca+m
            w=w+1
    m=m/x
    print(m)
n=int(input("Dame la cantidad de materias cursadas"))
c=Prom(n)
