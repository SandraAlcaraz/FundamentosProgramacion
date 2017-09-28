print("Compruebe si la frase es un palimdroma")
x=str(input("Ingrese la frase"))

j=""
for k in x:
    i=ord(k)
    if i==32:
        i=""
    else:
        i=chr(i)
    j=j+i
for i in j:
    p=ord(i)
    if p>=65 and p<=90:
        p=chr(p+32)
    else:
        j=j+i
print(x,end=" ")
    
    

y=x[::-1]       
if x==y:
    print("Es un palindroma")
else:
    print("No lo es")
