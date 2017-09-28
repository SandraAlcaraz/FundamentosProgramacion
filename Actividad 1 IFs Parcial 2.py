#capturar calificaciones dentro del rango

def CalcularProm(c1,c2,c3):
    if c1<0 or c1>100:
       c1=0
    if c2<0 or c2>100:
       c2=0
    if c3<0 or c3>100:
       c3=0
    prom=(c1+c2+c3)/3.0
    return prom
print("Ingrese 3 calificaciones entre 0 y 100")
p1=int(input("Ingrese la primera calificación"))
p2=int(input("Ingrese la segunda calificación"))
p3=int(input("Ingrese latercera calificación"))

prom=CalcularProm(p1,p2,p3)
print("Tu promedio es %0.2f"%prom)
if prom>95:
    print("Muchas felicidades por tu desempeño")
