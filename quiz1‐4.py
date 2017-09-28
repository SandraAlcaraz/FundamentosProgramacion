#Problema 4 Sandra Alcaraz
x=int(input("Ingrese el año"))
if x%4==0 and x%100!=0 or x%400==0:
    print("Es año bisiesto")
else:
    print("No es año bisiesto")
