#Programa 1 Tarea
#Sandra Alcaraz Amezcua

def Tabla (x):
    for c in range(1,11):
        h=c*x
        print(c,"*",x,"=",h)



x=int(input("Capture un número entre 0 y 100"))
if x<0 or x>100:
    print("Usted no capturó un número entre 0 y 100")
else:
    o=Tabla(x)
