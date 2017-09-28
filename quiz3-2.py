#problema 2
def Convertidor(valor):
   octal=oct(valor)
   hexag=hex(valor)
   binari=bin(valor)
   return(octal,hexag,binari)

val=int(input("Dame el valor "))
octal, hexag, binari=Convertidor(val)
print("El número es %d , su valor en octal es %s , su valor en hexadecimal es %s y en binario es %s" %(val,octal,hexag,binari))
