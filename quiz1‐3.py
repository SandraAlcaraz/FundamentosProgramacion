#Programa 3 Sandra Alcaraz

def CalculaM (x):
    if x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12:
        v=31
    elif x==2:
        v=28
    else:
        v=30
    return v

y=int(input("Capture el número del mes"))
if y<1 or y>12:
    print("El número de mes no está en el rango no se puede ejecutar")
else:
    resul=CalculaM(y)
    print("Los días de este mes son %i" %(resul))
    
