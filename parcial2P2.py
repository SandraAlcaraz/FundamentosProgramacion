#A01631701
#Sandra Gpe. Alcaraz Amezcua
def Factorial (x):
    v=x
    m=1
    while v>0:
        m=v*m
        v=v-1
    return m

n=int(input("Dame el número para calcular su factorial"))
s=Factorial(n)
print("El factorial de %d es %d" %(n,s))
