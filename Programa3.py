#Programa 3
#Sandra Alcaraz Amezcua
#A01631701
x=int(input("Ingrese el número de calificaciones que va a promediar"))
def Promedio (x):
    y=0
    for nu in range (x):
        m=x
        w=int(input("Ingrese la calificación"))
        if w>100 or w<0:
            w=0
            y=w+y
            m=m-1
        else:
            y=w+y
    u=y/x
    return u    

pro=Promedio(x)
print("El promedio de las %d calificaciones capturadas es %0.2f" %(x,pro))
