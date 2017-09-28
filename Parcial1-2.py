#Problema 2
#Sandra Alcaraz
def trian(b,h):
    x=(b*h)/2
    return x
a=float(input("Dame la altura"))
b=float(input("Dame la base"))
area=trian(a,b)
print("Un triángulo con una base %0.2f y una altura de %0.2f su área es: %0.2f" %(a,b,area))
