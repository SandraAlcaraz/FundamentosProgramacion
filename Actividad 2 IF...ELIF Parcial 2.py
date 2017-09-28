#Calficaciones dentro del rango con asignación
print("Ingrese 3 calificaciones entre 0 y 100")
c1=int(input("Ingrese la primera calificación"))
c2=int(input("Ingrese la segunda calificación"))
c3=int(input("Ingrese latercera calificación"))
if c1<0 or c2<0 or c3<0 or c1>100 or c2>100 or c3>100:
    print("Error de rango")
else:
    prom=(c1+c2+c3)/3.0
    print("Tu promedio es %0.2f"%prom)
    if prom>-1 and prom<21:
        print("F")
    elif prom<31:
         print("E")
    elif prom<41:
        print("D")
    elif prom<51:
        print("C-")
    elif prom<61:
        print("C")
    elif prom<71:
        print("C+")
    elif prom<76:
        print(" B-")
    elif prom<81:
        print("B")
    elif prom<86:
        print("B+")
    elif prom<91:
        print("A-")
    elif prom<96:
        print("A")
    else:
        print("A+")
                            
                            
        
