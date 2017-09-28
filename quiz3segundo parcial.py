#Problema
#Sandra Guadalupe Alcaraz Amezcua
def Valinput (m,inte,am):
    while m<0:
        print("Por favor capture números mayores a 0")
        m=int(input("Capture el monto que se prestó"))
    while inte<0:
        print("Por favor capture números mayores a 0")
        inte=int(input("Ingrese el interés en porcentaje"))
    while am<0:
        print("Por favor capture números mayores a 0")
        am=int(input("Ingrese el abono mensual"))    

m=int(input("Ingrese el monto que se prestó"))
inte=int(input("Ingrese el interés en porcentaje"))
am=int(input("Ingrese el abono mensual"))
x=Valinput(m,inte,am)
mo=m
mes=0
i=inte/2
c=0
while mo>0:
    y=mo*inte*.01
    c=c+y
    arc=am-y
    mes=mes+1
    print("%d   %0.2f   %0.2f   %0.2f   %0.2f  %0.2f" %(mes,mo,y,inte,am,arc))
    input("")
    mo=mo-arc
    if mo<am:
        am=mo+(y/2)
    if mo<=m/2:
        inte=i
        continue
d=m+c
print("Totales:   %0.2f       %0.2f    " %(c,d))   

