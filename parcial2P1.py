#Sandra Gpe Alcaraz Amezcua
#A01631701
def Calcula(a,b):
    for i in range(a,b+1):
        y=5*(i)**2+(3*i)+8
        print("Para el valor de x= %d y es igual a %d" %(i,y))
a=int(input("Dame el valor del rango inicial"))
b=int(input("Dame el valor del rango final"))
x=Calcula(a,b)
