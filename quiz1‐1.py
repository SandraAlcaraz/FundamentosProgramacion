#Problema 1 Sandra Alcaraz
def Promedio(c1,c2,c3):
    prom=(c1+c2+c3)/3
    return prom
def LaNota(w):
    if w<70:
        nota="Nota Baja"
    elif w<80:
        nota="Nota Mejorable"
    elif w<90:
        nota="Nota Buena"
    elif w<100:
        nota="Nota Aceptable"
    else:
        nota="Nota sobresaliente"
    return nota
def Captura():
    v=str(input("Ingrese el nombre:"))
    if v=="":
        print("Error, no se ingresaron datos")
    else:
        c1=int(input("Ingrese la primer calificación:"))
        c2=int(input("Ingrese la segunda calificación:"))
        c3=int(input("Ingrese la tercera calificación:"))
        if c1<0 or c1>100:
            c1=0
        if c2<0 or c2>100:
            c2=0
        if c3<0 or c3>100:
            c3=0
        x=Promedio(c1,c2,c3)
        nota=LaNota(x)
    return v, c1,c2,c3,x,nota
nombre,calificacion1, calificacion2, calificacion3,prom,nota=Captura()
print("Nombre:", nombre)
print("Primer calificación:", calificacion1)
print("Segunda calificación:", calificacion2)
print("Tercera calificación:", calificacion3)
print("El promedio es:", prom)
print(nota)

           
