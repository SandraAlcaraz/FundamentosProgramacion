#quiz3‐1.py
#Problema 1
def CalcularIVA (m,i):
   x=i/100
   cal=m*x
   return cal
monto=float(input("Dame el monto "))
inte=float(input("Dame el interés "))
cal=CalcularIVA(monto,inte)

print ("El monto prestado es: $",monto)
print ("El interés a cobrar es $%0.2f   " %(cal))
print("El total es: $%0.2f" %(cal+monto))


    
    
